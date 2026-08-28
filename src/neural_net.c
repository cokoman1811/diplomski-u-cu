#include "neural_net.h"

#include "ml_features.h"

#include <math.h>
#include <stdint.h>
#include <stdlib.h>

#define NN_IN      ML_NUM_FEATURES
#define NN_H1      24
#define NN_H2      12
#define NN_EPOCHS  200
#define NN_BATCH   32
#define NN_LR      0.01
#define NN_BETA1   0.9
#define NN_BETA2   0.999
#define NN_EPS     1e-8
#define NN_SEED    42ULL

/* Rasporedi parametara u jednom ravnom vektoru — pojednostavljuje Adam. */
#define NN_OFF_W1 0
#define NN_OFF_B1 (NN_OFF_W1 + NN_H1 * NN_IN)
#define NN_OFF_W2 (NN_OFF_B1 + NN_H1)
#define NN_OFF_B2 (NN_OFF_W2 + NN_H2 * NN_H1)
#define NN_OFF_W3 (NN_OFF_B2 + NN_H2)
#define NN_OFF_B3 (NN_OFF_W3 + NN_H2)
#define NN_NUM_PARAMS (NN_OFF_B3 + 1)

typedef struct {
    double p[NN_NUM_PARAMS];
    double g[NN_NUM_PARAMS];
    double m[NN_NUM_PARAMS];
    double v[NN_NUM_PARAMS];
    double a1[NN_H1];
    double a2[NN_H2];
} Mlp;

static uint64_t nn_rng_state;

static void nn_rng_seed(uint64_t seed) {
    nn_rng_state = seed ? seed : 0x9E3779B97F4A7C15ULL;
}

static uint64_t nn_rng_next(void) {
    uint64_t x = nn_rng_state;
    x ^= x << 13;
    x ^= x >> 7;
    x ^= x << 17;
    nn_rng_state = x;
    return x;
}

/* Uniformno iz [-1, 1). */
static double nn_rng_uniform(void) {
    return ((double)(nn_rng_next() >> 11) / 9007199254740992.0) * 2.0 - 1.0;
}

static size_t nn_rng_below(size_t bound) {
    if (bound == 0) {
        return 0;
    }
    return (size_t)(nn_rng_next() % (uint64_t)bound);
}

static void nn_init(Mlp *net) {
    int i;
    double lim1 = sqrt(6.0 / (double)(NN_IN + NN_H1));
    double lim2 = sqrt(6.0 / (double)(NN_H1 + NN_H2));
    double lim3 = sqrt(6.0 / (double)(NN_H2 + 1));

    for (i = 0; i < NN_NUM_PARAMS; i++) {
        net->p[i] = 0.0;
        net->m[i] = 0.0;
        net->v[i] = 0.0;
        net->g[i] = 0.0;
    }
    for (i = 0; i < NN_H1 * NN_IN; i++) {
        net->p[NN_OFF_W1 + i] = nn_rng_uniform() * lim1;
    }
    for (i = 0; i < NN_H2 * NN_H1; i++) {
        net->p[NN_OFF_W2 + i] = nn_rng_uniform() * lim2;
    }
    /* Izlazni sloj namjerno mali: pocetna predikcija ~ 0 = cista linearna baza. */
    for (i = 0; i < NN_H2; i++) {
        net->p[NN_OFF_W3 + i] = nn_rng_uniform() * lim3 * 0.1;
    }
}

static double nn_forward(Mlp *net, const double *x) {
    int i, j;
    double y;

    for (i = 0; i < NN_H1; i++) {
        double z = net->p[NN_OFF_B1 + i];
        const double *w = &net->p[NN_OFF_W1 + i * NN_IN];
        for (j = 0; j < NN_IN; j++) {
            z += w[j] * x[j];
        }
        net->a1[i] = tanh(z);
    }
    for (i = 0; i < NN_H2; i++) {
        double z = net->p[NN_OFF_B2 + i];
        const double *w = &net->p[NN_OFF_W2 + i * NN_H1];
        for (j = 0; j < NN_H1; j++) {
            z += w[j] * net->a1[j];
        }
        net->a2[i] = tanh(z);
    }
    y = net->p[NN_OFF_B3];
    for (i = 0; i < NN_H2; i++) {
        y += net->p[NN_OFF_W3 + i] * net->a2[i];
    }
    return y;
}

/* Akumulira gradijent kvadratnog gubitka za jedan uzorak. */
static void nn_backward(Mlp *net, const double *x, double y_pred, double y_true) {
    double d3 = y_pred - y_true;
    double d2[NN_H2];
    double d1[NN_H1];
    int i, j;

    net->g[NN_OFF_B3] += d3;
    for (i = 0; i < NN_H2; i++) {
        net->g[NN_OFF_W3 + i] += d3 * net->a2[i];
    }

    for (i = 0; i < NN_H2; i++) {
        d2[i] = d3 * net->p[NN_OFF_W3 + i] * (1.0 - net->a2[i] * net->a2[i]);
    }
    for (i = 0; i < NN_H1; i++) {
        double acc = 0.0;
        for (j = 0; j < NN_H2; j++) {
            acc += d2[j] * net->p[NN_OFF_W2 + j * NN_H1 + i];
        }
        d1[i] = acc * (1.0 - net->a1[i] * net->a1[i]);
    }

    for (i = 0; i < NN_H2; i++) {
        double *gw = &net->g[NN_OFF_W2 + i * NN_H1];
        net->g[NN_OFF_B2 + i] += d2[i];
        for (j = 0; j < NN_H1; j++) {
            gw[j] += d2[i] * net->a1[j];
        }
    }
    for (i = 0; i < NN_H1; i++) {
        double *gw = &net->g[NN_OFF_W1 + i * NN_IN];
        net->g[NN_OFF_B1 + i] += d1[i];
        for (j = 0; j < NN_IN; j++) {
            gw[j] += d1[i] * x[j];
        }
    }
}

static void nn_adam_step(Mlp *net, double lr, double scale, int step) {
    double bc1 = 1.0 - pow(NN_BETA1, (double)step);
    double bc2 = 1.0 - pow(NN_BETA2, (double)step);
    int i;

    for (i = 0; i < NN_NUM_PARAMS; i++) {
        double g = net->g[i] * scale;
        net->m[i] = NN_BETA1 * net->m[i] + (1.0 - NN_BETA1) * g;
        net->v[i] = NN_BETA2 * net->v[i] + (1.0 - NN_BETA2) * g * g;
        net->p[i] -= lr * (net->m[i] / bc1) / (sqrt(net->v[i] / bc2) + NN_EPS);
        net->g[i] = 0.0;
    }
}

int neural_net_imputation(const Series *series, const double *temp, double *out) {
    size_t n = series->n;
    size_t known_count = 0, kc = 0, i;
    size_t *known = NULL, *order = NULL;
    double *F = NULL, *X = NULL, *y = NULL;
    double mean[NN_IN], sd[NN_IN];
    double y_sd = 1.0;
    double lo, hi;
    Mlp *net = NULL;
    int epoch, step = 1, j;

    for (i = 0; i < n; i++) {
        out[i] = temp[i];
        if (!isnan(temp[i])) {
            known_count++;
        }
    }
    if (known_count < 8) {
        return 1;
    }
    ml_known_range(temp, n, &lo, &hi);

    F = (double *)malloc(n * ML_NUM_FEATURES * sizeof(double));
    X = (double *)malloc(n * NN_IN * sizeof(double));
    y = (double *)malloc(n * sizeof(double));
    known = (size_t *)malloc(known_count * sizeof(size_t));
    order = (size_t *)malloc(known_count * sizeof(size_t));
    net = (Mlp *)malloc(sizeof(Mlp));
    if (!F || !X || !y || !known || !order || !net) {
        free(F); free(X); free(y); free(known); free(order); free(net);
        return 1;
    }

    ml_features_build(series, temp, n, F);

    for (i = 0; i < n; i++) {
        for (j = 0; j < NN_IN; j++) {
            X[i * NN_IN + j] = F[i * ML_NUM_FEATURES + j];
        }
        y[i] = isnan(temp[i]) ? NAN : temp[i] - F[i * ML_NUM_FEATURES + GAP_F_LIN_BASE];
        if (!isnan(temp[i])) {
            known[kc++] = i;
        }
    }

    /* Standardizacija ulaza po statistikama POZNATIH tocaka. */
    for (j = 0; j < NN_IN; j++) {
        double s = 0.0, ss = 0.0;
        for (i = 0; i < known_count; i++) {
            double v = X[known[i] * NN_IN + j];
            s += v;
            ss += v * v;
        }
        mean[j] = s / (double)known_count;
        sd[j] = sqrt(ss / (double)known_count - mean[j] * mean[j]);
        if (!(sd[j] > 1e-9)) {
            sd[j] = 1.0;
        }
    }
    for (i = 0; i < n; i++) {
        for (j = 0; j < NN_IN; j++) {
            X[i * NN_IN + j] = (X[i * NN_IN + j] - mean[j]) / sd[j];
        }
    }

    /* Skaliranje cilja — reziduali su reda 0,1 C, mreza uci stabilnije na ~1. */
    {
        double ss = 0.0;
        for (i = 0; i < known_count; i++) {
            double v = y[known[i]];
            ss += v * v;
        }
        y_sd = sqrt(ss / (double)known_count);
        if (!(y_sd > 1e-9)) {
            y_sd = 1.0;
        }
    }

    nn_rng_seed(NN_SEED);
    nn_init(net);

    for (i = 0; i < known_count; i++) {
        order[i] = known[i];
    }

    for (epoch = 0; epoch < NN_EPOCHS; epoch++) {
        size_t b;
        /* Kosinusno gasenje stope ucenja — stabilizira zavrsne epohe. */
        double lr = NN_LR * (0.5 * (1.0 + cos(3.14159265358979323846
                                              * (double)epoch / (double)NN_EPOCHS)));
        if (lr < NN_LR * 0.02) {
            lr = NN_LR * 0.02;
        }

        for (i = known_count; i-- > 0;) {
            size_t r = nn_rng_below(i + 1);
            size_t tmp = order[i];
            order[i] = order[r];
            order[r] = tmp;
        }

        for (b = 0; b < known_count; b += NN_BATCH) {
            size_t end = b + NN_BATCH;
            size_t cnt;
            if (end > known_count) {
                end = known_count;
            }
            cnt = end - b;
            for (i = b; i < end; i++) {
                size_t idx = order[i];
                const double *x = &X[idx * NN_IN];
                double pred = nn_forward(net, x);
                nn_backward(net, x, pred, y[idx] / y_sd);
            }
            nn_adam_step(net, lr, 1.0 / (double)cnt, step++);
        }
    }

    for (i = 0; i < n; i++) {
        double value;
        if (!isnan(temp[i])) {
            continue;
        }
        value = F[i * ML_NUM_FEATURES + GAP_F_LIN_BASE]
              + nn_forward(net, &X[i * NN_IN]) * y_sd;
        if (value < lo) {
            value = lo;
        }
        if (value > hi) {
            value = hi;
        }
        out[i] = value;
    }

    free(F);
    free(X);
    free(y);
    free(known);
    free(order);
    free(net);
    ml_fill_remaining_gaps(out, n);
    return 0;
}
