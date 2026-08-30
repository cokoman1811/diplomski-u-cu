#!/usr/bin/env python3
"""Usporeduje MAE vrijednosti iz tablica u radu s aktualnim experiment_results.csv."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent

# MAE iz tablica 3-7 u radu (Diplomski-Toni_Jakelic_20.8_1.docx)
RAD = {
    "random": {
        "forward_fill":   [0.0521, 0.0741, 0.1012, 0.1366, 0.1549, 0.1648, 0.1722, 0.1970],
        "linear":         [0.0471, 0.0502, 0.0502, 0.0620, 0.0676, 0.0732, 0.0815, 0.0919],
        "cubic":          [0.0406, 0.0488, 0.0448, 0.0849, 0.0788, 0.0876, 0.0913, 0.1056],
        "knn":            [0.0865, 0.0841, 0.1016, 0.1304, 0.3761, 0.2792, 0.3915, 0.6353],
        "decision_tree":  [0.1568, 0.1662, 0.1633, 0.1693, 0.1729, 0.1861, 0.2082, 0.2824],
        "random_forest":  [0.1618, 0.1903, 0.1952, 0.2136, 0.2316, 0.2621, 0.2700, 0.2819],
    },
    "block": {
        "forward_fill":   [0.4883, 1.7912, 0.9838, 1.6503, 0.6913, 2.8020, 2.6239, 2.5757],
        "linear":         [0.1214, 0.2849, 0.4406, 0.6903, 0.7461, 0.6108, 0.7720, 0.6705],
        "cubic":          [0.3391, 0.1946, 0.4890, 1.1448, 1.8066, 1.8053, 1.7745, 1.8286],
        "knn":            [2.0580, 3.1533, 3.4313, 3.4468, 3.0574, 2.5015, 2.3487, 1.9468],
        "decision_tree":  [0.3173, 1.2948, 0.7618, 2.3168, 0.7364, 1.8812, 1.3845, 2.8560],
        "random_forest":  [0.5252, 1.9376, 0.9100, 1.3887, 0.8577, 2.7205, 2.6946, 2.5757],
    },
    "block_middle": {
        "linear":         [0.1674, 0.3654, 0.2554, 0.2665, 0.5473, 0.5395, 0.9671, 1.4370],
        "cubic":          [0.1513, 1.0215, 1.2902, 0.7192, 0.9723, 5.8078, 8.6021, 5.3329],
        "decision_tree":  [0.1081, 0.3651, 0.8338, 0.7853, 1.8916, 2.6106, 1.9831, 1.8817],
    },
}

IME = {"linear": "linear_interpolation", "cubic": "cubic_interpolation",
       "knn": "knn", "forward_fill": "forward_fill",
       "decision_tree": "decision_tree", "random_forest": "random_forest"}
RATES = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]


def main() -> None:
    res = pd.read_csv(ROOT / "results" / "experiment_results.csv")
    col = "mae_mean" if "mae_mean" in res.columns else "mae"
    print(f"aktualni CSV: {len(res)} redaka, stupac usporedbe: {col}")
    if "n_repeats" in res.columns:
        print(f"ponavljanja:  {int(res.n_repeats.max())}")
    print(f"metode u CSV-u ({res.method.nunique()}): {', '.join(sorted(res.method.unique()))}")

    u_radu = {"forward_fill", "linear_interpolation", "time_interpolation",
              "cubic_interpolation", "spline_interpolation", "knn",
              "decision_tree", "random_forest"}
    nedostaju = sorted(set(res.method.unique()) - u_radu)
    print(f"\nu CSV-u a NE u radu ({len(nedostaju)}): {', '.join(nedostaju)}")

    print()
    print("=" * 92)
    print("USPOREDBA MAE: rad naspram aktualnih rezultata")
    print("=" * 92)
    omjeri = []
    for scen, metode in RAD.items():
        print(f"\n--- {scen} ---")
        print(f"{'metoda':<18}{'rate':>6}{'rad':>10}{'sada':>10}{'omjer':>9}")
        for kratko, vrijednosti in metode.items():
            puno = IME[kratko]
            for rate, stara in zip(RATES, vrijednosti):
                r = res[(res.scenario == scen) & (res.method == puno)
                        & (res.missing_rate.round(2) == rate)]
                if r.empty:
                    continue
                nova = float(r[col].iloc[0])
                om = nova / stara if stara else float("nan")
                omjeri.append(om)
                if rate in (0.1, 0.4, 0.8):
                    print(f"{kratko:<18}{rate:>6.1f}{stara:>10.4f}{nova:>10.4f}{om:>9.1f}x")
    s = pd.Series(omjeri)
    print()
    print("=" * 92)
    print(f"omjer nova/stara po {len(s)} usporedenih celija:")
    print(f"  medijan {s.median():.1f}x   min {s.min():.1f}x   max {s.max():.1f}x")


if __name__ == "__main__":
    main()
