#include "knn_upgraded.h"

#include <math.h>
#include <stdlib.h>

static const double TWO_PI = 2.0 * 3.14159265358979323846;

KnnUpgradedConfig knn_upgraded_default(void) {
    KnnUpgradedConfig cfg;
    cfg.n_neighbors = 5;
    cfg.weight_position = 1.0;
    cfg.weight_hour = 2.0;
    cfg.weight_yday = 1.0;
    cfg.distance_epsilon = 1e-6;
    return cfg;
}

/*
 * Znacajke za udaljenost (5 dimenzija):
 *   [0] position_norm = index / (n - 1)
 *   [1] hour_sin, [2] hour_cos  — ciklicki sat (23:00 i 00:00 su blizu)
 *   [3] yday_sin, [4] yday_cos  — ciklicki dan (365. i 1. dan su blizu)
 *
 * Obicna udaljenost |23 - 0| = 23 ne hvata da su ti sati susjedni.
 * Sin/cos mapira sat i dan na krug — blizina na krugu = blizina u vremenu.
 */
static void upgraded_features(const Series *s, size_t idx, size_t n,
                              double out[5]) {
    double denom = (n > 1) ? (double)(n - 1) : 1.0;
    out[0] = (double)idx / denom;

    double hour_angle = TWO_PI * (double)s->hour[idx] / 24.0;
    out[1] = sin(hour_angle);
    out[2] = cos(hour_angle);

    double yday_angle = TWO_PI * (double)(s->yday[idx] - 1) / 365.0;
    out[3] = sin(yday_angle);
    out[4] = cos(yday_angle);
}

static double feature_distance_sq_upgraded(const Series *s, size_t a, size_t b,
                                           size_t n, const KnnUpgradedConfig *cfg) {
    double fa[5], fb[5];
    upgraded_features(s, a, n, fa);
    upgraded_features(s, b, n, fb);

    double dp = (fa[0] - fb[0]) * cfg->weight_position;
    double dhs = (fa[1] - fb[1]) * cfg->weight_hour;
    double dhc = (fa[2] - fb[2]) * cfg->weight_hour;
    double dys = (fa[3] - fb[3]) * cfg->weight_yday;
    double dyc = (fa[4] - fb[4]) * cfg->weight_yday;
    return dp * dp + dhs * dhs + dhc * dhc + dys * dys + dyc * dyc;
}

static int effective_neighbors(int requested_k, size_t known_count, size_t n) {
    int k = requested_k;
    if (k < 1) {
        k = 1;
    }
    if ((size_t)k > known_count) {
        k = (int)known_count;
    }
    /* Na malom nizu smanji k — manje overfittinga na par susjeda. */
    if (n <= 16 && k > 3) {
        k = 3;
    }
    if (n <= 8 && k > 2) {
        k = 2;
    }
    return k;
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

/*
 * Ulaz:  series (znacajke), temp (damaged niz s NaN), cfg (ili NULL za default)
 * Izlaz: out (popunjeni niz); temp i series->temp se ne mijenjaju
 * Povrat: 0 = uspjeh, 1 = greska (nema poznatih vrijednosti ili malloc)
 */
int knn_imputation_upgraded(const Series *series, const double *temp,
                            const KnnUpgradedConfig *cfg_in, double *out) {
    KnnUpgradedConfig defaults = knn_upgraded_default();
    const KnnUpgradedConfig *cfg = (cfg_in != NULL) ? cfg_in : &defaults;

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

    int k = effective_neighbors(cfg->n_neighbors, known_count, n);

    double *best_dist = (double *)malloc((size_t)k * sizeof(double));
    size_t *best_idx = (size_t *)malloc((size_t)k * sizeof(size_t));
    if (!best_dist || !best_idx) {
        free(known); free(best_dist); free(best_idx);
        return 1;
    }

    for (size_t i = 0; i < n; i++) {
        if (!isnan(temp[i])) {
            continue;
        }

        for (int t = 0; t < k; t++) {
            best_dist[t] = INFINITY;
            best_idx[t] = known[0];
        }

        for (size_t j = 0; j < known_count; j++) {
            size_t cand = known[j];
            double d = feature_distance_sq_upgraded(series, i, cand, n, cfg);
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

        /* Tezinski prosjek: blizi susjedi (manja udaljenost) vise utjecu. */
        double weight_sum = 0.0;
        double value_sum = 0.0;
        for (int t = 0; t < k; t++) {
            double dist = sqrt(best_dist[t]);
            double w = 1.0 / (dist + cfg->distance_epsilon);
            weight_sum += w;
            value_sum += w * temp[best_idx[t]];
        }
        out[i] = value_sum / weight_sum;
    }

    free(known);
    free(best_dist);
    free(best_idx);

    fill_remaining_gaps(out, n);
    return 0;
}
