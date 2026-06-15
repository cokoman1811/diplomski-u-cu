#ifndef EXPERIMENT_H
#define EXPERIMENT_H

#include "evaluation.h"
#include "series.h"

#include <stddef.h>

#define EXP_NUM_METHODS 8

/* Scenarij umjetnog uklanjanja vrijednosti. */
typedef enum {
    EXP_SCENARIO_RANDOM = 0,
    EXP_SCENARIO_BLOCK = 1
} ExpScenario;

typedef struct {
    const char *name;
    Metrics metrics;
    int ok;
} ExpMethodResult;

/* Naziv scenarija za ispis i CSV ("random", "block"). */
const char *exp_scenario_name(ExpScenario scenario);

/*
 * Parsira --scenario argument. Vraca 0 ako je valjan, inace -1.
 */
int exp_scenario_from_string(const char *text, ExpScenario *out);

/*
 * Kreira damaged niz i masku (original se ne mijenja).
 * random — pojedinacne nasumicne rupice; block — kontinuirani blokovi.
 */
size_t exp_create_damage(ExpScenario scenario, const double *temp, size_t n,
                         double missing_rate, unsigned long long seed,
                         double *damaged, int *mask);

/*
 * Pokreni svih 8 metoda na istom damaged nizu i evaluiraj samo na mask[i]==1.
 */
int exp_run_methods(const Series *s, const double *original, const double *damaged,
                    const int *mask, size_t n, double *out, ExpMethodResult *results);

/*
 * Primjeni jednu metodu po imenu (npr. "linear_interpolation"). Vraca 0 ako uspjeh.
 */
int exp_apply_method(const char *method_name, const Series *s,
                     const double *damaged, size_t n, double *out);

/*
 * Spremi reconstruction CSV: index, original, damaged, reconstructed, mask.
 * Ime datoteke: results/reconstruction_{method}_{scenario}_{rate}.csv
 */
int exp_export_reconstruction(const char *results_dir, const char *method_name,
                              ExpScenario scenario, double missing_rate,
                              const Series *s, const double *original,
                              const double *damaged, const int *mask,
                              size_t n, double *out);

/*
 * Brza usporedba svih metoda (--compare).
 * Ako export_reconstruction != 0, sprema CSV za metode iz konfiguracije (linear).
 */
int exp_run_compare(const char *source, const char *city, ExpScenario scenario,
                    double missing_rate, int export_reconstruction,
                    const char *results_dir);

/*
 * Pun eksperiment: scenariji random + block, missing rateovi 10-50%,
 * ispis u terminal i CSV u results_dir.
 */
int exp_run_full(const char *source, const char *city, const char *results_dir);

#endif /* EXPERIMENT_H */
