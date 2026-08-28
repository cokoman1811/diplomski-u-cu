#!/usr/bin/env python3
"""Presjeci rezultata za raspravu: gdje ML dobiva, gdje gubi i koliko."""

from __future__ import annotations

import numpy as np
import pandas as pd

SCEN = ["random", "block", "block_start", "block_middle", "block_end"]
ML = ["neural_net", "random_forest", "decision_tree", "knn_upgraded"]


def main() -> None:
    df = pd.read_csv("results/experiment_results.csv")
    lin = df[df.method == "linear_interpolation"].set_index(["scenario", "missing_rate"]).mae

    print("=" * 78)
    print("1. MAE po missing rateu — neural_net vs linear (svi scenariji zajedno)")
    print("=" * 78)
    print(f"{'rate':>6}{'linear':>10}{'neural_net':>12}{'razlika':>10}{'skill':>9}")
    for r in sorted(df.missing_rate.unique()):
        a = df[(df.method == "linear_interpolation") & (df.missing_rate == r)].mae.mean()
        b = df[(df.method == "neural_net") & (df.missing_rate == r)].mae.mean()
        print(f"{r:>6.0%}{a:>10.3f}{b:>12.3f}{b - a:>+10.3f}{1 - b / a:>+9.3f}")

    print()
    print("=" * 78)
    print("2. Skill score neuronske mreze po scenariju i rateu (+ = bolja od linear)")
    print("=" * 78)
    nn = df[df.method == "neural_net"].set_index(["scenario", "missing_rate"]).mae
    tab = pd.concat([nn.rename("nn"), lin.rename("lin")], axis=1)
    tab["skill"] = 1 - tab.nn / tab.lin
    piv = tab.skill.unstack(level=1)
    print(f"{'scenarij':<14}" + "".join(f"{c:>9.0%}" for c in piv.columns))
    for s in SCEN:
        print(f"{s:<14}" + "".join(f"{piv.loc[s, c]:>+9.3f}" for c in piv.columns))

    print()
    print("=" * 78)
    print("3. Koliko su ML metode medusobno slicne (korelacija MAE po testovima)")
    print("=" * 78)
    wide = df.pivot_table(index=["scenario", "missing_rate"], columns="method", values="mae")
    cols = ML + ["linear_interpolation"]
    print(wide[cols].corr().round(4).to_string())

    print()
    print("=" * 78)
    print("4. Raspon MAE medu 5 najboljih metoda (koliko je natjecanje tijesno)")
    print("=" * 78)
    top = ["neural_net", "random_forest", "decision_tree", "knn_upgraded",
           "linear_interpolation"]
    for s in SCEN:
        sub = df[(df.scenario == s) & (df.method.isin(top))].groupby("method").mae.mean()
        spread = sub.max() - sub.min()
        print(f"  {s:<14} min {sub.min():.3f}  max {sub.max():.3f}  "
              f"raspon {spread:.3f} C  ({spread / sub.min() * 100:.1f} %)")

    print()
    print("=" * 78)
    print("5. R2: koliko je negativnih po scenariju (problem metrike)")
    print("=" * 78)
    for s in SCEN:
        sub = df[df.scenario == s]
        neg = int((sub.r2 < 0).sum())
        print(f"  {s:<14} negativnih {neg:>3}/{len(sub):<4} min {sub.r2.min():>10.2f}"
              f"  max {sub.r2.max():>7.3f}")

    print()
    print("=" * 78)
    print("6. Najbolja metoda po svakoj kombinaciji (bez adaptive)")
    print("=" * 78)
    noad = df[df.method != "adaptive_imputation"]
    win = noad.loc[noad.groupby(["scenario", "missing_rate"]).mae.idxmin()]
    print(win.method.value_counts().to_string())

    print()
    print("=" * 78)
    print("7. Prosjecna |pogreska| u kontekstu signala")
    print("=" * 78)
    ts = pd.read_csv("data/processed/jena_temperature_7d.csv")
    col = [c for c in ts.columns if "T" in c or "temp" in c.lower()][-1]
    v = ts[col].to_numpy(dtype=float)
    sd = float(np.std(v))
    print(f"  sd cijelog niza:            {sd:.4f} C")
    print(f"  raspon:                     {v.max() - v.min():.4f} C")
    print(f"  prosjecna |promjena| 10 min: {np.mean(np.abs(np.diff(v))):.4f} C")
    print(f"  lag-1 autokorelacija:       {np.corrcoef(v[:-1], v[1:])[0, 1]:.6f}")
    for m in ["neural_net", "linear_interpolation", "forward_fill"]:
        mm = df[df.method == m].mae.mean()
        print(f"  nMAE ({m:<20}) = {mm / sd:.4f}")


if __name__ == "__main__":
    main()
