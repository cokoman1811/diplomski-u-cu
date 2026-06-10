#ifndef KNN_UPGRADED_H
#define KNN_UPGRADED_H

#include "series.h"

/*
 * Poboljsana KNN imputacija — usporedba s osnovnom knn_imputation().
 *
 * Razlike u odnosu na knn_methods.c:
 *   - normalizirana pozicija: index / (n - 1)
 *   - ciklicke znacajke hour i yday preko sin/cos (23:00 ~ 00:00, 365. ~ 1. dan)
 *   - podesive tezine znacajki (weight_position, weight_hour, weight_yday)
 *   - tezinska predikcija: weight = 1 / (distance + epsilon)
 *   - adaptivno k na malim nizovima
 *
 * Ulaz:  series, damaged niz (temp), opcionalni cfg (NULL = default)
 * Izlaz: out — poznate vrijednosti netaknute, NaN popunjeni
 * Povrat: 0 uspjeh, 1 greska
 */
typedef struct {
    int n_neighbors;          /* zadani k (npr. 5) */
    double weight_position;   /* tezina normalizirane pozicije */
    double weight_hour;       /* tezina ciklickog sata (sin + cos) */
    double weight_yday;       /* tezina ciklickog dana (sin + cos) */
    double distance_epsilon;  /* stabilizacija pri 1/(d+eps) tezinskom prosjeku */
} KnnUpgradedConfig;

KnnUpgradedConfig knn_upgraded_default(void);

int knn_imputation_upgraded(const Series *series, const double *temp,
                            const KnnUpgradedConfig *cfg, double *out);

#endif /* KNN_UPGRADED_H */
