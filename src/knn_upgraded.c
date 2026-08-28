#include "knn_upgraded.h"

#include "ml_features.h"

#include <math.h>
#include <stdlib.h>

#define KNN_UP_NUM_DIMS 5

static const double KNN_UP_TWO_PI = 2.0 * 3.14159265358979323846;

KnnUpgradedConfig knn_upgraded_default(void) {
    KnnUpgradedConfig cfg;
    cfg.n_neighbors = 12;
    cfg.weight_alpha = 1.0;
    cfg.weight_gap = 1.0;
    cfg.weight_hour = 0.5;
    cfg.distance_epsilon = 1e-6;
    return cfg;
}

/*
 * Opis "situacije" u kojoj se tocka nalazi:
 *   [0] alpha            relativan polozaj unutar praznine (0 = uz lijevi rub)
 *   [1] log(1 + d_prev)  koliko je daleko lijevi oslonac
 *   [2] log(1 + d_next)  koliko je daleko desni oslonac
 *   [3] hour_sin
 *   [4] hour_cos
 *
 * Logaritam se koristi jer d_prev/d_next variraju od 1 do nekoliko stotina;
 * bez njega bi duge praznine potpuno dominirale mjerom udaljenosti.
 */
static void knn_up_situation(const double *F, const Series *s, size_t idx,
                             const KnnUpgradedConfig *cfg, double *dst) {
    const double *row = &F[idx * ML_NUM_FEATURES];
    double hour_angle = KNN_UP_TWO_PI * (double)s->hour[idx] / 24.0;

    dst[0] = cfg->weight_alpha * row[GAP_F_ALPHA];
    dst[1] = cfg->weight_gap * log1p(row[GAP_F_D_PREV]);
    dst[2] = cfg->weight_gap * log1p(row[GAP_F_D_NEXT]);
    dst[3] = cfg->weight_hour * sin(hour_angle);
    dst[4] = cfg->weight_hour * cos(hour_angle);
}

int knn_imputation_upgraded(const Series *series, const double *temp,
                            const KnnUpgradedConfig *cfg_in, double *out) {
    KnnUpgradedConfig defaults = knn_upgraded_default();
    const KnnUpgradedConfig *cfg = (cfg_in != NULL) ? cfg_in : &defaults;

    size_t n = series->n;
    size_t known_count = 0, kc = 0, i;
    size_t *known = NULL;
    double *F = NULL, *resid = NULL, *situ = NULL;
    double *best_dist = NULL;
    size_t *best_idx = NULL;
    double lo, hi;
    int k, t;

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

    F = (double *)malloc(n * ML_NUM_FEATURES * sizeof(double));
    resid = (double *)malloc(n * sizeof(double));
    situ = (double *)malloc(n * KNN_UP_NUM_DIMS * sizeof(double));
    known = (size_t *)malloc(known_count * sizeof(size_t));
    if (!F || !resid || !situ || !known) {
        free(F);
        free(resid);
        free(situ);
        free(known);
        return 1;
    }

    ml_features_build(series, temp, n, F);

    for (i = 0; i < n; i++) {
        knn_up_situation(F, series, i, cfg, &situ[i * KNN_UP_NUM_DIMS]);
        if (!isnan(temp[i])) {
            resid[i] = temp[i] - F[i * ML_NUM_FEATURES + GAP_F_LIN_BASE];
            known[kc++] = i;
        } else {
            resid[i] = NAN;
        }
    }

    k = cfg->n_neighbors;
    if (k < 1) {
        k = 1;
    }
    if ((size_t)k > known_count) {
        k = (int)known_count;
    }

    best_dist = (double *)malloc((size_t)k * sizeof(double));
    best_idx = (size_t *)malloc((size_t)k * sizeof(size_t));
    if (!best_dist || !best_idx) {
        free(F);
        free(resid);
        free(situ);
        free(known);
        free(best_dist);
        free(best_idx);
        return 1;
    }

    for (i = 0; i < n; i++) {
        const double *qi;
        double weight_sum = 0.0, value_sum = 0.0, value;
        size_t j;

        if (!isnan(temp[i])) {
            continue;
        }
        qi = &situ[i * KNN_UP_NUM_DIMS];

        for (t = 0; t < k; t++) {
            best_dist[t] = INFINITY;
            best_idx[t] = known[0];
        }

        for (j = 0; j < known_count; j++) {
            size_t cand = known[j];
            const double *qc = &situ[cand * KNN_UP_NUM_DIMS];
            double d = 0.0;
            int dim;

            for (dim = 0; dim < KNN_UP_NUM_DIMS; dim++) {
                double diff = qi[dim] - qc[dim];
                d += diff * diff;
            }

            if (d < best_dist[k - 1]) {
                int pos = k - 1;
                while (pos > 0 && best_dist[pos - 1] > d) {
                    best_dist[pos] = best_dist[pos - 1];
                    best_idx[pos] = best_idx[pos - 1];
                    pos--;
                }
                best_dist[pos] = d;
                best_idx[pos] = cand;
            }
        }

        for (t = 0; t < k; t++) {
            double w = 1.0 / (sqrt(best_dist[t]) + cfg->distance_epsilon);
            weight_sum += w;
            value_sum += w * resid[best_idx[t]];
        }

        value = F[i * ML_NUM_FEATURES + GAP_F_LIN_BASE];
        if (weight_sum > 0.0) {
            value += value_sum / weight_sum;
        }
        if (value < lo) {
            value = lo;
        }
        if (value > hi) {
            value = hi;
        }
        out[i] = value;
    }

    free(F);
    free(resid);
    free(situ);
    free(known);
    free(best_dist);
    free(best_idx);
    ml_fill_remaining_gaps(out, n);
    return 0;
}
