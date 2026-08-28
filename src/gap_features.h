#ifndef GAP_FEATURES_H
#define GAP_FEATURES_H

#include <stddef.h>

/* Broj znacajki koje opisuju polozaj tocke unutar praznine. */
#define GAP_NUM_FEATURES 6

/* Indeksi pojedinih znacajki unutar retka. */
#define GAP_F_PREV_VAL 0
#define GAP_F_NEXT_VAL 1
#define GAP_F_ALPHA    2
#define GAP_F_D_PREV   3
#define GAP_F_D_NEXT   4
#define GAP_F_LIN_BASE 5

/*
 * Za svaku poziciju racuna sest znacajki izvedenih iz najblizih POZNATIH susjeda:
 *
 *   [0] prev_val   vrijednost najblizeg poznatog susjeda lijevo
 *   [1] next_val   vrijednost najblizeg poznatog susjeda desno
 *   [2] alpha      relativan polozaj u praznini: (i - pi) / (ni - pi)
 *   [3] d_prev     udaljenost do lijevog susjeda u uzorcima
 *   [4] d_next     udaljenost do desnog susjeda u uzorcima
 *   [5] lin_base   prev_val + alpha * (next_val - prev_val), tj. linearna baza
 *
 * Racuna se iskljucivo iz ostecenog niza, pa nema curenja informacija.
 *
 * Kljucno za korektnost: za POZNATU tocku susjedi se traze u skupu known \ {i},
 * dakle sama tocka se preskace. Bez toga bi prev_val za trening-tocku bio jednak
 * ciljnoj vrijednosti, model bi naucio identitet, a u testu bi ista znacajka
 * imala posve drugo znacenje.
 *
 * feat mora biti niz od n * GAP_NUM_FEATURES doubleova (row-major).
 */
void gap_features_compute(const double *temp, size_t n, double *feat);

/*
 * Pomocna funkcija: upisuje linearnu bazu (znacajka [5]) za cijeli niz.
 * Ekvivalentno linearnoj interpolaciji uz rubno produljenje konstantom.
 */
void gap_features_linear_base(const double *temp, size_t n, double *base);

#endif /* GAP_FEATURES_H */
