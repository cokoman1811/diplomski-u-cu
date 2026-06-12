#include "series.h"
#include "preprocessing.h"
#include "experiment.h"
#include "evaluation.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DEMO_CSV "data/raw/temperature_demo_cities.csv"
#define PROCESSED_CSV "data/processed/jena_temperature_48h.csv"
#define DEFAULT_CITY "Split"
#define RANDOM_SEED 42ULL
#define RESULTS_DIR "results"

static void print_usage(void) {
    printf("Diplomski projekt (C) - imputacija nedostajucih vrijednosti\n\n");
    printf("Naredbe:\n");
    printf("  diplomski --compare                      usporedi metode (zadano: jena_quick)\n");
    printf("  diplomski --experiment                   puni eksperiment (svi scenariji i rateovi)\n");
    printf("  diplomski --compare --source demo        koristi demo CSV (gradovi)\n");
    printf("  diplomski --compare --source demo --city Zagreb\n");
    printf("  diplomski --compare --missing-rate 0.3   udio uklonjenih vrijednosti\n\n");
    printf("Izvori (--source): jena_quick | processed | demo\n");
}

/* Ispis jednog retka tablice rezultata. */
static void print_metric_row(const char *name, Metrics m, int ok) {
    if (!ok) {
        printf("  %-22s %s\n", name, "[preskoceno: premalo poznatih tocaka]");
        return;
    }
    printf("  %-22s %10.4f %10.4f %10.4f\n", name, m.mae, m.rmse, m.r2);
}

static int run_compare(const char *source, const char *city, double missing_rate) {
    const char *path;
    const char *city_filter = NULL;
    const char *label_city = NULL;

    if (strcmp(source, "demo") == 0) {
        path = DEMO_CSV;
        city_filter = (city != NULL) ? city : DEFAULT_CITY;
        label_city = city_filter;
    } else if (strcmp(source, "jena_quick") == 0 || strcmp(source, "processed") == 0) {
        path = PROCESSED_CSV;
    } else {
        fprintf(stderr, "Nepoznat izvor: %s (koristi demo | jena_quick | processed)\n", source);
        return 1;
    }

    Series s = {0};
    if (series_load_csv(&s, path, city_filter) != 0) {
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

    size_t removed = create_missing_values(s.temp, n, missing_rate, RANDOM_SEED, damaged, mask);

    printf("\n");
    printf("======================================================================\n");
    printf("USPOREDBA METODA INTERPOLACIJE / IMPUTACIJE\n");
    printf("======================================================================\n");
    printf("Izvor:           %s\n", source);
    if (label_city) {
        printf("Grad:            %s\n", label_city);
    }
    printf("Zapisa:          %zu\n", n);
    printf("Scenarij:        random missing\n");
    printf("Obrisano (mask): %zu (%.0f%%)\n", removed, missing_rate * 100.0);
    printf("\n");
    printf("  %-22s %10s %10s %10s\n", "metoda", "MAE", "RMSE", "R2");
    printf("  ------------------------------------------------------------\n");

    exp_run_methods(&s, s.temp, damaged, mask, n, out, results);
    for (size_t i = 0; i < EXP_NUM_METHODS; i++) {
        print_metric_row(results[i].name, results[i].metrics, results[i].ok);
    }

    printf("\n");
    printf("Nizi MAE/RMSE = bolje. R2 blize 1 = bolje.\n\n");

    free(damaged);
    free(mask);
    free(out);
    series_free(&s);
    return 0;
}

int main(int argc, char **argv) {
    int do_compare = 0;
    int do_experiment = 0;
    const char *source = "jena_quick";
    const char *city = NULL;
    double missing_rate = 0.4;

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--compare") == 0) {
            do_compare = 1;
        } else if (strcmp(argv[i], "--experiment") == 0) {
            do_experiment = 1;
        } else if (strcmp(argv[i], "--source") == 0 && i + 1 < argc) {
            source = argv[++i];
        } else if (strcmp(argv[i], "--city") == 0 && i + 1 < argc) {
            city = argv[++i];
        } else if (strcmp(argv[i], "--missing-rate") == 0 && i + 1 < argc) {
            missing_rate = atof(argv[++i]);
        } else if (strcmp(argv[i], "--help") == 0 || strcmp(argv[i], "-h") == 0) {
            print_usage();
            return 0;
        } else {
            fprintf(stderr, "Nepoznat argument: %s\n", argv[i]);
            print_usage();
            return 1;
        }
    }

    if (do_experiment) {
        return exp_run_full(source, city, RESULTS_DIR);
    }

    if (!do_compare) {
        print_usage();
        return 0;
    }

    return run_compare(source, city, missing_rate);
}
