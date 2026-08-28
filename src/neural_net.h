#ifndef NEURAL_NET_H
#define NEURAL_NET_H

#include "series.h"

#include <stddef.h>

/*
 * Imputacija viseslojnim perceptronom (MLP), implementirana od nule u C99.
 *
 * Arhitektura:  ML_NUM_FEATURES -> 24 (tanh) -> 12 (tanh) -> 1 (linearno)
 * Ucenje:       backpropagation + Adam, mini-batch, deterministicki seed
 *
 * Dvije odluke koje su presudne za rezultat:
 *
 *   1. Mreza uci REZIDUAL iznad linearne baze, a ne temperaturu. Kako se
 *      izlazni sloj inicijalizira na male vrijednosti, mreza na pocetku
 *      predvida priblizno nulu, sto znaci "linearna baza je tocna". Ucenje
 *      je time popravljanje interpolacije, a ne ucenje niza od nule. Bez toga
 *      bi mreza morala nauciti cijeli oblik signala i bila bi znatno losija.
 *
 *   2. Ulazi ukljucuju vrijednosti najblizih poznatih susjeda (gap-znacajke).
 *      Mreza koja vidi samo vrijeme nema iz cega predvidjeti temperaturu na
 *      signalu ciji je jedini iskoristivi obrazac lokalna glatkoca.
 *
 * Ulaz:  series, damaged niz (NAN na rupama)
 * Izlaz: out — poznate vrijednosti netaknute, rupe popunjene
 * Povrat: 0 uspjeh, 1 greska (nema poznatih tocaka ili alokacija nije uspjela)
 */
int neural_net_imputation(const Series *series, const double *temp, double *out);

#endif /* NEURAL_NET_H */
