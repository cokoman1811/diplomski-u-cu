#ifndef ML_FEATURES_H
#define ML_FEATURES_H

#include "gap_features.h"
#include "series.h"

#include <stddef.h>

/*
 * Zajednicki prostor znacajki za sve ML metode (stablo, suma, neuronska mreza).
 *
 * Redoslijed stupaca:
 *   [0..5]  gap-znacajke (v. gap_features.h): prev_val, next_val, alpha,
 *           d_prev, d_next, lin_base
 *   [6]     position_norm = i / (n - 1)
 *   [7][8]  hour_sin, hour_cos
 *   [9][10] yday_sin, yday_cos
 *
 * Time se sve ML metode usporeduju na istom skupu znacajki, pa razlika u
 * rezultatu odrazava razliku u modelu, a ne u ulazima.
 */

#define ML_NUM_TIME_FEATURES 5
#define ML_NUM_FEATURES (GAP_NUM_FEATURES + ML_NUM_TIME_FEATURES)

/* F mora biti niz od n * ML_NUM_FEATURES doubleova (row-major). */
void ml_features_build(const Series *s, const double *temp, size_t n, double *F);

/* Popunjava preostale NAN vrijednosti forward pa backward fillom. */
void ml_fill_remaining_gaps(double *out, size_t n);

/* Raspon poznatih vrijednosti; koristi se za ogranicavanje predikcije. */
void ml_known_range(const double *temp, size_t n, double *lo, double *hi);

#endif /* ML_FEATURES_H */
