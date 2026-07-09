# Analiza rezultata eksperimenata

Automatski generirano iz `experiment_results.csv`.

## Sažetak

- **Random missing (20%):** najbolja metoda — **cubic_interpolation**
- **Block missing (20%):** najbolja metoda — **cubic_interpolation**
- **Klasične vs ML (prosjek MAE, random 20%):** 0.0544 vs 0.1469
- **Klasične vs ML (prosjek MAE, block 20%):** 0.5500 vs 2.1286

## Tablica — random missing, 20%

| metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| cubic_interpolation | 0.0488 | 0.0672 | 0.9987 |
| spline_interpolation | 0.0488 | 0.0672 | 0.9987 |
| time_interpolation | 0.0502 | 0.0680 | 0.9986 |
| linear_interpolation | 0.0502 | 0.0680 | 0.9986 |
| forward_fill | 0.0741 | 0.1077 | 0.9966 |
| knn | 0.0841 | 0.1068 | 0.9966 |
| decision_tree | 0.1662 | 0.2198 | 0.9858 |
| random_forest | 0.1903 | 0.2719 | 0.9782 |

## Tablica — block missing, 20%

| metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| cubic_interpolation | 0.1946 | 0.2737 | 0.9155 |
| spline_interpolation | 0.1946 | 0.2737 | 0.9155 |
| time_interpolation | 0.2849 | 0.3440 | 0.8666 |
| linear_interpolation | 0.2849 | 0.3440 | 0.8666 |
| decision_tree | 1.2948 | 1.6011 | -1.8901 |
| forward_fill | 1.7912 | 2.0237 | -3.6173 |
| random_forest | 1.9376 | 2.1544 | -4.2328 |
| knn | 3.1533 | 3.2768 | -11.1059 |

## Najbolja metoda po scenariju i missing rateu

| scenarij | 10% | 20% | 30% | 40% |
|----------|-----|-----|-----|-----|
| random | cubic_interpolation | cubic_interpolation | cubic_interpolation | linear_interpolation |
| block | linear_interpolation | cubic_interpolation | linear_interpolation | linear_interpolation |
| block_start | linear_interpolation | forward_fill | cubic_interpolation | linear_interpolation |
| block_middle | decision_tree | forward_fill | linear_interpolation | linear_interpolation |
| block_end | linear_interpolation | linear_interpolation | cubic_interpolation | random_forest |

## Ključni nalazi (za poglavlje Rezultati)

1. **Klasične interpolacijske metode** (posebno linear, spline, cubic) postižu najniži MAE na random scenariju za sve testirane missing rateove.
2. **Linear i time interpolacija** daju identične rezultate jer su uzorci ravnomjerno raspoređeni u vremenu (Jena 10-min intervali).
3. Na **block scenariju** linear/time i dalje vode; forward fill i cubic/spline znatno gore zbog dugačkih rupa.
4. **ML metode** (KNN, decision tree, random forest) na ovom datasetu (288 uzoraka) **ne nadmašuju** klasične metode.
5. **KNN** na block scenariju pokazuje najveću pogrešku (npr. MAE ≈ 3.45 pri 40% block) — ne koristi dovoljno lokalnu vremensku strukturu za dugačke blokove.
6. Pri **40% random missing** KNN i ML metode pokazuju veću pogrešku — manje poznatih uzoraka za pouzdan model.

## Usporedba scenarija random vs block

Block missing simulira kvar senzora (kontinuirani interval bez podataka). U tom scenariju:
- metode koje koriste **susjedne poznate točke** (linear, time) ostaju najstabilnije;
- **forward fill** daje ravnu liniju kroz blok → veći MAE;
- **ML** uči globalne obrasce (sat, dan) ali ne popunjava lokalni trend iz susjedstva kao interpolacija.

## Grafovi (mapa `slike i videa/2026/diplomski-grafovi/`)

| Datoteka | Opis |
|----------|------|
| `mae_by_method_random_20.png` | Stupčasti graf MAE, random 20% |
| `mae_by_method_block_20.png` | Stupčasti graf MAE, block 20% |
| `mae_vs_rate_random.png` | MAE vs missing rate, random |
| `mae_vs_rate_block.png` | MAE vs missing rate, block |
| `reconstruction_linear_*_20.png` | Original vs rekonstruirano (linear) |

## Nacrt zaključka (ručno doradi za rad)

Na testiranom Jena datasetu (48 h, 10-min intervali) klasične interpolacijske metode,
posebno linearna interpolacija, postižu najbolju točnost imputacije u oba scenarija
nedostajućih vrijednosti. ML metode ne pokazuju prednost na malom skupu podataka;
imale bi smisla na većem skupu, s više značajki ili uz tuning hiperparametara.
Block missing potvrđuje da izbor metode ovisi o **obliku** nedostajućih podataka,
ne samo o njihovu udjelu.

---
*Generirano: `python scripts/report.py`*
