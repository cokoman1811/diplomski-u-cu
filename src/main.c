#include "experiment.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define RESULTS_DIR "results"

static void print_usage(void) {
    printf("Diplomski projekt (C) - imputacija nedostajucih vrijednosti\n\n");
    printf("Naredbe:\n");
    printf("  diplomski --compare                              usporedi metode (random, 40%%)\n");
    printf("  diplomski --compare --scenario block_start       block na pocetku niza\n");
    printf("  diplomski --compare --missing-rate 0.2 --export  + CSV za graf (linear)\n");
    printf("  diplomski --experiment-all                       puni eksperiment -> CSV\n");
    printf("  diplomski --experiment                             alias za --experiment-all\n");
    printf("  diplomski --experiment-all --scenario random --missing-rate 0.20\n");
    printf("  diplomski --compare --source demo --city Split\n\n");
    printf("Scenariji (--scenario): random | block | block_start | block_middle | block_end\n");
    printf("Missing rate (--missing-rate): 0.10 | 0.20 | 0.30 | 0.40\n");
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
    ExpRunFilter filter = {0};

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--compare") == 0) {
            do_compare = 1;
        } else if (strcmp(argv[i], "--experiment") == 0 ||
                   strcmp(argv[i], "--experiment-all") == 0) {
            do_experiment = 1;
        } else if (strcmp(argv[i], "--export") == 0) {
            do_export = 1;
        } else if (strcmp(argv[i], "--source") == 0 && i + 1 < argc) {
            source = argv[++i];
        } else if (strcmp(argv[i], "--city") == 0 && i + 1 < argc) {
            city = argv[++i];
        } else if (strcmp(argv[i], "--missing-rate") == 0 && i + 1 < argc) {
            missing_rate = atof(argv[++i]);
            filter.has_rate = 1;
            filter.missing_rate = missing_rate;
        } else if (strcmp(argv[i], "--scenario") == 0 && i + 1 < argc) {
            if (exp_scenario_from_string(argv[++i], &scenario) != 0) {
                fprintf(stderr,
                        "Nepoznat scenarij (koristi random | block | block_start | "
                        "block_middle | block_end)\n");
                return 1;
            }
            filter.has_scenario = 1;
            filter.scenario = scenario;
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
        const ExpRunFilter *filter_ptr = NULL;
        if (filter.has_scenario || filter.has_rate) {
            filter_ptr = &filter;
        }
        return exp_run_all(source, city, RESULTS_DIR, filter_ptr);
    }

    if (!do_compare) {
        print_usage();
        return 0;
    }

    return exp_run_compare(source, city, scenario, missing_rate, do_export, RESULTS_DIR);
}
