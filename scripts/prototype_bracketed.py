#!/usr/bin/env python3
"""Prototip: KNN s obaveznim obuhvatom (bracketing) i lokalna linearna regresija.

Kljucna razlika prema obicnom KNN-u: susjedi se biraju tako da barem jedan bude
lijevo, a jedan desno od rupe. Obicni KNN to ne jamci, pa u blizini ruba bloka
uzme dvije tocke s iste strane i time izgubi nagib.
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


def knn_bracketed(temp, mask, per_side=1, weighted=True):
    known = np.where(~mask)[0]
    out = temp.copy()
    for i in np.where(mask)[0]:
        left = known[known < i][-per_side:]
        right = known[known > i][:per_side]
        nb = np.concatenate([left, right])
        if nb.size == 0:
            continue
        dist = np.abs(nb - i).astype(float)
        w = 1.0 / (dist + 1e-9) if weighted else np.ones(nb.size)
        out[i] = float((w * temp[nb]).sum() / w.sum())
    return out


def local_linear(temp, mask, half=12):
    """Lokalna linearna regresija na do `half` poznatih tocaka sa svake strane."""
    known = np.where(~mask)[0]
    out = temp.copy()
    for i in np.where(mask)[0]:
        left = known[known < i][-half:]
        right = known[known > i][:half]
        nb = np.concatenate([left, right])
        if nb.size < 2:
            if nb.size == 1:
                out[i] = temp[nb[0]]
            continue
        x = (nb - i).astype(float)
        y = temp[nb]
        A = np.column_stack([x, np.ones(x.size)])
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        out[i] = float(coef[1])
    return out


def evaluate(fn, temp, n):
    per = []
    for scen, pos in SCENARIOS:
        errs = []
        for rate in RATES:
            m = make_mask(n, scen, pos, rate)
            errs.append(np.abs(temp[m] - fn(temp, m)[m]).mean())
        per.append(float(np.mean(errs)))
    return per


def main() -> None:
    d = pd.read_csv("data/processed/jena_temperature_7d.csv")
    temp = d["temperature"].to_numpy(dtype=float)
    n = len(temp)

    variants = {
        "knn 1+1 obuhvat + pond.": lambda t, m: knn_bracketed(t, m, 1, True),
        "knn 2+2 obuhvat + pond.": lambda t, m: knn_bracketed(t, m, 2, True),
        "lok. linearna (+-6)": lambda t, m: local_linear(t, m, 6),
        "lok. linearna (+-12)": lambda t, m: local_linear(t, m, 12),
        "lok. linearna (+-36)": lambda t, m: local_linear(t, m, 36),
    }

    hdr = (f"{'varijanta':<28}{'random':>9}{'block':>9}{'b_start':>9}"
           f"{'b_mid':>9}{'b_end':>9}{'PROSJEK':>10}")
    print(hdr)
    print("-" * len(hdr))
    for name, fn in variants.items():
        r = evaluate(fn, temp, n)
        print(f"{name:<28}" + "".join(f"{v:>9.3f}" for v in r) + f"{np.mean(r):>10.3f}")

    print(f"{'linear (referenca)':<28}{0.112:>9.3f}{3.773:>9.3f}"
          f"{2.379:>9.3f}{4.252:>9.3f}{5.140:>9.3f}{3.131:>10.3f}")
    print(f"{'knn k=5 (TRENUTNO)':<28}{0.236:>9.3f}{3.845:>9.3f}"
          f"{3.220:>9.3f}{4.599:>9.3f}{6.794:>9.3f}{3.739:>10.3f}")


if __name__ == "__main__":
    main()
