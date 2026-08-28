# Analiza rezultata eksperimenata

Automatski generirano iz `experiment_results.csv`.

## Sažetak

- **Random missing (20%):** najbolja metoda — **spline_interpolation**
- **Block missing (20%):** najbolja metoda — **decision_tree**
- **Klasične vs ML (prosjek MAE, random 20%):** 0.1027 vs 0.0793
- **Klasične vs ML (prosjek MAE, block 20%):** 2.4410 vs 1.4785

## Tablica — random missing, 20%

| metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| spline_interpolation | 0.0635 | 0.1052 | 0.9997 |
| adaptive_imputation | 0.0635 | 0.1052 | 0.9997 |
| cubic_interpolation | 0.0635 | 0.1052 | 0.9997 |
| time_interpolation | 0.0730 | 0.1185 | 0.9996 |
| knn | 0.0730 | 0.1185 | 0.9996 |
| linear_interpolation | 0.0730 | 0.1185 | 0.9996 |
| random_forest | 0.0782 | 0.1259 | 0.9996 |
| decision_tree | 0.0819 | 0.1334 | 0.9995 |
| neural_net | 0.0871 | 0.1357 | 0.9995 |
| knn_upgraded | 0.0922 | 0.1464 | 0.9994 |
| forward_fill | 0.1635 | 0.2588 | 0.9982 |
| moving_average | 0.1796 | 0.2998 | 0.9976 |

## Tablica — block missing, 20%

| metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| decision_tree | 1.4761 | 1.6957 | -2.6736 |
| random_forest | 1.4763 | 1.6961 | -2.6753 |
| linear_interpolation | 1.4765 | 1.6968 | -2.6787 |
| time_interpolation | 1.4765 | 1.6968 | -2.6787 |
| knn | 1.4765 | 1.6968 | -2.6787 |
| adaptive_imputation | 1.4765 | 1.6968 | -2.6787 |
| neural_net | 1.4780 | 1.7466 | -2.8976 |
| knn_upgraded | 1.4877 | 1.7057 | -2.7171 |
| moving_average | 1.5990 | 1.8308 | -3.2827 |
| forward_fill | 1.6054 | 1.8330 | -3.2929 |
| spline_interpolation | 4.2442 | 5.0983 | -32.2091 |
| cubic_interpolation | 4.2442 | 5.0983 | -32.2091 |

## Najbolja metoda po scenariju i missing rateu

| scenarij | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|----------|---- | ---- | ---- | ---- | ---- | ---- | ---- | ----|
| random | spline_interpolation | spline_interpolation | linear_interpolation | spline_interpolation | spline_interpolation | cubic_interpolation | linear_interpolation | linear_interpolation |
| block | random_forest | decision_tree | neural_net | decision_tree | neural_net | neural_net | moving_average | neural_net |
| block_start | decision_tree | linear_interpolation | adaptive_imputation | linear_interpolation | neural_net | cubic_interpolation | cubic_interpolation | moving_average |
| block_middle | random_forest | neural_net | cubic_interpolation | moving_average | cubic_interpolation | moving_average | moving_average | moving_average |
| block_end | decision_tree | cubic_interpolation | spline_interpolation | decision_tree | neural_net | linear_interpolation | linear_interpolation | cubic_interpolation |

## Ključni nalazi (za poglavlje Rezultati)

1. **Klasične interpolacijske metode** (posebno linear, spline, cubic) postižu najniži MAE na random scenariju za sve testirane missing rateove (10–80 %).
2. **Linear i time interpolacija** daju identične rezultate jer su uzorci ravnomjerno raspoređeni u vremenu (Jena 10-min intervali).
3. Na **block scenariju** linear/time i dalje vode; forward fill i cubic/spline znatno gore zbog dugačkih rupa.
4. **ML metode** (KNN, decision tree, random forest) na ovom skupu (7 dana, 10-min) **ne nadmašuju** klasične metode.
5. **KNN** na block scenariju pokazuje najveću pogrešku (npr. MAE ≈ 4.80 pri 80% block).
6. Pri visokim missing rateovima (50–80 %) pogreška naglo raste na block_start, block_middle i block_end scenarijima.

## Grafovi

Otvori `results/grafovi_pregled.html` u pregledniku za vizualni pregled svih grafova.

---
*Generirano: `python scripts/report.py`*
