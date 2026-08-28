#include "gap_features.h"

#include <math.h>
#include <stdlib.h>

/* Zamjena za "beskonacnu" udaljenost kad susjed s jedne strane ne postoji. */
#define GAP_FAR 1.0e4

void gap_features_compute(const double *temp, size_t n, double *feat) {
    size_t i;
    long long last = -1;
    long long next = -1;

    if (!temp || !feat || n == 0) {
        return;
    }

    /*
     * Indeks susjeda privremeno spremamo u stupce [3] i [4].
     * Upis se radi PRIJE azuriranja `last`/`next`, cime poznata tocka
     * preskace samu sebe i rezim znacajki je isti u treningu i testu.
     */
    for (i = 0; i < n; i++) {
        feat[i * GAP_NUM_FEATURES + GAP_F_D_PREV] = (double)last;
        if (!isnan(temp[i])) {
            last = (long long)i;
        }
    }
    for (i = n; i-- > 0;) {
        feat[i * GAP_NUM_FEATURES + GAP_F_D_NEXT] = (double)next;
        if (!isnan(temp[i])) {
            next = (long long)i;
        }
    }

    for (i = 0; i < n; i++) {
        double *f = &feat[i * GAP_NUM_FEATURES];
        long long pi = (long long)f[GAP_F_D_PREV];
        long long ni = (long long)f[GAP_F_D_NEXT];
        double prev_val, next_val, alpha, d_prev, d_next;

        if (pi >= 0 && ni >= 0) {
            prev_val = temp[pi];
            next_val = temp[ni];
            alpha = (double)((long long)i - pi) / (double)(ni - pi);
            d_prev = (double)((long long)i - pi);
            d_next = (double)(ni - (long long)i);
        } else if (pi >= 0) {
            /* Nema poznatog susjeda desno — produljujemo lijevu vrijednost. */
            prev_val = temp[pi];
            next_val = temp[pi];
            alpha = 1.0;
            d_prev = (double)((long long)i - pi);
            d_next = GAP_FAR;
        } else if (ni >= 0) {
            /* Nema poznatog susjeda lijevo. */
            prev_val = temp[ni];
            next_val = temp[ni];
            alpha = 0.0;
            d_prev = GAP_FAR;
            d_next = (double)(ni - (long long)i);
        } else {
            /* Nema nijedne poznate tocke u nizu. */
            prev_val = 0.0;
            next_val = 0.0;
            alpha = 0.5;
            d_prev = GAP_FAR;
            d_next = GAP_FAR;
        }

        f[GAP_F_PREV_VAL] = prev_val;
        f[GAP_F_NEXT_VAL] = next_val;
        f[GAP_F_ALPHA] = alpha;
        f[GAP_F_D_PREV] = d_prev;
        f[GAP_F_D_NEXT] = d_next;
        f[GAP_F_LIN_BASE] = prev_val + alpha * (next_val - prev_val);
    }
}

void gap_features_linear_base(const double *temp, size_t n, double *base) {
    double *feat;
    size_t i;

    if (!temp || !base || n == 0) {
        return;
    }

    feat = (double *)malloc(n * GAP_NUM_FEATURES * sizeof(double));
    if (!feat) {
        for (i = 0; i < n; i++) {
            base[i] = isnan(temp[i]) ? 0.0 : temp[i];
        }
        return;
    }

    gap_features_compute(temp, n, feat);
    for (i = 0; i < n; i++) {
        base[i] = feat[i * GAP_NUM_FEATURES + GAP_F_LIN_BASE];
    }
    free(feat);
}
