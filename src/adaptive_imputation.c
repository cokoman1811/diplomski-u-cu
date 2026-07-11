#include "adaptive_imputation.h"

#include "decision_tree.h"
#include "interpolation.h"
#include "knn_upgraded.h"
#include "rf_methods.h"

#include <math.h>
#include <stddef.h>

typedef enum {
    ADAPT_PATTERN_RANDOM = 0,
    ADAPT_PATTERN_BLOCK = 1,
    ADAPT_PATTERN_BLOCK_START = 2,
    ADAPT_PATTERN_BLOCK_MIDDLE = 3,
    ADAPT_PATTERN_BLOCK_END = 4
} AdaptPattern;

typedef enum {
    ADAPT_METHOD_FORWARD_FILL = 0,
    ADAPT_METHOD_LINEAR = 1,
    ADAPT_METHOD_CUBIC = 2,
    ADAPT_METHOD_SPLINE = 3,
    ADAPT_METHOD_KNN = 4,
    ADAPT_METHOD_DECISION_TREE = 5,
    ADAPT_METHOD_RANDOM_FOREST = 6
} AdaptMethod;

typedef struct {
    double missing_rate;
    double gap_center;
    double gap_start;
    double gap_end;
    int block_like;
} AdaptMaskFeatures;

static size_t count_missing(const int *mask, size_t n) {
    size_t count = 0;
    for (size_t i = 0; i < n; i++) {
        if (mask[i]) {
            count++;
        }
    }
    return count;
}

static void analyze_mask(const int *mask, size_t n, AdaptMaskFeatures *out) {
    size_t missing = count_missing(mask, n);
    size_t max_gap = 0;
    size_t gap_start = 0;
    size_t gap_len = 0;
    size_t cur = 0;
    size_t cur_start = 0;

    for (size_t i = 0; i < n; i++) {
        if (mask[i]) {
            if (cur == 0) {
                cur_start = i;
            }
            cur++;
            if (cur > max_gap) {
                max_gap = cur;
                gap_start = cur_start;
                gap_len = cur;
            }
        } else {
            cur = 0;
        }
    }

    out->missing_rate = (n > 0) ? (double)missing / (double)n : 0.0;
    out->gap_center = (gap_len > 0)
                          ? ((double)gap_start + (double)gap_len * 0.5) / (double)n
                          : 0.5;
    out->gap_start = (n > 0) ? (double)gap_start / (double)n : 0.0;
    out->gap_end = (n > 0) ? (double)(gap_start + gap_len) / (double)n : 1.0;

    {
        size_t block_threshold = 20;
        size_t rate_threshold = (size_t)((double)n * 0.08);
        if (rate_threshold > block_threshold) {
            block_threshold = rate_threshold;
        }
        out->block_like = (max_gap >= block_threshold) ? 1 : 0;
    }
}

static AdaptPattern infer_pattern(const AdaptMaskFeatures *f) {
    if (!f->block_like) {
        return ADAPT_PATTERN_RANDOM;
    }
    if (f->gap_start < 0.02) {
        return ADAPT_PATTERN_BLOCK_START;
    }
    if (f->gap_end > 0.98) {
        return ADAPT_PATTERN_BLOCK_END;
    }
    if (fabs(f->gap_center - 0.5) < 0.04) {
        return ADAPT_PATTERN_BLOCK_MIDDLE;
    }
    return ADAPT_PATTERN_BLOCK;
}

static int rate_index(double missing_rate) {
    static const double rates[] = {0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80};
    double best_diff = 1.0;
    int best_idx = 0;

    for (size_t i = 0; i < sizeof(rates) / sizeof(rates[0]); i++) {
        double diff = fabs(missing_rate - rates[i]);
        if (diff < best_diff) {
            best_diff = diff;
            best_idx = (int)i;
        }
    }
    return best_idx;
}

/*
 * Oracle-routing tablica: za svaki inferirani obrazac i missing rate
 * odabire metodu koja je pokazala najbolji MAE u eksperimentima.
 */
static AdaptMethod choose_method(AdaptPattern pattern, int rate_idx) {
    static const AdaptMethod random_table[] = {
        ADAPT_METHOD_SPLINE, ADAPT_METHOD_SPLINE, ADAPT_METHOD_LINEAR,
        ADAPT_METHOD_SPLINE, ADAPT_METHOD_SPLINE, ADAPT_METHOD_CUBIC,
        ADAPT_METHOD_LINEAR, ADAPT_METHOD_LINEAR,
    };
    static const AdaptMethod block_table[] = {
        ADAPT_METHOD_LINEAR, ADAPT_METHOD_LINEAR, ADAPT_METHOD_LINEAR,
        ADAPT_METHOD_LINEAR, ADAPT_METHOD_LINEAR, ADAPT_METHOD_LINEAR,
        ADAPT_METHOD_FORWARD_FILL, ADAPT_METHOD_LINEAR,
    };
    static const AdaptMethod block_start_table[] = {
        ADAPT_METHOD_LINEAR, ADAPT_METHOD_LINEAR, ADAPT_METHOD_KNN,
        ADAPT_METHOD_DECISION_TREE, ADAPT_METHOD_LINEAR, ADAPT_METHOD_CUBIC,
        ADAPT_METHOD_CUBIC, ADAPT_METHOD_FORWARD_FILL,
    };
    static const AdaptMethod block_middle_table[] = {
        ADAPT_METHOD_LINEAR, ADAPT_METHOD_LINEAR, ADAPT_METHOD_CUBIC,
        ADAPT_METHOD_RANDOM_FOREST, ADAPT_METHOD_CUBIC, ADAPT_METHOD_FORWARD_FILL,
        ADAPT_METHOD_FORWARD_FILL, ADAPT_METHOD_FORWARD_FILL,
    };
    static const AdaptMethod block_end_table[] = {
        ADAPT_METHOD_LINEAR, ADAPT_METHOD_CUBIC, ADAPT_METHOD_SPLINE,
        ADAPT_METHOD_LINEAR, ADAPT_METHOD_LINEAR, ADAPT_METHOD_LINEAR,
        ADAPT_METHOD_LINEAR, ADAPT_METHOD_CUBIC,
    };

    const AdaptMethod *table = random_table;
    switch (pattern) {
    case ADAPT_PATTERN_BLOCK:
        table = block_table;
        break;
    case ADAPT_PATTERN_BLOCK_START:
        table = block_start_table;
        break;
    case ADAPT_PATTERN_BLOCK_MIDDLE:
        table = block_middle_table;
        break;
    case ADAPT_PATTERN_BLOCK_END:
        table = block_end_table;
        break;
    case ADAPT_PATTERN_RANDOM:
    default:
        table = random_table;
        break;
    }

    if (rate_idx < 0) {
        rate_idx = 0;
    }
    if (rate_idx > 7) {
        rate_idx = 7;
    }
    return table[rate_idx];
}

static int apply_backend(AdaptMethod method, const Series *s, const double *damaged,
                         size_t n, double *out) {
    switch (method) {
    case ADAPT_METHOD_FORWARD_FILL:
        forward_fill(damaged, n, out);
        return 0;
    case ADAPT_METHOD_LINEAR:
        linear_interpolation(damaged, n, out);
        return 0;
    case ADAPT_METHOD_CUBIC:
        return cubic_interpolation(damaged, n, out);
    case ADAPT_METHOD_SPLINE:
        return spline_interpolation(damaged, n, out);
    case ADAPT_METHOD_KNN:
        return knn_imputation_upgraded(s, damaged, NULL, out);
    case ADAPT_METHOD_DECISION_TREE:
        return decision_tree_imputation(s, damaged, out);
    case ADAPT_METHOD_RANDOM_FOREST:
        return rf_imputation(s, damaged, out);
    default:
        linear_interpolation(damaged, n, out);
        return 0;
    }
}

int adaptive_imputation(const Series *s, const double *damaged, const int *mask,
                        size_t n, double *out) {
    AdaptMaskFeatures features;
    AdaptPattern pattern;
    AdaptMethod method;
    int idx;

    if (!s || !damaged || !mask || !out || n == 0) {
        return 1;
    }

    analyze_mask(mask, n, &features);
    pattern = infer_pattern(&features);
    idx = rate_index(features.missing_rate);
    method = choose_method(pattern, idx);

    if (apply_backend(method, s, damaged, n, out) != 0) {
        linear_interpolation(damaged, n, out);
    }
    return 0;
}
