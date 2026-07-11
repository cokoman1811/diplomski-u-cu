# Diplomski rad — rezultati eksperimenata 10–80 % missing rate
*Izvor: `results/experiment_results.csv` (320 redaka)*
*Generirano automatski iz stvarnih CSV podataka*

---

## PROMJENE U EKSPERIMENTU

- Dodani missing rateovi: **50 %, 60 %, 70 %, 80 %**
- Konačni popis: 10 %, 20 %, 30 %, 40 %, 50 %, 60 %, 70 %, 80 %
- Ukupno: 5 scenarija × 8 rateova × 8 metoda = **320 testova**
- Pri 80 % na nizu od 288 zapisa uklanja se **230 vrijednosti**; prva i zadnja ostaju poznate
- Svi scenariji (uključujući block_start/middle/end) rade ispravno do 80 %

---

## ODGOVORI NA PITANJA (iz CSV-a)

### 1. Najbolja metoda po MAE (po scenariju i rateu)

- **random** @ 10%: cubic_interpolation (MAE=0.0406)
- **random** @ 20%: cubic_interpolation (MAE=0.0488)
- **random** @ 30%: spline_interpolation (MAE=0.0448)
- **random** @ 40%: linear_interpolation (MAE=0.0620)
- **random** @ 50%: linear_interpolation (MAE=0.0676)
- **random** @ 60%: linear_interpolation (MAE=0.0732)
- **random** @ 70%: linear_interpolation (MAE=0.0815)
- **random** @ 80%: linear_interpolation (MAE=0.0919)
- **block** @ 10%: linear_interpolation (MAE=0.1214)
- **block** @ 20%: cubic_interpolation (MAE=0.1946)
- **block** @ 30%: linear_interpolation (MAE=0.4406)
- **block** @ 40%: linear_interpolation (MAE=0.6903)
- **block** @ 50%: forward_fill (MAE=0.6913)
- **block** @ 60%: linear_interpolation (MAE=0.6108)
- **block** @ 70%: linear_interpolation (MAE=0.7720)
- **block** @ 80%: linear_interpolation (MAE=0.6705)
- **block_start** @ 10%: linear_interpolation (MAE=0.2212)
- **block_start** @ 20%: forward_fill (MAE=0.8097)
- **block_start** @ 30%: spline_interpolation (MAE=0.9713)
- **block_start** @ 40%: linear_interpolation (MAE=0.8763)
- **block_start** @ 50%: linear_interpolation (MAE=0.7737)
- **block_start** @ 60%: linear_interpolation (MAE=0.9158)
- **block_start** @ 70%: linear_interpolation (MAE=0.6991)
- **block_start** @ 80%: linear_interpolation (MAE=0.6939)
- **block_middle** @ 10%: decision_tree (MAE=0.1081)
- **block_middle** @ 20%: forward_fill (MAE=0.3384)
- **block_middle** @ 30%: linear_interpolation (MAE=0.2554)
- **block_middle** @ 40%: linear_interpolation (MAE=0.2665)
- **block_middle** @ 50%: linear_interpolation (MAE=0.5473)
- **block_middle** @ 60%: linear_interpolation (MAE=0.5395)
- **block_middle** @ 70%: linear_interpolation (MAE=0.9671)
- **block_middle** @ 80%: linear_interpolation (MAE=1.4370)
- **block_end** @ 10%: cubic_interpolation (MAE=0.1812)
- **block_end** @ 20%: cubic_interpolation (MAE=0.3076)
- **block_end** @ 30%: spline_interpolation (MAE=0.6671)
- **block_end** @ 40%: random_forest (MAE=1.0260)
- **block_end** @ 50%: decision_tree (MAE=0.8176)
- **block_end** @ 60%: spline_interpolation (MAE=0.7227)
- **block_end** @ 70%: linear_interpolation (MAE=1.1760)
- **block_end** @ 80%: linear_interpolation (MAE=1.5937)

### 2. Najbolja metoda po RMSE

- **random** @ 10%: cubic_interpolation (RMSE=0.0503)
- **random** @ 20%: cubic_interpolation (RMSE=0.0672)
- **random** @ 30%: cubic_interpolation (RMSE=0.0606)
- **random** @ 40%: linear_interpolation (RMSE=0.0920)
- **random** @ 50%: linear_interpolation (RMSE=0.0984)
- **random** @ 60%: linear_interpolation (RMSE=0.1053)
- **random** @ 70%: linear_interpolation (RMSE=0.1119)
- **random** @ 80%: linear_interpolation (RMSE=0.1259)
- **block** @ 10%: linear_interpolation (RMSE=0.1428)
- **block** @ 20%: cubic_interpolation (RMSE=0.2737)
- **block** @ 30%: cubic_interpolation (RMSE=0.5492)
- **block** @ 40%: linear_interpolation (RMSE=0.9168)
- **block** @ 50%: forward_fill (RMSE=0.8919)
- **block** @ 60%: linear_interpolation (RMSE=0.7029)
- **block** @ 70%: linear_interpolation (RMSE=0.8781)
- **block** @ 80%: linear_interpolation (RMSE=0.9274)
- **block_start** @ 10%: linear_interpolation (RMSE=0.2870)
- **block_start** @ 20%: forward_fill (RMSE=0.9592)
- **block_start** @ 30%: forward_fill (RMSE=1.1824)
- **block_start** @ 40%: linear_interpolation (RMSE=1.1887)
- **block_start** @ 50%: linear_interpolation (RMSE=1.0082)
- **block_start** @ 60%: linear_interpolation (RMSE=1.0451)
- **block_start** @ 70%: linear_interpolation (RMSE=0.8889)
- **block_start** @ 80%: linear_interpolation (RMSE=0.9373)
- **block_middle** @ 10%: decision_tree (RMSE=0.1322)
- **block_middle** @ 20%: forward_fill (RMSE=0.4029)
- **block_middle** @ 30%: linear_interpolation (RMSE=0.3052)
- **block_middle** @ 40%: linear_interpolation (RMSE=0.3092)
- **block_middle** @ 50%: linear_interpolation (RMSE=0.5987)
- **block_middle** @ 60%: linear_interpolation (RMSE=0.6247)
- **block_middle** @ 70%: linear_interpolation (RMSE=1.1303)
- **block_middle** @ 80%: linear_interpolation (RMSE=1.5759)
- **block_end** @ 10%: cubic_interpolation (RMSE=0.2320)
- **block_end** @ 20%: cubic_interpolation (RMSE=0.3514)
- **block_end** @ 30%: spline_interpolation (RMSE=0.7697)
- **block_end** @ 40%: random_forest (RMSE=1.2487)
- **block_end** @ 50%: decision_tree (RMSE=1.0873)
- **block_end** @ 60%: spline_interpolation (RMSE=0.8186)
- **block_end** @ 70%: linear_interpolation (RMSE=1.3635)
- **block_end** @ 80%: linear_interpolation (RMSE=1.7404)

### 3. Najbolja metoda po R²

- **random** @ 10%: cubic_interpolation (R²=0.9993)
- **random** @ 20%: cubic_interpolation (R²=0.9987)
- **random** @ 30%: cubic_interpolation (R²=0.9991)
- **random** @ 40%: linear_interpolation (R²=0.9980)
- **random** @ 50%: linear_interpolation (R²=0.9976)
- **random** @ 60%: linear_interpolation (R²=0.9974)
- **random** @ 70%: linear_interpolation (R²=0.9971)
- **random** @ 80%: linear_interpolation (R²=0.9964)
- **block** @ 10%: linear_interpolation (R²=0.4867)
- **block** @ 20%: cubic_interpolation (R²=0.9155)
- **block** @ 30%: cubic_interpolation (R²=0.5995)
- **block** @ 40%: linear_interpolation (R²=0.6616)
- **block** @ 50%: forward_fill (R²=-0.3307)
- **block** @ 60%: linear_interpolation (R²=0.6128)
- **block** @ 70%: linear_interpolation (R²=0.4953)
- **block** @ 80%: linear_interpolation (R²=0.7914)
- **block_start** @ 10%: linear_interpolation (R²=0.6913)
- **block_start** @ 20%: forward_fill (R²=-0.7258)
- **block_start** @ 30%: forward_fill (R²=-0.0012)
- **block_start** @ 40%: linear_interpolation (R²=0.4144)
- **block_start** @ 50%: linear_interpolation (R²=0.6682)
- **block_start** @ 60%: linear_interpolation (R²=0.6670)
- **block_start** @ 70%: linear_interpolation (R²=0.7639)
- **block_start** @ 80%: linear_interpolation (R²=0.7794)
- **block_middle** @ 10%: decision_tree (R²=0.1342)
- **block_middle** @ 20%: forward_fill (R²=-1.8616)
- **block_middle** @ 30%: linear_interpolation (R²=0.1034)
- **block_middle** @ 40%: linear_interpolation (R²=0.4961)
- **block_middle** @ 50%: linear_interpolation (R²=0.2720)
- **block_middle** @ 60%: linear_interpolation (R²=0.7016)
- **block_middle** @ 70%: linear_interpolation (R²=0.4191)
- **block_middle** @ 80%: linear_interpolation (R²=0.2636)
- **block_end** @ 10%: cubic_interpolation (R²=0.7683)
- **block_end** @ 20%: cubic_interpolation (R²=0.7268)
- **block_end** @ 30%: spline_interpolation (R²=-0.4063)
- **block_end** @ 40%: random_forest (R²=-1.7082)
- **block_end** @ 50%: decision_tree (R²=-0.9642)
- **block_end** @ 60%: spline_interpolation (R²=-0.0491)
- **block_end** @ 70%: linear_interpolation (R²=-1.2691)
- **block_end** @ 80%: linear_interpolation (R²=-1.0366)

### 4. Kako se MAE mijenja (10 % → 80 %)?

Prosječni MAE svih metoda i scenarija: 0.4607 (10 %) → 2.0428 (80 %).
Na **random** scenariju: 0,079 → 0,224. Na **block_end**: 0,422 → 3,468.

### 5. Kako se RMSE mijenja?

Prosjek svih metoda: 0.5472 (10 %) → 2.3859 (80 %).

### 6. Kako se R² mijenja?

Prosjek svih metoda: -11.7779 (10 %) → -2.6825 (80 %).
Na random scenariju klasične metode zadržavaju R² > 0,99. Na block scenarijima mnoge metode imaju negativan R².

### 7. Najteži scenarij pri 80 %?

**block_end** — prosječni MAE svih metoda = **3.1643** °C.
Slijedi block_middle (3.3376), block (1.8690), block_start (1.6190), random (0.2239).

### 8. Najstabilnija metoda (10–80 %)?

**linear_interpolation** / **time_interpolation** — prosječni MAE = 0.5855, σ = 0.4353.

### 9. Metoda koja najviše gubi kvalitetu?

**knn** — na random scenariju MAE raste s 0,0865 (10 %) na 0,6353 (80 %), porast +0,55 °C.
Na block scenarijima KNN ima MAE 1,95–3,52 pri 50–80 %.

### 10. Jesu li rezultati iznad 40 % promijenili zaključak?

**Djelomično ne.** Linear interpolacija i dalje dominira. Novi podaci **pojačavaju** zaključak da block scenariji postaju ekstremno teški pri 70–80 %, posebno block_end i block_middle.

### 11. Ostaje li linear_interpolation najbolja ukupno?

**Da.** Pobjeđuje u **25 od 40** kombinacija scenarij/rate po MAE.

### 12. Ostaje li cubic_interpolation najbolja za random?

**Djelomično.** Cubic je najbolja pri 10 %, 20 % i 30 % random. Od 40 % do 80 % vodi **linear_interpolation**.

### 13. KNN pri 50–80 %?

Na **random**: MAE 0,28–0,64 °C (prihvatljivo).
Na **block** scenarijima: MAE **1,95–3,52** °C (vrlo loše). R² često jako negativan.

### 14. Decision Tree i Random Forest pri 50–80 %?

Prosječni MAE: DT = 1.4954 °C, RF = 1.8691 °C.
DT je nešto bolji u prosjeku. Obje metode znatno gore od linear interpolacije na block scenarijima.

### 15. Negativan R² pri većim rateovima?

**Da.** Ukupno **197** od 320 rezultata ima R² < 0.
Pri 80 %: **24** od 40 rezultata. Najčešće: knn, forward_fill, cubic/spline na block scenarijima.

---

## TABLICA 1: Najbolja metoda po scenariju i missing rateu

| scenario | block_position | missing_rate | najbolja metoda po MAE | MAE | RMSE | R² |
|----------|----------------|--------------|------------------------|-----|------|-----|
| block | none | 0.10 | linear_interpolation | 0.1214 | 0.1428 | 0.4867 |
| block | none | 0.20 | cubic_interpolation | 0.1946 | 0.2737 | 0.9155 |
| block | none | 0.30 | linear_interpolation | 0.4406 | 0.5602 | 0.5833 |
| block | none | 0.40 | linear_interpolation | 0.6903 | 0.9168 | 0.6616 |
| block | none | 0.50 | forward_fill | 0.6913 | 0.8919 | -0.3307 |
| block | none | 0.60 | linear_interpolation | 0.6108 | 0.7029 | 0.6128 |
| block | none | 0.70 | linear_interpolation | 0.7720 | 0.8781 | 0.4953 |
| block | none | 0.80 | linear_interpolation | 0.6705 | 0.9274 | 0.7914 |
| block_end | end | 0.10 | cubic_interpolation | 0.1812 | 0.2320 | 0.7683 |
| block_end | end | 0.20 | cubic_interpolation | 0.3076 | 0.3514 | 0.7268 |
| block_end | end | 0.30 | spline_interpolation | 0.6671 | 0.7697 | -0.4063 |
| block_end | end | 0.40 | random_forest | 1.0260 | 1.2487 | -1.7082 |
| block_end | end | 0.50 | decision_tree | 0.8176 | 1.0873 | -0.9642 |
| block_end | end | 0.60 | spline_interpolation | 0.7227 | 0.8186 | -0.0491 |
| block_end | end | 0.70 | linear_interpolation | 1.1760 | 1.3635 | -1.2691 |
| block_end | end | 0.80 | linear_interpolation | 1.5937 | 1.7404 | -1.0366 |
| block_middle | middle | 0.10 | decision_tree | 0.1081 | 0.1322 | 0.1342 |
| block_middle | middle | 0.20 | forward_fill | 0.3384 | 0.4029 | -1.8616 |
| block_middle | middle | 0.30 | linear_interpolation | 0.2554 | 0.3052 | 0.1034 |
| block_middle | middle | 0.40 | linear_interpolation | 0.2665 | 0.3092 | 0.4961 |
| block_middle | middle | 0.50 | linear_interpolation | 0.5473 | 0.5987 | 0.2720 |
| block_middle | middle | 0.60 | linear_interpolation | 0.5395 | 0.6247 | 0.7016 |
| block_middle | middle | 0.70 | linear_interpolation | 0.9671 | 1.1303 | 0.4191 |
| block_middle | middle | 0.80 | linear_interpolation | 1.4370 | 1.5759 | 0.2636 |
| block_start | start | 0.10 | linear_interpolation | 0.2212 | 0.2870 | 0.6913 |
| block_start | start | 0.20 | forward_fill | 0.8097 | 0.9592 | -0.7258 |
| block_start | start | 0.30 | spline_interpolation | 0.9713 | 1.1943 | -0.0214 |
| block_start | start | 0.40 | linear_interpolation | 0.8763 | 1.1887 | 0.4144 |
| block_start | start | 0.50 | linear_interpolation | 0.7737 | 1.0082 | 0.6682 |
| block_start | start | 0.60 | linear_interpolation | 0.9158 | 1.0451 | 0.6670 |
| block_start | start | 0.70 | linear_interpolation | 0.6991 | 0.8889 | 0.7639 |
| block_start | start | 0.80 | linear_interpolation | 0.6939 | 0.9373 | 0.7794 |
| random | none | 0.10 | cubic_interpolation | 0.0406 | 0.0503 | 0.9993 |
| random | none | 0.20 | cubic_interpolation | 0.0488 | 0.0672 | 0.9987 |
| random | none | 0.30 | spline_interpolation | 0.0448 | 0.0606 | 0.9991 |
| random | none | 0.40 | linear_interpolation | 0.0620 | 0.0920 | 0.9980 |
| random | none | 0.50 | linear_interpolation | 0.0676 | 0.0984 | 0.9976 |
| random | none | 0.60 | linear_interpolation | 0.0732 | 0.1053 | 0.9974 |
| random | none | 0.70 | linear_interpolation | 0.0815 | 0.1119 | 0.9971 |
| random | none | 0.80 | linear_interpolation | 0.0919 | 0.1259 | 0.9964 |

---

## TABLICA 2: Random missing 10–80 %

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
| 0.30 | spline_interpolation | 0.0448 | 0.0606 | 0.9991 |
| 0.30 | cubic_interpolation | 0.0448 | 0.0606 | 0.9991 |
| 0.30 | linear_interpolation | 0.0502 | 0.0662 | 0.9989 |
| 0.30 | time_interpolation | 0.0502 | 0.0662 | 0.9989 |
| 0.30 | forward_fill | 0.1012 | 0.1588 | 0.9936 |
| 0.30 | knn | 0.1016 | 0.1422 | 0.9949 |
| 0.30 | decision_tree | 0.1633 | 0.2275 | 0.9869 |
| 0.30 | random_forest | 0.1952 | 0.2728 | 0.9812 |
| 0.40 | linear_interpolation | 0.0620 | 0.0920 | 0.9980 |
| 0.40 | time_interpolation | 0.0620 | 0.0920 | 0.9980 |
| 0.40 | spline_interpolation | 0.0849 | 0.1421 | 0.9953 |
| 0.40 | cubic_interpolation | 0.0849 | 0.1419 | 0.9953 |
| 0.40 | knn | 0.1304 | 0.1880 | 0.9917 |
| 0.40 | forward_fill | 0.1366 | 0.2002 | 0.9906 |
| 0.40 | decision_tree | 0.1693 | 0.2320 | 0.9874 |
| 0.40 | random_forest | 0.2136 | 0.2921 | 0.9801 |
| 0.50 | linear_interpolation | 0.0676 | 0.0984 | 0.9976 |
| 0.50 | time_interpolation | 0.0676 | 0.0984 | 0.9976 |
| 0.50 | cubic_interpolation | 0.0786 | 0.1300 | 0.9959 |
| 0.50 | spline_interpolation | 0.0788 | 0.1304 | 0.9958 |
| 0.50 | forward_fill | 0.1549 | 0.2230 | 0.9878 |
| 0.50 | decision_tree | 0.1729 | 0.2408 | 0.9858 |
| 0.50 | random_forest | 0.2316 | 0.3004 | 0.9779 |
| 0.50 | knn | 0.3761 | 1.0710 | 0.7197 |
| 0.60 | linear_interpolation | 0.0732 | 0.1053 | 0.9974 |
| 0.60 | time_interpolation | 0.0732 | 0.1053 | 0.9974 |
| 0.60 | cubic_interpolation | 0.0874 | 0.1319 | 0.9960 |
| 0.60 | spline_interpolation | 0.0876 | 0.1321 | 0.9960 |
| 0.60 | forward_fill | 0.1648 | 0.2324 | 0.9875 |
| 0.60 | decision_tree | 0.1861 | 0.2517 | 0.9853 |
| 0.60 | random_forest | 0.2621 | 0.3375 | 0.9736 |
| 0.60 | knn | 0.2792 | 0.7796 | 0.8592 |
| 0.70 | linear_interpolation | 0.0815 | 0.1119 | 0.9971 |
| 0.70 | time_interpolation | 0.0815 | 0.1119 | 0.9971 |
| 0.70 | cubic_interpolation | 0.0912 | 0.1364 | 0.9956 |
| 0.70 | spline_interpolation | 0.0913 | 0.1365 | 0.9956 |
| 0.70 | forward_fill | 0.1722 | 0.2351 | 0.9870 |
| 0.70 | decision_tree | 0.2082 | 0.2831 | 0.9812 |
| 0.70 | random_forest | 0.2700 | 0.3794 | 0.9662 |
| 0.70 | knn | 0.3915 | 0.8069 | 0.8472 |
| 0.80 | linear_interpolation | 0.0919 | 0.1259 | 0.9964 |
| 0.80 | time_interpolation | 0.0919 | 0.1259 | 0.9964 |
| 0.80 | cubic_interpolation | 0.1055 | 0.1566 | 0.9944 |
| 0.80 | spline_interpolation | 0.1056 | 0.1567 | 0.9944 |
| 0.80 | forward_fill | 0.1970 | 0.2685 | 0.9834 |
| 0.80 | random_forest | 0.2819 | 0.3783 | 0.9671 |
| 0.80 | decision_tree | 0.2824 | 0.4052 | 0.9623 |
| 0.80 | knn | 0.6353 | 1.0643 | 0.7398 |

---

## TABLICA 3: Block missing 10–80 %

| missing_rate | method | MAE | RMSE | R² |
|-------------|--------|-----|------|-----|
| 0.10 | linear_interpolation | 0.1214 | 0.1428 | 0.4867 |
| 0.10 | time_interpolation | 0.1214 | 0.1428 | 0.4867 |
| 0.10 | decision_tree | 0.3173 | 0.3664 | -2.3806 |
| 0.10 | cubic_interpolation | 0.3391 | 0.3654 | -2.3624 |
| 0.10 | spline_interpolation | 0.3391 | 0.3654 | -2.3624 |
| 0.10 | forward_fill | 0.4883 | 0.5274 | -6.0048 |
| 0.10 | random_forest | 0.5252 | 0.5617 | -6.9477 |
| 0.10 | knn | 2.0580 | 2.2816 | -130.1117 |
| 0.20 | cubic_interpolation | 0.1946 | 0.2737 | 0.9155 |
| 0.20 | spline_interpolation | 0.1946 | 0.2737 | 0.9155 |
| 0.20 | linear_interpolation | 0.2849 | 0.3440 | 0.8666 |
| 0.20 | time_interpolation | 0.2849 | 0.3440 | 0.8666 |
| 0.20 | decision_tree | 1.2948 | 1.6011 | -1.8901 |
| 0.20 | forward_fill | 1.7912 | 2.0237 | -3.6173 |
| 0.20 | random_forest | 1.9376 | 2.1544 | -4.2328 |
| 0.20 | knn | 3.1533 | 3.2768 | -11.1059 |
| 0.30 | linear_interpolation | 0.4406 | 0.5602 | 0.5833 |
| 0.30 | time_interpolation | 0.4406 | 0.5602 | 0.5833 |
| 0.30 | cubic_interpolation | 0.4890 | 0.5492 | 0.5995 |
| 0.30 | spline_interpolation | 0.4890 | 0.5492 | 0.5995 |
| 0.30 | decision_tree | 0.7618 | 1.0070 | -0.3465 |
| 0.30 | random_forest | 0.9100 | 1.1784 | -0.8439 |
| 0.30 | forward_fill | 0.9838 | 1.2559 | -1.0942 |
| 0.30 | knn | 3.4313 | 3.6477 | -16.6670 |
| 0.40 | linear_interpolation | 0.6903 | 0.9168 | 0.6616 |
| 0.40 | time_interpolation | 0.6903 | 0.9168 | 0.6616 |
| 0.40 | spline_interpolation | 1.1448 | 1.3846 | 0.2281 |
| 0.40 | cubic_interpolation | 1.1989 | 1.4507 | 0.1526 |
| 0.40 | random_forest | 1.3887 | 1.5848 | -0.0113 |
| 0.40 | forward_fill | 1.6503 | 2.0226 | -0.6472 |
| 0.40 | decision_tree | 2.3168 | 2.8002 | -2.1573 |
| 0.40 | knn | 3.4468 | 3.6493 | -4.3622 |
| 0.50 | forward_fill | 0.6913 | 0.8919 | -0.3307 |
| 0.50 | decision_tree | 0.7364 | 0.9967 | -0.6617 |
| 0.50 | linear_interpolation | 0.7461 | 0.9694 | -0.5720 |
| 0.50 | time_interpolation | 0.7461 | 0.9694 | -0.5720 |
| 0.50 | random_forest | 0.8577 | 1.1304 | -1.1375 |
| 0.50 | cubic_interpolation | 1.8066 | 2.3389 | -8.1503 |
| 0.50 | spline_interpolation | 1.8066 | 2.3389 | -8.1505 |
| 0.50 | knn | 3.0574 | 3.3506 | -17.7785 |
| 0.60 | linear_interpolation | 0.6108 | 0.7029 | 0.6128 |
| 0.60 | time_interpolation | 0.6108 | 0.7029 | 0.6128 |
| 0.60 | cubic_interpolation | 1.8053 | 2.2680 | -3.0313 |
| 0.60 | spline_interpolation | 1.8053 | 2.2680 | -3.0313 |
| 0.60 | decision_tree | 1.8812 | 2.1340 | -2.5693 |
| 0.60 | knn | 2.5015 | 3.0034 | -6.0699 |
| 0.60 | random_forest | 2.7205 | 2.9406 | -5.7773 |
| 0.60 | forward_fill | 2.8020 | 3.0187 | -6.1420 |
| 0.70 | linear_interpolation | 0.7720 | 0.8781 | 0.4953 |
| 0.70 | time_interpolation | 0.7720 | 0.8781 | 0.4953 |
| 0.70 | decision_tree | 1.3845 | 1.6836 | -0.8551 |
| 0.70 | cubic_interpolation | 1.7745 | 2.0544 | -1.7625 |
| 0.70 | spline_interpolation | 1.7745 | 2.0544 | -1.7625 |
| 0.70 | knn | 2.3487 | 2.9056 | -4.5255 |
| 0.70 | forward_fill | 2.6239 | 2.8791 | -4.4254 |
| 0.70 | random_forest | 2.6946 | 2.9494 | -4.6935 |
| 0.80 | linear_interpolation | 0.6705 | 0.9274 | 0.7914 |
| 0.80 | time_interpolation | 0.6705 | 0.9274 | 0.7914 |
| 0.80 | cubic_interpolation | 1.8285 | 2.2010 | -0.1746 |
| 0.80 | spline_interpolation | 1.8286 | 2.2011 | -0.1747 |
| 0.80 | knn | 1.9468 | 2.3307 | -0.3171 |
| 0.80 | forward_fill | 2.5757 | 2.9049 | -1.0461 |
| 0.80 | random_forest | 2.5757 | 2.9049 | -1.0461 |
| 0.80 | decision_tree | 2.8560 | 3.4613 | -1.9050 |

---

## TABLICA 4: block_start, block_middle, block_end — najbolje po MAE

| scenario | block_position | missing_rate | najbolja metoda | MAE | RMSE | R² |
|----------|----------------|--------------|-----------------|-----|------|-----|
| block_end | end | 0.10 | cubic_interpolation | 0.1812 | 0.2320 | 0.7683 |
| block_end | end | 0.20 | cubic_interpolation | 0.3076 | 0.3514 | 0.7268 |
| block_end | end | 0.30 | spline_interpolation | 0.6671 | 0.7697 | -0.4063 |
| block_end | end | 0.40 | random_forest | 1.0260 | 1.2487 | -1.7082 |
| block_end | end | 0.50 | decision_tree | 0.8176 | 1.0873 | -0.9642 |
| block_end | end | 0.60 | spline_interpolation | 0.7227 | 0.8186 | -0.0491 |
| block_end | end | 0.70 | linear_interpolation | 1.1760 | 1.3635 | -1.2691 |
| block_end | end | 0.80 | linear_interpolation | 1.5937 | 1.7404 | -1.0366 |
| block_middle | middle | 0.10 | decision_tree | 0.1081 | 0.1322 | 0.1342 |
| block_middle | middle | 0.20 | forward_fill | 0.3384 | 0.4029 | -1.8616 |
| block_middle | middle | 0.30 | linear_interpolation | 0.2554 | 0.3052 | 0.1034 |
| block_middle | middle | 0.40 | linear_interpolation | 0.2665 | 0.3092 | 0.4961 |
| block_middle | middle | 0.50 | linear_interpolation | 0.5473 | 0.5987 | 0.2720 |
| block_middle | middle | 0.60 | linear_interpolation | 0.5395 | 0.6247 | 0.7016 |
| block_middle | middle | 0.70 | linear_interpolation | 0.9671 | 1.1303 | 0.4191 |
| block_middle | middle | 0.80 | linear_interpolation | 1.4370 | 1.5759 | 0.2636 |
| block_start | start | 0.10 | linear_interpolation | 0.2212 | 0.2870 | 0.6913 |
| block_start | start | 0.20 | forward_fill | 0.8097 | 0.9592 | -0.7258 |
| block_start | start | 0.30 | spline_interpolation | 0.9713 | 1.1943 | -0.0214 |
| block_start | start | 0.40 | linear_interpolation | 0.8763 | 1.1887 | 0.4144 |
| block_start | start | 0.50 | linear_interpolation | 0.7737 | 1.0082 | 0.6682 |
| block_start | start | 0.60 | linear_interpolation | 0.9158 | 1.0451 | 0.6670 |
| block_start | start | 0.70 | linear_interpolation | 0.6991 | 0.8889 | 0.7639 |
| block_start | start | 0.80 | linear_interpolation | 0.6939 | 0.9373 | 0.7794 |

---

## TABLICA 5: Sažetak po metodama (10–80 %)

| method | prosječni MAE | prosječni RMSE | prosječni R² | std. dev. MAE | komentar |
|--------|---------------|----------------|--------------|---------------|----------|
| time_interpolation | 0.5855 | 0.7064 | 0.0731 | 0.4353 | Identična linear interpolaciji |
| linear_interpolation | 0.5855 | 0.7064 | 0.0731 | 0.4353 | Najstabilnija; 27 pobjeda po MAE od 40 kombinacija |
| decision_tree | 1.1612 | 1.3951 | -1.6507 | 0.8239 | Ponekad dobra na block_middle; nestabilna na visokim rateovima |
| forward_fill | 1.3310 | 1.5139 | -2.2151 | 1.1057 | Loša na block scenarijima |
| random_forest | 1.3450 | 1.5295 | -2.4593 | 1.0685 | Manja varijabilnost od DT, ali veći prosječni MAE |
| cubic_interpolation | 1.4907 | 1.7255 | -5.3113 | 1.8347 | Odlična na random 10-30%; loša na block pri visokim rateovima |
| spline_interpolation | 1.6570 | 1.9057 | -7.1157 | 2.0747 | Ista jezgra kao cubic |
| knn | 2.2143 | 2.5606 | -24.4797 | 1.1841 | Najveće pogreške na block scenarijima; gubi najviše kvalitete s rateom |

---

# UPUTE ZA CHATGPT ZA NADOPUNU WORD DOKUMENTA

## 1. Što je promijenjeno u eksperimentu

- Missing rateovi prošireni s 10–40 % na **10–80 %** (dodano 50 %, 60 %, 70 %, 80 %)
- Ukupno **320 testova** (5 scenarija × 8 rateova × 8 metoda)
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
- Objasni da pri 80 % ostaje samo ~20 % poznatih vrijednosti (58 od 288 na random; 2 rubna + ostatak)
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
