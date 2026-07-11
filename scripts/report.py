#!/usr/bin/env python3
"""
Generira grafove i tekstualnu analizu iz results/*.csv.

Koristenje (iz korijena projekta):
    python scripts/report.py          # generira grafove + otvara HTML pregled
    python scripts/report.py --no-open  # samo spremi datoteke
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
FIGURES = ROOT / "slike i videa" / "2026" / "diplomski-grafovi"
FIGURES_DISPLAY = "slike i videa/2026/diplomski-grafovi"
EXPERIMENT_CSV = RESULTS / "experiment_results.csv"
ANALYSIS_MD = RESULTS / "analysis.md"
HTML_GALLERY = RESULTS / "grafovi_pregled.html"

CLASSICAL = {
    "forward_fill",
    "linear_interpolation",
    "time_interpolation",
    "cubic_interpolation",
    "spline_interpolation",
}
ML = {"knn", "decision_tree", "random_forest"}

ALL_METHODS = [
    "forward_fill",
    "linear_interpolation",
    "time_interpolation",
    "cubic_interpolation",
    "spline_interpolation",
    "knn",
    "decision_tree",
    "random_forest",
]

METHOD_COLORS = {
    "forward_fill": "#8c564b",
    "linear_interpolation": "#1f77b4",
    "time_interpolation": "#aec7e8",
    "cubic_interpolation": "#2ca02c",
    "spline_interpolation": "#98df8a",
    "knn": "#ff7f0e",
    "decision_tree": "#d62728",
    "random_forest": "#9467bd",
}

ALL_SCENARIOS = [
    "random",
    "block",
    "block_start",
    "block_middle",
    "block_end",
]

SCENARIO_LABELS = {
    "random": "Random missing",
    "block": "Block missing (nasumična pozicija)",
    "block_start": "Block na početku niza",
    "block_middle": "Block u sredini niza",
    "block_end": "Block na kraju niza",
}

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
        print("Prvo pokreni: .\\diplomski.exe --experiment-all")
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
    label = SCENARIO_LABELS.get(scenario, scenario)

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.bar(sub["method"], sub["mae"], color=colors)
    ax.set_ylabel("MAE (°C)")
    ax.set_title(f"MAE po metodama — {label}, {rate:.0%} missing")
    ax.tick_params(axis="x", rotation=35)
    plt.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return True


def plot_metric_vs_rate(df, scenario: str, metric: str, out_path: Path):
    import matplotlib.pyplot as plt

    sub = df[df["scenario"] == scenario]
    if sub.empty:
        return False

    label = SCENARIO_LABELS.get(scenario, scenario)
    ylabel = {"mae": "MAE (°C)", "rmse": "RMSE (°C)", "r2": "R²"}[metric]
    title_metric = metric.upper() if metric != "r2" else "R²"

    fig, ax = plt.subplots(figsize=(10, 6))
    for method in ALL_METHODS:
        m = sub[sub["method"] == method].sort_values("missing_rate")
        if m.empty:
            continue
        ax.plot(
            m["missing_rate"] * 100,
            m[metric],
            marker="o",
            label=method,
            color=METHOD_COLORS.get(method),
            linewidth=1.8,
            markersize=5,
        )

    ax.set_xlabel("Missing rate (%)")
    ax.set_ylabel(ylabel)
    ax.set_title(f"{title_metric} vs missing rate — {label}")
    ax.set_xticks([10, 20, 30, 40, 50, 60, 70, 80])
    ax.legend(fontsize=7, ncol=2, loc="best")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return True


def plot_mae_overview_panel(df, scenario: str, out_path: Path):
    """Jedan graf po scenariju: stupčasti dijagram MAE za sve metode na svim rateovima."""
    import matplotlib.pyplot as plt
    import numpy as np

    sub = df[df["scenario"] == scenario]
    if sub.empty:
        return False

    rates = sorted(sub["missing_rate"].unique())
    label = SCENARIO_LABELS.get(scenario, scenario)

    ncols = 4
    nrows = int(np.ceil(len(rates) / ncols))
    fig, axes = plt.subplots(nrows, ncols, figsize=(16, 3.5 * nrows), squeeze=False)
    fig.suptitle(f"MAE po metodama — {label} (10–80 %)", fontsize=14, y=1.01)

    for idx, rate in enumerate(rates):
        row, col = divmod(idx, ncols)
        ax = axes[row][col]
        part = sub[sub["missing_rate"] == rate].sort_values("mae")
        colors = ["#4C78A8" if m in CLASSICAL else "#F58518" for m in part["method"]]
        ax.bar(range(len(part)), part["mae"], color=colors)
        ax.set_xticks(range(len(part)))
        ax.set_xticklabels(part["method"], rotation=55, ha="right", fontsize=6)
        ax.set_ylabel("MAE (°C)", fontsize=8)
        ax.set_title(f"{rate:.0%} missing", fontsize=10)
        ax.grid(True, axis="y", alpha=0.25)

    for idx in range(len(rates), nrows * ncols):
        row, col = divmod(idx, ncols)
        axes[row][col].axis("off")

    plt.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return True


def plot_reconstruction(csv_path: Path, out_path: Path, title: str):
    import matplotlib.pyplot as plt
    import pandas as pd

    if not csv_path.exists():
        return False

    df = pd.read_csv(csv_path)
    orig_col = "original_temperature" if "original_temperature" in df.columns else "original"
    recon_col = (
        "reconstructed_temperature"
        if "reconstructed_temperature" in df.columns
        else "reconstructed"
    )

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df["index"], df[orig_col], label="original", color="#1f77b4", linewidth=1.2)
    ax.plot(df["index"], df[recon_col], label="rekonstruirano", color="#ff7f0e", linewidth=1.2)

    masked = df[df["mask"] == 1]
    if not masked.empty:
        ax.scatter(
            masked["index"],
            masked[orig_col],
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
    rates = sorted(df["missing_rate"].unique())
    rate_cols = " | ".join(f"{r:.0%}" for r in rates)
    rate_hdr = " | ".join("----" for _ in rates)

    def best_row(scenario: str) -> str:
        cells = [best_method(df, scenario, r) for r in rates]
        return " | ".join(cells)

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

    knn_block_80 = df[
        (df["scenario"] == "block")
        & (df["missing_rate"] == 0.80)
        & (df["method"] == "knn")
    ]
    knn_80_mae = knn_block_80["mae"].iloc[0] if not knn_block_80.empty else float("nan")

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

| scenarij | {rate_cols} |
|----------|{rate_hdr}|
| random | {best_row("random")} |
| block | {best_row("block")} |
| block_start | {best_row("block_start")} |
| block_middle | {best_row("block_middle")} |
| block_end | {best_row("block_end")} |

## Ključni nalazi (za poglavlje Rezultati)

1. **Klasične interpolacijske metode** (posebno linear, spline, cubic) postižu najniži MAE na random scenariju za sve testirane missing rateove (10–80 %).
2. **Linear i time interpolacija** daju identične rezultate jer su uzorci ravnomjerno raspoređeni u vremenu (Jena 10-min intervali).
3. Na **block scenariju** linear/time i dalje vode; forward fill i cubic/spline znatno gore zbog dugačkih rupa.
    printf("Na ovom datasetu (7 dana, 10-min) ML metode (KNN, DT, RF) obicno ne nadmašuju klasicne.\n");
5. **KNN** na block scenariju pokazuje najveću pogrešku (npr. MAE ≈ {knn_80_mae:.2f} pri 80% block).
6. Pri visokim missing rateovima (50–80 %) pogreška naglo raste na block_start, block_middle i block_end scenarijima.

## Grafovi

Otvori `results/grafovi_pregled.html` u pregledniku za vizualni pregled svih grafova.

---
*Generirano: `python scripts/report.py`*
"""
    ANALYSIS_MD.write_text(text, encoding="utf-8")
    print("  analiza:  results/analysis.md")


def write_html_gallery(generated: list[tuple[str, Path, str]]) -> None:
    """HTML stranica sa svim grafovima — otvara se u pregledniku."""
    sections: dict[str, list[tuple[str, Path, str]]] = {
        "Pregled po scenariju (10–80 %)": [],
        "MAE vs missing rate (sve metode)": [],
        "RMSE vs missing rate (sve metode)": [],
        "R² vs missing rate (sve metode)": [],
        "MAE po metodama (20%)": [],
        "Rekonstrukcija (linear, 20%)": [],
    }

    for category, path, title in generated:
        if category == "overview":
            sections["Pregled po scenariju (10–80 %)"].append((title, path, title))
        elif category == "mae_vs_rate":
            sections["MAE vs missing rate (sve metode)"].append((title, path, title))
        elif category == "rmse_vs_rate":
            sections["RMSE vs missing rate (sve metode)"].append((title, path, title))
        elif category == "r2_vs_rate":
            sections["R² vs missing rate (sve metode)"].append((title, path, title))
        elif category == "mae_bars":
            sections["MAE po metodama (20%)"].append((title, path, title))
        elif category == "reconstruction":
            sections["Rekonstrukcija (linear, 20%)"].append((title, path, title))

    parts = [
        "<!DOCTYPE html>",
        "<html lang='hr'>",
        "<head>",
        "<meta charset='utf-8'>",
        "<title>Diplomski — pregled grafova</title>",
        "<style>",
        "body { font-family: Segoe UI, Arial, sans-serif; margin: 24px; background: #f5f5f5; }",
        "h1 { color: #1a1a2e; }",
        "h2 { color: #16213e; border-bottom: 2px solid #4C78A8; padding-bottom: 6px; }",
        ".card { background: white; border-radius: 8px; padding: 16px; margin: 16px 0; "
        "box-shadow: 0 2px 8px rgba(0,0,0,0.08); }",
        ".card img { max-width: 100%; height: auto; display: block; margin-top: 8px; }",
        ".card h3 { margin: 0 0 8px 0; font-size: 1rem; color: #333; }",
        ".legend { background: #e8f4f8; padding: 12px; border-radius: 6px; margin-bottom: 20px; }",
        ".legend li { margin: 4px 0; }",
        "</style>",
        "</head>",
        "<body>",
        "<h1>Pregled grafova — imputacija temperatura</h1>",
        "<div class='legend'>",
        "<strong>Kako čitati:</strong>",
        "<ul>",
        "<li><b>MAE</b> — prosječna pogreška u °C (niže = bolje)</li>",
        "<li><b>Plavi stupci</b> — klasične metode | <b>Narančasti</b> — ML metode</li>",
        "<li><b>Crvene točke</b> na rekonstrukciji — mjesta gdje su vrijednosti umjetno uklonjene</li>",
        "</ul>",
        "</div>",
    ]

    for section_title, items in sections.items():
        if not items:
            continue
        parts.append(f"<h2>{section_title}</h2>")
        for title, img_path, _ in items:
            rel = os.path.relpath(img_path.resolve(), HTML_GALLERY.parent).replace("\\", "/")
            parts.append("<div class='card'>")
            parts.append(f"<h3>{title}</h3>")
            parts.append(f"<img src='{rel}' alt='{title}'>")
            parts.append("</div>")

    parts.extend(["</body>", "</html>"])
    HTML_GALLERY.write_text("\n".join(parts), encoding="utf-8")
    print(f"  pregled:  {HTML_GALLERY.relative_to(ROOT)}")


def open_path(path: Path) -> None:
    path = path.resolve()
    try:
        if sys.platform == "win32":
            os.startfile(path)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.run(["open", str(path)], check=False)
        else:
            subprocess.run(["xdg-open", str(path)], check=False)
    except OSError as exc:
        print(f"  [upozorenje] Ne mogu otvoriti {path}: {exc}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generiraj grafove iz experiment_results.csv")
    parser.add_argument(
        "--no-open",
        action="store_true",
        help="Ne otvaraj automatski HTML pregled u pregledniku",
    )
    args = parser.parse_args()

    require_pandas_matplotlib()
    ensure_dirs()
    df = load_experiment()

    print("\nGeneriram grafove i analizu...\n")

    generated: list[tuple[str, Path, str]] = []

    for scenario in ALL_SCENARIOS:
        label = SCENARIO_LABELS.get(scenario, scenario)

        fname = f"mae_overview_{scenario}.png"
        out = FIGURES / fname
        if plot_mae_overview_panel(df, scenario, out):
            generated.append(("overview", out, f"{label} — pregled MAE (10–80 %)"))
            print(f"  graf:     {FIGURES_DISPLAY}/{fname}")

        for metric, cat in [("mae", "mae_vs_rate"), ("rmse", "rmse_vs_rate"), ("r2", "r2_vs_rate")]:
            fname = f"{metric}_vs_rate_{scenario}_all.png"
            out = FIGURES / fname
            if plot_metric_vs_rate(df, scenario, metric, out):
                generated.append((cat, out, f"{label} — {metric.upper()} vs missing rate"))
                print(f"  graf:     {FIGURES_DISPLAY}/{fname}")

    for scenario in ALL_SCENARIOS:
        fname = f"mae_by_method_{scenario}_20.png"
        out = FIGURES / fname
        label = SCENARIO_LABELS.get(scenario, scenario)
        if plot_mae_bars(df, scenario, SNAPSHOT_RATE, out):
            generated.append(("mae_bars", out, f"{label} — MAE po metodama (20%)"))
            print(f"  graf:     {FIGURES_DISPLAY}/{fname}")

    for recon in sorted(RESULTS.glob("reconstruction_linear_interpolation_*.csv")):
        name = recon.stem.replace("reconstruction_linear_interpolation_", "")
        fname = f"reconstruction_linear_{name}.png"
        out = FIGURES / fname
        title = f"Original vs linear — {name.replace('_', ' ')}"
        if plot_reconstruction(recon, out, title):
            generated.append(("reconstruction", out, title))
            print(f"  graf:     {FIGURES_DISPLAY}/{fname}")

    write_analysis(df)
    write_html_gallery(generated)

    print("\nGotovo.")
    print(f"  grafove:   {FIGURES_DISPLAY}/  ({len(generated)} PNG datoteka)")
    print(f"  pregled:   results/grafovi_pregled.html  (otvori u pregledniku)")
    print("  rezultati: results/experiment_results.csv")
    print("  analiza:   results/analysis.md")

    if not args.no_open:
        print("\nOtvaram vizualni pregled grafova u pregledniku...")
        open_path(HTML_GALLERY)

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
