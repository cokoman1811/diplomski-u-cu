#include "experiment.h"

#include "interpolation.h"
#include "knn_upgraded.h"
#include "decision_tree.h"
#include "rf_methods.h"
#include "preprocessing.h"

#include <errno.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
#include <direct.h>
#else
#include <sys/stat.h>
#endif

#define DEMO_CSV "data/raw/temperature_demo_cities.csv"
#define PROCESSED_CSV "data/processed/jena_temperature_48h.csv"
#define DEFAULT_CITY "Split"
#define RANDOM_SEED 42ULL

static const double EXP_MISSING_RATES[] = {0.10, 0.20, 0.30, 0.40, 0.50};
static const size_t EXP_NUM_RATES = sizeof(EXP_MISSING_RATES) / sizeof(EXP_MISSING_RATES[0]);

/* Missing rate pri kojem se automatski sprema reconstruction CSV u --experiment. */
#define EXP_RECON_SNAPSHOT_RATE 0.20

/*
 * Metode za koje se sprema reconstruction CSV (lako dodati vise imena).
 * Za graf original vs rekonstruirano koristi npr. linear_interpolation.
 */
static const char *EXP_RECON_EXPORT_METHODS[] = {
    "linear_interpolation",
};
static const size_t EXP_NUM_RECON_EXPORTS =
    sizeof(EXP_RECON_EXPORT_METHODS) / sizeof(EXP_RECON_EXPORT_METHODS[0]);

typedef int (*ExpApplyFn)(const Series *s, const double *damaged, size_t n, double *out);

typedef struct {
    const char *name;
    ExpApplyFn apply;
} ExpMethodEntry;

static int apply_forward_fill(const Series *s, const double *damaged, size_t n, double *out) {
    (void)s;
    forward_fill(damaged, n, out);
    return 0;
}

static int apply_linear(const Series *s, const double *damaged, size_t n, double *out) {
    (void)s;
    linear_interpolation(damaged, n, out);
    return 0;
}

static int apply_time(const Series *s, const double *damaged, size_t n, double *out) {
    time_interpolation(damaged, n, s->epoch, out);
    return 0;
}

static int apply_cubic(const Series *s, const double *damaged, size_t n, double *out) {
    (void)s;
    return cubic_interpolation(damaged, n, out);
}

static int apply_spline(const Series *s, const double *damaged, size_t n, double *out) {
    (void)s;
    return spline_interpolation(damaged, n, out);
}

static int apply_knn(const Series *s, const double *damaged, size_t n, double *out) {
    (void)n;
    return knn_imputation_upgraded(s, damaged, NULL, out);
}

static int apply_decision_tree(const Series *s, const double *damaged, size_t n, double *out) {
    (void)n;
    return decision_tree_imputation(s, damaged, out);
}

static int apply_random_forest(const Series *s, const double *damaged, size_t n, double *out) {
    (void)n;
    return rf_imputation(s, damaged, out);
}

static const ExpMethodEntry EXP_METHOD_TABLE[] = {
    {"forward_fill", apply_forward_fill},
    {"linear_interpolation", apply_linear},
    {"time_interpolation", apply_time},
    {"cubic_interpolation", apply_cubic},
    {"spline_interpolation", apply_spline},
    {"knn", apply_knn},
    {"decision_tree", apply_decision_tree},
    {"random_forest", apply_random_forest},
};

static const size_t EXP_METHOD_TABLE_SIZE =
    sizeof(EXP_METHOD_TABLE) / sizeof(EXP_METHOD_TABLE[0]);

const char *exp_scenario_name(ExpScenario scenario) {
    return (scenario == EXP_SCENARIO_BLOCK) ? "block" : "random";
}

int exp_scenario_from_string(const char *text, ExpScenario *out) {
    if (!text || !out) {
        return -1;
    }
    if (strcmp(text, "random") == 0) {
        *out = EXP_SCENARIO_RANDOM;
        return 0;
    }
    if (strcmp(text, "block") == 0) {
        *out = EXP_SCENARIO_BLOCK;
        return 0;
    }
    return -1;
}

size_t exp_create_damage(ExpScenario scenario, const double *temp, size_t n,
                         double missing_rate, unsigned long long seed,
                         double *damaged, int *mask) {
    if (scenario == EXP_SCENARIO_BLOCK) {
        return create_block_missing_values(temp, n, PREPROC_BLOCK_SIZE_2H_10MIN,
                                           missing_rate, seed, damaged, mask);
    }
    return create_missing_values(temp, n, missing_rate, seed, damaged, mask);
}

static int ensure_results_dir(const char *path) {
#ifdef _WIN32
    if (_mkdir(path) == 0) {
        return 0;
    }
#else
    if (mkdir(path, 0755) == 0) {
        return 0;
    }
#endif
    return (errno == EEXIST) ? 0 : -1;
}

static int load_series(const char *source, const char *city, Series *s,
                       const char **label_city) {
    const char *path;
    const char *city_filter = NULL;

    if (strcmp(source, "demo") == 0) {
        path = DEMO_CSV;
        city_filter = (city != NULL) ? city : DEFAULT_CITY;
        *label_city = city_filter;
    } else if (strcmp(source, "jena_quick") == 0 || strcmp(source, "processed") == 0) {
        path = PROCESSED_CSV;
        *label_city = NULL;
    } else {
        fprintf(stderr, "Nepoznat izvor: %s (koristi demo | jena_quick | processed)\n", source);
        return 1;
    }

    if (series_load_csv(s, path, city_filter) != 0) {
        return 1;
    }
    return 0;
}

static const ExpMethodEntry *find_method(const char *name) {
    for (size_t i = 0; i < EXP_METHOD_TABLE_SIZE; i++) {
        if (strcmp(EXP_METHOD_TABLE[i].name, name) == 0) {
            return &EXP_METHOD_TABLE[i];
        }
    }
    return NULL;
}

int exp_apply_method(const char *method_name, const Series *s,
                     const double *damaged, size_t n, double *out) {
    const ExpMethodEntry *entry = find_method(method_name);
    if (!entry) {
        return 1;
    }
    return entry->apply(s, damaged, n, out);
}

int exp_run_methods(const Series *s, const double *original, const double *damaged,
                    const int *mask, size_t n, double *out, ExpMethodResult *results) {
    if (!s || !original || !damaged || !mask || !out || !results) {
        return 1;
    }
    if (EXP_METHOD_TABLE_SIZE != EXP_NUM_METHODS) {
        fprintf(stderr, "Greska: tablica metoda i EXP_NUM_METHODS se ne podudaraju.\n");
        return 1;
    }

    for (size_t i = 0; i < EXP_METHOD_TABLE_SIZE; i++) {
        results[i].name = EXP_METHOD_TABLE[i].name;
        if (EXP_METHOD_TABLE[i].apply(s, damaged, n, out) == 0) {
            results[i].ok = 1;
            results[i].metrics = evaluate_reconstruction(original, out, mask, n);
        } else {
            results[i].ok = 0;
            results[i].metrics = (Metrics){0};
        }
    }
    return 0;
}

static void write_csv_header(FILE *fp, const char *header) {
    fprintf(fp, "%s\n", header);
}

static int write_reconstruction_csv(const char *path, const double *original,
                                  const double *damaged, const double *reconstructed,
                                  const int *mask, size_t n) {
    FILE *fp = fopen(path, "w");
    if (!fp) {
        fprintf(stderr, "Ne mogu otvoriti %s za pisanje.\n", path);
        return 1;
    }

    write_csv_header(fp, "index,original,damaged,reconstructed,mask");
    for (size_t i = 0; i < n; i++) {
        fprintf(fp, "%zu,%.6f,", i, original[i]);
        if (isnan(damaged[i])) {
            fprintf(fp, ",");
        } else {
            fprintf(fp, "%.6f,", damaged[i]);
        }
        if (isnan(reconstructed[i])) {
            fprintf(fp, ",");
        } else {
            fprintf(fp, "%.6f,", reconstructed[i]);
        }
        fprintf(fp, "%d\n", mask[i]);
    }

    fclose(fp);
    return 0;
}

static void reconstruction_path(char *buf, size_t buflen, const char *results_dir,
                              const char *method_name, ExpScenario scenario,
                              double missing_rate) {
    snprintf(buf, buflen, "%s/reconstruction_%s_%s_%.2f.csv",
             results_dir, method_name, exp_scenario_name(scenario), missing_rate);
}

int exp_export_reconstruction(const char *results_dir, const char *method_name,
                              ExpScenario scenario, double missing_rate,
                              const Series *s, const double *original,
                              const double *damaged, const int *mask,
                              size_t n, double *out) {
    if (!results_dir || !method_name || !s || !original || !damaged || !mask || !out) {
        return 1;
    }
    if (find_method(method_name) == NULL) {
        fprintf(stderr, "Nepoznata metoda za export: %s\n", method_name);
        return 1;
    }
    if (ensure_results_dir(results_dir) != 0) {
        fprintf(stderr, "Ne mogu kreirati mapu %s\n", results_dir);
        return 1;
    }
    if (exp_apply_method(method_name, s, damaged, n, out) != 0) {
        fprintf(stderr, "Metoda %s nije uspjela za reconstruction export.\n", method_name);
        return 1;
    }

    char path[512];
    reconstruction_path(path, sizeof(path), results_dir, method_name, scenario, missing_rate);
    return write_reconstruction_csv(path, original, damaged, out, mask, n);
}

static void export_configured_reconstructions(const char *results_dir, ExpScenario scenario,
                                              double missing_rate, const Series *s,
                                              const double *original, const double *damaged,
                                              const int *mask, size_t n, double *out) {
    for (size_t i = 0; i < EXP_NUM_RECON_EXPORTS; i++) {
        if (exp_export_reconstruction(results_dir, EXP_RECON_EXPORT_METHODS[i],
                                    scenario, missing_rate, s, original, damaged, mask, n,
                                    out) == 0) {
            char path[512];
            reconstruction_path(path, sizeof(path), results_dir,
                                  EXP_RECON_EXPORT_METHODS[i], scenario, missing_rate);
            printf("  reconstruction: %s\n", path);
        }
    }
}

static void print_exp_row(const char *scenario, double missing_rate,
                          const ExpMethodResult *r) {
    if (!r->ok) {
        printf("  %-8s %5.0f%%  %-22s  [preskoceno]\n",
               scenario, missing_rate * 100.0, r->name);
        return;
    }
    printf("  %-8s %5.0f%%  %-22s %10.4f %10.4f %10.4f  (n=%zu)\n",
           scenario, missing_rate * 100.0, r->name,
           r->metrics.mae, r->metrics.rmse, r->metrics.r2, r->metrics.count);
}

int exp_run_compare(const char *source, const char *city, ExpScenario scenario,
                    double missing_rate, int export_reconstruction,
                    const char *results_dir) {
    Series s = {0};
    const char *label_city = NULL;

    if (load_series(source, city, &s, &label_city) != 0) {
        return 1;
    }

    size_t n = s.n;
    double *damaged = (double *)malloc(n * sizeof(double));
    int *mask = (int *)malloc(n * sizeof(int));
    double *out = (double *)malloc(n * sizeof(double));
    ExpMethodResult results[EXP_NUM_METHODS];

    if (!damaged || !mask || !out) {
        fprintf(stderr, "Greska: nedostatak memorije.\n");
        free(damaged);
        free(mask);
        free(out);
        series_free(&s);
        return 1;
    }

    size_t removed = exp_create_damage(scenario, s.temp, n, missing_rate, RANDOM_SEED,
                                       damaged, mask);

    printf("\n");
    printf("======================================================================\n");
    printf("USPOREDBA METODA INTERPOLACIJE / IMPUTACIJE\n");
    printf("======================================================================\n");
    printf("Izvor:           %s\n", source);
    if (label_city) {
        printf("Grad:            %s\n", label_city);
    }
    printf("Zapisa:          %zu\n", n);
    printf("Scenarij:        %s missing\n", exp_scenario_name(scenario));
    if (scenario == EXP_SCENARIO_BLOCK) {
        printf("Velicina bloka:  %d uzoraka (2 h pri 10-min intervalu)\n",
               PREPROC_BLOCK_SIZE_2H_10MIN);
    }
    printf("Obrisano (mask): %zu (%.0f%%)\n", removed, missing_rate * 100.0);
    printf("\n");
    printf("  %-22s %10s %10s %10s\n", "metoda", "MAE", "RMSE", "R2");
    printf("  ------------------------------------------------------------\n");

    exp_run_methods(&s, s.temp, damaged, mask, n, out, results);
    for (size_t i = 0; i < EXP_NUM_METHODS; i++) {
        if (!results[i].ok) {
            printf("  %-22s %s\n", results[i].name, "[preskoceno: premalo poznatih tocaka]");
            continue;
        }
        printf("  %-22s %10.4f %10.4f %10.4f\n",
               results[i].name, results[i].metrics.mae,
               results[i].metrics.rmse, results[i].metrics.r2);
    }

    if (export_reconstruction && results_dir) {
        printf("\nExport reconstruction CSV:\n");
        export_configured_reconstructions(results_dir, scenario, missing_rate,
                                          &s, s.temp, damaged, mask, n, out);
    }

    printf("\nNizi MAE/RMSE = bolje. R2 blize 1 = bolje.\n\n");

    free(damaged);
    free(mask);
    free(out);
    series_free(&s);
    return 0;
}

int exp_run_full(const char *source, const char *city, const char *results_dir) {
    Series s = {0};
    const char *label_city = NULL;

    if (load_series(source, city, &s, &label_city) != 0) {
        return 1;
    }

    if (ensure_results_dir(results_dir) != 0) {
        fprintf(stderr, "Ne mogu kreirati mapu %s\n", results_dir);
        series_free(&s);
        return 1;
    }

    size_t n = s.n;
    double *damaged = (double *)malloc(n * sizeof(double));
    int *mask = (int *)malloc(n * sizeof(int));
    double *out = (double *)malloc(n * sizeof(double));
    ExpMethodResult results[EXP_NUM_METHODS];

    if (!damaged || !mask || !out) {
        fprintf(stderr, "Greska: nedostatak memorije.\n");
        free(damaged);
        free(mask);
        free(out);
        series_free(&s);
        return 1;
    }

    char main_csv[512];
    char mae_csv[512];
    char error_csv[512];
    snprintf(main_csv, sizeof(main_csv), "%s/experiment_results.csv", results_dir);
    snprintf(mae_csv, sizeof(mae_csv), "%s/mae_by_method.csv", results_dir);
    snprintf(error_csv, sizeof(error_csv), "%s/error_vs_missing_rate.csv", results_dir);

    FILE *fp_main = fopen(main_csv, "w");
    FILE *fp_mae = fopen(mae_csv, "w");
    FILE *fp_err = fopen(error_csv, "w");
    if (!fp_main || !fp_mae || !fp_err) {
        fprintf(stderr, "Ne mogu otvoriti CSV datoteke u %s\n", results_dir);
        fclose(fp_main);
        fclose(fp_mae);
        fclose(fp_err);
        free(damaged);
        free(mask);
        free(out);
        series_free(&s);
        return 1;
    }

    write_csv_header(fp_main, "scenario,missing_rate,method,mae,rmse,r2,count");
    write_csv_header(fp_mae, "method,mae,scenario,missing_rate");
    write_csv_header(fp_err, "missing_rate,method,mae,rmse,r2");

    printf("\n");
    printf("======================================================================\n");
    printf("EKSPERIMENT — USPOREDBA SVIH METODA\n");
    printf("======================================================================\n");
    printf("Izvor:      %s\n", source);
    if (label_city) {
        printf("Grad:       %s\n", label_city);
    }
    printf("Zapisa:     %zu\n", n);
    printf("Scenariji:  random, block (block_size=%d)\n", PREPROC_BLOCK_SIZE_2H_10MIN);
    printf("Rezultati:  %s/\n", results_dir);
    printf("\n");
    printf("  %-8s %5s  %-22s %10s %10s %10s\n",
           "scenario", "rate", "method", "MAE", "RMSE", "R2");
    printf("  ------------------------------------------------------------------------------\n");

    const ExpScenario scenarios[] = {EXP_SCENARIO_RANDOM, EXP_SCENARIO_BLOCK};
    for (size_t sc = 0; sc < 2; sc++) {
        for (size_t ri = 0; ri < EXP_NUM_RATES; ri++) {
            double rate = EXP_MISSING_RATES[ri];
            size_t removed = exp_create_damage(scenarios[sc], s.temp, n, rate, RANDOM_SEED,
                                               damaged, mask);
            (void)removed;

            exp_run_methods(&s, s.temp, damaged, mask, n, out, results);

            for (size_t mi = 0; mi < EXP_NUM_METHODS; mi++) {
                print_exp_row(exp_scenario_name(scenarios[sc]), rate, &results[mi]);
                if (!results[mi].ok) {
                    continue;
                }

                fprintf(fp_main, "%s,%.2f,%s,%.6f,%.6f,%.6f,%zu\n",
                        exp_scenario_name(scenarios[sc]), rate, results[mi].name,
                        results[mi].metrics.mae, results[mi].metrics.rmse,
                        results[mi].metrics.r2, results[mi].metrics.count);

                fprintf(fp_mae, "%s,%.6f,%s,%.2f\n",
                        results[mi].name, results[mi].metrics.mae,
                        exp_scenario_name(scenarios[sc]), rate);

                fprintf(fp_err, "%.2f,%s,%.6f,%.6f,%.6f\n",
                        rate, results[mi].name,
                        results[mi].metrics.mae, results[mi].metrics.rmse,
                        results[mi].metrics.r2);
            }

            if (fabs(rate - EXP_RECON_SNAPSHOT_RATE) < 1e-9) {
                export_configured_reconstructions(results_dir, scenarios[sc], rate,
                                                  &s, s.temp, damaged, mask, n, out);
            }
        }
    }

    fclose(fp_main);
    fclose(fp_mae);
    fclose(fp_err);

    printf("\n");
    printf("CSV spremljen:\n");
    printf("  %s\n", main_csv);
    printf("  %s\n", mae_csv);
    printf("  %s\n", error_csv);
    printf("  %s/reconstruction_*_*.csv (linear pri 20%%)\n", results_dir);
    printf("\n");

    free(damaged);
    free(mask);
    free(out);
    series_free(&s);
    return 0;
}
