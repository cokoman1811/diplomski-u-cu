#!/usr/bin/env python3
"""
Generira sve tablice rezultata za sve missing rateove (10-80 %).

Izlaz:
  results/tablice/
    sve_rezultate.csv              - kompletna ravna tablica (320 redaka)
    sve_rezultate.md              - ista tablica u markdownu
    {scenario}_detaljno.csv        - svi metodi x svi rateovi po scenariju
    {scenario}_mae_wide.csv       - pivot: metoda x rate (MAE)
    {scenario}_rmse_wide.csv
    {scenario}_r2_wide.csv
    sve_tablice_rezultata.xlsx     - Excel s listovima po scenariju
    sve_tablice_pregled.md         - markdown pregled svih tablica
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_IN = ROOT / "results" / "experiment_results.csv"
OUT_DIR = ROOT / "results" / "tablice"

SCENARIOS = ["random", "block", "block_start", "block_middle", "block_end"]
SCENARIO_LABELS = {
    "random": "Random missing",
    "block": "Block missing",
    "block_start": "Block na početku",
    "block_middle": "Block u sredini",
    "block_end": "Block na kraju",
}
METHODS = [
    "forward_fill",
    "linear_interpolation",
    "time_interpolation",
    "cubic_interpolation",
    "spline_interpolation",
    "knn",
    "decision_tree",
    "random_forest",
]
RATES = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80]
RATE_LABELS = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%"]
METRICS = ["mae", "rmse", "r2"]


def load_df():
    import pandas as pd

    if not CSV_IN.exists():
        raise FileNotFoundError(f"Nema {CSV_IN}. Pokreni: .\\diplomski.exe --experiment-all")
    df = pd.read_csv(CSV_IN)
    df["missing_rate_pct"] = (df["missing_rate"] * 100).round(0).astype(int)
    return df


def fmt(v: float, metric: str) -> str:
    if metric == "r2":
        return f"{v:.4f}"
    return f"{v:.4f}"


def pivot_wide(sub, metric: str):
    import pandas as pd

    p = sub.pivot_table(
        index="method",
        columns="missing_rate_pct",
        values=metric,
        aggfunc="first",
    )
    p = p.reindex(METHODS)
    for r in [10, 20, 30, 40, 50, 60, 70, 80]:
        if r not in p.columns:
            p[r] = float("nan")
    p = p[[10, 20, 30, 40, 50, 60, 70, 80]]
    p.columns = RATE_LABELS
    p.index.name = "method"
    return p.reset_index()


def wide_to_markdown(wide, title: str, metric: str) -> str:
    lines = [f"### {title}", ""]
    header = "| method | " + " | ".join(RATE_LABELS) + " |"
    sep = "|--------|" + "|".join(["------"] * len(RATE_LABELS)) + "|"
    lines.extend([header, sep])
    for _, row in wide.iterrows():
        cells = [row["method"]]
        for col in RATE_LABELS:
            val = row[col]
            if val != val:  # NaN
                cells.append("—")
            else:
                cells.append(fmt(val, metric))
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    return "\n".join(lines)


def detail_to_markdown(sub, title: str) -> str:
    lines = [f"### {title}", ""]
    lines.append("| missing_rate | method | MAE | RMSE | R² | missing | evaluated |")
    lines.append("|-------------|--------|-----|------|-----|---------|-----------|")
    sub = sub.sort_values(["missing_rate", "mae"])
    for _, r in sub.iterrows():
        lines.append(
            f"| {r.missing_rate:.0%} | {r['method']} | {r.mae:.4f} | {r.rmse:.4f} | "
            f"{r.r2:.4f} | {int(r.number_of_missing_values)} | {int(r.number_of_evaluated_values)} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    import pandas as pd

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df = load_df()

    # --- Kompletna ravna tablica ---
    flat_cols = [
        "scenario",
        "block_position",
        "missing_rate",
        "missing_rate_pct",
        "method",
        "mae",
        "rmse",
        "r2",
        "number_of_missing_values",
        "number_of_evaluated_values",
    ]
    flat = df[flat_cols].sort_values(["scenario", "missing_rate", "method"])
    flat.to_csv(OUT_DIR / "sve_rezultate.csv", index=False, encoding="utf-8-sig")

    md_parts = [
        "# Sve tablice rezultata — missing rate 10–80 %",
        "",
        f"*Izvor: `results/experiment_results.csv` ({len(df)} redaka)*",
        f"*Generirano: `python scripts/generate_results_tables.py`*",
        "",
        "---",
        "",
        "## KOMPLETNA TABLICA (svi scenariji, svi rateovi, sve metode)",
        "",
        "| scenario | block_position | missing_rate | method | MAE | RMSE | R² | missing | evaluated |",
        "|----------|----------------|--------------|--------|-----|------|-----|---------|-----------|",
    ]
    for _, r in flat.iterrows():
        md_parts.append(
            f"| {r.scenario} | {r.block_position} | {r.missing_rate:.0%} | {r['method']} | "
            f"{r.mae:.4f} | {r.rmse:.4f} | {r.r2:.4f} | "
            f"{int(r.number_of_missing_values)} | {int(r.number_of_evaluated_values)} |"
        )
    md_parts.extend(["", "---", ""])

    excel_path = OUT_DIR / "sve_tablice_rezultata.xlsx"
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        flat.to_excel(writer, sheet_name="sve_rezultate", index=False)

        for scenario in SCENARIOS:
            sub = df[df.scenario == scenario].copy()
            label = SCENARIO_LABELS[scenario]

            md_parts.append(f"## {label} (`{scenario}`)")
            md_parts.append("")

            # Detaljna tablica
            detail = sub[
                [
                    "missing_rate",
                    "method",
                    "mae",
                    "rmse",
                    "r2",
                    "number_of_missing_values",
                    "number_of_evaluated_values",
                ]
            ].sort_values(["missing_rate", "mae"])
            detail_path = OUT_DIR / f"{scenario}_detaljno.csv"
            detail.to_csv(detail_path, index=False, encoding="utf-8-sig")
            md_parts.append(detail_to_markdown(sub, f"{label} — detaljno (sortirano po rateu i MAE)"))

            sheet_prefix = scenario[:20]
            detail.to_excel(writer, sheet_name=f"{sheet_prefix}_detaljno"[:31], index=False)

            for metric in METRICS:
                wide = pivot_wide(sub, metric)
                metric_name = metric.upper() if metric != "r2" else "R2"
                wide_path = OUT_DIR / f"{scenario}_{metric}_wide.csv"
                wide.to_csv(wide_path, index=False, encoding="utf-8-sig")
                wide.to_excel(
                    writer,
                    sheet_name=f"{sheet_prefix}_{metric_name}"[:31],
                    index=False,
                )
                ylabel = {"mae": "MAE (°C)", "rmse": "RMSE (°C)", "r2": "R²"}[metric]
                md_parts.append(wide_to_markdown(wide, f"{label} — {ylabel}", metric))

            md_parts.append("---")
            md_parts.append("")

    # Sažetak: najbolja metoda po scenariju i rateu
    best_rows = []
    for scenario in SCENARIOS:
        for rate in RATES:
            sub = df[(df.scenario == scenario) & (df.missing_rate == rate)]
            if sub.empty:
                continue
            best = sub.loc[sub.mae.idxmin()]
            best_rows.append(
                {
                    "scenario": scenario,
                    "block_position": best.block_position,
                    "missing_rate": rate,
                    "best_method_mae": best["method"],
                    "mae": best.mae,
                    "rmse": best.rmse,
                    "r2": best.r2,
                }
            )
    best_df = pd.DataFrame(best_rows)
    best_df.to_csv(OUT_DIR / "najbolja_metoda_po_scenariju.csv", index=False, encoding="utf-8-sig")

    md_parts.extend(
        [
            "## Najbolja metoda po scenariju i missing rateu (po MAE)",
            "",
            "| scenario | block_position | missing_rate | najbolja metoda | MAE | RMSE | R² |",
            "|----------|----------------|--------------|-----------------|-----|------|-----|",
        ]
    )
    for _, r in best_df.iterrows():
        md_parts.append(
            f"| {r.scenario} | {r.block_position} | {r.missing_rate:.0%} | "
            f"{r.best_method_mae} | {r.mae:.4f} | {r.rmse:.4f} | {r.r2:.4f} |"
        )

    overview_md = OUT_DIR / "sve_tablice_pregled.md"
    overview_md.write_text("\n".join(md_parts), encoding="utf-8")

    # Kraći flat markdown samo za kopiranje (bez wide sekcija)
    flat_md = OUT_DIR / "sve_rezultate.md"
    flat_md.write_text("\n".join(md_parts[: len(md_parts)]), encoding="utf-8")

    print("Generirane tablice:")
    print(f"  {OUT_DIR.relative_to(ROOT)}/")
    print(f"    sve_rezultate.csv          ({len(flat)} redaka)")
    print(f"    sve_tablice_pregled.md     (sve tablice u markdownu)")
    print(f"    sve_tablice_rezultata.xlsx (Excel, list po scenariju)")
    for scenario in SCENARIOS:
        print(f"    {scenario}_detaljno.csv")
        print(f"    {scenario}_mae_wide.csv / rmse / r2")
    print(f"    najbolja_metoda_po_scenariju.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
