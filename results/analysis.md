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

| scenarij | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|----------|---- | ---- | ---- | ---- | ---- | ---- | ---- | ----|
| random | cubic_interpolation | cubic_interpolation | cubic_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation |
| block | linear_interpolation | cubic_interpolation | linear_interpolation | linear_interpolation | forward_fill | linear_interpolation | linear_interpolation | linear_interpolation |
| block_start | linear_interpolation | forward_fill | cubic_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation |
| block_middle | decision_tree | forward_fill | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation | linear_interpolation |
| block_end | linear_interpolation | linear_interpolation | cubic_interpolation | random_forest | decision_tree | cubic_interpolation | linear_interpolation | linear_interpolation |

## Ključni nalazi (za poglavlje Rezultati)

1. **Klasične interpolacijske metode** (posebno linear, spline, cubic) postižu najniži MAE na random scenariju za sve testirane missing rateove (10–80 %).
2. **Linear i time interpolacija** daju identične rezultate jer su uzorci ravnomjerno raspoređeni u vremenu (Jena 10-min intervali).
3. Na **block scenariju** linear/time i dalje vode; forward fill i cubic/spline znatno gore zbog dugačkih rupa.
4. **ML metode** (KNN, decision tree, random forest) na ovom datasetu (288 uzoraka) **ne nadmašuju** klasične metode.
5. **KNN** na block scenariju pokazuje najveću pogrešku (npr. MAE ≈ 1.95 pri 80% block).
6. Pri visokim missing rateovima (50–80 %) pogreška naglo raste na block_start, block_middle i block_end scenarijima.

## Grafovi

Otvori `results/grafovi_pregled.html` u pregledniku za vizualni pregled svih grafova.

---
*Generirano: `python scripts/report.py`*
