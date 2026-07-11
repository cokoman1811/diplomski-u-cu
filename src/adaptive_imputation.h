#ifndef ADAPTIVE_IMPUTATION_H
#define ADAPTIVE_IMPUTATION_H

#include "series.h"

#include <stddef.h>

/*
 * Adaptivna hibridna imputacija: analizira obrazac nedostajucih vrijednosti
 * (stopa, velicina i pozicija najveceg bloka) i automatski bira najbolju
 * poznatu metodu za taj obrazac.
 *
 * Vraca 0 ako je imputacija uspjela, != 0 ako nijedna metoda nije primjenjiva.
 */
int adaptive_imputation(const Series *s, const double *damaged, const int *mask,
                        size_t n, double *out);

#endif /* ADAPTIVE_IMPUTATION_H */
