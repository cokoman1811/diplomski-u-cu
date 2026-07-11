#!/usr/bin/env python3
"""
Priprema Jena temperaturnog niza za 7 dana (10-min intervali).

Izvor: Jena Climate 2009-2016 (TensorFlow/Keras, 10-min uzorkovanje).
Izlaz: data/processed/jena_temperature_7d.csv (1008 zapisa)

Koristenje:
    python scripts/prepare_jena_7d.py
"""
from __future__ import annotations

import zipfile
from pathlib import Path
from urllib.request import urlretrieve

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
OUT_CSV = ROOT / "data" / "processed" / "jena_temperature_7d.csv"
JENA_ZIP_URL = (
    "https://storage.googleapis.com/tensorflow/tf-keras-datasets/"
    "jena_climate_2009_2016.csv.zip"
)
DAYS = 7
SAMPLES_PER_HOUR = 6
EXPECTED_N = DAYS * 24 * SAMPLES_PER_HOUR  # 1008


def main() -> int:
    try:
        import pandas as pd
    except ImportError:
        print("Instaliraj: pip install pandas")
        return 1

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    zip_path = RAW_DIR / "jena_climate_2009_2016.csv.zip"
    csv_path = RAW_DIR / "jena_climate_2009_2016.csv"

    if not csv_path.exists():
        if not zip_path.exists():
            print("Preuzimam Jena Climate dataset (zip)...")
            urlretrieve(JENA_ZIP_URL, zip_path)
            print("  spremljeno zip")
        print("Raspakiram CSV...")
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(RAW_DIR)

    if not csv_path.exists():
        print(f"Greska: nema {csv_path} nakon raspakivanja")
        return 1

    df = pd.read_csv(csv_path)
    if "Date Time" not in df.columns or "T (degC)" not in df.columns:
        print("Neocekivan format Jena CSV-a")
        return 1

    df["datetime"] = pd.to_datetime(df["Date Time"], format="%d.%m.%Y %H:%M:%S")
    df = df.sort_values("datetime")

    # Izvorni Jena CSV je na 10-min; uzmi prvih 7 dana (1008 uzoraka).
    # Pocetak uskladen s postojecim 48h izrezom (00:10 na prvom retku).
    start = pd.Timestamp("2009-01-01 00:10:00")
    end = start + pd.Timedelta(minutes=10 * (EXPECTED_N - 1))
    part = df[(df["datetime"] >= start) & (df["datetime"] <= end)].copy()

    if len(part) < EXPECTED_N:
        print(f"Upozorenje: pronadjeno samo {len(part)} zapisa, uzimam prvih {EXPECTED_N} redaka")
        part = df.head(EXPECTED_N).copy()

    part = part.head(EXPECTED_N)

    out = pd.DataFrame(
        {
            "timestamp": part["datetime"].dt.strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": part["T (degC)"].astype(float),
        }
    )

    out.to_csv(OUT_CSV, index=False)
    print(f"Gotovo: {OUT_CSV.name}")
    print(f"  zapisa: {len(out)} ({DAYS} dana, 10-min intervali)")
    print(f"  od: {out['timestamp'].iloc[0]}")
    print(f"  do: {out['timestamp'].iloc[-1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
