#include "rf_methods.h"

#include <math.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#define RF_NUM_TREES 8
#define RF_MAX_DEPTH 4
#define RF_MIN_LEAF  3
#define RF_NUM_FEATURES 3

typedef struct RfNode {
    int is_leaf;
    double value;
    int feature;
    double threshold;
    struct RfNode *left;
    struct RfNode *right;
} RfNode;

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

static double feature_value(const Series *s, size_t idx, int feature) {
    switch (feature) {
    case 0: return (double)idx;
    case 1: return (double)s->hour[idx];
    default: return (double)s->yday[idx];
    }
}

static double mean_temp(const double *temp, const size_t *idx, size_t count) {
    double sum = 0.0;
    for (size_t i = 0; i < count; i++) {
        sum += temp[idx[i]];
    }
    return sum / (double)count;
}

static void free_tree(RfNode *node) {
    if (!node) {
        return;
    }
    free_tree(node->left);
    free_tree(node->right);
    free(node);
}

static RfNode *make_leaf(double value) {
    RfNode *node = (RfNode *)calloc(1, sizeof(RfNode));
    if (!node) {
        return NULL;
    }
    node->is_leaf = 1;
    node->value = value;
    return node;
}

static double split_mse(const double *temp, const size_t *idx, size_t count,
                          int feature, double threshold, const Series *s,
                          size_t *left_count, size_t *right_count) {
    double sum_l = 0.0, sum_r = 0.0;
    size_t n_l = 0, n_r = 0;

    for (size_t i = 0; i < count; i++) {
        double y = temp[idx[i]];
        if (feature_value(s, idx[i], feature) < threshold) {
            sum_l += y;
            n_l++;
        } else {
            sum_r += y;
            n_r++;
        }
    }

    *left_count = n_l;
    *right_count = n_r;
    if (n_l == 0 || n_r == 0) {
        return INFINITY;
    }

    double mean_l = sum_l / (double)n_l;
    double mean_r = sum_r / (double)n_r;
    double mse = 0.0;

    for (size_t i = 0; i < count; i++) {
        double y = temp[idx[i]];
        double m = (feature_value(s, idx[i], feature) < threshold) ? mean_l : mean_r;
        double d = y - m;
        mse += d * d;
    }
    return mse;
}

static RfNode *build_tree(const Series *s, const double *temp,
                          const size_t *idx, size_t count, int depth) {
    if (count == 0) {
        return NULL;
    }

    if (depth >= RF_MAX_DEPTH || count < (size_t)RF_MIN_LEAF * 2) {
        return make_leaf(mean_temp(temp, idx, count));
    }

    double best_mse = INFINITY;
    int best_feature = 0;
    double best_threshold = 0.0;
    size_t best_l = 0, best_r = 0;

    for (int f = 0; f < RF_NUM_FEATURES; f++) {
        for (size_t i = 0; i < count; i++) {
            double thr = feature_value(s, idx[i], f);
            size_t n_l = 0, n_r = 0;
            double mse = split_mse(temp, idx, count, f, thr, s, &n_l, &n_r);
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

    RfNode *node = (RfNode *)calloc(1, sizeof(RfNode));
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
        if (feature_value(s, idx[i], best_feature) < best_threshold) {
            left_idx[li++] = idx[i];
        } else {
            right_idx[ri++] = idx[i];
        }
    }

    node->left = build_tree(s, temp, left_idx, li, depth + 1);
    node->right = build_tree(s, temp, right_idx, ri, depth + 1);
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

static double predict_tree(const RfNode *node, const Series *s, size_t query_idx) {
    if (!node) {
        return NAN;
    }
    if (node->is_leaf) {
        return node->value;
    }
    if (feature_value(s, query_idx, node->feature) < node->threshold) {
        return predict_tree(node->left, s, query_idx);
    }
    return predict_tree(node->right, s, query_idx);
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

int rf_imputation(const Series *series, const double *temp, double *out) {
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

    RfNode *trees[RF_NUM_TREES];
    for (int t = 0; t < RF_NUM_TREES; t++) {
        trees[t] = NULL;
    }

    rf_rng_state = 42ULL;

    for (int t = 0; t < RF_NUM_TREES; t++) {
        size_t *boot = (size_t *)malloc(known_count * sizeof(size_t));
        if (!boot) {
            for (int j = 0; j < t; j++) {
                free_tree(trees[j]);
            }
            free(known);
            return 1;
        }
        for (size_t i = 0; i < known_count; i++) {
            boot[i] = known[rf_rng_below(known_count)];
        }
        trees[t] = build_tree(series, temp, boot, known_count, 0);
        free(boot);
        if (!trees[t]) {
            for (int j = 0; j < t; j++) {
                free_tree(trees[j]);
            }
            free(known);
            return 1;
        }
    }
    free(known);

    for (size_t i = 0; i < n; i++) {
        if (!isnan(temp[i])) {
            continue;
        }
        double sum = 0.0;
        int used = 0;
        for (int t = 0; t < RF_NUM_TREES; t++) {
            double p = predict_tree(trees[t], series, i);
            if (!isnan(p)) {
                sum += p;
                used++;
            }
        }
        if (used > 0) {
            out[i] = sum / (double)used;
        }
    }

    for (int t = 0; t < RF_NUM_TREES; t++) {
        free_tree(trees[t]);
    }

    fill_remaining_gaps(out, n);
    return 0;
}
