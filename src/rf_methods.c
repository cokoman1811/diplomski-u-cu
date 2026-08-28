#include "rf_methods.h"

#include "ml_features.h"

#include <math.h>
#include <stdint.h>
#include <stdlib.h>

/*
 * Slucajna suma za imputaciju.
 *
 * Izmjene prema prvoj verziji:
 *   1. Iste gap-znacajke kao stablo (vrijednosti susjeda, ne samo vrijeme).
 *   2. Cilj je rezidual iznad linearne baze.
 *   3. Vise i dublja stabla (24 x dubina 10 umjesto 8 x dubina 4).
 *   4. Slucajan podskup znacajki po cvoru (max_features) — bez toga je
 *      rijec o obicnom baggingu, a ne o slucajnoj sumi.
 *   5. RF_MIN_LEAF se stvarno primjenjuje pri odabiru reza; prije je bila
 *      mrtva konstanta pa su listovi mogli imati jedan uzorak.
 */

#define RF_NUM_TREES    24
#define RF_MAX_DEPTH    10
#define RF_MIN_LEAF     4
#define RF_NUM_FEATURES ML_NUM_FEATURES
#define RF_MAX_FEATURES 7 /* od 11 — dovoljno za dekorelaciju, a zadrzava lin_base */

typedef struct RfNode {
    int is_leaf;
    double value;
    int feature;
    double threshold;
    struct RfNode *left;
    struct RfNode *right;
} RfNode;

typedef struct {
    double v;
    double y;
} RfPair;

static uint64_t rf_rng_state = 42ULL;

static uint64_t rf_rng_next(void) {
    uint64_t x = rf_rng_state;
    x ^= x << 13;
    x ^= x >> 7;
    x ^= x << 17;
    rf_rng_state = x;
    return x;
}

static size_t rf_rng_below(size_t bound) {
    if (bound == 0) {
        return 0;
    }
    return (size_t)(rf_rng_next() % (uint64_t)bound);
}

static int rf_cmp_pair(const void *a, const void *b) {
    double va = ((const RfPair *)a)->v;
    double vb = ((const RfPair *)b)->v;
    if (va < vb) {
        return -1;
    }
    return (va > vb) ? 1 : 0;
}

static double rf_feature(const double *F, size_t idx, int feature) {
    return F[idx * RF_NUM_FEATURES + feature];
}

static double rf_mean(const double *y, const size_t *idx, size_t count) {
    double sum = 0.0;
    size_t i;
    for (i = 0; i < count; i++) {
        sum += y[idx[i]];
    }
    return sum / (double)count;
}

static void rf_free(RfNode *node) {
    if (!node) {
        return;
    }
    rf_free(node->left);
    rf_free(node->right);
    free(node);
}

static RfNode *rf_leaf(double value) {
    RfNode *node = (RfNode *)calloc(1, sizeof(RfNode));
    if (node) {
        node->is_leaf = 1;
        node->value = value;
    }
    return node;
}

static int rf_best_split_for_feature(const double *F, const double *y,
                                     const size_t *idx, size_t count, int feature,
                                     RfPair *buf, double *best_sse, double *best_thr) {
    double total = 0.0, total_sq = 0.0;
    double sum_l = 0.0, sum_sq_l = 0.0;
    size_t i;
    int found = 0;

    for (i = 0; i < count; i++) {
        buf[i].v = rf_feature(F, idx[i], feature);
        buf[i].y = y[idx[i]];
    }
    qsort(buf, count, sizeof(RfPair), rf_cmp_pair);

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

        if (n_l < (size_t)RF_MIN_LEAF || n_r < (size_t)RF_MIN_LEAF) {
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

/* Fisher-Yates nad popisom znacajki; prvih RF_MAX_FEATURES je slucajan podskup. */
static void rf_sample_features(int *pool, int n_total, int n_pick) {
    int i;
    for (i = 0; i < n_pick; i++) {
        int j = i + (int)rf_rng_below((size_t)(n_total - i));
        int tmp = pool[i];
        pool[i] = pool[j];
        pool[j] = tmp;
    }
}

static RfNode *rf_build(const double *F, const double *y, const size_t *idx,
                        size_t count, int depth, RfPair *buf) {
    double best_sse = 0.0, best_thr = 0.0;
    int best_feature = -1;
    int pool[RF_NUM_FEATURES];
    int f, fi;
    size_t i, li = 0, ri = 0, n_left = 0;
    size_t *left_idx, *right_idx;
    RfNode *node;

    if (count == 0) {
        return NULL;
    }
    if (depth >= RF_MAX_DEPTH || count < (size_t)RF_MIN_LEAF * 2) {
        return rf_leaf(rf_mean(y, idx, count));
    }

    for (f = 0; f < RF_NUM_FEATURES; f++) {
        pool[f] = f;
    }
    rf_sample_features(pool, RF_NUM_FEATURES, RF_MAX_FEATURES);

    for (fi = 0; fi < RF_MAX_FEATURES; fi++) {
        double sse = 0.0, thr = 0.0;
        if (!rf_best_split_for_feature(F, y, idx, count, pool[fi], buf, &sse, &thr)) {
            continue;
        }
        if (best_feature < 0 || sse < best_sse) {
            best_feature = pool[fi];
            best_sse = sse;
            best_thr = thr;
        }
    }

    if (best_feature < 0) {
        return rf_leaf(rf_mean(y, idx, count));
    }

    for (i = 0; i < count; i++) {
        if (rf_feature(F, idx[i], best_feature) <= best_thr) {
            n_left++;
        }
    }
    if (n_left == 0 || n_left == count) {
        return rf_leaf(rf_mean(y, idx, count));
    }

    left_idx = (size_t *)malloc(n_left * sizeof(size_t));
    right_idx = (size_t *)malloc((count - n_left) * sizeof(size_t));
    if (!left_idx || !right_idx) {
        free(left_idx);
        free(right_idx);
        return rf_leaf(rf_mean(y, idx, count));
    }

    for (i = 0; i < count; i++) {
        if (rf_feature(F, idx[i], best_feature) <= best_thr) {
            left_idx[li++] = idx[i];
        } else {
            right_idx[ri++] = idx[i];
        }
    }

    node = (RfNode *)calloc(1, sizeof(RfNode));
    if (!node) {
        free(left_idx);
        free(right_idx);
        return rf_leaf(rf_mean(y, idx, count));
    }
    node->feature = best_feature;
    node->threshold = best_thr;
    node->left = rf_build(F, y, left_idx, li, depth + 1, buf);
    node->right = rf_build(F, y, right_idx, ri, depth + 1, buf);
    free(left_idx);
    free(right_idx);

    if (!node->left || !node->right) {
        double fallback = rf_mean(y, idx, count);
        rf_free(node->left);
        rf_free(node->right);
        free(node);
        return rf_leaf(fallback);
    }
    return node;
}

static double rf_predict(const RfNode *node, const double *F, size_t idx) {
    while (node && !node->is_leaf) {
        node = (rf_feature(F, idx, node->feature) <= node->threshold)
             ? node->left : node->right;
    }
    return node ? node->value : 0.0;
}

int rf_imputation(const Series *series, const double *temp, double *out) {
    size_t n = series->n;
    size_t known_count = 0, kc = 0, i;
    double lo, hi;
    double *F = NULL, *resid = NULL;
    size_t *known = NULL, *boot = NULL;
    RfPair *buf = NULL;
    RfNode *trees[RF_NUM_TREES];
    int t;

    for (t = 0; t < RF_NUM_TREES; t++) {
        trees[t] = NULL;
    }

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

    F = (double *)malloc(n * RF_NUM_FEATURES * sizeof(double));
    resid = (double *)malloc(n * sizeof(double));
    known = (size_t *)malloc(known_count * sizeof(size_t));
    boot = (size_t *)malloc(known_count * sizeof(size_t));
    buf = (RfPair *)malloc(known_count * sizeof(RfPair));
    if (!F || !resid || !known || !boot || !buf) {
        free(F);
        free(resid);
        free(known);
        free(boot);
        free(buf);
        return 1;
    }

    ml_features_build(series, temp, n, F);

    for (i = 0; i < n; i++) {
        resid[i] = isnan(temp[i]) ? NAN : temp[i] - F[i * RF_NUM_FEATURES + GAP_F_LIN_BASE];
        if (!isnan(temp[i])) {
            known[kc++] = i;
        }
    }

    rf_rng_state = 42ULL;
    for (t = 0; t < RF_NUM_TREES; t++) {
        for (i = 0; i < known_count; i++) {
            boot[i] = known[rf_rng_below(known_count)];
        }
        trees[t] = rf_build(F, resid, boot, known_count, 0, buf);
        if (!trees[t]) {
            int j;
            for (j = 0; j < t; j++) {
                rf_free(trees[j]);
            }
            free(F);
            free(resid);
            free(known);
            free(boot);
            free(buf);
            return 1;
        }
    }

    for (i = 0; i < n; i++) {
        double sum = 0.0, value;
        if (!isnan(temp[i])) {
            continue;
        }
        for (t = 0; t < RF_NUM_TREES; t++) {
            sum += rf_predict(trees[t], F, i);
        }
        value = F[i * RF_NUM_FEATURES + GAP_F_LIN_BASE] + sum / (double)RF_NUM_TREES;
        if (value < lo) {
            value = lo;
        }
        if (value > hi) {
            value = hi;
        }
        out[i] = value;
    }

    for (t = 0; t < RF_NUM_TREES; t++) {
        rf_free(trees[t]);
    }
    free(F);
    free(resid);
    free(known);
    free(boot);
    free(buf);
    ml_fill_remaining_gaps(out, n);
    return 0;
}
