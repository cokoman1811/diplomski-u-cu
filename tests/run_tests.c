/*
 * Testovi za C verziju diplomskog (preslikano iz diplomski-kopija/cpp/tests).
 * Vlastiti mini-harness — bez vanjskih biblioteka (bez pytest-a).
 */

#include "series.h"
#include "preprocessing.h"
#include "interpolation.h"
#include "knn_methods.h"
#include "knn_upgraded.h"
#include "rf_methods.h"
#include "evaluation.h"

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define JENA_INTERVAL_MINUTES 10
#define QUICK_SAMPLE_HOURS 48
#define DEMO_CSV "data/raw/temperature_demo_cities.csv"

static int g_failures = 0;
static int g_checks = 0;

static void check(int condition, const char *message) {
    g_checks++;
    if (!condition) {
        g_failures++;
        printf("  [FAIL] %s\n", message);
    } else {
        printf("  [ok]   %s\n", message);
    }
}

static void check_near(double a, double b, double tol, const char *message) {
    check(fabs(a - b) <= tol, message);
}

/* Jednostavan PRNG za sinteticki niz (isti obrazac kao C++ generate_synthetic_series). */
static unsigned int synth_rng_state = 7u;

static unsigned int synth_rng_next(void) {
    synth_rng_state ^= synth_rng_state << 13;
    synth_rng_state ^= synth_rng_state >> 17;
    synth_rng_state ^= synth_rng_state << 5;
    return synth_rng_state;
}

static double synth_noise(void) {
    /* Aproksimacija N(0, 0.4) preko uniformnog [-1, 1]. */
    double u = (double)synth_rng_next() / 4294967295.0;
    return (u * 2.0 - 1.0) * 0.4;
}

static int generate_synthetic_series(Series *s, int hours) {
    int samples = hours * 60 / JENA_INTERVAL_MINUTES;
    if (samples < 2 || series_alloc(s, (size_t)samples) != 0) {
        return 1;
    }

    synth_rng_state = 7u;
    const long long start_epoch = 1230768600LL; /* 2009-01-01 00:10:00 UTC */
    const long long step = (long long)JENA_INTERVAL_MINUTES * 60LL;
    const double pi = 3.14159265358979323846;

    for (int i = 0; i < samples; i++) {
        double hours_elapsed = (i * JENA_INTERVAL_MINUTES) / 60.0;
        double daily = 6.0 * sin(2.0 * pi * (hours_elapsed - 9.0) / 24.0);
        double base = 2.0;
        double trend = 0.01 * (double)i;
        s->temp[i] = base + daily + trend + synth_noise();
        s->epoch[i] = start_epoch + (long long)i * step;
        s->hour[i] = (int)hours_elapsed % 24;
        s->yday[i] = 1;
    }
    return 0;
}

/* Mali niz s rupama — ekvivalent SAMPLE_SERIES iz test_ml_methods.py. */
static int build_sample_series(Series *s) {
    if (series_alloc(s, 8) != 0) {
        return 1;
    }

    const double vals[] = {10.0, 11.0, NAN, 13.0, NAN, 15.0, 16.0, 17.0};
    const long long base_epoch = 1704067200LL; /* 2024-01-01 00:00:00 UTC */

    for (size_t i = 0; i < 8; i++) {
        s->temp[i] = vals[i];
        s->epoch[i] = base_epoch + (long long)i * 3600LL;
        s->hour[i] = (int)i;
        s->yday[i] = 1;
    }
    return 0;
}

static int count_nan(const double *temp, size_t n) {
    int count = 0;
    for (size_t i = 0; i < n; i++) {
        if (isnan(temp[i])) {
            count++;
        }
    }
    return count;
}

/*
 * test_knn provjerava:
 *   - funkcija vraca uspjeh (0)
 *   - poznate vrijednosti ostaju iste
 *   - NaN mjesta su popunjena, u out nema NaN
 *   - damaged niz (sample.temp) nije mutiran
 */
static void test_knn(void) {
    printf("\n== KNN imputacija ==\n");

    Series sample = {0};
    if (build_sample_series(&sample) != 0) {
        check(0, "alokacija sample niza");
        return;
    }

    double out[8];
    int ok = knn_imputation(&sample, sample.temp, 3, out);
    check(ok == 0, "knn_imputation uspjeh");

    check(sample.n == 8, "isti broj zapisa");
    check(count_nan(out, 8) == 0, "nema NaN nakon imputacije");

    int known_unchanged = 1;
    for (size_t i = 0; i < sample.n; i++) {
        if (!isnan(sample.temp[i]) && out[i] != sample.temp[i]) {
            known_unchanged = 0;
            break;
        }
    }
    check(known_unchanged, "poznate vrijednosti nepromijenjene");

    check_near(out[2], 12.0, 2.0, "rupa na poziciji 2 ~ 12");
    check_near(out[4], 14.0, 2.0, "rupa na poziciji 4 ~ 14");
    check(isnan(sample.temp[2]), "original i dalje ima NaN (nije mutiran)");

    series_free(&sample);
}

/*
 * test_knn_upgraded provjerava:
 *   - funkcija vraca uspjeh (0)
 *   - poznate vrijednosti ostaju iste
 *   - NaN mjesta su popunjena (nema NaN u out)
 *   - damaged niz nije mutiran
 *   - radi na malom vremenskom nizu (8 satnih zapisa)
 */
static void test_knn_upgraded(void) {
    printf("\n== KNN upgraded imputacija ==\n");

    Series sample = {0};
    if (build_sample_series(&sample) != 0) {
        check(0, "alokacija sample niza");
        return;
    }

    double out[8];
    KnnUpgradedConfig cfg = knn_upgraded_default();
    cfg.n_neighbors = 3;
    cfg.weight_hour = 3.0;

    int ok = knn_imputation_upgraded(&sample, sample.temp, &cfg, out);
    check(ok == 0, "knn_imputation_upgraded uspjeh");
    check(count_nan(out, 8) == 0, "nema NaN nakon imputacije");

    int known_unchanged = 1;
    for (size_t i = 0; i < sample.n; i++) {
        if (!isnan(sample.temp[i]) && out[i] != sample.temp[i]) {
            known_unchanged = 0;
            break;
        }
    }
    check(known_unchanged, "poznate vrijednosti nepromijenjene");

    check(!isnan(out[2]), "NaN na poziciji 2 popunjen");
    check(!isnan(out[4]), "NaN na poziciji 4 popunjen");
    check_near(out[2], 12.0, 2.0, "rupa na poziciji 2 ~ 12");
    check_near(out[4], 14.0, 2.0, "rupa na poziciji 4 ~ 14");
    check(isnan(sample.temp[2]), "original i dalje ima NaN (nije mutiran)");

    series_free(&sample);
}

static void test_rf(void) {
    printf("\n== Random Forest imputacija ==\n");

    Series sample = {0};
    if (build_sample_series(&sample) != 0) {
        check(0, "alokacija sample niza");
        return;
    }

    double out[8];
    int ok = rf_imputation(&sample, sample.temp, out);
    check(ok == 0, "rf_imputation uspjeh");
    check(count_nan(out, 8) == 0, "nema NaN nakon imputacije");

    int known_unchanged = 1;
    for (size_t i = 0; i < sample.n; i++) {
        if (!isnan(sample.temp[i]) && out[i] != sample.temp[i]) {
            known_unchanged = 0;
            break;
        }
    }
    check(known_unchanged, "poznate vrijednosti nepromijenjene");
    check_near(out[2], 12.0, 4.0, "rupa na poziciji 2 u razumnom rasponu");
    check_near(out[4], 14.0, 4.0, "rupa na poziciji 4 u razumnom rasponu");

    series_free(&sample);
}

static void test_preprocessing(void) {
    printf("\n== Preprocessing (create_missing_values) ==\n");

    Series series = {0};
    if (generate_synthetic_series(&series, QUICK_SAMPLE_HOURS) != 0) {
        check(0, "generiranje sintetickog niza");
        return;
    }

    size_t n = series.n;
    double *damaged = (double *)malloc(n * sizeof(double));
    int *mask = (int *)malloc(n * sizeof(int));
    if (!damaged || !mask) {
        check(0, "alokacija memorije");
        free(damaged);
        free(mask);
        series_free(&series);
        return;
    }

    size_t removed = create_missing_values(series.temp, n, 0.4, 42ULL, damaged, mask);
    (void)removed;

    check(n == series.n, "isti broj zapisa nakon ostecenja");
    check(!isnan(damaged[0]), "prva vrijednost ocuvana");
    check(!isnan(damaged[n - 1]), "zadnja vrijednost ocuvana");

    size_t mask_count = 0;
    size_t nan_count = 0;
    for (size_t i = 0; i < n; i++) {
        if (mask[i]) {
            mask_count++;
        }
        if (isnan(damaged[i])) {
            nan_count++;
        }
    }
    check(mask_count == nan_count, "broj maske == broj NaN");
    check(mask_count > 0, "nesto je obrisano");
    check(count_nan(series.temp, n) == 0, "original nije promijenjen (bez NaN)");

    free(damaged);
    free(mask);
    series_free(&series);
}

static void test_interpolation(void) {
    printf("\n== Klasicne interpolacije ==\n");

    Series series = {0};
    if (generate_synthetic_series(&series, QUICK_SAMPLE_HOURS) != 0) {
        check(0, "generiranje sintetickog niza");
        return;
    }

    size_t n = series.n;
    double *damaged = (double *)malloc(n * sizeof(double));
    double *out = (double *)malloc(n * sizeof(double));
    int *mask = (int *)malloc(n * sizeof(int));
    if (!damaged || !out || !mask) {
        check(0, "alokacija memorije");
        free(damaged);
        free(out);
        free(mask);
        series_free(&series);
        return;
    }

    create_missing_values(series.temp, n, 0.4, 42ULL, damaged, mask);

    forward_fill(damaged, n, out);
    check(count_nan(out, n) == 0, "forward_fill: nema NaN");

    linear_interpolation(damaged, n, out);
    check(count_nan(out, n) == 0, "linear_interpolation: nema NaN");

    time_interpolation(damaged, n, series.epoch, out);
    check(count_nan(out, n) == 0, "time_interpolation: nema NaN");

    if (cubic_interpolation(damaged, n, out) == 0) {
        check(count_nan(out, n) == 0, "cubic_interpolation: nema NaN");
    } else {
        check(0, "cubic_interpolation: metoda nije primjenjiva");
    }

    if (spline_interpolation(damaged, n, out) == 0) {
        check(count_nan(out, n) == 0, "spline_interpolation: nema NaN");
    } else {
        check(0, "spline_interpolation: metoda nije primjenjiva");
    }

    /* forward_fill: rupa dobiva zadnju poznatu vrijednost. */
    double tiny[] = {5.0, NAN, 9.0};
    forward_fill(tiny, 3, out);
    check_near(out[1], 5.0, 1e-9, "forward_fill kopira zadnju poznatu");

    /* linear: sredina izmedu 5 i 9 je 7. */
    linear_interpolation(tiny, 3, out);
    check_near(out[1], 7.0, 1e-9, "linear: sredina 5 i 9 = 7");

    free(damaged);
    free(out);
    free(mask);
    series_free(&series);
}

static void test_metrics(void) {
    printf("\n== Evaluacija (MAE/RMSE/R2) ==\n");

    double original[] = {1.0, 2.0, 3.0, 4.0};
    int mask_all[] = {1, 1, 1, 1};

    Metrics perfect = evaluate_reconstruction(original, original, mask_all, 4);
    check_near(perfect.mae, 0.0, 1e-9, "savrsena: MAE = 0");
    check_near(perfect.rmse, 0.0, 1e-9, "savrsena: RMSE = 0");
    check_near(perfect.r2, 1.0, 1e-9, "savrsena: R2 = 1");

    double off[] = {3.0, 4.0, 5.0, 6.0};
    Metrics shifted = evaluate_reconstruction(original, off, mask_all, 4);
    check_near(shifted.mae, 2.0, 1e-9, "pomak 2: MAE = 2");
    check_near(shifted.rmse, 2.0, 1e-9, "pomak 2: RMSE = 2");

    /* Samo na maskiranim mjestima. */
    int mask_partial[] = {0, 1, 0, 1};
    double recon_partial[] = {1.0, 4.0, 3.0, 6.0};
    Metrics partial = evaluate_reconstruction(original, recon_partial, mask_partial, 4);
    check_near(partial.mae, 2.0, 1e-9, "parcijalna maska: MAE = 2");
    check(partial.count == 2, "parcijalna maska: count = 2");
}

static void test_dataset(void) {
    printf("\n== Ucitavanje CSV (demo) ==\n");

    Series s = {0};
    if (series_load_csv(&s, DEMO_CSV, "Split") != 0) {
        check(0, "ucitavanje demo CSV-a za Split");
        return;
    }

    check(s.n == 12, "Split ima 12 zapisa");
    check(count_nan(s.temp, s.n) == 0, "nema NaN u ucitanom nizu");

    int monotonic = 1;
    for (size_t i = 1; i < s.n; i++) {
        if (s.epoch[i] < s.epoch[i - 1]) {
            monotonic = 0;
            break;
        }
    }
    check(monotonic, "timestamp raste monotono");

    series_free(&s);
}

int main(void) {
    printf("======================================================================\n");
    printf("TESTOVI -- C verzija diplomskog\n");
    printf("======================================================================\n");

    test_knn();
    test_knn_upgraded();
    test_rf();
    test_preprocessing();
    test_interpolation();
    test_metrics();
    test_dataset();

    printf("\n----------------------------------------------------------------------\n");
    printf("Provjera: %d  |  Pala: %d\n", g_checks, g_failures);
    printf("Rezultat: %s\n", g_failures == 0 ? "SVE PROLAZI" : "IMA GRESAKA");
    return g_failures == 0 ? 0 : 1;
}
