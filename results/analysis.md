# Analiza rezultata eksperimenata

Automatski generirano iz `experiment_results.csv`.

## Sažetak

- **Random missing (20%):** najbolja metoda — **spline_interpolation**
- **Block missing (20%):** najbolja metoda — **neural_net**
- **Klasične vs ML (prosjek MAE, random 20%):** 0.1218 vs 0.0931
- **Klasične vs ML (prosjek MAE, block 20%):** 4.1674 vs 2.5459

## Tablica — random missing, 20%

| metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| spline_interpolation | 0.0821 | 0.1321 | 0.9985 |
| adaptive_imputation | 0.0821 | 0.1321 | 0.9985 |
| cubic_interpolation | 0.0821 | 0.1322 | 0.9985 |
| time_interpolation | 0.0887 | 0.1382 | 0.9984 |
| knn | 0.0887 | 0.1382 | 0.9984 |
| linear_interpolation | 0.0887 | 0.1382 | 0.9984 |
| random_forest | 0.0892 | 0.1378 | 0.9984 |
| decision_tree | 0.0974 | 0.1517 | 0.9981 |
| knn_upgraded | 0.0993 | 0.1508 | 0.9981 |
| neural_net | 0.1019 | 0.1573 | 0.9980 |
| forward_fill | 0.1903 | 0.2808 | 0.9936 |
| moving_average | 0.1990 | 0.2889 | 0.9932 |

## Tablica — block missing, 20%

| metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| neural_net | 2.5198 | 3.1131 | -0.3658 |
| knn_upgraded | 2.5281 | 3.1140 | -0.3600 |
| random_forest | 2.5299 | 3.1174 | -0.3611 |
| linear_interpolation | 2.5336 | 3.1165 | -0.3624 |
| knn | 2.5336 | 3.1165 | -0.3624 |
| time_interpolation | 2.5336 | 3.1165 | -0.3624 |
| decision_tree | 2.5355 | 3.1254 | -0.3672 |
| adaptive_imputation | 2.6286 | 3.2177 | -0.4873 |
| moving_average | 3.1532 | 3.8480 | -1.1418 |
| forward_fill | 3.2575 | 3.9366 | -1.2617 |
| cubic_interpolation | 6.7633 | 8.0402 | -11.9963 |
| spline_interpolation | 6.7633 | 8.0402 | -11.9963 |

## Najbolja metoda po scenariju i missing rateu

| scenarij | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|----------|---- | ---- | ---- | ---- | ---- | ---- | ---- | ----|
| random | spline_interpolation | spline_interpolation | cubic_interpolation | cubic_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation |
| block | neural_net | neural_net | neural_net | random_forest | random_forest | neural_net | decision_tree | decision_tree |
| block_start | cubic_interpolation | knn_upgraded | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation |
| block_middle | knn_upgraded | neural_net | decision_tree | neural_net | knn_upgraded | linear_interpolation | knn_upgraded | decision_tree |
| block_end | knn_upgraded | knn_upgraded | linear_interpolation | linear_interpolation | knn_upgraded | knn_upgraded | linear_interpolation | linear_interpolation |

## Ključni nalazi (za poglavlje Rezultati)

1. **Klasične interpolacijske metode** (posebno linear, spline, cubic) postižu najniži MAE na random scenariju za sve testirane missing rateove (10–80 %).
2. **Linear i time interpolacija** daju identične rezultate jer su uzorci ravnomjerno raspoređeni u vremenu (Jena 10-min intervali).
3. Na **block scenariju** linear/time i dalje vode; forward fill i cubic/spline znatno gore zbog dugačkih rupa.
4. **ML metode** (KNN, decision tree, random forest) na ovom skupu (7 dana, 10-min) **ne nadmašuju** klasične metode.
5. **KNN** na block scenariju pokazuje najveću pogrešku (npr. MAE ≈ 3.56 pri 80% block).
6. Pri visokim missing rateovima (50–80 %) pogreška naglo raste na block_start, block_middle i block_end scenarijima.

## Grafovi

Otvori `results/grafovi_pregled.html` u pregledniku za vizualni pregled svih grafova.

---
*Generirano: `python scripts/report.py`*
