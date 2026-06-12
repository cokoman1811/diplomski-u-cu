#ifndef EXPERIMENT_H
#define EXPERIMENT_H

#include "evaluation.h"
#include "series.h"

#include <stddef.h>

#define EXP_NUM_METHODS 8

typedef struct {
    const char *name;
    Metrics metrics;
    int ok;
} ExpMethodResult;

/*
 * Pokreni svih 8 metoda na istom damaged nizu i evaluiraj samo na mask[i]==1.
 * out je radni buffer (velicina n). results mora imati EXP_NUM_METHODS elemenata.
 */
int exp_run_methods(const Series *s, const double *original, const double *damaged,
                    const int *mask, size_t n, double *out, ExpMethodResult *results);

/*
 * Pun eksperiment: scenariji random + block, missing rateovi 10-50%,
 * ispis u terminal i CSV u results_dir (kreira mapu ako ne postoji).
 */
int exp_run_full(const char *source, const char *city, const char *results_dir);

#endif /* EXPERIMENT_H */
