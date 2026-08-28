# Sve tablice rezultata — missing rate 10–80 %

*Izvor: `results/experiment_results.csv` (480 redaka)*
*Generirano: `python scripts/generate_results_tables.py`*

---

## KOMPLETNA TABLICA (svi scenariji, svi rateovi, sve metode)

| scenario | block_position | missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|----------|----------------|--------------|--------|-----|------|-----|---------|-----------|
| block | none | 10% | adaptive_imputation | 1.0285 | 1.1880 | -1.6311 | 101 | 101 |
| block | none | 10% | cubic_interpolation | 1.1604 | 1.3978 | -2.6421 | 101 | 101 |
| block | none | 10% | decision_tree | 1.0268 | 1.1854 | -1.6195 | 101 | 101 |
| block | none | 10% | forward_fill | 1.5435 | 1.7084 | -4.4409 | 101 | 101 |
| block | none | 10% | knn | 1.0285 | 1.1880 | -1.6311 | 101 | 101 |
| block | none | 10% | knn_upgraded | 1.0387 | 1.1966 | -1.6692 | 101 | 101 |
| block | none | 10% | linear_interpolation | 1.0285 | 1.1880 | -1.6311 | 101 | 101 |
| block | none | 10% | moving_average | 1.4884 | 1.6774 | -4.2453 | 101 | 101 |
| block | none | 10% | neural_net | 1.0249 | 1.1710 | -1.5564 | 101 | 101 |
| block | none | 10% | random_forest | 1.0145 | 1.1739 | -1.5687 | 101 | 101 |
| block | none | 10% | spline_interpolation | 1.1604 | 1.3978 | -2.6421 | 101 | 101 |
| block | none | 10% | time_interpolation | 1.0285 | 1.1880 | -1.6311 | 101 | 101 |
| block | none | 20% | adaptive_imputation | 1.4765 | 1.6968 | -2.6787 | 202 | 202 |
| block | none | 20% | cubic_interpolation | 4.2442 | 5.0983 | -32.2091 | 202 | 202 |
| block | none | 20% | decision_tree | 1.4761 | 1.6957 | -2.6736 | 202 | 202 |
| block | none | 20% | forward_fill | 1.6054 | 1.8330 | -3.2929 | 202 | 202 |
| block | none | 20% | knn | 1.4765 | 1.6968 | -2.6787 | 202 | 202 |
| block | none | 20% | knn_upgraded | 1.4877 | 1.7057 | -2.7171 | 202 | 202 |
| block | none | 20% | linear_interpolation | 1.4765 | 1.6968 | -2.6787 | 202 | 202 |
| block | none | 20% | moving_average | 1.5990 | 1.8308 | -3.2827 | 202 | 202 |
| block | none | 20% | neural_net | 1.4780 | 1.7466 | -2.8976 | 202 | 202 |
| block | none | 20% | random_forest | 1.4763 | 1.6961 | -2.6753 | 202 | 202 |
| block | none | 20% | spline_interpolation | 4.2442 | 5.0983 | -32.2091 | 202 | 202 |
| block | none | 20% | time_interpolation | 1.4765 | 1.6968 | -2.6787 | 202 | 202 |
| block | none | 30% | adaptive_imputation | 3.4286 | 4.0453 | 0.3980 | 302 | 302 |
| block | none | 30% | cubic_interpolation | 7.7599 | 9.5520 | -2.3562 | 302 | 302 |
| block | none | 30% | decision_tree | 3.5234 | 4.1382 | 0.3701 | 302 | 302 |
| block | none | 30% | forward_fill | 4.1018 | 6.5393 | -0.5729 | 302 | 302 |
| block | none | 30% | knn | 3.4286 | 4.0453 | 0.3980 | 302 | 302 |
| block | none | 30% | knn_upgraded | 3.4334 | 4.0528 | 0.3958 | 302 | 302 |
| block | none | 30% | linear_interpolation | 3.4286 | 4.0453 | 0.3980 | 302 | 302 |
| block | none | 30% | moving_average | 3.8178 | 6.1890 | -0.4090 | 302 | 302 |
| block | none | 30% | neural_net | 3.4236 | 4.0464 | 0.3977 | 302 | 302 |
| block | none | 30% | random_forest | 3.4364 | 4.0565 | 0.3947 | 302 | 302 |
| block | none | 30% | spline_interpolation | 7.7599 | 9.5520 | -2.3562 | 302 | 302 |
| block | none | 30% | time_interpolation | 3.4286 | 4.0453 | 0.3980 | 302 | 302 |
| block | none | 40% | adaptive_imputation | 2.9308 | 3.6053 | 0.7248 | 403 | 403 |
| block | none | 40% | cubic_interpolation | 27.7372 | 31.8543 | -20.4801 | 403 | 403 |
| block | none | 40% | decision_tree | 2.7163 | 3.3872 | 0.7571 | 403 | 403 |
| block | none | 40% | forward_fill | 7.3827 | 10.0695 | -1.1464 | 403 | 403 |
| block | none | 40% | knn | 2.9308 | 3.6053 | 0.7248 | 403 | 403 |
| block | none | 40% | knn_upgraded | 2.8677 | 3.5369 | 0.7352 | 403 | 403 |
| block | none | 40% | linear_interpolation | 2.9308 | 3.6053 | 0.7248 | 403 | 403 |
| block | none | 40% | moving_average | 7.0965 | 9.7645 | -1.0184 | 403 | 403 |
| block | none | 40% | neural_net | 2.7429 | 3.3750 | 0.7589 | 403 | 403 |
| block | none | 40% | random_forest | 2.7685 | 3.4427 | 0.7491 | 403 | 403 |
| block | none | 40% | spline_interpolation | 27.7372 | 31.8543 | -20.4801 | 403 | 403 |
| block | none | 40% | time_interpolation | 2.9308 | 3.6053 | 0.7248 | 403 | 403 |
| block | none | 50% | adaptive_imputation | 5.4362 | 7.0441 | 0.1425 | 504 | 504 |
| block | none | 50% | cubic_interpolation | 6.0174 | 7.4492 | 0.0410 | 504 | 504 |
| block | none | 50% | decision_tree | 5.3983 | 6.9366 | 0.1684 | 504 | 504 |
| block | none | 50% | forward_fill | 8.2467 | 10.9793 | -1.0833 | 504 | 504 |
| block | none | 50% | knn | 5.4362 | 7.0441 | 0.1425 | 504 | 504 |
| block | none | 50% | knn_upgraded | 5.4447 | 7.0452 | 0.1422 | 504 | 504 |
| block | none | 50% | linear_interpolation | 5.4362 | 7.0441 | 0.1425 | 504 | 504 |
| block | none | 50% | moving_average | 8.1601 | 10.9449 | -1.0703 | 504 | 504 |
| block | none | 50% | neural_net | 5.3664 | 6.9675 | 0.1610 | 504 | 504 |
| block | none | 50% | random_forest | 5.4200 | 6.9994 | 0.1533 | 504 | 504 |
| block | none | 50% | spline_interpolation | 6.0174 | 7.4492 | 0.0410 | 504 | 504 |
| block | none | 50% | time_interpolation | 5.4362 | 7.0441 | 0.1425 | 504 | 504 |
| block | none | 60% | adaptive_imputation | 5.3499 | 6.8720 | 0.1376 | 605 | 605 |
| block | none | 60% | cubic_interpolation | 12.8316 | 15.8642 | -3.5960 | 605 | 605 |
| block | none | 60% | decision_tree | 5.3601 | 6.9710 | 0.1126 | 605 | 605 |
| block | none | 60% | forward_fill | 6.7044 | 9.1770 | -0.5379 | 605 | 605 |
| block | none | 60% | knn | 5.3499 | 6.8720 | 0.1376 | 605 | 605 |
| block | none | 60% | knn_upgraded | 5.3496 | 6.8887 | 0.1334 | 605 | 605 |
| block | none | 60% | linear_interpolation | 5.3499 | 6.8720 | 0.1376 | 605 | 605 |
| block | none | 60% | moving_average | 6.6641 | 9.1634 | -0.5334 | 605 | 605 |
| block | none | 60% | neural_net | 5.1730 | 6.7561 | 0.1664 | 605 | 605 |
| block | none | 60% | random_forest | 5.3146 | 6.8543 | 0.1420 | 605 | 605 |
| block | none | 60% | spline_interpolation | 12.8316 | 15.8642 | -3.5960 | 605 | 605 |
| block | none | 60% | time_interpolation | 5.3499 | 6.8720 | 0.1376 | 605 | 605 |
| block | none | 70% | adaptive_imputation | 3.5043 | 4.8567 | -0.0586 | 706 | 706 |
| block | none | 70% | cubic_interpolation | 10.1423 | 11.1737 | -4.6034 | 706 | 706 |
| block | none | 70% | decision_tree | 5.6223 | 6.9391 | -1.1610 | 706 | 706 |
| block | none | 70% | forward_fill | 3.5043 | 4.8567 | -0.0586 | 706 | 706 |
| block | none | 70% | knn | 5.7381 | 7.0407 | -1.2248 | 706 | 706 |
| block | none | 70% | knn_upgraded | 5.6963 | 7.0022 | -1.2006 | 706 | 706 |
| block | none | 70% | linear_interpolation | 5.7381 | 7.0407 | -1.2248 | 706 | 706 |
| block | none | 70% | moving_average | 3.4009 | 4.7069 | 0.0057 | 706 | 706 |
| block | none | 70% | neural_net | 5.5727 | 6.8960 | -1.1343 | 706 | 706 |
| block | none | 70% | random_forest | 5.6928 | 7.0058 | -1.2028 | 706 | 706 |
| block | none | 70% | spline_interpolation | 10.1423 | 11.1737 | -4.6034 | 706 | 706 |
| block | none | 70% | time_interpolation | 5.7381 | 7.0407 | -1.2248 | 706 | 706 |
| block | none | 80% | adaptive_imputation | 4.7975 | 6.1094 | 0.1660 | 806 | 806 |
| block | none | 80% | cubic_interpolation | 22.9276 | 28.3087 | -16.9062 | 806 | 806 |
| block | none | 80% | decision_tree | 4.7976 | 6.1093 | 0.1660 | 806 | 806 |
| block | none | 80% | forward_fill | 5.3337 | 7.4566 | -0.2424 | 806 | 806 |
| block | none | 80% | knn | 4.7975 | 6.1094 | 0.1660 | 806 | 806 |
| block | none | 80% | knn_upgraded | 4.8028 | 6.1130 | 0.1650 | 806 | 806 |
| block | none | 80% | linear_interpolation | 4.7975 | 6.1094 | 0.1660 | 806 | 806 |
| block | none | 80% | moving_average | 5.3070 | 7.4487 | -0.2397 | 806 | 806 |
| block | none | 80% | neural_net | 4.7335 | 6.0506 | 0.1820 | 806 | 806 |
| block | none | 80% | random_forest | 4.7788 | 6.0769 | 0.1749 | 806 | 806 |
| block | none | 80% | spline_interpolation | 22.9276 | 28.3087 | -16.9062 | 806 | 806 |
| block | none | 80% | time_interpolation | 4.7975 | 6.1094 | 0.1660 | 806 | 806 |
| block_end | end | 10% | adaptive_imputation | 3.4473 | 4.1538 | 0.3437 | 101 | 101 |
| block_end | end | 10% | cubic_interpolation | 4.9709 | 5.9253 | -0.3356 | 101 | 101 |
| block_end | end | 10% | decision_tree | 2.6289 | 2.9110 | 0.6776 | 101 | 101 |
| block_end | end | 10% | forward_fill | 8.4606 | 9.7525 | -2.6181 | 101 | 101 |
| block_end | end | 10% | knn | 3.4473 | 4.1538 | 0.3437 | 101 | 101 |
| block_end | end | 10% | knn_upgraded | 3.4495 | 4.1576 | 0.3424 | 101 | 101 |
| block_end | end | 10% | linear_interpolation | 3.4473 | 4.1538 | 0.3437 | 101 | 101 |
| block_end | end | 10% | moving_average | 7.8220 | 9.3988 | -2.3604 | 101 | 101 |
| block_end | end | 10% | neural_net | 3.2624 | 4.0373 | 0.3800 | 101 | 101 |
| block_end | end | 10% | random_forest | 2.8922 | 3.3180 | 0.5812 | 101 | 101 |
| block_end | end | 10% | spline_interpolation | 5.2391 | 6.2332 | -0.4780 | 101 | 101 |
| block_end | end | 10% | time_interpolation | 3.4473 | 4.1538 | 0.3437 | 101 | 101 |
| block_end | end | 20% | adaptive_imputation | 4.1828 | 4.5838 | 0.2258 | 202 | 202 |
| block_end | end | 20% | cubic_interpolation | 4.1828 | 4.5838 | 0.2258 | 202 | 202 |
| block_end | end | 20% | decision_tree | 5.5309 | 6.6861 | -0.6472 | 202 | 202 |
| block_end | end | 20% | forward_fill | 5.5124 | 6.3678 | -0.4942 | 202 | 202 |
| block_end | end | 20% | knn | 5.5318 | 6.6875 | -0.6479 | 202 | 202 |
| block_end | end | 20% | knn_upgraded | 5.5862 | 6.7538 | -0.6807 | 202 | 202 |
| block_end | end | 20% | linear_interpolation | 5.5318 | 6.6875 | -0.6479 | 202 | 202 |
| block_end | end | 20% | moving_average | 5.4719 | 6.3617 | -0.4913 | 202 | 202 |
| block_end | end | 20% | neural_net | 5.5046 | 6.6913 | -0.6498 | 202 | 202 |
| block_end | end | 20% | random_forest | 5.5697 | 6.7857 | -0.6967 | 202 | 202 |
| block_end | end | 20% | spline_interpolation | 8.3969 | 8.9561 | -1.9556 | 202 | 202 |
| block_end | end | 20% | time_interpolation | 5.5318 | 6.6875 | -0.6479 | 202 | 202 |
| block_end | end | 30% | adaptive_imputation | 4.8486 | 5.9726 | -0.7742 | 302 | 302 |
| block_end | end | 30% | cubic_interpolation | 5.0029 | 6.1929 | -0.9075 | 302 | 302 |
| block_end | end | 30% | decision_tree | 5.3206 | 6.4961 | -1.0988 | 302 | 302 |
| block_end | end | 30% | forward_fill | 5.4791 | 6.6979 | -1.2312 | 302 | 302 |
| block_end | end | 30% | knn | 5.4043 | 6.5802 | -1.1535 | 302 | 302 |
| block_end | end | 30% | knn_upgraded | 5.3792 | 6.5632 | -1.1424 | 302 | 302 |
| block_end | end | 30% | linear_interpolation | 5.4043 | 6.5802 | -1.1535 | 302 | 302 |
| block_end | end | 30% | moving_average | 5.4775 | 6.6978 | -1.2312 | 302 | 302 |
| block_end | end | 30% | neural_net | 5.3996 | 6.5774 | -1.1517 | 302 | 302 |
| block_end | end | 30% | random_forest | 5.3325 | 6.5065 | -1.1055 | 302 | 302 |
| block_end | end | 30% | spline_interpolation | 4.8486 | 5.9726 | -0.7742 | 302 | 302 |
| block_end | end | 30% | time_interpolation | 5.4043 | 6.5802 | -1.1535 | 302 | 302 |
| block_end | end | 40% | adaptive_imputation | 6.8261 | 8.3215 | -0.8504 | 403 | 403 |
| block_end | end | 40% | cubic_interpolation | 9.5956 | 11.1944 | -2.3486 | 403 | 403 |
| block_end | end | 40% | decision_tree | 5.4621 | 6.6719 | -0.1895 | 403 | 403 |
| block_end | end | 40% | forward_fill | 11.0101 | 12.5944 | -3.2385 | 403 | 403 |
| block_end | end | 40% | knn | 6.8261 | 8.3215 | -0.8504 | 403 | 403 |
| block_end | end | 40% | knn_upgraded | 6.0592 | 7.5231 | -0.5124 | 403 | 403 |
| block_end | end | 40% | linear_interpolation | 6.8261 | 8.3215 | -0.8504 | 403 | 403 |
| block_end | end | 40% | moving_average | 10.8786 | 12.5466 | -3.2064 | 403 | 403 |
| block_end | end | 40% | neural_net | 6.6972 | 8.1089 | -0.7570 | 403 | 403 |
| block_end | end | 40% | random_forest | 5.5721 | 6.8514 | -0.2543 | 403 | 403 |
| block_end | end | 40% | spline_interpolation | 10.3644 | 12.1292 | -2.9312 | 403 | 403 |
| block_end | end | 40% | time_interpolation | 6.8261 | 8.3215 | -0.8504 | 403 | 403 |
| block_end | end | 50% | adaptive_imputation | 5.2375 | 7.0389 | 0.0246 | 504 | 504 |
| block_end | end | 50% | cubic_interpolation | 6.3027 | 8.2675 | -0.3457 | 504 | 504 |
| block_end | end | 50% | decision_tree | 4.8178 | 5.8106 | 0.3353 | 504 | 504 |
| block_end | end | 50% | forward_fill | 9.3483 | 11.7349 | -1.7111 | 504 | 504 |
| block_end | end | 50% | knn | 5.2375 | 7.0389 | 0.0246 | 504 | 504 |
| block_end | end | 50% | knn_upgraded | 4.9521 | 6.3431 | 0.2079 | 504 | 504 |
| block_end | end | 50% | linear_interpolation | 5.2375 | 7.0389 | 0.0246 | 504 | 504 |
| block_end | end | 50% | moving_average | 9.2358 | 11.6882 | -1.6896 | 504 | 504 |
| block_end | end | 50% | neural_net | 4.5343 | 6.1421 | 0.2573 | 504 | 504 |
| block_end | end | 50% | random_forest | 5.0979 | 6.2580 | 0.2290 | 504 | 504 |
| block_end | end | 50% | spline_interpolation | 6.4615 | 8.4590 | -0.4087 | 504 | 504 |
| block_end | end | 50% | time_interpolation | 5.2375 | 7.0389 | 0.0246 | 504 | 504 |
| block_end | end | 60% | adaptive_imputation | 4.9650 | 6.0693 | 0.3007 | 605 | 605 |
| block_end | end | 60% | cubic_interpolation | 8.1166 | 9.5544 | -0.7330 | 605 | 605 |
| block_end | end | 60% | decision_tree | 5.1470 | 5.8590 | 0.3483 | 605 | 605 |
| block_end | end | 60% | forward_fill | 6.8690 | 8.9755 | -0.5293 | 605 | 605 |
| block_end | end | 60% | knn | 4.9650 | 6.0693 | 0.3007 | 605 | 605 |
| block_end | end | 60% | knn_upgraded | 5.0400 | 5.8996 | 0.3392 | 605 | 605 |
| block_end | end | 60% | linear_interpolation | 4.9650 | 6.0693 | 0.3007 | 605 | 605 |
| block_end | end | 60% | moving_average | 6.8013 | 8.9486 | -0.5202 | 605 | 605 |
| block_end | end | 60% | neural_net | 5.0808 | 6.1411 | 0.2840 | 605 | 605 |
| block_end | end | 60% | random_forest | 5.0473 | 5.8173 | 0.3576 | 605 | 605 |
| block_end | end | 60% | spline_interpolation | 10.6070 | 12.5410 | -1.9857 | 605 | 605 |
| block_end | end | 60% | time_interpolation | 4.9650 | 6.0693 | 0.3007 | 605 | 605 |
| block_end | end | 70% | adaptive_imputation | 5.2253 | 6.0540 | 0.2256 | 706 | 706 |
| block_end | end | 70% | cubic_interpolation | 10.9486 | 13.3992 | -2.7937 | 706 | 706 |
| block_end | end | 70% | decision_tree | 5.4158 | 6.2233 | 0.1816 | 706 | 706 |
| block_end | end | 70% | forward_fill | 5.8994 | 7.2303 | -0.1047 | 706 | 706 |
| block_end | end | 70% | knn | 5.2253 | 6.0540 | 0.2256 | 706 | 706 |
| block_end | end | 70% | knn_upgraded | 5.3300 | 6.1250 | 0.2073 | 706 | 706 |
| block_end | end | 70% | linear_interpolation | 5.2253 | 6.0540 | 0.2256 | 706 | 706 |
| block_end | end | 70% | moving_average | 5.8638 | 7.2191 | -0.1012 | 706 | 706 |
| block_end | end | 70% | neural_net | 5.2308 | 6.0477 | 0.2272 | 706 | 706 |
| block_end | end | 70% | random_forest | 5.3365 | 6.1235 | 0.2077 | 706 | 706 |
| block_end | end | 70% | spline_interpolation | 13.5750 | 16.3927 | -4.6782 | 706 | 706 |
| block_end | end | 70% | time_interpolation | 5.2253 | 6.0540 | 0.2256 | 706 | 706 |
| block_end | end | 80% | adaptive_imputation | 4.0472 | 5.7523 | 0.2535 | 806 | 806 |
| block_end | end | 80% | cubic_interpolation | 4.0472 | 5.7523 | 0.2535 | 806 | 806 |
| block_end | end | 80% | decision_tree | 4.4766 | 5.4951 | 0.3188 | 806 | 806 |
| block_end | end | 80% | forward_fill | 5.5918 | 7.8095 | -0.3759 | 806 | 806 |
| block_end | end | 80% | knn | 4.4828 | 5.4898 | 0.3201 | 806 | 806 |
| block_end | end | 80% | knn_upgraded | 4.6598 | 5.5251 | 0.3113 | 806 | 806 |
| block_end | end | 80% | linear_interpolation | 4.4828 | 5.4898 | 0.3201 | 806 | 806 |
| block_end | end | 80% | moving_average | 5.5421 | 7.7871 | -0.3680 | 806 | 806 |
| block_end | end | 80% | neural_net | 4.3280 | 5.2041 | 0.3890 | 806 | 806 |
| block_end | end | 80% | random_forest | 4.6644 | 5.4900 | 0.3201 | 806 | 806 |
| block_end | end | 80% | spline_interpolation | 4.4920 | 6.4914 | 0.0494 | 806 | 806 |
| block_end | end | 80% | time_interpolation | 4.4828 | 5.4898 | 0.3201 | 806 | 806 |
| block_middle | middle | 10% | adaptive_imputation | 0.4913 | 0.5870 | -2.4255 | 101 | 101 |
| block_middle | middle | 10% | cubic_interpolation | 0.8615 | 1.0260 | -9.4641 | 101 | 101 |
| block_middle | middle | 10% | decision_tree | 0.4908 | 0.5865 | -2.4198 | 101 | 101 |
| block_middle | middle | 10% | forward_fill | 0.6767 | 0.7474 | -4.5524 | 101 | 101 |
| block_middle | middle | 10% | knn | 0.4913 | 0.5870 | -2.4255 | 101 | 101 |
| block_middle | middle | 10% | knn_upgraded | 0.4755 | 0.5717 | -2.2489 | 101 | 101 |
| block_middle | middle | 10% | linear_interpolation | 0.4913 | 0.5870 | -2.4255 | 101 | 101 |
| block_middle | middle | 10% | moving_average | 0.6685 | 0.7448 | -4.5139 | 101 | 101 |
| block_middle | middle | 10% | neural_net | 0.4786 | 0.5711 | -2.2422 | 101 | 101 |
| block_middle | middle | 10% | random_forest | 0.4707 | 0.5657 | -2.1814 | 101 | 101 |
| block_middle | middle | 10% | spline_interpolation | 0.8615 | 1.0260 | -9.4641 | 101 | 101 |
| block_middle | middle | 10% | time_interpolation | 0.4913 | 0.5870 | -2.4255 | 101 | 101 |
| block_middle | middle | 20% | adaptive_imputation | 1.1449 | 1.2988 | -2.6120 | 202 | 202 |
| block_middle | middle | 20% | cubic_interpolation | 1.3420 | 1.5821 | -4.3600 | 202 | 202 |
| block_middle | middle | 20% | decision_tree | 1.1447 | 1.2986 | -2.6109 | 202 | 202 |
| block_middle | middle | 20% | forward_fill | 2.1429 | 2.2442 | -9.7854 | 202 | 202 |
| block_middle | middle | 20% | knn | 1.1449 | 1.2988 | -2.6120 | 202 | 202 |
| block_middle | middle | 20% | knn_upgraded | 1.1405 | 1.2988 | -2.6122 | 202 | 202 |
| block_middle | middle | 20% | linear_interpolation | 1.1449 | 1.2988 | -2.6120 | 202 | 202 |
| block_middle | middle | 20% | moving_average | 2.0836 | 2.2178 | -9.5331 | 202 | 202 |
| block_middle | middle | 20% | neural_net | 1.1338 | 1.2839 | -2.5297 | 202 | 202 |
| block_middle | middle | 20% | random_forest | 1.1499 | 1.3042 | -2.6423 | 202 | 202 |
| block_middle | middle | 20% | spline_interpolation | 1.3420 | 1.5821 | -4.3600 | 202 | 202 |
| block_middle | middle | 20% | time_interpolation | 1.1449 | 1.2988 | -2.6120 | 202 | 202 |
| block_middle | middle | 30% | adaptive_imputation | 3.9194 | 4.8003 | -13.3868 | 302 | 302 |
| block_middle | middle | 30% | cubic_interpolation | 3.9194 | 4.8003 | -13.3868 | 302 | 302 |
| block_middle | middle | 30% | decision_tree | 4.0575 | 4.3019 | -10.5545 | 302 | 302 |
| block_middle | middle | 30% | forward_fill | 5.9705 | 6.1031 | -22.2562 | 302 | 302 |
| block_middle | middle | 30% | knn | 4.0555 | 4.3002 | -10.5455 | 302 | 302 |
| block_middle | middle | 30% | knn_upgraded | 4.0167 | 4.2671 | -10.3686 | 302 | 302 |
| block_middle | middle | 30% | linear_interpolation | 4.0555 | 4.3002 | -10.5455 | 302 | 302 |
| block_middle | middle | 30% | moving_average | 5.8994 | 6.0770 | -22.0575 | 302 | 302 |
| block_middle | middle | 30% | neural_net | 3.9762 | 4.2144 | -10.0895 | 302 | 302 |
| block_middle | middle | 30% | random_forest | 4.0302 | 4.2756 | -10.4139 | 302 | 302 |
| block_middle | middle | 30% | spline_interpolation | 3.9194 | 4.8003 | -13.3868 | 302 | 302 |
| block_middle | middle | 30% | time_interpolation | 4.0555 | 4.3002 | -10.5455 | 302 | 302 |
| block_middle | middle | 40% | adaptive_imputation | 5.3158 | 5.8442 | -3.8208 | 403 | 403 |
| block_middle | middle | 40% | cubic_interpolation | 9.9783 | 11.0953 | -16.3760 | 403 | 403 |
| block_middle | middle | 40% | decision_tree | 5.3155 | 5.8436 | -3.8198 | 403 | 403 |
| block_middle | middle | 40% | forward_fill | 3.6737 | 4.0426 | -1.3067 | 403 | 403 |
| block_middle | middle | 40% | knn | 5.3133 | 5.8414 | -3.8162 | 403 | 403 |
| block_middle | middle | 40% | knn_upgraded | 5.3101 | 5.8375 | -3.8098 | 403 | 403 |
| block_middle | middle | 40% | linear_interpolation | 5.3133 | 5.8414 | -3.8162 | 403 | 403 |
| block_middle | middle | 40% | moving_average | 3.6225 | 4.0178 | -1.2784 | 403 | 403 |
| block_middle | middle | 40% | neural_net | 5.2951 | 5.8182 | -3.7779 | 403 | 403 |
| block_middle | middle | 40% | random_forest | 5.3158 | 5.8442 | -3.8208 | 403 | 403 |
| block_middle | middle | 40% | spline_interpolation | 9.9783 | 11.0953 | -16.3760 | 403 | 403 |
| block_middle | middle | 40% | time_interpolation | 5.3133 | 5.8414 | -3.8162 | 403 | 403 |
| block_middle | middle | 50% | adaptive_imputation | 1.2192 | 1.7261 | 0.7966 | 504 | 504 |
| block_middle | middle | 50% | cubic_interpolation | 1.2192 | 1.7261 | 0.7966 | 504 | 504 |
| block_middle | middle | 50% | decision_tree | 5.4629 | 6.3873 | -1.7854 | 504 | 504 |
| block_middle | middle | 50% | forward_fill | 2.8546 | 4.1145 | -0.1558 | 504 | 504 |
| block_middle | middle | 50% | knn | 5.4614 | 6.3855 | -1.7838 | 504 | 504 |
| block_middle | middle | 50% | knn_upgraded | 5.4252 | 6.3499 | -1.7528 | 504 | 504 |
| block_middle | middle | 50% | linear_interpolation | 5.4614 | 6.3855 | -1.7838 | 504 | 504 |
| block_middle | middle | 50% | moving_average | 2.7176 | 3.8942 | -0.0353 | 504 | 504 |
| block_middle | middle | 50% | neural_net | 5.3664 | 6.2753 | -1.6885 | 504 | 504 |
| block_middle | middle | 50% | random_forest | 5.4537 | 6.3790 | -1.7781 | 504 | 504 |
| block_middle | middle | 50% | spline_interpolation | 1.2192 | 1.7261 | 0.7966 | 504 | 504 |
| block_middle | middle | 50% | time_interpolation | 5.4614 | 6.3855 | -1.7838 | 504 | 504 |
| block_middle | middle | 60% | adaptive_imputation | 3.3930 | 4.7624 | -0.0919 | 605 | 605 |
| block_middle | middle | 60% | cubic_interpolation | 4.3577 | 5.3804 | -0.3936 | 605 | 605 |
| block_middle | middle | 60% | decision_tree | 4.0806 | 4.7868 | -0.1030 | 605 | 605 |
| block_middle | middle | 60% | forward_fill | 3.3930 | 4.7624 | -0.0919 | 605 | 605 |
| block_middle | middle | 60% | knn | 4.0808 | 4.7870 | -0.1031 | 605 | 605 |
| block_middle | middle | 60% | knn_upgraded | 4.0750 | 4.7792 | -0.0995 | 605 | 605 |
| block_middle | middle | 60% | linear_interpolation | 4.0808 | 4.7870 | -0.1031 | 605 | 605 |
| block_middle | middle | 60% | moving_average | 3.3220 | 4.6986 | -0.0628 | 605 | 605 |
| block_middle | middle | 60% | neural_net | 4.0725 | 4.7950 | -0.1069 | 605 | 605 |
| block_middle | middle | 60% | random_forest | 4.0854 | 4.7926 | -0.1057 | 605 | 605 |
| block_middle | middle | 60% | spline_interpolation | 4.3577 | 5.3804 | -0.3936 | 605 | 605 |
| block_middle | middle | 60% | time_interpolation | 4.0808 | 4.7870 | -0.1031 | 605 | 605 |
| block_middle | middle | 70% | adaptive_imputation | 3.8792 | 5.4544 | -0.1006 | 706 | 706 |
| block_middle | middle | 70% | cubic_interpolation | 12.3579 | 13.6447 | -5.8872 | 706 | 706 |
| block_middle | middle | 70% | decision_tree | 6.7057 | 8.0111 | -1.3741 | 706 | 706 |
| block_middle | middle | 70% | forward_fill | 3.8792 | 5.4544 | -0.1006 | 706 | 706 |
| block_middle | middle | 70% | knn | 6.6070 | 7.9146 | -1.3173 | 706 | 706 |
| block_middle | middle | 70% | knn_upgraded | 6.5630 | 7.8732 | -1.2931 | 706 | 706 |
| block_middle | middle | 70% | linear_interpolation | 6.6070 | 7.9146 | -1.3173 | 706 | 706 |
| block_middle | middle | 70% | moving_average | 3.7491 | 5.2530 | -0.0208 | 706 | 706 |
| block_middle | middle | 70% | neural_net | 6.5101 | 7.8359 | -1.2714 | 706 | 706 |
| block_middle | middle | 70% | random_forest | 6.5847 | 7.8942 | -1.3054 | 706 | 706 |
| block_middle | middle | 70% | spline_interpolation | 12.3579 | 13.6447 | -5.8872 | 706 | 706 |
| block_middle | middle | 70% | time_interpolation | 6.6070 | 7.9146 | -1.3173 | 706 | 706 |
| block_middle | middle | 80% | adaptive_imputation | 4.6316 | 6.3931 | -0.0673 | 806 | 806 |
| block_middle | middle | 80% | cubic_interpolation | 7.6603 | 8.9431 | -1.0885 | 806 | 806 |
| block_middle | middle | 80% | decision_tree | 6.8578 | 8.2550 | -0.7795 | 806 | 806 |
| block_middle | middle | 80% | forward_fill | 4.6316 | 6.3931 | -0.0673 | 806 | 806 |
| block_middle | middle | 80% | knn | 6.8624 | 8.2591 | -0.7813 | 806 | 806 |
| block_middle | middle | 80% | knn_upgraded | 6.8409 | 8.2367 | -0.7716 | 806 | 806 |
| block_middle | middle | 80% | linear_interpolation | 6.8624 | 8.2591 | -0.7813 | 806 | 806 |
| block_middle | middle | 80% | moving_average | 4.5123 | 6.2311 | -0.0139 | 806 | 806 |
| block_middle | middle | 80% | neural_net | 6.9829 | 8.3910 | -0.8386 | 806 | 806 |
| block_middle | middle | 80% | random_forest | 6.8553 | 8.2505 | -0.7775 | 806 | 806 |
| block_middle | middle | 80% | spline_interpolation | 7.6603 | 8.9431 | -1.0885 | 806 | 806 |
| block_middle | middle | 80% | time_interpolation | 6.8624 | 8.2591 | -0.7813 | 806 | 806 |
| block_start | start | 10% | adaptive_imputation | 0.9636 | 1.2281 | 0.2477 | 101 | 101 |
| block_start | start | 10% | cubic_interpolation | 1.1022 | 1.2203 | 0.2573 | 101 | 101 |
| block_start | start | 10% | decision_tree | 0.7313 | 0.8856 | 0.6088 | 101 | 101 |
| block_start | start | 10% | forward_fill | 1.2386 | 1.4759 | -0.0865 | 101 | 101 |
| block_start | start | 10% | knn | 0.9636 | 1.2281 | 0.2477 | 101 | 101 |
| block_start | start | 10% | knn_upgraded | 0.9610 | 1.2179 | 0.2601 | 101 | 101 |
| block_start | start | 10% | linear_interpolation | 0.9636 | 1.2281 | 0.2477 | 101 | 101 |
| block_start | start | 10% | moving_average | 1.0817 | 1.3208 | 0.1299 | 101 | 101 |
| block_start | start | 10% | neural_net | 0.8793 | 1.0966 | 0.4002 | 101 | 101 |
| block_start | start | 10% | random_forest | 0.7752 | 0.9541 | 0.5459 | 101 | 101 |
| block_start | start | 10% | spline_interpolation | 1.0886 | 1.3436 | 0.0996 | 101 | 101 |
| block_start | start | 10% | time_interpolation | 0.9636 | 1.2281 | 0.2477 | 101 | 101 |
| block_start | start | 20% | adaptive_imputation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| block_start | start | 20% | cubic_interpolation | 1.6762 | 1.7713 | 0.0624 | 202 | 202 |
| block_start | start | 20% | decision_tree | 1.1276 | 1.2592 | 0.5262 | 202 | 202 |
| block_start | start | 20% | forward_fill | 2.3393 | 2.6579 | -1.1111 | 202 | 202 |
| block_start | start | 20% | knn | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| block_start | start | 20% | knn_upgraded | 0.8446 | 1.0182 | 0.6902 | 202 | 202 |
| block_start | start | 20% | linear_interpolation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| block_start | start | 20% | moving_average | 2.2213 | 2.5650 | -0.9661 | 202 | 202 |
| block_start | start | 20% | neural_net | 0.7237 | 0.8947 | 0.7608 | 202 | 202 |
| block_start | start | 20% | random_forest | 0.7880 | 0.9141 | 0.7503 | 202 | 202 |
| block_start | start | 20% | spline_interpolation | 2.1933 | 2.3259 | -0.6166 | 202 | 202 |
| block_start | start | 20% | time_interpolation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| block_start | start | 30% | adaptive_imputation | 1.9325 | 2.1842 | -0.2000 | 302 | 302 |
| block_start | start | 30% | cubic_interpolation | 5.8913 | 6.8477 | -10.7939 | 302 | 302 |
| block_start | start | 30% | decision_tree | 2.4442 | 2.7547 | -0.9087 | 302 | 302 |
| block_start | start | 30% | forward_fill | 3.0183 | 3.3915 | -1.8930 | 302 | 302 |
| block_start | start | 30% | knn | 2.1272 | 2.3947 | -0.4423 | 302 | 302 |
| block_start | start | 30% | knn_upgraded | 2.2903 | 2.5707 | -0.6622 | 302 | 302 |
| block_start | start | 30% | linear_interpolation | 2.1272 | 2.3947 | -0.4423 | 302 | 302 |
| block_start | start | 30% | moving_average | 2.9869 | 3.3823 | -1.8774 | 302 | 302 |
| block_start | start | 30% | neural_net | 2.2451 | 2.5608 | -0.6494 | 302 | 302 |
| block_start | start | 30% | random_forest | 2.3518 | 2.6547 | -0.7726 | 302 | 302 |
| block_start | start | 30% | spline_interpolation | 7.7047 | 8.7130 | -18.0946 | 302 | 302 |
| block_start | start | 30% | time_interpolation | 2.1272 | 2.3947 | -0.4423 | 302 | 302 |
| block_start | start | 40% | adaptive_imputation | 2.2722 | 2.5830 | -0.4165 | 403 | 403 |
| block_start | start | 40% | cubic_interpolation | 7.2939 | 8.5596 | -14.5553 | 403 | 403 |
| block_start | start | 40% | decision_tree | 2.2722 | 2.5830 | -0.4165 | 403 | 403 |
| block_start | start | 40% | forward_fill | 2.9323 | 3.3907 | -1.4409 | 403 | 403 |
| block_start | start | 40% | knn | 1.8038 | 2.1093 | 0.0554 | 403 | 403 |
| block_start | start | 40% | knn_upgraded | 2.0140 | 2.3052 | -0.1282 | 403 | 403 |
| block_start | start | 40% | linear_interpolation | 1.8038 | 2.1093 | 0.0554 | 403 | 403 |
| block_start | start | 40% | moving_average | 2.8713 | 3.3525 | -1.3863 | 403 | 403 |
| block_start | start | 40% | neural_net | 1.8528 | 2.1683 | 0.0019 | 403 | 403 |
| block_start | start | 40% | random_forest | 2.1198 | 2.4193 | -0.2427 | 403 | 403 |
| block_start | start | 40% | spline_interpolation | 10.6173 | 12.0995 | -30.0816 | 403 | 403 |
| block_start | start | 40% | time_interpolation | 1.8038 | 2.1093 | 0.0554 | 403 | 403 |
| block_start | start | 50% | adaptive_imputation | 1.4386 | 1.9513 | 0.3576 | 504 | 504 |
| block_start | start | 50% | cubic_interpolation | 1.4492 | 1.7988 | 0.4541 | 504 | 504 |
| block_start | start | 50% | decision_tree | 2.1973 | 2.4875 | -0.0438 | 504 | 504 |
| block_start | start | 50% | forward_fill | 3.5791 | 4.1150 | -1.8567 | 504 | 504 |
| block_start | start | 50% | knn | 1.4386 | 1.9513 | 0.3576 | 504 | 504 |
| block_start | start | 50% | knn_upgraded | 1.6976 | 2.0434 | 0.2956 | 504 | 504 |
| block_start | start | 50% | linear_interpolation | 1.4386 | 1.9513 | 0.3576 | 504 | 504 |
| block_start | start | 50% | moving_average | 3.4995 | 4.0461 | -1.7618 | 504 | 504 |
| block_start | start | 50% | neural_net | 1.3679 | 1.7544 | 0.4808 | 504 | 504 |
| block_start | start | 50% | random_forest | 1.8680 | 2.1857 | 0.1941 | 504 | 504 |
| block_start | start | 50% | spline_interpolation | 1.8363 | 2.2186 | 0.1696 | 504 | 504 |
| block_start | start | 50% | time_interpolation | 1.4386 | 1.9513 | 0.3576 | 504 | 504 |
| block_start | start | 60% | adaptive_imputation | 1.5243 | 1.8189 | 0.4898 | 605 | 605 |
| block_start | start | 60% | cubic_interpolation | 1.5243 | 1.8189 | 0.4898 | 605 | 605 |
| block_start | start | 60% | decision_tree | 2.6418 | 2.8869 | -0.2852 | 605 | 605 |
| block_start | start | 60% | forward_fill | 4.0896 | 4.6341 | -2.3116 | 605 | 605 |
| block_start | start | 60% | knn | 1.5972 | 1.8882 | 0.4502 | 605 | 605 |
| block_start | start | 60% | knn_upgraded | 2.1038 | 2.3440 | 0.1527 | 605 | 605 |
| block_start | start | 60% | linear_interpolation | 1.5972 | 1.8882 | 0.4502 | 605 | 605 |
| block_start | start | 60% | moving_average | 4.0279 | 4.5922 | -2.2521 | 605 | 605 |
| block_start | start | 60% | neural_net | 1.6366 | 1.9258 | 0.4281 | 605 | 605 |
| block_start | start | 60% | random_forest | 2.3232 | 2.5625 | -0.0126 | 605 | 605 |
| block_start | start | 60% | spline_interpolation | 1.6913 | 1.9643 | 0.4050 | 605 | 605 |
| block_start | start | 60% | time_interpolation | 1.5972 | 1.8882 | 0.4502 | 605 | 605 |
| block_start | start | 70% | adaptive_imputation | 3.5094 | 4.7387 | -2.3956 | 706 | 706 |
| block_start | start | 70% | cubic_interpolation | 3.5094 | 4.7387 | -2.3956 | 706 | 706 |
| block_start | start | 70% | decision_tree | 4.5831 | 5.2619 | -3.1869 | 706 | 706 |
| block_start | start | 70% | forward_fill | 3.9994 | 4.5389 | -2.1154 | 706 | 706 |
| block_start | start | 70% | knn | 5.1465 | 5.8430 | -4.1626 | 706 | 706 |
| block_start | start | 70% | knn_upgraded | 4.8318 | 5.5203 | -3.6081 | 706 | 706 |
| block_start | start | 70% | linear_interpolation | 5.1465 | 5.8430 | -4.1626 | 706 | 706 |
| block_start | start | 70% | moving_average | 3.9828 | 4.5339 | -2.1084 | 706 | 706 |
| block_start | start | 70% | neural_net | 5.0912 | 5.7983 | -4.0840 | 706 | 706 |
| block_start | start | 70% | random_forest | 4.6731 | 5.3597 | -3.3438 | 706 | 706 |
| block_start | start | 70% | spline_interpolation | 7.4183 | 8.8242 | -10.7748 | 706 | 706 |
| block_start | start | 70% | time_interpolation | 5.1465 | 5.8430 | -4.1626 | 706 | 706 |
| block_start | start | 80% | adaptive_imputation | 4.2559 | 4.7930 | -0.3835 | 806 | 806 |
| block_start | start | 80% | cubic_interpolation | 23.7657 | 27.8532 | -45.7205 | 806 | 806 |
| block_start | start | 80% | decision_tree | 4.5569 | 5.2906 | -0.6857 | 806 | 806 |
| block_start | start | 80% | forward_fill | 4.2559 | 4.7930 | -0.3835 | 806 | 806 |
| block_start | start | 80% | knn | 5.2599 | 6.0752 | -1.2227 | 806 | 806 |
| block_start | start | 80% | knn_upgraded | 4.8518 | 5.6160 | -0.8994 | 806 | 806 |
| block_start | start | 80% | linear_interpolation | 5.2599 | 6.0752 | -1.2227 | 806 | 806 |
| block_start | start | 80% | moving_average | 4.2301 | 4.7813 | -0.3767 | 806 | 806 |
| block_start | start | 80% | neural_net | 4.6294 | 5.4547 | -0.7919 | 806 | 806 |
| block_start | start | 80% | random_forest | 4.8662 | 5.6133 | -0.8976 | 806 | 806 |
| block_start | start | 80% | spline_interpolation | 32.9873 | 36.9107 | -81.0472 | 806 | 806 |
| block_start | start | 80% | time_interpolation | 5.2599 | 6.0752 | -1.2227 | 806 | 806 |
| random | none | 10% | adaptive_imputation | 0.0470 | 0.0828 | 0.9998 | 101 | 101 |
| random | none | 10% | cubic_interpolation | 0.0472 | 0.0829 | 0.9998 | 101 | 101 |
| random | none | 10% | decision_tree | 0.0761 | 0.1209 | 0.9996 | 101 | 101 |
| random | none | 10% | forward_fill | 0.1587 | 0.2867 | 0.9976 | 101 | 101 |
| random | none | 10% | knn | 0.0626 | 0.0983 | 0.9997 | 101 | 101 |
| random | none | 10% | knn_upgraded | 0.0696 | 0.1060 | 0.9997 | 101 | 101 |
| random | none | 10% | linear_interpolation | 0.0626 | 0.0983 | 0.9997 | 101 | 101 |
| random | none | 10% | moving_average | 0.1464 | 0.2212 | 0.9986 | 101 | 101 |
| random | none | 10% | neural_net | 0.0724 | 0.1175 | 0.9996 | 101 | 101 |
| random | none | 10% | random_forest | 0.0657 | 0.1051 | 0.9997 | 101 | 101 |
| random | none | 10% | spline_interpolation | 0.0470 | 0.0828 | 0.9998 | 101 | 101 |
| random | none | 10% | time_interpolation | 0.0626 | 0.0983 | 0.9997 | 101 | 101 |
| random | none | 20% | adaptive_imputation | 0.0635 | 0.1052 | 0.9997 | 202 | 202 |
| random | none | 20% | cubic_interpolation | 0.0635 | 0.1052 | 0.9997 | 202 | 202 |
| random | none | 20% | decision_tree | 0.0819 | 0.1334 | 0.9995 | 202 | 202 |
| random | none | 20% | forward_fill | 0.1635 | 0.2588 | 0.9982 | 202 | 202 |
| random | none | 20% | knn | 0.0730 | 0.1185 | 0.9996 | 202 | 202 |
| random | none | 20% | knn_upgraded | 0.0922 | 0.1464 | 0.9994 | 202 | 202 |
| random | none | 20% | linear_interpolation | 0.0730 | 0.1185 | 0.9996 | 202 | 202 |
| random | none | 20% | moving_average | 0.1796 | 0.2998 | 0.9976 | 202 | 202 |
| random | none | 20% | neural_net | 0.0871 | 0.1357 | 0.9995 | 202 | 202 |
| random | none | 20% | random_forest | 0.0782 | 0.1259 | 0.9996 | 202 | 202 |
| random | none | 20% | spline_interpolation | 0.0635 | 0.1052 | 0.9997 | 202 | 202 |
| random | none | 20% | time_interpolation | 0.0730 | 0.1185 | 0.9996 | 202 | 202 |
| random | none | 30% | adaptive_imputation | 0.0834 | 0.1401 | 0.9995 | 302 | 302 |
| random | none | 30% | cubic_interpolation | 0.0879 | 0.1789 | 0.9991 | 302 | 302 |
| random | none | 30% | decision_tree | 0.0930 | 0.1494 | 0.9994 | 302 | 302 |
| random | none | 30% | forward_fill | 0.1820 | 0.2989 | 0.9975 | 302 | 302 |
| random | none | 30% | knn | 0.0834 | 0.1401 | 0.9995 | 302 | 302 |
| random | none | 30% | knn_upgraded | 0.1015 | 0.1598 | 0.9993 | 302 | 302 |
| random | none | 30% | linear_interpolation | 0.0834 | 0.1401 | 0.9995 | 302 | 302 |
| random | none | 30% | moving_average | 0.1986 | 0.3207 | 0.9972 | 302 | 302 |
| random | none | 30% | neural_net | 0.0950 | 0.1524 | 0.9994 | 302 | 302 |
| random | none | 30% | random_forest | 0.0840 | 0.1368 | 0.9995 | 302 | 302 |
| random | none | 30% | spline_interpolation | 0.0879 | 0.1789 | 0.9991 | 302 | 302 |
| random | none | 30% | time_interpolation | 0.0834 | 0.1401 | 0.9995 | 302 | 302 |
| random | none | 40% | adaptive_imputation | 0.0908 | 0.1724 | 0.9992 | 403 | 403 |
| random | none | 40% | cubic_interpolation | 0.0909 | 0.1726 | 0.9992 | 403 | 403 |
| random | none | 40% | decision_tree | 0.1062 | 0.1822 | 0.9991 | 403 | 403 |
| random | none | 40% | forward_fill | 0.2157 | 0.3499 | 0.9966 | 403 | 403 |
| random | none | 40% | knn | 0.0950 | 0.1596 | 0.9993 | 403 | 403 |
| random | none | 40% | knn_upgraded | 0.1214 | 0.1867 | 0.9990 | 403 | 403 |
| random | none | 40% | linear_interpolation | 0.0950 | 0.1596 | 0.9993 | 403 | 403 |
| random | none | 40% | moving_average | 0.2038 | 0.3281 | 0.9970 | 403 | 403 |
| random | none | 40% | neural_net | 0.1238 | 0.1882 | 0.9990 | 403 | 403 |
| random | none | 40% | random_forest | 0.0938 | 0.1519 | 0.9994 | 403 | 403 |
| random | none | 40% | spline_interpolation | 0.0908 | 0.1724 | 0.9992 | 403 | 403 |
| random | none | 40% | time_interpolation | 0.0950 | 0.1596 | 0.9993 | 403 | 403 |
| random | none | 50% | adaptive_imputation | 0.0997 | 0.2109 | 0.9988 | 504 | 504 |
| random | none | 50% | cubic_interpolation | 0.0998 | 0.2110 | 0.9988 | 504 | 504 |
| random | none | 50% | decision_tree | 0.1266 | 0.2178 | 0.9987 | 504 | 504 |
| random | none | 50% | forward_fill | 0.2415 | 0.3979 | 0.9956 | 504 | 504 |
| random | none | 50% | knn | 0.1020 | 0.1809 | 0.9991 | 504 | 504 |
| random | none | 50% | knn_upgraded | 0.1364 | 0.2146 | 0.9987 | 504 | 504 |
| random | none | 50% | linear_interpolation | 0.1020 | 0.1809 | 0.9991 | 504 | 504 |
| random | none | 50% | moving_average | 0.2293 | 0.3686 | 0.9962 | 504 | 504 |
| random | none | 50% | neural_net | 0.1429 | 0.2385 | 0.9984 | 504 | 504 |
| random | none | 50% | random_forest | 0.1002 | 0.1650 | 0.9992 | 504 | 504 |
| random | none | 50% | spline_interpolation | 0.0997 | 0.2109 | 0.9988 | 504 | 504 |
| random | none | 50% | time_interpolation | 0.1020 | 0.1809 | 0.9991 | 504 | 504 |
| random | none | 60% | adaptive_imputation | 0.1230 | 0.2369 | 0.9985 | 605 | 605 |
| random | none | 60% | cubic_interpolation | 0.1230 | 0.2369 | 0.9985 | 605 | 605 |
| random | none | 60% | decision_tree | 0.1501 | 0.2654 | 0.9981 | 605 | 605 |
| random | none | 60% | forward_fill | 0.2741 | 0.4235 | 0.9951 | 605 | 605 |
| random | none | 60% | knn | 0.1276 | 0.2484 | 0.9983 | 605 | 605 |
| random | none | 60% | knn_upgraded | 0.1614 | 0.2741 | 0.9980 | 605 | 605 |
| random | none | 60% | linear_interpolation | 0.1276 | 0.2484 | 0.9983 | 605 | 605 |
| random | none | 60% | moving_average | 0.2323 | 0.3733 | 0.9962 | 605 | 605 |
| random | none | 60% | neural_net | 0.1754 | 0.2798 | 0.9979 | 605 | 605 |
| random | none | 60% | random_forest | 0.1291 | 0.2528 | 0.9983 | 605 | 605 |
| random | none | 60% | spline_interpolation | 0.1232 | 0.2371 | 0.9985 | 605 | 605 |
| random | none | 60% | time_interpolation | 0.1276 | 0.2484 | 0.9983 | 605 | 605 |
| random | none | 70% | adaptive_imputation | 0.1774 | 0.3320 | 0.9971 | 706 | 706 |
| random | none | 70% | cubic_interpolation | 0.2138 | 0.4691 | 0.9941 | 706 | 706 |
| random | none | 70% | decision_tree | 0.2095 | 0.3992 | 0.9958 | 706 | 706 |
| random | none | 70% | forward_fill | 0.4076 | 0.7183 | 0.9863 | 706 | 706 |
| random | none | 70% | knn | 0.1774 | 0.3320 | 0.9971 | 706 | 706 |
| random | none | 70% | knn_upgraded | 0.2082 | 0.3630 | 0.9965 | 706 | 706 |
| random | none | 70% | linear_interpolation | 0.1774 | 0.3320 | 0.9971 | 706 | 706 |
| random | none | 70% | moving_average | 0.2955 | 0.5134 | 0.9930 | 706 | 706 |
| random | none | 70% | neural_net | 0.2181 | 0.3737 | 0.9963 | 706 | 706 |
| random | none | 70% | random_forest | 0.1904 | 0.3628 | 0.9965 | 706 | 706 |
| random | none | 70% | spline_interpolation | 0.2140 | 0.4692 | 0.9941 | 706 | 706 |
| random | none | 70% | time_interpolation | 0.1774 | 0.3320 | 0.9971 | 706 | 706 |
| random | none | 80% | adaptive_imputation | 0.1785 | 0.3145 | 0.9974 | 806 | 806 |
| random | none | 80% | cubic_interpolation | 0.1939 | 0.3446 | 0.9968 | 806 | 806 |
| random | none | 80% | decision_tree | 0.2368 | 0.3748 | 0.9962 | 806 | 806 |
| random | none | 80% | forward_fill | 0.5416 | 0.9838 | 0.9741 | 806 | 806 |
| random | none | 80% | knn | 0.1785 | 0.3145 | 0.9974 | 806 | 806 |
| random | none | 80% | knn_upgraded | 0.2013 | 0.3327 | 0.9970 | 806 | 806 |
| random | none | 80% | linear_interpolation | 0.1785 | 0.3145 | 0.9974 | 806 | 806 |
| random | none | 80% | moving_average | 0.3528 | 0.6606 | 0.9883 | 806 | 806 |
| random | none | 80% | neural_net | 0.2531 | 0.3886 | 0.9960 | 806 | 806 |
| random | none | 80% | random_forest | 0.1829 | 0.3146 | 0.9974 | 806 | 806 |
| random | none | 80% | spline_interpolation | 0.1936 | 0.3443 | 0.9968 | 806 | 806 |
| random | none | 80% | time_interpolation | 0.1785 | 0.3145 | 0.9974 | 806 | 806 |

---

## Random missing (`random`)

### Random missing — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | spline_interpolation | 0.0470 | 0.0828 | 0.9998 | 101 | 101 |
| 10% | adaptive_imputation | 0.0470 | 0.0828 | 0.9998 | 101 | 101 |
| 10% | cubic_interpolation | 0.0472 | 0.0829 | 0.9998 | 101 | 101 |
| 10% | linear_interpolation | 0.0626 | 0.0983 | 0.9997 | 101 | 101 |
| 10% | time_interpolation | 0.0626 | 0.0983 | 0.9997 | 101 | 101 |
| 10% | knn | 0.0626 | 0.0983 | 0.9997 | 101 | 101 |
| 10% | random_forest | 0.0657 | 0.1051 | 0.9997 | 101 | 101 |
| 10% | knn_upgraded | 0.0696 | 0.1060 | 0.9997 | 101 | 101 |
| 10% | neural_net | 0.0724 | 0.1175 | 0.9996 | 101 | 101 |
| 10% | decision_tree | 0.0761 | 0.1209 | 0.9996 | 101 | 101 |
| 10% | moving_average | 0.1464 | 0.2212 | 0.9986 | 101 | 101 |
| 10% | forward_fill | 0.1587 | 0.2867 | 0.9976 | 101 | 101 |
| 20% | spline_interpolation | 0.0635 | 0.1052 | 0.9997 | 202 | 202 |
| 20% | adaptive_imputation | 0.0635 | 0.1052 | 0.9997 | 202 | 202 |
| 20% | cubic_interpolation | 0.0635 | 0.1052 | 0.9997 | 202 | 202 |
| 20% | linear_interpolation | 0.0730 | 0.1185 | 0.9996 | 202 | 202 |
| 20% | time_interpolation | 0.0730 | 0.1185 | 0.9996 | 202 | 202 |
| 20% | knn | 0.0730 | 0.1185 | 0.9996 | 202 | 202 |
| 20% | random_forest | 0.0782 | 0.1259 | 0.9996 | 202 | 202 |
| 20% | decision_tree | 0.0819 | 0.1334 | 0.9995 | 202 | 202 |
| 20% | neural_net | 0.0871 | 0.1357 | 0.9995 | 202 | 202 |
| 20% | knn_upgraded | 0.0922 | 0.1464 | 0.9994 | 202 | 202 |
| 20% | forward_fill | 0.1635 | 0.2588 | 0.9982 | 202 | 202 |
| 20% | moving_average | 0.1796 | 0.2998 | 0.9976 | 202 | 202 |
| 30% | linear_interpolation | 0.0834 | 0.1401 | 0.9995 | 302 | 302 |
| 30% | time_interpolation | 0.0834 | 0.1401 | 0.9995 | 302 | 302 |
| 30% | knn | 0.0834 | 0.1401 | 0.9995 | 302 | 302 |
| 30% | adaptive_imputation | 0.0834 | 0.1401 | 0.9995 | 302 | 302 |
| 30% | random_forest | 0.0840 | 0.1368 | 0.9995 | 302 | 302 |
| 30% | spline_interpolation | 0.0879 | 0.1789 | 0.9991 | 302 | 302 |
| 30% | cubic_interpolation | 0.0879 | 0.1789 | 0.9991 | 302 | 302 |
| 30% | decision_tree | 0.0930 | 0.1494 | 0.9994 | 302 | 302 |
| 30% | neural_net | 0.0950 | 0.1524 | 0.9994 | 302 | 302 |
| 30% | knn_upgraded | 0.1015 | 0.1598 | 0.9993 | 302 | 302 |
| 30% | forward_fill | 0.1820 | 0.2989 | 0.9975 | 302 | 302 |
| 30% | moving_average | 0.1986 | 0.3207 | 0.9972 | 302 | 302 |
| 40% | spline_interpolation | 0.0908 | 0.1724 | 0.9992 | 403 | 403 |
| 40% | adaptive_imputation | 0.0908 | 0.1724 | 0.9992 | 403 | 403 |
| 40% | cubic_interpolation | 0.0909 | 0.1726 | 0.9992 | 403 | 403 |
| 40% | random_forest | 0.0938 | 0.1519 | 0.9994 | 403 | 403 |
| 40% | linear_interpolation | 0.0950 | 0.1596 | 0.9993 | 403 | 403 |
| 40% | time_interpolation | 0.0950 | 0.1596 | 0.9993 | 403 | 403 |
| 40% | knn | 0.0950 | 0.1596 | 0.9993 | 403 | 403 |
| 40% | decision_tree | 0.1062 | 0.1822 | 0.9991 | 403 | 403 |
| 40% | knn_upgraded | 0.1214 | 0.1867 | 0.9990 | 403 | 403 |
| 40% | neural_net | 0.1238 | 0.1882 | 0.9990 | 403 | 403 |
| 40% | moving_average | 0.2038 | 0.3281 | 0.9970 | 403 | 403 |
| 40% | forward_fill | 0.2157 | 0.3499 | 0.9966 | 403 | 403 |
| 50% | spline_interpolation | 0.0997 | 0.2109 | 0.9988 | 504 | 504 |
| 50% | adaptive_imputation | 0.0997 | 0.2109 | 0.9988 | 504 | 504 |
| 50% | cubic_interpolation | 0.0998 | 0.2110 | 0.9988 | 504 | 504 |
| 50% | random_forest | 0.1002 | 0.1650 | 0.9992 | 504 | 504 |
| 50% | linear_interpolation | 0.1020 | 0.1809 | 0.9991 | 504 | 504 |
| 50% | time_interpolation | 0.1020 | 0.1809 | 0.9991 | 504 | 504 |
| 50% | knn | 0.1020 | 0.1809 | 0.9991 | 504 | 504 |
| 50% | decision_tree | 0.1266 | 0.2178 | 0.9987 | 504 | 504 |
| 50% | knn_upgraded | 0.1364 | 0.2146 | 0.9987 | 504 | 504 |
| 50% | neural_net | 0.1429 | 0.2385 | 0.9984 | 504 | 504 |
| 50% | moving_average | 0.2293 | 0.3686 | 0.9962 | 504 | 504 |
| 50% | forward_fill | 0.2415 | 0.3979 | 0.9956 | 504 | 504 |
| 60% | cubic_interpolation | 0.1230 | 0.2369 | 0.9985 | 605 | 605 |
| 60% | adaptive_imputation | 0.1230 | 0.2369 | 0.9985 | 605 | 605 |
| 60% | spline_interpolation | 0.1232 | 0.2371 | 0.9985 | 605 | 605 |
| 60% | linear_interpolation | 0.1276 | 0.2484 | 0.9983 | 605 | 605 |
| 60% | time_interpolation | 0.1276 | 0.2484 | 0.9983 | 605 | 605 |
| 60% | knn | 0.1276 | 0.2484 | 0.9983 | 605 | 605 |
| 60% | random_forest | 0.1291 | 0.2528 | 0.9983 | 605 | 605 |
| 60% | decision_tree | 0.1501 | 0.2654 | 0.9981 | 605 | 605 |
| 60% | knn_upgraded | 0.1614 | 0.2741 | 0.9980 | 605 | 605 |
| 60% | neural_net | 0.1754 | 0.2798 | 0.9979 | 605 | 605 |
| 60% | moving_average | 0.2323 | 0.3733 | 0.9962 | 605 | 605 |
| 60% | forward_fill | 0.2741 | 0.4235 | 0.9951 | 605 | 605 |
| 70% | linear_interpolation | 0.1774 | 0.3320 | 0.9971 | 706 | 706 |
| 70% | time_interpolation | 0.1774 | 0.3320 | 0.9971 | 706 | 706 |
| 70% | knn | 0.1774 | 0.3320 | 0.9971 | 706 | 706 |
| 70% | adaptive_imputation | 0.1774 | 0.3320 | 0.9971 | 706 | 706 |
| 70% | random_forest | 0.1904 | 0.3628 | 0.9965 | 706 | 706 |
| 70% | knn_upgraded | 0.2082 | 0.3630 | 0.9965 | 706 | 706 |
| 70% | decision_tree | 0.2095 | 0.3992 | 0.9958 | 706 | 706 |
| 70% | cubic_interpolation | 0.2138 | 0.4691 | 0.9941 | 706 | 706 |
| 70% | spline_interpolation | 0.2140 | 0.4692 | 0.9941 | 706 | 706 |
| 70% | neural_net | 0.2181 | 0.3737 | 0.9963 | 706 | 706 |
| 70% | moving_average | 0.2955 | 0.5134 | 0.9930 | 706 | 706 |
| 70% | forward_fill | 0.4076 | 0.7183 | 0.9863 | 706 | 706 |
| 80% | linear_interpolation | 0.1785 | 0.3145 | 0.9974 | 806 | 806 |
| 80% | time_interpolation | 0.1785 | 0.3145 | 0.9974 | 806 | 806 |
| 80% | knn | 0.1785 | 0.3145 | 0.9974 | 806 | 806 |
| 80% | adaptive_imputation | 0.1785 | 0.3145 | 0.9974 | 806 | 806 |
| 80% | random_forest | 0.1829 | 0.3146 | 0.9974 | 806 | 806 |
| 80% | spline_interpolation | 0.1936 | 0.3443 | 0.9968 | 806 | 806 |
| 80% | cubic_interpolation | 0.1939 | 0.3446 | 0.9968 | 806 | 806 |
| 80% | knn_upgraded | 0.2013 | 0.3327 | 0.9970 | 806 | 806 |
| 80% | decision_tree | 0.2368 | 0.3748 | 0.9962 | 806 | 806 |
| 80% | neural_net | 0.2531 | 0.3886 | 0.9960 | 806 | 806 |
| 80% | moving_average | 0.3528 | 0.6606 | 0.9883 | 806 | 806 |
| 80% | forward_fill | 0.5416 | 0.9838 | 0.9741 | 806 | 806 |

### Random missing — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.1587 | 0.1635 | 0.1820 | 0.2157 | 0.2415 | 0.2741 | 0.4076 | 0.5416 |
| linear_interpolation | 0.0626 | 0.0730 | 0.0834 | 0.0950 | 0.1020 | 0.1276 | 0.1774 | 0.1785 |
| time_interpolation | 0.0626 | 0.0730 | 0.0834 | 0.0950 | 0.1020 | 0.1276 | 0.1774 | 0.1785 |
| cubic_interpolation | 0.0472 | 0.0635 | 0.0879 | 0.0909 | 0.0998 | 0.1230 | 0.2138 | 0.1939 |
| spline_interpolation | 0.0470 | 0.0635 | 0.0879 | 0.0908 | 0.0997 | 0.1232 | 0.2140 | 0.1936 |
| knn | 0.0626 | 0.0730 | 0.0834 | 0.0950 | 0.1020 | 0.1276 | 0.1774 | 0.1785 |
| decision_tree | 0.0761 | 0.0819 | 0.0930 | 0.1062 | 0.1266 | 0.1501 | 0.2095 | 0.2368 |
| random_forest | 0.0657 | 0.0782 | 0.0840 | 0.0938 | 0.1002 | 0.1291 | 0.1904 | 0.1829 |

### Random missing — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.2867 | 0.2588 | 0.2989 | 0.3499 | 0.3979 | 0.4235 | 0.7183 | 0.9838 |
| linear_interpolation | 0.0983 | 0.1185 | 0.1401 | 0.1596 | 0.1809 | 0.2484 | 0.3320 | 0.3145 |
| time_interpolation | 0.0983 | 0.1185 | 0.1401 | 0.1596 | 0.1809 | 0.2484 | 0.3320 | 0.3145 |
| cubic_interpolation | 0.0829 | 0.1052 | 0.1789 | 0.1726 | 0.2110 | 0.2369 | 0.4691 | 0.3446 |
| spline_interpolation | 0.0828 | 0.1052 | 0.1789 | 0.1724 | 0.2109 | 0.2371 | 0.4692 | 0.3443 |
| knn | 0.0983 | 0.1185 | 0.1401 | 0.1596 | 0.1809 | 0.2484 | 0.3320 | 0.3145 |
| decision_tree | 0.1209 | 0.1334 | 0.1494 | 0.1822 | 0.2178 | 0.2654 | 0.3992 | 0.3748 |
| random_forest | 0.1051 | 0.1259 | 0.1368 | 0.1519 | 0.1650 | 0.2528 | 0.3628 | 0.3146 |

### Random missing — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.9976 | 0.9982 | 0.9975 | 0.9966 | 0.9956 | 0.9951 | 0.9863 | 0.9741 |
| linear_interpolation | 0.9997 | 0.9996 | 0.9995 | 0.9993 | 0.9991 | 0.9983 | 0.9971 | 0.9974 |
| time_interpolation | 0.9997 | 0.9996 | 0.9995 | 0.9993 | 0.9991 | 0.9983 | 0.9971 | 0.9974 |
| cubic_interpolation | 0.9998 | 0.9997 | 0.9991 | 0.9992 | 0.9988 | 0.9985 | 0.9941 | 0.9968 |
| spline_interpolation | 0.9998 | 0.9997 | 0.9991 | 0.9992 | 0.9988 | 0.9985 | 0.9941 | 0.9968 |
| knn | 0.9997 | 0.9996 | 0.9995 | 0.9993 | 0.9991 | 0.9983 | 0.9971 | 0.9974 |
| decision_tree | 0.9996 | 0.9995 | 0.9994 | 0.9991 | 0.9987 | 0.9981 | 0.9958 | 0.9962 |
| random_forest | 0.9997 | 0.9996 | 0.9995 | 0.9994 | 0.9992 | 0.9983 | 0.9965 | 0.9974 |

---

## Block missing (`block`)

### Block missing — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | random_forest | 1.0145 | 1.1739 | -1.5687 | 101 | 101 |
| 10% | neural_net | 1.0249 | 1.1710 | -1.5564 | 101 | 101 |
| 10% | decision_tree | 1.0268 | 1.1854 | -1.6195 | 101 | 101 |
| 10% | linear_interpolation | 1.0285 | 1.1880 | -1.6311 | 101 | 101 |
| 10% | time_interpolation | 1.0285 | 1.1880 | -1.6311 | 101 | 101 |
| 10% | knn | 1.0285 | 1.1880 | -1.6311 | 101 | 101 |
| 10% | adaptive_imputation | 1.0285 | 1.1880 | -1.6311 | 101 | 101 |
| 10% | knn_upgraded | 1.0387 | 1.1966 | -1.6692 | 101 | 101 |
| 10% | cubic_interpolation | 1.1604 | 1.3978 | -2.6421 | 101 | 101 |
| 10% | spline_interpolation | 1.1604 | 1.3978 | -2.6421 | 101 | 101 |
| 10% | moving_average | 1.4884 | 1.6774 | -4.2453 | 101 | 101 |
| 10% | forward_fill | 1.5435 | 1.7084 | -4.4409 | 101 | 101 |
| 20% | decision_tree | 1.4761 | 1.6957 | -2.6736 | 202 | 202 |
| 20% | random_forest | 1.4763 | 1.6961 | -2.6753 | 202 | 202 |
| 20% | linear_interpolation | 1.4765 | 1.6968 | -2.6787 | 202 | 202 |
| 20% | time_interpolation | 1.4765 | 1.6968 | -2.6787 | 202 | 202 |
| 20% | knn | 1.4765 | 1.6968 | -2.6787 | 202 | 202 |
| 20% | adaptive_imputation | 1.4765 | 1.6968 | -2.6787 | 202 | 202 |
| 20% | neural_net | 1.4780 | 1.7466 | -2.8976 | 202 | 202 |
| 20% | knn_upgraded | 1.4877 | 1.7057 | -2.7171 | 202 | 202 |
| 20% | moving_average | 1.5990 | 1.8308 | -3.2827 | 202 | 202 |
| 20% | forward_fill | 1.6054 | 1.8330 | -3.2929 | 202 | 202 |
| 20% | cubic_interpolation | 4.2442 | 5.0983 | -32.2091 | 202 | 202 |
| 20% | spline_interpolation | 4.2442 | 5.0983 | -32.2091 | 202 | 202 |
| 30% | neural_net | 3.4236 | 4.0464 | 0.3977 | 302 | 302 |
| 30% | linear_interpolation | 3.4286 | 4.0453 | 0.3980 | 302 | 302 |
| 30% | time_interpolation | 3.4286 | 4.0453 | 0.3980 | 302 | 302 |
| 30% | knn | 3.4286 | 4.0453 | 0.3980 | 302 | 302 |
| 30% | adaptive_imputation | 3.4286 | 4.0453 | 0.3980 | 302 | 302 |
| 30% | knn_upgraded | 3.4334 | 4.0528 | 0.3958 | 302 | 302 |
| 30% | random_forest | 3.4364 | 4.0565 | 0.3947 | 302 | 302 |
| 30% | decision_tree | 3.5234 | 4.1382 | 0.3701 | 302 | 302 |
| 30% | moving_average | 3.8178 | 6.1890 | -0.4090 | 302 | 302 |
| 30% | forward_fill | 4.1018 | 6.5393 | -0.5729 | 302 | 302 |
| 30% | cubic_interpolation | 7.7599 | 9.5520 | -2.3562 | 302 | 302 |
| 30% | spline_interpolation | 7.7599 | 9.5520 | -2.3562 | 302 | 302 |
| 40% | decision_tree | 2.7163 | 3.3872 | 0.7571 | 403 | 403 |
| 40% | neural_net | 2.7429 | 3.3750 | 0.7589 | 403 | 403 |
| 40% | random_forest | 2.7685 | 3.4427 | 0.7491 | 403 | 403 |
| 40% | knn_upgraded | 2.8677 | 3.5369 | 0.7352 | 403 | 403 |
| 40% | linear_interpolation | 2.9308 | 3.6053 | 0.7248 | 403 | 403 |
| 40% | time_interpolation | 2.9308 | 3.6053 | 0.7248 | 403 | 403 |
| 40% | knn | 2.9308 | 3.6053 | 0.7248 | 403 | 403 |
| 40% | adaptive_imputation | 2.9308 | 3.6053 | 0.7248 | 403 | 403 |
| 40% | moving_average | 7.0965 | 9.7645 | -1.0184 | 403 | 403 |
| 40% | forward_fill | 7.3827 | 10.0695 | -1.1464 | 403 | 403 |
| 40% | cubic_interpolation | 27.7372 | 31.8543 | -20.4801 | 403 | 403 |
| 40% | spline_interpolation | 27.7372 | 31.8543 | -20.4801 | 403 | 403 |
| 50% | neural_net | 5.3664 | 6.9675 | 0.1610 | 504 | 504 |
| 50% | decision_tree | 5.3983 | 6.9366 | 0.1684 | 504 | 504 |
| 50% | random_forest | 5.4200 | 6.9994 | 0.1533 | 504 | 504 |
| 50% | linear_interpolation | 5.4362 | 7.0441 | 0.1425 | 504 | 504 |
| 50% | time_interpolation | 5.4362 | 7.0441 | 0.1425 | 504 | 504 |
| 50% | knn | 5.4362 | 7.0441 | 0.1425 | 504 | 504 |
| 50% | adaptive_imputation | 5.4362 | 7.0441 | 0.1425 | 504 | 504 |
| 50% | knn_upgraded | 5.4447 | 7.0452 | 0.1422 | 504 | 504 |
| 50% | cubic_interpolation | 6.0174 | 7.4492 | 0.0410 | 504 | 504 |
| 50% | spline_interpolation | 6.0174 | 7.4492 | 0.0410 | 504 | 504 |
| 50% | moving_average | 8.1601 | 10.9449 | -1.0703 | 504 | 504 |
| 50% | forward_fill | 8.2467 | 10.9793 | -1.0833 | 504 | 504 |
| 60% | neural_net | 5.1730 | 6.7561 | 0.1664 | 605 | 605 |
| 60% | random_forest | 5.3146 | 6.8543 | 0.1420 | 605 | 605 |
| 60% | knn_upgraded | 5.3496 | 6.8887 | 0.1334 | 605 | 605 |
| 60% | linear_interpolation | 5.3499 | 6.8720 | 0.1376 | 605 | 605 |
| 60% | time_interpolation | 5.3499 | 6.8720 | 0.1376 | 605 | 605 |
| 60% | knn | 5.3499 | 6.8720 | 0.1376 | 605 | 605 |
| 60% | adaptive_imputation | 5.3499 | 6.8720 | 0.1376 | 605 | 605 |
| 60% | decision_tree | 5.3601 | 6.9710 | 0.1126 | 605 | 605 |
| 60% | moving_average | 6.6641 | 9.1634 | -0.5334 | 605 | 605 |
| 60% | forward_fill | 6.7044 | 9.1770 | -0.5379 | 605 | 605 |
| 60% | cubic_interpolation | 12.8316 | 15.8642 | -3.5960 | 605 | 605 |
| 60% | spline_interpolation | 12.8316 | 15.8642 | -3.5960 | 605 | 605 |
| 70% | moving_average | 3.4009 | 4.7069 | 0.0057 | 706 | 706 |
| 70% | forward_fill | 3.5043 | 4.8567 | -0.0586 | 706 | 706 |
| 70% | adaptive_imputation | 3.5043 | 4.8567 | -0.0586 | 706 | 706 |
| 70% | neural_net | 5.5727 | 6.8960 | -1.1343 | 706 | 706 |
| 70% | decision_tree | 5.6223 | 6.9391 | -1.1610 | 706 | 706 |
| 70% | random_forest | 5.6928 | 7.0058 | -1.2028 | 706 | 706 |
| 70% | knn_upgraded | 5.6963 | 7.0022 | -1.2006 | 706 | 706 |
| 70% | linear_interpolation | 5.7381 | 7.0407 | -1.2248 | 706 | 706 |
| 70% | time_interpolation | 5.7381 | 7.0407 | -1.2248 | 706 | 706 |
| 70% | knn | 5.7381 | 7.0407 | -1.2248 | 706 | 706 |
| 70% | cubic_interpolation | 10.1423 | 11.1737 | -4.6034 | 706 | 706 |
| 70% | spline_interpolation | 10.1423 | 11.1737 | -4.6034 | 706 | 706 |
| 80% | neural_net | 4.7335 | 6.0506 | 0.1820 | 806 | 806 |
| 80% | random_forest | 4.7788 | 6.0769 | 0.1749 | 806 | 806 |
| 80% | linear_interpolation | 4.7975 | 6.1094 | 0.1660 | 806 | 806 |
| 80% | time_interpolation | 4.7975 | 6.1094 | 0.1660 | 806 | 806 |
| 80% | knn | 4.7975 | 6.1094 | 0.1660 | 806 | 806 |
| 80% | adaptive_imputation | 4.7975 | 6.1094 | 0.1660 | 806 | 806 |
| 80% | decision_tree | 4.7976 | 6.1093 | 0.1660 | 806 | 806 |
| 80% | knn_upgraded | 4.8028 | 6.1130 | 0.1650 | 806 | 806 |
| 80% | moving_average | 5.3070 | 7.4487 | -0.2397 | 806 | 806 |
| 80% | forward_fill | 5.3337 | 7.4566 | -0.2424 | 806 | 806 |
| 80% | cubic_interpolation | 22.9276 | 28.3087 | -16.9062 | 806 | 806 |
| 80% | spline_interpolation | 22.9276 | 28.3087 | -16.9062 | 806 | 806 |

### Block missing — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 1.5435 | 1.6054 | 4.1018 | 7.3827 | 8.2467 | 6.7044 | 3.5043 | 5.3337 |
| linear_interpolation | 1.0285 | 1.4765 | 3.4286 | 2.9308 | 5.4362 | 5.3499 | 5.7381 | 4.7975 |
| time_interpolation | 1.0285 | 1.4765 | 3.4286 | 2.9308 | 5.4362 | 5.3499 | 5.7381 | 4.7975 |
| cubic_interpolation | 1.1604 | 4.2442 | 7.7599 | 27.7372 | 6.0174 | 12.8316 | 10.1423 | 22.9276 |
| spline_interpolation | 1.1604 | 4.2442 | 7.7599 | 27.7372 | 6.0174 | 12.8316 | 10.1423 | 22.9276 |
| knn | 1.0285 | 1.4765 | 3.4286 | 2.9308 | 5.4362 | 5.3499 | 5.7381 | 4.7975 |
| decision_tree | 1.0268 | 1.4761 | 3.5234 | 2.7163 | 5.3983 | 5.3601 | 5.6223 | 4.7976 |
| random_forest | 1.0145 | 1.4763 | 3.4364 | 2.7685 | 5.4200 | 5.3146 | 5.6928 | 4.7788 |

### Block missing — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 1.7084 | 1.8330 | 6.5393 | 10.0695 | 10.9793 | 9.1770 | 4.8567 | 7.4566 |
| linear_interpolation | 1.1880 | 1.6968 | 4.0453 | 3.6053 | 7.0441 | 6.8720 | 7.0407 | 6.1094 |
| time_interpolation | 1.1880 | 1.6968 | 4.0453 | 3.6053 | 7.0441 | 6.8720 | 7.0407 | 6.1094 |
| cubic_interpolation | 1.3978 | 5.0983 | 9.5520 | 31.8543 | 7.4492 | 15.8642 | 11.1737 | 28.3087 |
| spline_interpolation | 1.3978 | 5.0983 | 9.5520 | 31.8543 | 7.4492 | 15.8642 | 11.1737 | 28.3087 |
| knn | 1.1880 | 1.6968 | 4.0453 | 3.6053 | 7.0441 | 6.8720 | 7.0407 | 6.1094 |
| decision_tree | 1.1854 | 1.6957 | 4.1382 | 3.3872 | 6.9366 | 6.9710 | 6.9391 | 6.1093 |
| random_forest | 1.1739 | 1.6961 | 4.0565 | 3.4427 | 6.9994 | 6.8543 | 7.0058 | 6.0769 |

### Block missing — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -4.4409 | -3.2929 | -0.5729 | -1.1464 | -1.0833 | -0.5379 | -0.0586 | -0.2424 |
| linear_interpolation | -1.6311 | -2.6787 | 0.3980 | 0.7248 | 0.1425 | 0.1376 | -1.2248 | 0.1660 |
| time_interpolation | -1.6311 | -2.6787 | 0.3980 | 0.7248 | 0.1425 | 0.1376 | -1.2248 | 0.1660 |
| cubic_interpolation | -2.6421 | -32.2091 | -2.3562 | -20.4801 | 0.0410 | -3.5960 | -4.6034 | -16.9062 |
| spline_interpolation | -2.6421 | -32.2091 | -2.3562 | -20.4801 | 0.0410 | -3.5960 | -4.6034 | -16.9062 |
| knn | -1.6311 | -2.6787 | 0.3980 | 0.7248 | 0.1425 | 0.1376 | -1.2248 | 0.1660 |
| decision_tree | -1.6195 | -2.6736 | 0.3701 | 0.7571 | 0.1684 | 0.1126 | -1.1610 | 0.1660 |
| random_forest | -1.5687 | -2.6753 | 0.3947 | 0.7491 | 0.1533 | 0.1420 | -1.2028 | 0.1749 |

---

## Block na početku (`block_start`)

### Block na početku — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | decision_tree | 0.7313 | 0.8856 | 0.6088 | 101 | 101 |
| 10% | random_forest | 0.7752 | 0.9541 | 0.5459 | 101 | 101 |
| 10% | neural_net | 0.8793 | 1.0966 | 0.4002 | 101 | 101 |
| 10% | knn_upgraded | 0.9610 | 1.2179 | 0.2601 | 101 | 101 |
| 10% | linear_interpolation | 0.9636 | 1.2281 | 0.2477 | 101 | 101 |
| 10% | time_interpolation | 0.9636 | 1.2281 | 0.2477 | 101 | 101 |
| 10% | knn | 0.9636 | 1.2281 | 0.2477 | 101 | 101 |
| 10% | adaptive_imputation | 0.9636 | 1.2281 | 0.2477 | 101 | 101 |
| 10% | moving_average | 1.0817 | 1.3208 | 0.1299 | 101 | 101 |
| 10% | spline_interpolation | 1.0886 | 1.3436 | 0.0996 | 101 | 101 |
| 10% | cubic_interpolation | 1.1022 | 1.2203 | 0.2573 | 101 | 101 |
| 10% | forward_fill | 1.2386 | 1.4759 | -0.0865 | 101 | 101 |
| 20% | linear_interpolation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| 20% | time_interpolation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| 20% | knn | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| 20% | adaptive_imputation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| 20% | neural_net | 0.7237 | 0.8947 | 0.7608 | 202 | 202 |
| 20% | random_forest | 0.7880 | 0.9141 | 0.7503 | 202 | 202 |
| 20% | knn_upgraded | 0.8446 | 1.0182 | 0.6902 | 202 | 202 |
| 20% | decision_tree | 1.1276 | 1.2592 | 0.5262 | 202 | 202 |
| 20% | cubic_interpolation | 1.6762 | 1.7713 | 0.0624 | 202 | 202 |
| 20% | spline_interpolation | 2.1933 | 2.3259 | -0.6166 | 202 | 202 |
| 20% | moving_average | 2.2213 | 2.5650 | -0.9661 | 202 | 202 |
| 20% | forward_fill | 2.3393 | 2.6579 | -1.1111 | 202 | 202 |
| 30% | adaptive_imputation | 1.9325 | 2.1842 | -0.2000 | 302 | 302 |
| 30% | linear_interpolation | 2.1272 | 2.3947 | -0.4423 | 302 | 302 |
| 30% | time_interpolation | 2.1272 | 2.3947 | -0.4423 | 302 | 302 |
| 30% | knn | 2.1272 | 2.3947 | -0.4423 | 302 | 302 |
| 30% | neural_net | 2.2451 | 2.5608 | -0.6494 | 302 | 302 |
| 30% | knn_upgraded | 2.2903 | 2.5707 | -0.6622 | 302 | 302 |
| 30% | random_forest | 2.3518 | 2.6547 | -0.7726 | 302 | 302 |
| 30% | decision_tree | 2.4442 | 2.7547 | -0.9087 | 302 | 302 |
| 30% | moving_average | 2.9869 | 3.3823 | -1.8774 | 302 | 302 |
| 30% | forward_fill | 3.0183 | 3.3915 | -1.8930 | 302 | 302 |
| 30% | cubic_interpolation | 5.8913 | 6.8477 | -10.7939 | 302 | 302 |
| 30% | spline_interpolation | 7.7047 | 8.7130 | -18.0946 | 302 | 302 |
| 40% | linear_interpolation | 1.8038 | 2.1093 | 0.0554 | 403 | 403 |
| 40% | time_interpolation | 1.8038 | 2.1093 | 0.0554 | 403 | 403 |
| 40% | knn | 1.8038 | 2.1093 | 0.0554 | 403 | 403 |
| 40% | neural_net | 1.8528 | 2.1683 | 0.0019 | 403 | 403 |
| 40% | knn_upgraded | 2.0140 | 2.3052 | -0.1282 | 403 | 403 |
| 40% | random_forest | 2.1198 | 2.4193 | -0.2427 | 403 | 403 |
| 40% | decision_tree | 2.2722 | 2.5830 | -0.4165 | 403 | 403 |
| 40% | adaptive_imputation | 2.2722 | 2.5830 | -0.4165 | 403 | 403 |
| 40% | moving_average | 2.8713 | 3.3525 | -1.3863 | 403 | 403 |
| 40% | forward_fill | 2.9323 | 3.3907 | -1.4409 | 403 | 403 |
| 40% | cubic_interpolation | 7.2939 | 8.5596 | -14.5553 | 403 | 403 |
| 40% | spline_interpolation | 10.6173 | 12.0995 | -30.0816 | 403 | 403 |
| 50% | neural_net | 1.3679 | 1.7544 | 0.4808 | 504 | 504 |
| 50% | linear_interpolation | 1.4386 | 1.9513 | 0.3576 | 504 | 504 |
| 50% | time_interpolation | 1.4386 | 1.9513 | 0.3576 | 504 | 504 |
| 50% | knn | 1.4386 | 1.9513 | 0.3576 | 504 | 504 |
| 50% | adaptive_imputation | 1.4386 | 1.9513 | 0.3576 | 504 | 504 |
| 50% | cubic_interpolation | 1.4492 | 1.7988 | 0.4541 | 504 | 504 |
| 50% | knn_upgraded | 1.6976 | 2.0434 | 0.2956 | 504 | 504 |
| 50% | spline_interpolation | 1.8363 | 2.2186 | 0.1696 | 504 | 504 |
| 50% | random_forest | 1.8680 | 2.1857 | 0.1941 | 504 | 504 |
| 50% | decision_tree | 2.1973 | 2.4875 | -0.0438 | 504 | 504 |
| 50% | moving_average | 3.4995 | 4.0461 | -1.7618 | 504 | 504 |
| 50% | forward_fill | 3.5791 | 4.1150 | -1.8567 | 504 | 504 |
| 60% | cubic_interpolation | 1.5243 | 1.8189 | 0.4898 | 605 | 605 |
| 60% | adaptive_imputation | 1.5243 | 1.8189 | 0.4898 | 605 | 605 |
| 60% | linear_interpolation | 1.5972 | 1.8882 | 0.4502 | 605 | 605 |
| 60% | time_interpolation | 1.5972 | 1.8882 | 0.4502 | 605 | 605 |
| 60% | knn | 1.5972 | 1.8882 | 0.4502 | 605 | 605 |
| 60% | neural_net | 1.6366 | 1.9258 | 0.4281 | 605 | 605 |
| 60% | spline_interpolation | 1.6913 | 1.9643 | 0.4050 | 605 | 605 |
| 60% | knn_upgraded | 2.1038 | 2.3440 | 0.1527 | 605 | 605 |
| 60% | random_forest | 2.3232 | 2.5625 | -0.0126 | 605 | 605 |
| 60% | decision_tree | 2.6418 | 2.8869 | -0.2852 | 605 | 605 |
| 60% | moving_average | 4.0279 | 4.5922 | -2.2521 | 605 | 605 |
| 60% | forward_fill | 4.0896 | 4.6341 | -2.3116 | 605 | 605 |
| 70% | cubic_interpolation | 3.5094 | 4.7387 | -2.3956 | 706 | 706 |
| 70% | adaptive_imputation | 3.5094 | 4.7387 | -2.3956 | 706 | 706 |
| 70% | moving_average | 3.9828 | 4.5339 | -2.1084 | 706 | 706 |
| 70% | forward_fill | 3.9994 | 4.5389 | -2.1154 | 706 | 706 |
| 70% | decision_tree | 4.5831 | 5.2619 | -3.1869 | 706 | 706 |
| 70% | random_forest | 4.6731 | 5.3597 | -3.3438 | 706 | 706 |
| 70% | knn_upgraded | 4.8318 | 5.5203 | -3.6081 | 706 | 706 |
| 70% | neural_net | 5.0912 | 5.7983 | -4.0840 | 706 | 706 |
| 70% | linear_interpolation | 5.1465 | 5.8430 | -4.1626 | 706 | 706 |
| 70% | time_interpolation | 5.1465 | 5.8430 | -4.1626 | 706 | 706 |
| 70% | knn | 5.1465 | 5.8430 | -4.1626 | 706 | 706 |
| 70% | spline_interpolation | 7.4183 | 8.8242 | -10.7748 | 706 | 706 |
| 80% | moving_average | 4.2301 | 4.7813 | -0.3767 | 806 | 806 |
| 80% | forward_fill | 4.2559 | 4.7930 | -0.3835 | 806 | 806 |
| 80% | adaptive_imputation | 4.2559 | 4.7930 | -0.3835 | 806 | 806 |
| 80% | decision_tree | 4.5569 | 5.2906 | -0.6857 | 806 | 806 |
| 80% | neural_net | 4.6294 | 5.4547 | -0.7919 | 806 | 806 |
| 80% | knn_upgraded | 4.8518 | 5.6160 | -0.8994 | 806 | 806 |
| 80% | random_forest | 4.8662 | 5.6133 | -0.8976 | 806 | 806 |
| 80% | linear_interpolation | 5.2599 | 6.0752 | -1.2227 | 806 | 806 |
| 80% | time_interpolation | 5.2599 | 6.0752 | -1.2227 | 806 | 806 |
| 80% | knn | 5.2599 | 6.0752 | -1.2227 | 806 | 806 |
| 80% | cubic_interpolation | 23.7657 | 27.8532 | -45.7205 | 806 | 806 |
| 80% | spline_interpolation | 32.9873 | 36.9107 | -81.0472 | 806 | 806 |

### Block na početku — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 1.2386 | 2.3393 | 3.0183 | 2.9323 | 3.5791 | 4.0896 | 3.9994 | 4.2559 |
| linear_interpolation | 0.9636 | 0.6991 | 2.1272 | 1.8038 | 1.4386 | 1.5972 | 5.1465 | 5.2599 |
| time_interpolation | 0.9636 | 0.6991 | 2.1272 | 1.8038 | 1.4386 | 1.5972 | 5.1465 | 5.2599 |
| cubic_interpolation | 1.1022 | 1.6762 | 5.8913 | 7.2939 | 1.4492 | 1.5243 | 3.5094 | 23.7657 |
| spline_interpolation | 1.0886 | 2.1933 | 7.7047 | 10.6173 | 1.8363 | 1.6913 | 7.4183 | 32.9873 |
| knn | 0.9636 | 0.6991 | 2.1272 | 1.8038 | 1.4386 | 1.5972 | 5.1465 | 5.2599 |
| decision_tree | 0.7313 | 1.1276 | 2.4442 | 2.2722 | 2.1973 | 2.6418 | 4.5831 | 4.5569 |
| random_forest | 0.7752 | 0.7880 | 2.3518 | 2.1198 | 1.8680 | 2.3232 | 4.6731 | 4.8662 |

### Block na početku — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 1.4759 | 2.6579 | 3.3915 | 3.3907 | 4.1150 | 4.6341 | 4.5389 | 4.7930 |
| linear_interpolation | 1.2281 | 0.8889 | 2.3947 | 2.1093 | 1.9513 | 1.8882 | 5.8430 | 6.0752 |
| time_interpolation | 1.2281 | 0.8889 | 2.3947 | 2.1093 | 1.9513 | 1.8882 | 5.8430 | 6.0752 |
| cubic_interpolation | 1.2203 | 1.7713 | 6.8477 | 8.5596 | 1.7988 | 1.8189 | 4.7387 | 27.8532 |
| spline_interpolation | 1.3436 | 2.3259 | 8.7130 | 12.0995 | 2.2186 | 1.9643 | 8.8242 | 36.9107 |
| knn | 1.2281 | 0.8889 | 2.3947 | 2.1093 | 1.9513 | 1.8882 | 5.8430 | 6.0752 |
| decision_tree | 0.8856 | 1.2592 | 2.7547 | 2.5830 | 2.4875 | 2.8869 | 5.2619 | 5.2906 |
| random_forest | 0.9541 | 0.9141 | 2.6547 | 2.4193 | 2.1857 | 2.5625 | 5.3597 | 5.6133 |

### Block na početku — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -0.0865 | -1.1111 | -1.8930 | -1.4409 | -1.8567 | -2.3116 | -2.1154 | -0.3835 |
| linear_interpolation | 0.2477 | 0.7639 | -0.4423 | 0.0554 | 0.3576 | 0.4502 | -4.1626 | -1.2227 |
| time_interpolation | 0.2477 | 0.7639 | -0.4423 | 0.0554 | 0.3576 | 0.4502 | -4.1626 | -1.2227 |
| cubic_interpolation | 0.2573 | 0.0624 | -10.7939 | -14.5553 | 0.4541 | 0.4898 | -2.3956 | -45.7205 |
| spline_interpolation | 0.0996 | -0.6166 | -18.0946 | -30.0816 | 0.1696 | 0.4050 | -10.7748 | -81.0472 |
| knn | 0.2477 | 0.7639 | -0.4423 | 0.0554 | 0.3576 | 0.4502 | -4.1626 | -1.2227 |
| decision_tree | 0.6088 | 0.5262 | -0.9087 | -0.4165 | -0.0438 | -0.2852 | -3.1869 | -0.6857 |
| random_forest | 0.5459 | 0.7503 | -0.7726 | -0.2427 | 0.1941 | -0.0126 | -3.3438 | -0.8976 |

---

## Block u sredini (`block_middle`)

### Block u sredini — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | random_forest | 0.4707 | 0.5657 | -2.1814 | 101 | 101 |
| 10% | knn_upgraded | 0.4755 | 0.5717 | -2.2489 | 101 | 101 |
| 10% | neural_net | 0.4786 | 0.5711 | -2.2422 | 101 | 101 |
| 10% | decision_tree | 0.4908 | 0.5865 | -2.4198 | 101 | 101 |
| 10% | linear_interpolation | 0.4913 | 0.5870 | -2.4255 | 101 | 101 |
| 10% | time_interpolation | 0.4913 | 0.5870 | -2.4255 | 101 | 101 |
| 10% | knn | 0.4913 | 0.5870 | -2.4255 | 101 | 101 |
| 10% | adaptive_imputation | 0.4913 | 0.5870 | -2.4255 | 101 | 101 |
| 10% | moving_average | 0.6685 | 0.7448 | -4.5139 | 101 | 101 |
| 10% | forward_fill | 0.6767 | 0.7474 | -4.5524 | 101 | 101 |
| 10% | cubic_interpolation | 0.8615 | 1.0260 | -9.4641 | 101 | 101 |
| 10% | spline_interpolation | 0.8615 | 1.0260 | -9.4641 | 101 | 101 |
| 20% | neural_net | 1.1338 | 1.2839 | -2.5297 | 202 | 202 |
| 20% | knn_upgraded | 1.1405 | 1.2988 | -2.6122 | 202 | 202 |
| 20% | decision_tree | 1.1447 | 1.2986 | -2.6109 | 202 | 202 |
| 20% | linear_interpolation | 1.1449 | 1.2988 | -2.6120 | 202 | 202 |
| 20% | time_interpolation | 1.1449 | 1.2988 | -2.6120 | 202 | 202 |
| 20% | knn | 1.1449 | 1.2988 | -2.6120 | 202 | 202 |
| 20% | adaptive_imputation | 1.1449 | 1.2988 | -2.6120 | 202 | 202 |
| 20% | random_forest | 1.1499 | 1.3042 | -2.6423 | 202 | 202 |
| 20% | cubic_interpolation | 1.3420 | 1.5821 | -4.3600 | 202 | 202 |
| 20% | spline_interpolation | 1.3420 | 1.5821 | -4.3600 | 202 | 202 |
| 20% | moving_average | 2.0836 | 2.2178 | -9.5331 | 202 | 202 |
| 20% | forward_fill | 2.1429 | 2.2442 | -9.7854 | 202 | 202 |
| 30% | cubic_interpolation | 3.9194 | 4.8003 | -13.3868 | 302 | 302 |
| 30% | spline_interpolation | 3.9194 | 4.8003 | -13.3868 | 302 | 302 |
| 30% | adaptive_imputation | 3.9194 | 4.8003 | -13.3868 | 302 | 302 |
| 30% | neural_net | 3.9762 | 4.2144 | -10.0895 | 302 | 302 |
| 30% | knn_upgraded | 4.0167 | 4.2671 | -10.3686 | 302 | 302 |
| 30% | random_forest | 4.0302 | 4.2756 | -10.4139 | 302 | 302 |
| 30% | linear_interpolation | 4.0555 | 4.3002 | -10.5455 | 302 | 302 |
| 30% | time_interpolation | 4.0555 | 4.3002 | -10.5455 | 302 | 302 |
| 30% | knn | 4.0555 | 4.3002 | -10.5455 | 302 | 302 |
| 30% | decision_tree | 4.0575 | 4.3019 | -10.5545 | 302 | 302 |
| 30% | moving_average | 5.8994 | 6.0770 | -22.0575 | 302 | 302 |
| 30% | forward_fill | 5.9705 | 6.1031 | -22.2562 | 302 | 302 |
| 40% | moving_average | 3.6225 | 4.0178 | -1.2784 | 403 | 403 |
| 40% | forward_fill | 3.6737 | 4.0426 | -1.3067 | 403 | 403 |
| 40% | neural_net | 5.2951 | 5.8182 | -3.7779 | 403 | 403 |
| 40% | knn_upgraded | 5.3101 | 5.8375 | -3.8098 | 403 | 403 |
| 40% | linear_interpolation | 5.3133 | 5.8414 | -3.8162 | 403 | 403 |
| 40% | time_interpolation | 5.3133 | 5.8414 | -3.8162 | 403 | 403 |
| 40% | knn | 5.3133 | 5.8414 | -3.8162 | 403 | 403 |
| 40% | decision_tree | 5.3155 | 5.8436 | -3.8198 | 403 | 403 |
| 40% | random_forest | 5.3158 | 5.8442 | -3.8208 | 403 | 403 |
| 40% | adaptive_imputation | 5.3158 | 5.8442 | -3.8208 | 403 | 403 |
| 40% | cubic_interpolation | 9.9783 | 11.0953 | -16.3760 | 403 | 403 |
| 40% | spline_interpolation | 9.9783 | 11.0953 | -16.3760 | 403 | 403 |
| 50% | cubic_interpolation | 1.2192 | 1.7261 | 0.7966 | 504 | 504 |
| 50% | spline_interpolation | 1.2192 | 1.7261 | 0.7966 | 504 | 504 |
| 50% | adaptive_imputation | 1.2192 | 1.7261 | 0.7966 | 504 | 504 |
| 50% | moving_average | 2.7176 | 3.8942 | -0.0353 | 504 | 504 |
| 50% | forward_fill | 2.8546 | 4.1145 | -0.1558 | 504 | 504 |
| 50% | neural_net | 5.3664 | 6.2753 | -1.6885 | 504 | 504 |
| 50% | knn_upgraded | 5.4252 | 6.3499 | -1.7528 | 504 | 504 |
| 50% | random_forest | 5.4537 | 6.3790 | -1.7781 | 504 | 504 |
| 50% | linear_interpolation | 5.4614 | 6.3855 | -1.7838 | 504 | 504 |
| 50% | time_interpolation | 5.4614 | 6.3855 | -1.7838 | 504 | 504 |
| 50% | knn | 5.4614 | 6.3855 | -1.7838 | 504 | 504 |
| 50% | decision_tree | 5.4629 | 6.3873 | -1.7854 | 504 | 504 |
| 60% | moving_average | 3.3220 | 4.6986 | -0.0628 | 605 | 605 |
| 60% | forward_fill | 3.3930 | 4.7624 | -0.0919 | 605 | 605 |
| 60% | adaptive_imputation | 3.3930 | 4.7624 | -0.0919 | 605 | 605 |
| 60% | neural_net | 4.0725 | 4.7950 | -0.1069 | 605 | 605 |
| 60% | knn_upgraded | 4.0750 | 4.7792 | -0.0995 | 605 | 605 |
| 60% | decision_tree | 4.0806 | 4.7868 | -0.1030 | 605 | 605 |
| 60% | linear_interpolation | 4.0808 | 4.7870 | -0.1031 | 605 | 605 |
| 60% | time_interpolation | 4.0808 | 4.7870 | -0.1031 | 605 | 605 |
| 60% | knn | 4.0808 | 4.7870 | -0.1031 | 605 | 605 |
| 60% | random_forest | 4.0854 | 4.7926 | -0.1057 | 605 | 605 |
| 60% | cubic_interpolation | 4.3577 | 5.3804 | -0.3936 | 605 | 605 |
| 60% | spline_interpolation | 4.3577 | 5.3804 | -0.3936 | 605 | 605 |
| 70% | moving_average | 3.7491 | 5.2530 | -0.0208 | 706 | 706 |
| 70% | forward_fill | 3.8792 | 5.4544 | -0.1006 | 706 | 706 |
| 70% | adaptive_imputation | 3.8792 | 5.4544 | -0.1006 | 706 | 706 |
| 70% | neural_net | 6.5101 | 7.8359 | -1.2714 | 706 | 706 |
| 70% | knn_upgraded | 6.5630 | 7.8732 | -1.2931 | 706 | 706 |
| 70% | random_forest | 6.5847 | 7.8942 | -1.3054 | 706 | 706 |
| 70% | linear_interpolation | 6.6070 | 7.9146 | -1.3173 | 706 | 706 |
| 70% | time_interpolation | 6.6070 | 7.9146 | -1.3173 | 706 | 706 |
| 70% | knn | 6.6070 | 7.9146 | -1.3173 | 706 | 706 |
| 70% | decision_tree | 6.7057 | 8.0111 | -1.3741 | 706 | 706 |
| 70% | cubic_interpolation | 12.3579 | 13.6447 | -5.8872 | 706 | 706 |
| 70% | spline_interpolation | 12.3579 | 13.6447 | -5.8872 | 706 | 706 |
| 80% | moving_average | 4.5123 | 6.2311 | -0.0139 | 806 | 806 |
| 80% | forward_fill | 4.6316 | 6.3931 | -0.0673 | 806 | 806 |
| 80% | adaptive_imputation | 4.6316 | 6.3931 | -0.0673 | 806 | 806 |
| 80% | knn_upgraded | 6.8409 | 8.2367 | -0.7716 | 806 | 806 |
| 80% | random_forest | 6.8553 | 8.2505 | -0.7775 | 806 | 806 |
| 80% | decision_tree | 6.8578 | 8.2550 | -0.7795 | 806 | 806 |
| 80% | linear_interpolation | 6.8624 | 8.2591 | -0.7813 | 806 | 806 |
| 80% | time_interpolation | 6.8624 | 8.2591 | -0.7813 | 806 | 806 |
| 80% | knn | 6.8624 | 8.2591 | -0.7813 | 806 | 806 |
| 80% | neural_net | 6.9829 | 8.3910 | -0.8386 | 806 | 806 |
| 80% | cubic_interpolation | 7.6603 | 8.9431 | -1.0885 | 806 | 806 |
| 80% | spline_interpolation | 7.6603 | 8.9431 | -1.0885 | 806 | 806 |

### Block u sredini — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.6767 | 2.1429 | 5.9705 | 3.6737 | 2.8546 | 3.3930 | 3.8792 | 4.6316 |
| linear_interpolation | 0.4913 | 1.1449 | 4.0555 | 5.3133 | 5.4614 | 4.0808 | 6.6070 | 6.8624 |
| time_interpolation | 0.4913 | 1.1449 | 4.0555 | 5.3133 | 5.4614 | 4.0808 | 6.6070 | 6.8624 |
| cubic_interpolation | 0.8615 | 1.3420 | 3.9194 | 9.9783 | 1.2192 | 4.3577 | 12.3579 | 7.6603 |
| spline_interpolation | 0.8615 | 1.3420 | 3.9194 | 9.9783 | 1.2192 | 4.3577 | 12.3579 | 7.6603 |
| knn | 0.4913 | 1.1449 | 4.0555 | 5.3133 | 5.4614 | 4.0808 | 6.6070 | 6.8624 |
| decision_tree | 0.4908 | 1.1447 | 4.0575 | 5.3155 | 5.4629 | 4.0806 | 6.7057 | 6.8578 |
| random_forest | 0.4707 | 1.1499 | 4.0302 | 5.3158 | 5.4537 | 4.0854 | 6.5847 | 6.8553 |

### Block u sredini — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.7474 | 2.2442 | 6.1031 | 4.0426 | 4.1145 | 4.7624 | 5.4544 | 6.3931 |
| linear_interpolation | 0.5870 | 1.2988 | 4.3002 | 5.8414 | 6.3855 | 4.7870 | 7.9146 | 8.2591 |
| time_interpolation | 0.5870 | 1.2988 | 4.3002 | 5.8414 | 6.3855 | 4.7870 | 7.9146 | 8.2591 |
| cubic_interpolation | 1.0260 | 1.5821 | 4.8003 | 11.0953 | 1.7261 | 5.3804 | 13.6447 | 8.9431 |
| spline_interpolation | 1.0260 | 1.5821 | 4.8003 | 11.0953 | 1.7261 | 5.3804 | 13.6447 | 8.9431 |
| knn | 0.5870 | 1.2988 | 4.3002 | 5.8414 | 6.3855 | 4.7870 | 7.9146 | 8.2591 |
| decision_tree | 0.5865 | 1.2986 | 4.3019 | 5.8436 | 6.3873 | 4.7868 | 8.0111 | 8.2550 |
| random_forest | 0.5657 | 1.3042 | 4.2756 | 5.8442 | 6.3790 | 4.7926 | 7.8942 | 8.2505 |

### Block u sredini — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -4.5524 | -9.7854 | -22.2562 | -1.3067 | -0.1558 | -0.0919 | -0.1006 | -0.0673 |
| linear_interpolation | -2.4255 | -2.6120 | -10.5455 | -3.8162 | -1.7838 | -0.1031 | -1.3173 | -0.7813 |
| time_interpolation | -2.4255 | -2.6120 | -10.5455 | -3.8162 | -1.7838 | -0.1031 | -1.3173 | -0.7813 |
| cubic_interpolation | -9.4641 | -4.3600 | -13.3868 | -16.3760 | 0.7966 | -0.3936 | -5.8872 | -1.0885 |
| spline_interpolation | -9.4641 | -4.3600 | -13.3868 | -16.3760 | 0.7966 | -0.3936 | -5.8872 | -1.0885 |
| knn | -2.4255 | -2.6120 | -10.5455 | -3.8162 | -1.7838 | -0.1031 | -1.3173 | -0.7813 |
| decision_tree | -2.4198 | -2.6109 | -10.5545 | -3.8198 | -1.7854 | -0.1030 | -1.3741 | -0.7795 |
| random_forest | -2.1814 | -2.6423 | -10.4139 | -3.8208 | -1.7781 | -0.1057 | -1.3054 | -0.7775 |

---

## Block na kraju (`block_end`)

### Block na kraju — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | decision_tree | 2.6289 | 2.9110 | 0.6776 | 101 | 101 |
| 10% | random_forest | 2.8922 | 3.3180 | 0.5812 | 101 | 101 |
| 10% | neural_net | 3.2624 | 4.0373 | 0.3800 | 101 | 101 |
| 10% | linear_interpolation | 3.4473 | 4.1538 | 0.3437 | 101 | 101 |
| 10% | time_interpolation | 3.4473 | 4.1538 | 0.3437 | 101 | 101 |
| 10% | knn | 3.4473 | 4.1538 | 0.3437 | 101 | 101 |
| 10% | adaptive_imputation | 3.4473 | 4.1538 | 0.3437 | 101 | 101 |
| 10% | knn_upgraded | 3.4495 | 4.1576 | 0.3424 | 101 | 101 |
| 10% | cubic_interpolation | 4.9709 | 5.9253 | -0.3356 | 101 | 101 |
| 10% | spline_interpolation | 5.2391 | 6.2332 | -0.4780 | 101 | 101 |
| 10% | moving_average | 7.8220 | 9.3988 | -2.3604 | 101 | 101 |
| 10% | forward_fill | 8.4606 | 9.7525 | -2.6181 | 101 | 101 |
| 20% | cubic_interpolation | 4.1828 | 4.5838 | 0.2258 | 202 | 202 |
| 20% | adaptive_imputation | 4.1828 | 4.5838 | 0.2258 | 202 | 202 |
| 20% | moving_average | 5.4719 | 6.3617 | -0.4913 | 202 | 202 |
| 20% | neural_net | 5.5046 | 6.6913 | -0.6498 | 202 | 202 |
| 20% | forward_fill | 5.5124 | 6.3678 | -0.4942 | 202 | 202 |
| 20% | decision_tree | 5.5309 | 6.6861 | -0.6472 | 202 | 202 |
| 20% | linear_interpolation | 5.5318 | 6.6875 | -0.6479 | 202 | 202 |
| 20% | time_interpolation | 5.5318 | 6.6875 | -0.6479 | 202 | 202 |
| 20% | knn | 5.5318 | 6.6875 | -0.6479 | 202 | 202 |
| 20% | random_forest | 5.5697 | 6.7857 | -0.6967 | 202 | 202 |
| 20% | knn_upgraded | 5.5862 | 6.7538 | -0.6807 | 202 | 202 |
| 20% | spline_interpolation | 8.3969 | 8.9561 | -1.9556 | 202 | 202 |
| 30% | spline_interpolation | 4.8486 | 5.9726 | -0.7742 | 302 | 302 |
| 30% | adaptive_imputation | 4.8486 | 5.9726 | -0.7742 | 302 | 302 |
| 30% | cubic_interpolation | 5.0029 | 6.1929 | -0.9075 | 302 | 302 |
| 30% | decision_tree | 5.3206 | 6.4961 | -1.0988 | 302 | 302 |
| 30% | random_forest | 5.3325 | 6.5065 | -1.1055 | 302 | 302 |
| 30% | knn_upgraded | 5.3792 | 6.5632 | -1.1424 | 302 | 302 |
| 30% | neural_net | 5.3996 | 6.5774 | -1.1517 | 302 | 302 |
| 30% | linear_interpolation | 5.4043 | 6.5802 | -1.1535 | 302 | 302 |
| 30% | time_interpolation | 5.4043 | 6.5802 | -1.1535 | 302 | 302 |
| 30% | knn | 5.4043 | 6.5802 | -1.1535 | 302 | 302 |
| 30% | moving_average | 5.4775 | 6.6978 | -1.2312 | 302 | 302 |
| 30% | forward_fill | 5.4791 | 6.6979 | -1.2312 | 302 | 302 |
| 40% | decision_tree | 5.4621 | 6.6719 | -0.1895 | 403 | 403 |
| 40% | random_forest | 5.5721 | 6.8514 | -0.2543 | 403 | 403 |
| 40% | knn_upgraded | 6.0592 | 7.5231 | -0.5124 | 403 | 403 |
| 40% | neural_net | 6.6972 | 8.1089 | -0.7570 | 403 | 403 |
| 40% | linear_interpolation | 6.8261 | 8.3215 | -0.8504 | 403 | 403 |
| 40% | time_interpolation | 6.8261 | 8.3215 | -0.8504 | 403 | 403 |
| 40% | knn | 6.8261 | 8.3215 | -0.8504 | 403 | 403 |
| 40% | adaptive_imputation | 6.8261 | 8.3215 | -0.8504 | 403 | 403 |
| 40% | cubic_interpolation | 9.5956 | 11.1944 | -2.3486 | 403 | 403 |
| 40% | spline_interpolation | 10.3644 | 12.1292 | -2.9312 | 403 | 403 |
| 40% | moving_average | 10.8786 | 12.5466 | -3.2064 | 403 | 403 |
| 40% | forward_fill | 11.0101 | 12.5944 | -3.2385 | 403 | 403 |
| 50% | neural_net | 4.5343 | 6.1421 | 0.2573 | 504 | 504 |
| 50% | decision_tree | 4.8178 | 5.8106 | 0.3353 | 504 | 504 |
| 50% | knn_upgraded | 4.9521 | 6.3431 | 0.2079 | 504 | 504 |
| 50% | random_forest | 5.0979 | 6.2580 | 0.2290 | 504 | 504 |
| 50% | linear_interpolation | 5.2375 | 7.0389 | 0.0246 | 504 | 504 |
| 50% | time_interpolation | 5.2375 | 7.0389 | 0.0246 | 504 | 504 |
| 50% | knn | 5.2375 | 7.0389 | 0.0246 | 504 | 504 |
| 50% | adaptive_imputation | 5.2375 | 7.0389 | 0.0246 | 504 | 504 |
| 50% | cubic_interpolation | 6.3027 | 8.2675 | -0.3457 | 504 | 504 |
| 50% | spline_interpolation | 6.4615 | 8.4590 | -0.4087 | 504 | 504 |
| 50% | moving_average | 9.2358 | 11.6882 | -1.6896 | 504 | 504 |
| 50% | forward_fill | 9.3483 | 11.7349 | -1.7111 | 504 | 504 |
| 60% | linear_interpolation | 4.9650 | 6.0693 | 0.3007 | 605 | 605 |
| 60% | time_interpolation | 4.9650 | 6.0693 | 0.3007 | 605 | 605 |
| 60% | knn | 4.9650 | 6.0693 | 0.3007 | 605 | 605 |
| 60% | adaptive_imputation | 4.9650 | 6.0693 | 0.3007 | 605 | 605 |
| 60% | knn_upgraded | 5.0400 | 5.8996 | 0.3392 | 605 | 605 |
| 60% | random_forest | 5.0473 | 5.8173 | 0.3576 | 605 | 605 |
| 60% | neural_net | 5.0808 | 6.1411 | 0.2840 | 605 | 605 |
| 60% | decision_tree | 5.1470 | 5.8590 | 0.3483 | 605 | 605 |
| 60% | moving_average | 6.8013 | 8.9486 | -0.5202 | 605 | 605 |
| 60% | forward_fill | 6.8690 | 8.9755 | -0.5293 | 605 | 605 |
| 60% | cubic_interpolation | 8.1166 | 9.5544 | -0.7330 | 605 | 605 |
| 60% | spline_interpolation | 10.6070 | 12.5410 | -1.9857 | 605 | 605 |
| 70% | linear_interpolation | 5.2253 | 6.0540 | 0.2256 | 706 | 706 |
| 70% | time_interpolation | 5.2253 | 6.0540 | 0.2256 | 706 | 706 |
| 70% | knn | 5.2253 | 6.0540 | 0.2256 | 706 | 706 |
| 70% | adaptive_imputation | 5.2253 | 6.0540 | 0.2256 | 706 | 706 |
| 70% | neural_net | 5.2308 | 6.0477 | 0.2272 | 706 | 706 |
| 70% | knn_upgraded | 5.3300 | 6.1250 | 0.2073 | 706 | 706 |
| 70% | random_forest | 5.3365 | 6.1235 | 0.2077 | 706 | 706 |
| 70% | decision_tree | 5.4158 | 6.2233 | 0.1816 | 706 | 706 |
| 70% | moving_average | 5.8638 | 7.2191 | -0.1012 | 706 | 706 |
| 70% | forward_fill | 5.8994 | 7.2303 | -0.1047 | 706 | 706 |
| 70% | cubic_interpolation | 10.9486 | 13.3992 | -2.7937 | 706 | 706 |
| 70% | spline_interpolation | 13.5750 | 16.3927 | -4.6782 | 706 | 706 |
| 80% | cubic_interpolation | 4.0472 | 5.7523 | 0.2535 | 806 | 806 |
| 80% | adaptive_imputation | 4.0472 | 5.7523 | 0.2535 | 806 | 806 |
| 80% | neural_net | 4.3280 | 5.2041 | 0.3890 | 806 | 806 |
| 80% | decision_tree | 4.4766 | 5.4951 | 0.3188 | 806 | 806 |
| 80% | linear_interpolation | 4.4828 | 5.4898 | 0.3201 | 806 | 806 |
| 80% | time_interpolation | 4.4828 | 5.4898 | 0.3201 | 806 | 806 |
| 80% | knn | 4.4828 | 5.4898 | 0.3201 | 806 | 806 |
| 80% | spline_interpolation | 4.4920 | 6.4914 | 0.0494 | 806 | 806 |
| 80% | knn_upgraded | 4.6598 | 5.5251 | 0.3113 | 806 | 806 |
| 80% | random_forest | 4.6644 | 5.4900 | 0.3201 | 806 | 806 |
| 80% | moving_average | 5.5421 | 7.7871 | -0.3680 | 806 | 806 |
| 80% | forward_fill | 5.5918 | 7.8095 | -0.3759 | 806 | 806 |

### Block na kraju — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 8.4606 | 5.5124 | 5.4791 | 11.0101 | 9.3483 | 6.8690 | 5.8994 | 5.5918 |
| linear_interpolation | 3.4473 | 5.5318 | 5.4043 | 6.8261 | 5.2375 | 4.9650 | 5.2253 | 4.4828 |
| time_interpolation | 3.4473 | 5.5318 | 5.4043 | 6.8261 | 5.2375 | 4.9650 | 5.2253 | 4.4828 |
| cubic_interpolation | 4.9709 | 4.1828 | 5.0029 | 9.5956 | 6.3027 | 8.1166 | 10.9486 | 4.0472 |
| spline_interpolation | 5.2391 | 8.3969 | 4.8486 | 10.3644 | 6.4615 | 10.6070 | 13.5750 | 4.4920 |
| knn | 3.4473 | 5.5318 | 5.4043 | 6.8261 | 5.2375 | 4.9650 | 5.2253 | 4.4828 |
| decision_tree | 2.6289 | 5.5309 | 5.3206 | 5.4621 | 4.8178 | 5.1470 | 5.4158 | 4.4766 |
| random_forest | 2.8922 | 5.5697 | 5.3325 | 5.5721 | 5.0979 | 5.0473 | 5.3365 | 4.6644 |

### Block na kraju — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 9.7525 | 6.3678 | 6.6979 | 12.5944 | 11.7349 | 8.9755 | 7.2303 | 7.8095 |
| linear_interpolation | 4.1538 | 6.6875 | 6.5802 | 8.3215 | 7.0389 | 6.0693 | 6.0540 | 5.4898 |
| time_interpolation | 4.1538 | 6.6875 | 6.5802 | 8.3215 | 7.0389 | 6.0693 | 6.0540 | 5.4898 |
| cubic_interpolation | 5.9253 | 4.5838 | 6.1929 | 11.1944 | 8.2675 | 9.5544 | 13.3992 | 5.7523 |
| spline_interpolation | 6.2332 | 8.9561 | 5.9726 | 12.1292 | 8.4590 | 12.5410 | 16.3927 | 6.4914 |
| knn | 4.1538 | 6.6875 | 6.5802 | 8.3215 | 7.0389 | 6.0693 | 6.0540 | 5.4898 |
| decision_tree | 2.9110 | 6.6861 | 6.4961 | 6.6719 | 5.8106 | 5.8590 | 6.2233 | 5.4951 |
| random_forest | 3.3180 | 6.7857 | 6.5065 | 6.8514 | 6.2580 | 5.8173 | 6.1235 | 5.4900 |

### Block na kraju — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -2.6181 | -0.4942 | -1.2312 | -3.2385 | -1.7111 | -0.5293 | -0.1047 | -0.3759 |
| linear_interpolation | 0.3437 | -0.6479 | -1.1535 | -0.8504 | 0.0246 | 0.3007 | 0.2256 | 0.3201 |
| time_interpolation | 0.3437 | -0.6479 | -1.1535 | -0.8504 | 0.0246 | 0.3007 | 0.2256 | 0.3201 |
| cubic_interpolation | -0.3356 | 0.2258 | -0.9075 | -2.3486 | -0.3457 | -0.7330 | -2.7937 | 0.2535 |
| spline_interpolation | -0.4780 | -1.9556 | -0.7742 | -2.9312 | -0.4087 | -1.9857 | -4.6782 | 0.0494 |
| knn | 0.3437 | -0.6479 | -1.1535 | -0.8504 | 0.0246 | 0.3007 | 0.2256 | 0.3201 |
| decision_tree | 0.6776 | -0.6472 | -1.0988 | -0.1895 | 0.3353 | 0.3483 | 0.1816 | 0.3188 |
| random_forest | 0.5812 | -0.6967 | -1.1055 | -0.2543 | 0.2290 | 0.3576 | 0.2077 | 0.3201 |

---

## Najbolja metoda po scenariju i missing rateu (po MAE)

| scenario | block_position | missing_rate | najbolja metoda | MAE | RMSE | R² |
|----------|----------------|--------------|-----------------|-----|------|-----|
| random | none | 10% | spline_interpolation | 0.0470 | 0.0828 | 0.9998 |
| random | none | 20% | spline_interpolation | 0.0635 | 0.1052 | 0.9997 |
| random | none | 30% | linear_interpolation | 0.0834 | 0.1401 | 0.9995 |
| random | none | 40% | spline_interpolation | 0.0908 | 0.1724 | 0.9992 |
| random | none | 50% | spline_interpolation | 0.0997 | 0.2109 | 0.9988 |
| random | none | 60% | cubic_interpolation | 0.1230 | 0.2369 | 0.9985 |
| random | none | 70% | linear_interpolation | 0.1774 | 0.3320 | 0.9971 |
| random | none | 80% | linear_interpolation | 0.1785 | 0.3145 | 0.9974 |
| block | none | 10% | random_forest | 1.0145 | 1.1739 | -1.5687 |
| block | none | 20% | decision_tree | 1.4761 | 1.6957 | -2.6736 |
| block | none | 30% | neural_net | 3.4236 | 4.0464 | 0.3977 |
| block | none | 40% | decision_tree | 2.7163 | 3.3872 | 0.7571 |
| block | none | 50% | neural_net | 5.3664 | 6.9675 | 0.1610 |
| block | none | 60% | neural_net | 5.1730 | 6.7561 | 0.1664 |
| block | none | 70% | moving_average | 3.4009 | 4.7069 | 0.0057 |
| block | none | 80% | neural_net | 4.7335 | 6.0506 | 0.1820 |
| block_start | start | 10% | decision_tree | 0.7313 | 0.8856 | 0.6088 |
| block_start | start | 20% | linear_interpolation | 0.6991 | 0.8889 | 0.7639 |
| block_start | start | 30% | adaptive_imputation | 1.9325 | 2.1842 | -0.2000 |
| block_start | start | 40% | linear_interpolation | 1.8038 | 2.1093 | 0.0554 |
| block_start | start | 50% | neural_net | 1.3679 | 1.7544 | 0.4808 |
| block_start | start | 60% | cubic_interpolation | 1.5243 | 1.8189 | 0.4898 |
| block_start | start | 70% | cubic_interpolation | 3.5094 | 4.7387 | -2.3956 |
| block_start | start | 80% | moving_average | 4.2301 | 4.7813 | -0.3767 |
| block_middle | middle | 10% | random_forest | 0.4707 | 0.5657 | -2.1814 |
| block_middle | middle | 20% | neural_net | 1.1338 | 1.2839 | -2.5297 |
| block_middle | middle | 30% | cubic_interpolation | 3.9194 | 4.8003 | -13.3868 |
| block_middle | middle | 40% | moving_average | 3.6225 | 4.0178 | -1.2784 |
| block_middle | middle | 50% | cubic_interpolation | 1.2192 | 1.7261 | 0.7966 |
| block_middle | middle | 60% | moving_average | 3.3220 | 4.6986 | -0.0628 |
| block_middle | middle | 70% | moving_average | 3.7491 | 5.2530 | -0.0208 |
| block_middle | middle | 80% | moving_average | 4.5123 | 6.2311 | -0.0139 |
| block_end | end | 10% | decision_tree | 2.6289 | 2.9110 | 0.6776 |
| block_end | end | 20% | cubic_interpolation | 4.1828 | 4.5838 | 0.2258 |
| block_end | end | 30% | spline_interpolation | 4.8486 | 5.9726 | -0.7742 |
| block_end | end | 40% | decision_tree | 5.4621 | 6.6719 | -0.1895 |
| block_end | end | 50% | neural_net | 4.5343 | 6.1421 | 0.2573 |
| block_end | end | 60% | linear_interpolation | 4.9650 | 6.0693 | 0.3007 |
| block_end | end | 70% | linear_interpolation | 5.2253 | 6.0540 | 0.2256 |
| block_end | end | 80% | cubic_interpolation | 4.0472 | 5.7523 | 0.2535 |