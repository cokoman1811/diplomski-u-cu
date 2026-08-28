# Sve tablice rezultata — missing rate 10–80 %

*Izvor: `results/experiment_results.csv` (480 redaka)*
*Generirano: `python scripts/generate_results_tables.py`*

---

## KOMPLETNA TABLICA (svi scenariji, svi rateovi, sve metode)

| scenario | block_position | missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|----------|----------------|--------------|--------|-----|------|-----|---------|-----------|
| block | none | 10% | adaptive_imputation | 2.1669 | 2.5400 | -0.6694 | 101 | 101 |
| block | none | 10% | cubic_interpolation | 2.2159 | 2.7342 | -2.5604 | 101 | 101 |
| block | none | 10% | decision_tree | 2.1369 | 2.5103 | -0.6646 | 101 | 101 |
| block | none | 10% | forward_fill | 3.4311 | 4.0140 | -2.0658 | 101 | 101 |
| block | none | 10% | knn | 2.1669 | 2.5400 | -0.6694 | 101 | 101 |
| block | none | 10% | knn_upgraded | 2.1504 | 2.5247 | -0.6509 | 101 | 101 |
| block | none | 10% | linear_interpolation | 2.1669 | 2.5400 | -0.6694 | 101 | 101 |
| block | none | 10% | moving_average | 3.1873 | 3.8070 | -1.8208 | 101 | 101 |
| block | none | 10% | neural_net | 2.1311 | 2.5063 | -0.6337 | 101 | 101 |
| block | none | 10% | random_forest | 2.1507 | 2.5245 | -0.6515 | 101 | 101 |
| block | none | 10% | spline_interpolation | 2.2159 | 2.7342 | -2.5604 | 101 | 101 |
| block | none | 10% | time_interpolation | 2.1669 | 2.5400 | -0.6694 | 101 | 101 |
| block | none | 20% | adaptive_imputation | 2.6286 | 3.2177 | -0.4873 | 202 | 202 |
| block | none | 20% | cubic_interpolation | 6.7633 | 8.0402 | -11.9963 | 202 | 202 |
| block | none | 20% | decision_tree | 2.5355 | 3.1254 | -0.3672 | 202 | 202 |
| block | none | 20% | forward_fill | 3.2575 | 3.9366 | -1.2617 | 202 | 202 |
| block | none | 20% | knn | 2.5336 | 3.1165 | -0.3624 | 202 | 202 |
| block | none | 20% | knn_upgraded | 2.5281 | 3.1140 | -0.3600 | 202 | 202 |
| block | none | 20% | linear_interpolation | 2.5336 | 3.1165 | -0.3624 | 202 | 202 |
| block | none | 20% | moving_average | 3.1532 | 3.8480 | -1.1418 | 202 | 202 |
| block | none | 20% | neural_net | 2.5198 | 3.1131 | -0.3658 | 202 | 202 |
| block | none | 20% | random_forest | 2.5299 | 3.1174 | -0.3611 | 202 | 202 |
| block | none | 20% | spline_interpolation | 6.7633 | 8.0402 | -11.9963 | 202 | 202 |
| block | none | 20% | time_interpolation | 2.5336 | 3.1165 | -0.3624 | 202 | 202 |
| block | none | 30% | adaptive_imputation | 5.6602 | 6.6625 | -6.2216 | 302 | 302 |
| block | none | 30% | cubic_interpolation | 9.1979 | 10.7027 | -14.6333 | 302 | 302 |
| block | none | 30% | decision_tree | 3.7704 | 4.4610 | -1.1290 | 302 | 302 |
| block | none | 30% | forward_fill | 4.7738 | 5.5457 | -1.8891 | 302 | 302 |
| block | none | 30% | knn | 3.7564 | 4.4475 | -1.1330 | 302 | 302 |
| block | none | 30% | knn_upgraded | 3.7551 | 4.4470 | -1.1302 | 302 | 302 |
| block | none | 30% | linear_interpolation | 3.7564 | 4.4475 | -1.1330 | 302 | 302 |
| block | none | 30% | moving_average | 4.6951 | 5.4889 | -1.8393 | 302 | 302 |
| block | none | 30% | neural_net | 3.7507 | 4.4459 | -1.1276 | 302 | 302 |
| block | none | 30% | random_forest | 3.7656 | 4.4580 | -1.1396 | 302 | 302 |
| block | none | 30% | spline_interpolation | 9.1979 | 10.7027 | -14.6333 | 302 | 302 |
| block | none | 30% | time_interpolation | 3.7564 | 4.4475 | -1.1330 | 302 | 302 |
| block | none | 40% | adaptive_imputation | 2.8299 | 3.5155 | -0.6770 | 403 | 403 |
| block | none | 40% | cubic_interpolation | 11.4708 | 13.5059 | -30.8877 | 403 | 403 |
| block | none | 40% | decision_tree | 2.8276 | 3.5164 | -0.6885 | 403 | 403 |
| block | none | 40% | forward_fill | 4.0476 | 4.8470 | -1.4412 | 403 | 403 |
| block | none | 40% | knn | 2.8349 | 3.5204 | -0.6839 | 403 | 403 |
| block | none | 40% | knn_upgraded | 2.8223 | 3.5072 | -0.6663 | 403 | 403 |
| block | none | 40% | linear_interpolation | 2.8349 | 3.5204 | -0.6839 | 403 | 403 |
| block | none | 40% | moving_average | 3.9736 | 4.7874 | -1.3872 | 403 | 403 |
| block | none | 40% | neural_net | 2.8297 | 3.5198 | -0.6877 | 403 | 403 |
| block | none | 40% | random_forest | 2.8163 | 3.5018 | -0.6697 | 403 | 403 |
| block | none | 40% | spline_interpolation | 11.4708 | 13.5059 | -30.8877 | 403 | 403 |
| block | none | 40% | time_interpolation | 2.8349 | 3.5204 | -0.6839 | 403 | 403 |
| block | none | 50% | adaptive_imputation | 4.8938 | 5.9512 | -4.4041 | 504 | 504 |
| block | none | 50% | cubic_interpolation | 12.4437 | 14.4897 | -28.1072 | 504 | 504 |
| block | none | 50% | decision_tree | 3.0915 | 3.8730 | -0.2155 | 504 | 504 |
| block | none | 50% | forward_fill | 4.0175 | 4.8459 | -0.8167 | 504 | 504 |
| block | none | 50% | knn | 3.0897 | 3.8749 | -0.2134 | 504 | 504 |
| block | none | 50% | knn_upgraded | 3.0903 | 3.8729 | -0.2114 | 504 | 504 |
| block | none | 50% | linear_interpolation | 3.0897 | 3.8749 | -0.2134 | 504 | 504 |
| block | none | 50% | moving_average | 3.9649 | 4.8081 | -0.7849 | 504 | 504 |
| block | none | 50% | neural_net | 3.0885 | 3.8732 | -0.2157 | 504 | 504 |
| block | none | 50% | random_forest | 3.0882 | 3.8701 | -0.2135 | 504 | 504 |
| block | none | 50% | spline_interpolation | 12.4437 | 14.4897 | -28.1072 | 504 | 504 |
| block | none | 50% | time_interpolation | 3.0897 | 3.8749 | -0.2134 | 504 | 504 |
| block | none | 60% | adaptive_imputation | 4.3340 | 5.1401 | -1.5458 | 605 | 605 |
| block | none | 60% | cubic_interpolation | 21.3524 | 24.6079 | -68.9215 | 605 | 605 |
| block | none | 60% | decision_tree | 3.7402 | 4.5503 | -0.7871 | 605 | 605 |
| block | none | 60% | forward_fill | 5.7158 | 6.5606 | -2.9819 | 605 | 605 |
| block | none | 60% | knn | 3.7336 | 4.5401 | -0.7819 | 605 | 605 |
| block | none | 60% | knn_upgraded | 3.7346 | 4.5431 | -0.7841 | 605 | 605 |
| block | none | 60% | linear_interpolation | 3.7336 | 4.5401 | -0.7819 | 605 | 605 |
| block | none | 60% | moving_average | 5.6654 | 6.5276 | -2.9424 | 605 | 605 |
| block | none | 60% | neural_net | 3.7285 | 4.5471 | -0.7923 | 605 | 605 |
| block | none | 60% | random_forest | 3.7481 | 4.5574 | -0.8020 | 605 | 605 |
| block | none | 60% | spline_interpolation | 21.3970 | 24.6600 | -69.5461 | 605 | 605 |
| block | none | 60% | time_interpolation | 3.7336 | 4.5401 | -0.7819 | 605 | 605 |
| block | none | 70% | adaptive_imputation | 4.3185 | 5.1378 | -1.5666 | 706 | 706 |
| block | none | 70% | cubic_interpolation | 16.9042 | 19.7851 | -55.0985 | 706 | 706 |
| block | none | 70% | decision_tree | 3.7657 | 4.5868 | -1.1037 | 706 | 706 |
| block | none | 70% | forward_fill | 4.2738 | 5.0736 | -1.5385 | 706 | 706 |
| block | none | 70% | knn | 3.7852 | 4.6027 | -1.1138 | 706 | 706 |
| block | none | 70% | knn_upgraded | 3.7799 | 4.5993 | -1.1126 | 706 | 706 |
| block | none | 70% | linear_interpolation | 3.7852 | 4.6027 | -1.1138 | 706 | 706 |
| block | none | 70% | moving_average | 4.2395 | 5.0447 | -1.5173 | 706 | 706 |
| block | none | 70% | neural_net | 3.7822 | 4.6177 | -1.1366 | 706 | 706 |
| block | none | 70% | random_forest | 3.7718 | 4.5904 | -1.1070 | 706 | 706 |
| block | none | 70% | spline_interpolation | 16.9042 | 19.7851 | -55.0985 | 706 | 706 |
| block | none | 70% | time_interpolation | 3.7852 | 4.6027 | -1.1138 | 706 | 706 |
| block | none | 80% | adaptive_imputation | 11.6266 | 13.5576 | -110.0308 | 806 | 806 |
| block | none | 80% | cubic_interpolation | 29.3598 | 33.6612 | -181.9469 | 806 | 806 |
| block | none | 80% | decision_tree | 3.5502 | 4.4147 | -0.5277 | 806 | 806 |
| block | none | 80% | forward_fill | 5.0784 | 5.9290 | -2.2239 | 806 | 806 |
| block | none | 80% | knn | 3.5617 | 4.4259 | -0.5369 | 806 | 806 |
| block | none | 80% | knn_upgraded | 3.5544 | 4.4192 | -0.5309 | 806 | 806 |
| block | none | 80% | linear_interpolation | 3.5617 | 4.4259 | -0.5369 | 806 | 806 |
| block | none | 80% | moving_average | 5.0404 | 5.9042 | -2.1914 | 806 | 806 |
| block | none | 80% | neural_net | 3.5561 | 4.4239 | -0.5281 | 806 | 806 |
| block | none | 80% | random_forest | 3.5510 | 4.4152 | -0.5290 | 806 | 806 |
| block | none | 80% | spline_interpolation | 29.4213 | 33.7329 | -183.2164 | 806 | 806 |
| block | none | 80% | time_interpolation | 3.5617 | 4.4259 | -0.5369 | 806 | 806 |
| block_end | end | 10% | adaptive_imputation | 2.2360 | 2.7231 | -0.5868 | 101 | 101 |
| block_end | end | 10% | cubic_interpolation | 2.8200 | 3.3263 | -1.5008 | 101 | 101 |
| block_end | end | 10% | decision_tree | 2.3154 | 2.7306 | -0.5348 | 101 | 101 |
| block_end | end | 10% | forward_fill | 3.5266 | 4.0676 | -2.6489 | 101 | 101 |
| block_end | end | 10% | knn | 2.2360 | 2.7231 | -0.5868 | 101 | 101 |
| block_end | end | 10% | knn_upgraded | 2.2315 | 2.7191 | -0.5752 | 101 | 101 |
| block_end | end | 10% | linear_interpolation | 2.2360 | 2.7231 | -0.5868 | 101 | 101 |
| block_end | end | 10% | moving_average | 3.3288 | 3.9310 | -2.4035 | 101 | 101 |
| block_end | end | 10% | neural_net | 2.2468 | 2.7399 | -0.5965 | 101 | 101 |
| block_end | end | 10% | random_forest | 2.2696 | 2.7117 | -0.4908 | 101 | 101 |
| block_end | end | 10% | spline_interpolation | 3.3231 | 3.8600 | -2.9737 | 101 | 101 |
| block_end | end | 10% | time_interpolation | 2.2360 | 2.7231 | -0.5868 | 101 | 101 |
| block_end | end | 20% | adaptive_imputation | 4.3268 | 5.3714 | -6.1576 | 202 | 202 |
| block_end | end | 20% | cubic_interpolation | 4.3268 | 5.3714 | -6.1576 | 202 | 202 |
| block_end | end | 20% | decision_tree | 2.7030 | 3.2443 | -0.5509 | 202 | 202 |
| block_end | end | 20% | forward_fill | 3.0373 | 3.6133 | -0.8494 | 202 | 202 |
| block_end | end | 20% | knn | 2.5602 | 3.0986 | -0.3547 | 202 | 202 |
| block_end | end | 20% | knn_upgraded | 2.5292 | 3.0747 | -0.3597 | 202 | 202 |
| block_end | end | 20% | linear_interpolation | 2.5602 | 3.0986 | -0.3547 | 202 | 202 |
| block_end | end | 20% | moving_average | 2.9462 | 3.5482 | -0.7772 | 202 | 202 |
| block_end | end | 20% | neural_net | 2.6860 | 3.2208 | -0.4458 | 202 | 202 |
| block_end | end | 20% | random_forest | 2.6628 | 3.1954 | -0.5103 | 202 | 202 |
| block_end | end | 20% | spline_interpolation | 5.6416 | 6.7526 | -11.7030 | 202 | 202 |
| block_end | end | 20% | time_interpolation | 2.5602 | 3.0986 | -0.3547 | 202 | 202 |
| block_end | end | 30% | adaptive_imputation | 6.5507 | 7.4569 | -15.4252 | 302 | 302 |
| block_end | end | 30% | cubic_interpolation | 4.9419 | 5.8202 | -7.9157 | 302 | 302 |
| block_end | end | 30% | decision_tree | 2.7768 | 3.3904 | -0.7531 | 302 | 302 |
| block_end | end | 30% | forward_fill | 2.9232 | 3.5516 | -1.0643 | 302 | 302 |
| block_end | end | 30% | knn | 2.6552 | 3.2323 | -0.6430 | 302 | 302 |
| block_end | end | 30% | knn_upgraded | 2.6745 | 3.2643 | -0.6540 | 302 | 302 |
| block_end | end | 30% | linear_interpolation | 2.6552 | 3.2323 | -0.6430 | 302 | 302 |
| block_end | end | 30% | moving_average | 2.8771 | 3.5208 | -1.0345 | 302 | 302 |
| block_end | end | 30% | neural_net | 2.7204 | 3.3156 | -0.6989 | 302 | 302 |
| block_end | end | 30% | random_forest | 2.7065 | 3.2981 | -0.6850 | 302 | 302 |
| block_end | end | 30% | spline_interpolation | 6.5507 | 7.4569 | -15.4252 | 302 | 302 |
| block_end | end | 30% | time_interpolation | 2.6552 | 3.2323 | -0.6430 | 302 | 302 |
| block_end | end | 40% | adaptive_imputation | 2.8122 | 3.4494 | -0.3589 | 403 | 403 |
| block_end | end | 40% | cubic_interpolation | 7.4638 | 8.9455 | -33.4697 | 403 | 403 |
| block_end | end | 40% | decision_tree | 2.9264 | 3.5781 | -0.5088 | 403 | 403 |
| block_end | end | 40% | forward_fill | 3.2711 | 3.9006 | -0.8295 | 403 | 403 |
| block_end | end | 40% | knn | 2.8122 | 3.4494 | -0.3589 | 403 | 403 |
| block_end | end | 40% | knn_upgraded | 2.8247 | 3.4815 | -0.3984 | 403 | 403 |
| block_end | end | 40% | linear_interpolation | 2.8122 | 3.4494 | -0.3589 | 403 | 403 |
| block_end | end | 40% | moving_average | 3.2289 | 3.8735 | -0.8019 | 403 | 403 |
| block_end | end | 40% | neural_net | 2.8351 | 3.4809 | -0.3946 | 403 | 403 |
| block_end | end | 40% | random_forest | 2.8842 | 3.5477 | -0.4615 | 403 | 403 |
| block_end | end | 40% | spline_interpolation | 10.2407 | 11.7425 | -64.7224 | 403 | 403 |
| block_end | end | 40% | time_interpolation | 2.8122 | 3.4494 | -0.3589 | 403 | 403 |
| block_end | end | 50% | adaptive_imputation | 3.0938 | 3.8936 | -0.6455 | 504 | 504 |
| block_end | end | 50% | cubic_interpolation | 7.8997 | 9.2728 | -13.8338 | 504 | 504 |
| block_end | end | 50% | decision_tree | 3.1401 | 3.8229 | -0.6210 | 504 | 504 |
| block_end | end | 50% | forward_fill | 4.7663 | 5.5476 | -2.6809 | 504 | 504 |
| block_end | end | 50% | knn | 3.0938 | 3.8936 | -0.6455 | 504 | 504 |
| block_end | end | 50% | knn_upgraded | 2.9683 | 3.7025 | -0.4941 | 504 | 504 |
| block_end | end | 50% | linear_interpolation | 3.0938 | 3.8936 | -0.6455 | 504 | 504 |
| block_end | end | 50% | moving_average | 4.7041 | 5.5076 | -2.6225 | 504 | 504 |
| block_end | end | 50% | neural_net | 3.1202 | 3.8948 | -0.6888 | 504 | 504 |
| block_end | end | 50% | random_forest | 3.0636 | 3.7564 | -0.5528 | 504 | 504 |
| block_end | end | 50% | spline_interpolation | 10.7038 | 12.1357 | -25.0044 | 504 | 504 |
| block_end | end | 50% | time_interpolation | 3.0938 | 3.8936 | -0.6455 | 504 | 504 |
| block_end | end | 60% | adaptive_imputation | 3.2528 | 4.0267 | -0.7316 | 605 | 605 |
| block_end | end | 60% | cubic_interpolation | 10.0488 | 11.9508 | -19.6469 | 605 | 605 |
| block_end | end | 60% | decision_tree | 3.2171 | 3.9368 | -0.5818 | 605 | 605 |
| block_end | end | 60% | forward_fill | 4.8022 | 5.6160 | -2.4665 | 605 | 605 |
| block_end | end | 60% | knn | 3.2528 | 4.0267 | -0.7316 | 605 | 605 |
| block_end | end | 60% | knn_upgraded | 3.1501 | 3.8980 | -0.5832 | 605 | 605 |
| block_end | end | 60% | linear_interpolation | 3.2528 | 4.0267 | -0.7316 | 605 | 605 |
| block_end | end | 60% | moving_average | 4.7516 | 5.5839 | -2.4314 | 605 | 605 |
| block_end | end | 60% | neural_net | 3.2511 | 4.0377 | -0.6972 | 605 | 605 |
| block_end | end | 60% | random_forest | 3.1812 | 3.9082 | -0.5876 | 605 | 605 |
| block_end | end | 60% | spline_interpolation | 14.6728 | 16.4953 | -40.1225 | 605 | 605 |
| block_end | end | 60% | time_interpolation | 3.2528 | 4.0267 | -0.7316 | 605 | 605 |
| block_end | end | 70% | adaptive_imputation | 3.1762 | 3.9139 | -0.2615 | 706 | 706 |
| block_end | end | 70% | cubic_interpolation | 23.8038 | 28.0182 | -124.5358 | 706 | 706 |
| block_end | end | 70% | decision_tree | 3.3991 | 4.1678 | -0.4089 | 706 | 706 |
| block_end | end | 70% | forward_fill | 3.5122 | 4.3200 | -0.6267 | 706 | 706 |
| block_end | end | 70% | knn | 3.1762 | 3.9139 | -0.2615 | 706 | 706 |
| block_end | end | 70% | knn_upgraded | 3.2731 | 4.0449 | -0.3339 | 706 | 706 |
| block_end | end | 70% | linear_interpolation | 3.1762 | 3.9139 | -0.2615 | 706 | 706 |
| block_end | end | 70% | moving_average | 3.4882 | 4.3041 | -0.6110 | 706 | 706 |
| block_end | end | 70% | neural_net | 3.2612 | 4.0244 | -0.3267 | 706 | 706 |
| block_end | end | 70% | random_forest | 3.3540 | 4.1190 | -0.3897 | 706 | 706 |
| block_end | end | 70% | spline_interpolation | 35.0891 | 39.0360 | -249.6283 | 706 | 706 |
| block_end | end | 70% | time_interpolation | 3.1762 | 3.9139 | -0.2615 | 706 | 706 |
| block_end | end | 80% | adaptive_imputation | 14.0329 | 16.5526 | -100.9549 | 806 | 806 |
| block_end | end | 80% | cubic_interpolation | 14.0329 | 16.5526 | -100.9549 | 806 | 806 |
| block_end | end | 80% | decision_tree | 3.4093 | 4.1680 | -0.3356 | 806 | 806 |
| block_end | end | 80% | forward_fill | 4.3384 | 5.0966 | -1.3228 | 806 | 806 |
| block_end | end | 80% | knn | 3.2232 | 3.9508 | -0.2344 | 806 | 806 |
| block_end | end | 80% | knn_upgraded | 3.2579 | 4.0116 | -0.2404 | 806 | 806 |
| block_end | end | 80% | linear_interpolation | 3.2232 | 3.9508 | -0.2344 | 806 | 806 |
| block_end | end | 80% | moving_average | 4.3037 | 5.0727 | -1.2979 | 806 | 806 |
| block_end | end | 80% | neural_net | 3.3167 | 4.0709 | -0.3276 | 806 | 806 |
| block_end | end | 80% | random_forest | 3.2577 | 3.9994 | -0.2382 | 806 | 806 |
| block_end | end | 80% | spline_interpolation | 19.9462 | 22.3597 | -196.8562 | 806 | 806 |
| block_end | end | 80% | time_interpolation | 3.2232 | 3.9508 | -0.2344 | 806 | 806 |
| block_middle | middle | 10% | adaptive_imputation | 2.4936 | 2.9240 | -0.8101 | 101 | 101 |
| block_middle | middle | 10% | cubic_interpolation | 2.8902 | 3.4244 | -4.8049 | 101 | 101 |
| block_middle | middle | 10% | decision_tree | 2.5238 | 2.9579 | -0.8497 | 101 | 101 |
| block_middle | middle | 10% | forward_fill | 3.3713 | 3.8757 | -2.1698 | 101 | 101 |
| block_middle | middle | 10% | knn | 2.4936 | 2.9240 | -0.8101 | 101 | 101 |
| block_middle | middle | 10% | knn_upgraded | 2.4864 | 2.9165 | -0.7950 | 101 | 101 |
| block_middle | middle | 10% | linear_interpolation | 2.4936 | 2.9240 | -0.8101 | 101 | 101 |
| block_middle | middle | 10% | moving_average | 3.1420 | 3.6840 | -1.8895 | 101 | 101 |
| block_middle | middle | 10% | neural_net | 2.4911 | 2.9222 | -0.8105 | 101 | 101 |
| block_middle | middle | 10% | random_forest | 2.4939 | 2.9248 | -0.8009 | 101 | 101 |
| block_middle | middle | 10% | spline_interpolation | 2.8902 | 3.4244 | -4.8049 | 101 | 101 |
| block_middle | middle | 10% | time_interpolation | 2.4936 | 2.9240 | -0.8101 | 101 | 101 |
| block_middle | middle | 20% | adaptive_imputation | 2.4287 | 3.0196 | -0.3214 | 202 | 202 |
| block_middle | middle | 20% | cubic_interpolation | 7.0993 | 8.4025 | -17.1314 | 202 | 202 |
| block_middle | middle | 20% | decision_tree | 2.4272 | 3.0207 | -0.3236 | 202 | 202 |
| block_middle | middle | 20% | forward_fill | 3.6248 | 4.3054 | -2.1059 | 202 | 202 |
| block_middle | middle | 20% | knn | 2.4287 | 3.0196 | -0.3214 | 202 | 202 |
| block_middle | middle | 20% | knn_upgraded | 2.4231 | 3.0166 | -0.3225 | 202 | 202 |
| block_middle | middle | 20% | linear_interpolation | 2.4287 | 3.0196 | -0.3214 | 202 | 202 |
| block_middle | middle | 20% | moving_average | 3.5030 | 4.2108 | -1.9514 | 202 | 202 |
| block_middle | middle | 20% | neural_net | 2.4173 | 3.0136 | -0.3261 | 202 | 202 |
| block_middle | middle | 20% | random_forest | 2.4256 | 3.0213 | -0.3282 | 202 | 202 |
| block_middle | middle | 20% | spline_interpolation | 7.0993 | 8.4025 | -17.1314 | 202 | 202 |
| block_middle | middle | 20% | time_interpolation | 2.4287 | 3.0196 | -0.3214 | 202 | 202 |
| block_middle | middle | 30% | adaptive_imputation | 7.5157 | 8.8354 | -9.8463 | 302 | 302 |
| block_middle | middle | 30% | cubic_interpolation | 7.5157 | 8.8354 | -9.8463 | 302 | 302 |
| block_middle | middle | 30% | decision_tree | 2.9535 | 3.6183 | -0.9175 | 302 | 302 |
| block_middle | middle | 30% | forward_fill | 4.4178 | 5.0875 | -3.1045 | 302 | 302 |
| block_middle | middle | 30% | knn | 2.9642 | 3.6305 | -0.9238 | 302 | 302 |
| block_middle | middle | 30% | knn_upgraded | 2.9657 | 3.6355 | -0.9249 | 302 | 302 |
| block_middle | middle | 30% | linear_interpolation | 2.9642 | 3.6305 | -0.9238 | 302 | 302 |
| block_middle | middle | 30% | moving_average | 4.3349 | 5.0339 | -3.0334 | 302 | 302 |
| block_middle | middle | 30% | neural_net | 2.9640 | 3.6404 | -0.9123 | 302 | 302 |
| block_middle | middle | 30% | random_forest | 2.9625 | 3.6329 | -0.9174 | 302 | 302 |
| block_middle | middle | 30% | spline_interpolation | 7.5157 | 8.8354 | -9.8463 | 302 | 302 |
| block_middle | middle | 30% | time_interpolation | 2.9642 | 3.6305 | -0.9238 | 302 | 302 |
| block_middle | middle | 40% | adaptive_imputation | 3.3784 | 4.0501 | -1.0471 | 403 | 403 |
| block_middle | middle | 40% | cubic_interpolation | 9.2167 | 11.0021 | -14.7989 | 403 | 403 |
| block_middle | middle | 40% | decision_tree | 3.3739 | 4.0479 | -1.0437 | 403 | 403 |
| block_middle | middle | 40% | forward_fill | 3.4973 | 4.1845 | -1.0817 | 403 | 403 |
| block_middle | middle | 40% | knn | 3.3800 | 4.0495 | -1.0486 | 403 | 403 |
| block_middle | middle | 40% | knn_upgraded | 3.3730 | 4.0436 | -1.0475 | 403 | 403 |
| block_middle | middle | 40% | linear_interpolation | 3.3800 | 4.0495 | -1.0486 | 403 | 403 |
| block_middle | middle | 40% | moving_average | 3.4675 | 4.1654 | -1.0534 | 403 | 403 |
| block_middle | middle | 40% | neural_net | 3.3719 | 4.0516 | -1.0600 | 403 | 403 |
| block_middle | middle | 40% | random_forest | 3.3784 | 4.0501 | -1.0471 | 403 | 403 |
| block_middle | middle | 40% | spline_interpolation | 9.2167 | 11.0021 | -14.7989 | 403 | 403 |
| block_middle | middle | 40% | time_interpolation | 3.3800 | 4.0495 | -1.0486 | 403 | 403 |
| block_middle | middle | 50% | adaptive_imputation | 13.4306 | 15.7456 | -32.2616 | 504 | 504 |
| block_middle | middle | 50% | cubic_interpolation | 13.4306 | 15.7456 | -32.2616 | 504 | 504 |
| block_middle | middle | 50% | decision_tree | 3.2622 | 3.9272 | -0.4119 | 504 | 504 |
| block_middle | middle | 50% | forward_fill | 4.1161 | 4.8768 | -1.4949 | 504 | 504 |
| block_middle | middle | 50% | knn | 3.2633 | 3.9330 | -0.4140 | 504 | 504 |
| block_middle | middle | 50% | knn_upgraded | 3.2569 | 3.9244 | -0.4088 | 504 | 504 |
| block_middle | middle | 50% | linear_interpolation | 3.2633 | 3.9330 | -0.4140 | 504 | 504 |
| block_middle | middle | 50% | moving_average | 4.0500 | 4.8115 | -1.4269 | 504 | 504 |
| block_middle | middle | 50% | neural_net | 3.2800 | 3.9480 | -0.4332 | 504 | 504 |
| block_middle | middle | 50% | random_forest | 3.2658 | 3.9344 | -0.4174 | 504 | 504 |
| block_middle | middle | 50% | spline_interpolation | 13.4306 | 15.7456 | -32.2616 | 504 | 504 |
| block_middle | middle | 50% | time_interpolation | 3.2633 | 3.9330 | -0.4140 | 504 | 504 |
| block_middle | middle | 60% | adaptive_imputation | 4.0337 | 4.7417 | -1.3271 | 605 | 605 |
| block_middle | middle | 60% | cubic_interpolation | 11.0021 | 13.0503 | -68.1359 | 605 | 605 |
| block_middle | middle | 60% | decision_tree | 3.2947 | 4.0635 | -0.4516 | 605 | 605 |
| block_middle | middle | 60% | forward_fill | 4.0337 | 4.7417 | -1.3271 | 605 | 605 |
| block_middle | middle | 60% | knn | 3.2926 | 4.0603 | -0.4461 | 605 | 605 |
| block_middle | middle | 60% | knn_upgraded | 3.2985 | 4.0675 | -0.4570 | 605 | 605 |
| block_middle | middle | 60% | linear_interpolation | 3.2926 | 4.0603 | -0.4461 | 605 | 605 |
| block_middle | middle | 60% | moving_average | 3.9999 | 4.7228 | -1.3084 | 605 | 605 |
| block_middle | middle | 60% | neural_net | 3.3139 | 4.0932 | -0.4800 | 605 | 605 |
| block_middle | middle | 60% | random_forest | 3.3012 | 4.0707 | -0.4622 | 605 | 605 |
| block_middle | middle | 60% | spline_interpolation | 11.0021 | 13.0503 | -68.1359 | 605 | 605 |
| block_middle | middle | 60% | time_interpolation | 3.2926 | 4.0603 | -0.4461 | 605 | 605 |
| block_middle | middle | 70% | adaptive_imputation | 4.3486 | 5.1866 | -1.6280 | 706 | 706 |
| block_middle | middle | 70% | cubic_interpolation | 19.5858 | 22.8486 | -99.0380 | 706 | 706 |
| block_middle | middle | 70% | decision_tree | 3.9613 | 4.8249 | -1.0372 | 706 | 706 |
| block_middle | middle | 70% | forward_fill | 4.3486 | 5.1866 | -1.6280 | 706 | 706 |
| block_middle | middle | 70% | knn | 3.9484 | 4.8092 | -1.0233 | 706 | 706 |
| block_middle | middle | 70% | knn_upgraded | 3.9330 | 4.7945 | -1.0048 | 706 | 706 |
| block_middle | middle | 70% | linear_interpolation | 3.9484 | 4.8092 | -1.0233 | 706 | 706 |
| block_middle | middle | 70% | moving_average | 4.3156 | 5.1611 | -1.6078 | 706 | 706 |
| block_middle | middle | 70% | neural_net | 3.9508 | 4.8138 | -1.0151 | 706 | 706 |
| block_middle | middle | 70% | random_forest | 3.9432 | 4.8049 | -1.0188 | 706 | 706 |
| block_middle | middle | 70% | spline_interpolation | 19.5858 | 22.8486 | -99.0380 | 706 | 706 |
| block_middle | middle | 70% | time_interpolation | 3.9484 | 4.8092 | -1.0233 | 706 | 706 |
| block_middle | middle | 80% | adaptive_imputation | 5.5145 | 6.4044 | -1.9761 | 806 | 806 |
| block_middle | middle | 80% | cubic_interpolation | 24.9233 | 28.5951 | -78.2922 | 806 | 806 |
| block_middle | middle | 80% | decision_tree | 3.6115 | 4.5303 | -0.4314 | 806 | 806 |
| block_middle | middle | 80% | forward_fill | 5.5145 | 6.4044 | -1.9761 | 806 | 806 |
| block_middle | middle | 80% | knn | 3.6322 | 4.5532 | -0.4499 | 806 | 806 |
| block_middle | middle | 80% | knn_upgraded | 3.6241 | 4.5440 | -0.4431 | 806 | 806 |
| block_middle | middle | 80% | linear_interpolation | 3.6322 | 4.5532 | -0.4499 | 806 | 806 |
| block_middle | middle | 80% | moving_average | 5.4578 | 6.3559 | -1.9343 | 806 | 806 |
| block_middle | middle | 80% | neural_net | 3.6280 | 4.5500 | -0.4427 | 806 | 806 |
| block_middle | middle | 80% | random_forest | 3.6163 | 4.5367 | -0.4365 | 806 | 806 |
| block_middle | middle | 80% | spline_interpolation | 24.9233 | 28.5951 | -78.2922 | 806 | 806 |
| block_middle | middle | 80% | time_interpolation | 3.6322 | 4.5532 | -0.4499 | 806 | 806 |
| block_start | start | 10% | adaptive_imputation | 2.1935 | 2.5342 | -0.5554 | 101 | 101 |
| block_start | start | 10% | cubic_interpolation | 2.0883 | 2.4984 | -0.4797 | 101 | 101 |
| block_start | start | 10% | decision_tree | 2.4108 | 2.8080 | -0.6081 | 101 | 101 |
| block_start | start | 10% | forward_fill | 3.2454 | 3.8822 | -1.5198 | 101 | 101 |
| block_start | start | 10% | knn | 2.1935 | 2.5342 | -0.5554 | 101 | 101 |
| block_start | start | 10% | knn_upgraded | 2.1801 | 2.5213 | -0.5421 | 101 | 101 |
| block_start | start | 10% | linear_interpolation | 2.1935 | 2.5342 | -0.5554 | 101 | 101 |
| block_start | start | 10% | moving_average | 3.0268 | 3.7093 | -1.3377 | 101 | 101 |
| block_start | start | 10% | neural_net | 2.2066 | 2.5792 | -0.5654 | 101 | 101 |
| block_start | start | 10% | random_forest | 2.2469 | 2.6107 | -0.5232 | 101 | 101 |
| block_start | start | 10% | spline_interpolation | 2.3357 | 2.7472 | -0.9159 | 101 | 101 |
| block_start | start | 10% | time_interpolation | 2.1935 | 2.5342 | -0.5554 | 101 | 101 |
| block_start | start | 20% | adaptive_imputation | 2.8362 | 3.5406 | -0.5235 | 202 | 202 |
| block_start | start | 20% | cubic_interpolation | 4.6230 | 5.8036 | -4.8747 | 202 | 202 |
| block_start | start | 20% | decision_tree | 3.0008 | 3.6520 | -0.5518 | 202 | 202 |
| block_start | start | 20% | forward_fill | 3.4633 | 4.1554 | -1.1046 | 202 | 202 |
| block_start | start | 20% | knn | 2.8362 | 3.5406 | -0.5235 | 202 | 202 |
| block_start | start | 20% | knn_upgraded | 2.7903 | 3.4767 | -0.4325 | 202 | 202 |
| block_start | start | 20% | linear_interpolation | 2.8362 | 3.5406 | -0.5235 | 202 | 202 |
| block_start | start | 20% | moving_average | 3.3169 | 4.0259 | -0.9689 | 202 | 202 |
| block_start | start | 20% | neural_net | 2.9052 | 3.5747 | -0.5858 | 202 | 202 |
| block_start | start | 20% | random_forest | 2.8921 | 3.5607 | -0.4654 | 202 | 202 |
| block_start | start | 20% | spline_interpolation | 5.6963 | 6.9300 | -8.0180 | 202 | 202 |
| block_start | start | 20% | time_interpolation | 2.8362 | 3.5406 | -0.5235 | 202 | 202 |
| block_start | start | 30% | adaptive_imputation | 3.1570 | 3.9690 | -0.4601 | 302 | 302 |
| block_start | start | 30% | cubic_interpolation | 5.2982 | 6.4774 | -5.8230 | 302 | 302 |
| block_start | start | 30% | decision_tree | 3.3207 | 4.0397 | -0.5476 | 302 | 302 |
| block_start | start | 30% | forward_fill | 3.8785 | 4.6261 | -0.9921 | 302 | 302 |
| block_start | start | 30% | knn | 3.1027 | 3.8831 | -0.4297 | 302 | 302 |
| block_start | start | 30% | knn_upgraded | 3.1379 | 3.8925 | -0.4460 | 302 | 302 |
| block_start | start | 30% | linear_interpolation | 3.1027 | 3.8831 | -0.4297 | 302 | 302 |
| block_start | start | 30% | moving_average | 3.8130 | 4.5793 | -0.9568 | 302 | 302 |
| block_start | start | 30% | neural_net | 3.1169 | 3.8915 | -0.4507 | 302 | 302 |
| block_start | start | 30% | random_forest | 3.2191 | 3.9583 | -0.5043 | 302 | 302 |
| block_start | start | 30% | spline_interpolation | 6.9550 | 8.1771 | -11.6508 | 302 | 302 |
| block_start | start | 30% | time_interpolation | 3.1027 | 3.8831 | -0.4297 | 302 | 302 |
| block_start | start | 40% | adaptive_imputation | 3.4974 | 4.1910 | -0.5730 | 403 | 403 |
| block_start | start | 40% | cubic_interpolation | 7.7071 | 9.2377 | -13.9591 | 403 | 403 |
| block_start | start | 40% | decision_tree | 3.4974 | 4.1910 | -0.5730 | 403 | 403 |
| block_start | start | 40% | forward_fill | 4.2018 | 4.9705 | -1.1020 | 403 | 403 |
| block_start | start | 40% | knn | 3.1895 | 3.8872 | -0.5076 | 403 | 403 |
| block_start | start | 40% | knn_upgraded | 3.2904 | 3.9908 | -0.5004 | 403 | 403 |
| block_start | start | 40% | linear_interpolation | 3.1895 | 3.8872 | -0.5076 | 403 | 403 |
| block_start | start | 40% | moving_average | 4.1368 | 4.9230 | -1.0637 | 403 | 403 |
| block_start | start | 40% | neural_net | 3.2257 | 3.9483 | -0.5070 | 403 | 403 |
| block_start | start | 40% | random_forest | 3.3091 | 4.0009 | -0.5001 | 403 | 403 |
| block_start | start | 40% | spline_interpolation | 10.7131 | 12.2507 | -28.4796 | 403 | 403 |
| block_start | start | 40% | time_interpolation | 3.1895 | 3.8872 | -0.5076 | 403 | 403 |
| block_start | start | 50% | adaptive_imputation | 3.0703 | 3.8144 | -0.2076 | 504 | 504 |
| block_start | start | 50% | cubic_interpolation | 7.0279 | 8.4252 | -12.7017 | 504 | 504 |
| block_start | start | 50% | decision_tree | 3.3272 | 4.0544 | -0.2935 | 504 | 504 |
| block_start | start | 50% | forward_fill | 4.4899 | 5.3117 | -1.1226 | 504 | 504 |
| block_start | start | 50% | knn | 3.0703 | 3.8144 | -0.2076 | 504 | 504 |
| block_start | start | 50% | knn_upgraded | 3.1737 | 3.9217 | -0.2186 | 504 | 504 |
| block_start | start | 50% | linear_interpolation | 3.0703 | 3.8144 | -0.2076 | 504 | 504 |
| block_start | start | 50% | moving_average | 4.4217 | 5.2560 | -1.0774 | 504 | 504 |
| block_start | start | 50% | neural_net | 3.0949 | 3.8435 | -0.2116 | 504 | 504 |
| block_start | start | 50% | random_forest | 3.1894 | 3.9164 | -0.2262 | 504 | 504 |
| block_start | start | 50% | spline_interpolation | 10.0062 | 11.4416 | -26.6400 | 504 | 504 |
| block_start | start | 50% | time_interpolation | 3.0703 | 3.8144 | -0.2076 | 504 | 504 |
| block_start | start | 60% | adaptive_imputation | 11.3422 | 13.2668 | -35.0885 | 605 | 605 |
| block_start | start | 60% | cubic_interpolation | 11.3422 | 13.2668 | -35.0885 | 605 | 605 |
| block_start | start | 60% | decision_tree | 3.8827 | 4.6781 | -0.7344 | 605 | 605 |
| block_start | start | 60% | forward_fill | 4.5089 | 5.3190 | -1.1824 | 605 | 605 |
| block_start | start | 60% | knn | 3.5792 | 4.3585 | -0.5799 | 605 | 605 |
| block_start | start | 60% | knn_upgraded | 3.6654 | 4.4541 | -0.6121 | 605 | 605 |
| block_start | start | 60% | linear_interpolation | 3.5792 | 4.3585 | -0.5799 | 605 | 605 |
| block_start | start | 60% | moving_average | 4.4693 | 5.2925 | -1.1625 | 605 | 605 |
| block_start | start | 60% | neural_net | 3.6427 | 4.4369 | -0.6054 | 605 | 605 |
| block_start | start | 60% | random_forest | 3.7472 | 4.5327 | -0.6507 | 605 | 605 |
| block_start | start | 60% | spline_interpolation | 15.8351 | 17.7297 | -69.2969 | 605 | 605 |
| block_start | start | 60% | time_interpolation | 3.5792 | 4.3585 | -0.5799 | 605 | 605 |
| block_start | start | 70% | adaptive_imputation | 9.5612 | 11.3483 | -14.9275 | 706 | 706 |
| block_start | start | 70% | cubic_interpolation | 9.5612 | 11.3483 | -14.9275 | 706 | 706 |
| block_start | start | 70% | decision_tree | 4.1595 | 4.9917 | -1.0482 | 706 | 706 |
| block_start | start | 70% | forward_fill | 4.5190 | 5.3266 | -1.2056 | 706 | 706 |
| block_start | start | 70% | knn | 3.9971 | 4.8378 | -1.0472 | 706 | 706 |
| block_start | start | 70% | knn_upgraded | 4.0605 | 4.9036 | -1.0196 | 706 | 706 |
| block_start | start | 70% | linear_interpolation | 3.9971 | 4.8378 | -1.0472 | 706 | 706 |
| block_start | start | 70% | moving_average | 4.4992 | 5.3155 | -1.1966 | 706 | 706 |
| block_start | start | 70% | neural_net | 4.0425 | 4.8959 | -1.0793 | 706 | 706 |
| block_start | start | 70% | random_forest | 4.0886 | 4.9301 | -1.0313 | 706 | 706 |
| block_start | start | 70% | spline_interpolation | 13.3992 | 15.2091 | -29.9568 | 706 | 706 |
| block_start | start | 70% | time_interpolation | 3.9971 | 4.8378 | -1.0472 | 706 | 706 |
| block_start | start | 80% | adaptive_imputation | 4.5077 | 5.3638 | -1.0658 | 806 | 806 |
| block_start | start | 80% | cubic_interpolation | 10.8286 | 12.7500 | -17.6325 | 806 | 806 |
| block_start | start | 80% | decision_tree | 3.9284 | 4.8320 | -0.6777 | 806 | 806 |
| block_start | start | 80% | forward_fill | 4.5077 | 5.3638 | -1.0658 | 806 | 806 |
| block_start | start | 80% | knn | 3.6322 | 4.5405 | -0.5088 | 806 | 806 |
| block_start | start | 80% | knn_upgraded | 3.7887 | 4.7033 | -0.5973 | 806 | 806 |
| block_start | start | 80% | linear_interpolation | 3.6322 | 4.5405 | -0.5088 | 806 | 806 |
| block_start | start | 80% | moving_average | 4.4819 | 5.3513 | -1.0557 | 806 | 806 |
| block_start | start | 80% | neural_net | 3.6481 | 4.5679 | -0.5436 | 806 | 806 |
| block_start | start | 80% | random_forest | 3.8540 | 4.7575 | -0.6333 | 806 | 806 |
| block_start | start | 80% | spline_interpolation | 15.0115 | 16.9479 | -34.3614 | 806 | 806 |
| block_start | start | 80% | time_interpolation | 3.6322 | 4.5405 | -0.5088 | 806 | 806 |
| random | none | 10% | adaptive_imputation | 0.0721 | 0.1114 | 0.9990 | 101 | 101 |
| random | none | 10% | cubic_interpolation | 0.0721 | 0.1115 | 0.9990 | 101 | 101 |
| random | none | 10% | decision_tree | 0.0857 | 0.1302 | 0.9986 | 101 | 101 |
| random | none | 10% | forward_fill | 0.1771 | 0.2579 | 0.9947 | 101 | 101 |
| random | none | 10% | knn | 0.0802 | 0.1216 | 0.9988 | 101 | 101 |
| random | none | 10% | knn_upgraded | 0.0871 | 0.1298 | 0.9986 | 101 | 101 |
| random | none | 10% | linear_interpolation | 0.0802 | 0.1216 | 0.9988 | 101 | 101 |
| random | none | 10% | moving_average | 0.1941 | 0.2822 | 0.9933 | 101 | 101 |
| random | none | 10% | neural_net | 0.0913 | 0.1388 | 0.9984 | 101 | 101 |
| random | none | 10% | random_forest | 0.0796 | 0.1209 | 0.9988 | 101 | 101 |
| random | none | 10% | spline_interpolation | 0.0721 | 0.1114 | 0.9990 | 101 | 101 |
| random | none | 10% | time_interpolation | 0.0802 | 0.1216 | 0.9988 | 101 | 101 |
| random | none | 20% | adaptive_imputation | 0.0821 | 0.1321 | 0.9985 | 202 | 202 |
| random | none | 20% | cubic_interpolation | 0.0821 | 0.1322 | 0.9985 | 202 | 202 |
| random | none | 20% | decision_tree | 0.0974 | 0.1517 | 0.9981 | 202 | 202 |
| random | none | 20% | forward_fill | 0.1903 | 0.2808 | 0.9936 | 202 | 202 |
| random | none | 20% | knn | 0.0887 | 0.1382 | 0.9984 | 202 | 202 |
| random | none | 20% | knn_upgraded | 0.0993 | 0.1508 | 0.9981 | 202 | 202 |
| random | none | 20% | linear_interpolation | 0.0887 | 0.1382 | 0.9984 | 202 | 202 |
| random | none | 20% | moving_average | 0.1990 | 0.2889 | 0.9932 | 202 | 202 |
| random | none | 20% | neural_net | 0.1019 | 0.1573 | 0.9980 | 202 | 202 |
| random | none | 20% | random_forest | 0.0892 | 0.1378 | 0.9984 | 202 | 202 |
| random | none | 20% | spline_interpolation | 0.0821 | 0.1321 | 0.9985 | 202 | 202 |
| random | none | 20% | time_interpolation | 0.0887 | 0.1382 | 0.9984 | 202 | 202 |
| random | none | 30% | adaptive_imputation | 0.0960 | 0.1521 | 0.9980 | 302 | 302 |
| random | none | 30% | cubic_interpolation | 0.0923 | 0.1511 | 0.9981 | 302 | 302 |
| random | none | 30% | decision_tree | 0.1044 | 0.1636 | 0.9976 | 302 | 302 |
| random | none | 30% | forward_fill | 0.2121 | 0.3210 | 0.9916 | 302 | 302 |
| random | none | 30% | knn | 0.0960 | 0.1521 | 0.9980 | 302 | 302 |
| random | none | 30% | knn_upgraded | 0.1109 | 0.1709 | 0.9975 | 302 | 302 |
| random | none | 30% | linear_interpolation | 0.0960 | 0.1521 | 0.9980 | 302 | 302 |
| random | none | 30% | moving_average | 0.2080 | 0.3054 | 0.9923 | 302 | 302 |
| random | none | 30% | neural_net | 0.1109 | 0.1705 | 0.9975 | 302 | 302 |
| random | none | 30% | random_forest | 0.0969 | 0.1531 | 0.9980 | 302 | 302 |
| random | none | 30% | spline_interpolation | 0.0923 | 0.1512 | 0.9981 | 302 | 302 |
| random | none | 30% | time_interpolation | 0.0960 | 0.1521 | 0.9980 | 302 | 302 |
| random | none | 40% | adaptive_imputation | 0.1055 | 0.1746 | 0.9974 | 403 | 403 |
| random | none | 40% | cubic_interpolation | 0.1055 | 0.1745 | 0.9974 | 403 | 403 |
| random | none | 40% | decision_tree | 0.1188 | 0.1875 | 0.9971 | 403 | 403 |
| random | none | 40% | forward_fill | 0.2453 | 0.3803 | 0.9884 | 403 | 403 |
| random | none | 40% | knn | 0.1067 | 0.1690 | 0.9976 | 403 | 403 |
| random | none | 40% | knn_upgraded | 0.1264 | 0.1918 | 0.9969 | 403 | 403 |
| random | none | 40% | linear_interpolation | 0.1067 | 0.1690 | 0.9976 | 403 | 403 |
| random | none | 40% | moving_average | 0.2199 | 0.3192 | 0.9916 | 403 | 403 |
| random | none | 40% | neural_net | 0.1326 | 0.2019 | 0.9966 | 403 | 403 |
| random | none | 40% | random_forest | 0.1079 | 0.1705 | 0.9975 | 403 | 403 |
| random | none | 40% | spline_interpolation | 0.1055 | 0.1746 | 0.9974 | 403 | 403 |
| random | none | 40% | time_interpolation | 0.1067 | 0.1690 | 0.9976 | 403 | 403 |
| random | none | 50% | adaptive_imputation | 0.1220 | 0.2018 | 0.9965 | 504 | 504 |
| random | none | 50% | cubic_interpolation | 0.1219 | 0.2017 | 0.9965 | 504 | 504 |
| random | none | 50% | decision_tree | 0.1352 | 0.2099 | 0.9964 | 504 | 504 |
| random | none | 50% | forward_fill | 0.2808 | 0.4354 | 0.9854 | 504 | 504 |
| random | none | 50% | knn | 0.1184 | 0.1850 | 0.9972 | 504 | 504 |
| random | none | 50% | knn_upgraded | 0.1479 | 0.2208 | 0.9960 | 504 | 504 |
| random | none | 50% | linear_interpolation | 0.1184 | 0.1850 | 0.9972 | 504 | 504 |
| random | none | 50% | moving_average | 0.2342 | 0.3408 | 0.9907 | 504 | 504 |
| random | none | 50% | neural_net | 0.1504 | 0.2251 | 0.9959 | 504 | 504 |
| random | none | 50% | random_forest | 0.1202 | 0.1859 | 0.9971 | 504 | 504 |
| random | none | 50% | spline_interpolation | 0.1220 | 0.2018 | 0.9965 | 504 | 504 |
| random | none | 50% | time_interpolation | 0.1184 | 0.1850 | 0.9972 | 504 | 504 |
| random | none | 60% | adaptive_imputation | 0.1466 | 0.2411 | 0.9952 | 605 | 605 |
| random | none | 60% | cubic_interpolation | 0.1466 | 0.2411 | 0.9952 | 605 | 605 |
| random | none | 60% | decision_tree | 0.1642 | 0.2573 | 0.9945 | 605 | 605 |
| random | none | 60% | forward_fill | 0.3343 | 0.5297 | 0.9782 | 605 | 605 |
| random | none | 60% | knn | 0.1381 | 0.2257 | 0.9957 | 605 | 605 |
| random | none | 60% | knn_upgraded | 0.1673 | 0.2550 | 0.9946 | 605 | 605 |
| random | none | 60% | linear_interpolation | 0.1381 | 0.2257 | 0.9957 | 605 | 605 |
| random | none | 60% | moving_average | 0.2549 | 0.3778 | 0.9885 | 605 | 605 |
| random | none | 60% | neural_net | 0.1835 | 0.2754 | 0.9937 | 605 | 605 |
| random | none | 60% | random_forest | 0.1403 | 0.2245 | 0.9957 | 605 | 605 |
| random | none | 60% | spline_interpolation | 0.1466 | 0.2411 | 0.9952 | 605 | 605 |
| random | none | 60% | time_interpolation | 0.1381 | 0.2257 | 0.9957 | 605 | 605 |
| random | none | 70% | adaptive_imputation | 0.1684 | 0.2747 | 0.9938 | 706 | 706 |
| random | none | 70% | cubic_interpolation | 0.1812 | 0.3063 | 0.9924 | 706 | 706 |
| random | none | 70% | decision_tree | 0.2007 | 0.3183 | 0.9917 | 706 | 706 |
| random | none | 70% | forward_fill | 0.4246 | 0.6898 | 0.9645 | 706 | 706 |
| random | none | 70% | knn | 0.1684 | 0.2747 | 0.9938 | 706 | 706 |
| random | none | 70% | knn_upgraded | 0.1907 | 0.2963 | 0.9928 | 706 | 706 |
| random | none | 70% | linear_interpolation | 0.1684 | 0.2747 | 0.9938 | 706 | 706 |
| random | none | 70% | moving_average | 0.2955 | 0.4520 | 0.9846 | 706 | 706 |
| random | none | 70% | neural_net | 0.2274 | 0.3465 | 0.9904 | 706 | 706 |
| random | none | 70% | random_forest | 0.1714 | 0.2767 | 0.9938 | 706 | 706 |
| random | none | 70% | spline_interpolation | 0.1812 | 0.3062 | 0.9924 | 706 | 706 |
| random | none | 70% | time_interpolation | 0.1684 | 0.2747 | 0.9938 | 706 | 706 |
| random | none | 80% | adaptive_imputation | 0.2116 | 0.3424 | 0.9902 | 806 | 806 |
| random | none | 80% | cubic_interpolation | 0.2356 | 0.4015 | 0.9859 | 806 | 806 |
| random | none | 80% | decision_tree | 0.2666 | 0.3996 | 0.9872 | 806 | 806 |
| random | none | 80% | forward_fill | 0.5769 | 0.9487 | 0.9333 | 806 | 806 |
| random | none | 80% | knn | 0.2116 | 0.3424 | 0.9902 | 806 | 806 |
| random | none | 80% | knn_upgraded | 0.2272 | 0.3521 | 0.9898 | 806 | 806 |
| random | none | 80% | linear_interpolation | 0.2116 | 0.3424 | 0.9902 | 806 | 806 |
| random | none | 80% | moving_average | 0.3761 | 0.6111 | 0.9717 | 806 | 806 |
| random | none | 80% | neural_net | 0.2964 | 0.4488 | 0.9831 | 806 | 806 |
| random | none | 80% | random_forest | 0.2193 | 0.3446 | 0.9902 | 806 | 806 |
| random | none | 80% | spline_interpolation | 0.2357 | 0.4017 | 0.9859 | 806 | 806 |
| random | none | 80% | time_interpolation | 0.2116 | 0.3424 | 0.9902 | 806 | 806 |

---

## Random missing (`random`)

### Random missing — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | spline_interpolation | 0.0721 | 0.1114 | 0.9990 | 101 | 101 |
| 10% | adaptive_imputation | 0.0721 | 0.1114 | 0.9990 | 101 | 101 |
| 10% | cubic_interpolation | 0.0721 | 0.1115 | 0.9990 | 101 | 101 |
| 10% | random_forest | 0.0796 | 0.1209 | 0.9988 | 101 | 101 |
| 10% | linear_interpolation | 0.0802 | 0.1216 | 0.9988 | 101 | 101 |
| 10% | time_interpolation | 0.0802 | 0.1216 | 0.9988 | 101 | 101 |
| 10% | knn | 0.0802 | 0.1216 | 0.9988 | 101 | 101 |
| 10% | decision_tree | 0.0857 | 0.1302 | 0.9986 | 101 | 101 |
| 10% | knn_upgraded | 0.0871 | 0.1298 | 0.9986 | 101 | 101 |
| 10% | neural_net | 0.0913 | 0.1388 | 0.9984 | 101 | 101 |
| 10% | forward_fill | 0.1771 | 0.2579 | 0.9947 | 101 | 101 |
| 10% | moving_average | 0.1941 | 0.2822 | 0.9933 | 101 | 101 |
| 20% | spline_interpolation | 0.0821 | 0.1321 | 0.9985 | 202 | 202 |
| 20% | adaptive_imputation | 0.0821 | 0.1321 | 0.9985 | 202 | 202 |
| 20% | cubic_interpolation | 0.0821 | 0.1322 | 0.9985 | 202 | 202 |
| 20% | linear_interpolation | 0.0887 | 0.1382 | 0.9984 | 202 | 202 |
| 20% | time_interpolation | 0.0887 | 0.1382 | 0.9984 | 202 | 202 |
| 20% | knn | 0.0887 | 0.1382 | 0.9984 | 202 | 202 |
| 20% | random_forest | 0.0892 | 0.1378 | 0.9984 | 202 | 202 |
| 20% | decision_tree | 0.0974 | 0.1517 | 0.9981 | 202 | 202 |
| 20% | knn_upgraded | 0.0993 | 0.1508 | 0.9981 | 202 | 202 |
| 20% | neural_net | 0.1019 | 0.1573 | 0.9980 | 202 | 202 |
| 20% | forward_fill | 0.1903 | 0.2808 | 0.9936 | 202 | 202 |
| 20% | moving_average | 0.1990 | 0.2889 | 0.9932 | 202 | 202 |
| 30% | cubic_interpolation | 0.0923 | 0.1511 | 0.9981 | 302 | 302 |
| 30% | spline_interpolation | 0.0923 | 0.1512 | 0.9981 | 302 | 302 |
| 30% | linear_interpolation | 0.0960 | 0.1521 | 0.9980 | 302 | 302 |
| 30% | time_interpolation | 0.0960 | 0.1521 | 0.9980 | 302 | 302 |
| 30% | knn | 0.0960 | 0.1521 | 0.9980 | 302 | 302 |
| 30% | adaptive_imputation | 0.0960 | 0.1521 | 0.9980 | 302 | 302 |
| 30% | random_forest | 0.0969 | 0.1531 | 0.9980 | 302 | 302 |
| 30% | decision_tree | 0.1044 | 0.1636 | 0.9976 | 302 | 302 |
| 30% | neural_net | 0.1109 | 0.1705 | 0.9975 | 302 | 302 |
| 30% | knn_upgraded | 0.1109 | 0.1709 | 0.9975 | 302 | 302 |
| 30% | moving_average | 0.2080 | 0.3054 | 0.9923 | 302 | 302 |
| 30% | forward_fill | 0.2121 | 0.3210 | 0.9916 | 302 | 302 |
| 40% | cubic_interpolation | 0.1055 | 0.1745 | 0.9974 | 403 | 403 |
| 40% | spline_interpolation | 0.1055 | 0.1746 | 0.9974 | 403 | 403 |
| 40% | adaptive_imputation | 0.1055 | 0.1746 | 0.9974 | 403 | 403 |
| 40% | linear_interpolation | 0.1067 | 0.1690 | 0.9976 | 403 | 403 |
| 40% | time_interpolation | 0.1067 | 0.1690 | 0.9976 | 403 | 403 |
| 40% | knn | 0.1067 | 0.1690 | 0.9976 | 403 | 403 |
| 40% | random_forest | 0.1079 | 0.1705 | 0.9975 | 403 | 403 |
| 40% | decision_tree | 0.1188 | 0.1875 | 0.9971 | 403 | 403 |
| 40% | knn_upgraded | 0.1264 | 0.1918 | 0.9969 | 403 | 403 |
| 40% | neural_net | 0.1326 | 0.2019 | 0.9966 | 403 | 403 |
| 40% | moving_average | 0.2199 | 0.3192 | 0.9916 | 403 | 403 |
| 40% | forward_fill | 0.2453 | 0.3803 | 0.9884 | 403 | 403 |
| 50% | linear_interpolation | 0.1184 | 0.1850 | 0.9972 | 504 | 504 |
| 50% | time_interpolation | 0.1184 | 0.1850 | 0.9972 | 504 | 504 |
| 50% | knn | 0.1184 | 0.1850 | 0.9972 | 504 | 504 |
| 50% | random_forest | 0.1202 | 0.1859 | 0.9971 | 504 | 504 |
| 50% | cubic_interpolation | 0.1219 | 0.2017 | 0.9965 | 504 | 504 |
| 50% | spline_interpolation | 0.1220 | 0.2018 | 0.9965 | 504 | 504 |
| 50% | adaptive_imputation | 0.1220 | 0.2018 | 0.9965 | 504 | 504 |
| 50% | decision_tree | 0.1352 | 0.2099 | 0.9964 | 504 | 504 |
| 50% | knn_upgraded | 0.1479 | 0.2208 | 0.9960 | 504 | 504 |
| 50% | neural_net | 0.1504 | 0.2251 | 0.9959 | 504 | 504 |
| 50% | moving_average | 0.2342 | 0.3408 | 0.9907 | 504 | 504 |
| 50% | forward_fill | 0.2808 | 0.4354 | 0.9854 | 504 | 504 |
| 60% | linear_interpolation | 0.1381 | 0.2257 | 0.9957 | 605 | 605 |
| 60% | time_interpolation | 0.1381 | 0.2257 | 0.9957 | 605 | 605 |
| 60% | knn | 0.1381 | 0.2257 | 0.9957 | 605 | 605 |
| 60% | random_forest | 0.1403 | 0.2245 | 0.9957 | 605 | 605 |
| 60% | cubic_interpolation | 0.1466 | 0.2411 | 0.9952 | 605 | 605 |
| 60% | adaptive_imputation | 0.1466 | 0.2411 | 0.9952 | 605 | 605 |
| 60% | spline_interpolation | 0.1466 | 0.2411 | 0.9952 | 605 | 605 |
| 60% | decision_tree | 0.1642 | 0.2573 | 0.9945 | 605 | 605 |
| 60% | knn_upgraded | 0.1673 | 0.2550 | 0.9946 | 605 | 605 |
| 60% | neural_net | 0.1835 | 0.2754 | 0.9937 | 605 | 605 |
| 60% | moving_average | 0.2549 | 0.3778 | 0.9885 | 605 | 605 |
| 60% | forward_fill | 0.3343 | 0.5297 | 0.9782 | 605 | 605 |
| 70% | linear_interpolation | 0.1684 | 0.2747 | 0.9938 | 706 | 706 |
| 70% | time_interpolation | 0.1684 | 0.2747 | 0.9938 | 706 | 706 |
| 70% | knn | 0.1684 | 0.2747 | 0.9938 | 706 | 706 |
| 70% | adaptive_imputation | 0.1684 | 0.2747 | 0.9938 | 706 | 706 |
| 70% | random_forest | 0.1714 | 0.2767 | 0.9938 | 706 | 706 |
| 70% | cubic_interpolation | 0.1812 | 0.3063 | 0.9924 | 706 | 706 |
| 70% | spline_interpolation | 0.1812 | 0.3062 | 0.9924 | 706 | 706 |
| 70% | knn_upgraded | 0.1907 | 0.2963 | 0.9928 | 706 | 706 |
| 70% | decision_tree | 0.2007 | 0.3183 | 0.9917 | 706 | 706 |
| 70% | neural_net | 0.2274 | 0.3465 | 0.9904 | 706 | 706 |
| 70% | moving_average | 0.2955 | 0.4520 | 0.9846 | 706 | 706 |
| 70% | forward_fill | 0.4246 | 0.6898 | 0.9645 | 706 | 706 |
| 80% | linear_interpolation | 0.2116 | 0.3424 | 0.9902 | 806 | 806 |
| 80% | time_interpolation | 0.2116 | 0.3424 | 0.9902 | 806 | 806 |
| 80% | knn | 0.2116 | 0.3424 | 0.9902 | 806 | 806 |
| 80% | adaptive_imputation | 0.2116 | 0.3424 | 0.9902 | 806 | 806 |
| 80% | random_forest | 0.2193 | 0.3446 | 0.9902 | 806 | 806 |
| 80% | knn_upgraded | 0.2272 | 0.3521 | 0.9898 | 806 | 806 |
| 80% | cubic_interpolation | 0.2356 | 0.4015 | 0.9859 | 806 | 806 |
| 80% | spline_interpolation | 0.2357 | 0.4017 | 0.9859 | 806 | 806 |
| 80% | decision_tree | 0.2666 | 0.3996 | 0.9872 | 806 | 806 |
| 80% | neural_net | 0.2964 | 0.4488 | 0.9831 | 806 | 806 |
| 80% | moving_average | 0.3761 | 0.6111 | 0.9717 | 806 | 806 |
| 80% | forward_fill | 0.5769 | 0.9487 | 0.9333 | 806 | 806 |

### Random missing — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.1771 | 0.1903 | 0.2121 | 0.2453 | 0.2808 | 0.3343 | 0.4246 | 0.5769 |
| linear_interpolation | 0.0802 | 0.0887 | 0.0960 | 0.1067 | 0.1184 | 0.1381 | 0.1684 | 0.2116 |
| time_interpolation | 0.0802 | 0.0887 | 0.0960 | 0.1067 | 0.1184 | 0.1381 | 0.1684 | 0.2116 |
| cubic_interpolation | 0.0721 | 0.0821 | 0.0923 | 0.1055 | 0.1219 | 0.1466 | 0.1812 | 0.2356 |
| spline_interpolation | 0.0721 | 0.0821 | 0.0923 | 0.1055 | 0.1220 | 0.1466 | 0.1812 | 0.2357 |
| knn | 0.0802 | 0.0887 | 0.0960 | 0.1067 | 0.1184 | 0.1381 | 0.1684 | 0.2116 |
| decision_tree | 0.0857 | 0.0974 | 0.1044 | 0.1188 | 0.1352 | 0.1642 | 0.2007 | 0.2666 |
| random_forest | 0.0796 | 0.0892 | 0.0969 | 0.1079 | 0.1202 | 0.1403 | 0.1714 | 0.2193 |

### Random missing — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.2579 | 0.2808 | 0.3210 | 0.3803 | 0.4354 | 0.5297 | 0.6898 | 0.9487 |
| linear_interpolation | 0.1216 | 0.1382 | 0.1521 | 0.1690 | 0.1850 | 0.2257 | 0.2747 | 0.3424 |
| time_interpolation | 0.1216 | 0.1382 | 0.1521 | 0.1690 | 0.1850 | 0.2257 | 0.2747 | 0.3424 |
| cubic_interpolation | 0.1115 | 0.1322 | 0.1511 | 0.1745 | 0.2017 | 0.2411 | 0.3063 | 0.4015 |
| spline_interpolation | 0.1114 | 0.1321 | 0.1512 | 0.1746 | 0.2018 | 0.2411 | 0.3062 | 0.4017 |
| knn | 0.1216 | 0.1382 | 0.1521 | 0.1690 | 0.1850 | 0.2257 | 0.2747 | 0.3424 |
| decision_tree | 0.1302 | 0.1517 | 0.1636 | 0.1875 | 0.2099 | 0.2573 | 0.3183 | 0.3996 |
| random_forest | 0.1209 | 0.1378 | 0.1531 | 0.1705 | 0.1859 | 0.2245 | 0.2767 | 0.3446 |

### Random missing — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.9947 | 0.9936 | 0.9916 | 0.9884 | 0.9854 | 0.9782 | 0.9645 | 0.9333 |
| linear_interpolation | 0.9988 | 0.9984 | 0.9980 | 0.9976 | 0.9972 | 0.9957 | 0.9938 | 0.9902 |
| time_interpolation | 0.9988 | 0.9984 | 0.9980 | 0.9976 | 0.9972 | 0.9957 | 0.9938 | 0.9902 |
| cubic_interpolation | 0.9990 | 0.9985 | 0.9981 | 0.9974 | 0.9965 | 0.9952 | 0.9924 | 0.9859 |
| spline_interpolation | 0.9990 | 0.9985 | 0.9981 | 0.9974 | 0.9965 | 0.9952 | 0.9924 | 0.9859 |
| knn | 0.9988 | 0.9984 | 0.9980 | 0.9976 | 0.9972 | 0.9957 | 0.9938 | 0.9902 |
| decision_tree | 0.9986 | 0.9981 | 0.9976 | 0.9971 | 0.9964 | 0.9945 | 0.9917 | 0.9872 |
| random_forest | 0.9988 | 0.9984 | 0.9980 | 0.9975 | 0.9971 | 0.9957 | 0.9938 | 0.9902 |

---

## Block missing (`block`)

### Block missing — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | neural_net | 2.1311 | 2.5063 | -0.6337 | 101 | 101 |
| 10% | decision_tree | 2.1369 | 2.5103 | -0.6646 | 101 | 101 |
| 10% | knn_upgraded | 2.1504 | 2.5247 | -0.6509 | 101 | 101 |
| 10% | random_forest | 2.1507 | 2.5245 | -0.6515 | 101 | 101 |
| 10% | linear_interpolation | 2.1669 | 2.5400 | -0.6694 | 101 | 101 |
| 10% | time_interpolation | 2.1669 | 2.5400 | -0.6694 | 101 | 101 |
| 10% | knn | 2.1669 | 2.5400 | -0.6694 | 101 | 101 |
| 10% | adaptive_imputation | 2.1669 | 2.5400 | -0.6694 | 101 | 101 |
| 10% | cubic_interpolation | 2.2159 | 2.7342 | -2.5604 | 101 | 101 |
| 10% | spline_interpolation | 2.2159 | 2.7342 | -2.5604 | 101 | 101 |
| 10% | moving_average | 3.1873 | 3.8070 | -1.8208 | 101 | 101 |
| 10% | forward_fill | 3.4311 | 4.0140 | -2.0658 | 101 | 101 |
| 20% | neural_net | 2.5198 | 3.1131 | -0.3658 | 202 | 202 |
| 20% | knn_upgraded | 2.5281 | 3.1140 | -0.3600 | 202 | 202 |
| 20% | random_forest | 2.5299 | 3.1174 | -0.3611 | 202 | 202 |
| 20% | linear_interpolation | 2.5336 | 3.1165 | -0.3624 | 202 | 202 |
| 20% | time_interpolation | 2.5336 | 3.1165 | -0.3624 | 202 | 202 |
| 20% | knn | 2.5336 | 3.1165 | -0.3624 | 202 | 202 |
| 20% | decision_tree | 2.5355 | 3.1254 | -0.3672 | 202 | 202 |
| 20% | adaptive_imputation | 2.6286 | 3.2177 | -0.4873 | 202 | 202 |
| 20% | moving_average | 3.1532 | 3.8480 | -1.1418 | 202 | 202 |
| 20% | forward_fill | 3.2575 | 3.9366 | -1.2617 | 202 | 202 |
| 20% | cubic_interpolation | 6.7633 | 8.0402 | -11.9963 | 202 | 202 |
| 20% | spline_interpolation | 6.7633 | 8.0402 | -11.9963 | 202 | 202 |
| 30% | neural_net | 3.7507 | 4.4459 | -1.1276 | 302 | 302 |
| 30% | knn_upgraded | 3.7551 | 4.4470 | -1.1302 | 302 | 302 |
| 30% | linear_interpolation | 3.7564 | 4.4475 | -1.1330 | 302 | 302 |
| 30% | time_interpolation | 3.7564 | 4.4475 | -1.1330 | 302 | 302 |
| 30% | knn | 3.7564 | 4.4475 | -1.1330 | 302 | 302 |
| 30% | random_forest | 3.7656 | 4.4580 | -1.1396 | 302 | 302 |
| 30% | decision_tree | 3.7704 | 4.4610 | -1.1290 | 302 | 302 |
| 30% | moving_average | 4.6951 | 5.4889 | -1.8393 | 302 | 302 |
| 30% | forward_fill | 4.7738 | 5.5457 | -1.8891 | 302 | 302 |
| 30% | adaptive_imputation | 5.6602 | 6.6625 | -6.2216 | 302 | 302 |
| 30% | cubic_interpolation | 9.1979 | 10.7027 | -14.6333 | 302 | 302 |
| 30% | spline_interpolation | 9.1979 | 10.7027 | -14.6333 | 302 | 302 |
| 40% | random_forest | 2.8163 | 3.5018 | -0.6697 | 403 | 403 |
| 40% | knn_upgraded | 2.8223 | 3.5072 | -0.6663 | 403 | 403 |
| 40% | decision_tree | 2.8276 | 3.5164 | -0.6885 | 403 | 403 |
| 40% | neural_net | 2.8297 | 3.5198 | -0.6877 | 403 | 403 |
| 40% | adaptive_imputation | 2.8299 | 3.5155 | -0.6770 | 403 | 403 |
| 40% | linear_interpolation | 2.8349 | 3.5204 | -0.6839 | 403 | 403 |
| 40% | time_interpolation | 2.8349 | 3.5204 | -0.6839 | 403 | 403 |
| 40% | knn | 2.8349 | 3.5204 | -0.6839 | 403 | 403 |
| 40% | moving_average | 3.9736 | 4.7874 | -1.3872 | 403 | 403 |
| 40% | forward_fill | 4.0476 | 4.8470 | -1.4412 | 403 | 403 |
| 40% | cubic_interpolation | 11.4708 | 13.5059 | -30.8877 | 403 | 403 |
| 40% | spline_interpolation | 11.4708 | 13.5059 | -30.8877 | 403 | 403 |
| 50% | random_forest | 3.0882 | 3.8701 | -0.2135 | 504 | 504 |
| 50% | neural_net | 3.0885 | 3.8732 | -0.2157 | 504 | 504 |
| 50% | linear_interpolation | 3.0897 | 3.8749 | -0.2134 | 504 | 504 |
| 50% | time_interpolation | 3.0897 | 3.8749 | -0.2134 | 504 | 504 |
| 50% | knn | 3.0897 | 3.8749 | -0.2134 | 504 | 504 |
| 50% | knn_upgraded | 3.0903 | 3.8729 | -0.2114 | 504 | 504 |
| 50% | decision_tree | 3.0915 | 3.8730 | -0.2155 | 504 | 504 |
| 50% | moving_average | 3.9649 | 4.8081 | -0.7849 | 504 | 504 |
| 50% | forward_fill | 4.0175 | 4.8459 | -0.8167 | 504 | 504 |
| 50% | adaptive_imputation | 4.8938 | 5.9512 | -4.4041 | 504 | 504 |
| 50% | cubic_interpolation | 12.4437 | 14.4897 | -28.1072 | 504 | 504 |
| 50% | spline_interpolation | 12.4437 | 14.4897 | -28.1072 | 504 | 504 |
| 60% | neural_net | 3.7285 | 4.5471 | -0.7923 | 605 | 605 |
| 60% | linear_interpolation | 3.7336 | 4.5401 | -0.7819 | 605 | 605 |
| 60% | time_interpolation | 3.7336 | 4.5401 | -0.7819 | 605 | 605 |
| 60% | knn | 3.7336 | 4.5401 | -0.7819 | 605 | 605 |
| 60% | knn_upgraded | 3.7346 | 4.5431 | -0.7841 | 605 | 605 |
| 60% | decision_tree | 3.7402 | 4.5503 | -0.7871 | 605 | 605 |
| 60% | random_forest | 3.7481 | 4.5574 | -0.8020 | 605 | 605 |
| 60% | adaptive_imputation | 4.3340 | 5.1401 | -1.5458 | 605 | 605 |
| 60% | moving_average | 5.6654 | 6.5276 | -2.9424 | 605 | 605 |
| 60% | forward_fill | 5.7158 | 6.5606 | -2.9819 | 605 | 605 |
| 60% | cubic_interpolation | 21.3524 | 24.6079 | -68.9215 | 605 | 605 |
| 60% | spline_interpolation | 21.3970 | 24.6600 | -69.5461 | 605 | 605 |
| 70% | decision_tree | 3.7657 | 4.5868 | -1.1037 | 706 | 706 |
| 70% | random_forest | 3.7718 | 4.5904 | -1.1070 | 706 | 706 |
| 70% | knn_upgraded | 3.7799 | 4.5993 | -1.1126 | 706 | 706 |
| 70% | neural_net | 3.7822 | 4.6177 | -1.1366 | 706 | 706 |
| 70% | linear_interpolation | 3.7852 | 4.6027 | -1.1138 | 706 | 706 |
| 70% | time_interpolation | 3.7852 | 4.6027 | -1.1138 | 706 | 706 |
| 70% | knn | 3.7852 | 4.6027 | -1.1138 | 706 | 706 |
| 70% | moving_average | 4.2395 | 5.0447 | -1.5173 | 706 | 706 |
| 70% | forward_fill | 4.2738 | 5.0736 | -1.5385 | 706 | 706 |
| 70% | adaptive_imputation | 4.3185 | 5.1378 | -1.5666 | 706 | 706 |
| 70% | cubic_interpolation | 16.9042 | 19.7851 | -55.0985 | 706 | 706 |
| 70% | spline_interpolation | 16.9042 | 19.7851 | -55.0985 | 706 | 706 |
| 80% | decision_tree | 3.5502 | 4.4147 | -0.5277 | 806 | 806 |
| 80% | random_forest | 3.5510 | 4.4152 | -0.5290 | 806 | 806 |
| 80% | knn_upgraded | 3.5544 | 4.4192 | -0.5309 | 806 | 806 |
| 80% | neural_net | 3.5561 | 4.4239 | -0.5281 | 806 | 806 |
| 80% | linear_interpolation | 3.5617 | 4.4259 | -0.5369 | 806 | 806 |
| 80% | time_interpolation | 3.5617 | 4.4259 | -0.5369 | 806 | 806 |
| 80% | knn | 3.5617 | 4.4259 | -0.5369 | 806 | 806 |
| 80% | moving_average | 5.0404 | 5.9042 | -2.1914 | 806 | 806 |
| 80% | forward_fill | 5.0784 | 5.9290 | -2.2239 | 806 | 806 |
| 80% | adaptive_imputation | 11.6266 | 13.5576 | -110.0308 | 806 | 806 |
| 80% | cubic_interpolation | 29.3598 | 33.6612 | -181.9469 | 806 | 806 |
| 80% | spline_interpolation | 29.4213 | 33.7329 | -183.2164 | 806 | 806 |

### Block missing — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 3.4311 | 3.2575 | 4.7738 | 4.0476 | 4.0175 | 5.7158 | 4.2738 | 5.0784 |
| linear_interpolation | 2.1669 | 2.5336 | 3.7564 | 2.8349 | 3.0897 | 3.7336 | 3.7852 | 3.5617 |
| time_interpolation | 2.1669 | 2.5336 | 3.7564 | 2.8349 | 3.0897 | 3.7336 | 3.7852 | 3.5617 |
| cubic_interpolation | 2.2159 | 6.7633 | 9.1979 | 11.4708 | 12.4437 | 21.3524 | 16.9042 | 29.3598 |
| spline_interpolation | 2.2159 | 6.7633 | 9.1979 | 11.4708 | 12.4437 | 21.3970 | 16.9042 | 29.4213 |
| knn | 2.1669 | 2.5336 | 3.7564 | 2.8349 | 3.0897 | 3.7336 | 3.7852 | 3.5617 |
| decision_tree | 2.1369 | 2.5355 | 3.7704 | 2.8276 | 3.0915 | 3.7402 | 3.7657 | 3.5502 |
| random_forest | 2.1507 | 2.5299 | 3.7656 | 2.8163 | 3.0882 | 3.7481 | 3.7718 | 3.5510 |

### Block missing — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 4.0140 | 3.9366 | 5.5457 | 4.8470 | 4.8459 | 6.5606 | 5.0736 | 5.9290 |
| linear_interpolation | 2.5400 | 3.1165 | 4.4475 | 3.5204 | 3.8749 | 4.5401 | 4.6027 | 4.4259 |
| time_interpolation | 2.5400 | 3.1165 | 4.4475 | 3.5204 | 3.8749 | 4.5401 | 4.6027 | 4.4259 |
| cubic_interpolation | 2.7342 | 8.0402 | 10.7027 | 13.5059 | 14.4897 | 24.6079 | 19.7851 | 33.6612 |
| spline_interpolation | 2.7342 | 8.0402 | 10.7027 | 13.5059 | 14.4897 | 24.6600 | 19.7851 | 33.7329 |
| knn | 2.5400 | 3.1165 | 4.4475 | 3.5204 | 3.8749 | 4.5401 | 4.6027 | 4.4259 |
| decision_tree | 2.5103 | 3.1254 | 4.4610 | 3.5164 | 3.8730 | 4.5503 | 4.5868 | 4.4147 |
| random_forest | 2.5245 | 3.1174 | 4.4580 | 3.5018 | 3.8701 | 4.5574 | 4.5904 | 4.4152 |

### Block missing — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -2.0658 | -1.2617 | -1.8891 | -1.4412 | -0.8167 | -2.9819 | -1.5385 | -2.2239 |
| linear_interpolation | -0.6694 | -0.3624 | -1.1330 | -0.6839 | -0.2134 | -0.7819 | -1.1138 | -0.5369 |
| time_interpolation | -0.6694 | -0.3624 | -1.1330 | -0.6839 | -0.2134 | -0.7819 | -1.1138 | -0.5369 |
| cubic_interpolation | -2.5604 | -11.9963 | -14.6333 | -30.8877 | -28.1072 | -68.9215 | -55.0985 | -181.9469 |
| spline_interpolation | -2.5604 | -11.9963 | -14.6333 | -30.8877 | -28.1072 | -69.5461 | -55.0985 | -183.2164 |
| knn | -0.6694 | -0.3624 | -1.1330 | -0.6839 | -0.2134 | -0.7819 | -1.1138 | -0.5369 |
| decision_tree | -0.6646 | -0.3672 | -1.1290 | -0.6885 | -0.2155 | -0.7871 | -1.1037 | -0.5277 |
| random_forest | -0.6515 | -0.3611 | -1.1396 | -0.6697 | -0.2135 | -0.8020 | -1.1070 | -0.5290 |

---

## Block na početku (`block_start`)

### Block na početku — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | cubic_interpolation | 2.0883 | 2.4984 | -0.4797 | 101 | 101 |
| 10% | knn_upgraded | 2.1801 | 2.5213 | -0.5421 | 101 | 101 |
| 10% | linear_interpolation | 2.1935 | 2.5342 | -0.5554 | 101 | 101 |
| 10% | time_interpolation | 2.1935 | 2.5342 | -0.5554 | 101 | 101 |
| 10% | knn | 2.1935 | 2.5342 | -0.5554 | 101 | 101 |
| 10% | adaptive_imputation | 2.1935 | 2.5342 | -0.5554 | 101 | 101 |
| 10% | neural_net | 2.2066 | 2.5792 | -0.5654 | 101 | 101 |
| 10% | random_forest | 2.2469 | 2.6107 | -0.5232 | 101 | 101 |
| 10% | spline_interpolation | 2.3357 | 2.7472 | -0.9159 | 101 | 101 |
| 10% | decision_tree | 2.4108 | 2.8080 | -0.6081 | 101 | 101 |
| 10% | moving_average | 3.0268 | 3.7093 | -1.3377 | 101 | 101 |
| 10% | forward_fill | 3.2454 | 3.8822 | -1.5198 | 101 | 101 |
| 20% | knn_upgraded | 2.7903 | 3.4767 | -0.4325 | 202 | 202 |
| 20% | linear_interpolation | 2.8362 | 3.5406 | -0.5235 | 202 | 202 |
| 20% | time_interpolation | 2.8362 | 3.5406 | -0.5235 | 202 | 202 |
| 20% | knn | 2.8362 | 3.5406 | -0.5235 | 202 | 202 |
| 20% | adaptive_imputation | 2.8362 | 3.5406 | -0.5235 | 202 | 202 |
| 20% | random_forest | 2.8921 | 3.5607 | -0.4654 | 202 | 202 |
| 20% | neural_net | 2.9052 | 3.5747 | -0.5858 | 202 | 202 |
| 20% | decision_tree | 3.0008 | 3.6520 | -0.5518 | 202 | 202 |
| 20% | moving_average | 3.3169 | 4.0259 | -0.9689 | 202 | 202 |
| 20% | forward_fill | 3.4633 | 4.1554 | -1.1046 | 202 | 202 |
| 20% | cubic_interpolation | 4.6230 | 5.8036 | -4.8747 | 202 | 202 |
| 20% | spline_interpolation | 5.6963 | 6.9300 | -8.0180 | 202 | 202 |
| 30% | linear_interpolation | 3.1027 | 3.8831 | -0.4297 | 302 | 302 |
| 30% | time_interpolation | 3.1027 | 3.8831 | -0.4297 | 302 | 302 |
| 30% | knn | 3.1027 | 3.8831 | -0.4297 | 302 | 302 |
| 30% | neural_net | 3.1169 | 3.8915 | -0.4507 | 302 | 302 |
| 30% | knn_upgraded | 3.1379 | 3.8925 | -0.4460 | 302 | 302 |
| 30% | adaptive_imputation | 3.1570 | 3.9690 | -0.4601 | 302 | 302 |
| 30% | random_forest | 3.2191 | 3.9583 | -0.5043 | 302 | 302 |
| 30% | decision_tree | 3.3207 | 4.0397 | -0.5476 | 302 | 302 |
| 30% | moving_average | 3.8130 | 4.5793 | -0.9568 | 302 | 302 |
| 30% | forward_fill | 3.8785 | 4.6261 | -0.9921 | 302 | 302 |
| 30% | cubic_interpolation | 5.2982 | 6.4774 | -5.8230 | 302 | 302 |
| 30% | spline_interpolation | 6.9550 | 8.1771 | -11.6508 | 302 | 302 |
| 40% | linear_interpolation | 3.1895 | 3.8872 | -0.5076 | 403 | 403 |
| 40% | time_interpolation | 3.1895 | 3.8872 | -0.5076 | 403 | 403 |
| 40% | knn | 3.1895 | 3.8872 | -0.5076 | 403 | 403 |
| 40% | neural_net | 3.2257 | 3.9483 | -0.5070 | 403 | 403 |
| 40% | knn_upgraded | 3.2904 | 3.9908 | -0.5004 | 403 | 403 |
| 40% | random_forest | 3.3091 | 4.0009 | -0.5001 | 403 | 403 |
| 40% | decision_tree | 3.4974 | 4.1910 | -0.5730 | 403 | 403 |
| 40% | adaptive_imputation | 3.4974 | 4.1910 | -0.5730 | 403 | 403 |
| 40% | moving_average | 4.1368 | 4.9230 | -1.0637 | 403 | 403 |
| 40% | forward_fill | 4.2018 | 4.9705 | -1.1020 | 403 | 403 |
| 40% | cubic_interpolation | 7.7071 | 9.2377 | -13.9591 | 403 | 403 |
| 40% | spline_interpolation | 10.7131 | 12.2507 | -28.4796 | 403 | 403 |
| 50% | linear_interpolation | 3.0703 | 3.8144 | -0.2076 | 504 | 504 |
| 50% | time_interpolation | 3.0703 | 3.8144 | -0.2076 | 504 | 504 |
| 50% | knn | 3.0703 | 3.8144 | -0.2076 | 504 | 504 |
| 50% | adaptive_imputation | 3.0703 | 3.8144 | -0.2076 | 504 | 504 |
| 50% | neural_net | 3.0949 | 3.8435 | -0.2116 | 504 | 504 |
| 50% | knn_upgraded | 3.1737 | 3.9217 | -0.2186 | 504 | 504 |
| 50% | random_forest | 3.1894 | 3.9164 | -0.2262 | 504 | 504 |
| 50% | decision_tree | 3.3272 | 4.0544 | -0.2935 | 504 | 504 |
| 50% | moving_average | 4.4217 | 5.2560 | -1.0774 | 504 | 504 |
| 50% | forward_fill | 4.4899 | 5.3117 | -1.1226 | 504 | 504 |
| 50% | cubic_interpolation | 7.0279 | 8.4252 | -12.7017 | 504 | 504 |
| 50% | spline_interpolation | 10.0062 | 11.4416 | -26.6400 | 504 | 504 |
| 60% | linear_interpolation | 3.5792 | 4.3585 | -0.5799 | 605 | 605 |
| 60% | time_interpolation | 3.5792 | 4.3585 | -0.5799 | 605 | 605 |
| 60% | knn | 3.5792 | 4.3585 | -0.5799 | 605 | 605 |
| 60% | neural_net | 3.6427 | 4.4369 | -0.6054 | 605 | 605 |
| 60% | knn_upgraded | 3.6654 | 4.4541 | -0.6121 | 605 | 605 |
| 60% | random_forest | 3.7472 | 4.5327 | -0.6507 | 605 | 605 |
| 60% | decision_tree | 3.8827 | 4.6781 | -0.7344 | 605 | 605 |
| 60% | moving_average | 4.4693 | 5.2925 | -1.1625 | 605 | 605 |
| 60% | forward_fill | 4.5089 | 5.3190 | -1.1824 | 605 | 605 |
| 60% | cubic_interpolation | 11.3422 | 13.2668 | -35.0885 | 605 | 605 |
| 60% | adaptive_imputation | 11.3422 | 13.2668 | -35.0885 | 605 | 605 |
| 60% | spline_interpolation | 15.8351 | 17.7297 | -69.2969 | 605 | 605 |
| 70% | linear_interpolation | 3.9971 | 4.8378 | -1.0472 | 706 | 706 |
| 70% | time_interpolation | 3.9971 | 4.8378 | -1.0472 | 706 | 706 |
| 70% | knn | 3.9971 | 4.8378 | -1.0472 | 706 | 706 |
| 70% | neural_net | 4.0425 | 4.8959 | -1.0793 | 706 | 706 |
| 70% | knn_upgraded | 4.0605 | 4.9036 | -1.0196 | 706 | 706 |
| 70% | random_forest | 4.0886 | 4.9301 | -1.0313 | 706 | 706 |
| 70% | decision_tree | 4.1595 | 4.9917 | -1.0482 | 706 | 706 |
| 70% | moving_average | 4.4992 | 5.3155 | -1.1966 | 706 | 706 |
| 70% | forward_fill | 4.5190 | 5.3266 | -1.2056 | 706 | 706 |
| 70% | cubic_interpolation | 9.5612 | 11.3483 | -14.9275 | 706 | 706 |
| 70% | adaptive_imputation | 9.5612 | 11.3483 | -14.9275 | 706 | 706 |
| 70% | spline_interpolation | 13.3992 | 15.2091 | -29.9568 | 706 | 706 |
| 80% | linear_interpolation | 3.6322 | 4.5405 | -0.5088 | 806 | 806 |
| 80% | time_interpolation | 3.6322 | 4.5405 | -0.5088 | 806 | 806 |
| 80% | knn | 3.6322 | 4.5405 | -0.5088 | 806 | 806 |
| 80% | neural_net | 3.6481 | 4.5679 | -0.5436 | 806 | 806 |
| 80% | knn_upgraded | 3.7887 | 4.7033 | -0.5973 | 806 | 806 |
| 80% | random_forest | 3.8540 | 4.7575 | -0.6333 | 806 | 806 |
| 80% | decision_tree | 3.9284 | 4.8320 | -0.6777 | 806 | 806 |
| 80% | moving_average | 4.4819 | 5.3513 | -1.0557 | 806 | 806 |
| 80% | forward_fill | 4.5077 | 5.3638 | -1.0658 | 806 | 806 |
| 80% | adaptive_imputation | 4.5077 | 5.3638 | -1.0658 | 806 | 806 |
| 80% | cubic_interpolation | 10.8286 | 12.7500 | -17.6325 | 806 | 806 |
| 80% | spline_interpolation | 15.0115 | 16.9479 | -34.3614 | 806 | 806 |

### Block na početku — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 3.2454 | 3.4633 | 3.8785 | 4.2018 | 4.4899 | 4.5089 | 4.5190 | 4.5077 |
| linear_interpolation | 2.1935 | 2.8362 | 3.1027 | 3.1895 | 3.0703 | 3.5792 | 3.9971 | 3.6322 |
| time_interpolation | 2.1935 | 2.8362 | 3.1027 | 3.1895 | 3.0703 | 3.5792 | 3.9971 | 3.6322 |
| cubic_interpolation | 2.0883 | 4.6230 | 5.2982 | 7.7071 | 7.0279 | 11.3422 | 9.5612 | 10.8286 |
| spline_interpolation | 2.3357 | 5.6963 | 6.9550 | 10.7131 | 10.0062 | 15.8351 | 13.3992 | 15.0115 |
| knn | 2.1935 | 2.8362 | 3.1027 | 3.1895 | 3.0703 | 3.5792 | 3.9971 | 3.6322 |
| decision_tree | 2.4108 | 3.0008 | 3.3207 | 3.4974 | 3.3272 | 3.8827 | 4.1595 | 3.9284 |
| random_forest | 2.2469 | 2.8921 | 3.2191 | 3.3091 | 3.1894 | 3.7472 | 4.0886 | 3.8540 |

### Block na početku — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 3.8822 | 4.1554 | 4.6261 | 4.9705 | 5.3117 | 5.3190 | 5.3266 | 5.3638 |
| linear_interpolation | 2.5342 | 3.5406 | 3.8831 | 3.8872 | 3.8144 | 4.3585 | 4.8378 | 4.5405 |
| time_interpolation | 2.5342 | 3.5406 | 3.8831 | 3.8872 | 3.8144 | 4.3585 | 4.8378 | 4.5405 |
| cubic_interpolation | 2.4984 | 5.8036 | 6.4774 | 9.2377 | 8.4252 | 13.2668 | 11.3483 | 12.7500 |
| spline_interpolation | 2.7472 | 6.9300 | 8.1771 | 12.2507 | 11.4416 | 17.7297 | 15.2091 | 16.9479 |
| knn | 2.5342 | 3.5406 | 3.8831 | 3.8872 | 3.8144 | 4.3585 | 4.8378 | 4.5405 |
| decision_tree | 2.8080 | 3.6520 | 4.0397 | 4.1910 | 4.0544 | 4.6781 | 4.9917 | 4.8320 |
| random_forest | 2.6107 | 3.5607 | 3.9583 | 4.0009 | 3.9164 | 4.5327 | 4.9301 | 4.7575 |

### Block na početku — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -1.5198 | -1.1046 | -0.9921 | -1.1020 | -1.1226 | -1.1824 | -1.2056 | -1.0658 |
| linear_interpolation | -0.5554 | -0.5235 | -0.4297 | -0.5076 | -0.2076 | -0.5799 | -1.0472 | -0.5088 |
| time_interpolation | -0.5554 | -0.5235 | -0.4297 | -0.5076 | -0.2076 | -0.5799 | -1.0472 | -0.5088 |
| cubic_interpolation | -0.4797 | -4.8747 | -5.8230 | -13.9591 | -12.7017 | -35.0885 | -14.9275 | -17.6325 |
| spline_interpolation | -0.9159 | -8.0180 | -11.6508 | -28.4796 | -26.6400 | -69.2969 | -29.9568 | -34.3614 |
| knn | -0.5554 | -0.5235 | -0.4297 | -0.5076 | -0.2076 | -0.5799 | -1.0472 | -0.5088 |
| decision_tree | -0.6081 | -0.5518 | -0.5476 | -0.5730 | -0.2935 | -0.7344 | -1.0482 | -0.6777 |
| random_forest | -0.5232 | -0.4654 | -0.5043 | -0.5001 | -0.2262 | -0.6507 | -1.0313 | -0.6333 |

---

## Block u sredini (`block_middle`)

### Block u sredini — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | knn_upgraded | 2.4864 | 2.9165 | -0.7950 | 101 | 101 |
| 10% | neural_net | 2.4911 | 2.9222 | -0.8105 | 101 | 101 |
| 10% | linear_interpolation | 2.4936 | 2.9240 | -0.8101 | 101 | 101 |
| 10% | time_interpolation | 2.4936 | 2.9240 | -0.8101 | 101 | 101 |
| 10% | knn | 2.4936 | 2.9240 | -0.8101 | 101 | 101 |
| 10% | adaptive_imputation | 2.4936 | 2.9240 | -0.8101 | 101 | 101 |
| 10% | random_forest | 2.4939 | 2.9248 | -0.8009 | 101 | 101 |
| 10% | decision_tree | 2.5238 | 2.9579 | -0.8497 | 101 | 101 |
| 10% | cubic_interpolation | 2.8902 | 3.4244 | -4.8049 | 101 | 101 |
| 10% | spline_interpolation | 2.8902 | 3.4244 | -4.8049 | 101 | 101 |
| 10% | moving_average | 3.1420 | 3.6840 | -1.8895 | 101 | 101 |
| 10% | forward_fill | 3.3713 | 3.8757 | -2.1698 | 101 | 101 |
| 20% | neural_net | 2.4173 | 3.0136 | -0.3261 | 202 | 202 |
| 20% | knn_upgraded | 2.4231 | 3.0166 | -0.3225 | 202 | 202 |
| 20% | random_forest | 2.4256 | 3.0213 | -0.3282 | 202 | 202 |
| 20% | decision_tree | 2.4272 | 3.0207 | -0.3236 | 202 | 202 |
| 20% | linear_interpolation | 2.4287 | 3.0196 | -0.3214 | 202 | 202 |
| 20% | time_interpolation | 2.4287 | 3.0196 | -0.3214 | 202 | 202 |
| 20% | knn | 2.4287 | 3.0196 | -0.3214 | 202 | 202 |
| 20% | adaptive_imputation | 2.4287 | 3.0196 | -0.3214 | 202 | 202 |
| 20% | moving_average | 3.5030 | 4.2108 | -1.9514 | 202 | 202 |
| 20% | forward_fill | 3.6248 | 4.3054 | -2.1059 | 202 | 202 |
| 20% | cubic_interpolation | 7.0993 | 8.4025 | -17.1314 | 202 | 202 |
| 20% | spline_interpolation | 7.0993 | 8.4025 | -17.1314 | 202 | 202 |
| 30% | decision_tree | 2.9535 | 3.6183 | -0.9175 | 302 | 302 |
| 30% | random_forest | 2.9625 | 3.6329 | -0.9174 | 302 | 302 |
| 30% | neural_net | 2.9640 | 3.6404 | -0.9123 | 302 | 302 |
| 30% | linear_interpolation | 2.9642 | 3.6305 | -0.9238 | 302 | 302 |
| 30% | time_interpolation | 2.9642 | 3.6305 | -0.9238 | 302 | 302 |
| 30% | knn | 2.9642 | 3.6305 | -0.9238 | 302 | 302 |
| 30% | knn_upgraded | 2.9657 | 3.6355 | -0.9249 | 302 | 302 |
| 30% | moving_average | 4.3349 | 5.0339 | -3.0334 | 302 | 302 |
| 30% | forward_fill | 4.4178 | 5.0875 | -3.1045 | 302 | 302 |
| 30% | cubic_interpolation | 7.5157 | 8.8354 | -9.8463 | 302 | 302 |
| 30% | spline_interpolation | 7.5157 | 8.8354 | -9.8463 | 302 | 302 |
| 30% | adaptive_imputation | 7.5157 | 8.8354 | -9.8463 | 302 | 302 |
| 40% | neural_net | 3.3719 | 4.0516 | -1.0600 | 403 | 403 |
| 40% | knn_upgraded | 3.3730 | 4.0436 | -1.0475 | 403 | 403 |
| 40% | decision_tree | 3.3739 | 4.0479 | -1.0437 | 403 | 403 |
| 40% | random_forest | 3.3784 | 4.0501 | -1.0471 | 403 | 403 |
| 40% | adaptive_imputation | 3.3784 | 4.0501 | -1.0471 | 403 | 403 |
| 40% | linear_interpolation | 3.3800 | 4.0495 | -1.0486 | 403 | 403 |
| 40% | time_interpolation | 3.3800 | 4.0495 | -1.0486 | 403 | 403 |
| 40% | knn | 3.3800 | 4.0495 | -1.0486 | 403 | 403 |
| 40% | moving_average | 3.4675 | 4.1654 | -1.0534 | 403 | 403 |
| 40% | forward_fill | 3.4973 | 4.1845 | -1.0817 | 403 | 403 |
| 40% | cubic_interpolation | 9.2167 | 11.0021 | -14.7989 | 403 | 403 |
| 40% | spline_interpolation | 9.2167 | 11.0021 | -14.7989 | 403 | 403 |
| 50% | knn_upgraded | 3.2569 | 3.9244 | -0.4088 | 504 | 504 |
| 50% | decision_tree | 3.2622 | 3.9272 | -0.4119 | 504 | 504 |
| 50% | linear_interpolation | 3.2633 | 3.9330 | -0.4140 | 504 | 504 |
| 50% | time_interpolation | 3.2633 | 3.9330 | -0.4140 | 504 | 504 |
| 50% | knn | 3.2633 | 3.9330 | -0.4140 | 504 | 504 |
| 50% | random_forest | 3.2658 | 3.9344 | -0.4174 | 504 | 504 |
| 50% | neural_net | 3.2800 | 3.9480 | -0.4332 | 504 | 504 |
| 50% | moving_average | 4.0500 | 4.8115 | -1.4269 | 504 | 504 |
| 50% | forward_fill | 4.1161 | 4.8768 | -1.4949 | 504 | 504 |
| 50% | cubic_interpolation | 13.4306 | 15.7456 | -32.2616 | 504 | 504 |
| 50% | spline_interpolation | 13.4306 | 15.7456 | -32.2616 | 504 | 504 |
| 50% | adaptive_imputation | 13.4306 | 15.7456 | -32.2616 | 504 | 504 |
| 60% | linear_interpolation | 3.2926 | 4.0603 | -0.4461 | 605 | 605 |
| 60% | time_interpolation | 3.2926 | 4.0603 | -0.4461 | 605 | 605 |
| 60% | knn | 3.2926 | 4.0603 | -0.4461 | 605 | 605 |
| 60% | decision_tree | 3.2947 | 4.0635 | -0.4516 | 605 | 605 |
| 60% | knn_upgraded | 3.2985 | 4.0675 | -0.4570 | 605 | 605 |
| 60% | random_forest | 3.3012 | 4.0707 | -0.4622 | 605 | 605 |
| 60% | neural_net | 3.3139 | 4.0932 | -0.4800 | 605 | 605 |
| 60% | moving_average | 3.9999 | 4.7228 | -1.3084 | 605 | 605 |
| 60% | forward_fill | 4.0337 | 4.7417 | -1.3271 | 605 | 605 |
| 60% | adaptive_imputation | 4.0337 | 4.7417 | -1.3271 | 605 | 605 |
| 60% | cubic_interpolation | 11.0021 | 13.0503 | -68.1359 | 605 | 605 |
| 60% | spline_interpolation | 11.0021 | 13.0503 | -68.1359 | 605 | 605 |
| 70% | knn_upgraded | 3.9330 | 4.7945 | -1.0048 | 706 | 706 |
| 70% | random_forest | 3.9432 | 4.8049 | -1.0188 | 706 | 706 |
| 70% | linear_interpolation | 3.9484 | 4.8092 | -1.0233 | 706 | 706 |
| 70% | time_interpolation | 3.9484 | 4.8092 | -1.0233 | 706 | 706 |
| 70% | knn | 3.9484 | 4.8092 | -1.0233 | 706 | 706 |
| 70% | neural_net | 3.9508 | 4.8138 | -1.0151 | 706 | 706 |
| 70% | decision_tree | 3.9613 | 4.8249 | -1.0372 | 706 | 706 |
| 70% | moving_average | 4.3156 | 5.1611 | -1.6078 | 706 | 706 |
| 70% | forward_fill | 4.3486 | 5.1866 | -1.6280 | 706 | 706 |
| 70% | adaptive_imputation | 4.3486 | 5.1866 | -1.6280 | 706 | 706 |
| 70% | cubic_interpolation | 19.5858 | 22.8486 | -99.0380 | 706 | 706 |
| 70% | spline_interpolation | 19.5858 | 22.8486 | -99.0380 | 706 | 706 |
| 80% | decision_tree | 3.6115 | 4.5303 | -0.4314 | 806 | 806 |
| 80% | random_forest | 3.6163 | 4.5367 | -0.4365 | 806 | 806 |
| 80% | knn_upgraded | 3.6241 | 4.5440 | -0.4431 | 806 | 806 |
| 80% | neural_net | 3.6280 | 4.5500 | -0.4427 | 806 | 806 |
| 80% | linear_interpolation | 3.6322 | 4.5532 | -0.4499 | 806 | 806 |
| 80% | time_interpolation | 3.6322 | 4.5532 | -0.4499 | 806 | 806 |
| 80% | knn | 3.6322 | 4.5532 | -0.4499 | 806 | 806 |
| 80% | moving_average | 5.4578 | 6.3559 | -1.9343 | 806 | 806 |
| 80% | forward_fill | 5.5145 | 6.4044 | -1.9761 | 806 | 806 |
| 80% | adaptive_imputation | 5.5145 | 6.4044 | -1.9761 | 806 | 806 |
| 80% | cubic_interpolation | 24.9233 | 28.5951 | -78.2922 | 806 | 806 |
| 80% | spline_interpolation | 24.9233 | 28.5951 | -78.2922 | 806 | 806 |

### Block u sredini — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 3.3713 | 3.6248 | 4.4178 | 3.4973 | 4.1161 | 4.0337 | 4.3486 | 5.5145 |
| linear_interpolation | 2.4936 | 2.4287 | 2.9642 | 3.3800 | 3.2633 | 3.2926 | 3.9484 | 3.6322 |
| time_interpolation | 2.4936 | 2.4287 | 2.9642 | 3.3800 | 3.2633 | 3.2926 | 3.9484 | 3.6322 |
| cubic_interpolation | 2.8902 | 7.0993 | 7.5157 | 9.2167 | 13.4306 | 11.0021 | 19.5858 | 24.9233 |
| spline_interpolation | 2.8902 | 7.0993 | 7.5157 | 9.2167 | 13.4306 | 11.0021 | 19.5858 | 24.9233 |
| knn | 2.4936 | 2.4287 | 2.9642 | 3.3800 | 3.2633 | 3.2926 | 3.9484 | 3.6322 |
| decision_tree | 2.5238 | 2.4272 | 2.9535 | 3.3739 | 3.2622 | 3.2947 | 3.9613 | 3.6115 |
| random_forest | 2.4939 | 2.4256 | 2.9625 | 3.3784 | 3.2658 | 3.3012 | 3.9432 | 3.6163 |

### Block u sredini — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 3.8757 | 4.3054 | 5.0875 | 4.1845 | 4.8768 | 4.7417 | 5.1866 | 6.4044 |
| linear_interpolation | 2.9240 | 3.0196 | 3.6305 | 4.0495 | 3.9330 | 4.0603 | 4.8092 | 4.5532 |
| time_interpolation | 2.9240 | 3.0196 | 3.6305 | 4.0495 | 3.9330 | 4.0603 | 4.8092 | 4.5532 |
| cubic_interpolation | 3.4244 | 8.4025 | 8.8354 | 11.0021 | 15.7456 | 13.0503 | 22.8486 | 28.5951 |
| spline_interpolation | 3.4244 | 8.4025 | 8.8354 | 11.0021 | 15.7456 | 13.0503 | 22.8486 | 28.5951 |
| knn | 2.9240 | 3.0196 | 3.6305 | 4.0495 | 3.9330 | 4.0603 | 4.8092 | 4.5532 |
| decision_tree | 2.9579 | 3.0207 | 3.6183 | 4.0479 | 3.9272 | 4.0635 | 4.8249 | 4.5303 |
| random_forest | 2.9248 | 3.0213 | 3.6329 | 4.0501 | 3.9344 | 4.0707 | 4.8049 | 4.5367 |

### Block u sredini — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -2.1698 | -2.1059 | -3.1045 | -1.0817 | -1.4949 | -1.3271 | -1.6280 | -1.9761 |
| linear_interpolation | -0.8101 | -0.3214 | -0.9238 | -1.0486 | -0.4140 | -0.4461 | -1.0233 | -0.4499 |
| time_interpolation | -0.8101 | -0.3214 | -0.9238 | -1.0486 | -0.4140 | -0.4461 | -1.0233 | -0.4499 |
| cubic_interpolation | -4.8049 | -17.1314 | -9.8463 | -14.7989 | -32.2616 | -68.1359 | -99.0380 | -78.2922 |
| spline_interpolation | -4.8049 | -17.1314 | -9.8463 | -14.7989 | -32.2616 | -68.1359 | -99.0380 | -78.2922 |
| knn | -0.8101 | -0.3214 | -0.9238 | -1.0486 | -0.4140 | -0.4461 | -1.0233 | -0.4499 |
| decision_tree | -0.8497 | -0.3236 | -0.9175 | -1.0437 | -0.4119 | -0.4516 | -1.0372 | -0.4314 |
| random_forest | -0.8009 | -0.3282 | -0.9174 | -1.0471 | -0.4174 | -0.4622 | -1.0188 | -0.4365 |

---

## Block na kraju (`block_end`)

### Block na kraju — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | knn_upgraded | 2.2315 | 2.7191 | -0.5752 | 101 | 101 |
| 10% | linear_interpolation | 2.2360 | 2.7231 | -0.5868 | 101 | 101 |
| 10% | time_interpolation | 2.2360 | 2.7231 | -0.5868 | 101 | 101 |
| 10% | knn | 2.2360 | 2.7231 | -0.5868 | 101 | 101 |
| 10% | adaptive_imputation | 2.2360 | 2.7231 | -0.5868 | 101 | 101 |
| 10% | neural_net | 2.2468 | 2.7399 | -0.5965 | 101 | 101 |
| 10% | random_forest | 2.2696 | 2.7117 | -0.4908 | 101 | 101 |
| 10% | decision_tree | 2.3154 | 2.7306 | -0.5348 | 101 | 101 |
| 10% | cubic_interpolation | 2.8200 | 3.3263 | -1.5008 | 101 | 101 |
| 10% | spline_interpolation | 3.3231 | 3.8600 | -2.9737 | 101 | 101 |
| 10% | moving_average | 3.3288 | 3.9310 | -2.4035 | 101 | 101 |
| 10% | forward_fill | 3.5266 | 4.0676 | -2.6489 | 101 | 101 |
| 20% | knn_upgraded | 2.5292 | 3.0747 | -0.3597 | 202 | 202 |
| 20% | linear_interpolation | 2.5602 | 3.0986 | -0.3547 | 202 | 202 |
| 20% | time_interpolation | 2.5602 | 3.0986 | -0.3547 | 202 | 202 |
| 20% | knn | 2.5602 | 3.0986 | -0.3547 | 202 | 202 |
| 20% | random_forest | 2.6628 | 3.1954 | -0.5103 | 202 | 202 |
| 20% | neural_net | 2.6860 | 3.2208 | -0.4458 | 202 | 202 |
| 20% | decision_tree | 2.7030 | 3.2443 | -0.5509 | 202 | 202 |
| 20% | moving_average | 2.9462 | 3.5482 | -0.7772 | 202 | 202 |
| 20% | forward_fill | 3.0373 | 3.6133 | -0.8494 | 202 | 202 |
| 20% | cubic_interpolation | 4.3268 | 5.3714 | -6.1576 | 202 | 202 |
| 20% | adaptive_imputation | 4.3268 | 5.3714 | -6.1576 | 202 | 202 |
| 20% | spline_interpolation | 5.6416 | 6.7526 | -11.7030 | 202 | 202 |
| 30% | linear_interpolation | 2.6552 | 3.2323 | -0.6430 | 302 | 302 |
| 30% | time_interpolation | 2.6552 | 3.2323 | -0.6430 | 302 | 302 |
| 30% | knn | 2.6552 | 3.2323 | -0.6430 | 302 | 302 |
| 30% | knn_upgraded | 2.6745 | 3.2643 | -0.6540 | 302 | 302 |
| 30% | random_forest | 2.7065 | 3.2981 | -0.6850 | 302 | 302 |
| 30% | neural_net | 2.7204 | 3.3156 | -0.6989 | 302 | 302 |
| 30% | decision_tree | 2.7768 | 3.3904 | -0.7531 | 302 | 302 |
| 30% | moving_average | 2.8771 | 3.5208 | -1.0345 | 302 | 302 |
| 30% | forward_fill | 2.9232 | 3.5516 | -1.0643 | 302 | 302 |
| 30% | cubic_interpolation | 4.9419 | 5.8202 | -7.9157 | 302 | 302 |
| 30% | spline_interpolation | 6.5507 | 7.4569 | -15.4252 | 302 | 302 |
| 30% | adaptive_imputation | 6.5507 | 7.4569 | -15.4252 | 302 | 302 |
| 40% | linear_interpolation | 2.8122 | 3.4494 | -0.3589 | 403 | 403 |
| 40% | time_interpolation | 2.8122 | 3.4494 | -0.3589 | 403 | 403 |
| 40% | knn | 2.8122 | 3.4494 | -0.3589 | 403 | 403 |
| 40% | adaptive_imputation | 2.8122 | 3.4494 | -0.3589 | 403 | 403 |
| 40% | knn_upgraded | 2.8247 | 3.4815 | -0.3984 | 403 | 403 |
| 40% | neural_net | 2.8351 | 3.4809 | -0.3946 | 403 | 403 |
| 40% | random_forest | 2.8842 | 3.5477 | -0.4615 | 403 | 403 |
| 40% | decision_tree | 2.9264 | 3.5781 | -0.5088 | 403 | 403 |
| 40% | moving_average | 3.2289 | 3.8735 | -0.8019 | 403 | 403 |
| 40% | forward_fill | 3.2711 | 3.9006 | -0.8295 | 403 | 403 |
| 40% | cubic_interpolation | 7.4638 | 8.9455 | -33.4697 | 403 | 403 |
| 40% | spline_interpolation | 10.2407 | 11.7425 | -64.7224 | 403 | 403 |
| 50% | knn_upgraded | 2.9683 | 3.7025 | -0.4941 | 504 | 504 |
| 50% | random_forest | 3.0636 | 3.7564 | -0.5528 | 504 | 504 |
| 50% | linear_interpolation | 3.0938 | 3.8936 | -0.6455 | 504 | 504 |
| 50% | time_interpolation | 3.0938 | 3.8936 | -0.6455 | 504 | 504 |
| 50% | knn | 3.0938 | 3.8936 | -0.6455 | 504 | 504 |
| 50% | adaptive_imputation | 3.0938 | 3.8936 | -0.6455 | 504 | 504 |
| 50% | neural_net | 3.1202 | 3.8948 | -0.6888 | 504 | 504 |
| 50% | decision_tree | 3.1401 | 3.8229 | -0.6210 | 504 | 504 |
| 50% | moving_average | 4.7041 | 5.5076 | -2.6225 | 504 | 504 |
| 50% | forward_fill | 4.7663 | 5.5476 | -2.6809 | 504 | 504 |
| 50% | cubic_interpolation | 7.8997 | 9.2728 | -13.8338 | 504 | 504 |
| 50% | spline_interpolation | 10.7038 | 12.1357 | -25.0044 | 504 | 504 |
| 60% | knn_upgraded | 3.1501 | 3.8980 | -0.5832 | 605 | 605 |
| 60% | random_forest | 3.1812 | 3.9082 | -0.5876 | 605 | 605 |
| 60% | decision_tree | 3.2171 | 3.9368 | -0.5818 | 605 | 605 |
| 60% | neural_net | 3.2511 | 4.0377 | -0.6972 | 605 | 605 |
| 60% | linear_interpolation | 3.2528 | 4.0267 | -0.7316 | 605 | 605 |
| 60% | time_interpolation | 3.2528 | 4.0267 | -0.7316 | 605 | 605 |
| 60% | knn | 3.2528 | 4.0267 | -0.7316 | 605 | 605 |
| 60% | adaptive_imputation | 3.2528 | 4.0267 | -0.7316 | 605 | 605 |
| 60% | moving_average | 4.7516 | 5.5839 | -2.4314 | 605 | 605 |
| 60% | forward_fill | 4.8022 | 5.6160 | -2.4665 | 605 | 605 |
| 60% | cubic_interpolation | 10.0488 | 11.9508 | -19.6469 | 605 | 605 |
| 60% | spline_interpolation | 14.6728 | 16.4953 | -40.1225 | 605 | 605 |
| 70% | linear_interpolation | 3.1762 | 3.9139 | -0.2615 | 706 | 706 |
| 70% | time_interpolation | 3.1762 | 3.9139 | -0.2615 | 706 | 706 |
| 70% | knn | 3.1762 | 3.9139 | -0.2615 | 706 | 706 |
| 70% | adaptive_imputation | 3.1762 | 3.9139 | -0.2615 | 706 | 706 |
| 70% | neural_net | 3.2612 | 4.0244 | -0.3267 | 706 | 706 |
| 70% | knn_upgraded | 3.2731 | 4.0449 | -0.3339 | 706 | 706 |
| 70% | random_forest | 3.3540 | 4.1190 | -0.3897 | 706 | 706 |
| 70% | decision_tree | 3.3991 | 4.1678 | -0.4089 | 706 | 706 |
| 70% | moving_average | 3.4882 | 4.3041 | -0.6110 | 706 | 706 |
| 70% | forward_fill | 3.5122 | 4.3200 | -0.6267 | 706 | 706 |
| 70% | cubic_interpolation | 23.8038 | 28.0182 | -124.5358 | 706 | 706 |
| 70% | spline_interpolation | 35.0891 | 39.0360 | -249.6283 | 706 | 706 |
| 80% | linear_interpolation | 3.2232 | 3.9508 | -0.2344 | 806 | 806 |
| 80% | time_interpolation | 3.2232 | 3.9508 | -0.2344 | 806 | 806 |
| 80% | knn | 3.2232 | 3.9508 | -0.2344 | 806 | 806 |
| 80% | random_forest | 3.2577 | 3.9994 | -0.2382 | 806 | 806 |
| 80% | knn_upgraded | 3.2579 | 4.0116 | -0.2404 | 806 | 806 |
| 80% | neural_net | 3.3167 | 4.0709 | -0.3276 | 806 | 806 |
| 80% | decision_tree | 3.4093 | 4.1680 | -0.3356 | 806 | 806 |
| 80% | moving_average | 4.3037 | 5.0727 | -1.2979 | 806 | 806 |
| 80% | forward_fill | 4.3384 | 5.0966 | -1.3228 | 806 | 806 |
| 80% | cubic_interpolation | 14.0329 | 16.5526 | -100.9549 | 806 | 806 |
| 80% | adaptive_imputation | 14.0329 | 16.5526 | -100.9549 | 806 | 806 |
| 80% | spline_interpolation | 19.9462 | 22.3597 | -196.8562 | 806 | 806 |

### Block na kraju — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 3.5266 | 3.0373 | 2.9232 | 3.2711 | 4.7663 | 4.8022 | 3.5122 | 4.3384 |
| linear_interpolation | 2.2360 | 2.5602 | 2.6552 | 2.8122 | 3.0938 | 3.2528 | 3.1762 | 3.2232 |
| time_interpolation | 2.2360 | 2.5602 | 2.6552 | 2.8122 | 3.0938 | 3.2528 | 3.1762 | 3.2232 |
| cubic_interpolation | 2.8200 | 4.3268 | 4.9419 | 7.4638 | 7.8997 | 10.0488 | 23.8038 | 14.0329 |
| spline_interpolation | 3.3231 | 5.6416 | 6.5507 | 10.2407 | 10.7038 | 14.6728 | 35.0891 | 19.9462 |
| knn | 2.2360 | 2.5602 | 2.6552 | 2.8122 | 3.0938 | 3.2528 | 3.1762 | 3.2232 |
| decision_tree | 2.3154 | 2.7030 | 2.7768 | 2.9264 | 3.1401 | 3.2171 | 3.3991 | 3.4093 |
| random_forest | 2.2696 | 2.6628 | 2.7065 | 2.8842 | 3.0636 | 3.1812 | 3.3540 | 3.2577 |

### Block na kraju — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 4.0676 | 3.6133 | 3.5516 | 3.9006 | 5.5476 | 5.6160 | 4.3200 | 5.0966 |
| linear_interpolation | 2.7231 | 3.0986 | 3.2323 | 3.4494 | 3.8936 | 4.0267 | 3.9139 | 3.9508 |
| time_interpolation | 2.7231 | 3.0986 | 3.2323 | 3.4494 | 3.8936 | 4.0267 | 3.9139 | 3.9508 |
| cubic_interpolation | 3.3263 | 5.3714 | 5.8202 | 8.9455 | 9.2728 | 11.9508 | 28.0182 | 16.5526 |
| spline_interpolation | 3.8600 | 6.7526 | 7.4569 | 11.7425 | 12.1357 | 16.4953 | 39.0360 | 22.3597 |
| knn | 2.7231 | 3.0986 | 3.2323 | 3.4494 | 3.8936 | 4.0267 | 3.9139 | 3.9508 |
| decision_tree | 2.7306 | 3.2443 | 3.3904 | 3.5781 | 3.8229 | 3.9368 | 4.1678 | 4.1680 |
| random_forest | 2.7117 | 3.1954 | 3.2981 | 3.5477 | 3.7564 | 3.9082 | 4.1190 | 3.9994 |

### Block na kraju — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -2.6489 | -0.8494 | -1.0643 | -0.8295 | -2.6809 | -2.4665 | -0.6267 | -1.3228 |
| linear_interpolation | -0.5868 | -0.3547 | -0.6430 | -0.3589 | -0.6455 | -0.7316 | -0.2615 | -0.2344 |
| time_interpolation | -0.5868 | -0.3547 | -0.6430 | -0.3589 | -0.6455 | -0.7316 | -0.2615 | -0.2344 |
| cubic_interpolation | -1.5008 | -6.1576 | -7.9157 | -33.4697 | -13.8338 | -19.6469 | -124.5358 | -100.9549 |
| spline_interpolation | -2.9737 | -11.7030 | -15.4252 | -64.7224 | -25.0044 | -40.1225 | -249.6283 | -196.8562 |
| knn | -0.5868 | -0.3547 | -0.6430 | -0.3589 | -0.6455 | -0.7316 | -0.2615 | -0.2344 |
| decision_tree | -0.5348 | -0.5509 | -0.7531 | -0.5088 | -0.6210 | -0.5818 | -0.4089 | -0.3356 |
| random_forest | -0.4908 | -0.5103 | -0.6850 | -0.4615 | -0.5528 | -0.5876 | -0.3897 | -0.2382 |

---

## Najbolja metoda po scenariju i missing rateu (po MAE)

| scenario | block_position | missing_rate | najbolja metoda | MAE | RMSE | R² |
|----------|----------------|--------------|-----------------|-----|------|-----|
| random | none | 10% | spline_interpolation | 0.0721 | 0.1114 | 0.9990 |
| random | none | 20% | spline_interpolation | 0.0821 | 0.1321 | 0.9985 |
| random | none | 30% | cubic_interpolation | 0.0923 | 0.1511 | 0.9981 |
| random | none | 40% | cubic_interpolation | 0.1055 | 0.1745 | 0.9974 |
| random | none | 50% | linear_interpolation | 0.1184 | 0.1850 | 0.9972 |
| random | none | 60% | linear_interpolation | 0.1381 | 0.2257 | 0.9957 |
| random | none | 70% | linear_interpolation | 0.1684 | 0.2747 | 0.9938 |
| random | none | 80% | linear_interpolation | 0.2116 | 0.3424 | 0.9902 |
| block | none | 10% | neural_net | 2.1311 | 2.5063 | -0.6337 |
| block | none | 20% | neural_net | 2.5198 | 3.1131 | -0.3658 |
| block | none | 30% | neural_net | 3.7507 | 4.4459 | -1.1276 |
| block | none | 40% | random_forest | 2.8163 | 3.5018 | -0.6697 |
| block | none | 50% | random_forest | 3.0882 | 3.8701 | -0.2135 |
| block | none | 60% | neural_net | 3.7285 | 4.5471 | -0.7923 |
| block | none | 70% | decision_tree | 3.7657 | 4.5868 | -1.1037 |
| block | none | 80% | decision_tree | 3.5502 | 4.4147 | -0.5277 |
| block_start | start | 10% | cubic_interpolation | 2.0883 | 2.4984 | -0.4797 |
| block_start | start | 20% | knn_upgraded | 2.7903 | 3.4767 | -0.4325 |
| block_start | start | 30% | linear_interpolation | 3.1027 | 3.8831 | -0.4297 |
| block_start | start | 40% | linear_interpolation | 3.1895 | 3.8872 | -0.5076 |
| block_start | start | 50% | linear_interpolation | 3.0703 | 3.8144 | -0.2076 |
| block_start | start | 60% | linear_interpolation | 3.5792 | 4.3585 | -0.5799 |
| block_start | start | 70% | linear_interpolation | 3.9971 | 4.8378 | -1.0472 |
| block_start | start | 80% | linear_interpolation | 3.6322 | 4.5405 | -0.5088 |
| block_middle | middle | 10% | knn_upgraded | 2.4864 | 2.9165 | -0.7950 |
| block_middle | middle | 20% | neural_net | 2.4173 | 3.0136 | -0.3261 |
| block_middle | middle | 30% | decision_tree | 2.9535 | 3.6183 | -0.9175 |
| block_middle | middle | 40% | neural_net | 3.3719 | 4.0516 | -1.0600 |
| block_middle | middle | 50% | knn_upgraded | 3.2569 | 3.9244 | -0.4088 |
| block_middle | middle | 60% | linear_interpolation | 3.2926 | 4.0603 | -0.4461 |
| block_middle | middle | 70% | knn_upgraded | 3.9330 | 4.7945 | -1.0048 |
| block_middle | middle | 80% | decision_tree | 3.6115 | 4.5303 | -0.4314 |
| block_end | end | 10% | knn_upgraded | 2.2315 | 2.7191 | -0.5752 |
| block_end | end | 20% | knn_upgraded | 2.5292 | 3.0747 | -0.3597 |
| block_end | end | 30% | linear_interpolation | 2.6552 | 3.2323 | -0.6430 |
| block_end | end | 40% | linear_interpolation | 2.8122 | 3.4494 | -0.3589 |
| block_end | end | 50% | knn_upgraded | 2.9683 | 3.7025 | -0.4941 |
| block_end | end | 60% | knn_upgraded | 3.1501 | 3.8980 | -0.5832 |
| block_end | end | 70% | linear_interpolation | 3.1762 | 3.9139 | -0.2615 |
| block_end | end | 80% | linear_interpolation | 3.2232 | 3.9508 | -0.2344 |