import pandas as pd
from pathlib import Path

INPUT_CSV = "results/reconstructions.csv"
OUTPUT_DIR = Path("results/method_tables")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_CSV)

required_columns = [
    "index",
    "timestamp",
    "original_temperature",
    "damaged_temperature",
    "reconstructed_temperature",
    "mask",
    "scenario",
    "block_position",
    "missing_rate",
    "method",
]

missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    raise ValueError(f"Nedostaju stupci u CSV datoteci: {missing_columns}")

# Zadržavamo samo umjetno uklonjene vrijednosti jer se tu vidi što je metoda rekonstruirala
df_missing = df[df["mask"] == 1].copy()

df_missing["error"] = (
    df_missing["original_temperature"] - df_missing["reconstructed_temperature"]
).abs()

# Za uredniji prikaz
df_missing["missing_rate_percent"] = (df_missing["missing_rate"] * 100).round(0).astype("Int64")

columns_for_output = [
    "index",
    "timestamp",
    "scenario",
    "block_position",
    "missing_rate_percent",
    "method",
    "original_temperature",
    "damaged_temperature",
    "reconstructed_temperature",
    "error",
]

df_missing = df_missing[columns_for_output]

# Jedna velika Excel datoteka, svaki method/scenario/rate u svoj sheet
excel_path = OUTPUT_DIR / "sve_metode_rekonstrukcija.xlsx"

with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
    for (method, scenario, block_position, missing_rate), group in df_missing.groupby(
        ["method", "scenario", "block_position", "missing_rate_percent"],
        dropna=False
    ):
        block_position_text = str(block_position) if pd.notna(block_position) else "none"

        sheet_name = f"{method}_{scenario}_{block_position_text}_{missing_rate}"
        sheet_name = sheet_name.replace("/", "_").replace("\\", "_")[:31]

        group = group.sort_values("index")
        group.to_excel(writer, sheet_name=sheet_name, index=False)

# Odvojeni CSV za svaku metodu i scenarij
for (method, scenario, block_position, missing_rate), group in df_missing.groupby(
    ["method", "scenario", "block_position", "missing_rate_percent"],
    dropna=False
):
    block_position_text = str(block_position) if pd.notna(block_position) else "none"

    safe_name = f"{method}_{scenario}_{block_position_text}_{missing_rate}pct"
    safe_name = safe_name.replace("/", "_").replace("\\", "_").replace(" ", "_")

    output_path = OUTPUT_DIR / f"{safe_name}.csv"

    group = group.sort_values("index")
    group.to_csv(output_path, index=False, encoding="utf-8-sig")

# Sažetak po metodi
summary = (
    df_missing
    .groupby(["method", "scenario", "block_position", "missing_rate_percent"], dropna=False)
    .agg(
        number_of_values=("index", "count"),
        mean_absolute_error=("error", "mean"),
        max_error=("error", "max"),
        min_error=("error", "min"),
    )
    .reset_index()
)

summary_path = OUTPUT_DIR / "sazetak_rekonstrukcija_po_metodi.csv"
summary.to_csv(summary_path, index=False, encoding="utf-8-sig")

print("Gotovo.")
print(f"Excel tablice spremljene u: {excel_path}")
print(f"Odvojene CSV tablice spremljene u: {OUTPUT_DIR}")
print(f"Sažetak spremljen u: {summary_path}")
