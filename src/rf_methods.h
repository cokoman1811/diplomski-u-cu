#ifndef RF_METHODS_H
#define RF_METHODS_H

#include "series.h"

/*
 * Minimalna Random Forest imputacija (regresija).
 *
 * Stil kao KNN: trenira se samo na poznatim vrijednostima, predvida samo NaN.
 * Znacajke: pozicija u nizu, hour, yday.
 *
 * Implementacija je namjerno jednostavna (malo stabala, plitko stablo).
 * TODO za kasnije: vise stabala, OOB evaluacija, finiji split kriterij.
 *
 * Vraca 0 kod uspjeha, != 0 ako nema poznatih vrijednosti.
 */
int rf_imputation(const Series *series, const double *temp, double *out);

#endif /* RF_METHODS_H */
