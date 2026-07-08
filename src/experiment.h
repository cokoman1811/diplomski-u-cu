#ifndef EXPERIMENT_H
#define EXPERIMENT_H

#include "evaluation.h"
#include "series.h"

#include <stddef.h>

#define EXP_NUM_METHODS 8

/* Scenarij umjetnog uklanjanja vrijednosti. */
typedef enum {
    EXP_SCENARIO_RANDOM = 0,
    EXP_SCENARIO_BLOCK = 1,
    EXP_SCENARIO_BLOCK_START = 2,
    EXP_SCENARIO_BLOCK_MIDDLE = 3,
    EXP_SCENARIO_BLOCK_END = 4
} ExpScenario;

#define EXP_NUM_SCENARIOS 5

typedef struct {
    const char *name;
    Metrics metrics;
    int ok;
} ExpMethodResult;

/* Opcijski filter za djelomicni eksperiment (--scenario / --missing-rate). */
typedef struct {
    int has_scenario;
    ExpScenario scenario;
    int has_rate;
    double missing_rate;
} ExpRunFilter;

/* Naziv scenarija za ispis i CSV. */
const char *exp_scenario_name(ExpScenario scenario);

/* Pozicija bloka: "none" za random/block, inace "start"/"middle"/"end". */
const char *exp_block_position_name(ExpScenario scenario);

/*
 * Parsira --scenario argument. Vraca 0 ako je valjan, inace -1.
 */
int exp_scenario_from_string(const char *text, ExpScenario *out);

/*
 * Kreira damaged niz i masku (original se ne mijenja).
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
 * Spremi reconstruction CSV s metapodacima eksperimenta.
 */
int exp_export_reconstruction(const char *results_dir, const char *method_name,
                              ExpScenario scenario, double missing_rate,
                              const Series *s, const double *original,
                              const double *damaged, const int *mask,
                              size_t n, double *out);

/*
 * Brza usporedba svih metoda (--compare).
 */
int exp_run_compare(const char *source, const char *city, ExpScenario scenario,
                    double missing_rate, int export_reconstruction,
                    const char *results_dir);

/*
 * Pun eksperiment: svi scenariji, missing rateovi 10-40%, sve metode.
 * filter == NULL ili prazni filter pokrece sve kombinacije.
 */
int exp_run_all(const char *source, const char *city, const char *results_dir,
                const ExpRunFilter *filter);

#endif /* EXPERIMENT_H */
