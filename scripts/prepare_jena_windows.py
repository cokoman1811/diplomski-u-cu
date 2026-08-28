#!/usr/bin/env python3
"""
Priprema vise nezavisnih 7-dnevnih prozora iz Jena Climate niza (2009-2016).

Zasto: cijeli eksperiment vrtio se na jednom tjednu (1.-8. sijecnja 2009.), pa
zakljucci nisu imali mjeru nesigurnosti. Uz to su scenariji block_start,
block_middle i block_end potpuno deterministicki — seed maske na njima ne mijenja
nista — pa je ponavljanje preko razlicitih PROZORA jedini nacin da se i za njih
dobije varijabilnost.

Prozori su ravnomjerno rasporedeni kroz cijeli niz, cime se pokrivaju sva
godisnja doba. Prvi prozor namjerno je identican dosadasnjem
data/processed/jena_temperature_7d.csv, pa rezultati ostaju usporedivi.

Izlaz:
    data/processed/jena_windows/window_00.csv ... window_19.csv
    data/processed/jena_windows/index.csv      (metapodaci prozora)

Koristenje:
    python scripts/prepare_jena_windows.py [broj_prozora]
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path
from urllib.request import urlretrieve

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
OUT_DIR = ROOT / "data" / "processed" / "jena_windows"
JENA_ZIP_URL = (
    "https://storage.googleapis.com/tensorflow/tf-keras-datasets/"
    "jena_climate_2009_2016.csv.zip"
)

DAYS = 7
SAMPLES_PER_HOUR = 6
WINDOW_N = DAYS * 24 * SAMPLES_PER_HOUR  # 1008
DEFAULT_WINDOWS = 20
STEP_MINUTES = 10


def ensure_raw_csv() -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = RAW_DIR / "jena_climate_2009_2016.csv.zip"
    csv_path = RAW_DIR / "jena_climate_2009_2016.csv"

    if not csv_path.exists():
        if not zip_path.exists():
            print("Preuzimam Jena Climate dataset (zip)...")
            urlretrieve(JENA_ZIP_URL, zip_path)
        print("Raspakiram CSV...")
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(RAW_DIR)
    return csv_path


def find_clean_window(dt, temp, start: int, limit: int) -> int | None:
    """Prvi indeks >= start na kojem je WINDOW_N uzastopnih uzoraka na tocno 10 min."""
    import numpy as np

    step = np.timedelta64(STEP_MINUTES, "m")
    pos = start
    while pos + WINDOW_N <= limit:
        seg_dt = dt[pos:pos + WINDOW_N]
        seg_t = temp[pos:pos + WINDOW_N]
        gaps = np.diff(seg_dt)
        if np.all(gaps == step) and not np.isnan(seg_t).any():
            return pos
        # Preskoci do prve neregularnosti, pa dalje od nje.
        bad = np.nonzero(gaps != step)[0]
        pos = pos + (int(bad[0]) + 1 if len(bad) else WINDOW_N)
    return None


def main() -> int:
    try:
        import numpy as np
        import pandas as pd
    except ImportError:
        print("Instaliraj: pip install pandas numpy")
        return 1

    n_windows = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_WINDOWS
    csv_path = ensure_raw_csv()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Ucitavam {csv_path.name} ...")
    df = pd.read_csv(csv_path, usecols=["Date Time", "T (degC)"])
    df["datetime"] = pd.to_datetime(df["Date Time"], format="%d.%m.%Y %H:%M:%S")
    df = df.sort_values("datetime").reset_index(drop=True)

    dt = df["datetime"].to_numpy(dtype="datetime64[m]")
    temp = df["T (degC)"].to_numpy(dtype=float)
    total = len(df)
    print(f"  ukupno zapisa: {total}")
    print(f"  raspon: {dt[0]} .. {dt[-1]}")

    # Ravnomjerno rasporedeni pocetci; prvi je 0 da ostane jednak dosadasnjem izrezu.
    span = total - WINDOW_N
    targets = [int(round(i * span / max(n_windows - 1, 1))) for i in range(n_windows)]

    rows = []
    used_starts: set[int] = set()
    for wid, target in enumerate(targets):
        start = find_clean_window(dt, temp, target, total)
        if start is None or start in used_starts:
            print(f"  [preskacem] prozor {wid}: nema cistog izreza od indeksa {target}")
            continue
        used_starts.add(start)

        seg_dt = dt[start:start + WINDOW_N]
        seg_t = temp[start:start + WINDOW_N]
        out = pd.DataFrame(
            {
                "timestamp": pd.to_datetime(seg_dt).strftime("%Y-%m-%d %H:%M:%S"),
                "temperature": seg_t,
            }
        )
        path = OUT_DIR / f"window_{wid:02d}.csv"
        out.to_csv(path, index=False)

        rows.append(
            {
                "window_id": wid,
                "start_index": start,
                "start": str(seg_dt[0]),
                "end": str(seg_dt[-1]),
                "mean_temp": round(float(np.mean(seg_t)), 4),
                "sd_temp": round(float(np.std(seg_t)), 4),
                "min_temp": round(float(np.min(seg_t)), 4),
                "max_temp": round(float(np.max(seg_t)), 4),
                "lag1_autocorr": round(
                    float(np.corrcoef(seg_t[:-1], seg_t[1:])[0, 1]), 6
                ),
            }
        )

    index = pd.DataFrame(rows)
    index.to_csv(OUT_DIR / "index.csv", index=False)

    print(f"\nGotovo: {len(rows)} prozora u {OUT_DIR.relative_to(ROOT)}")
    print(index.to_string(index=False))
    print()
    print(f"  sd temperature po prozorima: {index.sd_temp.min():.2f} .. "
          f"{index.sd_temp.max():.2f} °C")
    print(f"  srednja temperatura:         {index.mean_temp.min():.2f} .. "
          f"{index.mean_temp.max():.2f} °C")
    print(f"  lag-1 autokorelacija:        {index.lag1_autocorr.min():.6f} .. "
          f"{index.lag1_autocorr.max():.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
