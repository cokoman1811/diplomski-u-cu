# Sve tablice rezultata — missing rate 10–80 %

*Izvor: `results/experiment_results.csv` (320 redaka)*
*Generirano: `python scripts/generate_results_tables.py`*

---

## KOMPLETNA TABLICA (svi scenariji, svi rateovi, sve metode)

| scenario | block_position | missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|----------|----------------|--------------|--------|-----|------|-----|---------|-----------|
| block | none | 10% | cubic_interpolation | 0.3391 | 0.3654 | -2.3624 | 29 | 29 |
| block | none | 10% | decision_tree | 0.3173 | 0.3664 | -2.3806 | 29 | 29 |
| block | none | 10% | forward_fill | 0.4883 | 0.5274 | -6.0048 | 29 | 29 |
| block | none | 10% | knn | 2.0580 | 2.2816 | -130.1117 | 29 | 29 |
| block | none | 10% | linear_interpolation | 0.1214 | 0.1428 | 0.4867 | 29 | 29 |
| block | none | 10% | random_forest | 0.5252 | 0.5617 | -6.9477 | 29 | 29 |
| block | none | 10% | spline_interpolation | 0.3391 | 0.3654 | -2.3624 | 29 | 29 |
| block | none | 10% | time_interpolation | 0.1214 | 0.1428 | 0.4867 | 29 | 29 |
| block | none | 20% | cubic_interpolation | 0.1946 | 0.2737 | 0.9155 | 58 | 58 |
| block | none | 20% | decision_tree | 1.2948 | 1.6011 | -1.8901 | 58 | 58 |
| block | none | 20% | forward_fill | 1.7912 | 2.0237 | -3.6173 | 58 | 58 |
| block | none | 20% | knn | 3.1533 | 3.2768 | -11.1059 | 58 | 58 |
| block | none | 20% | linear_interpolation | 0.2849 | 0.3440 | 0.8666 | 58 | 58 |
| block | none | 20% | random_forest | 1.9376 | 2.1544 | -4.2328 | 58 | 58 |
| block | none | 20% | spline_interpolation | 0.1946 | 0.2737 | 0.9155 | 58 | 58 |
| block | none | 20% | time_interpolation | 0.2849 | 0.3440 | 0.8666 | 58 | 58 |
| block | none | 30% | cubic_interpolation | 0.4890 | 0.5492 | 0.5995 | 86 | 86 |
| block | none | 30% | decision_tree | 0.7618 | 1.0070 | -0.3465 | 86 | 86 |
| block | none | 30% | forward_fill | 0.9838 | 1.2559 | -1.0942 | 86 | 86 |
| block | none | 30% | knn | 3.4313 | 3.6477 | -16.6670 | 86 | 86 |
| block | none | 30% | linear_interpolation | 0.4406 | 0.5602 | 0.5833 | 86 | 86 |
| block | none | 30% | random_forest | 0.9100 | 1.1784 | -0.8439 | 86 | 86 |
| block | none | 30% | spline_interpolation | 0.4890 | 0.5492 | 0.5995 | 86 | 86 |
| block | none | 30% | time_interpolation | 0.4406 | 0.5602 | 0.5833 | 86 | 86 |
| block | none | 40% | cubic_interpolation | 1.1989 | 1.4507 | 0.1526 | 115 | 115 |
| block | none | 40% | decision_tree | 2.3168 | 2.8002 | -2.1573 | 115 | 115 |
| block | none | 40% | forward_fill | 1.6503 | 2.0226 | -0.6472 | 115 | 115 |
| block | none | 40% | knn | 3.4468 | 3.6493 | -4.3622 | 115 | 115 |
| block | none | 40% | linear_interpolation | 0.6903 | 0.9168 | 0.6616 | 115 | 115 |
| block | none | 40% | random_forest | 1.3887 | 1.5848 | -0.0113 | 115 | 115 |
| block | none | 40% | spline_interpolation | 1.1448 | 1.3846 | 0.2281 | 115 | 115 |
| block | none | 40% | time_interpolation | 0.6903 | 0.9168 | 0.6616 | 115 | 115 |
| block | none | 50% | cubic_interpolation | 1.8066 | 2.3389 | -8.1503 | 144 | 144 |
| block | none | 50% | decision_tree | 0.7364 | 0.9967 | -0.6617 | 144 | 144 |
| block | none | 50% | forward_fill | 0.6913 | 0.8919 | -0.3307 | 144 | 144 |
| block | none | 50% | knn | 3.0574 | 3.3506 | -17.7785 | 144 | 144 |
| block | none | 50% | linear_interpolation | 0.7461 | 0.9694 | -0.5720 | 144 | 144 |
| block | none | 50% | random_forest | 0.8577 | 1.1304 | -1.1375 | 144 | 144 |
| block | none | 50% | spline_interpolation | 1.8066 | 2.3389 | -8.1505 | 144 | 144 |
| block | none | 50% | time_interpolation | 0.7461 | 0.9694 | -0.5720 | 144 | 144 |
| block | none | 60% | cubic_interpolation | 1.8053 | 2.2680 | -3.0313 | 173 | 173 |
| block | none | 60% | decision_tree | 1.8812 | 2.1340 | -2.5693 | 173 | 173 |
| block | none | 60% | forward_fill | 2.8020 | 3.0187 | -6.1420 | 173 | 173 |
| block | none | 60% | knn | 2.5015 | 3.0034 | -6.0699 | 173 | 173 |
| block | none | 60% | linear_interpolation | 0.6108 | 0.7029 | 0.6128 | 173 | 173 |
| block | none | 60% | random_forest | 2.7205 | 2.9406 | -5.7773 | 173 | 173 |
| block | none | 60% | spline_interpolation | 1.8053 | 2.2680 | -3.0313 | 173 | 173 |
| block | none | 60% | time_interpolation | 0.6108 | 0.7029 | 0.6128 | 173 | 173 |
| block | none | 70% | cubic_interpolation | 1.7745 | 2.0544 | -1.7625 | 202 | 202 |
| block | none | 70% | decision_tree | 1.3845 | 1.6836 | -0.8551 | 202 | 202 |
| block | none | 70% | forward_fill | 2.6239 | 2.8791 | -4.4254 | 202 | 202 |
| block | none | 70% | knn | 2.3487 | 2.9056 | -4.5255 | 202 | 202 |
| block | none | 70% | linear_interpolation | 0.7720 | 0.8781 | 0.4953 | 202 | 202 |
| block | none | 70% | random_forest | 2.6946 | 2.9494 | -4.6935 | 202 | 202 |
| block | none | 70% | spline_interpolation | 1.7745 | 2.0544 | -1.7625 | 202 | 202 |
| block | none | 70% | time_interpolation | 0.7720 | 0.8781 | 0.4953 | 202 | 202 |
| block | none | 80% | cubic_interpolation | 1.8285 | 2.2010 | -0.1746 | 230 | 230 |
| block | none | 80% | decision_tree | 2.8560 | 3.4613 | -1.9050 | 230 | 230 |
| block | none | 80% | forward_fill | 2.5757 | 2.9049 | -1.0461 | 230 | 230 |
| block | none | 80% | knn | 1.9468 | 2.3307 | -0.3171 | 230 | 230 |
| block | none | 80% | linear_interpolation | 0.6705 | 0.9274 | 0.7914 | 230 | 230 |
| block | none | 80% | random_forest | 2.5757 | 2.9049 | -1.0461 | 230 | 230 |
| block | none | 80% | spline_interpolation | 1.8286 | 2.2011 | -0.1747 | 230 | 230 |
| block | none | 80% | time_interpolation | 0.6705 | 0.9274 | 0.7914 | 230 | 230 |
| block_end | end | 10% | cubic_interpolation | 0.1812 | 0.2320 | 0.7683 | 29 | 29 |
| block_end | end | 10% | decision_tree | 0.5777 | 0.7523 | -1.4371 | 29 | 29 |
| block_end | end | 10% | forward_fill | 0.5000 | 0.6880 | -1.0382 | 29 | 29 |
| block_end | end | 10% | knn | 0.6262 | 0.8969 | -2.4639 | 29 | 29 |
| block_end | end | 10% | linear_interpolation | 0.1970 | 0.2523 | 0.7258 | 29 | 29 |
| block_end | end | 10% | random_forest | 0.8392 | 0.9678 | -3.0328 | 29 | 29 |
| block_end | end | 10% | spline_interpolation | 0.2195 | 0.2765 | 0.6707 | 29 | 29 |
| block_end | end | 10% | time_interpolation | 0.1970 | 0.2523 | 0.7258 | 29 | 29 |
| block_end | end | 20% | cubic_interpolation | 0.3076 | 0.3514 | 0.7268 | 58 | 58 |
| block_end | end | 20% | decision_tree | 0.7769 | 0.9023 | -0.8017 | 58 | 58 |
| block_end | end | 20% | forward_fill | 0.7819 | 0.9642 | -1.0573 | 58 | 58 |
| block_end | end | 20% | knn | 1.4977 | 1.7814 | -6.0227 | 58 | 58 |
| block_end | end | 20% | linear_interpolation | 0.3538 | 0.3940 | 0.6565 | 58 | 58 |
| block_end | end | 20% | random_forest | 0.8945 | 1.0807 | -1.5848 | 58 | 58 |
| block_end | end | 20% | spline_interpolation | 0.4108 | 0.4501 | 0.5516 | 58 | 58 |
| block_end | end | 20% | time_interpolation | 0.3538 | 0.3940 | 0.6565 | 58 | 58 |
| block_end | end | 30% | cubic_interpolation | 0.7642 | 0.8689 | -0.7920 | 86 | 86 |
| block_end | end | 30% | decision_tree | 1.0387 | 1.1565 | -2.1745 | 86 | 86 |
| block_end | end | 30% | forward_fill | 0.7772 | 0.9142 | -0.9836 | 86 | 86 |
| block_end | end | 30% | knn | 2.2341 | 2.5644 | -14.6091 | 86 | 86 |
| block_end | end | 30% | linear_interpolation | 1.0496 | 1.1980 | -2.4069 | 86 | 86 |
| block_end | end | 30% | random_forest | 1.0321 | 1.1827 | -2.3205 | 86 | 86 |
| block_end | end | 30% | spline_interpolation | 0.6671 | 0.7697 | -0.4063 | 86 | 86 |
| block_end | end | 30% | time_interpolation | 1.0496 | 1.1980 | -2.4069 | 86 | 86 |
| block_end | end | 40% | cubic_interpolation | 2.3721 | 2.6629 | -11.3162 | 115 | 115 |
| block_end | end | 40% | decision_tree | 1.1899 | 1.4157 | -2.4808 | 115 | 115 |
| block_end | end | 40% | forward_fill | 1.3230 | 1.5207 | -3.0167 | 115 | 115 |
| block_end | end | 40% | knn | 2.7625 | 3.0981 | -15.6708 | 115 | 115 |
| block_end | end | 40% | linear_interpolation | 1.2481 | 1.4505 | -2.6540 | 115 | 115 |
| block_end | end | 40% | random_forest | 1.0260 | 1.2487 | -1.7082 | 115 | 115 |
| block_end | end | 40% | spline_interpolation | 2.9237 | 3.2509 | -17.3551 | 115 | 115 |
| block_end | end | 40% | time_interpolation | 1.2481 | 1.4505 | -2.6540 | 115 | 115 |
| block_end | end | 50% | cubic_interpolation | 4.5362 | 5.0518 | -41.4015 | 144 | 144 |
| block_end | end | 50% | decision_tree | 0.8176 | 1.0873 | -0.9642 | 144 | 144 |
| block_end | end | 50% | forward_fill | 0.8833 | 1.1522 | -1.2055 | 144 | 144 |
| block_end | end | 50% | knn | 3.0573 | 3.3505 | -17.6510 | 144 | 144 |
| block_end | end | 50% | linear_interpolation | 0.9438 | 1.2138 | -1.4476 | 144 | 144 |
| block_end | end | 50% | random_forest | 0.9334 | 1.2041 | -1.4088 | 144 | 144 |
| block_end | end | 50% | spline_interpolation | 6.3491 | 6.9499 | -79.2497 | 144 | 144 |
| block_end | end | 50% | time_interpolation | 0.9438 | 1.2138 | -1.4476 | 144 | 144 |
| block_end | end | 60% | cubic_interpolation | 0.8052 | 0.9921 | -0.5409 | 173 | 173 |
| block_end | end | 60% | decision_tree | 1.0997 | 1.3593 | -1.8929 | 173 | 173 |
| block_end | end | 60% | forward_fill | 1.2220 | 1.4601 | -2.3382 | 173 | 173 |
| block_end | end | 60% | knn | 3.0490 | 3.3249 | -16.3091 | 173 | 173 |
| block_end | end | 60% | linear_interpolation | 1.0220 | 1.2567 | -1.4729 | 173 | 173 |
| block_end | end | 60% | random_forest | 1.1813 | 1.4262 | -2.1849 | 173 | 173 |
| block_end | end | 60% | spline_interpolation | 0.7227 | 0.8186 | -0.0491 | 173 | 173 |
| block_end | end | 60% | time_interpolation | 1.0220 | 1.2567 | -1.4729 | 173 | 173 |
| block_end | end | 70% | cubic_interpolation | 1.9274 | 2.2346 | -5.0946 | 202 | 202 |
| block_end | end | 70% | decision_tree | 1.4107 | 1.6652 | -2.3843 | 202 | 202 |
| block_end | end | 70% | forward_fill | 1.7410 | 1.9622 | -3.6996 | 202 | 202 |
| block_end | end | 70% | knn | 3.2164 | 3.4458 | -13.4922 | 202 | 202 |
| block_end | end | 70% | linear_interpolation | 1.1760 | 1.3635 | -1.2691 | 202 | 202 |
| block_end | end | 70% | random_forest | 1.8083 | 2.0222 | -3.9910 | 202 | 202 |
| block_end | end | 70% | spline_interpolation | 2.6468 | 3.1874 | -11.4000 | 202 | 202 |
| block_end | end | 70% | time_interpolation | 1.1760 | 1.3635 | -1.2691 | 202 | 202 |
| block_end | end | 80% | cubic_interpolation | 4.0390 | 4.8866 | -15.0551 | 230 | 230 |
| block_end | end | 80% | decision_tree | 2.1961 | 2.4319 | -2.9762 | 230 | 230 |
| block_end | end | 80% | forward_fill | 2.8784 | 3.1220 | -5.5534 | 230 | 230 |
| block_end | end | 80% | knn | 3.5170 | 3.7468 | -8.4386 | 230 | 230 |
| block_end | end | 80% | linear_interpolation | 1.5937 | 1.7404 | -1.0366 | 230 | 230 |
| block_end | end | 80% | random_forest | 3.0300 | 3.2659 | -6.1715 | 230 | 230 |
| block_end | end | 80% | spline_interpolation | 6.4665 | 7.3344 | -35.1676 | 230 | 230 |
| block_end | end | 80% | time_interpolation | 1.5937 | 1.7404 | -1.0366 | 230 | 230 |
| block_middle | middle | 10% | cubic_interpolation | 0.1513 | 0.1870 | -0.7331 | 29 | 29 |
| block_middle | middle | 10% | decision_tree | 0.1081 | 0.1322 | 0.1342 | 29 | 29 |
| block_middle | middle | 10% | forward_fill | 0.4234 | 0.4466 | -8.8880 | 29 | 29 |
| block_middle | middle | 10% | knn | 1.4963 | 2.2245 | -244.2807 | 29 | 29 |
| block_middle | middle | 10% | linear_interpolation | 0.1674 | 0.2230 | -1.4652 | 29 | 29 |
| block_middle | middle | 10% | random_forest | 0.3726 | 0.3987 | -6.8806 | 29 | 29 |
| block_middle | middle | 10% | spline_interpolation | 0.1513 | 0.1870 | -0.7331 | 29 | 29 |
| block_middle | middle | 10% | time_interpolation | 0.1674 | 0.2230 | -1.4652 | 29 | 29 |
| block_middle | middle | 20% | cubic_interpolation | 1.0215 | 1.2310 | -25.7088 | 58 | 58 |
| block_middle | middle | 20% | decision_tree | 0.3651 | 0.4303 | -2.2631 | 58 | 58 |
| block_middle | middle | 20% | forward_fill | 0.3384 | 0.4029 | -1.8616 | 58 | 58 |
| block_middle | middle | 20% | knn | 2.4358 | 3.0429 | -162.1881 | 58 | 58 |
| block_middle | middle | 20% | linear_interpolation | 0.3654 | 0.4325 | -2.2972 | 58 | 58 |
| block_middle | middle | 20% | random_forest | 0.6154 | 0.6599 | -6.6742 | 58 | 58 |
| block_middle | middle | 20% | spline_interpolation | 1.0215 | 1.2310 | -25.7088 | 58 | 58 |
| block_middle | middle | 20% | time_interpolation | 0.3654 | 0.4325 | -2.2972 | 58 | 58 |
| block_middle | middle | 30% | cubic_interpolation | 1.2902 | 1.4448 | -19.0888 | 86 | 86 |
| block_middle | middle | 30% | decision_tree | 0.8338 | 1.2512 | -14.0659 | 86 | 86 |
| block_middle | middle | 30% | forward_fill | 0.6723 | 0.7427 | -4.3078 | 86 | 86 |
| block_middle | middle | 30% | knn | 2.7403 | 3.2364 | -99.7954 | 86 | 86 |
| block_middle | middle | 30% | linear_interpolation | 0.2554 | 0.3052 | 0.1034 | 86 | 86 |
| block_middle | middle | 30% | random_forest | 0.6738 | 0.7441 | -4.3276 | 86 | 86 |
| block_middle | middle | 30% | spline_interpolation | 1.2902 | 1.4448 | -19.0888 | 86 | 86 |
| block_middle | middle | 30% | time_interpolation | 0.2554 | 0.3052 | 0.1034 | 86 | 86 |
| block_middle | middle | 40% | cubic_interpolation | 0.7192 | 0.7955 | -2.3344 | 115 | 115 |
| block_middle | middle | 40% | decision_tree | 0.7853 | 0.8976 | -3.2450 | 115 | 115 |
| block_middle | middle | 40% | forward_fill | 1.0452 | 1.1324 | -5.7561 | 115 | 115 |
| block_middle | middle | 40% | knn | 2.7436 | 3.1944 | -52.7663 | 115 | 115 |
| block_middle | middle | 40% | linear_interpolation | 0.2665 | 0.3092 | 0.4961 | 115 | 115 |
| block_middle | middle | 40% | random_forest | 1.1690 | 1.2475 | -7.2003 | 115 | 115 |
| block_middle | middle | 40% | spline_interpolation | 0.7192 | 0.7955 | -2.3344 | 115 | 115 |
| block_middle | middle | 40% | time_interpolation | 0.2665 | 0.3092 | 0.4961 | 115 | 115 |
| block_middle | middle | 50% | cubic_interpolation | 0.9723 | 1.1106 | -1.5050 | 144 | 144 |
| block_middle | middle | 50% | decision_tree | 1.8916 | 2.0175 | -7.2665 | 144 | 144 |
| block_middle | middle | 50% | forward_fill | 2.1344 | 2.2468 | -9.2525 | 144 | 144 |
| block_middle | middle | 50% | knn | 2.9208 | 3.2727 | -20.7521 | 144 | 144 |
| block_middle | middle | 50% | linear_interpolation | 0.5473 | 0.5987 | 0.2720 | 144 | 144 |
| block_middle | middle | 50% | random_forest | 2.3135 | 2.4175 | -10.8696 | 144 | 144 |
| block_middle | middle | 50% | spline_interpolation | 0.9723 | 1.1106 | -1.5050 | 144 | 144 |
| block_middle | middle | 50% | time_interpolation | 0.5473 | 0.5987 | 0.2720 | 144 | 144 |
| block_middle | middle | 60% | cubic_interpolation | 5.8078 | 6.2969 | -29.3209 | 173 | 173 |
| block_middle | middle | 60% | decision_tree | 2.6106 | 2.8501 | -5.2117 | 173 | 173 |
| block_middle | middle | 60% | forward_fill | 2.5203 | 2.7622 | -4.8346 | 173 | 173 |
| block_middle | middle | 60% | knn | 2.6008 | 3.0483 | -6.1057 | 173 | 173 |
| block_middle | middle | 60% | linear_interpolation | 0.5395 | 0.6247 | 0.7016 | 173 | 173 |
| block_middle | middle | 60% | random_forest | 2.7120 | 2.9432 | -5.6244 | 173 | 173 |
| block_middle | middle | 60% | spline_interpolation | 5.8078 | 6.2969 | -29.3209 | 173 | 173 |
| block_middle | middle | 60% | time_interpolation | 0.5395 | 0.6247 | 0.7016 | 173 | 173 |
| block_middle | middle | 70% | cubic_interpolation | 8.6021 | 9.6499 | -41.3432 | 202 | 202 |
| block_middle | middle | 70% | decision_tree | 1.9831 | 2.3853 | -1.5871 | 202 | 202 |
| block_middle | middle | 70% | forward_fill | 3.8817 | 4.1554 | -6.8516 | 202 | 202 |
| block_middle | middle | 70% | knn | 2.5298 | 3.0901 | -3.3420 | 202 | 202 |
| block_middle | middle | 70% | linear_interpolation | 0.9671 | 1.1303 | 0.4191 | 202 | 202 |
| block_middle | middle | 70% | random_forest | 4.1547 | 4.4114 | -7.8491 | 202 | 202 |
| block_middle | middle | 70% | spline_interpolation | 8.6021 | 9.6499 | -41.3432 | 202 | 202 |
| block_middle | middle | 70% | time_interpolation | 0.9671 | 1.1303 | 0.4191 | 202 | 202 |
| block_middle | middle | 80% | cubic_interpolation | 5.3329 | 6.1881 | -10.3548 | 230 | 230 |
| block_middle | middle | 80% | decision_tree | 1.8817 | 2.4652 | -0.8021 | 230 | 230 |
| block_middle | middle | 80% | forward_fill | 4.4810 | 4.8282 | -5.9124 | 230 | 230 |
| block_middle | middle | 80% | knn | 2.3632 | 2.9842 | -1.6407 | 230 | 230 |
| block_middle | middle | 80% | linear_interpolation | 1.4370 | 1.5759 | 0.2636 | 230 | 230 |
| block_middle | middle | 80% | random_forest | 4.4352 | 4.7827 | -5.7827 | 230 | 230 |
| block_middle | middle | 80% | spline_interpolation | 5.3329 | 6.1881 | -10.3548 | 230 | 230 |
| block_middle | middle | 80% | time_interpolation | 1.4370 | 1.5759 | 0.2636 | 230 | 230 |
| block_start | start | 10% | cubic_interpolation | 0.4806 | 0.5507 | -0.1368 | 29 | 29 |
| block_start | start | 10% | decision_tree | 0.7110 | 0.8111 | -1.4658 | 29 | 29 |
| block_start | start | 10% | forward_fill | 0.7866 | 0.8892 | -1.9636 | 29 | 29 |
| block_start | start | 10% | knn | 3.6560 | 3.9546 | -57.6198 | 29 | 29 |
| block_start | start | 10% | linear_interpolation | 0.2212 | 0.2870 | 0.6913 | 29 | 29 |
| block_start | start | 10% | random_forest | 0.4947 | 0.5892 | -0.3013 | 29 | 29 |
| block_start | start | 10% | spline_interpolation | 0.5369 | 0.6085 | -0.3880 | 29 | 29 |
| block_start | start | 10% | time_interpolation | 0.2212 | 0.2870 | 0.6913 | 29 | 29 |
| block_start | start | 20% | cubic_interpolation | 1.0331 | 1.2093 | -1.7426 | 58 | 58 |
| block_start | start | 20% | decision_tree | 1.4746 | 1.6829 | -4.3117 | 58 | 58 |
| block_start | start | 20% | forward_fill | 0.8097 | 0.9592 | -0.7258 | 58 | 58 |
| block_start | start | 20% | knn | 4.0126 | 4.1607 | -31.4677 | 58 | 58 |
| block_start | start | 20% | linear_interpolation | 1.1335 | 1.3189 | -2.2624 | 58 | 58 |
| block_start | start | 20% | random_forest | 1.0161 | 1.1934 | -1.6710 | 58 | 58 |
| block_start | start | 20% | spline_interpolation | 0.9311 | 1.0954 | -1.2504 | 58 | 58 |
| block_start | start | 20% | time_interpolation | 1.1335 | 1.3189 | -2.2624 | 58 | 58 |
| block_start | start | 30% | cubic_interpolation | 1.1125 | 1.3589 | -0.3223 | 86 | 86 |
| block_start | start | 30% | decision_tree | 1.6348 | 1.8912 | -1.5613 | 86 | 86 |
| block_start | start | 30% | forward_fill | 1.0057 | 1.1824 | -0.0012 | 86 | 86 |
| block_start | start | 30% | knn | 3.7127 | 3.9081 | -9.9374 | 86 | 86 |
| block_start | start | 30% | linear_interpolation | 1.1155 | 1.3455 | -0.2964 | 86 | 86 |
| block_start | start | 30% | random_forest | 1.2255 | 1.4521 | -0.5100 | 86 | 86 |
| block_start | start | 30% | spline_interpolation | 0.9713 | 1.1943 | -0.0214 | 86 | 86 |
| block_start | start | 30% | time_interpolation | 1.1155 | 1.3455 | -0.2964 | 86 | 86 |
| block_start | start | 40% | cubic_interpolation | 1.9440 | 2.1614 | -0.9359 | 115 | 115 |
| block_start | start | 40% | decision_tree | 1.6954 | 2.0516 | -0.7443 | 115 | 115 |
| block_start | start | 40% | forward_fill | 1.4386 | 1.7107 | -0.2128 | 115 | 115 |
| block_start | start | 40% | knn | 3.4647 | 3.6508 | -4.5235 | 115 | 115 |
| block_start | start | 40% | linear_interpolation | 0.8763 | 1.1887 | 0.4144 | 115 | 115 |
| block_start | start | 40% | random_forest | 1.5356 | 1.7611 | -0.2853 | 115 | 115 |
| block_start | start | 40% | spline_interpolation | 2.2900 | 2.5576 | -1.7108 | 115 | 115 |
| block_start | start | 40% | time_interpolation | 0.8763 | 1.1887 | 0.4144 | 115 | 115 |
| block_start | start | 50% | cubic_interpolation | 1.0440 | 1.3250 | 0.4269 | 144 | 144 |
| block_start | start | 50% | decision_tree | 1.6370 | 2.0098 | -0.3185 | 144 | 144 |
| block_start | start | 50% | forward_fill | 1.8256 | 2.1502 | -0.5091 | 144 | 144 |
| block_start | start | 50% | knn | 2.9592 | 3.3045 | -2.5642 | 144 | 144 |
| block_start | start | 50% | linear_interpolation | 0.7737 | 1.0082 | 0.6682 | 144 | 144 |
| block_start | start | 50% | random_forest | 1.6998 | 1.8797 | -0.1533 | 144 | 144 |
| block_start | start | 50% | spline_interpolation | 1.1219 | 1.4115 | 0.3497 | 144 | 144 |
| block_start | start | 50% | time_interpolation | 0.7737 | 1.0082 | 0.6682 | 144 | 144 |
| block_start | start | 60% | cubic_interpolation | 2.4579 | 2.8602 | -1.4938 | 173 | 173 |
| block_start | start | 60% | decision_tree | 1.5867 | 1.8727 | -0.0691 | 173 | 173 |
| block_start | start | 60% | forward_fill | 2.1107 | 2.4371 | -0.8106 | 173 | 173 |
| block_start | start | 60% | knn | 2.4720 | 2.9078 | -1.5774 | 173 | 173 |
| block_start | start | 60% | linear_interpolation | 0.9158 | 1.0451 | 0.6670 | 173 | 173 |
| block_start | start | 60% | random_forest | 1.4247 | 1.7191 | 0.0991 | 173 | 173 |
| block_start | start | 60% | spline_interpolation | 3.0857 | 3.6795 | -3.1269 | 173 | 173 |
| block_start | start | 60% | time_interpolation | 0.9158 | 1.0451 | 0.6670 | 173 | 173 |
| block_start | start | 70% | cubic_interpolation | 1.6762 | 1.7713 | 0.0624 | 202 | 202 |
| block_start | start | 70% | decision_tree | 2.0837 | 2.6150 | -1.0435 | 202 | 202 |
| block_start | start | 70% | forward_fill | 2.3393 | 2.6579 | -1.1111 | 202 | 202 |
| block_start | start | 70% | knn | 2.2064 | 2.7076 | -1.1908 | 202 | 202 |
| block_start | start | 70% | linear_interpolation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| block_start | start | 70% | random_forest | 2.0780 | 2.3135 | -0.5994 | 202 | 202 |
| block_start | start | 70% | spline_interpolation | 2.1933 | 2.3259 | -0.6166 | 202 | 202 |
| block_start | start | 70% | time_interpolation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| block_start | start | 80% | cubic_interpolation | 1.0307 | 1.2238 | 0.6238 | 230 | 230 |
| block_start | start | 80% | decision_tree | 3.0026 | 3.5665 | -2.1947 | 230 | 230 |
| block_start | start | 80% | forward_fill | 2.6620 | 3.0456 | -1.3297 | 230 | 230 |
| block_start | start | 80% | knn | 2.2679 | 2.8132 | -0.9877 | 230 | 230 |
| block_start | start | 80% | linear_interpolation | 0.6939 | 0.9373 | 0.7794 | 230 | 230 |
| block_start | start | 80% | random_forest | 1.7179 | 2.4124 | -0.4617 | 230 | 230 |
| block_start | start | 80% | spline_interpolation | 0.8830 | 1.1028 | 0.6945 | 230 | 230 |
| block_start | start | 80% | time_interpolation | 0.6939 | 0.9373 | 0.7794 | 230 | 230 |
| random | none | 10% | cubic_interpolation | 0.0406 | 0.0503 | 0.9993 | 29 | 29 |
| random | none | 10% | decision_tree | 0.1568 | 0.1939 | 0.9893 | 29 | 29 |
| random | none | 10% | forward_fill | 0.0521 | 0.0726 | 0.9985 | 29 | 29 |
| random | none | 10% | knn | 0.0865 | 0.1110 | 0.9965 | 29 | 29 |
| random | none | 10% | linear_interpolation | 0.0471 | 0.0588 | 0.9990 | 29 | 29 |
| random | none | 10% | random_forest | 0.1618 | 0.2204 | 0.9862 | 29 | 29 |
| random | none | 10% | spline_interpolation | 0.0406 | 0.0503 | 0.9993 | 29 | 29 |
| random | none | 10% | time_interpolation | 0.0471 | 0.0588 | 0.9990 | 29 | 29 |
| random | none | 20% | cubic_interpolation | 0.0488 | 0.0672 | 0.9987 | 58 | 58 |
| random | none | 20% | decision_tree | 0.1662 | 0.2198 | 0.9858 | 58 | 58 |
| random | none | 20% | forward_fill | 0.0741 | 0.1077 | 0.9966 | 58 | 58 |
| random | none | 20% | knn | 0.0841 | 0.1068 | 0.9966 | 58 | 58 |
| random | none | 20% | linear_interpolation | 0.0502 | 0.0680 | 0.9986 | 58 | 58 |
| random | none | 20% | random_forest | 0.1903 | 0.2719 | 0.9782 | 58 | 58 |
| random | none | 20% | spline_interpolation | 0.0488 | 0.0672 | 0.9987 | 58 | 58 |
| random | none | 20% | time_interpolation | 0.0502 | 0.0680 | 0.9986 | 58 | 58 |
| random | none | 30% | cubic_interpolation | 0.0448 | 0.0606 | 0.9991 | 86 | 86 |
| random | none | 30% | decision_tree | 0.1633 | 0.2275 | 0.9869 | 86 | 86 |
| random | none | 30% | forward_fill | 0.1012 | 0.1588 | 0.9936 | 86 | 86 |
| random | none | 30% | knn | 0.1016 | 0.1422 | 0.9949 | 86 | 86 |
| random | none | 30% | linear_interpolation | 0.0502 | 0.0662 | 0.9989 | 86 | 86 |
| random | none | 30% | random_forest | 0.1952 | 0.2728 | 0.9812 | 86 | 86 |
| random | none | 30% | spline_interpolation | 0.0448 | 0.0606 | 0.9991 | 86 | 86 |
| random | none | 30% | time_interpolation | 0.0502 | 0.0662 | 0.9989 | 86 | 86 |
| random | none | 40% | cubic_interpolation | 0.0849 | 0.1419 | 0.9953 | 115 | 115 |
| random | none | 40% | decision_tree | 0.1693 | 0.2320 | 0.9874 | 115 | 115 |
| random | none | 40% | forward_fill | 0.1366 | 0.2002 | 0.9906 | 115 | 115 |
| random | none | 40% | knn | 0.1304 | 0.1880 | 0.9917 | 115 | 115 |
| random | none | 40% | linear_interpolation | 0.0620 | 0.0920 | 0.9980 | 115 | 115 |
| random | none | 40% | random_forest | 0.2136 | 0.2921 | 0.9801 | 115 | 115 |
| random | none | 40% | spline_interpolation | 0.0849 | 0.1421 | 0.9953 | 115 | 115 |
| random | none | 40% | time_interpolation | 0.0620 | 0.0920 | 0.9980 | 115 | 115 |
| random | none | 50% | cubic_interpolation | 0.0786 | 0.1300 | 0.9959 | 144 | 144 |
| random | none | 50% | decision_tree | 0.1729 | 0.2408 | 0.9858 | 144 | 144 |
| random | none | 50% | forward_fill | 0.1549 | 0.2230 | 0.9878 | 144 | 144 |
| random | none | 50% | knn | 0.3761 | 1.0710 | 0.7197 | 144 | 144 |
| random | none | 50% | linear_interpolation | 0.0676 | 0.0984 | 0.9976 | 144 | 144 |
| random | none | 50% | random_forest | 0.2316 | 0.3004 | 0.9779 | 144 | 144 |
| random | none | 50% | spline_interpolation | 0.0788 | 0.1304 | 0.9958 | 144 | 144 |
| random | none | 50% | time_interpolation | 0.0676 | 0.0984 | 0.9976 | 144 | 144 |
| random | none | 60% | cubic_interpolation | 0.0874 | 0.1319 | 0.9960 | 173 | 173 |
| random | none | 60% | decision_tree | 0.1861 | 0.2517 | 0.9853 | 173 | 173 |
| random | none | 60% | forward_fill | 0.1648 | 0.2324 | 0.9875 | 173 | 173 |
| random | none | 60% | knn | 0.2792 | 0.7796 | 0.8592 | 173 | 173 |
| random | none | 60% | linear_interpolation | 0.0732 | 0.1053 | 0.9974 | 173 | 173 |
| random | none | 60% | random_forest | 0.2621 | 0.3375 | 0.9736 | 173 | 173 |
| random | none | 60% | spline_interpolation | 0.0876 | 0.1321 | 0.9960 | 173 | 173 |
| random | none | 60% | time_interpolation | 0.0732 | 0.1053 | 0.9974 | 173 | 173 |
| random | none | 70% | cubic_interpolation | 0.0912 | 0.1364 | 0.9956 | 202 | 202 |
| random | none | 70% | decision_tree | 0.2082 | 0.2831 | 0.9812 | 202 | 202 |
| random | none | 70% | forward_fill | 0.1722 | 0.2351 | 0.9870 | 202 | 202 |
| random | none | 70% | knn | 0.3915 | 0.8069 | 0.8472 | 202 | 202 |
| random | none | 70% | linear_interpolation | 0.0815 | 0.1119 | 0.9971 | 202 | 202 |
| random | none | 70% | random_forest | 0.2700 | 0.3794 | 0.9662 | 202 | 202 |
| random | none | 70% | spline_interpolation | 0.0913 | 0.1365 | 0.9956 | 202 | 202 |
| random | none | 70% | time_interpolation | 0.0815 | 0.1119 | 0.9971 | 202 | 202 |
| random | none | 80% | cubic_interpolation | 0.1055 | 0.1566 | 0.9944 | 230 | 230 |
| random | none | 80% | decision_tree | 0.2824 | 0.4052 | 0.9623 | 230 | 230 |
| random | none | 80% | forward_fill | 0.1970 | 0.2685 | 0.9834 | 230 | 230 |
| random | none | 80% | knn | 0.6353 | 1.0643 | 0.7398 | 230 | 230 |
| random | none | 80% | linear_interpolation | 0.0919 | 0.1259 | 0.9964 | 230 | 230 |
| random | none | 80% | random_forest | 0.2819 | 0.3783 | 0.9671 | 230 | 230 |
| random | none | 80% | spline_interpolation | 0.1056 | 0.1567 | 0.9944 | 230 | 230 |
| random | none | 80% | time_interpolation | 0.0919 | 0.1259 | 0.9964 | 230 | 230 |

---

## Random missing (`random`)

### Random missing — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | cubic_interpolation | 0.0406 | 0.0503 | 0.9993 | 29 | 29 |
| 10% | spline_interpolation | 0.0406 | 0.0503 | 0.9993 | 29 | 29 |
| 10% | linear_interpolation | 0.0471 | 0.0588 | 0.9990 | 29 | 29 |
| 10% | time_interpolation | 0.0471 | 0.0588 | 0.9990 | 29 | 29 |
| 10% | forward_fill | 0.0521 | 0.0726 | 0.9985 | 29 | 29 |
| 10% | knn | 0.0865 | 0.1110 | 0.9965 | 29 | 29 |
| 10% | decision_tree | 0.1568 | 0.1939 | 0.9893 | 29 | 29 |
| 10% | random_forest | 0.1618 | 0.2204 | 0.9862 | 29 | 29 |
| 20% | cubic_interpolation | 0.0488 | 0.0672 | 0.9987 | 58 | 58 |
| 20% | spline_interpolation | 0.0488 | 0.0672 | 0.9987 | 58 | 58 |
| 20% | linear_interpolation | 0.0502 | 0.0680 | 0.9986 | 58 | 58 |
| 20% | time_interpolation | 0.0502 | 0.0680 | 0.9986 | 58 | 58 |
| 20% | forward_fill | 0.0741 | 0.1077 | 0.9966 | 58 | 58 |
| 20% | knn | 0.0841 | 0.1068 | 0.9966 | 58 | 58 |
| 20% | decision_tree | 0.1662 | 0.2198 | 0.9858 | 58 | 58 |
| 20% | random_forest | 0.1903 | 0.2719 | 0.9782 | 58 | 58 |
| 30% | spline_interpolation | 0.0448 | 0.0606 | 0.9991 | 86 | 86 |
| 30% | cubic_interpolation | 0.0448 | 0.0606 | 0.9991 | 86 | 86 |
| 30% | linear_interpolation | 0.0502 | 0.0662 | 0.9989 | 86 | 86 |
| 30% | time_interpolation | 0.0502 | 0.0662 | 0.9989 | 86 | 86 |
| 30% | forward_fill | 0.1012 | 0.1588 | 0.9936 | 86 | 86 |
| 30% | knn | 0.1016 | 0.1422 | 0.9949 | 86 | 86 |
| 30% | decision_tree | 0.1633 | 0.2275 | 0.9869 | 86 | 86 |
| 30% | random_forest | 0.1952 | 0.2728 | 0.9812 | 86 | 86 |
| 40% | linear_interpolation | 0.0620 | 0.0920 | 0.9980 | 115 | 115 |
| 40% | time_interpolation | 0.0620 | 0.0920 | 0.9980 | 115 | 115 |
| 40% | spline_interpolation | 0.0849 | 0.1421 | 0.9953 | 115 | 115 |
| 40% | cubic_interpolation | 0.0849 | 0.1419 | 0.9953 | 115 | 115 |
| 40% | knn | 0.1304 | 0.1880 | 0.9917 | 115 | 115 |
| 40% | forward_fill | 0.1366 | 0.2002 | 0.9906 | 115 | 115 |
| 40% | decision_tree | 0.1693 | 0.2320 | 0.9874 | 115 | 115 |
| 40% | random_forest | 0.2136 | 0.2921 | 0.9801 | 115 | 115 |
| 50% | linear_interpolation | 0.0676 | 0.0984 | 0.9976 | 144 | 144 |
| 50% | time_interpolation | 0.0676 | 0.0984 | 0.9976 | 144 | 144 |
| 50% | cubic_interpolation | 0.0786 | 0.1300 | 0.9959 | 144 | 144 |
| 50% | spline_interpolation | 0.0788 | 0.1304 | 0.9958 | 144 | 144 |
| 50% | forward_fill | 0.1549 | 0.2230 | 0.9878 | 144 | 144 |
| 50% | decision_tree | 0.1729 | 0.2408 | 0.9858 | 144 | 144 |
| 50% | random_forest | 0.2316 | 0.3004 | 0.9779 | 144 | 144 |
| 50% | knn | 0.3761 | 1.0710 | 0.7197 | 144 | 144 |
| 60% | linear_interpolation | 0.0732 | 0.1053 | 0.9974 | 173 | 173 |
| 60% | time_interpolation | 0.0732 | 0.1053 | 0.9974 | 173 | 173 |
| 60% | cubic_interpolation | 0.0874 | 0.1319 | 0.9960 | 173 | 173 |
| 60% | spline_interpolation | 0.0876 | 0.1321 | 0.9960 | 173 | 173 |
| 60% | forward_fill | 0.1648 | 0.2324 | 0.9875 | 173 | 173 |
| 60% | decision_tree | 0.1861 | 0.2517 | 0.9853 | 173 | 173 |
| 60% | random_forest | 0.2621 | 0.3375 | 0.9736 | 173 | 173 |
| 60% | knn | 0.2792 | 0.7796 | 0.8592 | 173 | 173 |
| 70% | linear_interpolation | 0.0815 | 0.1119 | 0.9971 | 202 | 202 |
| 70% | time_interpolation | 0.0815 | 0.1119 | 0.9971 | 202 | 202 |
| 70% | cubic_interpolation | 0.0912 | 0.1364 | 0.9956 | 202 | 202 |
| 70% | spline_interpolation | 0.0913 | 0.1365 | 0.9956 | 202 | 202 |
| 70% | forward_fill | 0.1722 | 0.2351 | 0.9870 | 202 | 202 |
| 70% | decision_tree | 0.2082 | 0.2831 | 0.9812 | 202 | 202 |
| 70% | random_forest | 0.2700 | 0.3794 | 0.9662 | 202 | 202 |
| 70% | knn | 0.3915 | 0.8069 | 0.8472 | 202 | 202 |
| 80% | linear_interpolation | 0.0919 | 0.1259 | 0.9964 | 230 | 230 |
| 80% | time_interpolation | 0.0919 | 0.1259 | 0.9964 | 230 | 230 |
| 80% | cubic_interpolation | 0.1055 | 0.1566 | 0.9944 | 230 | 230 |
| 80% | spline_interpolation | 0.1056 | 0.1567 | 0.9944 | 230 | 230 |
| 80% | forward_fill | 0.1970 | 0.2685 | 0.9834 | 230 | 230 |
| 80% | random_forest | 0.2819 | 0.3783 | 0.9671 | 230 | 230 |
| 80% | decision_tree | 0.2824 | 0.4052 | 0.9623 | 230 | 230 |
| 80% | knn | 0.6353 | 1.0643 | 0.7398 | 230 | 230 |

### Random missing — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.0521 | 0.0741 | 0.1012 | 0.1366 | 0.1549 | 0.1648 | 0.1722 | 0.1970 |
| linear_interpolation | 0.0471 | 0.0502 | 0.0502 | 0.0620 | 0.0676 | 0.0732 | 0.0815 | 0.0919 |
| time_interpolation | 0.0471 | 0.0502 | 0.0502 | 0.0620 | 0.0676 | 0.0732 | 0.0815 | 0.0919 |
| cubic_interpolation | 0.0406 | 0.0488 | 0.0448 | 0.0849 | 0.0786 | 0.0874 | 0.0912 | 0.1055 |
| spline_interpolation | 0.0406 | 0.0488 | 0.0448 | 0.0849 | 0.0788 | 0.0876 | 0.0913 | 0.1056 |
| knn | 0.0865 | 0.0841 | 0.1016 | 0.1304 | 0.3761 | 0.2792 | 0.3915 | 0.6353 |
| decision_tree | 0.1568 | 0.1662 | 0.1633 | 0.1693 | 0.1729 | 0.1861 | 0.2082 | 0.2824 |
| random_forest | 0.1618 | 0.1903 | 0.1952 | 0.2136 | 0.2316 | 0.2621 | 0.2700 | 0.2819 |

### Random missing — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.0726 | 0.1077 | 0.1588 | 0.2002 | 0.2230 | 0.2324 | 0.2351 | 0.2685 |
| linear_interpolation | 0.0588 | 0.0680 | 0.0662 | 0.0920 | 0.0984 | 0.1053 | 0.1119 | 0.1259 |
| time_interpolation | 0.0588 | 0.0680 | 0.0662 | 0.0920 | 0.0984 | 0.1053 | 0.1119 | 0.1259 |
| cubic_interpolation | 0.0503 | 0.0672 | 0.0606 | 0.1419 | 0.1300 | 0.1319 | 0.1364 | 0.1566 |
| spline_interpolation | 0.0503 | 0.0672 | 0.0606 | 0.1421 | 0.1304 | 0.1321 | 0.1365 | 0.1567 |
| knn | 0.1110 | 0.1068 | 0.1422 | 0.1880 | 1.0710 | 0.7796 | 0.8069 | 1.0643 |
| decision_tree | 0.1939 | 0.2198 | 0.2275 | 0.2320 | 0.2408 | 0.2517 | 0.2831 | 0.4052 |
| random_forest | 0.2204 | 0.2719 | 0.2728 | 0.2921 | 0.3004 | 0.3375 | 0.3794 | 0.3783 |

### Random missing — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.9985 | 0.9966 | 0.9936 | 0.9906 | 0.9878 | 0.9875 | 0.9870 | 0.9834 |
| linear_interpolation | 0.9990 | 0.9986 | 0.9989 | 0.9980 | 0.9976 | 0.9974 | 0.9971 | 0.9964 |
| time_interpolation | 0.9990 | 0.9986 | 0.9989 | 0.9980 | 0.9976 | 0.9974 | 0.9971 | 0.9964 |
| cubic_interpolation | 0.9993 | 0.9987 | 0.9991 | 0.9953 | 0.9959 | 0.9960 | 0.9956 | 0.9944 |
| spline_interpolation | 0.9993 | 0.9987 | 0.9991 | 0.9953 | 0.9958 | 0.9960 | 0.9956 | 0.9944 |
| knn | 0.9965 | 0.9966 | 0.9949 | 0.9917 | 0.7197 | 0.8592 | 0.8472 | 0.7398 |
| decision_tree | 0.9893 | 0.9858 | 0.9869 | 0.9874 | 0.9858 | 0.9853 | 0.9812 | 0.9623 |
| random_forest | 0.9862 | 0.9782 | 0.9812 | 0.9801 | 0.9779 | 0.9736 | 0.9662 | 0.9671 |

---

## Block missing (`block`)

### Block missing — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | linear_interpolation | 0.1214 | 0.1428 | 0.4867 | 29 | 29 |
| 10% | time_interpolation | 0.1214 | 0.1428 | 0.4867 | 29 | 29 |
| 10% | decision_tree | 0.3173 | 0.3664 | -2.3806 | 29 | 29 |
| 10% | cubic_interpolation | 0.3391 | 0.3654 | -2.3624 | 29 | 29 |
| 10% | spline_interpolation | 0.3391 | 0.3654 | -2.3624 | 29 | 29 |
| 10% | forward_fill | 0.4883 | 0.5274 | -6.0048 | 29 | 29 |
| 10% | random_forest | 0.5252 | 0.5617 | -6.9477 | 29 | 29 |
| 10% | knn | 2.0580 | 2.2816 | -130.1117 | 29 | 29 |
| 20% | cubic_interpolation | 0.1946 | 0.2737 | 0.9155 | 58 | 58 |
| 20% | spline_interpolation | 0.1946 | 0.2737 | 0.9155 | 58 | 58 |
| 20% | linear_interpolation | 0.2849 | 0.3440 | 0.8666 | 58 | 58 |
| 20% | time_interpolation | 0.2849 | 0.3440 | 0.8666 | 58 | 58 |
| 20% | decision_tree | 1.2948 | 1.6011 | -1.8901 | 58 | 58 |
| 20% | forward_fill | 1.7912 | 2.0237 | -3.6173 | 58 | 58 |
| 20% | random_forest | 1.9376 | 2.1544 | -4.2328 | 58 | 58 |
| 20% | knn | 3.1533 | 3.2768 | -11.1059 | 58 | 58 |
| 30% | linear_interpolation | 0.4406 | 0.5602 | 0.5833 | 86 | 86 |
| 30% | time_interpolation | 0.4406 | 0.5602 | 0.5833 | 86 | 86 |
| 30% | cubic_interpolation | 0.4890 | 0.5492 | 0.5995 | 86 | 86 |
| 30% | spline_interpolation | 0.4890 | 0.5492 | 0.5995 | 86 | 86 |
| 30% | decision_tree | 0.7618 | 1.0070 | -0.3465 | 86 | 86 |
| 30% | random_forest | 0.9100 | 1.1784 | -0.8439 | 86 | 86 |
| 30% | forward_fill | 0.9838 | 1.2559 | -1.0942 | 86 | 86 |
| 30% | knn | 3.4313 | 3.6477 | -16.6670 | 86 | 86 |
| 40% | linear_interpolation | 0.6903 | 0.9168 | 0.6616 | 115 | 115 |
| 40% | time_interpolation | 0.6903 | 0.9168 | 0.6616 | 115 | 115 |
| 40% | spline_interpolation | 1.1448 | 1.3846 | 0.2281 | 115 | 115 |
| 40% | cubic_interpolation | 1.1989 | 1.4507 | 0.1526 | 115 | 115 |
| 40% | random_forest | 1.3887 | 1.5848 | -0.0113 | 115 | 115 |
| 40% | forward_fill | 1.6503 | 2.0226 | -0.6472 | 115 | 115 |
| 40% | decision_tree | 2.3168 | 2.8002 | -2.1573 | 115 | 115 |
| 40% | knn | 3.4468 | 3.6493 | -4.3622 | 115 | 115 |
| 50% | forward_fill | 0.6913 | 0.8919 | -0.3307 | 144 | 144 |
| 50% | decision_tree | 0.7364 | 0.9967 | -0.6617 | 144 | 144 |
| 50% | linear_interpolation | 0.7461 | 0.9694 | -0.5720 | 144 | 144 |
| 50% | time_interpolation | 0.7461 | 0.9694 | -0.5720 | 144 | 144 |
| 50% | random_forest | 0.8577 | 1.1304 | -1.1375 | 144 | 144 |
| 50% | cubic_interpolation | 1.8066 | 2.3389 | -8.1503 | 144 | 144 |
| 50% | spline_interpolation | 1.8066 | 2.3389 | -8.1505 | 144 | 144 |
| 50% | knn | 3.0574 | 3.3506 | -17.7785 | 144 | 144 |
| 60% | linear_interpolation | 0.6108 | 0.7029 | 0.6128 | 173 | 173 |
| 60% | time_interpolation | 0.6108 | 0.7029 | 0.6128 | 173 | 173 |
| 60% | cubic_interpolation | 1.8053 | 2.2680 | -3.0313 | 173 | 173 |
| 60% | spline_interpolation | 1.8053 | 2.2680 | -3.0313 | 173 | 173 |
| 60% | decision_tree | 1.8812 | 2.1340 | -2.5693 | 173 | 173 |
| 60% | knn | 2.5015 | 3.0034 | -6.0699 | 173 | 173 |
| 60% | random_forest | 2.7205 | 2.9406 | -5.7773 | 173 | 173 |
| 60% | forward_fill | 2.8020 | 3.0187 | -6.1420 | 173 | 173 |
| 70% | linear_interpolation | 0.7720 | 0.8781 | 0.4953 | 202 | 202 |
| 70% | time_interpolation | 0.7720 | 0.8781 | 0.4953 | 202 | 202 |
| 70% | decision_tree | 1.3845 | 1.6836 | -0.8551 | 202 | 202 |
| 70% | cubic_interpolation | 1.7745 | 2.0544 | -1.7625 | 202 | 202 |
| 70% | spline_interpolation | 1.7745 | 2.0544 | -1.7625 | 202 | 202 |
| 70% | knn | 2.3487 | 2.9056 | -4.5255 | 202 | 202 |
| 70% | forward_fill | 2.6239 | 2.8791 | -4.4254 | 202 | 202 |
| 70% | random_forest | 2.6946 | 2.9494 | -4.6935 | 202 | 202 |
| 80% | linear_interpolation | 0.6705 | 0.9274 | 0.7914 | 230 | 230 |
| 80% | time_interpolation | 0.6705 | 0.9274 | 0.7914 | 230 | 230 |
| 80% | cubic_interpolation | 1.8285 | 2.2010 | -0.1746 | 230 | 230 |
| 80% | spline_interpolation | 1.8286 | 2.2011 | -0.1747 | 230 | 230 |
| 80% | knn | 1.9468 | 2.3307 | -0.3171 | 230 | 230 |
| 80% | forward_fill | 2.5757 | 2.9049 | -1.0461 | 230 | 230 |
| 80% | random_forest | 2.5757 | 2.9049 | -1.0461 | 230 | 230 |
| 80% | decision_tree | 2.8560 | 3.4613 | -1.9050 | 230 | 230 |

### Block missing — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.4883 | 1.7912 | 0.9838 | 1.6503 | 0.6913 | 2.8020 | 2.6239 | 2.5757 |
| linear_interpolation | 0.1214 | 0.2849 | 0.4406 | 0.6903 | 0.7461 | 0.6108 | 0.7720 | 0.6705 |
| time_interpolation | 0.1214 | 0.2849 | 0.4406 | 0.6903 | 0.7461 | 0.6108 | 0.7720 | 0.6705 |
| cubic_interpolation | 0.3391 | 0.1946 | 0.4890 | 1.1989 | 1.8066 | 1.8053 | 1.7745 | 1.8285 |
| spline_interpolation | 0.3391 | 0.1946 | 0.4890 | 1.1448 | 1.8066 | 1.8053 | 1.7745 | 1.8286 |
| knn | 2.0580 | 3.1533 | 3.4313 | 3.4468 | 3.0574 | 2.5015 | 2.3487 | 1.9468 |
| decision_tree | 0.3173 | 1.2948 | 0.7618 | 2.3168 | 0.7364 | 1.8812 | 1.3845 | 2.8560 |
| random_forest | 0.5252 | 1.9376 | 0.9100 | 1.3887 | 0.8577 | 2.7205 | 2.6946 | 2.5757 |

### Block missing — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.5274 | 2.0237 | 1.2559 | 2.0226 | 0.8919 | 3.0187 | 2.8791 | 2.9049 |
| linear_interpolation | 0.1428 | 0.3440 | 0.5602 | 0.9168 | 0.9694 | 0.7029 | 0.8781 | 0.9274 |
| time_interpolation | 0.1428 | 0.3440 | 0.5602 | 0.9168 | 0.9694 | 0.7029 | 0.8781 | 0.9274 |
| cubic_interpolation | 0.3654 | 0.2737 | 0.5492 | 1.4507 | 2.3389 | 2.2680 | 2.0544 | 2.2010 |
| spline_interpolation | 0.3654 | 0.2737 | 0.5492 | 1.3846 | 2.3389 | 2.2680 | 2.0544 | 2.2011 |
| knn | 2.2816 | 3.2768 | 3.6477 | 3.6493 | 3.3506 | 3.0034 | 2.9056 | 2.3307 |
| decision_tree | 0.3664 | 1.6011 | 1.0070 | 2.8002 | 0.9967 | 2.1340 | 1.6836 | 3.4613 |
| random_forest | 0.5617 | 2.1544 | 1.1784 | 1.5848 | 1.1304 | 2.9406 | 2.9494 | 2.9049 |

### Block missing — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -6.0048 | -3.6173 | -1.0942 | -0.6472 | -0.3307 | -6.1420 | -4.4254 | -1.0461 |
| linear_interpolation | 0.4867 | 0.8666 | 0.5833 | 0.6616 | -0.5720 | 0.6128 | 0.4953 | 0.7914 |
| time_interpolation | 0.4867 | 0.8666 | 0.5833 | 0.6616 | -0.5720 | 0.6128 | 0.4953 | 0.7914 |
| cubic_interpolation | -2.3624 | 0.9155 | 0.5995 | 0.1526 | -8.1503 | -3.0313 | -1.7625 | -0.1746 |
| spline_interpolation | -2.3624 | 0.9155 | 0.5995 | 0.2281 | -8.1505 | -3.0313 | -1.7625 | -0.1747 |
| knn | -130.1117 | -11.1059 | -16.6670 | -4.3622 | -17.7785 | -6.0699 | -4.5255 | -0.3171 |
| decision_tree | -2.3806 | -1.8901 | -0.3465 | -2.1573 | -0.6617 | -2.5693 | -0.8551 | -1.9050 |
| random_forest | -6.9477 | -4.2328 | -0.8439 | -0.0113 | -1.1375 | -5.7773 | -4.6935 | -1.0461 |

---

## Block na početku (`block_start`)

### Block na početku — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | linear_interpolation | 0.2212 | 0.2870 | 0.6913 | 29 | 29 |
| 10% | time_interpolation | 0.2212 | 0.2870 | 0.6913 | 29 | 29 |
| 10% | cubic_interpolation | 0.4806 | 0.5507 | -0.1368 | 29 | 29 |
| 10% | random_forest | 0.4947 | 0.5892 | -0.3013 | 29 | 29 |
| 10% | spline_interpolation | 0.5369 | 0.6085 | -0.3880 | 29 | 29 |
| 10% | decision_tree | 0.7110 | 0.8111 | -1.4658 | 29 | 29 |
| 10% | forward_fill | 0.7866 | 0.8892 | -1.9636 | 29 | 29 |
| 10% | knn | 3.6560 | 3.9546 | -57.6198 | 29 | 29 |
| 20% | forward_fill | 0.8097 | 0.9592 | -0.7258 | 58 | 58 |
| 20% | spline_interpolation | 0.9311 | 1.0954 | -1.2504 | 58 | 58 |
| 20% | random_forest | 1.0161 | 1.1934 | -1.6710 | 58 | 58 |
| 20% | cubic_interpolation | 1.0331 | 1.2093 | -1.7426 | 58 | 58 |
| 20% | linear_interpolation | 1.1335 | 1.3189 | -2.2624 | 58 | 58 |
| 20% | time_interpolation | 1.1335 | 1.3189 | -2.2624 | 58 | 58 |
| 20% | decision_tree | 1.4746 | 1.6829 | -4.3117 | 58 | 58 |
| 20% | knn | 4.0126 | 4.1607 | -31.4677 | 58 | 58 |
| 30% | spline_interpolation | 0.9713 | 1.1943 | -0.0214 | 86 | 86 |
| 30% | forward_fill | 1.0057 | 1.1824 | -0.0012 | 86 | 86 |
| 30% | cubic_interpolation | 1.1125 | 1.3589 | -0.3223 | 86 | 86 |
| 30% | linear_interpolation | 1.1155 | 1.3455 | -0.2964 | 86 | 86 |
| 30% | time_interpolation | 1.1155 | 1.3455 | -0.2964 | 86 | 86 |
| 30% | random_forest | 1.2255 | 1.4521 | -0.5100 | 86 | 86 |
| 30% | decision_tree | 1.6348 | 1.8912 | -1.5613 | 86 | 86 |
| 30% | knn | 3.7127 | 3.9081 | -9.9374 | 86 | 86 |
| 40% | linear_interpolation | 0.8763 | 1.1887 | 0.4144 | 115 | 115 |
| 40% | time_interpolation | 0.8763 | 1.1887 | 0.4144 | 115 | 115 |
| 40% | forward_fill | 1.4386 | 1.7107 | -0.2128 | 115 | 115 |
| 40% | random_forest | 1.5356 | 1.7611 | -0.2853 | 115 | 115 |
| 40% | decision_tree | 1.6954 | 2.0516 | -0.7443 | 115 | 115 |
| 40% | cubic_interpolation | 1.9440 | 2.1614 | -0.9359 | 115 | 115 |
| 40% | spline_interpolation | 2.2900 | 2.5576 | -1.7108 | 115 | 115 |
| 40% | knn | 3.4647 | 3.6508 | -4.5235 | 115 | 115 |
| 50% | linear_interpolation | 0.7737 | 1.0082 | 0.6682 | 144 | 144 |
| 50% | time_interpolation | 0.7737 | 1.0082 | 0.6682 | 144 | 144 |
| 50% | cubic_interpolation | 1.0440 | 1.3250 | 0.4269 | 144 | 144 |
| 50% | spline_interpolation | 1.1219 | 1.4115 | 0.3497 | 144 | 144 |
| 50% | decision_tree | 1.6370 | 2.0098 | -0.3185 | 144 | 144 |
| 50% | random_forest | 1.6998 | 1.8797 | -0.1533 | 144 | 144 |
| 50% | forward_fill | 1.8256 | 2.1502 | -0.5091 | 144 | 144 |
| 50% | knn | 2.9592 | 3.3045 | -2.5642 | 144 | 144 |
| 60% | linear_interpolation | 0.9158 | 1.0451 | 0.6670 | 173 | 173 |
| 60% | time_interpolation | 0.9158 | 1.0451 | 0.6670 | 173 | 173 |
| 60% | random_forest | 1.4247 | 1.7191 | 0.0991 | 173 | 173 |
| 60% | decision_tree | 1.5867 | 1.8727 | -0.0691 | 173 | 173 |
| 60% | forward_fill | 2.1107 | 2.4371 | -0.8106 | 173 | 173 |
| 60% | cubic_interpolation | 2.4579 | 2.8602 | -1.4938 | 173 | 173 |
| 60% | knn | 2.4720 | 2.9078 | -1.5774 | 173 | 173 |
| 60% | spline_interpolation | 3.0857 | 3.6795 | -3.1269 | 173 | 173 |
| 70% | linear_interpolation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| 70% | time_interpolation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| 70% | cubic_interpolation | 1.6762 | 1.7713 | 0.0624 | 202 | 202 |
| 70% | random_forest | 2.0780 | 2.3135 | -0.5994 | 202 | 202 |
| 70% | decision_tree | 2.0837 | 2.6150 | -1.0435 | 202 | 202 |
| 70% | spline_interpolation | 2.1933 | 2.3259 | -0.6166 | 202 | 202 |
| 70% | knn | 2.2064 | 2.7076 | -1.1908 | 202 | 202 |
| 70% | forward_fill | 2.3393 | 2.6579 | -1.1111 | 202 | 202 |
| 80% | linear_interpolation | 0.6939 | 0.9373 | 0.7794 | 230 | 230 |
| 80% | time_interpolation | 0.6939 | 0.9373 | 0.7794 | 230 | 230 |
| 80% | spline_interpolation | 0.8830 | 1.1028 | 0.6945 | 230 | 230 |
| 80% | cubic_interpolation | 1.0307 | 1.2238 | 0.6238 | 230 | 230 |
| 80% | random_forest | 1.7179 | 2.4124 | -0.4617 | 230 | 230 |
| 80% | knn | 2.2679 | 2.8132 | -0.9877 | 230 | 230 |
| 80% | forward_fill | 2.6620 | 3.0456 | -1.3297 | 230 | 230 |
| 80% | decision_tree | 3.0026 | 3.5665 | -2.1947 | 230 | 230 |

### Block na početku — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.7866 | 0.8097 | 1.0057 | 1.4386 | 1.8256 | 2.1107 | 2.3393 | 2.6620 |
| linear_interpolation | 0.2212 | 1.1335 | 1.1155 | 0.8763 | 0.7737 | 0.9158 | 0.6991 | 0.6939 |
| time_interpolation | 0.2212 | 1.1335 | 1.1155 | 0.8763 | 0.7737 | 0.9158 | 0.6991 | 0.6939 |
| cubic_interpolation | 0.4806 | 1.0331 | 1.1125 | 1.9440 | 1.0440 | 2.4579 | 1.6762 | 1.0307 |
| spline_interpolation | 0.5369 | 0.9311 | 0.9713 | 2.2900 | 1.1219 | 3.0857 | 2.1933 | 0.8830 |
| knn | 3.6560 | 4.0126 | 3.7127 | 3.4647 | 2.9592 | 2.4720 | 2.2064 | 2.2679 |
| decision_tree | 0.7110 | 1.4746 | 1.6348 | 1.6954 | 1.6370 | 1.5867 | 2.0837 | 3.0026 |
| random_forest | 0.4947 | 1.0161 | 1.2255 | 1.5356 | 1.6998 | 1.4247 | 2.0780 | 1.7179 |

### Block na početku — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.8892 | 0.9592 | 1.1824 | 1.7107 | 2.1502 | 2.4371 | 2.6579 | 3.0456 |
| linear_interpolation | 0.2870 | 1.3189 | 1.3455 | 1.1887 | 1.0082 | 1.0451 | 0.8889 | 0.9373 |
| time_interpolation | 0.2870 | 1.3189 | 1.3455 | 1.1887 | 1.0082 | 1.0451 | 0.8889 | 0.9373 |
| cubic_interpolation | 0.5507 | 1.2093 | 1.3589 | 2.1614 | 1.3250 | 2.8602 | 1.7713 | 1.2238 |
| spline_interpolation | 0.6085 | 1.0954 | 1.1943 | 2.5576 | 1.4115 | 3.6795 | 2.3259 | 1.1028 |
| knn | 3.9546 | 4.1607 | 3.9081 | 3.6508 | 3.3045 | 2.9078 | 2.7076 | 2.8132 |
| decision_tree | 0.8111 | 1.6829 | 1.8912 | 2.0516 | 2.0098 | 1.8727 | 2.6150 | 3.5665 |
| random_forest | 0.5892 | 1.1934 | 1.4521 | 1.7611 | 1.8797 | 1.7191 | 2.3135 | 2.4124 |

### Block na početku — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -1.9636 | -0.7258 | -0.0012 | -0.2128 | -0.5091 | -0.8106 | -1.1111 | -1.3297 |
| linear_interpolation | 0.6913 | -2.2624 | -0.2964 | 0.4144 | 0.6682 | 0.6670 | 0.7639 | 0.7794 |
| time_interpolation | 0.6913 | -2.2624 | -0.2964 | 0.4144 | 0.6682 | 0.6670 | 0.7639 | 0.7794 |
| cubic_interpolation | -0.1368 | -1.7426 | -0.3223 | -0.9359 | 0.4269 | -1.4938 | 0.0624 | 0.6238 |
| spline_interpolation | -0.3880 | -1.2504 | -0.0214 | -1.7108 | 0.3497 | -3.1269 | -0.6166 | 0.6945 |
| knn | -57.6198 | -31.4677 | -9.9374 | -4.5235 | -2.5642 | -1.5774 | -1.1908 | -0.9877 |
| decision_tree | -1.4658 | -4.3117 | -1.5613 | -0.7443 | -0.3185 | -0.0691 | -1.0435 | -2.1947 |
| random_forest | -0.3013 | -1.6710 | -0.5100 | -0.2853 | -0.1533 | 0.0991 | -0.5994 | -0.4617 |

---

## Block u sredini (`block_middle`)

### Block u sredini — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | decision_tree | 0.1081 | 0.1322 | 0.1342 | 29 | 29 |
| 10% | cubic_interpolation | 0.1513 | 0.1870 | -0.7331 | 29 | 29 |
| 10% | spline_interpolation | 0.1513 | 0.1870 | -0.7331 | 29 | 29 |
| 10% | linear_interpolation | 0.1674 | 0.2230 | -1.4652 | 29 | 29 |
| 10% | time_interpolation | 0.1674 | 0.2230 | -1.4652 | 29 | 29 |
| 10% | random_forest | 0.3726 | 0.3987 | -6.8806 | 29 | 29 |
| 10% | forward_fill | 0.4234 | 0.4466 | -8.8880 | 29 | 29 |
| 10% | knn | 1.4963 | 2.2245 | -244.2807 | 29 | 29 |
| 20% | forward_fill | 0.3384 | 0.4029 | -1.8616 | 58 | 58 |
| 20% | decision_tree | 0.3651 | 0.4303 | -2.2631 | 58 | 58 |
| 20% | linear_interpolation | 0.3654 | 0.4325 | -2.2972 | 58 | 58 |
| 20% | time_interpolation | 0.3654 | 0.4325 | -2.2972 | 58 | 58 |
| 20% | random_forest | 0.6154 | 0.6599 | -6.6742 | 58 | 58 |
| 20% | cubic_interpolation | 1.0215 | 1.2310 | -25.7088 | 58 | 58 |
| 20% | spline_interpolation | 1.0215 | 1.2310 | -25.7088 | 58 | 58 |
| 20% | knn | 2.4358 | 3.0429 | -162.1881 | 58 | 58 |
| 30% | linear_interpolation | 0.2554 | 0.3052 | 0.1034 | 86 | 86 |
| 30% | time_interpolation | 0.2554 | 0.3052 | 0.1034 | 86 | 86 |
| 30% | forward_fill | 0.6723 | 0.7427 | -4.3078 | 86 | 86 |
| 30% | random_forest | 0.6738 | 0.7441 | -4.3276 | 86 | 86 |
| 30% | decision_tree | 0.8338 | 1.2512 | -14.0659 | 86 | 86 |
| 30% | cubic_interpolation | 1.2902 | 1.4448 | -19.0888 | 86 | 86 |
| 30% | spline_interpolation | 1.2902 | 1.4448 | -19.0888 | 86 | 86 |
| 30% | knn | 2.7403 | 3.2364 | -99.7954 | 86 | 86 |
| 40% | linear_interpolation | 0.2665 | 0.3092 | 0.4961 | 115 | 115 |
| 40% | time_interpolation | 0.2665 | 0.3092 | 0.4961 | 115 | 115 |
| 40% | cubic_interpolation | 0.7192 | 0.7955 | -2.3344 | 115 | 115 |
| 40% | spline_interpolation | 0.7192 | 0.7955 | -2.3344 | 115 | 115 |
| 40% | decision_tree | 0.7853 | 0.8976 | -3.2450 | 115 | 115 |
| 40% | forward_fill | 1.0452 | 1.1324 | -5.7561 | 115 | 115 |
| 40% | random_forest | 1.1690 | 1.2475 | -7.2003 | 115 | 115 |
| 40% | knn | 2.7436 | 3.1944 | -52.7663 | 115 | 115 |
| 50% | linear_interpolation | 0.5473 | 0.5987 | 0.2720 | 144 | 144 |
| 50% | time_interpolation | 0.5473 | 0.5987 | 0.2720 | 144 | 144 |
| 50% | cubic_interpolation | 0.9723 | 1.1106 | -1.5050 | 144 | 144 |
| 50% | spline_interpolation | 0.9723 | 1.1106 | -1.5050 | 144 | 144 |
| 50% | decision_tree | 1.8916 | 2.0175 | -7.2665 | 144 | 144 |
| 50% | forward_fill | 2.1344 | 2.2468 | -9.2525 | 144 | 144 |
| 50% | random_forest | 2.3135 | 2.4175 | -10.8696 | 144 | 144 |
| 50% | knn | 2.9208 | 3.2727 | -20.7521 | 144 | 144 |
| 60% | linear_interpolation | 0.5395 | 0.6247 | 0.7016 | 173 | 173 |
| 60% | time_interpolation | 0.5395 | 0.6247 | 0.7016 | 173 | 173 |
| 60% | forward_fill | 2.5203 | 2.7622 | -4.8346 | 173 | 173 |
| 60% | knn | 2.6008 | 3.0483 | -6.1057 | 173 | 173 |
| 60% | decision_tree | 2.6106 | 2.8501 | -5.2117 | 173 | 173 |
| 60% | random_forest | 2.7120 | 2.9432 | -5.6244 | 173 | 173 |
| 60% | cubic_interpolation | 5.8078 | 6.2969 | -29.3209 | 173 | 173 |
| 60% | spline_interpolation | 5.8078 | 6.2969 | -29.3209 | 173 | 173 |
| 70% | linear_interpolation | 0.9671 | 1.1303 | 0.4191 | 202 | 202 |
| 70% | time_interpolation | 0.9671 | 1.1303 | 0.4191 | 202 | 202 |
| 70% | decision_tree | 1.9831 | 2.3853 | -1.5871 | 202 | 202 |
| 70% | knn | 2.5298 | 3.0901 | -3.3420 | 202 | 202 |
| 70% | forward_fill | 3.8817 | 4.1554 | -6.8516 | 202 | 202 |
| 70% | random_forest | 4.1547 | 4.4114 | -7.8491 | 202 | 202 |
| 70% | cubic_interpolation | 8.6021 | 9.6499 | -41.3432 | 202 | 202 |
| 70% | spline_interpolation | 8.6021 | 9.6499 | -41.3432 | 202 | 202 |
| 80% | linear_interpolation | 1.4370 | 1.5759 | 0.2636 | 230 | 230 |
| 80% | time_interpolation | 1.4370 | 1.5759 | 0.2636 | 230 | 230 |
| 80% | decision_tree | 1.8817 | 2.4652 | -0.8021 | 230 | 230 |
| 80% | knn | 2.3632 | 2.9842 | -1.6407 | 230 | 230 |
| 80% | random_forest | 4.4352 | 4.7827 | -5.7827 | 230 | 230 |
| 80% | forward_fill | 4.4810 | 4.8282 | -5.9124 | 230 | 230 |
| 80% | cubic_interpolation | 5.3329 | 6.1881 | -10.3548 | 230 | 230 |
| 80% | spline_interpolation | 5.3329 | 6.1881 | -10.3548 | 230 | 230 |

### Block u sredini — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.4234 | 0.3384 | 0.6723 | 1.0452 | 2.1344 | 2.5203 | 3.8817 | 4.4810 |
| linear_interpolation | 0.1674 | 0.3654 | 0.2554 | 0.2665 | 0.5473 | 0.5395 | 0.9671 | 1.4370 |
| time_interpolation | 0.1674 | 0.3654 | 0.2554 | 0.2665 | 0.5473 | 0.5395 | 0.9671 | 1.4370 |
| cubic_interpolation | 0.1513 | 1.0215 | 1.2902 | 0.7192 | 0.9723 | 5.8078 | 8.6021 | 5.3329 |
| spline_interpolation | 0.1513 | 1.0215 | 1.2902 | 0.7192 | 0.9723 | 5.8078 | 8.6021 | 5.3329 |
| knn | 1.4963 | 2.4358 | 2.7403 | 2.7436 | 2.9208 | 2.6008 | 2.5298 | 2.3632 |
| decision_tree | 0.1081 | 0.3651 | 0.8338 | 0.7853 | 1.8916 | 2.6106 | 1.9831 | 1.8817 |
| random_forest | 0.3726 | 0.6154 | 0.6738 | 1.1690 | 2.3135 | 2.7120 | 4.1547 | 4.4352 |

### Block u sredini — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.4466 | 0.4029 | 0.7427 | 1.1324 | 2.2468 | 2.7622 | 4.1554 | 4.8282 |
| linear_interpolation | 0.2230 | 0.4325 | 0.3052 | 0.3092 | 0.5987 | 0.6247 | 1.1303 | 1.5759 |
| time_interpolation | 0.2230 | 0.4325 | 0.3052 | 0.3092 | 0.5987 | 0.6247 | 1.1303 | 1.5759 |
| cubic_interpolation | 0.1870 | 1.2310 | 1.4448 | 0.7955 | 1.1106 | 6.2969 | 9.6499 | 6.1881 |
| spline_interpolation | 0.1870 | 1.2310 | 1.4448 | 0.7955 | 1.1106 | 6.2969 | 9.6499 | 6.1881 |
| knn | 2.2245 | 3.0429 | 3.2364 | 3.1944 | 3.2727 | 3.0483 | 3.0901 | 2.9842 |
| decision_tree | 0.1322 | 0.4303 | 1.2512 | 0.8976 | 2.0175 | 2.8501 | 2.3853 | 2.4652 |
| random_forest | 0.3987 | 0.6599 | 0.7441 | 1.2475 | 2.4175 | 2.9432 | 4.4114 | 4.7827 |

### Block u sredini — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -8.8880 | -1.8616 | -4.3078 | -5.7561 | -9.2525 | -4.8346 | -6.8516 | -5.9124 |
| linear_interpolation | -1.4652 | -2.2972 | 0.1034 | 0.4961 | 0.2720 | 0.7016 | 0.4191 | 0.2636 |
| time_interpolation | -1.4652 | -2.2972 | 0.1034 | 0.4961 | 0.2720 | 0.7016 | 0.4191 | 0.2636 |
| cubic_interpolation | -0.7331 | -25.7088 | -19.0888 | -2.3344 | -1.5050 | -29.3209 | -41.3432 | -10.3548 |
| spline_interpolation | -0.7331 | -25.7088 | -19.0888 | -2.3344 | -1.5050 | -29.3209 | -41.3432 | -10.3548 |
| knn | -244.2807 | -162.1881 | -99.7954 | -52.7663 | -20.7521 | -6.1057 | -3.3420 | -1.6407 |
| decision_tree | 0.1342 | -2.2631 | -14.0659 | -3.2450 | -7.2665 | -5.2117 | -1.5871 | -0.8021 |
| random_forest | -6.8806 | -6.6742 | -4.3276 | -7.2003 | -10.8696 | -5.6244 | -7.8491 | -5.7827 |

---

## Block na kraju (`block_end`)

### Block na kraju — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | cubic_interpolation | 0.1812 | 0.2320 | 0.7683 | 29 | 29 |
| 10% | linear_interpolation | 0.1970 | 0.2523 | 0.7258 | 29 | 29 |
| 10% | time_interpolation | 0.1970 | 0.2523 | 0.7258 | 29 | 29 |
| 10% | spline_interpolation | 0.2195 | 0.2765 | 0.6707 | 29 | 29 |
| 10% | forward_fill | 0.5000 | 0.6880 | -1.0382 | 29 | 29 |
| 10% | decision_tree | 0.5777 | 0.7523 | -1.4371 | 29 | 29 |
| 10% | knn | 0.6262 | 0.8969 | -2.4639 | 29 | 29 |
| 10% | random_forest | 0.8392 | 0.9678 | -3.0328 | 29 | 29 |
| 20% | cubic_interpolation | 0.3076 | 0.3514 | 0.7268 | 58 | 58 |
| 20% | linear_interpolation | 0.3538 | 0.3940 | 0.6565 | 58 | 58 |
| 20% | time_interpolation | 0.3538 | 0.3940 | 0.6565 | 58 | 58 |
| 20% | spline_interpolation | 0.4108 | 0.4501 | 0.5516 | 58 | 58 |
| 20% | decision_tree | 0.7769 | 0.9023 | -0.8017 | 58 | 58 |
| 20% | forward_fill | 0.7819 | 0.9642 | -1.0573 | 58 | 58 |
| 20% | random_forest | 0.8945 | 1.0807 | -1.5848 | 58 | 58 |
| 20% | knn | 1.4977 | 1.7814 | -6.0227 | 58 | 58 |
| 30% | spline_interpolation | 0.6671 | 0.7697 | -0.4063 | 86 | 86 |
| 30% | cubic_interpolation | 0.7642 | 0.8689 | -0.7920 | 86 | 86 |
| 30% | forward_fill | 0.7772 | 0.9142 | -0.9836 | 86 | 86 |
| 30% | random_forest | 1.0321 | 1.1827 | -2.3205 | 86 | 86 |
| 30% | decision_tree | 1.0387 | 1.1565 | -2.1745 | 86 | 86 |
| 30% | linear_interpolation | 1.0496 | 1.1980 | -2.4069 | 86 | 86 |
| 30% | time_interpolation | 1.0496 | 1.1980 | -2.4069 | 86 | 86 |
| 30% | knn | 2.2341 | 2.5644 | -14.6091 | 86 | 86 |
| 40% | random_forest | 1.0260 | 1.2487 | -1.7082 | 115 | 115 |
| 40% | decision_tree | 1.1899 | 1.4157 | -2.4808 | 115 | 115 |
| 40% | linear_interpolation | 1.2481 | 1.4505 | -2.6540 | 115 | 115 |
| 40% | time_interpolation | 1.2481 | 1.4505 | -2.6540 | 115 | 115 |
| 40% | forward_fill | 1.3230 | 1.5207 | -3.0167 | 115 | 115 |
| 40% | cubic_interpolation | 2.3721 | 2.6629 | -11.3162 | 115 | 115 |
| 40% | knn | 2.7625 | 3.0981 | -15.6708 | 115 | 115 |
| 40% | spline_interpolation | 2.9237 | 3.2509 | -17.3551 | 115 | 115 |
| 50% | decision_tree | 0.8176 | 1.0873 | -0.9642 | 144 | 144 |
| 50% | forward_fill | 0.8833 | 1.1522 | -1.2055 | 144 | 144 |
| 50% | random_forest | 0.9334 | 1.2041 | -1.4088 | 144 | 144 |
| 50% | linear_interpolation | 0.9438 | 1.2138 | -1.4476 | 144 | 144 |
| 50% | time_interpolation | 0.9438 | 1.2138 | -1.4476 | 144 | 144 |
| 50% | knn | 3.0573 | 3.3505 | -17.6510 | 144 | 144 |
| 50% | cubic_interpolation | 4.5362 | 5.0518 | -41.4015 | 144 | 144 |
| 50% | spline_interpolation | 6.3491 | 6.9499 | -79.2497 | 144 | 144 |
| 60% | spline_interpolation | 0.7227 | 0.8186 | -0.0491 | 173 | 173 |
| 60% | cubic_interpolation | 0.8052 | 0.9921 | -0.5409 | 173 | 173 |
| 60% | linear_interpolation | 1.0220 | 1.2567 | -1.4729 | 173 | 173 |
| 60% | time_interpolation | 1.0220 | 1.2567 | -1.4729 | 173 | 173 |
| 60% | decision_tree | 1.0997 | 1.3593 | -1.8929 | 173 | 173 |
| 60% | random_forest | 1.1813 | 1.4262 | -2.1849 | 173 | 173 |
| 60% | forward_fill | 1.2220 | 1.4601 | -2.3382 | 173 | 173 |
| 60% | knn | 3.0490 | 3.3249 | -16.3091 | 173 | 173 |
| 70% | linear_interpolation | 1.1760 | 1.3635 | -1.2691 | 202 | 202 |
| 70% | time_interpolation | 1.1760 | 1.3635 | -1.2691 | 202 | 202 |
| 70% | decision_tree | 1.4107 | 1.6652 | -2.3843 | 202 | 202 |
| 70% | forward_fill | 1.7410 | 1.9622 | -3.6996 | 202 | 202 |
| 70% | random_forest | 1.8083 | 2.0222 | -3.9910 | 202 | 202 |
| 70% | cubic_interpolation | 1.9274 | 2.2346 | -5.0946 | 202 | 202 |
| 70% | spline_interpolation | 2.6468 | 3.1874 | -11.4000 | 202 | 202 |
| 70% | knn | 3.2164 | 3.4458 | -13.4922 | 202 | 202 |
| 80% | linear_interpolation | 1.5937 | 1.7404 | -1.0366 | 230 | 230 |
| 80% | time_interpolation | 1.5937 | 1.7404 | -1.0366 | 230 | 230 |
| 80% | decision_tree | 2.1961 | 2.4319 | -2.9762 | 230 | 230 |
| 80% | forward_fill | 2.8784 | 3.1220 | -5.5534 | 230 | 230 |
| 80% | random_forest | 3.0300 | 3.2659 | -6.1715 | 230 | 230 |
| 80% | knn | 3.5170 | 3.7468 | -8.4386 | 230 | 230 |
| 80% | cubic_interpolation | 4.0390 | 4.8866 | -15.0551 | 230 | 230 |
| 80% | spline_interpolation | 6.4665 | 7.3344 | -35.1676 | 230 | 230 |

### Block na kraju — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.5000 | 0.7819 | 0.7772 | 1.3230 | 0.8833 | 1.2220 | 1.7410 | 2.8784 |
| linear_interpolation | 0.1970 | 0.3538 | 1.0496 | 1.2481 | 0.9438 | 1.0220 | 1.1760 | 1.5937 |
| time_interpolation | 0.1970 | 0.3538 | 1.0496 | 1.2481 | 0.9438 | 1.0220 | 1.1760 | 1.5937 |
| cubic_interpolation | 0.1812 | 0.3076 | 0.7642 | 2.3721 | 4.5362 | 0.8052 | 1.9274 | 4.0390 |
| spline_interpolation | 0.2195 | 0.4108 | 0.6671 | 2.9237 | 6.3491 | 0.7227 | 2.6468 | 6.4665 |
| knn | 0.6262 | 1.4977 | 2.2341 | 2.7625 | 3.0573 | 3.0490 | 3.2164 | 3.5170 |
| decision_tree | 0.5777 | 0.7769 | 1.0387 | 1.1899 | 0.8176 | 1.0997 | 1.4107 | 2.1961 |
| random_forest | 0.8392 | 0.8945 | 1.0321 | 1.0260 | 0.9334 | 1.1813 | 1.8083 | 3.0300 |

### Block na kraju — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.6880 | 0.9642 | 0.9142 | 1.5207 | 1.1522 | 1.4601 | 1.9622 | 3.1220 |
| linear_interpolation | 0.2523 | 0.3940 | 1.1980 | 1.4505 | 1.2138 | 1.2567 | 1.3635 | 1.7404 |
| time_interpolation | 0.2523 | 0.3940 | 1.1980 | 1.4505 | 1.2138 | 1.2567 | 1.3635 | 1.7404 |
| cubic_interpolation | 0.2320 | 0.3514 | 0.8689 | 2.6629 | 5.0518 | 0.9921 | 2.2346 | 4.8866 |
| spline_interpolation | 0.2765 | 0.4501 | 0.7697 | 3.2509 | 6.9499 | 0.8186 | 3.1874 | 7.3344 |
| knn | 0.8969 | 1.7814 | 2.5644 | 3.0981 | 3.3505 | 3.3249 | 3.4458 | 3.7468 |
| decision_tree | 0.7523 | 0.9023 | 1.1565 | 1.4157 | 1.0873 | 1.3593 | 1.6652 | 2.4319 |
| random_forest | 0.9678 | 1.0807 | 1.1827 | 1.2487 | 1.2041 | 1.4262 | 2.0222 | 3.2659 |

### Block na kraju — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -1.0382 | -1.0573 | -0.9836 | -3.0167 | -1.2055 | -2.3382 | -3.6996 | -5.5534 |
| linear_interpolation | 0.7258 | 0.6565 | -2.4069 | -2.6540 | -1.4476 | -1.4729 | -1.2691 | -1.0366 |
| time_interpolation | 0.7258 | 0.6565 | -2.4069 | -2.6540 | -1.4476 | -1.4729 | -1.2691 | -1.0366 |
| cubic_interpolation | 0.7683 | 0.7268 | -0.7920 | -11.3162 | -41.4015 | -0.5409 | -5.0946 | -15.0551 |
| spline_interpolation | 0.6707 | 0.5516 | -0.4063 | -17.3551 | -79.2497 | -0.0491 | -11.4000 | -35.1676 |
| knn | -2.4639 | -6.0227 | -14.6091 | -15.6708 | -17.6510 | -16.3091 | -13.4922 | -8.4386 |
| decision_tree | -1.4371 | -0.8017 | -2.1745 | -2.4808 | -0.9642 | -1.8929 | -2.3843 | -2.9762 |
| random_forest | -3.0328 | -1.5848 | -2.3205 | -1.7082 | -1.4088 | -2.1849 | -3.9910 | -6.1715 |

---

## Najbolja metoda po scenariju i missing rateu (po MAE)

| scenario | block_position | missing_rate | najbolja metoda | MAE | RMSE | R² |
|----------|----------------|--------------|-----------------|-----|------|-----|
| random | none | 10% | cubic_interpolation | 0.0406 | 0.0503 | 0.9993 |
| random | none | 20% | cubic_interpolation | 0.0488 | 0.0672 | 0.9987 |
| random | none | 30% | spline_interpolation | 0.0448 | 0.0606 | 0.9991 |
| random | none | 40% | linear_interpolation | 0.0620 | 0.0920 | 0.9980 |
| random | none | 50% | linear_interpolation | 0.0676 | 0.0984 | 0.9976 |
| random | none | 60% | linear_interpolation | 0.0732 | 0.1053 | 0.9974 |
| random | none | 70% | linear_interpolation | 0.0815 | 0.1119 | 0.9971 |
| random | none | 80% | linear_interpolation | 0.0919 | 0.1259 | 0.9964 |
| block | none | 10% | linear_interpolation | 0.1214 | 0.1428 | 0.4867 |
| block | none | 20% | cubic_interpolation | 0.1946 | 0.2737 | 0.9155 |
| block | none | 30% | linear_interpolation | 0.4406 | 0.5602 | 0.5833 |
| block | none | 40% | linear_interpolation | 0.6903 | 0.9168 | 0.6616 |
| block | none | 50% | forward_fill | 0.6913 | 0.8919 | -0.3307 |
| block | none | 60% | linear_interpolation | 0.6108 | 0.7029 | 0.6128 |
| block | none | 70% | linear_interpolation | 0.7720 | 0.8781 | 0.4953 |
| block | none | 80% | linear_interpolation | 0.6705 | 0.9274 | 0.7914 |
| block_start | start | 10% | linear_interpolation | 0.2212 | 0.2870 | 0.6913 |
| block_start | start | 20% | forward_fill | 0.8097 | 0.9592 | -0.7258 |
| block_start | start | 30% | spline_interpolation | 0.9713 | 1.1943 | -0.0214 |
| block_start | start | 40% | linear_interpolation | 0.8763 | 1.1887 | 0.4144 |
| block_start | start | 50% | linear_interpolation | 0.7737 | 1.0082 | 0.6682 |
| block_start | start | 60% | linear_interpolation | 0.9158 | 1.0451 | 0.6670 |
| block_start | start | 70% | linear_interpolation | 0.6991 | 0.8889 | 0.7639 |
| block_start | start | 80% | linear_interpolation | 0.6939 | 0.9373 | 0.7794 |
| block_middle | middle | 10% | decision_tree | 0.1081 | 0.1322 | 0.1342 |
| block_middle | middle | 20% | forward_fill | 0.3384 | 0.4029 | -1.8616 |
| block_middle | middle | 30% | linear_interpolation | 0.2554 | 0.3052 | 0.1034 |
| block_middle | middle | 40% | linear_interpolation | 0.2665 | 0.3092 | 0.4961 |
| block_middle | middle | 50% | linear_interpolation | 0.5473 | 0.5987 | 0.2720 |
| block_middle | middle | 60% | linear_interpolation | 0.5395 | 0.6247 | 0.7016 |
| block_middle | middle | 70% | linear_interpolation | 0.9671 | 1.1303 | 0.4191 |
| block_middle | middle | 80% | linear_interpolation | 1.4370 | 1.5759 | 0.2636 |
| block_end | end | 10% | cubic_interpolation | 0.1812 | 0.2320 | 0.7683 |
| block_end | end | 20% | cubic_interpolation | 0.3076 | 0.3514 | 0.7268 |
| block_end | end | 30% | spline_interpolation | 0.6671 | 0.7697 | -0.4063 |
| block_end | end | 40% | random_forest | 1.0260 | 1.2487 | -1.7082 |
| block_end | end | 50% | decision_tree | 0.8176 | 1.0873 | -0.9642 |
| block_end | end | 60% | spline_interpolation | 0.7227 | 0.8186 | -0.0491 |
| block_end | end | 70% | linear_interpolation | 1.1760 | 1.3635 | -1.2691 |
| block_end | end | 80% | linear_interpolation | 1.5937 | 1.7404 | -1.0366 |