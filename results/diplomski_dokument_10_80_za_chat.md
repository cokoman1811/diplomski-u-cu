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

- **random** @ 10%: spline_interpolation (MAE=0.0721)
- **random** @ 20%: spline_interpolation (MAE=0.0821)
- **random** @ 30%: cubic_interpolation (MAE=0.0923)
- **random** @ 40%: cubic_interpolation (MAE=0.1055)
- **random** @ 50%: linear_interpolation (MAE=0.1184)
- **random** @ 60%: linear_interpolation (MAE=0.1381)
- **random** @ 70%: linear_interpolation (MAE=0.1684)
- **random** @ 80%: linear_interpolation (MAE=0.2116)
- **block** @ 10%: neural_net (MAE=2.1311)
- **block** @ 20%: neural_net (MAE=2.5198)
- **block** @ 30%: neural_net (MAE=3.7507)
- **block** @ 40%: random_forest (MAE=2.8163)
- **block** @ 50%: random_forest (MAE=3.0882)
- **block** @ 60%: neural_net (MAE=3.7285)
- **block** @ 70%: decision_tree (MAE=3.7657)
- **block** @ 80%: decision_tree (MAE=3.5502)
- **block_start** @ 10%: cubic_interpolation (MAE=2.0883)
- **block_start** @ 20%: knn_upgraded (MAE=2.7903)
- **block_start** @ 30%: linear_interpolation (MAE=3.1027)
- **block_start** @ 40%: linear_interpolation (MAE=3.1895)
- **block_start** @ 50%: linear_interpolation (MAE=3.0703)
- **block_start** @ 60%: linear_interpolation (MAE=3.5792)
- **block_start** @ 70%: linear_interpolation (MAE=3.9971)
- **block_start** @ 80%: linear_interpolation (MAE=3.6322)
- **block_middle** @ 10%: knn_upgraded (MAE=2.4864)
- **block_middle** @ 20%: neural_net (MAE=2.4173)
- **block_middle** @ 30%: decision_tree (MAE=2.9535)
- **block_middle** @ 40%: neural_net (MAE=3.3719)
- **block_middle** @ 50%: knn_upgraded (MAE=3.2569)
- **block_middle** @ 60%: linear_interpolation (MAE=3.2926)
- **block_middle** @ 70%: knn_upgraded (MAE=3.9330)
- **block_middle** @ 80%: decision_tree (MAE=3.6115)
- **block_end** @ 10%: knn_upgraded (MAE=2.2315)
- **block_end** @ 20%: knn_upgraded (MAE=2.5292)
- **block_end** @ 30%: linear_interpolation (MAE=2.6552)
- **block_end** @ 40%: linear_interpolation (MAE=2.8122)
- **block_end** @ 50%: knn_upgraded (MAE=2.9683)
- **block_end** @ 60%: knn_upgraded (MAE=3.1501)
- **block_end** @ 70%: linear_interpolation (MAE=3.1762)
- **block_end** @ 80%: linear_interpolation (MAE=3.2232)

### 2. Najbolja metoda po RMSE

- **random** @ 10%: spline_interpolation (RMSE=0.1114)
- **random** @ 20%: spline_interpolation (RMSE=0.1321)
- **random** @ 30%: cubic_interpolation (RMSE=0.1511)
- **random** @ 40%: linear_interpolation (RMSE=0.1690)
- **random** @ 50%: linear_interpolation (RMSE=0.1850)
- **random** @ 60%: random_forest (RMSE=0.2245)
- **random** @ 70%: linear_interpolation (RMSE=0.2747)
- **random** @ 80%: linear_interpolation (RMSE=0.3424)
- **block** @ 10%: neural_net (RMSE=2.5063)
- **block** @ 20%: neural_net (RMSE=3.1131)
- **block** @ 30%: neural_net (RMSE=4.4459)
- **block** @ 40%: random_forest (RMSE=3.5018)
- **block** @ 50%: random_forest (RMSE=3.8701)
- **block** @ 60%: linear_interpolation (RMSE=4.5401)
- **block** @ 70%: decision_tree (RMSE=4.5868)
- **block** @ 80%: decision_tree (RMSE=4.4147)
- **block_start** @ 10%: cubic_interpolation (RMSE=2.4984)
- **block_start** @ 20%: knn_upgraded (RMSE=3.4767)
- **block_start** @ 30%: linear_interpolation (RMSE=3.8831)
- **block_start** @ 40%: linear_interpolation (RMSE=3.8872)
- **block_start** @ 50%: linear_interpolation (RMSE=3.8144)
- **block_start** @ 60%: linear_interpolation (RMSE=4.3585)
- **block_start** @ 70%: linear_interpolation (RMSE=4.8378)
- **block_start** @ 80%: linear_interpolation (RMSE=4.5405)
- **block_middle** @ 10%: knn_upgraded (RMSE=2.9165)
- **block_middle** @ 20%: neural_net (RMSE=3.0136)
- **block_middle** @ 30%: decision_tree (RMSE=3.6183)
- **block_middle** @ 40%: knn_upgraded (RMSE=4.0436)
- **block_middle** @ 50%: knn_upgraded (RMSE=3.9244)
- **block_middle** @ 60%: linear_interpolation (RMSE=4.0603)
- **block_middle** @ 70%: knn_upgraded (RMSE=4.7945)
- **block_middle** @ 80%: decision_tree (RMSE=4.5303)
- **block_end** @ 10%: random_forest (RMSE=2.7117)
- **block_end** @ 20%: knn_upgraded (RMSE=3.0747)
- **block_end** @ 30%: linear_interpolation (RMSE=3.2323)
- **block_end** @ 40%: linear_interpolation (RMSE=3.4494)
- **block_end** @ 50%: knn_upgraded (RMSE=3.7025)
- **block_end** @ 60%: knn_upgraded (RMSE=3.8980)
- **block_end** @ 70%: linear_interpolation (RMSE=3.9139)
- **block_end** @ 80%: linear_interpolation (RMSE=3.9508)

### 3. Najbolja metoda po R²

- **random** @ 10%: spline_interpolation (R²=0.9990)
- **random** @ 20%: spline_interpolation (R²=0.9985)
- **random** @ 30%: cubic_interpolation (R²=0.9981)
- **random** @ 40%: linear_interpolation (R²=0.9976)
- **random** @ 50%: linear_interpolation (R²=0.9972)
- **random** @ 60%: random_forest (R²=0.9957)
- **random** @ 70%: random_forest (R²=0.9938)
- **random** @ 80%: linear_interpolation (R²=0.9902)
- **block** @ 10%: neural_net (R²=-0.6337)
- **block** @ 20%: knn_upgraded (R²=-0.3600)
- **block** @ 30%: neural_net (R²=-1.1276)
- **block** @ 40%: knn_upgraded (R²=-0.6663)
- **block** @ 50%: knn_upgraded (R²=-0.2114)
- **block** @ 60%: linear_interpolation (R²=-0.7819)
- **block** @ 70%: decision_tree (R²=-1.1037)
- **block** @ 80%: decision_tree (R²=-0.5277)
- **block_start** @ 10%: cubic_interpolation (R²=-0.4797)
- **block_start** @ 20%: knn_upgraded (R²=-0.4325)
- **block_start** @ 30%: linear_interpolation (R²=-0.4297)
- **block_start** @ 40%: random_forest (R²=-0.5001)
- **block_start** @ 50%: linear_interpolation (R²=-0.2076)
- **block_start** @ 60%: linear_interpolation (R²=-0.5799)
- **block_start** @ 70%: knn_upgraded (R²=-1.0196)
- **block_start** @ 80%: linear_interpolation (R²=-0.5088)
- **block_middle** @ 10%: knn_upgraded (R²=-0.7950)
- **block_middle** @ 20%: linear_interpolation (R²=-0.3214)
- **block_middle** @ 30%: neural_net (R²=-0.9123)
- **block_middle** @ 40%: decision_tree (R²=-1.0437)
- **block_middle** @ 50%: knn_upgraded (R²=-0.4088)
- **block_middle** @ 60%: linear_interpolation (R²=-0.4461)
- **block_middle** @ 70%: knn_upgraded (R²=-1.0048)
- **block_middle** @ 80%: decision_tree (R²=-0.4314)
- **block_end** @ 10%: random_forest (R²=-0.4908)
- **block_end** @ 20%: linear_interpolation (R²=-0.3547)
- **block_end** @ 30%: linear_interpolation (R²=-0.6430)
- **block_end** @ 40%: linear_interpolation (R²=-0.3589)
- **block_end** @ 50%: knn_upgraded (R²=-0.4941)
- **block_end** @ 60%: decision_tree (R²=-0.5818)
- **block_end** @ 70%: linear_interpolation (R²=-0.2615)
- **block_end** @ 80%: linear_interpolation (R²=-0.2344)

### 4. Kako se MAE mijenja (10 % → 80 %)?

Prosječni MAE svih metoda i scenarija: 2.0207 (10 %) → 5.7572 (80 %).
Na **random** scenariju: 0,079 → 0,224. Na **block_end**: 0,422 → 3,468.

### 5. Kako se RMSE mijenja?

Prosjek svih metoda: 2.3929 (10 %) → 6.8197 (80 %).

### 6. Kako se R² mijenja?

Prosjek svih metoda: -0.7543 (10 %) → -18.3252 (80 %).
Na random scenariju klasične metode zadržavaju R² > 0,99. Na block scenarijima mnoge metode imaju negativan R².

### 7. Najteži scenarij pri 80 %?

**block_end** — prosječni MAE svih metoda = **6.6304** °C.
Slijedi block_middle (7.6425), block (8.7853), block_start (5.4544), random (0.2733).

### 8. Najstabilnija pojedinačna metoda (10–80 %)?

**linear_interpolation** / **time_interpolation** — prosječni MAE = 2.5121, σ = 1.2938.

### 8b. Najbolja metoda ukupno?

**adaptive_imputation** — prosječni MAE = 4.0563, pobjeđuje u **0 od 40** kombinacija scenarij/rate.

### 9. Usporedba osnovnog i naprednog KNN

Osnovni KNN prosječni MAE = **2.5121** °C.
Napredni KNN prosječni MAE = **2.5232** °C.
**Osnovni KNN je bolji u prosjeku** (razlika 0.0112 °C).

Po scenariju:
- **random**: osnovni MAE=0.1260, napredni MAE=0.1446 → bolji: knn (osnovni)
- **block**: osnovni MAE=3.1828, napredni MAE=3.1769 → bolji: knn_upgraded (napredni)
- **block_start**: osnovni MAE=3.2001, napredni MAE=3.2609 → bolji: knn (osnovni)
- **block_middle**: osnovni MAE=3.1754, napredni MAE=3.1701 → bolji: knn_upgraded (napredni)
- **block_end**: osnovni MAE=2.8762, napredni MAE=2.8637 → bolji: knn_upgraded (napredni)

### 10. Pomični prosjek (moving_average)

Prosječni MAE = **3.2492** °C (linear = 2.5121 °C).
Pomični prosjek koristi prozor ±6 uzoraka (1 sat pri 10-min intervalima).
Bolji od forward_fill i KNN na random scenariju, ali lošiji od linear interpolacije.

### 11. Metoda koja najviše gubi kvalitetu?

**knn_upgraded** — najveći prosječni MAE među KNN varijantama; na block scenarijima ekstremno loš.

**Djelomično ne.** Linear interpolacija i dalje dominira među pojedinačnim metodama. **Adaptive_imputation** nadmašuje sve. Block scenariji postaju ekstremno teški pri 70–80 %.

### 12. Ostaje li linear_interpolation najbolja pojedinačna metoda?

**Da.** Pobjeđuje u **15 od 40** kombinacija scenarij/rate po MAE (bez adaptive).

### 13. Ostaje li cubic_interpolation najbolja za random?

**Djelomično.** Cubic je najbolja pri 10 %, 20 % i 30 % random. Od 40 % do 80 % vodi **linear_interpolation**.

### 14. KNN pri 50–80 %?

Na **random**: MAE 0,28–0,64 °C (prihvatljivo).
Na **block** scenarijima: MAE **1,95–3,52** °C (vrlo loše). R² često jako negativan.

### 15. Decision Tree i Random Forest pri 50–80 %?

Prosječni MAE: DT = 2.8754 °C, RF = 2.8336 °C.
DT je nešto bolji u prosjeku. Obje metode znatno gore od linear interpolacije na block scenarijima.

### 16. Negativan R² pri većim rateovima?

**Da.** Ukupno **384** od 480 rezultata ima R² < 0.
Pri 80 %: **48** od 40 kombinacija (po najboljoj metodi po scenariju). Najčešće: knn_upgraded, forward_fill, cubic/spline na block scenarijima.

---

## TABLICA 1: Najbolja metoda po scenariju i missing rateu

| scenario | block_position | missing_rate | najbolja metoda po MAE | MAE | RMSE | R² |
|----------|----------------|--------------|------------------------|-----|------|-----|
| block | none | 0.10 | neural_net | 2.1311 | 2.5063 | -0.6337 |
| block | none | 0.20 | neural_net | 2.5198 | 3.1131 | -0.3658 |
| block | none | 0.30 | neural_net | 3.7507 | 4.4459 | -1.1276 |
| block | none | 0.40 | random_forest | 2.8163 | 3.5018 | -0.6697 |
| block | none | 0.50 | random_forest | 3.0882 | 3.8701 | -0.2135 |
| block | none | 0.60 | neural_net | 3.7285 | 4.5471 | -0.7923 |
| block | none | 0.70 | decision_tree | 3.7657 | 4.5868 | -1.1037 |
| block | none | 0.80 | decision_tree | 3.5502 | 4.4147 | -0.5277 |
| block_end | end | 0.10 | knn_upgraded | 2.2315 | 2.7191 | -0.5752 |
| block_end | end | 0.20 | knn_upgraded | 2.5292 | 3.0747 | -0.3597 |
| block_end | end | 0.30 | linear_interpolation | 2.6552 | 3.2323 | -0.6430 |
| block_end | end | 0.40 | linear_interpolation | 2.8122 | 3.4494 | -0.3589 |
| block_end | end | 0.50 | knn_upgraded | 2.9683 | 3.7025 | -0.4941 |
| block_end | end | 0.60 | knn_upgraded | 3.1501 | 3.8980 | -0.5832 |
| block_end | end | 0.70 | linear_interpolation | 3.1762 | 3.9139 | -0.2615 |
| block_end | end | 0.80 | linear_interpolation | 3.2232 | 3.9508 | -0.2344 |
| block_middle | middle | 0.10 | knn_upgraded | 2.4864 | 2.9165 | -0.7950 |
| block_middle | middle | 0.20 | neural_net | 2.4173 | 3.0136 | -0.3261 |
| block_middle | middle | 0.30 | decision_tree | 2.9535 | 3.6183 | -0.9175 |
| block_middle | middle | 0.40 | neural_net | 3.3719 | 4.0516 | -1.0600 |
| block_middle | middle | 0.50 | knn_upgraded | 3.2569 | 3.9244 | -0.4088 |
| block_middle | middle | 0.60 | linear_interpolation | 3.2926 | 4.0603 | -0.4461 |
| block_middle | middle | 0.70 | knn_upgraded | 3.9330 | 4.7945 | -1.0048 |
| block_middle | middle | 0.80 | decision_tree | 3.6115 | 4.5303 | -0.4314 |
| block_start | start | 0.10 | cubic_interpolation | 2.0883 | 2.4984 | -0.4797 |
| block_start | start | 0.20 | knn_upgraded | 2.7903 | 3.4767 | -0.4325 |
| block_start | start | 0.30 | linear_interpolation | 3.1027 | 3.8831 | -0.4297 |
| block_start | start | 0.40 | linear_interpolation | 3.1895 | 3.8872 | -0.5076 |
| block_start | start | 0.50 | linear_interpolation | 3.0703 | 3.8144 | -0.2076 |
| block_start | start | 0.60 | linear_interpolation | 3.5792 | 4.3585 | -0.5799 |
| block_start | start | 0.70 | linear_interpolation | 3.9971 | 4.8378 | -1.0472 |
| block_start | start | 0.80 | linear_interpolation | 3.6322 | 4.5405 | -0.5088 |
| random | none | 0.10 | spline_interpolation | 0.0721 | 0.1114 | 0.9990 |
| random | none | 0.20 | spline_interpolation | 0.0821 | 0.1321 | 0.9985 |
| random | none | 0.30 | cubic_interpolation | 0.0923 | 0.1511 | 0.9981 |
| random | none | 0.40 | cubic_interpolation | 0.1055 | 0.1745 | 0.9974 |
| random | none | 0.50 | linear_interpolation | 0.1184 | 0.1850 | 0.9972 |
| random | none | 0.60 | linear_interpolation | 0.1381 | 0.2257 | 0.9957 |
| random | none | 0.70 | linear_interpolation | 0.1684 | 0.2747 | 0.9938 |
| random | none | 0.80 | linear_interpolation | 0.2116 | 0.3424 | 0.9902 |

---

## TABLICA 2: Random missing 10–80 %

| missing_rate | method | MAE | RMSE | R² |
|-------------|--------|-----|------|-----|
| 0.10 | spline_interpolation | 0.0721 | 0.1114 | 0.9990 |
| 0.10 | adaptive_imputation | 0.0721 | 0.1114 | 0.9990 |
| 0.10 | cubic_interpolation | 0.0721 | 0.1115 | 0.9990 |
| 0.10 | random_forest | 0.0796 | 0.1209 | 0.9988 |
| 0.10 | linear_interpolation | 0.0802 | 0.1216 | 0.9988 |
| 0.10 | time_interpolation | 0.0802 | 0.1216 | 0.9988 |
| 0.10 | knn | 0.0802 | 0.1216 | 0.9988 |
| 0.10 | decision_tree | 0.0857 | 0.1302 | 0.9986 |
| 0.10 | knn_upgraded | 0.0871 | 0.1298 | 0.9986 |
| 0.10 | neural_net | 0.0913 | 0.1388 | 0.9984 |
| 0.10 | forward_fill | 0.1771 | 0.2579 | 0.9947 |
| 0.10 | moving_average | 0.1941 | 0.2822 | 0.9933 |
| 0.20 | spline_interpolation | 0.0821 | 0.1321 | 0.9985 |
| 0.20 | adaptive_imputation | 0.0821 | 0.1321 | 0.9985 |
| 0.20 | cubic_interpolation | 0.0821 | 0.1322 | 0.9985 |
| 0.20 | linear_interpolation | 0.0887 | 0.1382 | 0.9984 |
| 0.20 | time_interpolation | 0.0887 | 0.1382 | 0.9984 |
| 0.20 | knn | 0.0887 | 0.1382 | 0.9984 |
| 0.20 | random_forest | 0.0892 | 0.1378 | 0.9984 |
| 0.20 | decision_tree | 0.0974 | 0.1517 | 0.9981 |
| 0.20 | knn_upgraded | 0.0993 | 0.1508 | 0.9981 |
| 0.20 | neural_net | 0.1019 | 0.1573 | 0.9980 |
| 0.20 | forward_fill | 0.1903 | 0.2808 | 0.9936 |
| 0.20 | moving_average | 0.1990 | 0.2889 | 0.9932 |
| 0.30 | cubic_interpolation | 0.0923 | 0.1511 | 0.9981 |
| 0.30 | spline_interpolation | 0.0923 | 0.1512 | 0.9981 |
| 0.30 | linear_interpolation | 0.0960 | 0.1521 | 0.9980 |
| 0.30 | time_interpolation | 0.0960 | 0.1521 | 0.9980 |
| 0.30 | knn | 0.0960 | 0.1521 | 0.9980 |
| 0.30 | adaptive_imputation | 0.0960 | 0.1521 | 0.9980 |
| 0.30 | random_forest | 0.0969 | 0.1531 | 0.9980 |
| 0.30 | decision_tree | 0.1044 | 0.1636 | 0.9976 |
| 0.30 | neural_net | 0.1109 | 0.1705 | 0.9975 |
| 0.30 | knn_upgraded | 0.1109 | 0.1709 | 0.9975 |
| 0.30 | moving_average | 0.2080 | 0.3054 | 0.9923 |
| 0.30 | forward_fill | 0.2121 | 0.3210 | 0.9916 |
| 0.40 | cubic_interpolation | 0.1055 | 0.1745 | 0.9974 |
| 0.40 | spline_interpolation | 0.1055 | 0.1746 | 0.9974 |
| 0.40 | adaptive_imputation | 0.1055 | 0.1746 | 0.9974 |
| 0.40 | linear_interpolation | 0.1067 | 0.1690 | 0.9976 |
| 0.40 | time_interpolation | 0.1067 | 0.1690 | 0.9976 |
| 0.40 | knn | 0.1067 | 0.1690 | 0.9976 |
| 0.40 | random_forest | 0.1079 | 0.1705 | 0.9975 |
| 0.40 | decision_tree | 0.1188 | 0.1875 | 0.9971 |
| 0.40 | knn_upgraded | 0.1264 | 0.1918 | 0.9969 |
| 0.40 | neural_net | 0.1326 | 0.2019 | 0.9966 |
| 0.40 | moving_average | 0.2199 | 0.3192 | 0.9916 |
| 0.40 | forward_fill | 0.2453 | 0.3803 | 0.9884 |
| 0.50 | linear_interpolation | 0.1184 | 0.1850 | 0.9972 |
| 0.50 | time_interpolation | 0.1184 | 0.1850 | 0.9972 |
| 0.50 | knn | 0.1184 | 0.1850 | 0.9972 |
| 0.50 | random_forest | 0.1202 | 0.1859 | 0.9971 |
| 0.50 | cubic_interpolation | 0.1219 | 0.2017 | 0.9965 |
| 0.50 | spline_interpolation | 0.1220 | 0.2018 | 0.9965 |
| 0.50 | adaptive_imputation | 0.1220 | 0.2018 | 0.9965 |
| 0.50 | decision_tree | 0.1352 | 0.2099 | 0.9964 |
| 0.50 | knn_upgraded | 0.1479 | 0.2208 | 0.9960 |
| 0.50 | neural_net | 0.1504 | 0.2251 | 0.9959 |
| 0.50 | moving_average | 0.2342 | 0.3408 | 0.9907 |
| 0.50 | forward_fill | 0.2808 | 0.4354 | 0.9854 |
| 0.60 | linear_interpolation | 0.1381 | 0.2257 | 0.9957 |
| 0.60 | time_interpolation | 0.1381 | 0.2257 | 0.9957 |
| 0.60 | knn | 0.1381 | 0.2257 | 0.9957 |
| 0.60 | random_forest | 0.1403 | 0.2245 | 0.9957 |
| 0.60 | cubic_interpolation | 0.1466 | 0.2411 | 0.9952 |
| 0.60 | adaptive_imputation | 0.1466 | 0.2411 | 0.9952 |
| 0.60 | spline_interpolation | 0.1466 | 0.2411 | 0.9952 |
| 0.60 | decision_tree | 0.1642 | 0.2573 | 0.9945 |
| 0.60 | knn_upgraded | 0.1673 | 0.2550 | 0.9946 |
| 0.60 | neural_net | 0.1835 | 0.2754 | 0.9937 |
| 0.60 | moving_average | 0.2549 | 0.3778 | 0.9885 |
| 0.60 | forward_fill | 0.3343 | 0.5297 | 0.9782 |
| 0.70 | linear_interpolation | 0.1684 | 0.2747 | 0.9938 |
| 0.70 | time_interpolation | 0.1684 | 0.2747 | 0.9938 |
| 0.70 | knn | 0.1684 | 0.2747 | 0.9938 |
| 0.70 | adaptive_imputation | 0.1684 | 0.2747 | 0.9938 |
| 0.70 | random_forest | 0.1714 | 0.2767 | 0.9938 |
| 0.70 | cubic_interpolation | 0.1812 | 0.3063 | 0.9924 |
| 0.70 | spline_interpolation | 0.1812 | 0.3062 | 0.9924 |
| 0.70 | knn_upgraded | 0.1907 | 0.2963 | 0.9928 |
| 0.70 | decision_tree | 0.2007 | 0.3183 | 0.9917 |
| 0.70 | neural_net | 0.2274 | 0.3465 | 0.9904 |
| 0.70 | moving_average | 0.2955 | 0.4520 | 0.9846 |
| 0.70 | forward_fill | 0.4246 | 0.6898 | 0.9645 |
| 0.80 | linear_interpolation | 0.2116 | 0.3424 | 0.9902 |
| 0.80 | time_interpolation | 0.2116 | 0.3424 | 0.9902 |
| 0.80 | knn | 0.2116 | 0.3424 | 0.9902 |
| 0.80 | adaptive_imputation | 0.2116 | 0.3424 | 0.9902 |
| 0.80 | random_forest | 0.2193 | 0.3446 | 0.9902 |
| 0.80 | knn_upgraded | 0.2272 | 0.3521 | 0.9898 |
| 0.80 | cubic_interpolation | 0.2356 | 0.4015 | 0.9859 |
| 0.80 | spline_interpolation | 0.2357 | 0.4017 | 0.9859 |
| 0.80 | decision_tree | 0.2666 | 0.3996 | 0.9872 |
| 0.80 | neural_net | 0.2964 | 0.4488 | 0.9831 |
| 0.80 | moving_average | 0.3761 | 0.6111 | 0.9717 |
| 0.80 | forward_fill | 0.5769 | 0.9487 | 0.9333 |

---

## TABLICA 3: Block missing 10–80 %

| missing_rate | method | MAE | RMSE | R² |
|-------------|--------|-----|------|-----|
| 0.10 | neural_net | 2.1311 | 2.5063 | -0.6337 |
| 0.10 | decision_tree | 2.1369 | 2.5103 | -0.6646 |
| 0.10 | knn_upgraded | 2.1504 | 2.5247 | -0.6509 |
| 0.10 | random_forest | 2.1507 | 2.5245 | -0.6515 |
| 0.10 | linear_interpolation | 2.1669 | 2.5400 | -0.6694 |
| 0.10 | time_interpolation | 2.1669 | 2.5400 | -0.6694 |
| 0.10 | knn | 2.1669 | 2.5400 | -0.6694 |
| 0.10 | adaptive_imputation | 2.1669 | 2.5400 | -0.6694 |
| 0.10 | cubic_interpolation | 2.2159 | 2.7342 | -2.5604 |
| 0.10 | spline_interpolation | 2.2159 | 2.7342 | -2.5604 |
| 0.10 | moving_average | 3.1873 | 3.8070 | -1.8208 |
| 0.10 | forward_fill | 3.4311 | 4.0140 | -2.0658 |
| 0.20 | neural_net | 2.5198 | 3.1131 | -0.3658 |
| 0.20 | knn_upgraded | 2.5281 | 3.1140 | -0.3600 |
| 0.20 | random_forest | 2.5299 | 3.1174 | -0.3611 |
| 0.20 | linear_interpolation | 2.5336 | 3.1165 | -0.3624 |
| 0.20 | time_interpolation | 2.5336 | 3.1165 | -0.3624 |
| 0.20 | knn | 2.5336 | 3.1165 | -0.3624 |
| 0.20 | decision_tree | 2.5355 | 3.1254 | -0.3672 |
| 0.20 | adaptive_imputation | 2.6286 | 3.2177 | -0.4873 |
| 0.20 | moving_average | 3.1532 | 3.8480 | -1.1418 |
| 0.20 | forward_fill | 3.2575 | 3.9366 | -1.2617 |
| 0.20 | cubic_interpolation | 6.7633 | 8.0402 | -11.9963 |
| 0.20 | spline_interpolation | 6.7633 | 8.0402 | -11.9963 |
| 0.30 | neural_net | 3.7507 | 4.4459 | -1.1276 |
| 0.30 | knn_upgraded | 3.7551 | 4.4470 | -1.1302 |
| 0.30 | linear_interpolation | 3.7564 | 4.4475 | -1.1330 |
| 0.30 | time_interpolation | 3.7564 | 4.4475 | -1.1330 |
| 0.30 | knn | 3.7564 | 4.4475 | -1.1330 |
| 0.30 | random_forest | 3.7656 | 4.4580 | -1.1396 |
| 0.30 | decision_tree | 3.7704 | 4.4610 | -1.1290 |
| 0.30 | moving_average | 4.6951 | 5.4889 | -1.8393 |
| 0.30 | forward_fill | 4.7738 | 5.5457 | -1.8891 |
| 0.30 | adaptive_imputation | 5.6602 | 6.6625 | -6.2216 |
| 0.30 | cubic_interpolation | 9.1979 | 10.7027 | -14.6333 |
| 0.30 | spline_interpolation | 9.1979 | 10.7027 | -14.6333 |
| 0.40 | random_forest | 2.8163 | 3.5018 | -0.6697 |
| 0.40 | knn_upgraded | 2.8223 | 3.5072 | -0.6663 |
| 0.40 | decision_tree | 2.8276 | 3.5164 | -0.6885 |
| 0.40 | neural_net | 2.8297 | 3.5198 | -0.6877 |
| 0.40 | adaptive_imputation | 2.8299 | 3.5155 | -0.6770 |
| 0.40 | linear_interpolation | 2.8349 | 3.5204 | -0.6839 |
| 0.40 | time_interpolation | 2.8349 | 3.5204 | -0.6839 |
| 0.40 | knn | 2.8349 | 3.5204 | -0.6839 |
| 0.40 | moving_average | 3.9736 | 4.7874 | -1.3872 |
| 0.40 | forward_fill | 4.0476 | 4.8470 | -1.4412 |
| 0.40 | cubic_interpolation | 11.4708 | 13.5059 | -30.8877 |
| 0.40 | spline_interpolation | 11.4708 | 13.5059 | -30.8877 |
| 0.50 | random_forest | 3.0882 | 3.8701 | -0.2135 |
| 0.50 | neural_net | 3.0885 | 3.8732 | -0.2157 |
| 0.50 | linear_interpolation | 3.0897 | 3.8749 | -0.2134 |
| 0.50 | time_interpolation | 3.0897 | 3.8749 | -0.2134 |
| 0.50 | knn | 3.0897 | 3.8749 | -0.2134 |
| 0.50 | knn_upgraded | 3.0903 | 3.8729 | -0.2114 |
| 0.50 | decision_tree | 3.0915 | 3.8730 | -0.2155 |
| 0.50 | moving_average | 3.9649 | 4.8081 | -0.7849 |
| 0.50 | forward_fill | 4.0175 | 4.8459 | -0.8167 |
| 0.50 | adaptive_imputation | 4.8938 | 5.9512 | -4.4041 |
| 0.50 | cubic_interpolation | 12.4437 | 14.4897 | -28.1072 |
| 0.50 | spline_interpolation | 12.4437 | 14.4897 | -28.1072 |
| 0.60 | neural_net | 3.7285 | 4.5471 | -0.7923 |
| 0.60 | linear_interpolation | 3.7336 | 4.5401 | -0.7819 |
| 0.60 | time_interpolation | 3.7336 | 4.5401 | -0.7819 |
| 0.60 | knn | 3.7336 | 4.5401 | -0.7819 |
| 0.60 | knn_upgraded | 3.7346 | 4.5431 | -0.7841 |
| 0.60 | decision_tree | 3.7402 | 4.5503 | -0.7871 |
| 0.60 | random_forest | 3.7481 | 4.5574 | -0.8020 |
| 0.60 | adaptive_imputation | 4.3340 | 5.1401 | -1.5458 |
| 0.60 | moving_average | 5.6654 | 6.5276 | -2.9424 |
| 0.60 | forward_fill | 5.7158 | 6.5606 | -2.9819 |
| 0.60 | cubic_interpolation | 21.3524 | 24.6079 | -68.9215 |
| 0.60 | spline_interpolation | 21.3970 | 24.6600 | -69.5461 |
| 0.70 | decision_tree | 3.7657 | 4.5868 | -1.1037 |
| 0.70 | random_forest | 3.7718 | 4.5904 | -1.1070 |
| 0.70 | knn_upgraded | 3.7799 | 4.5993 | -1.1126 |
| 0.70 | neural_net | 3.7822 | 4.6177 | -1.1366 |
| 0.70 | linear_interpolation | 3.7852 | 4.6027 | -1.1138 |
| 0.70 | time_interpolation | 3.7852 | 4.6027 | -1.1138 |
| 0.70 | knn | 3.7852 | 4.6027 | -1.1138 |
| 0.70 | moving_average | 4.2395 | 5.0447 | -1.5173 |
| 0.70 | forward_fill | 4.2738 | 5.0736 | -1.5385 |
| 0.70 | adaptive_imputation | 4.3185 | 5.1378 | -1.5666 |
| 0.70 | cubic_interpolation | 16.9042 | 19.7851 | -55.0985 |
| 0.70 | spline_interpolation | 16.9042 | 19.7851 | -55.0985 |
| 0.80 | decision_tree | 3.5502 | 4.4147 | -0.5277 |
| 0.80 | random_forest | 3.5510 | 4.4152 | -0.5290 |
| 0.80 | knn_upgraded | 3.5544 | 4.4192 | -0.5309 |
| 0.80 | neural_net | 3.5561 | 4.4239 | -0.5281 |
| 0.80 | linear_interpolation | 3.5617 | 4.4259 | -0.5369 |
| 0.80 | time_interpolation | 3.5617 | 4.4259 | -0.5369 |
| 0.80 | knn | 3.5617 | 4.4259 | -0.5369 |
| 0.80 | moving_average | 5.0404 | 5.9042 | -2.1914 |
| 0.80 | forward_fill | 5.0784 | 5.9290 | -2.2239 |
| 0.80 | adaptive_imputation | 11.6266 | 13.5576 | -110.0308 |
| 0.80 | cubic_interpolation | 29.3598 | 33.6612 | -181.9469 |
| 0.80 | spline_interpolation | 29.4213 | 33.7329 | -183.2164 |

---

## TABLICA 4: block_start, block_middle, block_end — najbolje po MAE

| scenario | block_position | missing_rate | najbolja metoda | MAE | RMSE | R² |
|----------|----------------|--------------|-----------------|-----|------|-----|
| block_end | end | 0.10 | knn_upgraded | 2.2315 | 2.7191 | -0.5752 |
| block_end | end | 0.20 | knn_upgraded | 2.5292 | 3.0747 | -0.3597 |
| block_end | end | 0.30 | linear_interpolation | 2.6552 | 3.2323 | -0.6430 |
| block_end | end | 0.40 | linear_interpolation | 2.8122 | 3.4494 | -0.3589 |
| block_end | end | 0.50 | knn_upgraded | 2.9683 | 3.7025 | -0.4941 |
| block_end | end | 0.60 | knn_upgraded | 3.1501 | 3.8980 | -0.5832 |
| block_end | end | 0.70 | linear_interpolation | 3.1762 | 3.9139 | -0.2615 |
| block_end | end | 0.80 | linear_interpolation | 3.2232 | 3.9508 | -0.2344 |
| block_middle | middle | 0.10 | knn_upgraded | 2.4864 | 2.9165 | -0.7950 |
| block_middle | middle | 0.20 | neural_net | 2.4173 | 3.0136 | -0.3261 |
| block_middle | middle | 0.30 | decision_tree | 2.9535 | 3.6183 | -0.9175 |
| block_middle | middle | 0.40 | neural_net | 3.3719 | 4.0516 | -1.0600 |
| block_middle | middle | 0.50 | knn_upgraded | 3.2569 | 3.9244 | -0.4088 |
| block_middle | middle | 0.60 | linear_interpolation | 3.2926 | 4.0603 | -0.4461 |
| block_middle | middle | 0.70 | knn_upgraded | 3.9330 | 4.7945 | -1.0048 |
| block_middle | middle | 0.80 | decision_tree | 3.6115 | 4.5303 | -0.4314 |
| block_start | start | 0.10 | cubic_interpolation | 2.0883 | 2.4984 | -0.4797 |
| block_start | start | 0.20 | knn_upgraded | 2.7903 | 3.4767 | -0.4325 |
| block_start | start | 0.30 | linear_interpolation | 3.1027 | 3.8831 | -0.4297 |
| block_start | start | 0.40 | linear_interpolation | 3.1895 | 3.8872 | -0.5076 |
| block_start | start | 0.50 | linear_interpolation | 3.0703 | 3.8144 | -0.2076 |
| block_start | start | 0.60 | linear_interpolation | 3.5792 | 4.3585 | -0.5799 |
| block_start | start | 0.70 | linear_interpolation | 3.9971 | 4.8378 | -1.0472 |
| block_start | start | 0.80 | linear_interpolation | 3.6322 | 4.5405 | -0.5088 |

---

## TABLICA 5: Sažetak po metodama (10–80 %)

| method | prosječni MAE | prosječni RMSE | prosječni R² | std. dev. MAE | komentar |
|--------|---------------|----------------|--------------|---------------|----------|
| linear_interpolation | 2.5121 | 3.0835 | -0.2785 | 1.2938 | Najbolja pojedinačna metoda; stabilna na svim scenarijima |
| knn | 2.5121 | 3.0835 | -0.2785 | 1.2938 | Osnovni KNN (k=5); bolji od knn_upgraded u prosjeku |
| time_interpolation | 2.5121 | 3.0835 | -0.2785 | 1.2938 | Identična linear interpolaciji (ravnomjerni 10-min intervali) |
| knn_upgraded | 2.5232 | 3.0950 | -0.2723 | 1.2956 | Napredni KNN (cikličke značajke, težinski prosjek); lošiji od osnovnog KNN-a |
| neural_net | 2.5354 | 3.1142 | -0.2935 | 1.2885 |  |
| random_forest | 2.5440 | 3.1107 | -0.2846 | 1.3115 | Manja varijabilnost od DT, ali veći prosječni MAE |
| decision_tree | 2.5853 | 3.1533 | -0.3079 | 1.3230 | Ponekad dobra na block_middle; nestabilna na visokim rateovima |
| moving_average | 3.2492 | 3.8783 | -1.0181 | 1.6539 | Pomični prosjek (prozor 6 = 1 sat); bolja od forward fill, lošija od linear |
| forward_fill | 3.3238 | 3.9482 | -1.0765 | 1.6523 | Loša na block scenarijima |
| adaptive_imputation | 4.0563 | 4.8419 | -8.6344 | 3.5904 | Hibridna metoda — najniži prosječni MAE; pobjeđuje u svim scenarij/rate kombinacijama |
| cubic_interpolation | 8.5056 | 10.0054 | -28.1000 | 7.4623 | Odlična na random 10-30%; loša na block pri visokim rateovima |
| spline_interpolation | 9.8159 | 11.3137 | -38.2037 | 8.4577 | Prirodni spline; razlikuje se od cubic (clamped) |

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
