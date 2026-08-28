#include "decision_tree.h"

#include "ml_features.h"

#include <math.h>
#include <stdlib.h>

/*
 * Regresijsko stablo (CART) za imputaciju.
 *
 * Kljucne razlike prema prvoj verziji:
 *
 *   1. Znacajke ukljucuju vrijednosti najblizih poznatih susjeda (gap-znacajke).
 *      Bez njih model uci preslikavanje vrijeme -> temperatura, sto je na signalu
 *      s lag-1 autokorelacijom 0,999 neusporedivo tezi problem od onoga koji
 *      rjesava interpolacija (susjedi -> temperatura).
 *
 *   2. Cilj ucenja je REZIDUAL iznad linearne baze, a ne sama temperatura.
 *      Stablo tako popravlja linearnu interpolaciju umjesto da je zamjenjuje;
 *      predikcija 0 znaci "linearna baza je vec dobra".
 *
 *   3. Matrica znacajki racuna se jednom, a najbolji rez trazi se sortiranjem
 *      i prefiksnim sumama umjesto kvadratnom pretragom s trigonometrijom.
 *      To je red velicine brze i tek time dublja stabla postaju izvediva.
 */

#define DT_MAX_DEPTH 8
#define DT_MIN_LEAF  4
#define DT_NUM_FEATURES ML_NUM_FEATURES

typedef struct DtNode {
    int is_leaf;
    double value;
    int feature;
    double threshold;
    struct DtNode *left;
    struct DtNode *right;
} DtNode;

typedef struct {
    double v; /* vrijednost znacajke */
    double y; /* ciljna vrijednost (rezidual) */
} DtPair;

static int dt_cmp_pair(const void *a, const void *b) {
    double va = ((const DtPair *)a)->v;
    double vb = ((const DtPair *)b)->v;
    if (va < vb) {
        return -1;
    }
    return (va > vb) ? 1 : 0;
}

static double dt_feature(const double *F, size_t idx, int feature) {
    return F[idx * DT_NUM_FEATURES + feature];
}

static double dt_mean(const double *y, const size_t *idx, size_t count) {
    double sum = 0.0;
    size_t i;
    for (i = 0; i < count; i++) {
        sum += y[idx[i]];
    }
    return sum / (double)count;
}

static void dt_free(DtNode *node) {
    if (!node) {
        return;
    }
    dt_free(node->left);
    dt_free(node->right);
    free(node);
}

static DtNode *dt_leaf(double value) {
    DtNode *node = (DtNode *)calloc(1, sizeof(DtNode));
    if (node) {
        node->is_leaf = 1;
        node->value = value;
    }
    return node;
}

/*
 * Najbolji rez po jednoj znacajci: sortiraj po vrijednosti znacajke, zatim
 * jednim prolazom kroz prefiksne sume evaluiraj sve pragove.
 * SSE grane = sum(y^2) - sum(y)^2 / count.
 */
static int dt_best_split_for_feature(const double *F, const double *y,
                                     const size_t *idx, size_t count, int feature,
                                     DtPair *buf, double *best_sse, double *best_thr) {
    double total = 0.0, total_sq = 0.0;
    double sum_l = 0.0, sum_sq_l = 0.0;
    size_t i;
    int found = 0;

    for (i = 0; i < count; i++) {
        buf[i].v = dt_feature(F, idx[i], feature);
        buf[i].y = y[idx[i]];
    }
    qsort(buf, count, sizeof(DtPair), dt_cmp_pair);

    for (i = 0; i < count; i++) {
        total += buf[i].y;
        total_sq += buf[i].y * buf[i].y;
    }

    for (i = 0; i + 1 < count; i++) {
        size_t n_l = i + 1;
        size_t n_r = count - n_l;
        double sse;

        sum_l += buf[i].y;
        sum_sq_l += buf[i].y * buf[i].y;

        if (n_l < (size_t)DT_MIN_LEAF || n_r < (size_t)DT_MIN_LEAF) {
            continue;
        }
        if (buf[i].v == buf[i + 1].v) {
            continue;
        }

        sse = (sum_sq_l - sum_l * sum_l / (double)n_l)
            + ((total_sq - sum_sq_l) - (total - sum_l) * (total - sum_l) / (double)n_r);

        if (!found || sse < *best_sse) {
            found = 1;
            *best_sse = sse;
            *best_thr = 0.5 * (buf[i].v + buf[i + 1].v);
        }
    }
    return found;
}

static DtNode *dt_build(const double *F, const double *y, const size_t *idx,
                        size_t count, int depth, DtPair *buf,
                        const int *feature_subset, int n_subset) {
    double best_sse = 0.0, best_thr = 0.0;
    int best_feature = -1;
    int fi;
    size_t i, li = 0, ri = 0, n_left = 0;
    size_t *left_idx, *right_idx;
    DtNode *node;

    if (count == 0) {
        return NULL;
    }
    if (depth >= DT_MAX_DEPTH || count < (size_t)DT_MIN_LEAF * 2) {
        return dt_leaf(dt_mean(y, idx, count));
    }

    for (fi = 0; fi < n_subset; fi++) {
        int f = feature_subset[fi];
        double sse = 0.0, thr = 0.0;
        if (!dt_best_split_for_feature(F, y, idx, count, f, buf, &sse, &thr)) {
            continue;
        }
        if (best_feature < 0 || sse < best_sse) {
            best_feature = f;
            best_sse = sse;
            best_thr = thr;
        }
    }

    if (best_feature < 0) {
        return dt_leaf(dt_mean(y, idx, count));
    }

    for (i = 0; i < count; i++) {
        if (dt_feature(F, idx[i], best_feature) <= best_thr) {
            n_left++;
        }
    }
    if (n_left == 0 || n_left == count) {
        return dt_leaf(dt_mean(y, idx, count));
    }

    left_idx = (size_t *)malloc(n_left * sizeof(size_t));
    right_idx = (size_t *)malloc((count - n_left) * sizeof(size_t));
    if (!left_idx || !right_idx) {
        free(left_idx);
        free(right_idx);
        return dt_leaf(dt_mean(y, idx, count));
    }

    for (i = 0; i < count; i++) {
        if (dt_feature(F, idx[i], best_feature) <= best_thr) {
            left_idx[li++] = idx[i];
        } else {
            right_idx[ri++] = idx[i];
        }
    }

    node = (DtNode *)calloc(1, sizeof(DtNode));
    if (!node) {
        free(left_idx);
        free(right_idx);
        return dt_leaf(dt_mean(y, idx, count));
    }
    node->feature = best_feature;
    node->threshold = best_thr;
    node->left = dt_build(F, y, left_idx, li, depth + 1, buf, feature_subset, n_subset);
    node->right = dt_build(F, y, right_idx, ri, depth + 1, buf, feature_subset, n_subset);
    free(left_idx);
    free(right_idx);

    if (!node->left || !node->right) {
        double fallback = dt_mean(y, idx, count);
        dt_free(node->left);
        dt_free(node->right);
        free(node);
        return dt_leaf(fallback);
    }
    return node;
}

static double dt_predict(const DtNode *node, const double *F, size_t idx) {
    while (node && !node->is_leaf) {
        node = (dt_feature(F, idx, node->feature) <= node->threshold)
             ? node->left : node->right;
    }
    return node ? node->value : 0.0;
}

int decision_tree_imputation(const Series *series, const double *temp, double *out) {
    size_t n = series->n;
    size_t known_count = 0, kc = 0, i;
    double lo = INFINITY, hi = -INFINITY;
    double *F = NULL, *resid = NULL;
    size_t *known = NULL;
    DtPair *buf = NULL;
    DtNode *tree = NULL;
    int all_features[DT_NUM_FEATURES];
    int f;

    for (i = 0; i < n; i++) {
        out[i] = temp[i];
        if (!isnan(temp[i])) {
            known_count++;
        }
    }
    if (known_count == 0) {
        return 1;
    }
    ml_known_range(temp, n, &lo, &hi);

    F = (double *)malloc(n * DT_NUM_FEATURES * sizeof(double));
    resid = (double *)malloc(n * sizeof(double));
    known = (size_t *)malloc(known_count * sizeof(size_t));
    buf = (DtPair *)malloc(known_count * sizeof(DtPair));
    if (!F || !resid || !known || !buf) {
        free(F);
        free(resid);
        free(known);
        free(buf);
        return 1;
    }

    ml_features_build(series, temp, n, F);

    for (i = 0; i < n; i++) {
        resid[i] = isnan(temp[i]) ? NAN : temp[i] - F[i * DT_NUM_FEATURES + GAP_F_LIN_BASE];
        if (!isnan(temp[i])) {
            known[kc++] = i;
        }
    }
    for (f = 0; f < DT_NUM_FEATURES; f++) {
        all_features[f] = f;
    }

    tree = dt_build(F, resid, known, known_count, 0, buf, all_features, DT_NUM_FEATURES);
    free(known);
    free(buf);
    if (!tree) {
        free(F);
        free(resid);
        return 1;
    }

    for (i = 0; i < n; i++) {
        double value;
        if (!isnan(temp[i])) {
            continue;
        }
        value = F[i * DT_NUM_FEATURES + GAP_F_LIN_BASE] + dt_predict(tree, F, i);
        /* Predikcija se drzi unutar raspona opazenih temperatura — sprjecava
           ekstrapolacijski overshoot na dugim prazninama. */
        if (value < lo) {
            value = lo;
        }
        if (value > hi) {
            value = hi;
        }
        out[i] = value;
    }

    dt_free(tree);
    free(F);
    free(resid);
    ml_fill_remaining_gaps(out, n);
    return 0;
}
