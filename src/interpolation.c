#include "interpolation.h"

#include <math.h>
#include <stdlib.h>

/* Popuni preostale NAN vrijednosti: prvo forward, zatim backward fill. */
static void fill_remaining_gaps(double *out, size_t n) {
    double last = NAN;
    for (size_t i = 0; i < n; i++) {
        if (!isnan(out[i])) {
            last = out[i];
        } else if (!isnan(last)) {
            out[i] = last;
        }
    }
    /* Backward fill za eventualne pocetne NAN vrijednosti. */
    double next = NAN;
    for (size_t i = n; i-- > 0;) {
        if (!isnan(out[i])) {
            next = out[i];
        } else if (!isnan(next)) {
            out[i] = next;
        }
    }
}

void forward_fill(const double *temp, size_t n, double *out) {
    for (size_t i = 0; i < n; i++) {
        out[i] = temp[i];
    }
    fill_remaining_gaps(out, n);
}

/* Linearna interpolacija s proizvoljnom x-osi (pozicije ili vrijeme). */
static void linear_on_axis(const double *temp, size_t n, const double *x, double *out) {
    for (size_t i = 0; i < n; i++) {
        out[i] = temp[i];
    }

    for (size_t i = 0; i < n; i++) {
        if (!isnan(out[i])) {
            continue;
        }

        /* Najblizi poznati susjed lijevo. */
        long long left = -1;
        for (long long j = (long long)i - 1; j >= 0; j--) {
            if (!isnan(temp[j])) {
                left = j;
                break;
            }
        }

        /* Najblizi poznati susjed desno. */
        long long right = -1;
        for (size_t j = i + 1; j < n; j++) {
            if (!isnan(temp[j])) {
                right = (long long)j;
                break;
            }
        }

        if (left >= 0 && right >= 0) {
            double xl = x[left], xr = x[right];
            double yl = temp[left], yr = temp[right];
            double span = xr - xl;
            if (span != 0.0) {
                out[i] = yl + (yr - yl) * (x[i] - xl) / span;
            }
        }
    }

    fill_remaining_gaps(out, n);
}

void linear_interpolation(const double *temp, size_t n, double *out) {
    double *x = (double *)malloc(n * sizeof(double));
    if (!x) {
        forward_fill(temp, n, out);
        return;
    }
    for (size_t i = 0; i < n; i++) {
        x[i] = (double)i;
    }
    linear_on_axis(temp, n, x, out);
    free(x);
}

void time_interpolation(const double *temp, size_t n, const long long *epoch, double *out) {
    double *x = (double *)malloc(n * sizeof(double));
    if (!x) {
        forward_fill(temp, n, out);
        return;
    }
    for (size_t i = 0; i < n; i++) {
        x[i] = (double)epoch[i];
    }
    linear_on_axis(temp, n, x, out);
    free(x);
}

static int solve_tridiagonal(size_t m, const double *lower, const double *diag,
                             const double *upper, const double *rhs, double *x) {
    double *cp = (double *)malloc(m * sizeof(double));
    double *dp = (double *)malloc(m * sizeof(double));
    if (!cp || !dp) {
        free(cp);
        free(dp);
        return 1;
    }

    cp[0] = upper[0] / diag[0];
    dp[0] = rhs[0] / diag[0];
    for (size_t i = 1; i < m; i++) {
        double denom = diag[i] - lower[i] * cp[i - 1];
        if (denom == 0.0) {
            free(cp);
            free(dp);
            return 1;
        }
        if (i < m - 1) {
            cp[i] = upper[i] / denom;
        }
        dp[i] = (rhs[i] - lower[i] * dp[i - 1]) / denom;
    }

    x[m - 1] = dp[m - 1];
    for (size_t i = m - 1; i-- > 0;) {
        x[i] = dp[i] - cp[i] * x[i + 1];
    }

    free(cp);
    free(dp);
    return 0;
}

static void estimate_clamped_derivatives(size_t m, const double *kx, const double *ky,
                                         double *d0, double *dn) {
    if (m >= 3) {
        double h0 = kx[1] - kx[0];
        double hm1 = kx[m - 1] - kx[m - 2];
        *d0 = (-3.0 * ky[0] + 4.0 * ky[1] - ky[2]) / (2.0 * h0);
        *dn = (3.0 * ky[m - 1] - 4.0 * ky[m - 2] + ky[m - 3]) / (2.0 * hm1);
        return;
    }
    *d0 = (ky[1] - ky[0]) / (kx[1] - kx[0]);
    *dn = (ky[m - 1] - ky[m - 2]) / (kx[m - 1] - kx[m - 2]);
}

/*
 * Prirodni ili zakljucani kubicki spline kroz poznate tocke.
 * Os x su pozicije (0..n-1); query su pozicije nedostajucih vrijednosti.
 */
typedef enum {
    SPLINE_NATURAL,
    SPLINE_CLAMPED
} SplineBoundary;

static int cubic_spline_impl(const double *temp, size_t n, double *out, SplineBoundary bc) {
    size_t m = 0;
    for (size_t i = 0; i < n; i++) {
        if (!isnan(temp[i])) {
            m++;
        }
    }
    if (m < 4) {
        return 1;
    }

    double *kx = (double *)malloc(m * sizeof(double));
    double *ky = (double *)malloc(m * sizeof(double));
    double *y2 = (double *)malloc(m * sizeof(double));
    double *lower = (double *)malloc(m * sizeof(double));
    double *diag = (double *)malloc(m * sizeof(double));
    double *upper = (double *)malloc(m * sizeof(double));
    double *rhs = (double *)malloc(m * sizeof(double));
    if (!kx || !ky || !y2 || !lower || !diag || !upper || !rhs) {
        free(kx); free(ky); free(y2); free(lower); free(diag); free(upper); free(rhs);
        return 1;
    }

    size_t k = 0;
    for (size_t i = 0; i < n; i++) {
        if (!isnan(temp[i])) {
            kx[k] = (double)i;
            ky[k] = temp[i];
            k++;
        }
    }

    if (bc == SPLINE_NATURAL) {
        y2[0] = 0.0;
        lower[0] = 0.0;
        diag[0] = 1.0;
        upper[0] = 0.0;
        rhs[0] = 0.0;

        for (size_t i = 1; i < m - 1; i++) {
            double him1 = kx[i] - kx[i - 1];
            double hi = kx[i + 1] - kx[i];
            lower[i] = him1;
            diag[i] = 2.0 * (him1 + hi);
            upper[i] = hi;
            rhs[i] = 6.0 * ((ky[i + 1] - ky[i]) / hi - (ky[i] - ky[i - 1]) / him1);
        }

        lower[m - 1] = 0.0;
        diag[m - 1] = 1.0;
        upper[m - 1] = 0.0;
        rhs[m - 1] = 0.0;

        if (solve_tridiagonal(m, lower, diag, upper, rhs, y2) != 0) {
            free(kx); free(ky); free(y2); free(lower); free(diag); free(upper); free(rhs);
            return 1;
        }
    } else {
        double h0 = kx[1] - kx[0];
        double hm = kx[m - 1] - kx[m - 2];
        double d0, dn;
        estimate_clamped_derivatives(m, kx, ky, &d0, &dn);

        lower[0] = 0.0;
        diag[0] = 2.0 * h0;
        upper[0] = h0;
        rhs[0] = 6.0 * ((ky[1] - ky[0]) / h0 - d0);

        for (size_t i = 1; i < m - 1; i++) {
            double him1 = kx[i] - kx[i - 1];
            double hi = kx[i + 1] - kx[i];
            lower[i] = him1;
            diag[i] = 2.0 * (him1 + hi);
            upper[i] = hi;
            rhs[i] = 6.0 * ((ky[i + 1] - ky[i]) / hi - (ky[i] - ky[i - 1]) / him1);
        }

        lower[m - 1] = hm;
        diag[m - 1] = 2.0 * hm;
        upper[m - 1] = 0.0;
        rhs[m - 1] = 6.0 * (dn - (ky[m - 1] - ky[m - 2]) / hm);

        if (solve_tridiagonal(m, lower, diag, upper, rhs, y2) != 0) {
            free(kx); free(ky); free(y2); free(lower); free(diag); free(upper); free(rhs);
            return 1;
        }
    }

    for (size_t i = 0; i < n; i++) {
        if (!isnan(temp[i])) {
            out[i] = temp[i];
            continue;
        }

        double xq = (double)i;
        /* Pronadi interval [kx[lo], kx[hi]] binarnim trazenjem. */
        size_t lo = 0, hi = m - 1;
        while (hi - lo > 1) {
            size_t mid = (lo + hi) / 2;
            if (kx[mid] > xq) {
                hi = mid;
            } else {
                lo = mid;
            }
        }

        double h = kx[hi] - kx[lo];
        double a = (kx[hi] - xq) / h;
        double b = (xq - kx[lo]) / h;
        out[i] = a * ky[lo] + b * ky[hi]
               + ((a * a * a - a) * y2[lo] + (b * b * b - b) * y2[hi]) * (h * h) / 6.0;
    }

    free(kx); free(ky); free(y2); free(lower); free(diag); free(upper); free(rhs);
    fill_remaining_gaps(out, n);
    return 0;
}

int cubic_interpolation(const double *temp, size_t n, double *out) {
    return cubic_spline_impl(temp, n, out, SPLINE_CLAMPED);
}

int spline_interpolation(const double *temp, size_t n, double *out) {
    return cubic_spline_impl(temp, n, out, SPLINE_NATURAL);
}

void moving_average_imputation(const double *temp, size_t n, int window, double *out) {
    size_t i;
    int w;

    for (i = 0; i < n; i++) {
        out[i] = temp[i];
    }

    if (window < 1) {
        window = 1;
    }
    w = window;

    for (i = 0; i < n; i++) {
        long long start;
        long long end;
        double sum = 0.0;
        size_t count = 0;
        size_t j;

        if (!isnan(temp[i])) {
            continue;
        }

        start = (long long)i - w;
        if (start < 0) {
            start = 0;
        }
        end = (long long)i + w;
        if (end >= (long long)n) {
            end = (long long)n - 1;
        }

        for (j = (size_t)start; j <= (size_t)end; j++) {
            if (!isnan(temp[j])) {
                sum += temp[j];
                count++;
            }
        }

        if (count > 0) {
            out[i] = sum / (double)count;
        }
    }

    fill_remaining_gaps(out, n);
}
