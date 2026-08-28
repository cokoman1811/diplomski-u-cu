#include "ml_features.h"

#include <math.h>
#include <stdlib.h>

static const double ML_TWO_PI = 2.0 * 3.14159265358979323846;

void ml_features_build(const Series *s, const double *temp, size_t n, double *F) {
    double denom = (n > 1) ? (double)(n - 1) : 1.0;
    double *gap;
    size_t i;
    int g;

    if (!s || !temp || !F || n == 0) {
        return;
    }

    gap = (double *)malloc(n * GAP_NUM_FEATURES * sizeof(double));
    if (!gap) {
        for (i = 0; i < n * ML_NUM_FEATURES; i++) {
            F[i] = 0.0;
        }
        return;
    }
    gap_features_compute(temp, n, gap);

    for (i = 0; i < n; i++) {
        double *row = &F[i * ML_NUM_FEATURES];
        double hour_angle = ML_TWO_PI * (double)s->hour[i] / 24.0;
        double yday_angle = ML_TWO_PI * (double)(s->yday[i] - 1) / 365.0;

        for (g = 0; g < GAP_NUM_FEATURES; g++) {
            row[g] = gap[i * GAP_NUM_FEATURES + g];
        }
        row[GAP_NUM_FEATURES + 0] = (double)i / denom;
        row[GAP_NUM_FEATURES + 1] = sin(hour_angle);
        row[GAP_NUM_FEATURES + 2] = cos(hour_angle);
        row[GAP_NUM_FEATURES + 3] = sin(yday_angle);
        row[GAP_NUM_FEATURES + 4] = cos(yday_angle);
    }
    free(gap);
}

void ml_fill_remaining_gaps(double *out, size_t n) {
    double last = NAN;
    double next = NAN;
    size_t i;

    for (i = 0; i < n; i++) {
        if (!isnan(out[i])) {
            last = out[i];
        } else if (!isnan(last)) {
            out[i] = last;
        }
    }
    for (i = n; i-- > 0;) {
        if (!isnan(out[i])) {
            next = out[i];
        } else if (!isnan(next)) {
            out[i] = next;
        }
    }
}

void ml_known_range(const double *temp, size_t n, double *lo, double *hi) {
    size_t i;
    *lo = INFINITY;
    *hi = -INFINITY;
    for (i = 0; i < n; i++) {
        if (isnan(temp[i])) {
            continue;
        }
        if (temp[i] < *lo) {
            *lo = temp[i];
        }
        if (temp[i] > *hi) {
            *hi = temp[i];
        }
    }
    if (*lo > *hi) {
        *lo = 0.0;
        *hi = 0.0;
    }
}
