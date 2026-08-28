#!/usr/bin/env python3
"""Neovisna provjera C implementacija: replicira masku i KNN, usporeduje s CSV-om.

Cilj je utvrditi:
  1. reproducira li vjerna Python replika iste brojke kao C (validacija implementacije)
  2. aktivira li se ikad fill_remaining_gaps
  3. dominira li pozicija nad satom/danom u knn (i obrnuto u knn_upgraded)
"""

from __future__ import annotations

import numpy as np
import pandas as pd

MASK64 = (1 << 64) - 1


class Xorshift64:
    """Isti PRNG kao u src/preprocessing.c."""

    def __init__(self, seed: int) -> None:
        self.state = seed if seed else 0x9E3779B97F4A7C15

    def next(self) -> int:
        x = self.state
        x ^= (x << 13) & MASK64
        x ^= x >> 7
        x ^= (x << 17) & MASK64
        self.state = x & MASK64
        return self.state

    def below(self, bound: int) -> int:
        return self.next() % bound


def create_missing_random(n: int, rate: float, seed: int = 42) -> np.ndarray:
    """Replika create_missing_values() iz preprocessing.c."""
    eligible = list(range(1, n - 1))
    eligible_count = n - 2
    n_remove = int(np.round(rate * n))
    n_remove = min(n_remove, eligible_count)

    rng = Xorshift64(seed)
    for i in range(n_remove):
        j = i + rng.below(eligible_count - i)
        eligible[i], eligible[j] = eligible[j], eligible[i]

    mask = np.zeros(n, dtype=bool)
    mask[eligible[:n_remove]] = True
    return mask


def create_single_block(n: int, rate: float, position: str, seed: int = 42) -> np.ndarray:
    """Replika create_single_block_missing_values() iz preprocessing.c."""
    block_size = max(1, int(np.round(rate * n)))
    block_size = min(block_size, n - 2)
    min_start, max_start = 1, n - 1 - block_size

    if position == "start":
        start = min_start
    elif position == "end":
        start = max_start
    elif position == "middle":
        start = min_start + (max_start - min_start) // 2
    else:
        start = min_start + Xorshift64(seed).below(max_start - min_start + 1)

    mask = np.zeros(n, dtype=bool)
    mask[start:start + block_size] = True
    return mask


def knn_impute(temp, hour, yday, mask, k=5):
    """Replika knn_imputation() — ukljucujuci redoslijed umetanja i ponasanje kod izjednacenja."""
    n = len(temp)
    known = np.where(~mask)[0]
    out = temp.copy()
    k = min(k, len(known))

    kh, ky = hour[known].astype(float), yday[known].astype(float)
    kpos = known.astype(float)

    n_unfilled = 0
    for i in np.where(mask)[0]:
        d = (kpos - i) ** 2 + (kh - hour[i]) ** 2 + (ky - yday[i]) ** 2
        # stabilan argsort = kod izjednacenja pobjeduje manji indeks, kao u C-u
        nb = known[np.argsort(d, kind="stable")[:k]]
        val = temp[nb].mean()
        if np.isnan(val):
            n_unfilled += 1
        out[i] = val
    return out, n_unfilled


def mae(truth, pred, mask):
    return np.abs(truth[mask] - pred[mask]).mean()


def main() -> None:
    df = pd.read_csv("data/processed/jena_temperature_7d.csv")
    temp = df["temperature"].to_numpy(dtype=float)
    ts = pd.to_datetime(df["timestamp"])
    hour = ts.dt.hour.to_numpy()
    yday = ts.dt.dayofyear.to_numpy()
    n = len(temp)

    res = pd.read_csv("results/experiment_results.csv")

    print("=" * 68)
    print("1. VALIDACIJA: Python replika vs C rezultat (metoda knn)")
    print("=" * 68)
    print(f"{'scenarij':<14}{'rate':>6}{'C (CSV)':>12}{'Python':>12}{'razlika':>12}")

    scenarios = [
        ("random", None),
        ("block", "random"),
        ("block_start", "start"),
        ("block_middle", "middle"),
        ("block_end", "end"),
    ]
    total_unfilled = 0
    diffs = []
    for scen, pos in scenarios:
        for rate in [0.10, 0.20, 0.50, 0.80]:
            m = create_missing_random(n, rate) if pos is None else create_single_block(n, rate, pos)
            pred, unfilled = knn_impute(temp, hour, yday, m)
            total_unfilled += unfilled
            py_mae = mae(temp, pred, m)

            row = res[(res.scenario == scen) & (res.missing_rate == rate) & (res.method == "knn")]
            c_mae = row.mae.iloc[0] if len(row) else np.nan
            diffs.append(abs(c_mae - py_mae))
            print(f"{scen:<14}{rate:>6.0%}{c_mae:>12.4f}{py_mae:>12.4f}{c_mae - py_mae:>12.6f}")

    print(f"\nnajveca razlika: {max(diffs):.6f} C")
    print(f"broj NaN-ova koje bi fill_remaining_gaps morao popuniti: {total_unfilled}")

    print()
    print("=" * 68)
    print("2. DOMINACIJA ZNACAJKI U KNN (udaljenost na kvadrat)")
    print("=" * 68)
    print("knn (neskalirano: pozicija u uzorcima, sat 0-23, yday):")
    print(f"  susjed 1 uzorak dalje (10 min):        d^2 = {1**2:>10.4f}")
    print(f"  susjed 1 sat dalje (6 uzoraka):        d^2 = {6**2 + 1:>10.4f}")
    print(f"  isti sat, 1 dan dalje (144 uzorka):    d^2 = {144**2 + 0 + 1:>10.4f}")
    print("  => pozicija potpuno dominira; sat i dan su zanemarivi")

    print("\nknn_upgraded (position_norm 0..1, hour_sin/cos * 2.0, yday_sin/cos * 1.0):")
    denom = n - 1
    two_pi = 2 * np.pi

    def up_feat(idx):
        ha, ya = two_pi * hour[idx] / 24.0, two_pi * (yday[idx] - 1) / 365.0
        return np.array([idx / denom, np.sin(ha), np.cos(ha), np.sin(ya), np.cos(ya)])

    w = np.array([1.0, 2.0, 2.0, 1.0, 1.0])
    ref = 500
    for label, other in [
        ("susjed 6 uzoraka dalje (1 sat)", ref + 6),
        ("susjed 12 uzoraka dalje (2 sata)", ref + 12),
        ("isti sat, 1 dan dalje (144 uzorka)", ref + 144),
        ("isti sat, 2 dana dalje (288 uzoraka)", ref + 288),
    ]:
        d2 = (((up_feat(ref) - up_feat(other)) * w) ** 2).sum()
        print(f"  {label:<38} d^2 = {d2:>10.5f}")
    print("  => tocka udaljena CIJELI DAN moze biti 'bliza' od one 1 sat dalje")


if __name__ == "__main__":
    main()
