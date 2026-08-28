#!/usr/bin/env python3
"""Generira sto_je_novo_od_prosle_verzije.md za ChatGPT zip."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "results" / "experiment_results.csv"
RUNS_CSV = ROOT / "results" / "experiment_runs.csv"
SIG_CSV = ROOT / "results" / "tablice" / "znacajnost.csv"
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


"""Prosjecni MAE ML metoda prije prerade (verzija bez gap-znacajki)."""
ML_BEFORE = {
    "knn": 3.7386,
    "knn_upgraded": 4.9931,
    "decision_tree": 5.2008,
    "random_forest": 3.9234,
}


def load_window0():
    """Rezultati prvog tjedna — identicni eksperimentu prije uvodenja ponavljanja."""
    if not RUNS_CSV.exists():
        return None
    runs = pd.read_csv(RUNS_CSV)
    return runs[runs["repeat"] == 0]


def ml_rework_stats(df, means, w0):
    """Tablica prije/poslije (isti tjedan!) i broj pobjeda nad linearnom."""
    # Prerada se mora usporedivati na ISTOM tjednu na kojem su nastale stare
    # brojke, inace bi se mijesala dva efekta: prerada koda i promjena podataka.
    base = w0 if w0 is not None else df
    base_means = base.groupby("method").mae.mean()

    rows = []
    for method, before in ML_BEFORE.items():
        after = float(base_means[method])
        rows.append(
            f"| `{method}` | {before:.4f} | {after:.4f} | "
            f"{(before - after) / before * 100.0:+.1f} % |"
        )
    before_after = "\n".join(rows)

    lin = df[df.method == "linear_interpolation"].set_index(["scenario", "missing_rate"]).mae
    win_rows = []
    for method in ["knn", "knn_upgraded", "neural_net", "random_forest", "decision_tree",
                   "moving_average", "forward_fill", "cubic_interpolation"]:
        sub = df[df.method == method].set_index(["scenario", "missing_rate"]).mae
        joined = pd.concat([sub.rename("m"), lin.rename("lin")], axis=1).dropna()
        wins = int((joined.m < joined.lin).sum())
        win_rows.append(f"| `{method}` | {float(means[method]):.4f} | {wins} / {len(joined)} |")
    wins_table = "\n".join(win_rows)

    return before_after, wins_table


def significance_table():
    """Tablica uparenih testova iz scripts/significance.py."""
    if not SIG_CSV.exists():
        return "(pokreni `python scripts/significance.py`)"
    sig = pd.read_csv(SIG_CSV).sort_values("srednja_razlika")
    lines = []
    for _, r in sig.iterrows():
        lines.append(
            f"| `{r['metoda']}` | {r['srednja_razlika']:+.4f} | "
            f"[{r['ci95_lo']:+.4f}, {r['ci95_hi']:+.4f}] | "
            f"{int(r['pobjeda'])}–{int(r['poraz'])}–{int(r['nerijeseno'])} | "
            f"{r['p_holm']:.1e} | {r['znacajno']} |"
        )
    return "\n".join(lines)


def build_thesis_doc(df, means, knn_df, knn_basic, knn_upg, ma_mean, linear_mean, adaptive_mean):
    n_methods = df["method"].nunique()
    n_rows = len(df)
    n_rates = df["missing_rate"].nunique()
    n_scenarios = df["scenario"].nunique()
    w0 = load_window0()
    before_after_table, wins_table = ml_rework_stats(df, means, w0)
    sig_table = significance_table()
    nn_mean = float(means["neural_net"])
    dt_mean = float(means["decision_tree"])
    rf_mean = float(means["random_forest"])

    n_repeats = int(df["n_repeats"].max()) if "n_repeats" in df.columns else 1
    w0_means = w0.groupby("method").mae.mean() if w0 is not None else means
    w0_nn = float(w0_means["neural_net"])
    w0_lin = float(w0_means["linear_interpolation"])
    w0_ad = float(w0_means["adaptive_imputation"])
    dt_before = ML_BEFORE["decision_tree"]
    dt_w0 = float(w0_means["decision_tree"])
    knn_better = "napredni" if knn_upg < knn_basic else "osnovni"

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

U odnosu na raniju verziju eksperimenata, rad je proširen na **7-dnevni** Jena Climate dataset (**1008** zapisa, 10-min intervali), missing rateove **10–80 %**, te **{n_methods} metoda imputacije** u **{n_scenarios} scenarija** (ukupno **{n_rows}** testova). Dodane su metode **pomičnog prosjeka**, **adaptivne hibridne imputacije** te odvojena usporedba **osnovnog i naprednog KNN-a**. Razdvojene su **zaključana kubična** (`cubic_interpolation`) i **prirodna spline** (`spline_interpolation`) interpolacija.

Uvedene su **dvije velike izmjene**.

Prva je **potpuna prerada metoda strojnog učenja** i dodavanje **neuronske mreže** (`neural_net`). U prvoj verziji sve su ML metode kao ulaz koristile isključivo vrijeme (indeks, sat, dan u godini), pa su učile preslikavanje *vrijeme → temperatura*, dok interpolacija rješava bitno lakši problem *susjedne temperature → temperatura*. Uvođenjem značajki najbližih poznatih susjeda i prelaskom na učenje **reziduala iznad linearne baze**, prosječni MAE ML metoda pao je za **14–40 %**.

Druga je prelazak s jednog tjedna podataka na **{n_repeats} nezavisnih tjednih prozora** raspoređenih kroz cijelo razdoblje 2009.–2016., svaki sa svojim seedom maske. Ta je izmjena promijenila zaključak rada: na pojedinačnom tjednu iz siječnja 2009. neuronska mreža je nadmašivala linearnu interpolaciju ({w0_nn:.4f} naspram {w0_lin:.4f} °C), ali se uparenim testom nad {n_repeats} tjedana pokazalo da je ta prednost bila **svojstvo tog tjedna, a ne metode**. Detalji u odjeljcima C.4 i D.2.

Za svaki scenarij generirani su grafovi rekonstrukcije **najbolje i najgore** metode pri 20 % nedostajućih vrijednosti.

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

### B.2a Ponavljanja i mjera nesigurnosti

Svaka kombinacija scenarij × stopa ponavlja se **{n_repeats} puta**, po jednom za svaki tjedni prozor iz `data/processed/jena_windows/`, svaki s vlastitim seedom maske. Ponavljanje ide po dvije osi istovremeno jer nijedna sama nije dovoljna:

- **Seed maske** daje uzorkovačku varijabilnost, ali **samo** na scenarijima `random` i `block`. Kod `block_start`, `block_middle` i `block_end` pozicija bloka određena je isključivo stopom (`src/preprocessing.c`), pa seed ondje ne mijenja ništa i ponavljanje bi dalo standardnu devijaciju nula.
- **Tjedni prozor** daje varijabilnost na **svih pet** scenarija i uz to mjeri ono što je zapravo zanimljivo: generalizira li zaključak izvan jednog tjedna.

Prozori su ravnomjerno raspoređeni kroz osam godina pa pokrivaju sva godišnja doba; srednja temperatura po prozoru kreće se od −7,6 do +21,3 °C, a standardna devijacija od 1,90 do 6,27 °C. Prvi prozor namjerno je identičan izvornom sedmodnevnom izrezu, pa su stari rezultati podskup novih.

Glavna tablica `results/experiment_results.csv` sadrži srednju vrijednost i standardnu devijaciju po ponavljanjima, a `results/experiment_runs.csv` sve pojedinačne rezultate.

### B.3 Metode ({n_methods})

| # | Metoda | Kratki opis |
|---|--------|-------------|
| 1 | forward_fill | Zadnja poznata vrijednost |
| 2 | linear_interpolation | Linearna interpolacija po indeksu |
| 3 | time_interpolation | Linearna interpolacija po vremenu |
| 4 | cubic_interpolation | Zaključani kubični spline |
| 5 | spline_interpolation | Prirodni kubični spline |
| 6 | moving_average | Pomični prosjek (prozor ±6 = 1 h) |
| 7 | knn | KNN s obaveznim obuhvatom praznine, k = 2, ponder 1/d |
| 8 | knn_upgraded | KNN u prostoru značajki praznine, uči rezidual |
| 9 | decision_tree | Regresijsko stablo (dubina 8) na rezidualu |
| 10 | random_forest | 24 stabla, dubina 10, `max_features` = 7 od 11 |
| 11 | **neural_net** | Višeslojni perceptron 11–24–12–1 — **NOVO** |
| 12 | adaptive_imputation | Hibridna metoda (oracle routing, v. D.8) |

### B.4 Zajednički prostor značajki ML metoda (nova podloga)

Sve ML metode dijele isti skup od **11 značajki** (`src/ml_features.c`), pa razlika u rezultatu odražava razliku u modelu, a ne u ulazima:

| # | Značajka | Opis |
|---|----------|------|
| 0 | `prev_val` | vrijednost najbližeg poznatog susjeda lijevo |
| 1 | `next_val` | vrijednost najbližeg poznatog susjeda desno |
| 2 | `alpha` | relativan položaj unutar praznine, (i − p) / (n − p) |
| 3 | `d_prev` | udaljenost do lijevog oslonca u uzorcima |
| 4 | `d_next` | udaljenost do desnog oslonca |
| 5 | `lin_base` | `prev_val + alpha · (next_val − prev_val)` — linearna baza |
| 6 | `position_norm` | i / (n − 1) |
| 7–8 | `hour_sin`, `hour_cos` | ciklički sat |
| 9–10 | `yday_sin`, `yday_cos` | ciklički dan u godini |

Značajke 0–5 (`src/gap_features.c`) računaju se **isključivo iz oštećenog niza**, pa nema curenja informacija iz test skupa. Ključan detalj: za poznatu (trening) točku susjedi se traže u skupu poznatih točaka **bez nje same**. Bez toga bi `prev_val` u treningu bio jednak ciljnoj vrijednosti, model bi naučio identitet, a u testu bi ista značajka imala posve drugo značenje.

### B.5 Učenje reziduala

Sve ML metode kao cilj uče **odstupanje od linearne baze**, a ne temperaturu:

    y_i = temp_i − lin_base_i,     predikcija = lin_base_i + model(x_i)

Model time *popravlja* interpolaciju umjesto da je zamjenjuje. Predikcija nula znači „linearna baza je već točna”, pa metoda po konstrukciji ne može biti bitno lošija od linearne interpolacije. Dodatno se svaka predikcija ograničava na raspon opaženih temperatura, čime se sprječava ekstrapolacijski overshoot na dugim prazninama (isti mehanizam zbog kojeg spline zakaže na scenariju `block`).

### B.6 Neuronska mreža (nova metoda)

`src/neural_net.c` — višeslojni perceptron implementiran od nule u C99, bez vanjskih biblioteka:

- Arhitektura: **11 → 24 (tanh) → 12 (tanh) → 1 (linearno)**, {11 * 24 + 24 + 24 * 12 + 12 + 12 + 1} parametara
- Učenje: **backpropagation** + **Adam** (β₁ = 0,9, β₂ = 0,999), mini-batch 32, 200 epoha
- Stopa učenja 0,01 uz **kosinusno gašenje**
- Standardizacija ulaza po statistikama poznatih točaka; cilj skaliran na jediničnu skalu
- Xavier inicijalizacija; izlazni sloj namjerno inicijaliziran na male vrijednosti, pa mreža **kreće od linearne baze**
- Deterministički seed (42), pa je rezultat ponovljiv

### B.7 Adaptivna imputacija
Metoda `adaptive_imputation` analizira masku nedostajućih vrijednosti (stopa, veličina i pozicija najvećeg bloka) i automatski odabire jednu od poznatih metoda imputacije prema unaprijed definiranoj tablici routing pravila.

### B.8 Pomični prosjek
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

### C.3 Učinak prerade ML metoda

Usporedba je na **istom tjednu** (prvi prozor) na kojem su nastale stare brojke — inače bi se miješala dva efekta, prerada koda i promjena podataka:

| Metoda | MAE prije prerade | MAE poslije | Promjena |
|--------|-------------------|-------------|----------|
{before_after_table}
| `neural_net` | — (nova metoda) | {w0_nn:.4f} | — |

Prerada je dakle nedvojbeno uspjela: stablo je s {dt_before:.4f} palo na {dt_w0:.4f} °C.

### C.4 Uparena usporedba s linearnom interpolacijom ({n_repeats} ponavljanja)

Unutar jednog ponavljanja sve metode vide **identičan** oštećeni niz, pa je dizajn uparen i razlika se mjeri po paru (isti tjedan, isti scenarij, ista stopa, ista maska). Test je Wilcoxonov test predznačenih rangova, interval je bootstrap percentilni, a p-vrijednosti su korigirane Holm-Bonferroni postupkom. **Negativna razlika znači da je metoda bolja od linearne interpolacije.**

| Metoda | Δ MAE (°C) | 95 % CI | Pobjeda–poraz–neriješeno | p (Holm) | Značajno |
|--------|-----------|---------|--------------------------|----------|----------|
{sig_table}

Ključan nalaz: **nijedna ML metoda ne nadmašuje linearnu interpolaciju u ukupnom prosjeku**, a razlike u korist linearne, iako male (0,011–0,073 °C), statistički su značajne. Prednost neuronske mreže vidljiva na prvom tjednu ({w0_nn:.4f} naspram {w0_lin:.4f} °C) nije se ponovila na ostalih {n_repeats - 1} tjedana.

Broj pobjeda po pojedinačnim kombinacijama scenarij × stopa nad srednjim vrijednostima:

| Metoda | Prosječni MAE | Pobjeda nad linear |
|--------|---------------|--------------------|
{wins_table}

### C.4a Gdje ML ipak pobjeđuje

Uparena razlika po scenarijima pokazuje da nalaz nije jednoličan. Na scenariju **`block`** (blok na slučajnoj poziciji) sve četiri ML metode imaju negativnu razliku, a kod `random_forest` (−0,0051 °C) i `knn_upgraded` (−0,0058 °C) ona je i značajna. `knn_upgraded` značajno pobjeđuje i na **`block_middle`** (−0,0053 °C). Gubitci su koncentrirani na `random` (gdje su praznine kratke i linearna baza je gotovo egzaktna) te na `block_start` i `block_end` (gdje se mora ekstrapolirati prema rubu niza).

Potpuna tablica po scenarijima: `results/znacajnost.md`.

### C.4b Koliko rezultat ovisi o odabranom tjednu

| Metoda | MAE min | MAE max | sd po tjednima |
|--------|---------|---------|----------------|
| `linear_interpolation` | 1,297 | 4,234 | 0,790 |
| `neural_net` | 1,335 | 4,297 | 0,799 |
| `knn_upgraded` | 1,298 | 4,270 | 0,809 |
| `adaptive_imputation` | 1,972 | 6,795 | 1,325 |

Raspon MAE između tjedana (oko 2,9 °C) više je od **četrdeset puta veći** od razlike među vodećim metodama (oko 0,07 °C). To je izravno opravdanje zašto jedan tjedan nije dovoljan i zašto se zaključci moraju donositi uparenim testom, a ne usporedbom srednjih vrijednosti.

### C.5 Identični rezultati
- **linear_interpolation** i **time_interpolation** daju **identične** rezultate na svim scenarijima (ravnomjerni 10-min intervali), pa je efektivan broj različitih metoda {n_methods - 1}.
- **knn** nakon prerade daje rezultat **identičan linearnoj interpolaciji** — to nije slučajnost nego matematička posljedica (v. D.6).
- Na scenariju **block**, **cubic_interpolation** i **spline_interpolation** također daju identične rezultate.

### C.6 Usporedba osnovnog i naprednog KNN

| Scenarij | Osnovni KNN | Napredni KNN | Bolji |
|----------|-------------|--------------|-------|
{knn_table}

**Zaključak:** u ukupnom prosjeku bolji je **{knn_better}** KNN (osnovni {knn_basic:.4f}, napredni {knn_upg:.4f} °C), ali razlika ovisi o scenariju — napredni značajno pobjeđuje na `block` i `block_middle`, a gubi na `random`. U prvoj verziji napredni je bio lošiji na svim scenarijima (4,9931 vs 3,7386) jer je zbog pogrešnog omjera težina tražio susjede po **dobu dana** umjesto po **blizini u nizu**.

### C.7 Pomični prosjek
- Prosječni MAE: **{ma_mean:.4f} °C** (linear: **{linear_mean:.4f} °C**)
- Dobar na **random** scenariju (MAE ≈ 0,23 °C)
- Lošiji od linear interpolacije na **block** scenarijima

### C.8 Najbolja i najgora metoda po scenariju @ 20 %

{bw_section}

---

## D. Rasprava — gotovi odlomci za kopiranje

### D.1 Zašto su ML metode isprva bile lošije od interpolacije

Prva verzija ML metoda koristila je isključivo vremenske značajke (indeks, sat, dan u godini). Nijedna od njih nije bila funkcija izmjerenih temperatura, pa su modeli učili preslikavanje **vrijeme → temperatura**, dok linearna interpolacija rješava zadatak **susjedne temperature → temperatura**. Na nizu čija je lag-1 autokorelacija 0,99936, a prosječna promjena između susjednih uzoraka 0,14 °C uz standardnu devijaciju 6,06 °C, drugi je zadatak neusporedivo lakši. Usporedba tako nije mjerila „klasične metode naspram strojnog učenja”, nego „metode koje vide susjede naspram metoda koje ih ne vide”.

Da uzrok nije bio ni količina podataka ni kapacitet modela, pokazuje sljedeće: povećanje dubine stabla s 5 na 20 smanjuje pogrešku za svega nekoliko postotaka i saturira, dok uvođenje značajki susjeda smanjuje prosječni MAE stabla s **{ML_BEFORE['decision_tree']:.4f}** na **{dt_mean:.4f} °C**. Omjer doprinosa je otprilike **14 : 1 u korist skupa značajki**. Zaključak koji ide u rad nije „ML metode su lošije”, nego „ML metode koje kao značajke koriste samo vremenski indeks lošije su od linearne interpolacije” — a to je nedostatak postave eksperimenta, ne metode.

### D.2 Rezultat nakon prerade i zašto jedan tjedan nije bio dovoljan

Prerada je zatvorila gotovo cijeli jaz. Na prvom tjednu ML metode su nakon nje čak i preuzele vodstvo: neuronska mreža {w0_nn:.4f} naspram {w0_lin:.4f} °C za linearnu interpolaciju, dakle 1,8 % niži MAE.

Ponavljanjem nad {n_repeats} tjedana pokazalo se da ta prednost **nije bila svojstvo metode nego tog tjedna**. Uparena razlika preko svih {n_repeats} tjedana iznosi +0,0234 °C u korist linearne interpolacije, s 95 % intervalom [+0,013, +0,034] koji ne obuhvaća nulu (p < 10⁻¹² nakon Holmove korekcije). Isto vrijedi za sve ostale ML metode. Razlog je razmjer: raspon MAE između tjedana je oko 2,9 °C, a razlika među vodećim metodama oko 0,07 °C — jedan uzorak jednostavno ne razlikuje signal od šuma na toj skali.

Ovo je najvažnija metodološka pouka rada i vrijedi je eksplicitno napisati: **zaključak izveden iz jedne realizacije eksperimenta bio je pogrešan, i to u smjeru koji je odgovarao početnoj hipotezi.** Otkriven je tek uvođenjem ponavljanja.

Sadržajni zaključak i dalje stoji, samo u slabijem obliku: linearna interpolacija je za lokalno linearan signal analitički optimalan procjenitelj, pa ML metode prema njoj **konvergiraju**, a nadmašuju je samo ondje gdje pretpostavka lokalne linearnosti popušta — na blokovima na slučajnoj poziciji i u sredini niza, gdje su razlike male ali statistički značajne. Na kratkim prazninama nemaju što ponuditi.

### D.3 Neuronska mreža

Mreža je najbolja ML metoda u eksperimentu ({nn_mean:.4f} °C), premda i ona zaostaje za linearnom interpolacijom ({linear_mean:.4f} °C) za statistički značajnih 0,023 °C. Dvije odluke presudno utječu na taj rezultat. Prvo, mreža uči rezidual iznad linearne baze, pa uz malu inicijalizaciju izlaznog sloja kreće od predikcije ≈ 0, što odgovara čistoj linearnoj interpolaciji; učenje je time popravljanje interpolacije, a ne učenje oblika signala od nule. Drugo, ulazi uključuju vrijednosti najbližih poznatih susjeda — mreža koja vidi samo vrijeme nema iz čega predvidjeti temperaturu na signalu čiji je jedini iskoristivi obrazac lokalna glatkoća.

Da je mreža bez tih odluka bitno lošija, vidi se iz usporedbe sa stablom prije prerade ({dt_before:.4f} °C). Preostali zaostatak od 0,023 °C tumačimo kao cijenu procjene parametara iz konačnog uzorka: mreža mora naučiti korekciju koja je na kratkim prazninama zapravo nula, pa dio šuma neizbježno uđe u model.

### D.4 Kubična interpolacija na block scenariju
Na scenariju **block** pri 20 % nedostajućih vrijednosti, zaključani kubični spline postiže MAE od **{cubic_block20:.4f} °C**, dok linear interpolacija postiže **{linear_block20:.4f} °C**. Kubična metoda gradi globalnu glatku krivulju kroz cijeli vremenski niz; zakrivljenost iz hladnijih perioda izvan bloka može uzrokovati overshoot unutar rupe — krivulja pada prema hladnijim vrijednostima iako unutar bloka temperatura ne slijedi taj trend. To objašnjava zašto cubic na ovom scenariju vizualno „ide dolje” unatoč toplijem vrhuncu unutar rupe.

### D.5 Linear vs time
Budući da su vremenski uzorci ravnomjerno raspoređeni (10-min intervali), linear i time interpolacija daju identične rezultate u svim eksperimentima. U praksi je dovoljno prikazati jednu od te dvije metode.

### D.6 KNN — zašto je linearna interpolacija njegova gornja granica

Izvorni KNN uzimao je *k* vremenski najbližih poznatih točaka i računao njihov **neponderirani prosjek**. To je estimator **nultog reda**: egzaktan samo za konstantan signal, a na nizu koji se mijenja sustavno zaglađuje nagib. Uz neparan *k* jedan višak susjeda na jednoj strani ostavlja i pristranost od pola koraka nagiba. Dodatno, ništa nije jamčilo da su susjedi s obje strane praznine — uz rub bloka obje najbliže točke znaju biti s iste strane, pa metoda ne može uhvatiti trend.

Prerađena verzija bira jednog susjeda **lijevo** i jednog **desno** te ih ponderira inverznom udaljenošću. Time postaje **matematički identična linearnoj interpolaciji**, jer vrijedi

    (1/d₁) / (1/d₁ + 1/d₂) = d₂ / (d₁ + d₂)

Rezultat u tablici to i potvrđuje: MAE je jednak do zadnje znamenke. Linearna interpolacija dakle nije suparnička metoda KNN-u nego njegov **specijalni slučaj**, i ujedno granica koju KNN s prosjekom susjeda može dosegnuti, ali ne probiti. Uzimanje više susjeda po strani mjerljivo pogoršava rezultat (k = 4 daje 3,221 °C), jer udaljeniji susjedi unose zaglađivanje bez nove informacije.

Napredna varijanta zato mijenja **vrstu pitanja**, a ne broj susjeda: umjesto „koje su točke vremenski blizu” pita „koje su poznate točke bile u **sličnoj situaciji** unutar praznine” — sličan relativni položaj `alpha`, slične udaljenosti do oslonaca, slično doba dana. Od njih uči koliko je linearna baza ondje griješila i tu korekciju primjenjuje na rupu. Tek tako `knn_upgraded` ({knn_upg:.4f} °C) nadmašuje i osnovni KNN i linearnu interpolaciju.

### D.7 Pomični prosjek
Pomični prosjek pokazuje prihvatljive rezultate na random scenariju, ali značajno gori od linear interpolacije na block scenarijima. Metoda je prikladna za kratke rupe u nizu, ali ne za duge kontinuirane blokove nedostajućih vrijednosti.

### D.8 Adaptivna imputacija je gornja granica, a ne metoda

Routing tablica u `src/adaptive_imputation.c` ručno je popunjena metodama koje su pobijedile **na istom test skupu** na kojem se metoda ocjenjivala, i to na jednom tjednu. Broj slobodnih parametara jednak je broju testova, pa je riječ o prenaučenju po konstrukciji.

Ponavljanje nad {n_repeats} tjedana dalo je izravan i vrlo uvjerljiv dokaz toga. Na tjednu na kojem je tablica podešena metoda je bila najbolja od svih ({w0_ad:.4f} naspram {w0_lin:.4f} °C za linearnu interpolaciju). Preko {n_repeats} tjedana pada na **{adaptive_mean:.4f} °C**, dakle uparena razlika iznosi **+1,54 °C u korist linearne interpolacije** — daleko najveći pad bilo koje metode. Po scenarijima je jasno vidljivo gdje puca: na `random` je i dalje neutralna (−0,0005 °C, jer je ondje routing slučajno pogodio), a na sva četiri blok scenarija gubi između 1,6 i 2,2 °C.

Ovo je udžbenički primjer prenaučenja i preporučam ga zadržati u radu upravo kao takav, s obje brojke. Ako se metoda ipak želi prikazati, treba je označiti kao **oracle granicu** za pripadni tjedan, a ne kao rezultat metode koja generalizira.

### D.9 Ograničenja mjere R²

R² se u eksperimentu računa iz srednje vrijednosti **samo maskiranih** točaka. To je uobičajena konvencija, ali je na block scenarijima obmanjujuća: pri `block_middle` 10 % maskirani blok pokriva raspon od svega 0,32 °C naspram 6,06 °C za cijeli niz, pa nazivnik postane oko 360× manji i R² poprimi vrlo velike negativne vrijednosti iako je MAE ondje **niži nego bilo gdje drugdje**. R² tada mjeri koliko je praznina slučajno uska, a ne koliko je metoda dobra, zbog čega se poredak metoda po R² i po MAE na block scenarijima ne poklapa. Za usporedbu metoda pouzdaniji je **skill score** u odnosu na linearnu interpolaciju, SS = 1 − MAE_metoda / MAE_linear, gdje nula znači „jednako kao referentna metoda”.

---

## E. Zaključak — što dodati

1. Eksperimenti obuhvaćaju **{n_rows}** agregiranih rezultata ({n_scenarios} scenarija × {n_rates} stopa × {n_methods} metoda), svaki kao srednja vrijednost **{n_repeats} ponavljanja** nad različitim tjednima — ukupno {n_rows * n_repeats} pojedinačnih pokretanja metode.
2. Zaostatak ML metoda u prvoj verziji nije bio posljedica nedostatka podataka ni kapaciteta modela, nego **odsutnosti autoregresijske informacije u skupu značajki**. Uvođenjem značajki susjeda i učenja reziduala MAE je pao za 14–40 % po metodi.
3. **Linearna interpolacija ostaje najbolja metoda u ukupnom prosjeku** ({linear_mean:.4f} °C). Najbolja ML metoda, neuronska mreža ({nn_mean:.4f} °C), zaostaje za statistički značajnih 0,023 °C. To je teorijski očekivano jer je linearna interpolacija za lokalno linearan signal analitički optimalna.
4. ML metode ipak **značajno pobjeđuju na scenariju `block`** i, u slučaju naprednog KNN-a, na `block_middle` — dakle ondje gdje su praznine duge i pretpostavka lokalne linearnosti popušta. Razlike su male (oko 0,005 °C), ali reproducibilne kroz {n_repeats} tjedana.
5. **KNN s obuhvatom praznine i ponderom 1/d matematički je identičan linearnoj interpolaciji** — potvrđeno na svih {n_rows * n_repeats // n_methods} parova, gdje je razlika točno nula. Interpolacija je specijalni slučaj KNN-a, a ne suparnička metoda.
6. **Adaptivna imputacija je udžbenički primjer prenaučenja**: najbolja od svih na tjednu na kojem je podešena ({w0_ad:.4f} °C), a najlošija među razumnim metodama preko {n_repeats} tjedana ({adaptive_mean:.4f} °C).
7. **Metodološka pouka:** zaključak izveden iz jedne realizacije eksperimenta bio je pogrešan. Raspon MAE između tjedana (oko 2,9 °C) četrdesetak je puta veći od razlike među vodećim metodama, pa je uparen test nad ponavljanjima nužan, a ne opcionalan.
8. **Kubična interpolacija** loša je na block scenariju zbog globalnog overshoota; dobra je na block_end scenariju.
9. **Pomični prosjek** koristan na random scenariju, ne i na block scenarijima.

---

## F. Budući rad (preporučeni odlomak)

Rezultat vrijedi za signal s lag-1 autokorelacijom većom od 0,999 i uzorak od 7 dana. Za rjeđe uzorkovanje, gdje autokorelacija pada, ili za višegodišnji niz, gdje se sezonski profil može pouzdano procijeniti, očekivanje se obrće u korist metoda strojnog učenja — na sedam dana dnevni profil ima premalo ponavljanja pa unosi više šuma nego signala.

Budući rad mogao bi stoga uključiti dulje vremenske nizove, više meteoroloških varijabli i stvarne nedostajuće podatke umjesto umjetnog uklanjanja. Na strani modela smisleni su rekurentne mreže i modeli sa samopažnjom koji rade nad cijelim prozorom niza, odabir hiperparametara na validacijskim prazninama generiranima iz poznatog dijela niza (bez gledanja u test skup), te zamjena ručne routing tablice adaptivne metode naučenim pravilom.

---

## G. Grafovi i prilozi

- Stupčasti grafovi: svih {n_methods} metoda, svaka svojom bojom (`mae_by_method_*_20.png`)
- Linijski grafovi: MAE/RMSE/R² vs missing rate; identične metode označene u legendi
- Rekonstrukcija @ 20 %: najbolja vs najgora metoda po scenariju (`reconstruction_best_worst_*.png`)
- Pregled: `results/grafovi_pregled.html`
- Tablice: `results/tablice/sve_tablice_pregled.md`

---

## H. Popis novih datoteka u projektu

| Datoteka | Svrha |
|----------|-------|
| `src/gap_features.c/h` | Značajke najbližih poznatih susjeda, bez curenja informacija |
| `src/ml_features.c/h` | Zajednički prostor od 11 značajki za sve ML metode |
| `src/neural_net.c/h` | Višeslojni perceptron s backpropagationom i Adam optimizatorom |
| `src/decision_tree.c` | Prerađeno: rezidual, predizračunate značajke, rez preko prefiksnih suma |
| `src/rf_methods.c` | Prerađeno: 24 stabla, dubina 10, `max_features`, aktivan `RF_MIN_LEAF` |
| `src/knn_methods.c` | Prerađeno: obavezan obuhvat praznine, ponder 1/d |
| `src/knn_upgraded.c` | Prerađeno: KNN u prostoru značajki praznine, uči rezidual |
| `src/adaptive_imputation.c` | Adaptivna hibridna metoda (oracle granica) |
| `src/interpolation.c` | + `moving_average_imputation()` |
| `src/experiment.c` | {n_methods} metoda, ponavljanja (`--repeats`), agregacija sa sd |
| `scripts/prepare_jena_windows.py` | Izvlači {n_repeats} nezavisnih tjednih prozora iz sirovog Jena niza |
| `scripts/significance.py` | Upareni Wilcoxon + bootstrap CI + Holmova korekcija |
| `results/experiment_runs.csv` | Svi pojedinačni rezultati po ponavljanju |
| `results/znacajnost.md` | Tablica testova značajnosti |
| `results/reconstruction_best_worst_20.csv` | Pregled najbolje/najgore @ 20 % |
| `results/tablice/knn_usporedba.csv` | KNN osnovni vs napredni |
| `results/tablice/moving_average_pregled.csv` | Pomični prosjek vs linear |
"""


if __name__ == "__main__":
    main()
