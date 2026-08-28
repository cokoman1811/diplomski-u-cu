#!/usr/bin/env python3
"""
Testovi znacajnosti nad ponovljenim eksperimentom (results/experiment_runs.csv).

Dizajn je UPAREN: unutar jednog ponavljanja sve metode vide identican osteceni
niz, pa se usporeduje razlika po paru (isti tjedan, isti scenarij, ista stopa,
ista maska). Uparena razlika ima bitno manju varijancu od dviju srednjih
vrijednosti zasebno, pa je to jedini nacin da se male razlike uopce testiraju.

Test: Wilcoxonov test predznacenih rangova (ne pretpostavlja normalnost).
Interval: bootstrap percentilni 95 % interval srednje razlike.
Korekcija: Holm-Bonferroni preko svih usporedenih metoda.

Koristenje:
    python scripts/significance.py [referentna_metoda]
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "results" / "experiment_runs.csv"
OUT_MD = ROOT / "results" / "znacajnost.md"
OUT_CSV = ROOT / "results" / "tablice" / "znacajnost.csv"

KEY = ["repeat", "scenario", "missing_rate"]
SCEN = ["random", "block", "block_start", "block_middle", "block_end"]
BOOT = 10000
RNG = np.random.default_rng(42)


def bootstrap_ci(diff: np.ndarray, n_boot: int = BOOT) -> tuple[float, float]:
    idx = RNG.integers(0, len(diff), size=(n_boot, len(diff)))
    means = diff[idx].mean(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def holm(pvals: list[float]) -> list[float]:
    """Holm-Bonferroni prilagodene p-vrijednosti."""
    m = len(pvals)
    order = np.argsort(pvals)
    adj = np.empty(m)
    running = 0.0
    for rank, i in enumerate(order):
        val = (m - rank) * pvals[i]
        running = max(running, val)
        adj[i] = min(running, 1.0)
    return adj.tolist()


def paired_table(df: pd.DataFrame, ref: str, methods: list[str]) -> pd.DataFrame:
    wide = df.pivot_table(index=KEY, columns="method", values="mae")
    rows = []
    for m in methods:
        pair = wide[[m, ref]].dropna()
        diff = (pair[m] - pair[ref]).to_numpy()
        n = len(diff)
        nonzero = diff[diff != 0.0]

        if len(nonzero) == 0:
            rows.append(
                {
                    "metoda": m,
                    "n_parova": n,
                    "srednja_razlika": 0.0,
                    "ci95_lo": 0.0,
                    "ci95_hi": 0.0,
                    "pobjeda": 0,
                    "poraz": 0,
                    "nerijeseno": n,
                    "p": 1.0,
                }
            )
            continue

        lo, hi = bootstrap_ci(diff)
        _, p = stats.wilcoxon(nonzero, alternative="two-sided")
        rows.append(
            {
                "metoda": m,
                "n_parova": n,
                "srednja_razlika": float(diff.mean()),
                "ci95_lo": lo,
                "ci95_hi": hi,
                "pobjeda": int((diff < 0).sum()),
                "poraz": int((diff > 0).sum()),
                "nerijeseno": int((diff == 0).sum()),
                "p": float(p),
            }
        )

    out = pd.DataFrame(rows)
    out["p_holm"] = holm(out["p"].tolist())
    out["znacajno"] = np.where(
        out.p_holm >= 0.05, "ne",
        np.where(out.srednja_razlika < 0, "DA (bolja)", "DA (losija)"),
    )
    return out


def main() -> int:
    if not RUNS.exists():
        print(f"Nema {RUNS}. Pokreni: diplomski.exe --experiment-all --repeats 20")
        return 1

    ref = sys.argv[1] if len(sys.argv) > 1 else "linear_interpolation"
    df = pd.read_csv(RUNS)
    n_reps = df["repeat"].nunique()
    methods = [m for m in sorted(df.method.unique()) if m != ref]

    print("=" * 96)
    print(f"UPARENA USPOREDBA S REFERENCOM: {ref}")
    print(f"{n_reps} ponavljanja x {df.scenario.nunique()} scenarija x "
          f"{df.missing_rate.nunique()} stopa = {len(df) // df.method.nunique()} parova")
    print("=" * 96)
    print("Negativna razlika = metoda je BOLJA od reference.\n")

    overall = paired_table(df, ref, methods).sort_values("srednja_razlika")
    hdr = (f"{'metoda':<22}{'d MAE':>9}{'95% CI':>20}{'W-L-T':>14}"
           f"{'p (Holm)':>11}  znacajno")
    print(hdr)
    print("-" * len(hdr))
    for _, r in overall.iterrows():
        ci = f"[{r.ci95_lo:+.3f}, {r.ci95_hi:+.3f}]"
        wlt = f"{r.pobjeda}-{r.poraz}-{r.nerijeseno}"
        print(f"{r.metoda:<22}{r.srednja_razlika:>+9.4f}{ci:>20}{wlt:>14}"
              f"{r.p_holm:>11.2e}  {r.znacajno}")

    per_scen = []
    print()
    print("=" * 96)
    print("PO SCENARIJIMA (srednja uparena razlika u MAE prema referenci)")
    print("=" * 96)
    ml = [m for m in ["neural_net", "random_forest", "decision_tree", "knn_upgraded",
                      "adaptive_imputation"] if m in methods]
    print(f"{'scenarij':<14}" + "".join(f"{m[:13]:>15}" for m in ml))
    print("-" * (14 + 15 * len(ml)))
    for sc in SCEN:
        sub = df[df.scenario == sc]
        tab = paired_table(sub, ref, ml).set_index("metoda")
        cells = []
        for m in ml:
            d = tab.loc[m, "srednja_razlika"]
            star = "*" if tab.loc[m, "p_holm"] < 0.05 else " "
            cells.append(f"{d:>+14.4f}{star}")
            per_scen.append({"scenarij": sc, "metoda": m,
                             "srednja_razlika": d,
                             "p_holm": tab.loc[m, "p_holm"]})
        print(f"{sc:<14}" + "".join(cells))
    print("\n* = znacajno na 0,05 nakon Holmove korekcije")

    print()
    print("=" * 96)
    print("VARIJABILNOST: koliko rezultat ovisi o odabranom tjednu")
    print("=" * 96)
    per_win = df.groupby(["method", "repeat"]).mae.mean().unstack()
    for m in [ref] + ml:
        v = per_win.loc[m]
        print(f"  {m:<22} MAE po tjednu: {v.min():.3f} .. {v.max():.3f}  "
              f"(sd {v.std():.3f}, prosjek {v.mean():.3f})")

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    overall.to_csv(OUT_CSV, index=False)

    lines = [
        "# Testovi znacajnosti (upareni)",
        "",
        f"Referenca: `{ref}`. Ponavljanja: **{n_reps}** tjednih prozora, svaki sa "
        "svojim seedom maske.",
        "",
        "Dizajn je uparen: unutar jednog ponavljanja sve metode dobivaju identican "
        "osteceni niz, pa se usporeduju razlike po paru. Test je Wilcoxonov test "
        "predznacenih rangova, interval je bootstrap percentilni 95 %, a "
        "p-vrijednosti su korigirane Holm-Bonferroni postupkom.",
        "",
        "Negativna razlika znaci da je metoda **bolja** od reference.",
        "",
        "| Metoda | Δ MAE (°C) | 95 % CI | Pobjeda–poraz–nerijeseno | p (Holm) | Znacajno |",
        "|--------|-----------|---------|--------------------------|----------|----------|",
    ]
    for _, r in overall.iterrows():
        lines.append(
            f"| `{r.metoda}` | {r.srednja_razlika:+.4f} | "
            f"[{r.ci95_lo:+.4f}, {r.ci95_hi:+.4f}] | "
            f"{r.pobjeda}–{r.poraz}–{r.nerijeseno} | {r.p_holm:.2e} | {r.znacajno} |"
        )
    lines += ["", "## Po scenarijima", "",
              "| Scenarij | " + " | ".join(f"`{m}`" for m in ml) + " |",
              "|---|" + "---|" * len(ml)]
    ps = pd.DataFrame(per_scen)
    for sc in SCEN:
        sub = ps[ps.scenarij == sc].set_index("metoda")
        cells = []
        for m in ml:
            star = " \\*" if sub.loc[m, "p_holm"] < 0.05 else ""
            cells.append(f"{sub.loc[m, 'srednja_razlika']:+.4f}{star}")
        lines.append(f"| {sc} | " + " | ".join(cells) + " |")
    lines += ["", "\\* = znacajno na razini 0,05 nakon Holmove korekcije", ""]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print()
    print(f"Zapisano: {OUT_MD.relative_to(ROOT)}")
    print(f"Zapisano: {OUT_CSV.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
