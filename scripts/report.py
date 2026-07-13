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
    "moving_average",
}
ML = {"knn", "knn_upgraded", "decision_tree", "random_forest", "adaptive_imputation"}

ALL_METHODS = [
    "forward_fill",
    "linear_interpolation",
    "time_interpolation",
    "cubic_interpolation",
    "spline_interpolation",
    "moving_average",
    "knn",
    "knn_upgraded",
    "decision_tree",
    "random_forest",
    "adaptive_imputation",
]

METHOD_COLORS = {
    "forward_fill": "#8c564b",
    "linear_interpolation": "#1f77b4",
    "time_interpolation": "#aec7e8",
    "cubic_interpolation": "#2ca02c",
    "spline_interpolation": "#98df8a",
    "moving_average": "#17becf",
    "knn": "#ff7f0e",
    "knn_upgraded": "#ffbb78",
    "decision_tree": "#d62728",
    "random_forest": "#9467bd",
    "adaptive_imputation": "#e377c2",
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


def _series_close(a, b, metric: str, tol: float = 1e-6) -> bool:
    import numpy as np

    if len(a) != len(b) or len(a) == 0:
        return False
    return bool(np.allclose(a[metric].values, b[metric].values, atol=tol, rtol=0))


def group_methods_for_plot(sub, metric: str) -> list[tuple[str, object, str]]:
    """
    Grupira metode s identičnim rezultatima u jednu liniju/stupac.
    Vraća (label, dataframe_sortiran_po_rate, boja).
    """
    groups: list[tuple[str, object, str]] = []
    used: set[str] = set()

    for method in ALL_METHODS:
        if method in used:
            continue
        part = sub[sub["method"] == method].sort_values("missing_rate")
        if part.empty:
            continue

        same = [method]
        for other in ALL_METHODS:
            if other == method or other in used:
                continue
            other_part = sub[sub["method"] == other].sort_values("missing_rate")
            if other_part.empty:
                continue
            if _series_close(part, other_part, metric):
                same.append(other)

        for name in same:
            used.add(name)

        if len(same) > 1:
            label = " / ".join(same)
        else:
            label = same[0]
        groups.append((label, part, METHOD_COLORS.get(method, "#333333")))

    return groups


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

    groups = group_methods_for_plot(sub, "mae")
    groups.sort(key=lambda g: g[1]["mae"].iloc[0])
    labels = [g[0] for g in groups]
    values = [g[1]["mae"].iloc[0] for g in groups]
    colors = ["#4C78A8" if any(m in CLASSICAL for m in lbl.split(" / ")) else "#F58518" for lbl in labels]
    label = SCENARIO_LABELS.get(scenario, scenario)
    n_methods = len(sub)
    n_bars = len(groups)

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(labels, values, color=colors)
    ax.set_ylabel("MAE (°C)")
    title = f"MAE po metodama — {label}, {rate:.0%} missing"
    if n_bars < n_methods:
        title += f"\n({n_bars} stupaca = {n_methods} metoda; identični rezultati spojeni)"
    ax.set_title(title, fontsize=11)
    ax.tick_params(axis="x", rotation=40, labelsize=8)
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
    groups = group_methods_for_plot(sub, metric)
    n_methods = sub["method"].nunique()
    n_lines = len(groups)

    fig, ax = plt.subplots(figsize=(11, 6))
    linestyles = ["-", "--", "-.", ":", (0, (3, 1, 1, 1))]
    for idx, (method_label, part, color) in enumerate(groups):
        ax.plot(
            part["missing_rate"] * 100,
            part[metric],
            marker="o",
            label=method_label,
            color=color,
            linewidth=1.8,
            markersize=5,
            linestyle=linestyles[idx % len(linestyles)],
        )

    ax.set_xlabel("Missing rate (%)")
    ax.set_ylabel(ylabel)
    title = f"{title_metric} vs missing rate — {label}"
    if n_lines < n_methods:
        title += f"\n({n_lines} linija = {n_methods} metoda; identični rezultati spojeni u legendi)"
    ax.set_title(title, fontsize=11)
    ax.set_xticks([10, 20, 30, 40, 50, 60, 70, 80])
    ax.legend(fontsize=6.5, ncol=2, loc="best")
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
    n_methods = sub["method"].nunique()

    ncols = 4
    nrows = int(np.ceil(len(rates) / ncols))
    fig, axes = plt.subplots(nrows, ncols, figsize=(18, 3.8 * nrows), squeeze=False)
    fig.suptitle(
        f"MAE po metodama — {label} (10–80 %, {n_methods} metoda)",
        fontsize=14,
        y=1.01,
    )

    for idx, rate in enumerate(rates):
        row, col = divmod(idx, ncols)
        ax = axes[row][col]
        part = sub[sub["missing_rate"] == rate]
        groups = group_methods_for_plot(part, "mae")
        groups.sort(key=lambda g: g[1]["mae"].iloc[0])
        values = [g[1]["mae"].iloc[0] for g in groups]
        names = [g[0] for g in groups]
        colors = [
            "#4C78A8" if any(m in CLASSICAL for m in lbl.split(" / ")) else "#F58518"
            for lbl in names
        ]
        ax.bar(range(len(groups)), values, color=colors)
        ax.set_xticks(range(len(groups)))
        ax.set_xticklabels(names, rotation=60, ha="right", fontsize=5.5)
        ax.set_ylabel("MAE (°C)", fontsize=8)
        suffix = ""
        if len(groups) < n_methods:
            suffix = f" ({len(groups)}/{n_methods} linija)"
        ax.set_title(f"{rate:.0%} missing{suffix}", fontsize=9)
        ax.grid(True, axis="y", alpha=0.25)

    for idx in range(len(rates), nrows * ncols):
        row, col = divmod(idx, ncols)
        axes[row][col].axis("off")

    plt.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return True


def plot_reconstruction_on_ax(df, ax, title: str):
    """Crta original, rekonstrukciju i maskirane točke na zadani axes."""
    orig_col = "original_temperature" if "original_temperature" in df.columns else "original"
    recon_col = (
        "reconstructed_temperature"
        if "reconstructed_temperature" in df.columns
        else "reconstructed"
    )

    ax.plot(df["index"], df[orig_col], label="original", color="#1f77b4", linewidth=1.0)
    ax.plot(df["index"], df[recon_col], label="rekonstruirano", color="#ff7f0e", linewidth=1.0)

    masked = df[df["mask"] == 1]
    if not masked.empty:
        ax.scatter(
            masked["index"],
            masked[orig_col],
            s=8,
            color="red",
            alpha=0.45,
            label="maskirano (original)",
            zorder=3,
        )

    ax.set_xlabel("Indeks")
    ax.set_ylabel("Temperatura (°C)")
    ax.set_title(title, fontsize=10)
    ax.legend(loc="upper right", fontsize=7)
    ax.grid(True, alpha=0.3)


def plot_reconstruction(csv_path: Path, out_path: Path, title: str):
    import matplotlib.pyplot as plt
    import pandas as pd

    if not csv_path.exists():
        return False

    df = pd.read_csv(csv_path)
    fig, ax = plt.subplots(figsize=(12, 4))
    plot_reconstruction_on_ax(df, ax, title)
    plt.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return True


def plot_best_worst_reconstruction(
    scenario: str,
    rate: float,
    best_method: str,
    worst_method: str,
    best_mae: float,
    worst_mae: float,
    out_path: Path,
    scenario_label: str,
):
    import matplotlib.pyplot as plt
    import pandas as pd

    best_csv = RESULTS / f"reconstruction_{best_method}_{scenario}_{rate:.2f}.csv"
    worst_csv = RESULTS / f"reconstruction_{worst_method}_{scenario}_{rate:.2f}.csv"
    if not best_csv.exists():
        return False

    fig, axes = plt.subplots(1, 2, figsize=(14, 4), sharey=True)

    best_df = pd.read_csv(best_csv)
    plot_reconstruction_on_ax(
        best_df,
        axes[0],
        f"NAJBOLJA: {best_method}\nMAE = {best_mae:.4f} °C",
    )

    if worst_csv.exists() and worst_method != best_method:
        worst_df = pd.read_csv(worst_csv)
        plot_reconstruction_on_ax(
            worst_df,
            axes[1],
            f"NAJGORA: {worst_method}\nMAE = {worst_mae:.4f} °C",
        )
    else:
        axes[1].text(
            0.5,
            0.5,
            "Najbolja i najgora metoda\nsu iste za ovaj scenarij.",
            ha="center",
            va="center",
            transform=axes[1].transAxes,
        )
        axes[1].set_title("NAJGORA — nema razlike")

    fig.suptitle(
        f"Rekonstrukcija @ {rate * 100:.0f}% — {scenario_label}",
        fontsize=12,
        y=1.02,
    )
    plt.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
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
4. **ML metode** (KNN, decision tree, random forest) na ovom skupu (7 dana, 10-min) **ne nadmašuju** klasične metode.
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
        "Rekonstrukcija (najbolja vs najgora, 20%)": [],
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
            sections["Rekonstrukcija (najbolja vs najgora, 20%)"].append((title, path, title))

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
        "<li><b>Manje linija nego metoda?</b> — linear i time (te ponekad cubic i spline) "
        "daju identične rezultate pa se prikazuju kao jedna linija s oznakom npr. "
        "<code>linear_interpolation / time_interpolation</code></li>",
        "<li><b>Rekonstrukcijski grafovi</b> prikazuju samo najbolju i najgoru metodu po scenariju "
        "(ne svih 11 odjednom)</li>",
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

    recon_summary = RESULTS / "reconstruction_best_worst_20.csv"
    if recon_summary.exists():
        import pandas as pd

        bw = pd.read_csv(recon_summary)
        for _, row in bw.iterrows():
            scenario = row["scenario"]
            rate = float(row["missing_rate"])
            label = SCENARIO_LABELS.get(scenario, scenario)
            fname = f"reconstruction_best_worst_{scenario}_{int(rate * 100)}.png"
            out = FIGURES / fname
            title = f"{label} — najbolja vs najgora @ {rate * 100:.0f}%"
            if plot_best_worst_reconstruction(
                scenario,
                rate,
                row["best_method"],
                row["worst_method"],
                float(row["best_mae"]),
                float(row["worst_mae"]),
                out,
                label,
            ):
                generated.append(("reconstruction", out, title))
                print(f"  graf:     {FIGURES_DISPLAY}/{fname}")

            for role, method in [("best", row["best_method"]), ("worst", row["worst_method"])]:
                if role == "worst" and method == row["best_method"]:
                    continue
                csv_path = RESULTS / f"reconstruction_{method}_{scenario}_{rate:.2f}.csv"
                role_fname = f"reconstruction_{role}_{scenario}_{int(rate * 100)}.png"
                role_out = FIGURES / role_fname
                role_title = f"{label} — {role} ({method}) @ {rate * 100:.0f}%"
                if plot_reconstruction(csv_path, role_out, role_title):
                    generated.append(("reconstruction", role_out, role_title))
                    print(f"  graf:     {FIGURES_DISPLAY}/{role_fname}")
    else:
        print("  upozorenje: nema reconstruction_best_worst_20.csv — pokreni eksperiment")

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
