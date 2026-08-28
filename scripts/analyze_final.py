#!/usr/bin/env python3
"""Presjeci ponovljenog eksperimenta za raspravu u diplomskom radu."""

from __future__ import annotations

import numpy as np
import pandas as pd

SCEN = ["random", "block", "block_start", "block_middle", "block_end"]
REF = "linear_interpolation"
ML = ["neural_net", "knn_upgraded", "random_forest", "decision_tree"]
KEY = ["repeat", "scenario", "missing_rate"]


def main() -> None:
    runs = pd.read_csv("results/experiment_runs.csv")
    idx = pd.read_csv("data/processed/jena_windows/index.csv")
    n_rep = runs["repeat"].nunique()
    sd_all = float(idx.sd_temp.mean())

    print("=" * 96)
    print(f"1. UKUPNI RANG ({n_rep} tjedana x 5 scenarija x 8 stopa = "
          f"{len(runs) // runs.method.nunique()} testova po metodi)")
    print("=" * 96)
    piv = runs.pivot_table(index="method", columns="scenario", values="mae")
    piv["PROSJEK"] = runs.groupby("method").mae.mean()
    piv["nMAE"] = piv["PROSJEK"] / sd_all
    piv = piv[SCEN + ["PROSJEK", "nMAE"]].sort_values("PROSJEK")
    hdr = f"{'metoda':<23}" + "".join(f"{c[:9]:>10}" for c in SCEN) + f"{'PROSJEK':>10}{'nMAE':>8}"
    print(hdr)
    print("-" * len(hdr))
    for m, row in piv.iterrows():
        mark = "  <-- referenca" if m == REF else ""
        print(f"{m:<23}" + "".join(f"{row[c]:>10.3f}" for c in SCEN)
              + f"{row['PROSJEK']:>10.4f}{row['nMAE']:>8.3f}{mark}")

    print()
    print("=" * 96)
    print("2. UPARENA RAZLIKA PREMA LINEARNOJ, PO STOPI NEDOSTAJUCIH VRIJEDNOSTI")
    print("=" * 96)
    wide = runs.pivot_table(index=KEY, columns="method", values="mae")
    rates = sorted(runs.missing_rate.unique())
    print(f"{'metoda':<20}" + "".join(f"{r:>9.0%}" for r in rates))
    print("-" * (20 + 9 * len(rates)))
    for m in ML:
        cells = []
        for r in rates:
            sel = wide.xs(r, level="missing_rate")
            cells.append(f"{(sel[m] - sel[REF]).mean():>+9.4f}")
        print(f"{m:<20}" + "".join(cells))
    print("\nNegativno = ML bolji. Pozitivno = linearna bolja.")

    print()
    print("=" * 96)
    print("3. UDIO TESTOVA U KOJIMA JE RAZLIKA PREMA LINEARNOJ MANJA OD 0,01 C")
    print("=" * 96)
    for m in ML + ["moving_average", "forward_fill", "adaptive_imputation"]:
        d = (wide[m] - wide[REF]).abs()
        print(f"  {m:<22} |d| < 0,01: {100 * (d < 0.01).mean():>5.1f} %   "
              f"|d| < 0,10: {100 * (d < 0.10).mean():>5.1f} %   "
              f"medijan |d|: {d.median():.4f}")

    print()
    print("=" * 96)
    print("4. NAJBOLJA METODA PO KOMBINACIJI (svih 800 testova)")
    print("=" * 96)
    best = runs.loc[runs.groupby(KEY).mae.idxmin()]
    vc = best.method.value_counts()
    for m, c in vc.items():
        print(f"  {m:<24}{c:>5} / {len(best)}  ({100 * c / len(best):>5.1f} %)")
    print("\n  Napomena: linear = time = knn imaju identican MAE, pa se pobjeda")
    print("  dodjeljuje prvoj po redu u tablici — trojka zajedno drzi ta mjesta.")

    print()
    print("=" * 96)
    print("5. STABILNOST: koliko se rang mijenja od tjedna do tjedna")
    print("=" * 96)
    per_win = runs.groupby(["repeat", "method"]).mae.mean().unstack()
    ranks = per_win.rank(axis=1)
    for m in [REF] + ML + ["adaptive_imputation"]:
        rr = ranks[m]
        print(f"  {m:<22} rang po tjednu: {int(rr.min())}. - {int(rr.max())}."
              f"   prosjek {rr.mean():.2f}   prvi u {int((rr == rr.min().min()).sum())} tjedana")

    print()
    print("=" * 96)
    print("6. R2 PO SCENARIJU (i dalje neupotrebljiv na blokovima)")
    print("=" * 96)
    for sc in SCEN:
        sub = runs[runs.scenario == sc]
        print(f"  {sc:<14} negativnih {int((sub.r2 < 0).sum()):>5}/{len(sub):<6}"
              f" medijan {sub.r2.median():>8.3f}   min {sub.r2.min():>12.1f}")

    print()
    print("=" * 96)
    print("7. GDJE JE POGRESKA NAJVECA (prosjek svih metoda osim spline/cubic)")
    print("=" * 96)
    core = runs[~runs.method.isin(["cubic_interpolation", "spline_interpolation",
                                   "adaptive_imputation"])]
    hm = core.pivot_table(index="scenario", columns="missing_rate", values="mae")
    print(f"{'scenarij':<14}" + "".join(f"{c:>9.0%}" for c in hm.columns))
    for sc in SCEN:
        print(f"{sc:<14}" + "".join(f"{hm.loc[sc, c]:>9.3f}" for c in hm.columns))


if __name__ == "__main__":
    main()
