#include "decision_tree.h"

#include <math.h>
#include <stdlib.h>

#define DT_MAX_DEPTH    5
#define DT_MIN_LEAF     3
#define DT_NUM_FEATURES 5

static const double TWO_PI = 2.0 * 3.14159265358979323846;

typedef struct DtNode {
    int is_leaf;
    double value;
    int feature;
    double threshold;
    struct DtNode *left;
    struct DtNode *right;
} DtNode;

/*
 * Znacajke (5) — ista logika kao knn_upgraded za usporedivost ML metoda:
 *   [0] position_norm
 *   [1] hour_sin, [2] hour_cos
 *   [3] yday_sin, [4] yday_cos
 */
static void dt_features(const Series *s, size_t idx, size_t n, double out[5]) {
    double denom = (n > 1) ? (double)(n - 1) : 1.0;
    out[0] = (double)idx / denom;

    double hour_angle = TWO_PI * (double)s->hour[idx] / 24.0;
    out[1] = sin(hour_angle);
    out[2] = cos(hour_angle);

    double yday_angle = TWO_PI * (double)(s->yday[idx] - 1) / 365.0;
    out[3] = sin(yday_angle);
    out[4] = cos(yday_angle);
}

static double feature_value(const Series *s, size_t idx, size_t n, int feature) {
    double feats[5];
    dt_features(s, idx, n, feats);
    return feats[feature];
}

static double mean_temp(const double *temp, const size_t *idx, size_t count) {
    double sum = 0.0;
    for (size_t i = 0; i < count; i++) {
        sum += temp[idx[i]];
    }
    return sum / (double)count;
}

static void free_tree(DtNode *node) {
    if (!node) {
        return;
    }
    free_tree(node->left);
    free_tree(node->right);
    free(node);
}

static DtNode *make_leaf(double value) {
    DtNode *node = (DtNode *)calloc(1, sizeof(DtNode));
    if (!node) {
        return NULL;
    }
    node->is_leaf = 1;
    node->value = value;
    return node;
}

/* Suma kvadratnih pogresaka nakon podjele: feature <= threshold ide lijevo. */
static double split_mse(const double *temp, const size_t *idx, size_t count,
                        int feature, double threshold, const Series *s, size_t n,
                        size_t *left_count, size_t *right_count) {
    double sum_l = 0.0, sum_r = 0.0;
    size_t n_l = 0, n_r = 0;

    for (size_t i = 0; i < count; i++) {
        double y = temp[idx[i]];
        if (feature_value(s, idx[i], n, feature) <= threshold) {
            sum_l += y;
            n_l++;
        } else {
            sum_r += y;
            n_r++;
        }
    }

    *left_count = n_l;
    *right_count = n_r;
    if (n_l < (size_t)DT_MIN_LEAF || n_r < (size_t)DT_MIN_LEAF) {
        return INFINITY;
    }

    double mean_l = sum_l / (double)n_l;
    double mean_r = sum_r / (double)n_r;
    double mse = 0.0;

    for (size_t i = 0; i < count; i++) {
        double y = temp[idx[i]];
        double m = (feature_value(s, idx[i], n, feature) <= threshold) ? mean_l : mean_r;
        double d = y - m;
        mse += d * d;
    }
    return mse;
}

static DtNode *build_tree(const Series *s, const double *temp,
                          const size_t *idx, size_t count, size_t n, int depth) {
    if (count == 0) {
        return NULL;
    }

    if (depth >= DT_MAX_DEPTH || count < (size_t)DT_MIN_LEAF * 2) {
        return make_leaf(mean_temp(temp, idx, count));
    }

    double best_mse = INFINITY;
    int best_feature = 0;
    double best_threshold = 0.0;
    size_t best_l = 0, best_r = 0;

    for (int f = 0; f < DT_NUM_FEATURES; f++) {
        for (size_t i = 0; i < count; i++) {
            double thr = feature_value(s, idx[i], n, f);
            size_t n_l = 0, n_r = 0;
            double mse = split_mse(temp, idx, count, f, thr, s, n, &n_l, &n_r);
            if (mse < best_mse) {
                best_mse = mse;
                best_feature = f;
                best_threshold = thr;
                best_l = n_l;
                best_r = n_r;
            }
        }
    }

    if (best_mse == INFINITY || best_l == 0 || best_r == 0) {
        return make_leaf(mean_temp(temp, idx, count));
    }

    DtNode *node = (DtNode *)calloc(1, sizeof(DtNode));
    if (!node) {
        return NULL;
    }
    node->feature = best_feature;
    node->threshold = best_threshold;

    size_t *left_idx = (size_t *)malloc(best_l * sizeof(size_t));
    size_t *right_idx = (size_t *)malloc(best_r * sizeof(size_t));
    if (!left_idx || !right_idx) {
        free(left_idx);
        free(right_idx);
        free(node);
        return make_leaf(mean_temp(temp, idx, count));
    }

    size_t li = 0, ri = 0;
    for (size_t i = 0; i < count; i++) {
        if (feature_value(s, idx[i], n, best_feature) <= best_threshold) {
            left_idx[li++] = idx[i];
        } else {
            right_idx[ri++] = idx[i];
        }
    }

    node->left = build_tree(s, temp, left_idx, li, n, depth + 1);
    node->right = build_tree(s, temp, right_idx, ri, n, depth + 1);
    free(left_idx);
    free(right_idx);

    if (!node->left || !node->right) {
        double fallback = mean_temp(temp, idx, count);
        free_tree(node->left);
        free_tree(node->right);
        free(node);
        return make_leaf(fallback);
    }
    return node;
}

static double predict_tree(const DtNode *node, const Series *s, size_t query_idx, size_t n) {
    if (!node) {
        return NAN;
    }
    if (node->is_leaf) {
        return node->value;
    }
    if (feature_value(s, query_idx, n, node->feature) <= node->threshold) {
        return predict_tree(node->left, s, query_idx, n);
    }
    return predict_tree(node->right, s, query_idx, n);
}

static void fill_remaining_gaps(double *out, size_t n) {
    double last = NAN;
    for (size_t i = 0; i < n; i++) {
        if (!isnan(out[i])) {
            last = out[i];
        } else if (!isnan(last)) {
            out[i] = last;
        }
    }
    double next = NAN;
    for (size_t i = n; i-- > 0;) {
        if (!isnan(out[i])) {
            next = out[i];
        } else if (!isnan(next)) {
            out[i] = next;
        }
    }
}

int decision_tree_imputation(const Series *series, const double *temp, double *out) {
    size_t n = series->n;

    for (size_t i = 0; i < n; i++) {
        out[i] = temp[i];
    }

    size_t known_count = 0;
    for (size_t i = 0; i < n; i++) {
        if (!isnan(temp[i])) {
            known_count++;
        }
    }
    if (known_count == 0) {
        return 1;
    }

    size_t *known = (size_t *)malloc(known_count * sizeof(size_t));
    if (!known) {
        return 1;
    }
    size_t kc = 0;
    for (size_t i = 0; i < n; i++) {
        if (!isnan(temp[i])) {
            known[kc++] = i;
        }
    }

    DtNode *tree = build_tree(series, temp, known, known_count, n, 0);
    free(known);

    if (!tree) {
        return 1;
    }

    for (size_t i = 0; i < n; i++) {
        if (!isnan(temp[i])) {
            continue;
        }
        out[i] = predict_tree(tree, series, i, n);
    }

    free_tree(tree);
    fill_remaining_gaps(out, n);
    return 0;
}
