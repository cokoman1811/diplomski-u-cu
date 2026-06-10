#include "knn_methods.h"

#include <math.h>
#include <stdlib.h>

/*
 * Udaljenost izmedu dva mjerenja u prostoru znacajki:
 *   pozicija u nizu, sat u danu (hour), dan u godini (yday).
 * Manja udaljenost = slicnije mjerenje (npr. isti sat, blizu u nizu).
 */
static double feature_distance_sq(const Series *s, size_t a, size_t b) {
    double dp = (double)a - (double)b;
    double dh = (double)s->hour[a] - (double)s->hour[b];
    double dy = (double)s->yday[a] - (double)s->yday[b];
    return dp * dp + dh * dh + dy * dy;
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

int knn_imputation(const Series *series, const double *temp, int n_neighbors, double *out) {
    size_t n = series->n;

    /* Kopija damaged niza; NaN mjesta popunjavamo kasnije. */
    for (size_t i = 0; i < n; i++) {
        out[i] = temp[i];
    }

    /* Indeksi poznatih (ne-NaN) vrijednosti — samo oni sluze kao "trening". */
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

    int k = n_neighbors;
    if (k < 1) {
        k = 1;
    }
    if ((size_t)k > known_count) {
        k = (int)known_count;
    }

    double *best_dist = (double *)malloc((size_t)k * sizeof(double));
    size_t *best_idx = (size_t *)malloc((size_t)k * sizeof(size_t));
    if (!best_dist || !best_idx) {
        free(known); free(best_dist); free(best_idx);
        return 1;
    }

    /* Samo NaN pozicije: pronadi k najblizih poznatih i prosjek njihovih temperatura. */
    for (size_t i = 0; i < n; i++) {
        if (!isnan(temp[i])) {
            continue;
        }

        for (int t = 0; t < k; t++) {
            best_dist[t] = INFINITY;
            best_idx[t] = 0;
        }

        for (size_t j = 0; j < known_count; j++) {
            size_t cand = known[j];
            double d = feature_distance_sq(series, i, cand);
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

        double sum = 0.0;
        for (int t = 0; t < k; t++) {
            sum += temp[best_idx[t]];
        }
        out[i] = sum / (double)k;
    }

    free(known);
    free(best_dist);
    free(best_idx);

    fill_remaining_gaps(out, n);
    return 0;
}
