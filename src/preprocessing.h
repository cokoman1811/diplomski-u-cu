#ifndef PREPROCESSING_H
#define PREPROCESSING_H

#include <stddef.h>

/*
 * Umjetno uklanjanje vrijednosti iz niza radi evaluacije.
 *
 * temp        - ulazni temperaturni niz (n vrijednosti)
 * n           - broj vrijednosti
 * missing_rate- udio vrijednosti za uklanjanje (0..1)
 * seed        - sjeme za ponovljiv slucajni odabir
 * damaged     - izlaz: kopija niza s NAN na uklonjenim mjestima (velicina n)
 * mask        - izlaz: 1 gdje je vrijednost uklonjena, inace 0 (velicina n)
 *
 * Prva i zadnja vrijednost se uvijek cuvaju (rubni oslonci za interpolaciju).
 * Vraca broj uklonjenih vrijednosti.
 */
size_t create_missing_values(const double *temp, size_t n, double missing_rate,
                             unsigned long long seed, double *damaged, int *mask);

/*
 * Block missing: uklanja kontinuirane blokove vrijednosti (npr. kvar senzora).
 *
 * block_size  - duljina jednog bloka (npr. 12 = 2 sata pri 10-min intervalu)
 * missing_rate- ciljani udio uklonjenih vrijednosti (0..1)
 *
 * Ista pravila kao create_missing_values: temp se ne mijenja, prva i zadnja
 * vrijednost ostaju poznate, mask[i]=1 gdje je damaged[i]=NAN.
 */
#define PREPROC_BLOCK_SIZE_2H_10MIN 12

size_t create_block_missing_values(const double *temp, size_t n, size_t block_size,
                                   double missing_rate, unsigned long long seed,
                                   double *damaged, int *mask);

#endif /* PREPROCESSING_H */
