#!/usr/bin/env python3
"""Uparena usporedba: svaka ML metoda protiv svake klasicne metode."""

from __future__ import annotations

import pandas as pd
from scipy import stats

KLAS = ["linear_interpolation", "time_interpolation", "cubic_interpolation",
        "spline_interpolation", "forward_fill", "moving_average"]
ML = ["neural_net", "knn_upgraded", "random_forest", "decision_tree"]
SCEN = ["random", "block", "block_start", "block_middle", "block_end"]


def main() -> None:
    runs = pd.read_csv("results/experiment_runs.csv")
    w = runs.pivot_table(index=["repeat", "scenario", "missing_rate"],
                         columns="method", values="mae")

    print("=" * 96)
    print("UPARENA RAZLIKA MAE: ML metoda minus klasicna metoda (800 parova)")
    print("=" * 96)
    print(f"{'ML metoda':<16}" + "".join(f"{k[:11]:>13}" for k in KLAS))
    print("-" * (16 + 13 * len(KLAS)))
    for m in ML:
        cells = []
        for k in KLAS:
            d = (w[m] - w[k]).dropna()
            nz = d[d != 0]
            p = stats.wilcoxon(nz)[1] if len(nz) else 1.0
            cells.append(f"{d.mean():>+12.3f}" + ("*" if p < 0.05 else " "))
        print(f"{m:<16}" + "".join(cells))
    print("\nNegativno = ML bolji.  * = znacajno (Wilcoxon, p < 0,05)")

    print()
    print("=" * 96)
    print("NAJBOLJA ML METODA PO TESTU protiv svake klasicne")
    print("=" * 96)
    best_ml = w[ML].min(axis=1)
    for k in KLAS:
        d = (best_ml - w[k]).dropna()
        print(f"  vs {k:<24}{d.mean():>+9.3f} C   pobjeda {int((d < 0).sum())}/{len(d)}"
              f"  ({100 * (d < 0).mean():.0f} %)")

    print()
    print("=" * 96)
    print("PO SCENARIJIMA: najbolja ML metoda minus linearna interpolacija")
    print("=" * 96)
    for sc in SCEN:
        sel = w.xs(sc, level="scenario")
        d = (sel[ML].min(axis=1) - sel["linear_interpolation"]).dropna()
        nz = d[d != 0]
        p = stats.wilcoxon(nz)[1] if len(nz) else 1.0
        print(f"  {sc:<14}{d.mean():>+9.4f} C   pobjeda {int((d < 0).sum()):>3}/{len(d)}"
              f"   p = {p:.1e}")


if __name__ == "__main__":
    main()
