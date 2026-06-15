#include "experiment.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define RESULTS_DIR "results"

static void print_usage(void) {
    printf("Diplomski projekt (C) - imputacija nedostajucih vrijednosti\n\n");
    printf("Naredbe:\n");
    printf("  diplomski --compare                              usporedi metode (random, 40%%)\n");
    printf("  diplomski --compare --scenario block             block missing (kvar senzora)\n");
    printf("  diplomski --compare --scenario random            pojedinacne rupice (zadano)\n");
    printf("  diplomski --compare --missing-rate 0.2 --export  + CSV za graf (linear)\n");
    printf("  diplomski --experiment                           puni eksperiment -> CSV\n");
    printf("  diplomski --compare --source demo --city Split\n\n");
    printf("Scenariji (--scenario): random | block\n");
    printf("Izvori (--source): jena_quick | processed | demo\n");
}

int main(int argc, char **argv) {
    int do_compare = 0;
    int do_experiment = 0;
    int do_export = 0;
    const char *source = "jena_quick";
    const char *city = NULL;
    double missing_rate = 0.4;
    ExpScenario scenario = EXP_SCENARIO_RANDOM;

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--compare") == 0) {
            do_compare = 1;
        } else if (strcmp(argv[i], "--experiment") == 0) {
            do_experiment = 1;
        } else if (strcmp(argv[i], "--export") == 0) {
            do_export = 1;
        } else if (strcmp(argv[i], "--source") == 0 && i + 1 < argc) {
            source = argv[++i];
        } else if (strcmp(argv[i], "--city") == 0 && i + 1 < argc) {
            city = argv[++i];
        } else if (strcmp(argv[i], "--missing-rate") == 0 && i + 1 < argc) {
            missing_rate = atof(argv[++i]);
        } else if (strcmp(argv[i], "--scenario") == 0 && i + 1 < argc) {
            if (exp_scenario_from_string(argv[++i], &scenario) != 0) {
                fprintf(stderr, "Nepoznat scenarij (koristi random | block)\n");
                return 1;
            }
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

    return exp_run_compare(source, city, scenario, missing_rate, do_export, RESULTS_DIR);
}
