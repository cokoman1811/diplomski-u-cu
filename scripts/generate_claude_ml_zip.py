#!/usr/bin/env python3
"""Pakira priloge za Claude analizu ML metoda (prompt: results/claude_prompt_analiza_ml.md)."""

from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZIP_PATH = ROOT / "results" / "claude_analiza_ml.zip"

FILES = [
    "results/claude_prompt_analiza_ml.md",
    "results/experiment_results.csv",
    "results/novo_za_diplomski.md",
    "results/tablice/sve_tablice_pregled.md",
    "data/processed/jena_temperature_7d.csv",
    "src/knn_methods.c",
    "src/knn_upgraded.c",
    "src/decision_tree.c",
    "src/rf_methods.c",
    "src/experiment.c",
    "src/interpolation.c",
    "src/adaptive_imputation.c",
    "src/evaluation.c",
]


def main() -> None:
    paths = [(ROOT / rel, rel) for rel in FILES]

    missing = [rel for path, rel in paths if not path.exists()]
    for rel in missing:
        print(f"UPOZORENJE: nedostaje {rel}")

    ZIP_PATH.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for path, rel in paths:
            if path.exists():
                zf.write(path, rel)

    size_kb = ZIP_PATH.stat().st_size / 1024
    print(f"ZIP spremljen ({size_kb:.0f} KB): results/claude_analiza_ml.zip")
    print(f"  datoteke: {len(paths) - len(missing)}/{len(paths)}")


if __name__ == "__main__":
    main()
