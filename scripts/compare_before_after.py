#!/usr/bin/env python3
"""Usporedba MAE prije i poslije prerade ML metoda."""

from __future__ import annotations

import numpy as np
import pandas as pd

# Prosjecni MAE po scenariju iz verzije prije prerade (11 metoda).
BEFORE = {
    "knn": [0.236, 3.845, 3.220, 4.599, 6.794, 3.739],
    "knn_upgraded": [0.538, 5.105, 5.483, 6.164, 7.676, 4.993],
    "decision_tree": [0.608, 7.598, 3.328, 8.048, 6.425, 5.201],
    "random_forest": [0.761, 4.820, 3.427, 3.291, 7.313, 3.923],
}
ORDER = ["random", "block", "block_start", "block_middle", "block_end"]


def main() -> None:
    df = pd.read_csv("results/experiment_results.csv")
    piv = df.pivot_table(index="method", columns="scenario", values="mae")
    piv["PROSJEK"] = df.groupby("method").mae.mean()
    piv = piv[ORDER + ["PROSJEK"]].sort_values("PROSJEK")

    print("=" * 92)
    print("SVE METODE — prosjecni MAE (C) po scenariju")
    print("=" * 92)
    hdr = f"{'metoda':<24}" + "".join(f"{c[:9]:>10}" for c in ORDER) + f"{'PROSJEK':>10}"
    print(hdr)
    print("-" * len(hdr))
    for m, row in piv.iterrows():
        star = "  <= referenca" if m == "linear_interpolation" else ""
        print(f"{m:<24}" + "".join(f"{row[c]:>10.3f}" for c in ORDER)
              + f"{row['PROSJEK']:>10.3f}{star}")

    print()
    print("=" * 92)
    print("ML METODE — prije i poslije prerade")
    print("=" * 92)
    hdr2 = (f"{'metoda':<20}{'verzija':<10}" + "".join(f"{c[:9]:>10}" for c in ORDER)
            + f"{'PROSJEK':>10}{'promjena':>11}")
    print(hdr2)
    print("-" * len(hdr2))
    for m, before in BEFORE.items():
        after = [piv.loc[m, c] for c in ORDER] + [piv.loc[m, "PROSJEK"]]
        gain = (before[5] - after[5]) / before[5] * 100.0
        print(f"{m:<20}{'prije':<10}" + "".join(f"{v:>10.3f}" for v in before[:5])
              + f"{before[5]:>10.3f}")
        print(f"{'':<20}{'poslije':<10}" + "".join(f"{v:>10.3f}" for v in after[:5])
              + f"{after[5]:>10.3f}{gain:>10.1f}%")

    nn = [piv.loc["neural_net", c] for c in ORDER] + [piv.loc["neural_net", "PROSJEK"]]
    print(f"{'neural_net':<20}{'NOVO':<10}" + "".join(f"{v:>10.3f}" for v in nn[:5])
          + f"{nn[5]:>10.3f}")

    print()
    print("=" * 92)
    print("POBJEDE NAD LINEARNOM INTERPOLACIJOM (od 40 kombinacija scenarij x rate)")
    print("=" * 92)
    lin = df[df.method == "linear_interpolation"].set_index(["scenario", "missing_rate"]).mae
    for m in ["neural_net", "decision_tree", "random_forest", "knn", "knn_upgraded",
              "moving_average", "cubic_interpolation", "forward_fill"]:
        sub = df[df.method == m].set_index(["scenario", "missing_rate"]).mae
        joined = pd.concat([sub.rename("m"), lin.rename("lin")], axis=1).dropna()
        wins = int((joined.m < joined.lin).sum())
        skill = float(np.median(1.0 - joined.m / joined.lin))
        print(f"  {m:<22} pobjeda: {wins:>2}/40   medijan skill score: {skill:+.3f}")


if __name__ == "__main__":
    main()
