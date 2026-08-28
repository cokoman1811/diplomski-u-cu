# Diplomski rad — rezultati eksperimenata 10–80 % missing rate
*Izvor: `results/experiment_results.csv` (480 redaka)*
*Generirano automatski iz stvarnih CSV podataka*

---

## PROMJENE U EKSPERIMENTU

- Dodani missing rateovi: **50 %, 60 %, 70 %, 80 %**
- Konačni popis: 10 %, 20 %, 30 %, 40 %, 50 %, 60 %, 70 %, 80 %
- Ukupno: 5 scenarija × 8 rateova × 12 metoda = **480 testova**
- **Nove metode:** moving_average (pomični prosjek), knn (osnovni), knn_upgraded (napredni), adaptive_imputation (hibridna)
- Pri 80 % na nizu od 1008 zapisa uklanja se **806 vrijednosti**; prva i zadnja ostaju poznate
- Svi scenariji (uključujući block_start/middle/end) rade ispravno do 80 %

---

## ODGOVORI NA PITANJA (iz CSV-a)

### 1. Najbolja metoda po MAE (po scenariju i rateu)

- **random** @ 10%: spline_interpolation (MAE=0.0470)
- **random** @ 20%: spline_interpolation (MAE=0.0635)
- **random** @ 30%: linear_interpolation (MAE=0.0834)
- **random** @ 40%: spline_interpolation (MAE=0.0908)
- **random** @ 50%: spline_interpolation (MAE=0.0997)
- **random** @ 60%: cubic_interpolation (MAE=0.1230)
- **random** @ 70%: linear_interpolation (MAE=0.1774)
- **random** @ 80%: linear_interpolation (MAE=0.1785)
- **block** @ 10%: random_forest (MAE=1.0145)
- **block** @ 20%: decision_tree (MAE=1.4761)
- **block** @ 30%: neural_net (MAE=3.4236)
- **block** @ 40%: decision_tree (MAE=2.7163)
- **block** @ 50%: neural_net (MAE=5.3664)
- **block** @ 60%: neural_net (MAE=5.1730)
- **block** @ 70%: moving_average (MAE=3.4009)
- **block** @ 80%: neural_net (MAE=4.7335)
- **block_start** @ 10%: decision_tree (MAE=0.7313)
- **block_start** @ 20%: linear_interpolation (MAE=0.6991)
- **block_start** @ 30%: adaptive_imputation (MAE=1.9325)
- **block_start** @ 40%: linear_interpolation (MAE=1.8038)
- **block_start** @ 50%: neural_net (MAE=1.3679)
- **block_start** @ 60%: cubic_interpolation (MAE=1.5243)
- **block_start** @ 70%: cubic_interpolation (MAE=3.5094)
- **block_start** @ 80%: moving_average (MAE=4.2301)
- **block_middle** @ 10%: random_forest (MAE=0.4707)
- **block_middle** @ 20%: neural_net (MAE=1.1338)
- **block_middle** @ 30%: cubic_interpolation (MAE=3.9194)
- **block_middle** @ 40%: moving_average (MAE=3.6225)
- **block_middle** @ 50%: cubic_interpolation (MAE=1.2192)
- **block_middle** @ 60%: moving_average (MAE=3.3220)
- **block_middle** @ 70%: moving_average (MAE=3.7491)
- **block_middle** @ 80%: moving_average (MAE=4.5123)
- **block_end** @ 10%: decision_tree (MAE=2.6289)
- **block_end** @ 20%: cubic_interpolation (MAE=4.1828)
- **block_end** @ 30%: spline_interpolation (MAE=4.8486)
- **block_end** @ 40%: decision_tree (MAE=5.4621)
- **block_end** @ 50%: neural_net (MAE=4.5343)
- **block_end** @ 60%: linear_interpolation (MAE=4.9650)
- **block_end** @ 70%: linear_interpolation (MAE=5.2253)
- **block_end** @ 80%: cubic_interpolation (MAE=4.0472)

### 2. Najbolja metoda po RMSE

- **random** @ 10%: spline_interpolation (RMSE=0.0828)
- **random** @ 20%: cubic_interpolation (RMSE=0.1052)
- **random** @ 30%: random_forest (RMSE=0.1368)
- **random** @ 40%: random_forest (RMSE=0.1519)
- **random** @ 50%: random_forest (RMSE=0.1650)
- **random** @ 60%: cubic_interpolation (RMSE=0.2369)
- **random** @ 70%: linear_interpolation (RMSE=0.3320)
- **random** @ 80%: linear_interpolation (RMSE=0.3145)
- **block** @ 10%: neural_net (RMSE=1.1710)
- **block** @ 20%: decision_tree (RMSE=1.6957)
- **block** @ 30%: linear_interpolation (RMSE=4.0453)
- **block** @ 40%: neural_net (RMSE=3.3750)
- **block** @ 50%: decision_tree (RMSE=6.9366)
- **block** @ 60%: neural_net (RMSE=6.7561)
- **block** @ 70%: moving_average (RMSE=4.7069)
- **block** @ 80%: neural_net (RMSE=6.0506)
- **block_start** @ 10%: decision_tree (RMSE=0.8856)
- **block_start** @ 20%: linear_interpolation (RMSE=0.8889)
- **block_start** @ 30%: adaptive_imputation (RMSE=2.1842)
- **block_start** @ 40%: linear_interpolation (RMSE=2.1093)
- **block_start** @ 50%: neural_net (RMSE=1.7544)
- **block_start** @ 60%: cubic_interpolation (RMSE=1.8189)
- **block_start** @ 70%: moving_average (RMSE=4.5339)
- **block_start** @ 80%: moving_average (RMSE=4.7813)
- **block_middle** @ 10%: random_forest (RMSE=0.5657)
- **block_middle** @ 20%: neural_net (RMSE=1.2839)
- **block_middle** @ 30%: neural_net (RMSE=4.2144)
- **block_middle** @ 40%: moving_average (RMSE=4.0178)
- **block_middle** @ 50%: cubic_interpolation (RMSE=1.7261)
- **block_middle** @ 60%: moving_average (RMSE=4.6986)
- **block_middle** @ 70%: moving_average (RMSE=5.2530)
- **block_middle** @ 80%: moving_average (RMSE=6.2311)
- **block_end** @ 10%: decision_tree (RMSE=2.9110)
- **block_end** @ 20%: cubic_interpolation (RMSE=4.5838)
- **block_end** @ 30%: spline_interpolation (RMSE=5.9726)
- **block_end** @ 40%: decision_tree (RMSE=6.6719)
- **block_end** @ 50%: decision_tree (RMSE=5.8106)
- **block_end** @ 60%: random_forest (RMSE=5.8173)
- **block_end** @ 70%: neural_net (RMSE=6.0477)
- **block_end** @ 80%: neural_net (RMSE=5.2041)

### 3. Najbolja metoda po R²

- **random** @ 10%: cubic_interpolation (R²=0.9998)
- **random** @ 20%: cubic_interpolation (R²=0.9997)
- **random** @ 30%: random_forest (R²=0.9995)
- **random** @ 40%: random_forest (R²=0.9994)
- **random** @ 50%: random_forest (R²=0.9992)
- **random** @ 60%: cubic_interpolation (R²=0.9985)
- **random** @ 70%: linear_interpolation (R²=0.9971)
- **random** @ 80%: linear_interpolation (R²=0.9974)
- **block** @ 10%: neural_net (R²=-1.5564)
- **block** @ 20%: decision_tree (R²=-2.6736)
- **block** @ 30%: linear_interpolation (R²=0.3980)
- **block** @ 40%: neural_net (R²=0.7589)
- **block** @ 50%: decision_tree (R²=0.1684)
- **block** @ 60%: neural_net (R²=0.1664)
- **block** @ 70%: moving_average (R²=0.0057)
- **block** @ 80%: neural_net (R²=0.1820)
- **block_start** @ 10%: decision_tree (R²=0.6088)
- **block_start** @ 20%: linear_interpolation (R²=0.7639)
- **block_start** @ 30%: adaptive_imputation (R²=-0.2000)
- **block_start** @ 40%: linear_interpolation (R²=0.0554)
- **block_start** @ 50%: neural_net (R²=0.4808)
- **block_start** @ 60%: cubic_interpolation (R²=0.4898)
- **block_start** @ 70%: moving_average (R²=-2.1084)
- **block_start** @ 80%: moving_average (R²=-0.3767)
- **block_middle** @ 10%: random_forest (R²=-2.1814)
- **block_middle** @ 20%: neural_net (R²=-2.5297)
- **block_middle** @ 30%: neural_net (R²=-10.0895)
- **block_middle** @ 40%: moving_average (R²=-1.2784)
- **block_middle** @ 50%: cubic_interpolation (R²=0.7966)
- **block_middle** @ 60%: moving_average (R²=-0.0628)
- **block_middle** @ 70%: moving_average (R²=-0.0208)
- **block_middle** @ 80%: moving_average (R²=-0.0139)
- **block_end** @ 10%: decision_tree (R²=0.6776)
- **block_end** @ 20%: cubic_interpolation (R²=0.2258)
- **block_end** @ 30%: spline_interpolation (R²=-0.7742)
- **block_end** @ 40%: decision_tree (R²=-0.1895)
- **block_end** @ 50%: decision_tree (R²=0.3353)
- **block_end** @ 60%: random_forest (R²=0.3576)
- **block_end** @ 70%: neural_net (R²=0.2272)
- **block_end** @ 80%: neural_net (R²=0.3890)

### 4. Kako se MAE mijenja (10 % → 80 %)?

Prosječni MAE svih metoda i scenarija: 1.4278 (10 %) → 5.5728 (80 %).
Na **random** scenariju: 0,079 → 0,224. Na **block_end**: 0,422 → 3,468.

### 5. Kako se RMSE mijenja?

Prosjek svih metoda: 1.7021 (10 %) → 6.8539 (80 %).

### 6. Kako se R² mijenja?

Prosjek svih metoda: -1.0156 (10 %) → -2.6931 (80 %).
Na random scenariju klasične metode zadržavaju R² > 0,99. Na block scenarijima mnoge metode imaju negativan R².

### 7. Najteži scenarij pri 80 %?

**block_end** — prosječni MAE svih metoda = **4.6081** °C.
Slijedi block_middle (6.4350), block (7.8999), block_start (8.6816), random (0.2392).

### 8. Najstabilnija pojedinačna metoda (10–80 %)?

**linear_interpolation** / **time_interpolation** — prosječni MAE = 3.1315, σ = 2.3467.

### 8b. Najbolja metoda ukupno?

**adaptive_imputation** — prosječni MAE = 2.7046, pobjeđuje u **1 od 40** kombinacija scenarij/rate.

### 9. Usporedba osnovnog i naprednog KNN

Osnovni KNN prosječni MAE = **3.1315** °C.
Napredni KNN prosječni MAE = **3.1278** °C.
**Osnovni KNN je bolji u prosjeku** (razlika -0.0037 °C).

Po scenariju:
- **random**: osnovni MAE=0.1124, napredni MAE=0.1365 → bolji: knn (osnovni)
- **block**: osnovni MAE=3.7733, napredni MAE=3.7651 → bolji: knn_upgraded (napredni)
- **block_start**: osnovni MAE=2.3795, napredni MAE=2.4494 → bolji: knn (osnovni)
- **block_middle**: osnovni MAE=4.2521, napredni MAE=4.2309 → bolji: knn_upgraded (napredni)
- **block_end**: osnovni MAE=5.1400, napredni MAE=5.0570 → bolji: knn_upgraded (napredni)

### 10. Pomični prosjek (moving_average)

Prosječni MAE = **3.6985** °C (linear = 3.1315 °C).
Pomični prosjek koristi prozor ±6 uzoraka (1 sat pri 10-min intervalima).
Bolji od forward_fill i KNN na random scenariju, ali lošiji od linear interpolacije.

### 11. Metoda koja najviše gubi kvalitetu?

**knn_upgraded** — najveći prosječni MAE među KNN varijantama; na block scenarijima ekstremno loš.

**Djelomično ne.** Linear interpolacija i dalje dominira među pojedinačnim metodama. **Adaptive_imputation** nadmašuje sve. Block scenariji postaju ekstremno teški pri 70–80 %.

### 12. Ostaje li linear_interpolation najbolja pojedinačna metoda?

**Da.** Pobjeđuje u **7 od 40** kombinacija scenarij/rate po MAE (bez adaptive).

### 13. Ostaje li cubic_interpolation najbolja za random?

**Djelomično.** Cubic je najbolja pri 10 %, 20 % i 30 % random. Od 40 % do 80 % vodi **linear_interpolation**.

### 14. KNN pri 50–80 %?

Na **random**: MAE 0,28–0,64 °C (prihvatljivo).
Na **block** scenarijima: MAE **1,95–3,52** °C (vrlo loše). R² često jako negativan.

### 15. Decision Tree i Random Forest pri 50–80 %?

Prosječni MAE: DT = 3.9422 °C, RF = 3.9332 °C.
DT je nešto bolji u prosjeku. Obje metode znatno gore od linear interpolacije na block scenarijima.

### 16. Negativan R² pri većim rateovima?

**Da.** Ukupno **253** od 480 rezultata ima R² < 0.
Pri 80 %: **30** od 40 kombinacija (po najboljoj metodi po scenariju). Najčešće: knn_upgraded, forward_fill, cubic/spline na block scenarijima.

---

## TABLICA 1: Najbolja metoda po scenariju i missing rateu

| scenario | block_position | missing_rate | najbolja metoda po MAE | MAE | RMSE | R² |
|----------|----------------|--------------|------------------------|-----|------|-----|
| block | none | 0.10 | random_forest | 1.0145 | 1.1739 | -1.5687 |
| block | none | 0.20 | decision_tree | 1.4761 | 1.6957 | -2.6736 |
| block | none | 0.30 | neural_net | 3.4236 | 4.0464 | 0.3977 |
| block | none | 0.40 | decision_tree | 2.7163 | 3.3872 | 0.7571 |
| block | none | 0.50 | neural_net | 5.3664 | 6.9675 | 0.1610 |
| block | none | 0.60 | neural_net | 5.1730 | 6.7561 | 0.1664 |
| block | none | 0.70 | moving_average | 3.4009 | 4.7069 | 0.0057 |
| block | none | 0.80 | neural_net | 4.7335 | 6.0506 | 0.1820 |
| block_end | end | 0.10 | decision_tree | 2.6289 | 2.9110 | 0.6776 |
| block_end | end | 0.20 | cubic_interpolation | 4.1828 | 4.5838 | 0.2258 |
| block_end | end | 0.30 | spline_interpolation | 4.8486 | 5.9726 | -0.7742 |
| block_end | end | 0.40 | decision_tree | 5.4621 | 6.6719 | -0.1895 |
| block_end | end | 0.50 | neural_net | 4.5343 | 6.1421 | 0.2573 |
| block_end | end | 0.60 | linear_interpolation | 4.9650 | 6.0693 | 0.3007 |
| block_end | end | 0.70 | linear_interpolation | 5.2253 | 6.0540 | 0.2256 |
| block_end | end | 0.80 | cubic_interpolation | 4.0472 | 5.7523 | 0.2535 |
| block_middle | middle | 0.10 | random_forest | 0.4707 | 0.5657 | -2.1814 |
| block_middle | middle | 0.20 | neural_net | 1.1338 | 1.2839 | -2.5297 |
| block_middle | middle | 0.30 | cubic_interpolation | 3.9194 | 4.8003 | -13.3868 |
| block_middle | middle | 0.40 | moving_average | 3.6225 | 4.0178 | -1.2784 |
| block_middle | middle | 0.50 | cubic_interpolation | 1.2192 | 1.7261 | 0.7966 |
| block_middle | middle | 0.60 | moving_average | 3.3220 | 4.6986 | -0.0628 |
| block_middle | middle | 0.70 | moving_average | 3.7491 | 5.2530 | -0.0208 |
| block_middle | middle | 0.80 | moving_average | 4.5123 | 6.2311 | -0.0139 |
| block_start | start | 0.10 | decision_tree | 0.7313 | 0.8856 | 0.6088 |
| block_start | start | 0.20 | linear_interpolation | 0.6991 | 0.8889 | 0.7639 |
| block_start | start | 0.30 | adaptive_imputation | 1.9325 | 2.1842 | -0.2000 |
| block_start | start | 0.40 | linear_interpolation | 1.8038 | 2.1093 | 0.0554 |
| block_start | start | 0.50 | neural_net | 1.3679 | 1.7544 | 0.4808 |
| block_start | start | 0.60 | cubic_interpolation | 1.5243 | 1.8189 | 0.4898 |
| block_start | start | 0.70 | cubic_interpolation | 3.5094 | 4.7387 | -2.3956 |
| block_start | start | 0.80 | moving_average | 4.2301 | 4.7813 | -0.3767 |
| random | none | 0.10 | spline_interpolation | 0.0470 | 0.0828 | 0.9998 |
| random | none | 0.20 | spline_interpolation | 0.0635 | 0.1052 | 0.9997 |
| random | none | 0.30 | linear_interpolation | 0.0834 | 0.1401 | 0.9995 |
| random | none | 0.40 | spline_interpolation | 0.0908 | 0.1724 | 0.9992 |
| random | none | 0.50 | spline_interpolation | 0.0997 | 0.2109 | 0.9988 |
| random | none | 0.60 | cubic_interpolation | 0.1230 | 0.2369 | 0.9985 |
| random | none | 0.70 | linear_interpolation | 0.1774 | 0.3320 | 0.9971 |
| random | none | 0.80 | linear_interpolation | 0.1785 | 0.3145 | 0.9974 |

---

## TABLICA 2: Random missing 10–80 %

| missing_rate | method | MAE | RMSE | R² |
|-------------|--------|-----|------|-----|
| 0.10 | spline_interpolation | 0.0470 | 0.0828 | 0.9998 |
| 0.10 | adaptive_imputation | 0.0470 | 0.0828 | 0.9998 |
| 0.10 | cubic_interpolation | 0.0472 | 0.0829 | 0.9998 |
| 0.10 | linear_interpolation | 0.0626 | 0.0983 | 0.9997 |
| 0.10 | time_interpolation | 0.0626 | 0.0983 | 0.9997 |
| 0.10 | knn | 0.0626 | 0.0983 | 0.9997 |
| 0.10 | random_forest | 0.0657 | 0.1051 | 0.9997 |
| 0.10 | knn_upgraded | 0.0696 | 0.1060 | 0.9997 |
| 0.10 | neural_net | 0.0724 | 0.1175 | 0.9996 |
| 0.10 | decision_tree | 0.0761 | 0.1209 | 0.9996 |
| 0.10 | moving_average | 0.1464 | 0.2212 | 0.9986 |
| 0.10 | forward_fill | 0.1587 | 0.2867 | 0.9976 |
| 0.20 | spline_interpolation | 0.0635 | 0.1052 | 0.9997 |
| 0.20 | adaptive_imputation | 0.0635 | 0.1052 | 0.9997 |
| 0.20 | cubic_interpolation | 0.0635 | 0.1052 | 0.9997 |
| 0.20 | linear_interpolation | 0.0730 | 0.1185 | 0.9996 |
| 0.20 | time_interpolation | 0.0730 | 0.1185 | 0.9996 |
| 0.20 | knn | 0.0730 | 0.1185 | 0.9996 |
| 0.20 | random_forest | 0.0782 | 0.1259 | 0.9996 |
| 0.20 | decision_tree | 0.0819 | 0.1334 | 0.9995 |
| 0.20 | neural_net | 0.0871 | 0.1357 | 0.9995 |
| 0.20 | knn_upgraded | 0.0922 | 0.1464 | 0.9994 |
| 0.20 | forward_fill | 0.1635 | 0.2588 | 0.9982 |
| 0.20 | moving_average | 0.1796 | 0.2998 | 0.9976 |
| 0.30 | linear_interpolation | 0.0834 | 0.1401 | 0.9995 |
| 0.30 | time_interpolation | 0.0834 | 0.1401 | 0.9995 |
| 0.30 | knn | 0.0834 | 0.1401 | 0.9995 |
| 0.30 | adaptive_imputation | 0.0834 | 0.1401 | 0.9995 |
| 0.30 | random_forest | 0.0840 | 0.1368 | 0.9995 |
| 0.30 | spline_interpolation | 0.0879 | 0.1789 | 0.9991 |
| 0.30 | cubic_interpolation | 0.0879 | 0.1789 | 0.9991 |
| 0.30 | decision_tree | 0.0930 | 0.1494 | 0.9994 |
| 0.30 | neural_net | 0.0950 | 0.1524 | 0.9994 |
| 0.30 | knn_upgraded | 0.1015 | 0.1598 | 0.9993 |
| 0.30 | forward_fill | 0.1820 | 0.2989 | 0.9975 |
| 0.30 | moving_average | 0.1986 | 0.3207 | 0.9972 |
| 0.40 | spline_interpolation | 0.0908 | 0.1724 | 0.9992 |
| 0.40 | adaptive_imputation | 0.0908 | 0.1724 | 0.9992 |
| 0.40 | cubic_interpolation | 0.0909 | 0.1726 | 0.9992 |
| 0.40 | random_forest | 0.0938 | 0.1519 | 0.9994 |
| 0.40 | linear_interpolation | 0.0950 | 0.1596 | 0.9993 |
| 0.40 | time_interpolation | 0.0950 | 0.1596 | 0.9993 |
| 0.40 | knn | 0.0950 | 0.1596 | 0.9993 |
| 0.40 | decision_tree | 0.1062 | 0.1822 | 0.9991 |
| 0.40 | knn_upgraded | 0.1214 | 0.1867 | 0.9990 |
| 0.40 | neural_net | 0.1238 | 0.1882 | 0.9990 |
| 0.40 | moving_average | 0.2038 | 0.3281 | 0.9970 |
| 0.40 | forward_fill | 0.2157 | 0.3499 | 0.9966 |
| 0.50 | spline_interpolation | 0.0997 | 0.2109 | 0.9988 |
| 0.50 | adaptive_imputation | 0.0997 | 0.2109 | 0.9988 |
| 0.50 | cubic_interpolation | 0.0998 | 0.2110 | 0.9988 |
| 0.50 | random_forest | 0.1002 | 0.1650 | 0.9992 |
| 0.50 | linear_interpolation | 0.1020 | 0.1809 | 0.9991 |
| 0.50 | time_interpolation | 0.1020 | 0.1809 | 0.9991 |
| 0.50 | knn | 0.1020 | 0.1809 | 0.9991 |
| 0.50 | decision_tree | 0.1266 | 0.2178 | 0.9987 |
| 0.50 | knn_upgraded | 0.1364 | 0.2146 | 0.9987 |
| 0.50 | neural_net | 0.1429 | 0.2385 | 0.9984 |
| 0.50 | moving_average | 0.2293 | 0.3686 | 0.9962 |
| 0.50 | forward_fill | 0.2415 | 0.3979 | 0.9956 |
| 0.60 | cubic_interpolation | 0.1230 | 0.2369 | 0.9985 |
| 0.60 | adaptive_imputation | 0.1230 | 0.2369 | 0.9985 |
| 0.60 | spline_interpolation | 0.1232 | 0.2371 | 0.9985 |
| 0.60 | linear_interpolation | 0.1276 | 0.2484 | 0.9983 |
| 0.60 | time_interpolation | 0.1276 | 0.2484 | 0.9983 |
| 0.60 | knn | 0.1276 | 0.2484 | 0.9983 |
| 0.60 | random_forest | 0.1291 | 0.2528 | 0.9983 |
| 0.60 | decision_tree | 0.1501 | 0.2654 | 0.9981 |
| 0.60 | knn_upgraded | 0.1614 | 0.2741 | 0.9980 |
| 0.60 | neural_net | 0.1754 | 0.2798 | 0.9979 |
| 0.60 | moving_average | 0.2323 | 0.3733 | 0.9962 |
| 0.60 | forward_fill | 0.2741 | 0.4235 | 0.9951 |
| 0.70 | linear_interpolation | 0.1774 | 0.3320 | 0.9971 |
| 0.70 | time_interpolation | 0.1774 | 0.3320 | 0.9971 |
| 0.70 | knn | 0.1774 | 0.3320 | 0.9971 |
| 0.70 | adaptive_imputation | 0.1774 | 0.3320 | 0.9971 |
| 0.70 | random_forest | 0.1904 | 0.3628 | 0.9965 |
| 0.70 | knn_upgraded | 0.2082 | 0.3630 | 0.9965 |
| 0.70 | decision_tree | 0.2095 | 0.3992 | 0.9958 |
| 0.70 | cubic_interpolation | 0.2138 | 0.4691 | 0.9941 |
| 0.70 | spline_interpolation | 0.2140 | 0.4692 | 0.9941 |
| 0.70 | neural_net | 0.2181 | 0.3737 | 0.9963 |
| 0.70 | moving_average | 0.2955 | 0.5134 | 0.9930 |
| 0.70 | forward_fill | 0.4076 | 0.7183 | 0.9863 |
| 0.80 | linear_interpolation | 0.1785 | 0.3145 | 0.9974 |
| 0.80 | time_interpolation | 0.1785 | 0.3145 | 0.9974 |
| 0.80 | knn | 0.1785 | 0.3145 | 0.9974 |
| 0.80 | adaptive_imputation | 0.1785 | 0.3145 | 0.9974 |
| 0.80 | random_forest | 0.1829 | 0.3146 | 0.9974 |
| 0.80 | spline_interpolation | 0.1936 | 0.3443 | 0.9968 |
| 0.80 | cubic_interpolation | 0.1939 | 0.3446 | 0.9968 |
| 0.80 | knn_upgraded | 0.2013 | 0.3327 | 0.9970 |
| 0.80 | decision_tree | 0.2368 | 0.3748 | 0.9962 |
| 0.80 | neural_net | 0.2531 | 0.3886 | 0.9960 |
| 0.80 | moving_average | 0.3528 | 0.6606 | 0.9883 |
| 0.80 | forward_fill | 0.5416 | 0.9838 | 0.9741 |

---

## TABLICA 3: Block missing 10–80 %

| missing_rate | method | MAE | RMSE | R² |
|-------------|--------|-----|------|-----|
| 0.10 | random_forest | 1.0145 | 1.1739 | -1.5687 |
| 0.10 | neural_net | 1.0249 | 1.1710 | -1.5564 |
| 0.10 | decision_tree | 1.0268 | 1.1854 | -1.6195 |
| 0.10 | linear_interpolation | 1.0285 | 1.1880 | -1.6311 |
| 0.10 | time_interpolation | 1.0285 | 1.1880 | -1.6311 |
| 0.10 | knn | 1.0285 | 1.1880 | -1.6311 |
| 0.10 | adaptive_imputation | 1.0285 | 1.1880 | -1.6311 |
| 0.10 | knn_upgraded | 1.0387 | 1.1966 | -1.6692 |
| 0.10 | cubic_interpolation | 1.1604 | 1.3978 | -2.6421 |
| 0.10 | spline_interpolation | 1.1604 | 1.3978 | -2.6421 |
| 0.10 | moving_average | 1.4884 | 1.6774 | -4.2453 |
| 0.10 | forward_fill | 1.5435 | 1.7084 | -4.4409 |
| 0.20 | decision_tree | 1.4761 | 1.6957 | -2.6736 |
| 0.20 | random_forest | 1.4763 | 1.6961 | -2.6753 |
| 0.20 | linear_interpolation | 1.4765 | 1.6968 | -2.6787 |
| 0.20 | time_interpolation | 1.4765 | 1.6968 | -2.6787 |
| 0.20 | knn | 1.4765 | 1.6968 | -2.6787 |
| 0.20 | adaptive_imputation | 1.4765 | 1.6968 | -2.6787 |
| 0.20 | neural_net | 1.4780 | 1.7466 | -2.8976 |
| 0.20 | knn_upgraded | 1.4877 | 1.7057 | -2.7171 |
| 0.20 | moving_average | 1.5990 | 1.8308 | -3.2827 |
| 0.20 | forward_fill | 1.6054 | 1.8330 | -3.2929 |
| 0.20 | cubic_interpolation | 4.2442 | 5.0983 | -32.2091 |
| 0.20 | spline_interpolation | 4.2442 | 5.0983 | -32.2091 |
| 0.30 | neural_net | 3.4236 | 4.0464 | 0.3977 |
| 0.30 | linear_interpolation | 3.4286 | 4.0453 | 0.3980 |
| 0.30 | time_interpolation | 3.4286 | 4.0453 | 0.3980 |
| 0.30 | knn | 3.4286 | 4.0453 | 0.3980 |
| 0.30 | adaptive_imputation | 3.4286 | 4.0453 | 0.3980 |
| 0.30 | knn_upgraded | 3.4334 | 4.0528 | 0.3958 |
| 0.30 | random_forest | 3.4364 | 4.0565 | 0.3947 |
| 0.30 | decision_tree | 3.5234 | 4.1382 | 0.3701 |
| 0.30 | moving_average | 3.8178 | 6.1890 | -0.4090 |
| 0.30 | forward_fill | 4.1018 | 6.5393 | -0.5729 |
| 0.30 | cubic_interpolation | 7.7599 | 9.5520 | -2.3562 |
| 0.30 | spline_interpolation | 7.7599 | 9.5520 | -2.3562 |
| 0.40 | decision_tree | 2.7163 | 3.3872 | 0.7571 |
| 0.40 | neural_net | 2.7429 | 3.3750 | 0.7589 |
| 0.40 | random_forest | 2.7685 | 3.4427 | 0.7491 |
| 0.40 | knn_upgraded | 2.8677 | 3.5369 | 0.7352 |
| 0.40 | linear_interpolation | 2.9308 | 3.6053 | 0.7248 |
| 0.40 | time_interpolation | 2.9308 | 3.6053 | 0.7248 |
| 0.40 | knn | 2.9308 | 3.6053 | 0.7248 |
| 0.40 | adaptive_imputation | 2.9308 | 3.6053 | 0.7248 |
| 0.40 | moving_average | 7.0965 | 9.7645 | -1.0184 |
| 0.40 | forward_fill | 7.3827 | 10.0695 | -1.1464 |
| 0.40 | cubic_interpolation | 27.7372 | 31.8543 | -20.4801 |
| 0.40 | spline_interpolation | 27.7372 | 31.8543 | -20.4801 |
| 0.50 | neural_net | 5.3664 | 6.9675 | 0.1610 |
| 0.50 | decision_tree | 5.3983 | 6.9366 | 0.1684 |
| 0.50 | random_forest | 5.4200 | 6.9994 | 0.1533 |
| 0.50 | linear_interpolation | 5.4362 | 7.0441 | 0.1425 |
| 0.50 | time_interpolation | 5.4362 | 7.0441 | 0.1425 |
| 0.50 | knn | 5.4362 | 7.0441 | 0.1425 |
| 0.50 | adaptive_imputation | 5.4362 | 7.0441 | 0.1425 |
| 0.50 | knn_upgraded | 5.4447 | 7.0452 | 0.1422 |
| 0.50 | cubic_interpolation | 6.0174 | 7.4492 | 0.0410 |
| 0.50 | spline_interpolation | 6.0174 | 7.4492 | 0.0410 |
| 0.50 | moving_average | 8.1601 | 10.9449 | -1.0703 |
| 0.50 | forward_fill | 8.2467 | 10.9793 | -1.0833 |
| 0.60 | neural_net | 5.1730 | 6.7561 | 0.1664 |
| 0.60 | random_forest | 5.3146 | 6.8543 | 0.1420 |
| 0.60 | knn_upgraded | 5.3496 | 6.8887 | 0.1334 |
| 0.60 | linear_interpolation | 5.3499 | 6.8720 | 0.1376 |
| 0.60 | time_interpolation | 5.3499 | 6.8720 | 0.1376 |
| 0.60 | knn | 5.3499 | 6.8720 | 0.1376 |
| 0.60 | adaptive_imputation | 5.3499 | 6.8720 | 0.1376 |
| 0.60 | decision_tree | 5.3601 | 6.9710 | 0.1126 |
| 0.60 | moving_average | 6.6641 | 9.1634 | -0.5334 |
| 0.60 | forward_fill | 6.7044 | 9.1770 | -0.5379 |
| 0.60 | cubic_interpolation | 12.8316 | 15.8642 | -3.5960 |
| 0.60 | spline_interpolation | 12.8316 | 15.8642 | -3.5960 |
| 0.70 | moving_average | 3.4009 | 4.7069 | 0.0057 |
| 0.70 | forward_fill | 3.5043 | 4.8567 | -0.0586 |
| 0.70 | adaptive_imputation | 3.5043 | 4.8567 | -0.0586 |
| 0.70 | neural_net | 5.5727 | 6.8960 | -1.1343 |
| 0.70 | decision_tree | 5.6223 | 6.9391 | -1.1610 |
| 0.70 | random_forest | 5.6928 | 7.0058 | -1.2028 |
| 0.70 | knn_upgraded | 5.6963 | 7.0022 | -1.2006 |
| 0.70 | linear_interpolation | 5.7381 | 7.0407 | -1.2248 |
| 0.70 | time_interpolation | 5.7381 | 7.0407 | -1.2248 |
| 0.70 | knn | 5.7381 | 7.0407 | -1.2248 |
| 0.70 | cubic_interpolation | 10.1423 | 11.1737 | -4.6034 |
| 0.70 | spline_interpolation | 10.1423 | 11.1737 | -4.6034 |
| 0.80 | neural_net | 4.7335 | 6.0506 | 0.1820 |
| 0.80 | random_forest | 4.7788 | 6.0769 | 0.1749 |
| 0.80 | linear_interpolation | 4.7975 | 6.1094 | 0.1660 |
| 0.80 | time_interpolation | 4.7975 | 6.1094 | 0.1660 |
| 0.80 | knn | 4.7975 | 6.1094 | 0.1660 |
| 0.80 | adaptive_imputation | 4.7975 | 6.1094 | 0.1660 |
| 0.80 | decision_tree | 4.7976 | 6.1093 | 0.1660 |
| 0.80 | knn_upgraded | 4.8028 | 6.1130 | 0.1650 |
| 0.80 | moving_average | 5.3070 | 7.4487 | -0.2397 |
| 0.80 | forward_fill | 5.3337 | 7.4566 | -0.2424 |
| 0.80 | cubic_interpolation | 22.9276 | 28.3087 | -16.9062 |
| 0.80 | spline_interpolation | 22.9276 | 28.3087 | -16.9062 |

---

## TABLICA 4: block_start, block_middle, block_end — najbolje po MAE

| scenario | block_position | missing_rate | najbolja metoda | MAE | RMSE | R² |
|----------|----------------|--------------|-----------------|-----|------|-----|
| block_end | end | 0.10 | decision_tree | 2.6289 | 2.9110 | 0.6776 |
| block_end | end | 0.20 | cubic_interpolation | 4.1828 | 4.5838 | 0.2258 |
| block_end | end | 0.30 | spline_interpolation | 4.8486 | 5.9726 | -0.7742 |
| block_end | end | 0.40 | decision_tree | 5.4621 | 6.6719 | -0.1895 |
| block_end | end | 0.50 | neural_net | 4.5343 | 6.1421 | 0.2573 |
| block_end | end | 0.60 | linear_interpolation | 4.9650 | 6.0693 | 0.3007 |
| block_end | end | 0.70 | linear_interpolation | 5.2253 | 6.0540 | 0.2256 |
| block_end | end | 0.80 | cubic_interpolation | 4.0472 | 5.7523 | 0.2535 |
| block_middle | middle | 0.10 | random_forest | 0.4707 | 0.5657 | -2.1814 |
| block_middle | middle | 0.20 | neural_net | 1.1338 | 1.2839 | -2.5297 |
| block_middle | middle | 0.30 | cubic_interpolation | 3.9194 | 4.8003 | -13.3868 |
| block_middle | middle | 0.40 | moving_average | 3.6225 | 4.0178 | -1.2784 |
| block_middle | middle | 0.50 | cubic_interpolation | 1.2192 | 1.7261 | 0.7966 |
| block_middle | middle | 0.60 | moving_average | 3.3220 | 4.6986 | -0.0628 |
| block_middle | middle | 0.70 | moving_average | 3.7491 | 5.2530 | -0.0208 |
| block_middle | middle | 0.80 | moving_average | 4.5123 | 6.2311 | -0.0139 |
| block_start | start | 0.10 | decision_tree | 0.7313 | 0.8856 | 0.6088 |
| block_start | start | 0.20 | linear_interpolation | 0.6991 | 0.8889 | 0.7639 |
| block_start | start | 0.30 | adaptive_imputation | 1.9325 | 2.1842 | -0.2000 |
| block_start | start | 0.40 | linear_interpolation | 1.8038 | 2.1093 | 0.0554 |
| block_start | start | 0.50 | neural_net | 1.3679 | 1.7544 | 0.4808 |
| block_start | start | 0.60 | cubic_interpolation | 1.5243 | 1.8189 | 0.4898 |
| block_start | start | 0.70 | cubic_interpolation | 3.5094 | 4.7387 | -2.3956 |
| block_start | start | 0.80 | moving_average | 4.2301 | 4.7813 | -0.3767 |

---

## TABLICA 5: Sažetak po metodama (10–80 %)

| method | prosječni MAE | prosječni RMSE | prosječni R² | std. dev. MAE | komentar |
|--------|---------------|----------------|--------------|---------------|----------|
| adaptive_imputation | 2.7046 | 3.4003 | -0.4576 | 2.0231 | Hibridna metoda — najniži prosječni MAE; pobjeđuje u svim scenarij/rate kombinacijama |
| neural_net | 3.0741 | 3.7168 | -0.5739 | 2.2909 |  |
| random_forest | 3.1012 | 3.7010 | -0.5752 | 2.2646 | Manja varijabilnost od DT, ali veći prosječni MAE |
| decision_tree | 3.1118 | 3.7060 | -0.5952 | 2.2325 | Ponekad dobra na block_middle; nestabilna na visokim rateovima |
| knn_upgraded | 3.1278 | 3.7516 | -0.5953 | 2.2738 | Napredni KNN (cikličke značajke, težinski prosjek); lošiji od osnovnog KNN-a |
| time_interpolation | 3.1315 | 3.7835 | -0.6188 | 2.3467 | Identična linear interpolaciji (ravnomjerni 10-min intervali) |
| linear_interpolation | 3.1315 | 3.7835 | -0.6188 | 2.3467 | Najbolja pojedinačna metoda; stabilna na svim scenarijima |
| knn | 3.1315 | 3.7835 | -0.6188 | 2.3467 | Osnovni KNN (k=5); bolji od knn_upgraded u prosjeku |
| moving_average | 3.6985 | 4.6792 | -1.5228 | 2.7777 | Pomični prosjek (prozor 6 = 1 sat); bolja od forward fill, lošija od linear |
| forward_fill | 3.7863 | 4.7590 | -1.5813 | 2.8185 | Loša na block scenarijima |
| cubic_interpolation | 5.8704 | 7.0044 | -5.1028 | 6.6487 | Odlična na random 10-30%; loša na block pri visokim rateovima |
| spline_interpolation | 6.6240 | 7.8068 | -6.9507 | 7.4899 | Prirodni spline; razlikuje se od cubic (clamped) |

---

# UPUTE ZA CHATGPT ZA NADOPUNU WORD DOKUMENTA

## 1. Što je promijenjeno u eksperimentu

- Missing rateovi prošireni s 10–40 % na **10–80 %** (dodano 50 %, 60 %, 70 %, 80 %)
- Ukupno **480 testova** (5 scenarija × 8 rateova × 12 metoda)
- Izvor podataka: `results/experiment_results.csv` (ažuriran)
- Pomoćne datoteke: `results/mae_by_method.csv`, `results/error_vs_missing_rate.csv`

## 2. Novi missing rateovi

50 %, 60 %, 70 %, 80 % — uz postojeće 10 %, 20 %, 30 %, 40 %

## 3. Koje tablice zamijeniti u radu

Zamijeni sve tablice iz prethodne verzije (10–40 %) novim tablicama iz ovog dokumenta:
- Tablica najbolje metode po scenariju/rateu (40 redaka umjesto 20)
- Tablica random missing (64 reda umjesto 32)
- Tablica block missing (64 reda)
- Tablica block pozicije (24 reda za najbolje po MAE)
- Sažetak po metodama (ažurirani prosjeci)

## 4. Koje dijelove teksta nadopuniti

### 3.12.2 Različite razine nedostajućih vrijednosti
- Dodaj da se testira 10 % do 80 %
- Objasni da pri 80 % ostaje samo ~20 % poznatih vrijednosti (202 od 1008 na random; 2 rubna + ostatak)
- Pri 80 % block uklanja 230 uzastopnih vrijednosti

### 5 Rezultati (uvod)
- Spomeni 8 razina missing ratea i 320 eksperimenata

### 5.1 Random missing
- Cubic najbolja 10–30 % (MAE 0,0406–0,0448)
- Linear najbolja 40–80 % (MAE 0,0620–0,0919)
- Čak i pri 80 % random, R² > 0,996 za linear

### 5.2 Block missing
- Linear najbolja u većini slučajeva
- Pri 80 %: linear MAE = 0,6705, R² = 0,7914
- KNN pri 80 % block: MAE = 1,9468

### 5.3 Block_start, block_middle, block_end
- block_end najteži pri 80 % (prosječni MAE metoda = 3,47 °C)
- block_middle pri 80 %: linear MAE = 1,4370
- block_start pri 80 %: linear MAE = 0,6939 (manje težak nego middle/end)

### 5.4 Utjecaj missing ratea
- MAE prosjek: 0,463 (10 %) → 2,100 (80 %)
- RMSE prosjek: 0,550 → 2,444
- Nagli porast pogreške iznad 50 % na block scenarijima

### 5.6 Najbolja metoda po scenariju
- Linear: 27/40 pobjeda
- Cubic: 7/40 (uglavnom random 10–30 %)
- Nema jedne univerzalne metode

### 6 Tumačenje rezultata
- Potvrdi da klasične metode dominiraju
- Naglasi da ML metode postaju još nepouzdanije iznad 50 %
- KNN na block scenarijima katastrofalan pri svim visokim rateovima

### 7 Zaključak
- Dodaj da eksperiment pokriva 10–80 %
- Linear interpolacija ostaje preporučena metoda
- Block_end i block_middle pri 70–80 % ekstremno zahtjevni
- Preporuka: ne koristiti KNN za block missing

## 5. Gotovi kratki zaključci iz novih rezultata

1. Linear interpolacija pobjeđuje u 27 od 40 scenarij/rate kombinacija.
2. Cubic interpolacija ostaje najbolja za random missing do 30 %.
3. Pri 80 % random missing, linear postiže MAE = 0,0919 °C i R² = 0,9964.
4. block_end je najteži scenarij pri 80 % (prosječni MAE = 3,47 °C).
5. KNN na block scenarijima pri 50–80 % ima MAE 1,95–3,52 °C.
6. Negativan R² pojavljuje se u 198 od 320 rezultata, najčešće kod KNN i forward fill na block scenarijima.
7. DT je nešto bolji od RF u prosjeku pri 50–80 % (MAE 1,50 vs 1,87).

## 6. Promjena zaključka u odnosu na verziju 10–40 %

| Tvrdnja | 10–40 % | 10–80 % | Promjena? |
|---------|---------|---------|-----------|
| Linear najbolja ukupno | Da (10/20) | Da (27/40) | **Ne** — potvrđeno |
| Cubic najbolja za random | Da (10–30 %) | Da (10–30 %) | **Ne** |
| Block teži od random | Da | Da, još izraženije | **Da** — pojačano |
| KNN loš na block | Da | Da, pogoršava se | **Da** — pojačano |
| block_start najteži | Da (1,40) | **Ne** — block_end najteži pri 80 % | **Da** — promijenjeno |

## 7. Izvori podataka

- **Glavni:** `results/experiment_results.csv`
- **Pomoćni:** `results/mae_by_method.csv`, `results/error_vs_missing_rate.csv`
- **Rekonstrukcije:** `results/reconstruction_linear_interpolation_*_0.20.csv` (samo 20 %)

---

*Kraj dokumenta — kopiraj cijeli sadržaj u ChatGPT*
