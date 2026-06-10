#ifndef KNN_UPGRADED_H
#define KNN_UPGRADED_H

#include "series.h"

/*
 * Poboljsana KNN imputacija — usporedba s osnovnom knn_imputation().
 *
 * Razlike u odnosu na knn_methods.c:
 *   - normalizirane znacajke (pozicija, hour, yday) prije udaljenosti
 *   - podesive tezine znacajki (nije fiksno 1:1:1 na sirovim vrijednostima)
 *   - tezinska predikcija: blizi susjedi imaju veci utjecaj
 *   - adaptivno k na malim nizovima
 *
 * Ako je cfg == NULL, koriste se zadane vrijednosti iz knn_upgraded_default().
 */
typedef struct {
    int n_neighbors;          /* zadani k (npr. 5) */
    double weight_position;   /* tezina normalizirane pozicije */
    double weight_hour;       /* tezina sata */
    double weight_yday;       /* tezina dana u godini */
    double distance_epsilon;  /* stabilizacija pri 1/(d+eps) tezinskom prosjeku */
} KnnUpgradedConfig;

KnnUpgradedConfig knn_upgraded_default(void);

int knn_imputation_upgraded(const Series *series, const double *temp,
                            const KnnUpgradedConfig *cfg, double *out);

#endif /* KNN_UPGRADED_H */
