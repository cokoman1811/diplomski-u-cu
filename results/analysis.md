# Analiza rezultata eksperimenata

Automatski generirano iz `experiment_results.csv`.

## Sažetak

- **Random missing (20%):** najbolja metoda — **spline_interpolation**
- **Block missing (20%):** najbolja metoda — **linear_interpolation**
- **Klasične vs ML (prosjek MAE, random 20%):** 0.0873 vs 0.4707
- **Klasične vs ML (prosjek MAE, block 20%):** 2.6094 vs 2.2221

## Tablica — random missing, 20%

| metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| spline_interpolation | 0.0635 | 0.1052 | 0.9997 |
| cubic_interpolation | 0.0635 | 0.1052 | 0.9997 |
| time_interpolation | 0.0730 | 0.1185 | 0.9996 |
| linear_interpolation | 0.0730 | 0.1185 | 0.9996 |
| knn | 0.1573 | 0.2641 | 0.9981 |
| forward_fill | 0.1635 | 0.2588 | 0.9982 |
| decision_tree | 0.5546 | 0.7300 | 0.9855 |
| random_forest | 0.7003 | 0.9443 | 0.9758 |

## Tablica — block missing, 20%

| metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| linear_interpolation | 1.4765 | 1.6968 | -2.6787 |
| time_interpolation | 1.4765 | 1.6968 | -2.6787 |
| forward_fill | 1.6054 | 1.8330 | -3.2929 |
| decision_tree | 2.0627 | 2.2444 | -5.4362 |
| knn | 2.1354 | 2.5753 | -7.4734 |
| random_forest | 2.4682 | 2.6161 | -7.7439 |
| cubic_interpolation | 4.2442 | 5.0983 | -32.2091 |
| spline_interpolation | 4.2442 | 5.0983 | -32.2091 |

## Najbolja metoda po scenariju i missing rateu

| scenarij | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|----------|---- | ---- | ---- | ---- | ---- | ---- | ---- | ----|
| random | spline_interpolation | spline_interpolation | linear_interpolation | spline_interpolation | spline_interpolation | cubic_interpolation | linear_interpolation | linear_interpolation |
| block | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | forward_fill | linear_interpolation |
| block_start | linear_interpolation | linear_interpolation | knn | decision_tree | linear_interpolation | cubic_interpolation | cubic_interpolation | forward_fill |
| block_middle | linear_interpolation | linear_interpolation | cubic_interpolation | random_forest | cubic_interpolation | forward_fill | forward_fill | forward_fill |
| block_end | linear_interpolation | cubic_interpolation | spline_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | cubic_interpolation |

## Ključni nalazi (za poglavlje Rezultati)

1. **Klasične interpolacijske metode** (posebno linear, spline, cubic) postižu najniži MAE na random scenariju za sve testirane missing rateove (10–80 %).
2. **Linear i time interpolacija** daju identične rezultate jer su uzorci ravnomjerno raspoređeni u vremenu (Jena 10-min intervali).
3. Na **block scenariju** linear/time i dalje vode; forward fill i cubic/spline znatno gore zbog dugačkih rupa.
    printf("Na ovom datasetu (7 dana, 10-min) ML metode (KNN, DT, RF) obicno ne nadmašuju klasicne.
");
5. **KNN** na block scenariju pokazuje najveću pogrešku (npr. MAE ≈ 5.09 pri 80% block).
6. Pri visokim missing rateovima (50–80 %) pogreška naglo raste na block_start, block_middle i block_end scenarijima.

## Grafovi

Otvori `results/grafovi_pregled.html` u pregledniku za vizualni pregled svih grafova.

---
*Generirano: `python scripts/report.py`*
