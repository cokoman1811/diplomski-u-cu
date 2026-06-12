#include "preprocessing.h"

#include <math.h>
#include <stdint.h>
#include <stdlib.h>

/* Jednostavan ponovljiv PRNG (xorshift64). */
static uint64_t rng_state;

static void rng_seed(uint64_t seed) {
    rng_state = seed ? seed : 0x9E3779B97F4A7C15ULL;
}

static uint64_t rng_next(void) {
    uint64_t x = rng_state;
    x ^= x << 13;
    x ^= x >> 7;
    x ^= x << 17;
    rng_state = x;
    return x;
}

/* Slucajan cijeli broj u [0, bound). */
static size_t rng_below(size_t bound) {
    return (size_t)(rng_next() % (uint64_t)bound);
}

size_t create_missing_values(const double *temp, size_t n, double missing_rate,
                             unsigned long long seed, double *damaged, int *mask) {
    for (size_t i = 0; i < n; i++) {
        damaged[i] = temp[i];
        mask[i] = 0;
    }

    if (n < 2 || missing_rate <= 0.0) {
        return 0;
    }
    if (missing_rate > 1.0) {
        missing_rate = 1.0;
    }

    /* Prihvatljive pozicije: sve osim prve i zadnje. */
    size_t eligible_count = n - 2;
    if (eligible_count == 0) {
        return 0;
    }

    size_t *eligible = (size_t *)malloc(eligible_count * sizeof(size_t));
    if (!eligible) {
        return 0;
    }
    for (size_t i = 0; i < eligible_count; i++) {
        eligible[i] = i + 1;
    }

    size_t n_to_remove = (size_t)llround(missing_rate * (double)n);
    if (n_to_remove > eligible_count) {
        n_to_remove = eligible_count;
    }

    /* Fisher-Yates: izmijesaj prvih n_to_remove pozicija. */
    rng_seed((uint64_t)seed);
    for (size_t i = 0; i < n_to_remove; i++) {
        size_t j = i + rng_below(eligible_count - i);
        size_t tmp = eligible[i];
        eligible[i] = eligible[j];
        eligible[j] = tmp;
    }

    for (size_t i = 0; i < n_to_remove; i++) {
        size_t pos = eligible[i];
        damaged[pos] = NAN;
        mask[pos] = 1;
    }

    free(eligible);
    return n_to_remove;
}

size_t create_block_missing_values(const double *temp, size_t n, size_t block_size,
                                   double missing_rate, unsigned long long seed,
                                   double *damaged, int *mask) {
    for (size_t i = 0; i < n; i++) {
        damaged[i] = temp[i];
        mask[i] = 0;
    }

    if (n < 2 || missing_rate <= 0.0 || block_size == 0) {
        return 0;
    }
    if (missing_rate > 1.0) {
        missing_rate = 1.0;
    }

    /* Blok mora stati unutar (1 .. n-2) da rubovi ostanu poznati. */
    if (block_size >= n - 2) {
        return 0;
    }

    size_t target = (size_t)llround(missing_rate * (double)n);
    if (target == 0) {
        return 0;
    }

    size_t num_blocks = target / block_size;
    if (num_blocks == 0) {
        num_blocks = 1;
    }

    size_t min_start = 1;
    size_t max_start = n - block_size - 1;
    if (max_start < min_start) {
        return 0;
    }

    size_t eligible_count = max_start - min_start + 1;
    size_t *eligible = (size_t *)malloc(eligible_count * sizeof(size_t));
    if (!eligible) {
        return 0;
    }
    for (size_t i = 0; i < eligible_count; i++) {
        eligible[i] = min_start + i;
    }

    rng_seed((uint64_t)seed);
    for (size_t i = 0; i < eligible_count; i++) {
        size_t j = i + rng_below(eligible_count - i);
        size_t tmp = eligible[i];
        eligible[i] = eligible[j];
        eligible[j] = tmp;
    }

    int *taken = (int *)calloc(n, sizeof(int));
    if (!taken) {
        free(eligible);
        return 0;
    }

    size_t blocks_placed = 0;
    size_t removed = 0;

    for (size_t i = 0; i < eligible_count && blocks_placed < num_blocks; i++) {
        size_t start = eligible[i];
        int overlap = 0;
        for (size_t k = 0; k < block_size; k++) {
            if (taken[start + k]) {
                overlap = 1;
                break;
            }
        }
        if (overlap) {
            continue;
        }

        for (size_t k = 0; k < block_size; k++) {
            size_t pos = start + k;
            taken[pos] = 1;
            damaged[pos] = NAN;
            mask[pos] = 1;
            removed++;
        }
        blocks_placed++;
    }

    free(taken);
    free(eligible);
    return removed;
}
