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

int exp_run_methods(const Series *s, const double *original, const double *damaged,
                    const int *mask, size_t n, double *out, ExpMethodResult *results) {
    if (!s || !original || !damaged || !mask || !out || !results) {
        return 1;
    }

    forward_fill(damaged, n, out);
    results[0].name = "forward_fill";
    results[0].ok = 1;
    results[0].metrics = evaluate_reconstruction(original, out, mask, n);

    linear_interpolation(damaged, n, out);
    results[1].name = "linear_interpolation";
    results[1].ok = 1;
    results[1].metrics = evaluate_reconstruction(original, out, mask, n);

    time_interpolation(damaged, n, s->epoch, out);
    results[2].name = "time_interpolation";
    results[2].ok = 1;
    results[2].metrics = evaluate_reconstruction(original, out, mask, n);

    results[3].name = "cubic_interpolation";
    if (cubic_interpolation(damaged, n, out) == 0) {
        results[3].ok = 1;
        results[3].metrics = evaluate_reconstruction(original, out, mask, n);
    } else {
        results[3].ok = 0;
        results[3].metrics = (Metrics){0};
    }

    results[4].name = "spline_interpolation";
    if (spline_interpolation(damaged, n, out) == 0) {
        results[4].ok = 1;
        results[4].metrics = evaluate_reconstruction(original, out, mask, n);
    } else {
        results[4].ok = 0;
        results[4].metrics = (Metrics){0};
    }

    results[5].name = "knn";
    if (knn_imputation_upgraded(s, damaged, NULL, out) == 0) {
        results[5].ok = 1;
        results[5].metrics = evaluate_reconstruction(original, out, mask, n);
    } else {
        results[5].ok = 0;
        results[5].metrics = (Metrics){0};
    }

    results[6].name = "decision_tree";
    if (decision_tree_imputation(s, damaged, out) == 0) {
        results[6].ok = 1;
        results[6].metrics = evaluate_reconstruction(original, out, mask, n);
    } else {
        results[6].ok = 0;
        results[6].metrics = (Metrics){0};
    }

    results[7].name = "random_forest";
    if (rf_imputation(s, damaged, out) == 0) {
        results[7].ok = 1;
        results[7].metrics = evaluate_reconstruction(original, out, mask, n);
    } else {
        results[7].ok = 0;
        results[7].metrics = (Metrics){0};
    }

    return 0;
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

static void write_csv_header(FILE *fp, const char *header) {
    fprintf(fp, "%s\n", header);
}

static int export_reconstruction(const char *path, const double *original,
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

static int export_random_forest_reconstruction(const Series *s, const double *original,
                                               const double *damaged, const int *mask,
                                               size_t n, const char *scenario,
                                               const char *results_dir, double *out) {
    if (rf_imputation(s, damaged, out) != 0) {
        return 1;
    }

    char path[512];
    snprintf(path, sizeof(path), "%s/reconstruction_random_forest_%s_0.20.csv",
             results_dir, scenario);
    return export_reconstruction(path, original, damaged, out, mask, n);
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

    const char *scenarios[] = {"random", "block"};
    for (size_t sc = 0; sc < 2; sc++) {
        for (size_t ri = 0; ri < EXP_NUM_RATES; ri++) {
            double rate = EXP_MISSING_RATES[ri];
            size_t removed;

            if (sc == 0) {
                removed = create_missing_values(s.temp, n, rate, RANDOM_SEED, damaged, mask);
            } else {
                removed = create_block_missing_values(s.temp, n, PREPROC_BLOCK_SIZE_2H_10MIN,
                                                      rate, RANDOM_SEED, damaged, mask);
            }

            (void)removed;
            exp_run_methods(&s, s.temp, damaged, mask, n, out, results);

            for (size_t mi = 0; mi < EXP_NUM_METHODS; mi++) {
                print_exp_row(scenarios[sc], rate, &results[mi]);
                if (!results[mi].ok) {
                    continue;
                }

                fprintf(fp_main, "%s,%.2f,%s,%.6f,%.6f,%.6f,%zu\n",
                        scenarios[sc], rate, results[mi].name,
                        results[mi].metrics.mae, results[mi].metrics.rmse,
                        results[mi].metrics.r2, results[mi].metrics.count);

                fprintf(fp_mae, "%s,%.6f,%s,%.2f\n",
                        results[mi].name, results[mi].metrics.mae,
                        scenarios[sc], rate);

                fprintf(fp_err, "%.2f,%s,%.6f,%.6f,%.6f\n",
                        rate, results[mi].name,
                        results[mi].metrics.mae, results[mi].metrics.rmse,
                        results[mi].metrics.r2);
            }

            /* Rekonstrukcija za graf: random_forest pri 20% missing rate. */
            if (fabs(rate - 0.20) < 1e-9) {
                export_random_forest_reconstruction(&s, s.temp, damaged, mask, n,
                                                    scenarios[sc], results_dir, out);
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
    printf("  %s/reconstruction_random_forest_*_0.20.csv\n", results_dir);
    printf("\n");

    free(damaged);
    free(mask);
    free(out);
    series_free(&s);
    return 0;
}
