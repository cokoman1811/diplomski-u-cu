#ifndef KNN_METHODS_H
#define KNN_METHODS_H

#include "series.h"

/*
 * KNN imputacija — prva ML metoda u usporedbi s klasicnom interpolacijom.
 *
 * Zašto KNN uz interpolaciju?
 *   Interpolacija gleda susjede u nizu (lijevo/desno). KNN trazi slicna
 *   mjerenja u cijelom nizu prema znacajkama (pozicija, sat, dan u godini).
 *
 * Ulaz:
 *   series      - znacajke (hour, yday, n); damaged temp se ne mijenja ovdje
 *   temp        - damaged niz (NAN = nedostaje)
 *   n_neighbors - k najblizih susjeda (u main.c: 5)
 *   out         - popunjeni niz (bez NAN)
 *
 * Poznate vrijednosti u out ostaju iste kao u temp; mijenjaju se samo NaN.
 * Usporedba u main.c: run_compare() -> knn_imputation -> evaluate_reconstruction.
 * Test: tests/run_tests.c -> test_knn().
 */
int knn_imputation(const Series *series, const double *temp, int n_neighbors, double *out);

#endif /* KNN_METHODS_H */
