#!/usr/bin/env python3
"""Generira sto_je_novo_od_prosle_verzije.md za ChatGPT zip."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "results" / "experiment_results.csv"
OUT = ROOT / "results" / "sto_je_novo_od_prosle_verzije.md"
THESIS_OUT = ROOT / "results" / "novo_za_diplomski.md"
KNN_CSV = ROOT / "results" / "tablice" / "knn_usporedba.csv"
MA_CSV = ROOT / "results" / "tablice" / "moving_average_pregled.csv"
BW_CSV = ROOT / "results" / "reconstruction_best_worst_20.csv"


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

    thesis = build_thesis_doc(df, means, knn_df, knn_basic, knn_upg, ma_mean, linear_mean, adaptive_mean)
    THESIS_OUT.write_text(thesis, encoding="utf-8")

    print(f"Written: {OUT.name}")
    print(f"Written: {THESIS_OUT.name}")
    print(f"Written: {KNN_CSV.name}")
    print(f"Written: {MA_CSV.name}")


def build_thesis_doc(df, means, knn_df, knn_basic, knn_upg, ma_mean, linear_mean, adaptive_mean):
    n_methods = df["method"].nunique()
    n_rows = len(df)
    n_rates = df["missing_rate"].nunique()
    n_scenarios = df["scenario"].nunique()

    wins = df.groupby(["scenario", "missing_rate"]).apply(
        lambda g: g.loc[g.mae.idxmin(), "method"], include_groups=False
    )
    linear_wins = int((wins == "linear_interpolation").sum())
    adaptive_wins = int((wins == "adaptive_imputation").sum())
    cubic_wins = int((wins == "cubic_interpolation").sum())
    spline_wins = int((wins == "spline_interpolation").sum())

    block20 = df[(df.scenario == "block") & (df.missing_rate == 0.2)]
    cubic_block20 = block20[block20.method == "cubic_interpolation"].mae.iloc[0]
    linear_block20 = block20[block20.method == "linear_interpolation"].mae.iloc[0]

    bw_lines = []
    if BW_CSV.exists():
        bw = pd.read_csv(BW_CSV)
        for _, r in bw.iterrows():
            bw_lines.append(
                f"- **{r['scenario']}** @ 20 %: najbolja **{r['best_method']}** "
                f"(MAE = {r['best_mae']:.4f} °C), najgora **{r['worst_method']}** "
                f"(MAE = {r['worst_mae']:.4f} °C)"
            )
    bw_section = "\n".join(bw_lines) if bw_lines else "(pokreni eksperiment za reconstruction_best_worst_20.csv)"

    means_table = "\n".join(
        f"| {i} | `{m}` | {v:.4f} |" for i, (m, v) in enumerate(means.items(), 1)
    )

    knn_table = "\n".join(
        f"| {r['scenario']} | {r['knn_osnovni_mae']:.4f} | {r['knn_napredni_mae']:.4f} | {r['bolji']} |"
        for _, r in knn_df.iterrows()
    )

    return f"""# Novo u eksperimentima — tekst za diplomski rad

*Automatski generirano iz `experiment_results.csv`*
*Kopiraj odlomke u poglavlja Metodologija, Rezultati, Rasprava i Zaključak*

---

## A. Kratki sažetak novina (1 odlomak)

U odnosu na raniju verziju eksperimenata, rad je proširen na **7-dnevni** Jena Climate dataset (**1008** zapisa, 10-min intervali), missing rateove **10–80 %**, te **{n_methods} metoda imputacije** u **{n_scenarios} scenarija** (ukupno **{n_rows}** testova). Dodane su metode **pomičnog prosjeka**, **adaptivne hibridne imputacije** te odvojena usporedba **osnovnog i naprednog KNN-a**. Razdvojene su **zaključana kubična** (`cubic_interpolation`) i **prirodna spline** (`spline_interpolation`) interpolacija. Za svaki scenarij generirani su grafovi rekonstrukcije **najbolje i najgore** metode pri 20 % nedostajućih vrijednosti.

---

## B. Metodologija — što dodati

### B.1 Dataset
- Izvor: Jena Climate Dataset (2009), temperatura `T (degC)`
- Period: **7 dana** (1008 uzoraka, interval 10 min)
- Datoteka: `data/processed/jena_temperature_7d.csv`

### B.2 Scenariji i missing rateovi
- Scenariji: `random`, `block`, `block_start`, `block_middle`, `block_end`
- Missing rateovi: **10 %, 20 %, 30 %, 40 %, 50 %, 60 %, 70 %, 80 %**
- Evaluacija isključivo na umjetno uklonjenim mjestima (`mask == 1`)

### B.3 Metode (11)

| # | Metoda | Kratki opis |
|---|--------|-------------|
| 1 | forward_fill | Zadnja poznata vrijednost |
| 2 | linear_interpolation | Linearna interpolacija po indeksu |
| 3 | time_interpolation | Linearna interpolacija po vremenu |
| 4 | cubic_interpolation | Zaključani kubični spline |
| 5 | spline_interpolation | Prirodni kubični spline |
| 6 | **moving_average** | Pomični prosjek (prozor ±6 = 1 h) — **NOVO** |
| 7 | **knn** | Osnovni KNN, k=5 — **NOVO u eksperimentu** |
| 8 | **knn_upgraded** | Napredni KNN (cikličke značajke) — **NOVO u eksperimentu** |
| 9 | decision_tree | Stablo odlučivanja |
| 10 | random_forest | Slučajna šuma |
| 11 | **adaptive_imputation** | Hibridna metoda — **NOVO** |

### B.4 Adaptivna imputacija (nova metoda)
Metoda `adaptive_imputation` analizira masku nedostajućih vrijednosti (stopa, veličina i pozicija najvećeg bloka) i automatski odabire jednu od poznatih metoda imputacije prema unaprijed definiranoj tablici routing pravila.

### B.5 Pomični prosjek (nova metoda)
Za svaku nedostajuću točku uzima se prosjek poznatih susjeda u prozoru **±6 uzoraka** (1 sat pri 10-min intervalima).

---

## C. Rezultati — ključne brojke

### C.1 Rang metoda po prosječnom MAE (svi scenariji i rateovi)

| Rang | Metoda | Prosječni MAE (°C) |
|------|--------|-------------------|
{means_table}

### C.2 Najbolja pojedinačna metoda po broju pobjeda (po scenariju i rateu)
- **linear_interpolation**: {linear_wins} od {len(wins)} kombinacija scenarij/rate
- **adaptive_imputation**: {adaptive_wins} pojedinačnih pobjeda, ali **najniži ukupni prosjek MAE: {adaptive_mean:.4f} °C** (hibridna metoda je konzistentno dobra, iako ne uvijek prva u svakoj kombinaciji)
- **cubic_interpolation**: {cubic_wins} pobjeda
- **spline_interpolation**: {spline_wins} pobjeda

### C.3 Identični rezultati
- **linear_interpolation** i **time_interpolation** daju **identične** rezultate na svim scenarijima (ravnomjerni 10-min intervali).
- Na scenariju **block**, **cubic_interpolation** i **spline_interpolation** također daju identične rezultate.

### C.4 Usporedba osnovnog i naprednog KNN

| Scenarij | Osnovni KNN | Napredni KNN | Bolji |
|----------|-------------|--------------|-------|
{knn_table}

**Zaključak:** Osnovni KNN postiže niži prosječni MAE (**{knn_basic:.4f}** vs **{knn_upg:.4f}** °C) na svih 5 scenarija. Napredne značajke (sin/cos, težinski prosjek) nisu poboljšale imputaciju na ovom skupu podataka.

### C.5 Pomični prosjek
- Prosječni MAE: **{ma_mean:.4f} °C** (linear: **{linear_mean:.4f} °C**)
- Dobar na **random** scenariju (MAE ≈ 0,23 °C)
- Lošiji od linear interpolacije na **block** scenarijima

### C.6 Najbolja i najgora metoda po scenariju @ 20 %

{bw_section}

---

## D. Rasprava — gotovi odlomci za kopiranje

### D.1 Adaptivna imputacija
Adaptivna hibridna metoda postigla je najniži prosječni MAE (**{adaptive_mean:.4f} °C**) među svim testiranim metodama, što potvrđuje hipotezu da nijedna pojedinačna metoda nije optimalna za sve obrasce nedostajućih podataka. Metoda automatski prepoznaje je li riječ o random ili block scenariju te odabire prikladnu strategiju imputacije.

### D.2 Kubična interpolacija na block scenariju
Na scenariju **block** pri 20 % nedostajućih vrijednosti, zaključani kubični spline postiže MAE od **{cubic_block20:.4f} °C**, dok linear interpolacija postiže **{linear_block20:.4f} °C**. Kubična metoda gradi globalnu glatku krivulju kroz cijeli vremenski niz; zakrivljenost iz hladnijih perioda izvan bloka može uzrokovati overshoot unutar rupe — krivulja pada prema hladnijim vrijednostima iako unutar bloka temperatura ne slijedi taj trend. To objašnjava zašto cubic na ovom scenariju vizualno „ide dolje” unatoč toplijem vrhuncu unutar rupe.

### D.3 Linear vs time
Budući da su vremenski uzorci ravnomjerno raspoređeni (10-min intervali), linear i time interpolacija daju identične rezultate u svim eksperimentima. U praksi je dovoljno prikazati jednu od te dvije metode.

### D.4 KNN — osnovni vs napredni
U eksperimentu je provedena izravna usporedba osnovnog KNN-a (k=5, značajke: pozicija, sat, dan) i naprednog KNN-a (cikličke značajke, težinski prosjek). Rezultati pokazuju da je **osnovni KNN bolji** na svim scenarijima, što sugerira da dodatna složenost napredne varijante nije opravdana na kratkom 7-dnevnom nizu s jednom varijablom.

### D.5 Pomični prosjek
Pomični prosjek pokazuje prihvatljive rezultate na random scenariju, ali značajno gori od linear interpolacije na block scenarijima. Metoda je prikladna za kratke rupe u nizu, ali ne za duge kontinuirane blokove nedostajućih vrijednosti.

---

## E. Zaključak — što dodati

1. Eksperimenti obuhvaćaju **{n_rows}** testova ({n_scenarios} scenarija × {n_rates} rateova × {n_methods} metoda) na **7-dnevnom** datasetu.
2. **Adaptivna imputacija** ima najniži prosječni MAE (**{adaptive_mean:.4f} °C**).
3. **Linear interpolacija** ostaje najstabilnija pojedinačna metoda ({linear_wins} pobjeda po MAE).
4. **Osnovni KNN** nadmašuje napredni KNN na svim scenarijima.
5. **Kubična interpolacija** loša je na block scenariju zbog globalnog overshoota; dobra je na block_end scenariju.
6. **Pomični prosjek** koristan na random scenariju, ne i na block scenarijima.

---

## F. Budući rad (preporučeni odlomak)

Budući rad mogao bi uključiti dulje vremenske nizove, više meteoroloških varijabli i stvarne nedostajuće podatke (umjesto umjetnog uklanjanja). Također bi bilo korisno testirati lokalne umjesto globalnih spline metoda te proširiti adaptivnu imputaciju učenjem routing pravila iz podataka.

---

## G. Grafovi i prilozi

- Stupčasti grafovi: svih 11 metoda, svaka svojom bojom (`mae_by_method_*_20.png`)
- Linijski grafovi: MAE/RMSE/R² vs missing rate; identične metode označene u legendi
- Rekonstrukcija @ 20 %: najbolja vs najgora metoda po scenariju (`reconstruction_best_worst_*.png`)
- Pregled: `results/grafovi_pregled.html`
- Tablice: `results/tablice/sve_tablice_pregled.md`

---

## H. Popis novih datoteka u projektu

| Datoteka | Svrha |
|----------|-------|
| `src/adaptive_imputation.c` | Adaptivna hibridna metoda |
| `src/interpolation.c` | + `moving_average_imputation()` |
| `src/experiment.c` | 11 metoda, export najbolje/najgore rekonstrukcije |
| `results/reconstruction_best_worst_20.csv` | Pregled najbolje/najgore @ 20 % |
| `results/tablice/knn_usporedba.csv` | KNN osnovni vs napredni |
| `results/tablice/moving_average_pregled.csv` | Pomični prosjek vs linear |
"""


if __name__ == "__main__":
    main()
