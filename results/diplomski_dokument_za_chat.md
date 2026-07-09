# Diplomski rad — kompletan dokument za nadopunu
*Generirano iz stvarnog koda i CSV rezultata projekta `diplomski-u-cu`*
*Izvor metrika: `results/experiment_results.csv` (160 redaka)*
*Datum: 2026-07-09*

---

## VAŽNE NAPOMENE PRIJE KORIŠTENJA

1. **Moving average** nije implementiran u projektu.
2. U eksperimentu se koristi **8 metoda**, ne 10. KNN u eksperimentu = `knn_imputation_upgraded` (napredni KNN), registriran kao `knn`.
3. **Osnovni KNN** (`knn_methods.c`) postoji samo u testovima — nema rezultata u CSV-u, usporedba KNN vs Advanced KNN nije moguća.
4. **Linear** i **time** interpolacija daju identične rezultate jer su Jena uzorci ravnomjerno raspoređeni (10-min intervali).
5. **Cubic** i **spline** interpolacija daju identične rezultate (ista jezgra u kodu).
6. Rekonstrukcijski CSV postoji za **linear_interpolation @ 20%** za svih 5 scenarija.

---

# DIO A — TEHNIČKI SAŽETAK IZ KODA

## A.1 Učitavanje podataka
- **`src/dataset.c`** — funkcija `series_load_csv()` učitava CSV i puni strukturu `Series`
- **`src/series.h`** — definicija `Series` (`temp`, `epoch`, `hour`, `yday`)
- **`src/experiment.c`** — funkcija `load_series()` odabire putanju:
  - Jena: `data/processed/jena_temperature_48h.csv` (288 zapisa, 10-min intervali)
  - Demo: `data/raw/temperature_demo_cities.csv`

## A.2 Stvaranje missing vrijednosti i maske
- **`src/preprocessing.c`** / **`src/preprocessing.h`**
  - `create_missing_values()` — random scenarij
  - `create_single_block_missing_values()` — block scenariji (random/start/middle/end pozicija)
  - `create_block_missing_values()` — stari višestruki blok (samo u testovima)
- **`src/experiment.c`** — `exp_create_damage()` povezuje scenarij s funkcijom iz preprocessinga

## A.3 Metode imputacije

| Datoteka | Metode |
|----------|--------|
| `src/interpolation.c` | forward_fill, linear_interpolation, time_interpolation, cubic_interpolation, spline_interpolation |
| `src/knn_upgraded.c` | knn (u eksperimentu: napredni KNN) |
| `src/decision_tree.c` | decision_tree |
| `src/rf_methods.c` | random_forest |
| `src/knn_methods.c` | osnovni KNN — samo u testovima, ne u eksperimentu |

## A.4 Evaluacija MAE, RMSE, R²
- **`src/evaluation.c`** — `evaluate_reconstruction()`
- **`src/evaluation.h`** — struktura `Metrics`
- Evaluacija **samo gdje je `mask[i] == 1`**

## A.5 Generirane CSV datoteke

| Datoteka | Izvor |
|----------|-------|
| `results/experiment_results.csv` | glavna tablica metrika |
| `results/mae_by_method.csv` | MAE po metodi |
| `results/error_vs_missing_rate.csv` | pogreške po rateu |
| `results/reconstruction_{method}_{scenario}_{rate}.csv` | rekonstrukcija po točkama (automatski: linear @ 20%) |
| `results/method_tables/*.csv` | skripta `scripts/generate_method_tables.py` |
| `results/method_tables/sazetak_rekonstrukcija_po_metodi.csv` | sažetak rekonstrukcija |
| `results/grafovi_pregled.html` | vizualni pregled grafova |

## A.6 Stupci u CSV-u s metrikama (`experiment_results.csv`)
`scenario`, `block_position`, `missing_rate`, `method`, `mae`, `rmse`, `r2`, `number_of_missing_values`, `number_of_evaluated_values`

## A.7 Stupci u CSV-u s rekonstrukcijama
`index`, `timestamp`, `original_temperature`, `damaged_temperature`, `reconstructed_temperature`, `mask`, `scenario`, `block_position`, `missing_rate`, `method`

## A.8 Pokretanje cijelog eksperimenta
```
.\diplomski.exe --experiment-all
```
ili
```
.\report.bat
```
(build + eksperiment + grafovi + HTML pregled)

## A.9 Pojedinačni scenariji
```
.\diplomski.exe --experiment-all --scenario random --missing-rate 0.20
.\diplomski.exe --compare --scenario block_middle --missing-rate 0.30
```

## A.10 Razlika scenarija u kodu

| Scenarij | Funkcija | Ponašanje |
|----------|----------|-----------|
| `random` | `create_missing_values()` | nasumične pojedinačne vrijednosti |
| `block` | `create_single_block_missing_values(..., RANDOM)` | jedan blok na nasumičnoj poziciji |
| `block_start` | `create_single_block_missing_values(..., START)` | blok od indeksa 1 |
| `block_middle` | `create_single_block_missing_values(..., MIDDLE)` | blok u sredini niza |
| `block_end` | `create_single_block_missing_values(..., END)` | blok na kraju (završava na n−2) |

Prva i zadnja vrijednost uvijek ostaju poznate. Duljina bloka = `round(missing_rate × n)`.

---

# DIO B — ODGOVORI IZ CSV REZULTATA
*Izvor: `results/experiment_results.csv`, stupci `scenario`, `missing_rate`, `method`, `mae`, `rmse`, `r2`*

## B.1 Random missing — najbolje metode

| Missing rate | Najbolji MAE | Najbolji RMSE | Najbolji R² |
|-------------|--------------|---------------|-------------|
| 10% | cubic_interpolation (0,0406) | cubic_interpolation (0,0503) | cubic_interpolation (0,9993) |
| 20% | cubic_interpolation (0,0488) | cubic_interpolation (0,0672) | cubic_interpolation (0,9987) |
| 30% | cubic_interpolation (0,0448) | cubic_interpolation (0,0606) | cubic_interpolation (0,9991) |
| 40% | linear_interpolation (0,0620) | linear_interpolation (0,0920) | linear_interpolation (0,9980) |

## B.2 Block missing — najbolje metode

| Missing rate | Najbolji MAE | Najbolji RMSE | Najbolji R² |
|-------------|--------------|---------------|-------------|
| 10% | linear_interpolation (0,1214) | linear_interpolation (0,1428) | linear_interpolation (0,4867) |
| 20% | cubic_interpolation (0,1946) | cubic_interpolation (0,2737) | cubic_interpolation (0,9155) |
| 30% | linear_interpolation (0,4406) | cubic_interpolation (0,5492) | cubic_interpolation (0,5995) |
| 40% | linear_interpolation (0,6903) | linear_interpolation (0,9168) | linear_interpolation (0,6616) |

## B.3 Najbolja metoda po poziciji bloka (prema MAE)

| Scenarij | 10% | 20% | 30% | 40% |
|----------|-----|-----|-----|-----|
| block_start | linear_interpolation (0,2212) | forward_fill (0,8097) | cubic_interpolation (0,9713) | linear_interpolation (0,8763) |
| block_middle | decision_tree (0,1081) | forward_fill (0,3384) | linear_interpolation (0,2554) | linear_interpolation (0,2665) |
| block_end | linear_interpolation (0,1970) | linear_interpolation (0,3538) | cubic_interpolation (0,6671) | random_forest (1,0260) |

**Napomena:** Rezultati nisu jednoznačni — najbolja metoda mijenja se po scenariju i rateu.

## B.4 Trendovi (pitanja 10–12)

**MAE raste s missing rateom:**
- random scenarij, prosjek svih metoda: 0,079 (10%) → 0,118 (40%)
- block_start: 0,896 → 1,808
- block: 0,539 → 1,559

**RMSE raste** — prosjek svih metoda i scenarija: 0,550 (10%) → 1,452 (40%)

**R² opada** — prosjek svih metoda: −11,79 (10%) → −3,53 (40%) na razini svih scenarija zajedno, jer block scenariji imaju mnogo negativnih R² (KNN, forward fill). Na random scenariju R² ostaje blizu 1,0.

## B.5 Scenariji (pitanja 13–14)
- **Najteži:** `block_start` — prosječni MAE svih metoda = **1,401**
- **Najlakši:** `random` — prosječni MAE = **0,095**

## B.6 Metode (pitanja 15–20)

**15. Najstabilnija metoda** (najmanja std. dev. MAE): **linear_interpolation** i **time_interpolation** (σ = 0,410)

**16. Najveće pogreške na block scenarijima:** **knn**
- block @ 10%: MAE = 2,058
- block_start @ 20%: MAE = 4,013
- block @ 40%: MAE = 3,447

**17. Klasične metode bolje?** Da, u svim scenarijima:
- random: klasične avg MAE 0,061 vs ML 0,152
- block: 0,616 vs 1,795
- block_start: 1,010 vs 2,053
- block_middle: 0,548 vs 1,195
- block_end: 0,876 vs 1,208

**18. ML bolje u nekim scenarijima?** Da, ali rijetko:
- block_middle @ 10%: decision_tree (0,108) bolji od linear (0,167)
- block_end @ 40%: random_forest (1,026) bolji od linear (1,248)
- block_start: random_forest bolji od decision_tree u prosjeku

**19. Advanced KNN vs obični KNN?** Usporedba **nije moguća iz CSV-a**. U eksperimentu se koristi samo `knn` (= `knn_imputation_upgraded`). Osnovni KNN nema rezultate u `experiment_results.csv`.

**20. Random Forest stabilniji od Decision Tree?** Djelomično da:
- std. dev. MAE: RF = 0,490, DT = 0,619
- RF bolji u prosjeku na block_start
- DT bolji na random, block, block_middle, block_end
- Nije jednoznačno

**Pobjede po MAE** (najbolja metoda po scenariju/rateu): linear_interpolation 10×, cubic_interpolation 6×, forward_fill 2×, random_forest 1×, decision_tree 1×

---

# DIO C — TABLICE ZA DIPLOMSKI RAD

## TABLICA 1: Najbolja metoda po scenariju i missing rateu
*Izvor: `experiment_results.csv`, min(`mae`)*

| scenario | block_position | missing_rate | najbolja metoda po MAE | MAE | RMSE | R² |
|----------|----------------|--------------|------------------------|-----|------|-----|
| random | none | 0.10 | cubic_interpolation | 0.0406 | 0.0503 | 0.9993 |
| random | none | 0.20 | cubic_interpolation | 0.0488 | 0.0672 | 0.9987 |
| random | none | 0.30 | cubic_interpolation | 0.0448 | 0.0606 | 0.9991 |
| random | none | 0.40 | linear_interpolation | 0.0620 | 0.0920 | 0.9980 |
| block | none | 0.10 | linear_interpolation | 0.1214 | 0.1428 | 0.4867 |
| block | none | 0.20 | cubic_interpolation | 0.1946 | 0.2737 | 0.9155 |
| block | none | 0.30 | linear_interpolation | 0.4406 | 0.5602 | 0.5833 |
| block | none | 0.40 | linear_interpolation | 0.6903 | 0.9168 | 0.6616 |
| block_start | start | 0.10 | linear_interpolation | 0.2212 | 0.2870 | 0.6913 |
| block_start | start | 0.20 | forward_fill | 0.8097 | 0.9592 | −0.7258 |
| block_start | start | 0.30 | cubic_interpolation | 0.9713 | 1.1943 | −0.0214 |
| block_start | start | 0.40 | linear_interpolation | 0.8763 | 1.1887 | 0.4144 |
| block_middle | middle | 0.10 | decision_tree | 0.1081 | 0.1322 | 0.1342 |
| block_middle | middle | 0.20 | forward_fill | 0.3384 | 0.4030 | −1.8616 |
| block_middle | middle | 0.30 | linear_interpolation | 0.2554 | 0.3052 | 0.1034 |
| block_middle | middle | 0.40 | linear_interpolation | 0.2665 | 0.3092 | 0.4961 |
| block_end | end | 0.10 | linear_interpolation | 0.1970 | 0.2523 | 0.7258 |
| block_end | end | 0.20 | linear_interpolation | 0.3538 | 0.3940 | 0.6565 |
| block_end | end | 0.30 | cubic_interpolation | 0.6671 | 0.7697 | −0.4063 |
| block_end | end | 0.40 | random_forest | 1.0260 | 1.2487 | −1.7082 |

---

## TABLICA 2: Random missing rezultati
*Izvor: `experiment_results.csv`, `scenario = random`*

| missing_rate | method | MAE | RMSE | R² |
|-------------|--------|-----|------|-----|
| 0.10 | cubic_interpolation | 0.0406 | 0.0503 | 0.9993 |
| 0.10 | spline_interpolation | 0.0406 | 0.0503 | 0.9993 |
| 0.10 | linear_interpolation | 0.0471 | 0.0588 | 0.9990 |
| 0.10 | time_interpolation | 0.0471 | 0.0588 | 0.9990 |
| 0.10 | forward_fill | 0.0521 | 0.0726 | 0.9985 |
| 0.10 | knn | 0.0865 | 0.1110 | 0.9965 |
| 0.10 | decision_tree | 0.1568 | 0.1939 | 0.9893 |
| 0.10 | random_forest | 0.1618 | 0.2204 | 0.9862 |
| 0.20 | cubic_interpolation | 0.0488 | 0.0672 | 0.9987 |
| 0.20 | spline_interpolation | 0.0488 | 0.0672 | 0.9987 |
| 0.20 | linear_interpolation | 0.0502 | 0.0680 | 0.9986 |
| 0.20 | time_interpolation | 0.0502 | 0.0680 | 0.9986 |
| 0.20 | forward_fill | 0.0741 | 0.1077 | 0.9966 |
| 0.20 | knn | 0.0841 | 0.1068 | 0.9966 |
| 0.20 | decision_tree | 0.1662 | 0.2198 | 0.9858 |
| 0.20 | random_forest | 0.1903 | 0.2719 | 0.9782 |
| 0.30 | cubic_interpolation | 0.0448 | 0.0606 | 0.9991 |
| 0.30 | spline_interpolation | 0.0448 | 0.0606 | 0.9991 |
| 0.30 | linear_interpolation | 0.0502 | 0.0662 | 0.9989 |
| 0.30 | time_interpolation | 0.0502 | 0.0662 | 0.9989 |
| 0.30 | forward_fill | 0.1012 | 0.1588 | 0.9936 |
| 0.30 | knn | 0.1016 | 0.1422 | 0.9949 |
| 0.30 | decision_tree | 0.1633 | 0.2275 | 0.9869 |
| 0.30 | random_forest | 0.1952 | 0.2728 | 0.9812 |
| 0.40 | linear_interpolation | 0.0620 | 0.0920 | 0.9980 |
| 0.40 | time_interpolation | 0.0620 | 0.0920 | 0.9980 |
| 0.40 | cubic_interpolation | 0.0849 | 0.1421 | 0.9953 |
| 0.40 | spline_interpolation | 0.0849 | 0.1421 | 0.9953 |
| 0.40 | knn | 0.1304 | 0.1880 | 0.9917 |
| 0.40 | forward_fill | 0.1366 | 0.2002 | 0.9906 |
| 0.40 | decision_tree | 0.1693 | 0.2320 | 0.9874 |
| 0.40 | random_forest | 0.2136 | 0.2921 | 0.9801 |

---

## TABLICA 3: Block missing rezultati
*Izvor: `experiment_results.csv`, `scenario = block`*

| missing_rate | method | MAE | RMSE | R² |
|-------------|--------|-----|------|-----|
| 0.10 | linear_interpolation | 0.1214 | 0.1428 | 0.4867 |
| 0.10 | time_interpolation | 0.1214 | 0.1428 | 0.4867 |
| 0.10 | decision_tree | 0.3173 | 0.3664 | −2.3806 |
| 0.10 | cubic_interpolation | 0.3391 | 0.3654 | −2.3624 |
| 0.10 | spline_interpolation | 0.3391 | 0.3654 | −2.3624 |
| 0.10 | forward_fill | 0.4883 | 0.5274 | −6.0048 |
| 0.10 | random_forest | 0.5252 | 0.5617 | −6.9477 |
| 0.10 | knn | 2.0580 | 2.2816 | −130.1117 |
| 0.20 | cubic_interpolation | 0.1946 | 0.2737 | 0.9155 |
| 0.20 | spline_interpolation | 0.1946 | 0.2737 | 0.9155 |
| 0.20 | linear_interpolation | 0.2849 | 0.3440 | 0.8666 |
| 0.20 | time_interpolation | 0.2849 | 0.3440 | 0.8666 |
| 0.20 | decision_tree | 1.2948 | 1.6011 | −1.8901 |
| 0.20 | random_forest | 1.9376 | 2.1544 | −4.2328 |
| 0.20 | forward_fill | 1.7912 | 2.0237 | −3.6173 |
| 0.20 | knn | 3.1533 | 3.2768 | −11.1059 |
| 0.30 | linear_interpolation | 0.4406 | 0.5602 | 0.5833 |
| 0.30 | time_interpolation | 0.4406 | 0.5602 | 0.5833 |
| 0.30 | cubic_interpolation | 0.4890 | 0.5492 | 0.5995 |
| 0.30 | spline_interpolation | 0.4890 | 0.5492 | 0.5995 |
| 0.30 | decision_tree | 0.7618 | 1.0070 | −0.3465 |
| 0.30 | random_forest | 0.9100 | 1.1784 | −0.8439 |
| 0.30 | forward_fill | 0.9838 | 1.2559 | −1.0942 |
| 0.30 | knn | 3.4313 | 3.6477 | −16.6670 |
| 0.40 | linear_interpolation | 0.6903 | 0.9168 | 0.6616 |
| 0.40 | time_interpolation | 0.6903 | 0.9168 | 0.6616 |
| 0.40 | random_forest | 1.3887 | 1.5848 | −0.0113 |
| 0.40 | cubic_interpolation | 1.1448 | 1.3846 | 0.2281 |
| 0.40 | spline_interpolation | 1.1448 | 1.3846 | 0.2281 |
| 0.40 | decision_tree | 2.3168 | 2.8002 | −2.1573 |
| 0.40 | forward_fill | 1.6503 | 2.0226 | −0.6472 |
| 0.40 | knn | 3.4468 | 3.6493 | −4.3622 |

---

## TABLICA 4: Block position rezultati — sažetak najboljih po MAE
*Izvor: `experiment_results.csv`, scenariji block_start, block_middle, block_end*
*(Puna tablica: 96 redaka — izvezi iz CSV-a)*

| block_position | missing_rate | najbolja metoda | MAE | RMSE | R² |
|----------------|--------------|-----------------|-----|------|-----|
| start | 0.10 | linear_interpolation | 0.2212 | 0.2870 | 0.6913 |
| start | 0.20 | forward_fill | 0.8097 | 0.9592 | −0.7258 |
| start | 0.30 | cubic_interpolation | 0.9713 | 1.1943 | −0.0214 |
| start | 0.40 | linear_interpolation | 0.8763 | 1.1887 | 0.4144 |
| middle | 0.10 | decision_tree | 0.1081 | 0.1322 | 0.1342 |
| middle | 0.20 | forward_fill | 0.3384 | 0.4030 | −1.8616 |
| middle | 0.30 | linear_interpolation | 0.2554 | 0.3052 | 0.1034 |
| middle | 0.40 | linear_interpolation | 0.2665 | 0.3092 | 0.4961 |
| end | 0.10 | linear_interpolation | 0.1970 | 0.2523 | 0.7258 |
| end | 0.20 | linear_interpolation | 0.3538 | 0.3940 | 0.6565 |
| end | 0.30 | cubic_interpolation | 0.6671 | 0.7697 | −0.4063 |
| end | 0.40 | random_forest | 1.0260 | 1.2487 | −1.7082 |

---

## TABLICA 5: Sažetak po metodama
*Izvor: `experiment_results.csv`, prosjek kroz svih 20 kombinacija (5 scenarija × 4 ratea)*

| method | prosječni MAE | prosječni RMSE | prosječni R² | komentar stabilnosti |
|--------|---------------|----------------|--------------|----------------------|
| linear_interpolation | 0.4498 | 0.5477 | −0.0851 | Najstabilnija; najčešće najbolja (10 pobjeda po MAE) |
| time_interpolation | 0.4498 | 0.5477 | −0.0851 | Identična linear — ravnomjeran vremenski interval |
| cubic_interpolation | 0.7259 | 0.8377 | −3.2201 | Odlična na random; nestabilna na block scenarijima |
| spline_interpolation | 0.7259 | 0.8377 | −3.2201 | Ista jezgra kao cubic |
| forward_fill | 0.7590 | 0.8961 | −1.8598 | Loša na block scenarijima |
| random_forest | 0.8209 | 0.9531 | −2.2303 | Manja varijabilnost od DT (σ MAE = 0,490) |
| decision_tree | 0.8269 | 1.0011 | −1.8621 | Povremeno dobra (block_middle 10%) |
| knn | 2.1937 | 2.4558 | −42.9806 | Najveće pogreške na block scenarijima |

---

# DIO D — TEKST ZA DIPLOMSKI RAD

## 3.12.1 Scenariji nedostajućih vrijednosti

U eksperimentu korišteno je pet scenarija umjetnog uklanjanja temperaturnih vrijednosti. Scenarij **random** simulira pojedinačne nasumične nedostatke u nizu. Funkcija `create_missing_values()` nasumično odabire pozicije za uklanjanje, uz očuvanje prve i zadnje vrijednosti.

Scenarij **block** uklanja jedan kontinuirani blok nasumične duljine i pozicije. Scenariji **block_start**, **block_middle** i **block_end** uklanjaju blok fiksne duljine na početku, u sredini odnosno na kraju niza. Duljina bloka izračunava se kao `round(missing_rate × n)`.

Svi scenariji koriste istu masku: vrijednost 1 označava umjetno uklonjeno mjesto. Evaluacija se provodi isključivo na tim pozicijama.

## 3.12.2 Različite razine nedostajućih vrijednosti

Testirani su missing rateovi od **10 %, 20 %, 30 % i 40 %**. Manji postotak ostavlja više poznatih vrijednosti i olakšava rekonstrukciju. Veći postotak smanjuje broj poznatih uzoraka i povećava težinu problema.

Na Jena skupu od 288 zapisa to znači 29, 58, 86 odnosno 115 uklonjenih vrijednosti (stupac `number_of_missing_values` u CSV-u).

## 3.12.4 Struktura rezultata u CSV datotekama

Glavna datoteka **`experiment_results.csv`** sadrži stupce: `scenario`, `block_position`, `missing_rate`, `method`, `mae`, `rmse`, `r2`, `number_of_missing_values`, `number_of_evaluated_values`.

Datoteka **`reconstruction_{method}_{scenario}_{rate}.csv`** sadrži rekonstrukciju po svakoj točki: `index`, `timestamp`, `original_temperature`, `damaged_temperature`, `reconstructed_temperature`, `mask`, `scenario`, `block_position`, `missing_rate`, `method`.

Pomoćne datoteke `mae_by_method.csv` i `error_vs_missing_rate.csv` sadrže iste metrike u drugačijem formatu za analizu.

Grafovi se spremaju u mapu `slike i videa/2026/diplomski-grafovi/` kao PNG datoteke. Vizualni pregled svih grafova dostupan je u `results/grafovi_pregled.html`.

---

## 5 REZULTATI

Poglavlje prikazuje rezultate imputacije temperaturnog niza iz Jena Climate dataseta (288 zapisa, 10-minutni intervali). Uspoređeno je osam metoda na pet scenarija i četiri razine missing ratea. Kvaliteta rekonstrukcije mjerena je MAE, RMSE i R² isključivo na maskiranim pozicijama.

### 5.1 Rezultati za random missing scenarij

Na random scenariju klasične interpolacijske metode postižu najniže pogreške. Pri 10 %, 20 % i 30 % najbolja je **cubic_interpolation** (MAE = 0,0406; 0,0488; 0,0448). Pri 40 % najbolja je **linear_interpolation** (MAE = 0,0620, R² = 0,9980).

KNN postiže MAE od 0,086 do 0,130, dok ML metode imaju MAE 0,157–0,214. Random scenarij je ukupno najlakši: prosječni MAE svih metoda je 0,095, u usporedbi s 1,058 na block scenariju.

### 5.2 Rezultati za block missing scenarij

Block scenarij znatno je teži. Pri 10 % najbolja je **linear_interpolation** (MAE = 0,1214). Pri 20 % **cubic_interpolation** (MAE = 0,1946, R² = 0,9155). Pri 30 % i 40 % ponovno vodi **linear_interpolation** (MAE = 0,4406 i 0,6903).

KNN na block scenariju ima MAE od 2,06 do 3,45, što je višestruko lošije od klasičnih metoda. Forward fill također pokazuje velike pogreške (MAE do 1,79 pri 20 %) jer popunjava blok zadnjom poznatom vrijednošću.

### 5.3 Rezultati za block_start, block_middle i block_end

**block_start** je najteži scenarij (prosječni MAE = 1,401). Linear interpolacija je najbolja pri 10 % i 40 %, ali forward fill „pobjeđuje" pri 20 % s MAE = 0,8097 — uz negativan R² (−0,7258), što ukazuje na lošu kvalitetu modela.

**block_middle** pokazuje da decision tree može biti najbolji pri 10 % (MAE = 0,1081), ali linear interpolacija dominira pri 30 % i 40 %.

**block_end** je sličan block_middle, s linear interpolacijom kao najboljom pri 10 % i 20 %. Pri 40 % random forest ima najmanji MAE (1,0260), ali i negativan R² (−1,7082).

Rezultati po poziciji bloka **nisu jednoznačni** — nema jedne metode koja je uvijek najbolja.

### 5.4 Utjecaj missing ratea na pogrešku

S porastom missing ratea s 10 % na 40 % MAE u prosjeku raste za sve scenarije. Na random scenariju prosječni MAE svih metoda raste s 0,079 na 0,118. RMSE u prosjeku (svi scenariji) raste s 0,550 na 1,452.

R² na random scenariju ostaje blizu 1,0 za klasične metode. Na block scenarijima mnoge metode imaju negativan R², posebno KNN, što znači da su lošije od predviđanja srednjom vrijednošću.

### 5.5 Vizualna rekonstrukcija vremenskog niza

CSV rekonstrukcije (`reconstruction_linear_interpolation_*_0.20.csv`) sadrže originalni, oštećeni i rekonstruirani niz. Za grafove se preporučuje prikazati:
- **linear_interpolation** — najčešće najbolja metoda (10 pobjeda po MAE)
- **cubic_interpolation** — najbolja na random scenariju
- **knn** — za usporedbu lošijeg ponašanja na block scenariju

Crvene točke označavaju maskirane pozicije. Datoteke postoje za svih 5 scenarija pri 20 % missing ratea. Grafovi su dostupni u `slike i videa/2026/diplomski-grafovi/`.

### 5.6 Najbolja metoda po scenariju

Prema Tablici 1, **linear_interpolation** je najbolja u 10 od 20 kombinacija scenarij/rate. **cubic_interpolation** pobjeđuje u 6 slučajeva, uglavnom na random scenariju. Nema jedne univerzalno najbolje metode — izbor ovisi o scenariju i missing rateu.

---

## 6 RASPRAVA

Rasprava povezuje numeričke rezultate s matematičkim ponašanjem metoda na vremenskom nizu temperature.

### 6.1 Usporedba klasičnih i metoda strojnog učenja

Klasične metode imaju niži prosječni MAE u svim scenarijima (random: 0,061 vs 0,152; block: 0,616 vs 1,795). ML metode nisu nadmašile klasične na ovom skupu od 288 uzoraka. Iznimka je block_middle pri 10 %, gdje decision tree postiže MAE = 0,1081.

### 6.2 Ponašanje metoda kod random missing scenarija

Klasične metode dobro iskorištavaju susjedne poznate vrijednosti. Cubic i spline interpolacija postižu MAE ispod 0,05 °C jer su rupe rijetke i okružene poznatim točkama. KNN i stabla ne pokazuju prednost jer imaju premalo podataka za pouzdan model.

### 6.3 Ponašanje metoda kod block missing scenarija

Kontinuirani blok bez unutarnjih poznatih vrijednosti zahtijeva ekstrapolaciju iz rubova. Linear interpolacija izravno spaja poznate vrijednosti lijevo i desno od bloka. Forward fill i KNN značajno gore. KNN ne koristi lokalnu vremensku strukturu dovoljno dobro za dugačke blokove.

### 6.4 Ponašanje metoda kod block_start, block_middle i block_end

Metode koje trebaju poznate vrijednosti s obje strane praznine (linear, cubic) bolje rade kad blok nije na rubu. **block_start** je najteži jer blok počinje odmah nakon prve poznate točke — ostaje samo jedan rubni oslonac s desne strane. **block_end** ima sličan problem s jednim osloncem s lijeve strane.

### 6.5 Prednosti i ograničenja KNN metode

U eksperimentu je implementiran napredni KNN (`knn_imputation_upgraded`) registriran kao `knn`. Koristi cikličke značajke sata i dana u godini. Prednost je prilagodba sezonskim obrascima. Ograničenje: na block scenarijima MAE prelazi 2 °C, jer metoda ne rekonstruira lokalni trend kroz blok.

Usporedba osnovnog i naprednog KNN-a **nije moguća** — osnovni KNN nije uključen u eksperiment.

### 6.6 Prednosti i ograničenja Decision Tree i Random Forest

Decision tree uči nelinearne obrasce iz poznatih vrijednosti. Random forest usrednjava predikcije više stabala i ima manju varijabilnost (σ MAE = 0,490 vs 0,619). RF je bolji na block_start u prosjeku, DT na random i block_middle. Nijedna ML metoda nije dominantna.

### 6.7 Ograničenja rada

- Korišten je jedan temperaturni niz (Jena, 48 h, 288 zapisa)
- Nedostajuće vrijednosti su umjetno generirane, ne stvarne
- Testirana je samo temperatura, ne drugi meteorološki parametri
- Implementacija je u programskom jeziku C, bez vanjskih biblioteka
- Moving average nije implementiran; osnovni KNN nije uključen u eksperiment
- Rezultati ovise o odabranim scenarijima, missing rateovima i značajkama ML metoda
- Rekonstrukcijski CSV postoji samo za linear_interpolation pri 20 %

---

## 7 ZAKLJUČAK

U radu je implementiran i testiran sustav za imputaciju nedostajućih temperaturnih vrijednosti na Jena Climate datasetu. Uspoređeno je osam metoda — pet klasičnih interpolacijskih, KNN (napredna verzija), decision tree i random forest — na pet scenarija (random, block, block_start, block_middle, block_end) i četiri razine missing ratea (10–40 %).

Evaluacija na maskiranim pozicijama pokazuje da je **random scenarij znatno lakši** od block scenarija. Klasične metode, posebno **linear interpolacija** i **cubic interpolacija**, postižu najniže MAE. Linear interpolacija je najbolja u 10 od 20 kombinacija scenarij/rate. KNN pokazuje najveće pogreške na block scenarijima (MAE do 4,01 °C).

S porastom missing ratea pogreška raste, ali na random scenariju klasične metode zadržavaju R² blizu 1,0. Na block scenarijima rezultati su manje stabilni i ovisni o poziciji bloka.

Za praktičnu primjenu na sličnim vremenskim nizovima preporučuje se **linearna interpolacija** kao robustan izbor, uz **cubic interpolaciju** za random missing. Izbor metode treba prilagoditi obliku nedostajućih podataka.

Budući rad mogao bi uključiti više skupova podataka, stvarne missing podatke, implementaciju moving average i usporedbu osnovnog i naprednog KNN-a u istom eksperimentalnom okviru.

---

# DIO E — POPIS GRAFOVA

| Datoteka | Opis |
|----------|------|
| `mae_by_method_random_20.png` | MAE po metodama, random 20% |
| `mae_by_method_block_20.png` | MAE po metodama, block 20% |
| `mae_by_method_block_start_20.png` | MAE po metodama, block_start 20% |
| `mae_by_method_block_middle_20.png` | MAE po metodama, block_middle 20% |
| `mae_by_method_block_end_20.png` | MAE po metodama, block_end 20% |
| `mae_vs_rate_random.png` | MAE vs missing rate, random |
| `mae_vs_rate_block.png` | MAE vs missing rate, block |
| `mae_vs_rate_block_start.png` | MAE vs missing rate, block_start |
| `mae_vs_rate_block_middle.png` | MAE vs missing rate, block_middle |
| `mae_vs_rate_block_end.png` | MAE vs missing rate, block_end |
| `reconstruction_linear_random_0.20.png` | Original vs rekonstruirano, random |
| `reconstruction_linear_block_0.20.png` | Original vs rekonstruirano, block |
| `reconstruction_linear_block_start_0.20.png` | Original vs rekonstruirano, block_start |
| `reconstruction_linear_block_middle_0.20.png` | Original vs rekonstruirano, block_middle |
| `reconstruction_linear_block_end_0.20.png` | Original vs rekonstruirano, block_end |

Svi grafovi: `slike i videa/2026/diplomski-grafovi/`
HTML pregled: `results/grafovi_pregled.html`

---

*Kraj dokumenta*
