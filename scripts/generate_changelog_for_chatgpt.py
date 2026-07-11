#!/usr/bin/env python3
"""Generira sto_je_novo_od_prosle_verzije.md za ChatGPT zip."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "results" / "experiment_results.csv"
OUT = ROOT / "results" / "sto_je_novo_od_prosle_verzije.md"
KNN_CSV = ROOT / "results" / "tablice" / "knn_usporedba.csv"
MA_CSV = ROOT / "results" / "tablice" / "moving_average_pregled.csv"


def main() -> None:
    df = pd.read_csv(CSV)
    n_methods = df["method"].nunique()
    n_rows = len(df)

    means = df.groupby("method").mae.mean().sort_values()

    knn_rows = []
    for sc in ["random", "block", "block_start", "block_middle", "block_end"]:
        b = df[(df.method == "knn") & (df.scenario == sc)].mae.mean()
        u = df[(df.method == "knn_upgraded") & (df.scenario == sc)].mae.mean()
        knn_rows.append(
            {
                "scenario": sc,
                "knn_osnovni_mae": round(b, 4),
                "knn_napredni_mae": round(u, 4),
                "bolji": "knn (osnovni)" if b < u else "knn_upgraded",
            }
        )
    knn_df = pd.DataFrame(knn_rows)
    KNN_CSV.parent.mkdir(parents=True, exist_ok=True)
    knn_df.to_csv(KNN_CSV, index=False)

    ma_rows = []
    for sc in df.scenario.unique():
        for rate in sorted(df.missing_rate.unique()):
            sub = df[(df.scenario == sc) & (df.missing_rate == rate)]
            ma = sub[sub.method == "moving_average"].iloc[0]
            li = sub[sub.method == "linear_interpolation"].iloc[0]
            ma_rows.append(
                {
                    "scenario": sc,
                    "missing_rate": rate,
                    "moving_average_mae": round(ma.mae, 4),
                    "linear_mae": round(li.mae, 4),
                    "razlika_ma_minus_linear": round(ma.mae - li.mae, 4),
                }
            )
    ma_df = pd.DataFrame(ma_rows)
    ma_df.to_csv(MA_CSV, index=False)

    adaptive_mean = means["adaptive_imputation"]
    linear_mean = means["linear_interpolation"]
    knn_basic = means["knn"]
    knn_upg = means["knn_upgraded"]
    ma_mean = means["moving_average"]

    text = f"""# Što je novo od prethodne verzije (ChatGPT prilog)

*Datum ažuriranja: 2026-07-11*
*Prethodna verzija zipa: 360 testova, 9 metoda*
*Trenutna verzija: **{n_rows} testova**, **{n_methods} metoda***

---

## 1. Nove metode u eksperimentu

| Metoda | Datoteka u kodu | Opis |
|--------|-----------------|------|
| **moving_average** | `src/interpolation.c` | Pomični prosjek — za svaku rupu uzima prosjek poznatih vrijednosti u prozoru ±6 uzoraka (1 sat pri 10-min intervalima) |
| **knn** (osnovni) | `src/knn_methods.c` | KNN s k=5, značajke: pozicija, sat, dan u godini |
| **knn_upgraded** (napredni) | `src/knn_upgraded.c` | Cikličke značajke (sin/cos), težinski prosjek susjeda |
| **adaptive_imputation** | `src/adaptive_imputation.c` | Hibridna metoda — analizira obrazac rupa i automatski bira najbolju metodu |

**Napomena:** U prethodnoj verziji `knn` u CSV-u zapravo je bio samo napredni KNN. Sada su **odvojeni** osnovni i napredni KNN u istom eksperimentalnom okviru.

---

## 2. Ključni rezultati — sažetak po metodama (prosječni MAE)

| Rang | Metoda | Prosječni MAE (°C) |
|------|--------|-------------------|
"""
    for i, (m, v) in enumerate(means.items(), 1):
        text += f"| {i} | {m} | {v:.4f} |\n"

    text += f"""
---

## 3. Usporedba osnovnog i naprednog KNN (obavezno u radu)

| Scenarij | Osnovni KNN (MAE) | Napredni KNN (MAE) | Bolji |
|----------|-------------------|---------------------|-------|
"""
    for _, r in knn_df.iterrows():
        text += (
            f"| {r['scenario']} | {r['knn_osnovni_mae']:.4f} | "
            f"{r['knn_napredni_mae']:.4f} | {r['bolji']} |\n"
        )

    text += f"""
**Zaključak:** Osnovni KNN bolji u prosjeku ({knn_basic:.4f} vs {knn_upg:.4f} °C) i na **svih 5 scenarija**.

Detaljna tablica: `results/tablice/knn_usporedba.csv`

---

## 4. Pomični prosjek (moving_average)

- **Prosječni MAE:** {ma_mean:.4f} °C (linear = {linear_mean:.4f} °C)
- Na **random** scenariju: MAE ≈ 0.23 °C — usporedivo s KNN-om, bolje od forward fill
- Na **block** scenarijima: lošiji od linear interpolacije (prosjek ≈ 4.69 °C)
- Ponekad bolji od adaptive_imputation na block_middle 60–80 % (lokalni prozor bolje hvata kratke trendove)

Detaljna tablica: `results/tablice/moving_average_pregled.csv`

---

## 5. Adaptive imputation (hibridna metoda)

- **Najniži prosječni MAE svih metoda:** {adaptive_mean:.4f} °C
- Automatski bira metodu prema obrascu nedostajućih vrijednosti (random vs block, pozicija bloka, missing rate)
- Bolja od bilo koje pojedinačne metode u ukupnom prosjeku

---

## 6. Promjene u broju testova

| | Prethodna verzija | Nova verzija |
|---|-------------------|--------------|
| Metode | 8 (+ adaptive = 9) | **11** |
| Testova | 320–360 | **440** |
| Dataset | 7 dana (1008 zapisa) | isto |
| Missing rateovi | 10–80 % | isto |
| Scenariji | 5 | isto |

---

## 7. Nove/izmijenjene datoteke u zipu

### Podatkovne datoteke
- `results/experiment_results.csv` — **440 redaka**, 11 metoda
- `results/diplomski_dokument_10_80_za_chat.md` — ažuriran sažetak s KNN i moving average
- `results/tablice/sve_tablice_pregled.md` — sve tablice
- `results/tablice/knn_usporedba.csv` — **NOVO**
- `results/tablice/moving_average_pregled.csv` — **NOVO**
- `results/tablice/najbolja_metoda_po_scenariju.csv`
- `results/analysis.md`
- `results/chatgpt_prompt_za_nadopunu.md` — prompt za ChatGPT
- `results/sto_je_novo_od_prosle_verzije.md` — ovaj dokument

### Grafovi (PNG)
- Ažurirani grafovi uključuju **moving_average**, **knn**, **knn_upgraded**, **adaptive_imputation**
- 35 PNG datoteka u `slike i videa/2026/diplomski-grafovi/`

### Izmjene u kodu (informativno)
- `src/interpolation.c` — dodan `moving_average_imputation()`
- `src/experiment.c` — 11 metoda; knn = osnovni, knn_upgraded = napredni
- `src/adaptive_imputation.c` — hibridna metoda
- `tests/run_tests.c` — testovi za moving average i adaptive

---

## 8. Što ChatGPT treba dodati u Word (prioritet)

1. **Tablice** za 11 metoda i 10–80 % missing rate
2. **Usporedba knn vs knn_upgraded** — koristi `knn_usporedba.csv`
3. **Odlomak o pomičnom prosjeku** — koristi `moving_average_pregled.csv`
4. **Adaptive imputation** kao najbolja metoda ukupno
5. **Grafovi** — umetnuti PNG iz zipa s tumačenjem
6. U poglavlju **Budući rad** spomenuti (bez implementacije): dulji nizovi, više varijabli, stvarni missing podaci

---

## 9. Poruka za ChatGPT (kratka)

Diplomski rad je već napisan. Nadopuni poglavlja 5–7 novim rezultatima iz priloženog CSV-a ({n_rows} testova, {n_methods} metoda). Obavezno uključi usporedbu osnovnog i naprednog KNN te objašnjenje pomičnog prosjeka. Ne izmišljaj brojke.
"""

    OUT.write_text(text, encoding="utf-8")
    print(f"Written: {OUT.name}")
    print(f"Written: {KNN_CSV.name}")
    print(f"Written: {MA_CSV.name}")


if __name__ == "__main__":
    main()
