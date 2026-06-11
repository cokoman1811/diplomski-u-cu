#ifndef DECISION_TREE_H
#define DECISION_TREE_H

#include "series.h"

/*
 * Jednostavno regresijsko stablo odlucivanja za imputaciju temperature.
 *
 * Trenira se samo na poznatim (ne-NaN) vrijednostima iz damaged niza.
 * Znacajke su iste kao kod knn_upgraded: normalizirana pozicija + sin/cos hour/yday.
 *
 * Ulaz:  series, damaged niz (temp), out
 * Izlaz: out — poznate netaknute, NaN popunjeni predikcijom stabla
 * Povrat: 0 uspjeh, 1 greska
 */
int decision_tree_imputation(const Series *series, const double *temp, double *out);

#endif /* DECISION_TREE_H */
