#!/usr/bin/env python3
"""
Tko pobjeduje u pojedinacnim testovima.

Vazno: linear_interpolation, time_interpolation i knn imaju po konstrukciji
identican MAE, a adaptive_imputation se na scenariju random svodi na linearnu,
pa je i ondje izjednacen. Naivni idxmin() bi pobjedu dodijelio prvoj metodi po
abecedi i dao posve krivu sliku. Zato se ovdje izjednacenja broje kao dijeljena
pobjeda (tolerancija 1e-9 C).
"""

from __future__ import annotations

import pandas as pd

LIN = ["linear_interpolation", "time_interpolation", "knn"]
ML = ["neural_net", "knn_upgraded", "random_forest", "decision_tree"]
OSTALO = ["moving_average", "cubic_interpolation", "spline_interpolation",
          "forward_fill", "adaptive_imputation"]
SCEN = ["random", "block", "block_start", "block_middle", "block_end"]
KEY = ["repeat", "scenario", "missing_rate"]
EPS = 1e-9


def main() -> None:
    runs = pd.read_csv("results/experiment_runs.csv")
    w = runs.pivot_table(index=KEY, columns="method", values="mae")
    best = w.min(axis=1)
    is_win = w.le(best + EPS, axis=0)
    n = len(w)

    print("=" * 86)
    print(f"1. TKO JE NAJBOLJI ILI IZJEDNACEN S NAJBOLJIM ({n} testova)")
    print("=" * 86)
    for grp, cols in [("linear (i istovjetne)", LIN), ("ML", ML), ("ostale klasicne", OSTALO)]:
        c = int(is_win[cols].any(axis=1).sum())
        print(f"  {grp:<26}{c:>5} / {n}   ({100 * c / n:>5.1f} %)")
    lin_or_ml = int(is_win[LIN + ML].any(axis=1).sum())
    print(f"\n  linear ILI ML medu najboljima: {100 * lin_or_ml / n:.1f} %")

    print()
    print("=" * 86)
    print("2. JEDINSTVENI POBJEDNIK (bez izjednacenja) — po metodi")
    print("=" * 86)
    unique = is_win.sum(axis=1) == 1
    sole = is_win[unique].idxmax(axis=1)
    print(f"  testova s jedinstvenim pobjednikom: {int(unique.sum())} / {n} "
          f"({100 * unique.mean():.1f} %)")
    for m, c in sole.value_counts().items():
        print(f"    {m:<24}{c:>5}  ({100 * c / int(unique.sum()):>5.1f} %)")

    print()
    print("=" * 86)
    print("3. UDIO TESTOVA U KOJIMA JE METODA NAJBOLJA ILI IZJEDNACENA")
    print("=" * 86)
    for m in sorted(w.columns, key=lambda x: -is_win[x].mean()):
        print(f"  {m:<24}{100 * is_win[m].mean():>6.1f} %")

    print()
    print("=" * 86)
    print("4. PO SCENARIJU: udio testova gdje je skupina najbolja ili izjednacena")
    print("=" * 86)
    print(f"{'scenarij':<14}{'linear':>12}{'ML':>12}{'ostale':>12}")
    for sc in SCEN:
        sel = is_win.xs(sc, level="scenario")
        print(f"{sc:<14}"
              f"{100 * sel[LIN].any(axis=1).mean():>11.1f}%"
              f"{100 * sel[ML].any(axis=1).mean():>11.1f}%"
              f"{100 * sel[OSTALO].any(axis=1).mean():>11.1f}%")

    print()
    print("=" * 86)
    print("5. GDJE MOVING_AVERAGE POBJEDUJE (po stopi nedostajanja)")
    print("=" * 86)
    ma_win = is_win["moving_average"] & ~is_win[LIN + ML].any(axis=1)
    tab = ma_win.reset_index().pivot_table(index="scenario", columns="missing_rate",
                                           values=0, aggfunc="sum")
    print(tab.to_string())
    adv = (w.loc[ma_win, LIN + ML].min(axis=1) - w.loc[ma_win, "moving_average"])
    print(f"\n  broj takvih pobjeda: {int(ma_win.sum())}")
    print(f"  prosjecna prednost pred najboljom linear/ML metodom: {adv.mean():.3f} C")


if __name__ == "__main__":
    main()
