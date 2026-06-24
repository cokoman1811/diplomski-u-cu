#!/usr/bin/env python3
"""
Generira grafove i tekstualnu analizu iz results/*.csv.

Koristenje (iz korijena projekta):
    python scripts/report.py

Preduvjet: results/experiment_results.csv (pokreni diplomski --experiment).
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
FIGURES = ROOT / "slike i videa" / "2026" / "diplomski-grafovi"
FIGURES_DISPLAY = "slike i videa/2026/diplomski-grafovi"
EXPERIMENT_CSV = RESULTS / "experiment_results.csv"
ANALYSIS_MD = RESULTS / "analysis.md"

CLASSICAL = {
    "forward_fill",
    "linear_interpolation",
    "time_interpolation",
    "cubic_interpolation",
    "spline_interpolation",
}
ML = {"knn", "decision_tree", "random_forest"}

# Metode na linijskim grafovima (citoljivo, ne svih 8 odjednom).
LINE_METHODS = [
    "linear_interpolation",
    "spline_interpolation",
    "knn",
    "random_forest",
]

SNAPSHOT_RATE = 0.20


def require_pandas_matplotlib():
    try:
        import pandas  # noqa: F401
        import matplotlib  # noqa: F401
    except ImportError:
        print("Instaliraj ovisnosti: pip install -r scripts/requirements.txt")
        sys.exit(1)


def load_experiment():
    import pandas as pd

    if not EXPERIMENT_CSV.exists():
        print(f"Nema {EXPERIMENT_CSV}")
        print("Prvo pokreni: diplomski.exe --experiment --source jena_quick")
        sys.exit(1)
    return pd.read_csv(EXPERIMENT_CSV)


def ensure_dirs():
    FIGURES.mkdir(parents=True, exist_ok=True)
    RESULTS.mkdir(parents=True, exist_ok=True)


def plot_mae_bars(df, scenario: str, rate: float, out_path: Path):
    import matplotlib.pyplot as plt

    sub = df[(df["scenario"] == scenario) & (df["missing_rate"] == rate)].copy()
    if sub.empty:
        return False

    sub = sub.sort_values("mae")
    colors = ["#4C78A8" if m in CLASSICAL else "#F58518" for m in sub["method"]]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sub["method"], sub["mae"], color=colors)
    ax.set_ylabel("MAE (°C)")
    ax.set_title(f"MAE po metodama — {scenario} missing, {rate:.0%}")
    ax.tick_params(axis="x", rotation=35)
    plt.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return True


def plot_mae_vs_rate(df, scenario: str, out_path: Path):
    import matplotlib.pyplot as plt

    sub = df[(df["scenario"] == scenario) & (df["method"].isin(LINE_METHODS))]
    if sub.empty:
        return False

    fig, ax = plt.subplots(figsize=(8, 5))
    for method in LINE_METHODS:
        m = sub[sub["method"] == method]
        if m.empty:
            continue
        m = m.sort_values("missing_rate")
        ax.plot(m["missing_rate"] * 100, m["mae"], marker="o", label=method)

    ax.set_xlabel("Missing rate (%)")
    ax.set_ylabel("MAE (°C)")
    ax.set_title(f"MAE vs missing rate — {scenario}")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return True


def plot_reconstruction(csv_path: Path, out_path: Path, title: str):
    import matplotlib.pyplot as plt
    import pandas as pd

    if not csv_path.exists():
        return False

    df = pd.read_csv(csv_path)
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df["index"], df["original"], label="original", color="#1f77b4", linewidth=1.2)
    ax.plot(df["index"], df["reconstructed"], label="rekonstruirano", color="#ff7f0e", linewidth=1.2)

    masked = df[df["mask"] == 1]
    if not masked.empty:
        ax.scatter(
            masked["index"],
            masked["original"],
            s=12,
            color="red",
            alpha=0.5,
            label="maskirano (original)",
            zorder=3,
        )

    ax.set_xlabel("Indeks")
    ax.set_ylabel("Temperatura (°C)")
    ax.set_title(title)
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return True


def fmt_table(df) -> str:
  lines = ["| metoda | MAE | RMSE | R² |", "|--------|-----|------|-----|"]
  for _, row in df.iterrows():
      lines.append(
          f"| {row['method']} | {row['mae']:.4f} | {row['rmse']:.4f} | {row['r2']:.4f} |"
      )
  return "\n".join(lines)


def best_method(df, scenario: str, rate: float) -> str:
    sub = df[(df["scenario"] == scenario) & (df["missing_rate"] == rate)]
    if sub.empty:
        return "—"
    return sub.loc[sub["mae"].idxmin(), "method"]


def group_mean_mae(df, scenario: str, rate: float, methods: set) -> float:
    sub = df[
        (df["scenario"] == scenario)
        & (df["missing_rate"] == rate)
        & (df["method"].isin(methods))
    ]
    if sub.empty:
        return float("nan")
    return sub["mae"].mean()


def write_analysis(df) -> None:
    random_20 = df[(df["scenario"] == "random") & (df["missing_rate"] == SNAPSHOT_RATE)].sort_values(
        "mae"
    )
    block_20 = df[(df["scenario"] == "block") & (df["missing_rate"] == SNAPSHOT_RATE)].sort_values(
        "mae"
    )

    best_random = best_method(df, "random", SNAPSHOT_RATE)
    best_block = best_method(df, "block", SNAPSHOT_RATE)

    cls_random = group_mean_mae(df, "random", SNAPSHOT_RATE, CLASSICAL)
    ml_random = group_mean_mae(df, "random", SNAPSHOT_RATE, ML)
    cls_block = group_mean_mae(df, "block", SNAPSHOT_RATE, CLASSICAL)
    ml_block = group_mean_mae(df, "block", SNAPSHOT_RATE, ML)

    knn_block_50 = df[
        (df["scenario"] == "block")
        & (df["missing_rate"] == 0.50)
        & (df["method"] == "knn")
    ]
    knn_50_mae = knn_block_50["mae"].iloc[0] if not knn_block_50.empty else float("nan")

    text = f"""# Analiza rezultata eksperimenata

Automatski generirano iz `experiment_results.csv`.

## Sažetak

- **Random missing ({SNAPSHOT_RATE:.0%}):** najbolja metoda — **{best_random}**
- **Block missing ({SNAPSHOT_RATE:.0%}):** najbolja metoda — **{best_block}**
- **Klasične vs ML (prosjek MAE, random {SNAPSHOT_RATE:.0%}):** {cls_random:.4f} vs {ml_random:.4f}
- **Klasične vs ML (prosjek MAE, block {SNAPSHOT_RATE:.0%}):** {cls_block:.4f} vs {ml_block:.4f}

## Tablica — random missing, {SNAPSHOT_RATE:.0%}

{fmt_table(random_20)}

## Tablica — block missing, {SNAPSHOT_RATE:.0%}

{fmt_table(block_20)}

## Najbolja metoda po scenariju i missing rateu

| scenarij | 10% | 20% | 30% | 40% | 50% |
|----------|-----|-----|-----|-----|-----|
| random | {best_method(df, "random", 0.10)} | {best_method(df, "random", 0.20)} | {best_method(df, "random", 0.30)} | {best_method(df, "random", 0.40)} | {best_method(df, "random", 0.50)} |
| block | {best_method(df, "block", 0.10)} | {best_method(df, "block", 0.20)} | {best_method(df, "block", 0.30)} | {best_method(df, "block", 0.40)} | {best_method(df, "block", 0.50)} |

## Ključni nalazi (za poglavlje Rezultati)

1. **Klasične interpolacijske metode** (posebno linear, spline, cubic) postižu najniži MAE na random scenariju za sve testirane missing rateove.
2. **Linear i time interpolacija** daju identične rezultate jer su uzorci ravnomjerno raspoređeni u vremenu (Jena 10-min intervali).
3. Na **block scenariju** linear/time i dalje vode; forward fill i cubic/spline znatno gore zbog dugačkih rupa.
4. **ML metode** (KNN, decision tree, random forest) na ovom datasetu (288 uzoraka) **ne nadmašuju** klasične metode.
5. **KNN** na block scenariju pokazuje najveću pogrešku (npr. MAE ≈ {knn_50_mae:.2f} pri 50% block) — ne koristi dovoljno lokalnu vremensku strukturu za dugačke blokove.
6. Pri **50% random missing** KNN pokazuje nagli porast pogreške — premalo poznatih uzoraka za pouzdan model.

## Usporedba scenarija random vs block

Block missing simulira kvar senzora (kontinuirani interval bez podataka). U tom scenariju:
- metode koje koriste **susjedne poznate točke** (linear, time) ostaju najstabilnije;
- **forward fill** daje ravnu liniju kroz blok → veći MAE;
- **ML** uči globalne obrasce (sat, dan) ali ne popunjava lokalni trend iz susjedstva kao interpolacija.

## Grafovi (mapa `{FIGURES_DISPLAY}/`)

| Datoteka | Opis |
|----------|------|
| `mae_by_method_random_20.png` | Stupčasti graf MAE, random 20% |
| `mae_by_method_block_20.png` | Stupčasti graf MAE, block 20% |
| `mae_vs_rate_random.png` | MAE vs missing rate, random |
| `mae_vs_rate_block.png` | MAE vs missing rate, block |
| `reconstruction_linear_*_20.png` | Original vs rekonstruirano (linear) |

## Nacrt zaključka (ručno doradi za rad)

Na testiranom Jena datasetu (48 h, 10-min intervali) klasične interpolacijske metode,
posebno linearna interpolacija, postižu najbolju točnost imputacije u oba scenarija
nedostajućih vrijednosti. ML metode ne pokazuju prednost na malom skupu podataka;
imale bi smisla na većem skupu, s više značajki ili uz tuning hiperparametara.
Block missing potvrđuje da izbor metode ovisi o **obliku** nedostajućih podataka,
ne samo o njihovu udjelu.

---
*Generirano: `python scripts/report.py`*
"""
    ANALYSIS_MD.write_text(text, encoding="utf-8")
    print("  analiza:  results/analysis.md")


def main() -> int:
    require_pandas_matplotlib()
    ensure_dirs()
    df = load_experiment()

    print("\nGeneriram grafove i analizu...\n")

    plots = [
        (plot_mae_bars(df, "random", SNAPSHOT_RATE, FIGURES / "mae_by_method_random_20.png"), "mae_by_method_random_20.png"),
        (plot_mae_bars(df, "block", SNAPSHOT_RATE, FIGURES / "mae_by_method_block_20.png"), "mae_by_method_block_20.png"),
        (plot_mae_vs_rate(df, "random", FIGURES / "mae_vs_rate_random.png"), "mae_vs_rate_random.png"),
        (plot_mae_vs_rate(df, "block", FIGURES / "mae_vs_rate_block.png"), "mae_vs_rate_block.png"),
    ]

    for recon in sorted(RESULTS.glob("reconstruction_linear_interpolation_*.csv")):
        name = recon.stem.replace("reconstruction_linear_interpolation_", "")
        out = FIGURES / f"reconstruction_linear_{name}.png"
        title = f"Original vs linear — {name.replace('_', ' ')}"
        plots.append((plot_reconstruction(recon, out, title), out.name))

    for ok, name in plots:
        if ok:
            print(f"  graf:     {FIGURES_DISPLAY}/{name}")

    write_analysis(df)

    print("\nGotovo.")
    print("  rezultati: results/experiment_results.csv")
    print(f"  grafove:   {FIGURES_DISPLAY}/")
    print("  analiza:   results/analysis.md")
    print("\nZakljucak za diplomski napisi rucno u Wordu (nacrt je u results/analysis.md).\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
