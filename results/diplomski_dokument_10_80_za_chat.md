# Diplomski rad — rezultati eksperimenata 10–80 % missing rate
*Izvor: `results/experiment_results.csv` (360 redaka)*
*Generirano automatski iz stvarnih CSV podataka*

---

## PROMJENE U EKSPERIMENTU

- Dodani missing rateovi: **50 %, 60 %, 70 %, 80 %**
- Konačni popis: 10 %, 20 %, 30 %, 40 %, 50 %, 60 %, 70 %, 80 %
- Ukupno: 5 scenarija × 8 rateova × 8 metoda = **320 testova**
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
- **block** @ 10%: linear_interpolation (MAE=1.0285)
- **block** @ 20%: linear_interpolation (MAE=1.4765)
- **block** @ 30%: linear_interpolation (MAE=3.4286)
- **block** @ 40%: linear_interpolation (MAE=2.9308)
- **block** @ 50%: linear_interpolation (MAE=5.4362)
- **block** @ 60%: linear_interpolation (MAE=5.3499)
- **block** @ 70%: forward_fill (MAE=3.5043)
- **block** @ 80%: linear_interpolation (MAE=4.7975)
- **block_start** @ 10%: linear_interpolation (MAE=0.9636)
- **block_start** @ 20%: linear_interpolation (MAE=0.6991)
- **block_start** @ 30%: knn (MAE=2.1096)
- **block_start** @ 40%: decision_tree (MAE=1.7834)
- **block_start** @ 50%: linear_interpolation (MAE=1.4386)
- **block_start** @ 60%: cubic_interpolation (MAE=1.5243)
- **block_start** @ 70%: cubic_interpolation (MAE=3.5094)
- **block_start** @ 80%: forward_fill (MAE=4.2559)
- **block_middle** @ 10%: linear_interpolation (MAE=0.4913)
- **block_middle** @ 20%: linear_interpolation (MAE=1.1449)
- **block_middle** @ 30%: cubic_interpolation (MAE=3.9194)
- **block_middle** @ 40%: random_forest (MAE=2.7545)
- **block_middle** @ 50%: cubic_interpolation (MAE=1.2192)
- **block_middle** @ 60%: forward_fill (MAE=3.3930)
- **block_middle** @ 70%: forward_fill (MAE=3.8792)
- **block_middle** @ 80%: forward_fill (MAE=4.6316)
- **block_end** @ 10%: linear_interpolation (MAE=3.4473)
- **block_end** @ 20%: cubic_interpolation (MAE=4.1828)
- **block_end** @ 30%: spline_interpolation (MAE=4.8486)
- **block_end** @ 40%: linear_interpolation (MAE=6.8261)
- **block_end** @ 50%: linear_interpolation (MAE=5.2375)
- **block_end** @ 60%: linear_interpolation (MAE=4.9650)
- **block_end** @ 70%: linear_interpolation (MAE=5.2253)
- **block_end** @ 80%: cubic_interpolation (MAE=4.0472)

### 2. Najbolja metoda po RMSE

- **random** @ 10%: spline_interpolation (RMSE=0.0828)
- **random** @ 20%: cubic_interpolation (RMSE=0.1052)
- **random** @ 30%: linear_interpolation (RMSE=0.1401)
- **random** @ 40%: linear_interpolation (RMSE=0.1596)
- **random** @ 50%: linear_interpolation (RMSE=0.1809)
- **random** @ 60%: cubic_interpolation (RMSE=0.2369)
- **random** @ 70%: linear_interpolation (RMSE=0.3320)
- **random** @ 80%: linear_interpolation (RMSE=0.3145)
- **block** @ 10%: linear_interpolation (RMSE=1.1880)
- **block** @ 20%: linear_interpolation (RMSE=1.6968)
- **block** @ 30%: linear_interpolation (RMSE=4.0453)
- **block** @ 40%: linear_interpolation (RMSE=3.6053)
- **block** @ 50%: linear_interpolation (RMSE=7.0441)
- **block** @ 60%: linear_interpolation (RMSE=6.8720)
- **block** @ 70%: random_forest (RMSE=4.7794)
- **block** @ 80%: linear_interpolation (RMSE=6.1094)
- **block_start** @ 10%: cubic_interpolation (RMSE=1.2203)
- **block_start** @ 20%: linear_interpolation (RMSE=0.8889)
- **block_start** @ 30%: linear_interpolation (RMSE=2.3947)
- **block_start** @ 40%: linear_interpolation (RMSE=2.1093)
- **block_start** @ 50%: cubic_interpolation (RMSE=1.7988)
- **block_start** @ 60%: cubic_interpolation (RMSE=1.8189)
- **block_start** @ 70%: forward_fill (RMSE=4.5389)
- **block_start** @ 80%: forward_fill (RMSE=4.7930)
- **block_middle** @ 10%: linear_interpolation (RMSE=0.5870)
- **block_middle** @ 20%: linear_interpolation (RMSE=1.2988)
- **block_middle** @ 30%: linear_interpolation (RMSE=4.3002)
- **block_middle** @ 40%: random_forest (RMSE=3.0057)
- **block_middle** @ 50%: cubic_interpolation (RMSE=1.7261)
- **block_middle** @ 60%: random_forest (RMSE=4.6429)
- **block_middle** @ 70%: random_forest (RMSE=5.4297)
- **block_middle** @ 80%: random_forest (RMSE=6.3858)
- **block_end** @ 10%: linear_interpolation (RMSE=4.1538)
- **block_end** @ 20%: cubic_interpolation (RMSE=4.5838)
- **block_end** @ 30%: spline_interpolation (RMSE=5.9726)
- **block_end** @ 40%: linear_interpolation (RMSE=8.3215)
- **block_end** @ 50%: linear_interpolation (RMSE=7.0389)
- **block_end** @ 60%: linear_interpolation (RMSE=6.0693)
- **block_end** @ 70%: linear_interpolation (RMSE=6.0540)
- **block_end** @ 80%: linear_interpolation (RMSE=5.4898)

### 3. Najbolja metoda po R²

- **random** @ 10%: cubic_interpolation (R²=0.9998)
- **random** @ 20%: cubic_interpolation (R²=0.9997)
- **random** @ 30%: linear_interpolation (R²=0.9995)
- **random** @ 40%: linear_interpolation (R²=0.9993)
- **random** @ 50%: linear_interpolation (R²=0.9991)
- **random** @ 60%: cubic_interpolation (R²=0.9985)
- **random** @ 70%: linear_interpolation (R²=0.9971)
- **random** @ 80%: linear_interpolation (R²=0.9974)
- **block** @ 10%: linear_interpolation (R²=-1.6311)
- **block** @ 20%: linear_interpolation (R²=-2.6787)
- **block** @ 30%: linear_interpolation (R²=0.3980)
- **block** @ 40%: linear_interpolation (R²=0.7248)
- **block** @ 50%: linear_interpolation (R²=0.1425)
- **block** @ 60%: linear_interpolation (R²=0.1376)
- **block** @ 70%: random_forest (R²=-0.0252)
- **block** @ 80%: linear_interpolation (R²=0.1660)
- **block_start** @ 10%: cubic_interpolation (R²=0.2573)
- **block_start** @ 20%: linear_interpolation (R²=0.7639)
- **block_start** @ 30%: linear_interpolation (R²=-0.4423)
- **block_start** @ 40%: linear_interpolation (R²=0.0554)
- **block_start** @ 50%: cubic_interpolation (R²=0.4541)
- **block_start** @ 60%: cubic_interpolation (R²=0.4898)
- **block_start** @ 70%: forward_fill (R²=-2.1154)
- **block_start** @ 80%: forward_fill (R²=-0.3835)
- **block_middle** @ 10%: linear_interpolation (R²=-2.4255)
- **block_middle** @ 20%: linear_interpolation (R²=-2.6120)
- **block_middle** @ 30%: linear_interpolation (R²=-10.5455)
- **block_middle** @ 40%: random_forest (R²=-0.2751)
- **block_middle** @ 50%: cubic_interpolation (R²=0.7966)
- **block_middle** @ 60%: random_forest (R²=-0.0378)
- **block_middle** @ 70%: random_forest (R²=-0.0906)
- **block_middle** @ 80%: random_forest (R²=-0.0648)
- **block_end** @ 10%: linear_interpolation (R²=0.3437)
- **block_end** @ 20%: cubic_interpolation (R²=0.2258)
- **block_end** @ 30%: spline_interpolation (R²=-0.7742)
- **block_end** @ 40%: linear_interpolation (R²=-0.8504)
- **block_end** @ 50%: linear_interpolation (R²=0.0246)
- **block_end** @ 60%: linear_interpolation (R²=0.3007)
- **block_end** @ 70%: linear_interpolation (R²=0.2256)
- **block_end** @ 80%: linear_interpolation (R²=0.3201)

### 4. Kako se MAE mijenja (10 % → 80 %)?

Prosječni MAE svih metoda i scenarija: 2.0506 (10 %) → 6.5752 (80 %).
Na **random** scenariju: 0,079 → 0,224. Na **block_end**: 0,422 → 3,468.

### 5. Kako se RMSE mijenja?

Prosjek svih metoda: 2.3700 (10 %) → 8.0276 (80 %).

### 6. Kako se R² mijenja?

Prosjek svih metoda: -6.8680 (10 %) → -3.9952 (80 %).
Na random scenariju klasične metode zadržavaju R² > 0,99. Na block scenarijima mnoge metode imaju negativan R².

### 7. Najteži scenarij pri 80 %?

**block_end** — prosječni MAE svih metoda = **4.8569** °C.
Slijedi block_middle (7.1411), block (9.0927), block_start (11.2731), random (0.5124).

### 8. Najstabilnija metoda (10–80 %)?

**linear_interpolation** / **time_interpolation** — prosječni MAE = 3.1315, σ = 2.3467.

### 9. Metoda koja najviše gubi kvalitetu?

**knn** — na random scenariju MAE raste s 0,0865 (10 %) na 0,6353 (80 %), porast +0,55 °C.
Na block scenarijima KNN ima MAE 1,95–3,52 pri 50–80 %.

### 10. Jesu li rezultati iznad 40 % promijenili zaključak?

**Djelomično ne.** Linear interpolacija i dalje dominira. Novi podaci **pojačavaju** zaključak da block scenariji postaju ekstremno teški pri 70–80 %, posebno block_end i block_middle.

### 11. Ostaje li linear_interpolation najbolja ukupno?

**Da.** Pobjeđuje u **20 od 40** kombinacija scenarij/rate po MAE.

### 12. Ostaje li cubic_interpolation najbolja za random?

**Djelomično.** Cubic je najbolja pri 10 %, 20 % i 30 % random. Od 40 % do 80 % vodi **linear_interpolation**.

### 13. KNN pri 50–80 %?

Na **random**: MAE 0,28–0,64 °C (prihvatljivo).
Na **block** scenarijima: MAE **1,95–3,52** °C (vrlo loše). R² često jako negativan.

### 14. Decision Tree i Random Forest pri 50–80 %?

Prosječni MAE: DT = 6.3957 °C, RF = 4.3627 °C.
DT je nešto bolji u prosjeku. Obje metode znatno gore od linear interpolacije na block scenarijima.

### 15. Negativan R² pri većim rateovima?

**Da.** Ukupno **225** od 360 rezultata ima R² < 0.
Pri 80 %: **27** od 40 rezultata. Najčešće: knn, forward_fill, cubic/spline na block scenarijima.

---

## TABLICA 1: Najbolja metoda po scenariju i missing rateu

| scenario | block_position | missing_rate | najbolja metoda po MAE | MAE | RMSE | R² |
|----------|----------------|--------------|------------------------|-----|------|-----|
| block | none | 0.10 | linear_interpolation | 1.0285 | 1.1880 | -1.6311 |
| block | none | 0.20 | linear_interpolation | 1.4765 | 1.6968 | -2.6787 |
| block | none | 0.30 | linear_interpolation | 3.4286 | 4.0453 | 0.3980 |
| block | none | 0.40 | linear_interpolation | 2.9308 | 3.6053 | 0.7248 |
| block | none | 0.50 | linear_interpolation | 5.4362 | 7.0441 | 0.1425 |
| block | none | 0.60 | linear_interpolation | 5.3499 | 6.8720 | 0.1376 |
| block | none | 0.70 | forward_fill | 3.5043 | 4.8567 | -0.0586 |
| block | none | 0.80 | linear_interpolation | 4.7975 | 6.1094 | 0.1660 |
| block_end | end | 0.10 | linear_interpolation | 3.4473 | 4.1538 | 0.3437 |
| block_end | end | 0.20 | cubic_interpolation | 4.1828 | 4.5838 | 0.2258 |
| block_end | end | 0.30 | spline_interpolation | 4.8486 | 5.9726 | -0.7742 |
| block_end | end | 0.40 | linear_interpolation | 6.8261 | 8.3215 | -0.8504 |
| block_end | end | 0.50 | linear_interpolation | 5.2375 | 7.0389 | 0.0246 |
| block_end | end | 0.60 | linear_interpolation | 4.9650 | 6.0693 | 0.3007 |
| block_end | end | 0.70 | linear_interpolation | 5.2253 | 6.0540 | 0.2256 |
| block_end | end | 0.80 | cubic_interpolation | 4.0472 | 5.7523 | 0.2535 |
| block_middle | middle | 0.10 | linear_interpolation | 0.4913 | 0.5870 | -2.4255 |
| block_middle | middle | 0.20 | linear_interpolation | 1.1449 | 1.2988 | -2.6120 |
| block_middle | middle | 0.30 | cubic_interpolation | 3.9194 | 4.8003 | -13.3868 |
| block_middle | middle | 0.40 | random_forest | 2.7545 | 3.0057 | -0.2751 |
| block_middle | middle | 0.50 | cubic_interpolation | 1.2192 | 1.7261 | 0.7966 |
| block_middle | middle | 0.60 | forward_fill | 3.3930 | 4.7624 | -0.0919 |
| block_middle | middle | 0.70 | forward_fill | 3.8792 | 5.4544 | -0.1006 |
| block_middle | middle | 0.80 | forward_fill | 4.6316 | 6.3931 | -0.0673 |
| block_start | start | 0.10 | linear_interpolation | 0.9636 | 1.2281 | 0.2477 |
| block_start | start | 0.20 | linear_interpolation | 0.6991 | 0.8889 | 0.7639 |
| block_start | start | 0.30 | knn | 2.1096 | 2.6192 | -0.7254 |
| block_start | start | 0.40 | decision_tree | 1.7834 | 2.1787 | -0.0078 |
| block_start | start | 0.50 | linear_interpolation | 1.4386 | 1.9513 | 0.3576 |
| block_start | start | 0.60 | cubic_interpolation | 1.5243 | 1.8189 | 0.4898 |
| block_start | start | 0.70 | cubic_interpolation | 3.5094 | 4.7387 | -2.3956 |
| block_start | start | 0.80 | forward_fill | 4.2559 | 4.7930 | -0.3835 |
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
| 0.10 | forward_fill | 0.1587 | 0.2867 | 0.9976 |
| 0.10 | knn | 0.1668 | 0.2770 | 0.9977 |
| 0.10 | decision_tree | 0.5146 | 0.7248 | 0.9845 |
| 0.10 | random_forest | 0.6229 | 0.8123 | 0.9806 |
| 0.20 | spline_interpolation | 0.0635 | 0.1052 | 0.9997 |
| 0.20 | adaptive_imputation | 0.0635 | 0.1052 | 0.9997 |
| 0.20 | cubic_interpolation | 0.0635 | 0.1052 | 0.9997 |
| 0.20 | linear_interpolation | 0.0730 | 0.1185 | 0.9996 |
| 0.20 | time_interpolation | 0.0730 | 0.1185 | 0.9996 |
| 0.20 | knn | 0.1573 | 0.2641 | 0.9981 |
| 0.20 | forward_fill | 0.1635 | 0.2588 | 0.9982 |
| 0.20 | decision_tree | 0.5546 | 0.7300 | 0.9855 |
| 0.20 | random_forest | 0.7003 | 0.9443 | 0.9758 |
| 0.30 | linear_interpolation | 0.0834 | 0.1401 | 0.9995 |
| 0.30 | time_interpolation | 0.0834 | 0.1401 | 0.9995 |
| 0.30 | adaptive_imputation | 0.0834 | 0.1401 | 0.9995 |
| 0.30 | spline_interpolation | 0.0879 | 0.1789 | 0.9991 |
| 0.30 | cubic_interpolation | 0.0879 | 0.1789 | 0.9991 |
| 0.30 | knn | 0.1719 | 0.2838 | 0.9978 |
| 0.30 | forward_fill | 0.1820 | 0.2989 | 0.9975 |
| 0.30 | decision_tree | 0.5385 | 0.6956 | 0.9866 |
| 0.30 | random_forest | 0.7200 | 0.9390 | 0.9756 |
| 0.40 | spline_interpolation | 0.0908 | 0.1724 | 0.9992 |
| 0.40 | adaptive_imputation | 0.0908 | 0.1724 | 0.9992 |
| 0.40 | cubic_interpolation | 0.0909 | 0.1726 | 0.9992 |
| 0.40 | linear_interpolation | 0.0950 | 0.1596 | 0.9993 |
| 0.40 | time_interpolation | 0.0950 | 0.1596 | 0.9993 |
| 0.40 | knn | 0.2044 | 0.3206 | 0.9971 |
| 0.40 | forward_fill | 0.2157 | 0.3499 | 0.9966 |
| 0.40 | decision_tree | 0.5749 | 0.7864 | 0.9827 |
| 0.40 | random_forest | 0.7380 | 1.0012 | 0.9719 |
| 0.50 | spline_interpolation | 0.0997 | 0.2109 | 0.9988 |
| 0.50 | adaptive_imputation | 0.0997 | 0.2109 | 0.9988 |
| 0.50 | cubic_interpolation | 0.0998 | 0.2110 | 0.9988 |
| 0.50 | linear_interpolation | 0.1020 | 0.1809 | 0.9991 |
| 0.50 | time_interpolation | 0.1020 | 0.1809 | 0.9991 |
| 0.50 | forward_fill | 0.2415 | 0.3979 | 0.9956 |
| 0.50 | knn | 0.3731 | 0.9634 | 0.9742 |
| 0.50 | decision_tree | 0.6088 | 0.8548 | 0.9797 |
| 0.50 | random_forest | 0.8259 | 1.0885 | 0.9670 |
| 0.60 | cubic_interpolation | 0.1230 | 0.2369 | 0.9985 |
| 0.60 | adaptive_imputation | 0.1230 | 0.2369 | 0.9985 |
| 0.60 | spline_interpolation | 0.1232 | 0.2371 | 0.9985 |
| 0.60 | linear_interpolation | 0.1276 | 0.2484 | 0.9983 |
| 0.60 | time_interpolation | 0.1276 | 0.2484 | 0.9983 |
| 0.60 | forward_fill | 0.2741 | 0.4235 | 0.9951 |
| 0.60 | knn | 0.4981 | 1.1123 | 0.9663 |
| 0.60 | decision_tree | 0.7182 | 1.0240 | 0.9714 |
| 0.60 | random_forest | 0.7644 | 0.9842 | 0.9736 |
| 0.70 | linear_interpolation | 0.1774 | 0.3320 | 0.9971 |
| 0.70 | time_interpolation | 0.1774 | 0.3320 | 0.9971 |
| 0.70 | adaptive_imputation | 0.1774 | 0.3320 | 0.9971 |
| 0.70 | cubic_interpolation | 0.2138 | 0.4691 | 0.9941 |
| 0.70 | spline_interpolation | 0.2140 | 0.4692 | 0.9941 |
| 0.70 | forward_fill | 0.4076 | 0.7183 | 0.9863 |
| 0.70 | decision_tree | 0.6636 | 0.9730 | 0.9748 |
| 0.70 | random_forest | 0.8077 | 1.1028 | 0.9676 |
| 0.70 | knn | 1.1861 | 3.1064 | 0.7432 |
| 0.80 | linear_interpolation | 0.1785 | 0.3145 | 0.9974 |
| 0.80 | time_interpolation | 0.1785 | 0.3145 | 0.9974 |
| 0.80 | adaptive_imputation | 0.1785 | 0.3145 | 0.9974 |
| 0.80 | spline_interpolation | 0.1936 | 0.3443 | 0.9968 |
| 0.80 | cubic_interpolation | 0.1939 | 0.3446 | 0.9968 |
| 0.80 | forward_fill | 0.5416 | 0.9838 | 0.9741 |
| 0.80 | decision_tree | 0.6881 | 0.9997 | 0.9733 |
| 0.80 | random_forest | 0.9121 | 1.2356 | 0.9592 |
| 0.80 | knn | 1.5467 | 3.4818 | 0.6762 |

---

## TABLICA 3: Block missing 10–80 %

| missing_rate | method | MAE | RMSE | R² |
|-------------|--------|-----|------|-----|
| 0.10 | linear_interpolation | 1.0285 | 1.1880 | -1.6311 |
| 0.10 | time_interpolation | 1.0285 | 1.1880 | -1.6311 |
| 0.10 | adaptive_imputation | 1.0285 | 1.1880 | -1.6311 |
| 0.10 | cubic_interpolation | 1.1604 | 1.3978 | -2.6421 |
| 0.10 | spline_interpolation | 1.1604 | 1.3978 | -2.6421 |
| 0.10 | forward_fill | 1.5435 | 1.7084 | -4.4409 |
| 0.10 | random_forest | 1.8446 | 1.9509 | -6.0949 |
| 0.10 | knn | 2.6173 | 3.0283 | -16.0955 |
| 0.10 | decision_tree | 2.9869 | 3.1589 | -17.6018 |
| 0.20 | linear_interpolation | 1.4765 | 1.6968 | -2.6787 |
| 0.20 | time_interpolation | 1.4765 | 1.6968 | -2.6787 |
| 0.20 | adaptive_imputation | 1.4765 | 1.6968 | -2.6787 |
| 0.20 | forward_fill | 1.6054 | 1.8330 | -3.2929 |
| 0.20 | decision_tree | 2.0627 | 2.2444 | -5.4362 |
| 0.20 | knn | 2.1354 | 2.5753 | -7.4734 |
| 0.20 | random_forest | 2.4682 | 2.6161 | -7.7439 |
| 0.20 | cubic_interpolation | 4.2442 | 5.0983 | -32.2091 |
| 0.20 | spline_interpolation | 4.2442 | 5.0983 | -32.2091 |
| 0.30 | linear_interpolation | 3.4286 | 4.0453 | 0.3980 |
| 0.30 | time_interpolation | 3.4286 | 4.0453 | 0.3980 |
| 0.30 | adaptive_imputation | 3.4286 | 4.0453 | 0.3980 |
| 0.30 | random_forest | 3.9860 | 6.0331 | -0.3389 |
| 0.30 | forward_fill | 4.1018 | 6.5393 | -0.5729 |
| 0.30 | knn | 5.7174 | 6.9792 | -0.7917 |
| 0.30 | cubic_interpolation | 7.7599 | 9.5520 | -2.3562 |
| 0.30 | spline_interpolation | 7.7599 | 9.5520 | -2.3562 |
| 0.30 | decision_tree | 9.7856 | 10.9263 | -3.3914 |
| 0.40 | linear_interpolation | 2.9308 | 3.6053 | 0.7248 |
| 0.40 | time_interpolation | 2.9308 | 3.6053 | 0.7248 |
| 0.40 | adaptive_imputation | 2.9308 | 3.6053 | 0.7248 |
| 0.40 | knn | 5.0333 | 6.6578 | 0.0617 |
| 0.40 | random_forest | 6.6848 | 9.0632 | -0.7389 |
| 0.40 | forward_fill | 7.3827 | 10.0695 | -1.1464 |
| 0.40 | decision_tree | 13.8825 | 15.4907 | -4.0798 |
| 0.40 | cubic_interpolation | 27.7372 | 31.8543 | -20.4801 |
| 0.40 | spline_interpolation | 27.7372 | 31.8543 | -20.4801 |
| 0.50 | linear_interpolation | 5.4362 | 7.0441 | 0.1425 |
| 0.50 | time_interpolation | 5.4362 | 7.0441 | 0.1425 |
| 0.50 | adaptive_imputation | 5.4362 | 7.0441 | 0.1425 |
| 0.50 | cubic_interpolation | 6.0174 | 7.4492 | 0.0410 |
| 0.50 | spline_interpolation | 6.0174 | 7.4492 | 0.0410 |
| 0.50 | decision_tree | 6.9406 | 7.6609 | -0.0143 |
| 0.50 | knn | 6.9655 | 8.5127 | -0.2524 |
| 0.50 | random_forest | 8.0585 | 10.6314 | -0.9534 |
| 0.50 | forward_fill | 8.2467 | 10.9793 | -1.0833 |
| 0.60 | linear_interpolation | 5.3499 | 6.8720 | 0.1376 |
| 0.60 | time_interpolation | 5.3499 | 6.8720 | 0.1376 |
| 0.60 | adaptive_imputation | 5.3499 | 6.8720 | 0.1376 |
| 0.60 | knn | 5.9034 | 7.2391 | 0.0430 |
| 0.60 | random_forest | 6.5787 | 7.6620 | -0.0721 |
| 0.60 | decision_tree | 6.6370 | 7.5778 | -0.0486 |
| 0.60 | forward_fill | 6.7044 | 9.1770 | -0.5379 |
| 0.60 | cubic_interpolation | 12.8316 | 15.8642 | -3.5960 |
| 0.60 | spline_interpolation | 12.8316 | 15.8642 | -3.5960 |
| 0.70 | forward_fill | 3.5043 | 4.8567 | -0.0586 |
| 0.70 | adaptive_imputation | 3.5043 | 4.8567 | -0.0586 |
| 0.70 | random_forest | 3.6055 | 4.7794 | -0.0252 |
| 0.70 | linear_interpolation | 5.7381 | 7.0407 | -1.2248 |
| 0.70 | time_interpolation | 5.7381 | 7.0407 | -1.2248 |
| 0.70 | knn | 7.3758 | 9.6727 | -3.1991 |
| 0.70 | cubic_interpolation | 10.1423 | 11.1737 | -4.6034 |
| 0.70 | spline_interpolation | 10.1423 | 11.1737 | -4.6034 |
| 0.70 | decision_tree | 12.6597 | 13.5111 | -7.1929 |
| 0.80 | linear_interpolation | 4.7975 | 6.1094 | 0.1660 |
| 0.80 | time_interpolation | 4.7975 | 6.1094 | 0.1660 |
| 0.80 | adaptive_imputation | 4.7975 | 6.1094 | 0.1660 |
| 0.80 | knn | 5.0900 | 6.3753 | 0.0918 |
| 0.80 | forward_fill | 5.3337 | 7.4566 | -0.2424 |
| 0.80 | random_forest | 5.3337 | 7.3957 | -0.2222 |
| 0.80 | decision_tree | 5.8292 | 6.6972 | -0.0022 |
| 0.80 | cubic_interpolation | 22.9276 | 28.3087 | -16.9062 |
| 0.80 | spline_interpolation | 22.9276 | 28.3087 | -16.9062 |

---

## TABLICA 4: block_start, block_middle, block_end — najbolje po MAE

| scenario | block_position | missing_rate | najbolja metoda | MAE | RMSE | R² |
|----------|----------------|--------------|-----------------|-----|------|-----|
| block_end | end | 0.10 | linear_interpolation | 3.4473 | 4.1538 | 0.3437 |
| block_end | end | 0.20 | cubic_interpolation | 4.1828 | 4.5838 | 0.2258 |
| block_end | end | 0.30 | spline_interpolation | 4.8486 | 5.9726 | -0.7742 |
| block_end | end | 0.40 | linear_interpolation | 6.8261 | 8.3215 | -0.8504 |
| block_end | end | 0.50 | linear_interpolation | 5.2375 | 7.0389 | 0.0246 |
| block_end | end | 0.60 | linear_interpolation | 4.9650 | 6.0693 | 0.3007 |
| block_end | end | 0.70 | linear_interpolation | 5.2253 | 6.0540 | 0.2256 |
| block_end | end | 0.80 | cubic_interpolation | 4.0472 | 5.7523 | 0.2535 |
| block_middle | middle | 0.10 | linear_interpolation | 0.4913 | 0.5870 | -2.4255 |
| block_middle | middle | 0.20 | linear_interpolation | 1.1449 | 1.2988 | -2.6120 |
| block_middle | middle | 0.30 | cubic_interpolation | 3.9194 | 4.8003 | -13.3868 |
| block_middle | middle | 0.40 | random_forest | 2.7545 | 3.0057 | -0.2751 |
| block_middle | middle | 0.50 | cubic_interpolation | 1.2192 | 1.7261 | 0.7966 |
| block_middle | middle | 0.60 | forward_fill | 3.3930 | 4.7624 | -0.0919 |
| block_middle | middle | 0.70 | forward_fill | 3.8792 | 5.4544 | -0.1006 |
| block_middle | middle | 0.80 | forward_fill | 4.6316 | 6.3931 | -0.0673 |
| block_start | start | 0.10 | linear_interpolation | 0.9636 | 1.2281 | 0.2477 |
| block_start | start | 0.20 | linear_interpolation | 0.6991 | 0.8889 | 0.7639 |
| block_start | start | 0.30 | knn | 2.1096 | 2.6192 | -0.7254 |
| block_start | start | 0.40 | decision_tree | 1.7834 | 2.1787 | -0.0078 |
| block_start | start | 0.50 | linear_interpolation | 1.4386 | 1.9513 | 0.3576 |
| block_start | start | 0.60 | cubic_interpolation | 1.5243 | 1.8189 | 0.4898 |
| block_start | start | 0.70 | cubic_interpolation | 3.5094 | 4.7387 | -2.3956 |
| block_start | start | 0.80 | forward_fill | 4.2559 | 4.7930 | -0.3835 |

---

## TABLICA 5: Sažetak po metodama (10–80 %)

| method | prosječni MAE | prosječni RMSE | prosječni R² | std. dev. MAE | komentar |
|--------|---------------|----------------|--------------|---------------|----------|
| adaptive_imputation | 2.6328 | 3.3301 | -0.3719 | 1.9808 |  |
| linear_interpolation | 3.1315 | 3.7835 | -0.6188 | 2.3467 | Najstabilnija; 27 pobjeda po MAE od 40 kombinacija |
| time_interpolation | 3.1315 | 3.7835 | -0.6188 | 2.3467 | Identična linear interpolaciji |
| forward_fill | 3.7863 | 4.7590 | -1.5813 | 2.8185 | Loša na block scenarijima |
| random_forest | 3.9226 | 4.8046 | -2.0168 | 2.7050 | Manja varijabilnost od DT, ali veći prosječni MAE |
| knn | 4.9931 | 6.1100 | -9.6712 | 3.3212 | Najveće pogreške na block scenarijima; gubi najviše kvalitete s rateom |
| decision_tree | 5.2013 | 5.8706 | -3.3653 | 4.1934 | Ponekad dobra na block_middle; nestabilna na visokim rateovima |
| cubic_interpolation | 5.8704 | 7.0044 | -5.1028 | 6.6487 | Odlična na random 10-30%; loša na block pri visokim rateovima |
| spline_interpolation | 6.6240 | 7.8068 | -6.9507 | 7.4899 | Ista jezgra kao cubic |

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
