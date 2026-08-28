#!/usr/bin/env python3
"""Prototipi predlozenih poboljsanja ML metoda — procjena dobitka prije pisanja C koda.

Sve varijante koriste ISTE maske kao C eksperiment (replika xorshift64 + Fisher-Yates),
pa su brojke izravno usporedive s results/experiment_results.csv.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from verify_ml_methods import create_missing_random, create_single_block

SCENARIOS = [
    ("random", None),
    ("block", "random"),
    ("block_start", "start"),
    ("block_middle", "middle"),
    ("block_end", "end"),
]
RATES = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80]


def make_mask(n, scen, pos, rate):
    return create_missing_random(n, rate) if pos is None else create_single_block(n, rate, pos)


# --------------------------------------------------------------------------
# Varijante KNN-a
# --------------------------------------------------------------------------

def knn_variant(temp, hour, yday, mask, k=5, weighted=False, use_time_feats=True):
    n = len(temp)
    known = np.where(~mask)[0]
    out = temp.copy()
    k = min(k, len(known))
    kpos = known.astype(float)
    kh, ky = hour[known].astype(float), yday[known].astype(float)

    for i in np.where(mask)[0]:
        d2 = (kpos - i) ** 2
        if use_time_feats:
            d2 = d2 + (kh - hour[i]) ** 2 + (ky - yday[i]) ** 2
        sel = np.argsort(d2, kind="stable")[:k]
        nb, dist = known[sel], np.sqrt(d2[sel])
        if weighted:
            w = 1.0 / (dist + 1e-6)
            out[i] = (w * temp[nb]).sum() / w.sum()
        else:
            out[i] = temp[nb].mean()
    return out


# --------------------------------------------------------------------------
# Znacajke sa susjedima (lag/lead) — ono sto ML metodama trenutno nedostaje
# --------------------------------------------------------------------------

def gap_features(temp, mask):
    """Za svaki indeks: zadnja poznata lijevo, prva poznata desno i udaljenosti.

    Racuna se ISKLJUCIVO iz ostecenog niza, pa nema curenja informacija.
    """
    n = len(temp)
    prev_v, prev_d = np.full(n, np.nan), np.full(n, np.inf)
    last_i = -1
    for i in range(n):
        if not mask[i]:
            last_i = i
        elif last_i >= 0:
            prev_v[i], prev_d[i] = temp[last_i], i - last_i
        if not mask[i]:
            prev_v[i], prev_d[i] = temp[i], 0.0

    next_v, next_d = np.full(n, np.nan), np.full(n, np.inf)
    nxt_i = -1
    for i in range(n - 1, -1, -1):
        if not mask[i]:
            nxt_i = i
        elif nxt_i >= 0:
            next_v[i], next_d[i] = temp[nxt_i], nxt_i - i
        if not mask[i]:
            next_v[i], next_d[i] = temp[i], 0.0

    return prev_v, prev_d, next_v, next_d


def build_matrix(temp, hour, mask, with_lag):
    n = len(temp)
    idx = np.arange(n, dtype=float)
    cols = [idx / (n - 1), np.sin(2 * np.pi * hour / 24), np.cos(2 * np.pi * hour / 24)]
    if with_lag:
        pv, pd_, nv, nd = gap_features(temp, mask)
        big = 1e6
        cols += [
            np.nan_to_num(pv, nan=0.0),
            np.nan_to_num(nv, nan=0.0),
            np.minimum(pd_, big),
            np.minimum(nd, big),
        ]
    return np.column_stack(cols)


# --------------------------------------------------------------------------
# Stablo (CART, MSE) — s opcijom linearnog modela u listu
# --------------------------------------------------------------------------

class Tree:
    def __init__(self, max_depth=5, min_leaf=3, linear_leaf=False):
        self.max_depth, self.min_leaf, self.linear_leaf = max_depth, min_leaf, linear_leaf

    def fit(self, X, y):
        self.root = self._build(X, y, 0)
        return self

    def _leaf(self, X, y):
        if self.linear_leaf and len(y) >= 2 * X.shape[1]:
            A = np.column_stack([X, np.ones(len(X))])
            try:
                coef, *_ = np.linalg.lstsq(A, y, rcond=None)
                return ("lin", coef)
            except np.linalg.LinAlgError:
                pass
        return ("const", y.mean())

    def _build(self, X, y, depth):
        if depth >= self.max_depth or len(y) < 2 * self.min_leaf:
            return self._leaf(X, y)

        best, bf, bt = np.inf, -1, 0.0
        for f in range(X.shape[1]):
            v = X[:, f]
            order = np.argsort(v, kind="stable")
            ys, vs = y[order], v[order]
            csum = np.cumsum(ys)
            csq = np.cumsum(ys ** 2)
            tot, totsq = csum[-1], csq[-1]
            m = len(ys)
            for j in range(self.min_leaf - 1, m - self.min_leaf):
                if vs[j] == vs[j + 1]:
                    continue
                nl = j + 1
                sse = (csq[j] - csum[j] ** 2 / nl) + ((totsq - csq[j]) - (tot - csum[j]) ** 2 / (m - nl))
                if sse < best:
                    best, bf, bt = sse, f, 0.5 * (vs[j] + vs[j + 1])
        if bf < 0:
            return self._leaf(X, y)

        left = X[:, bf] <= bt
        return ("node", bf, bt, self._build(X[left], y[left], depth + 1),
                self._build(X[~left], y[~left], depth + 1))

    def predict(self, X):
        return np.array([self._one(self.root, x) for x in X])

    def _one(self, node, x):
        while node[0] == "node":
            node = node[3] if x[node[1]] <= node[2] else node[4]
        if node[0] == "lin":
            return float(np.append(x, 1.0) @ node[1])
        return node[1]


def tree_impute(temp, hour, mask, max_depth=5, with_lag=False, linear_leaf=False):
    X = build_matrix(temp, hour, mask, with_lag)
    known = ~mask
    t = Tree(max_depth=max_depth, linear_leaf=linear_leaf).fit(X[known], temp[known])
    out = temp.copy()
    out[mask] = t.predict(X[mask])
    return out


# --------------------------------------------------------------------------

def evaluate(fn, temp, hour, yday, n):
    per_scen = {}
    for scen, pos in SCENARIOS:
        errs = []
        for rate in RATES:
            m = make_mask(n, scen, pos, rate)
            pred = fn(temp, hour, yday, m)
            errs.append(np.abs(temp[m] - pred[m]).mean())
        per_scen[scen] = float(np.mean(errs))
    per_scen["PROSJEK"] = float(np.mean(list(per_scen.values())))
    return per_scen


def main() -> None:
    d = pd.read_csv("data/processed/jena_temperature_7d.csv")
    temp = d["temperature"].to_numpy(dtype=float)
    ts = pd.to_datetime(d["timestamp"])
    hour, yday = ts.dt.hour.to_numpy(), ts.dt.dayofyear.to_numpy()
    n = len(temp)

    variants = {
        "knn k=5 (TRENUTNO)": lambda t, h, y, m: knn_variant(t, h, y, m, k=5),
        "knn k=2": lambda t, h, y, m: knn_variant(t, h, y, m, k=2),
        "knn k=5 + ponderiranje": lambda t, h, y, m: knn_variant(t, h, y, m, k=5, weighted=True),
        "knn k=2 + ponderiranje": lambda t, h, y, m: knn_variant(t, h, y, m, k=2, weighted=True),
        "stablo d=5 (TRENUTNO)": lambda t, h, y, m: tree_impute(t, h, m, 5, False, False),
        "stablo d=10": lambda t, h, y, m: tree_impute(t, h, m, 10, False, False),
        "stablo d=5 + lag": lambda t, h, y, m: tree_impute(t, h, m, 5, True, False),
        "stablo d=10 + lag": lambda t, h, y, m: tree_impute(t, h, m, 10, True, False),
        "stablo d=5 + lag + lin. list": lambda t, h, y, m: tree_impute(t, h, m, 5, True, True),
    }

    print("Prosjecni MAE (C) po scenariju — svih 8 rateova\n")
    hdr = f"{'varijanta':<30}{'random':>9}{'block':>9}{'b_start':>9}{'b_mid':>9}{'b_end':>9}{'PROSJEK':>10}"
    print(hdr)
    print("-" * len(hdr))
    for name, fn in variants.items():
        r = evaluate(fn, temp, hour, yday, n)
        print(f"{name:<30}{r['random']:>9.3f}{r['block']:>9.3f}{r['block_start']:>9.3f}"
              f"{r['block_middle']:>9.3f}{r['block_end']:>9.3f}{r['PROSJEK']:>10.3f}")

    print(f"\n{'linear_interpolation (referenca)':<30}{0.112:>9.3f}{3.773:>9.3f}"
          f"{2.379:>9.3f}{4.252:>9.3f}{5.140:>9.3f}{3.131:>10.3f}")


if __name__ == "__main__":
    main()
