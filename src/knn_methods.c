#include "knn_methods.h"

#include <math.h>
#include <stdlib.h>

/*
 * KNN imputacija s obaveznim obuhvatom praznine.
 *
 * Prva verzija je uzimala k vremenski najblizih poznatih tocaka i racunala
 * njihov neponderirani prosjek. To ima dva nedostatka:
 *
 *   1. Prosjek je estimator NULTOG reda — egzaktan samo za konstantan signal.
 *      Na nizu koji se mijenja 0,14 C po uzorku sustavno zagladuje nagib.
 *   2. Nema jamstva da su susjedi s obje strane praznine. Uz rub bloka obje
 *      najblize tocke znaju biti s iste strane, pa metoda ne moze uhvatiti trend.
 *
 * Ova verzija bira po `per_side` najblizih poznatih tocaka LIJEVO i DESNO te
 * ih ponderira inverznom udaljenoscu. Za per_side = 1 to je matematicki
 * identicno linearnoj interpolaciji, jer je 1/d1 / (1/d1 + 1/d2) = d2/(d1+d2).
 * Linearna interpolacija je dakle specijalni slucaj KNN-a, a ne suparnicka
 * metoda — i ujedno donja granica koju KNN moze dosegnuti, ali ne probiti.
 *
 * Znacajke `hour` i `yday` izbacene su iz mjere udaljenosti: na sedmodnevnom
 * prozoru yday poprima samo 8 vrijednosti, a mjerenja pokazuju da njihovo
 * uklanjanje ne mijenja rezultat (3,739 -> 3,736), dok ih izjednacavanje
 * skale s pozicijom pogorsava na 4,793. Blizina u nizu je jedina relevantna
 * mjera slicnosti za signal s lag-1 autokorelacijom 0,99936.
 */

static void fill_remaining_gaps(double *out, size_t n) {
    double last = NAN;
    double next = NAN;
    size_t i;

    for (i = 0; i < n; i++) {
        if (!isnan(out[i])) {
            last = out[i];
        } else if (!isnan(last)) {
            out[i] = last;
        }
    }
    for (i = n; i-- > 0;) {
        if (!isnan(out[i])) {
            next = out[i];
        } else if (!isnan(next)) {
            out[i] = next;
        }
    }
}

int knn_imputation(const Series *series, const double *temp, int n_neighbors, double *out) {
    size_t n = series->n;
    size_t known_count = 0, kc = 0, i;
    size_t *known = NULL;
    int per_side;

    (void)series;

    for (i = 0; i < n; i++) {
        out[i] = temp[i];
        if (!isnan(temp[i])) {
            known_count++;
        }
    }
    if (known_count == 0) {
        return 1;
    }

    known = (size_t *)malloc(known_count * sizeof(size_t));
    if (!known) {
        return 1;
    }
    for (i = 0; i < n; i++) {
        if (!isnan(temp[i])) {
            known[kc++] = i;
        }
    }

    /* n_neighbors je ukupan broj susjeda; dijelimo ga na dvije strane. */
    per_side = n_neighbors / 2;
    if (per_side < 1) {
        per_side = 1;
    }

    for (i = 0; i < n; i++) {
        double weight_sum = 0.0;
        double value_sum = 0.0;
        size_t lo, hi, pos;
        int taken;

        if (!isnan(temp[i])) {
            continue;
        }

        /* Binarno trazenje prve poznate tocke desno od i. */
        lo = 0;
        hi = known_count;
        while (lo < hi) {
            size_t mid = lo + (hi - lo) / 2;
            if (known[mid] < i) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        pos = lo; /* known[pos] je prvi indeks > i (svi su != i jer je temp[i] NaN) */

        /* Do per_side susjeda lijevo. */
        taken = 0;
        while (taken < per_side && pos > (size_t)taken) {
            size_t j = known[pos - 1 - (size_t)taken];
            double d = (double)(i - j);
            double w = 1.0 / (d + 1e-9);
            weight_sum += w;
            value_sum += w * temp[j];
            taken++;
        }

        /* Do per_side susjeda desno. */
        taken = 0;
        while (taken < per_side && pos + (size_t)taken < known_count) {
            size_t j = known[pos + (size_t)taken];
            double d = (double)(j - i);
            double w = 1.0 / (d + 1e-9);
            weight_sum += w;
            value_sum += w * temp[j];
            taken++;
        }

        if (weight_sum > 0.0) {
            out[i] = value_sum / weight_sum;
        }
    }

    free(known);
    fill_remaining_gaps(out, n);
    return 0;
}
