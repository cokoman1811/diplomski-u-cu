# Sve tablice rezultata — missing rate 10–80 %

*Izvor: `results/experiment_results.csv` (320 redaka)*
*Generirano: `python scripts/generate_results_tables.py`*

---

## KOMPLETNA TABLICA (svi scenariji, svi rateovi, sve metode)

| scenario | block_position | missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|----------|----------------|--------------|--------|-----|------|-----|---------|-----------|
| block | none | 10% | cubic_interpolation | 1.1604 | 1.3978 | -2.6421 | 101 | 101 |
| block | none | 10% | decision_tree | 2.9869 | 3.1589 | -17.6018 | 101 | 101 |
| block | none | 10% | forward_fill | 1.5435 | 1.7084 | -4.4409 | 101 | 101 |
| block | none | 10% | knn | 2.6173 | 3.0283 | -16.0955 | 101 | 101 |
| block | none | 10% | linear_interpolation | 1.0285 | 1.1880 | -1.6311 | 101 | 101 |
| block | none | 10% | random_forest | 1.8446 | 1.9509 | -6.0949 | 101 | 101 |
| block | none | 10% | spline_interpolation | 1.1604 | 1.3978 | -2.6421 | 101 | 101 |
| block | none | 10% | time_interpolation | 1.0285 | 1.1880 | -1.6311 | 101 | 101 |
| block | none | 20% | cubic_interpolation | 4.2442 | 5.0983 | -32.2091 | 202 | 202 |
| block | none | 20% | decision_tree | 2.0627 | 2.2444 | -5.4362 | 202 | 202 |
| block | none | 20% | forward_fill | 1.6054 | 1.8330 | -3.2929 | 202 | 202 |
| block | none | 20% | knn | 2.1354 | 2.5753 | -7.4734 | 202 | 202 |
| block | none | 20% | linear_interpolation | 1.4765 | 1.6968 | -2.6787 | 202 | 202 |
| block | none | 20% | random_forest | 2.4682 | 2.6161 | -7.7439 | 202 | 202 |
| block | none | 20% | spline_interpolation | 4.2442 | 5.0983 | -32.2091 | 202 | 202 |
| block | none | 20% | time_interpolation | 1.4765 | 1.6968 | -2.6787 | 202 | 202 |
| block | none | 30% | cubic_interpolation | 7.7599 | 9.5520 | -2.3562 | 302 | 302 |
| block | none | 30% | decision_tree | 9.7856 | 10.9263 | -3.3914 | 302 | 302 |
| block | none | 30% | forward_fill | 4.1018 | 6.5393 | -0.5729 | 302 | 302 |
| block | none | 30% | knn | 5.7174 | 6.9792 | -0.7917 | 302 | 302 |
| block | none | 30% | linear_interpolation | 3.4286 | 4.0453 | 0.3980 | 302 | 302 |
| block | none | 30% | random_forest | 3.9860 | 6.0331 | -0.3389 | 302 | 302 |
| block | none | 30% | spline_interpolation | 7.7599 | 9.5520 | -2.3562 | 302 | 302 |
| block | none | 30% | time_interpolation | 3.4286 | 4.0453 | 0.3980 | 302 | 302 |
| block | none | 40% | cubic_interpolation | 27.7372 | 31.8543 | -20.4801 | 403 | 403 |
| block | none | 40% | decision_tree | 13.8825 | 15.4907 | -4.0798 | 403 | 403 |
| block | none | 40% | forward_fill | 7.3827 | 10.0695 | -1.1464 | 403 | 403 |
| block | none | 40% | knn | 5.0333 | 6.6578 | 0.0617 | 403 | 403 |
| block | none | 40% | linear_interpolation | 2.9308 | 3.6053 | 0.7248 | 403 | 403 |
| block | none | 40% | random_forest | 6.6848 | 9.0632 | -0.7389 | 403 | 403 |
| block | none | 40% | spline_interpolation | 27.7372 | 31.8543 | -20.4801 | 403 | 403 |
| block | none | 40% | time_interpolation | 2.9308 | 3.6053 | 0.7248 | 403 | 403 |
| block | none | 50% | cubic_interpolation | 6.0174 | 7.4492 | 0.0410 | 504 | 504 |
| block | none | 50% | decision_tree | 6.9406 | 7.6609 | -0.0143 | 504 | 504 |
| block | none | 50% | forward_fill | 8.2467 | 10.9793 | -1.0833 | 504 | 504 |
| block | none | 50% | knn | 6.9655 | 8.5127 | -0.2524 | 504 | 504 |
| block | none | 50% | linear_interpolation | 5.4362 | 7.0441 | 0.1425 | 504 | 504 |
| block | none | 50% | random_forest | 8.0585 | 10.6314 | -0.9534 | 504 | 504 |
| block | none | 50% | spline_interpolation | 6.0174 | 7.4492 | 0.0410 | 504 | 504 |
| block | none | 50% | time_interpolation | 5.4362 | 7.0441 | 0.1425 | 504 | 504 |
| block | none | 60% | cubic_interpolation | 12.8316 | 15.8642 | -3.5960 | 605 | 605 |
| block | none | 60% | decision_tree | 6.6370 | 7.5778 | -0.0486 | 605 | 605 |
| block | none | 60% | forward_fill | 6.7044 | 9.1770 | -0.5379 | 605 | 605 |
| block | none | 60% | knn | 5.9034 | 7.2391 | 0.0430 | 605 | 605 |
| block | none | 60% | linear_interpolation | 5.3499 | 6.8720 | 0.1376 | 605 | 605 |
| block | none | 60% | random_forest | 6.5787 | 7.6620 | -0.0721 | 605 | 605 |
| block | none | 60% | spline_interpolation | 12.8316 | 15.8642 | -3.5960 | 605 | 605 |
| block | none | 60% | time_interpolation | 5.3499 | 6.8720 | 0.1376 | 605 | 605 |
| block | none | 70% | cubic_interpolation | 10.1423 | 11.1737 | -4.6034 | 706 | 706 |
| block | none | 70% | decision_tree | 12.6597 | 13.5111 | -7.1929 | 706 | 706 |
| block | none | 70% | forward_fill | 3.5043 | 4.8567 | -0.0586 | 706 | 706 |
| block | none | 70% | knn | 7.3758 | 9.6727 | -3.1991 | 706 | 706 |
| block | none | 70% | linear_interpolation | 5.7381 | 7.0407 | -1.2248 | 706 | 706 |
| block | none | 70% | random_forest | 3.6055 | 4.7794 | -0.0252 | 706 | 706 |
| block | none | 70% | spline_interpolation | 10.1423 | 11.1737 | -4.6034 | 706 | 706 |
| block | none | 70% | time_interpolation | 5.7381 | 7.0407 | -1.2248 | 706 | 706 |
| block | none | 80% | cubic_interpolation | 22.9276 | 28.3087 | -16.9062 | 806 | 806 |
| block | none | 80% | decision_tree | 5.8292 | 6.6972 | -0.0022 | 806 | 806 |
| block | none | 80% | forward_fill | 5.3337 | 7.4566 | -0.2424 | 806 | 806 |
| block | none | 80% | knn | 5.0900 | 6.3753 | 0.0918 | 806 | 806 |
| block | none | 80% | linear_interpolation | 4.7975 | 6.1094 | 0.1660 | 806 | 806 |
| block | none | 80% | random_forest | 5.3337 | 7.3957 | -0.2222 | 806 | 806 |
| block | none | 80% | spline_interpolation | 22.9276 | 28.3087 | -16.9062 | 806 | 806 |
| block | none | 80% | time_interpolation | 4.7975 | 6.1094 | 0.1660 | 806 | 806 |
| block_end | end | 10% | cubic_interpolation | 4.9709 | 5.9253 | -0.3356 | 101 | 101 |
| block_end | end | 10% | decision_tree | 5.8625 | 6.6532 | -0.6838 | 101 | 101 |
| block_end | end | 10% | forward_fill | 8.4606 | 9.7525 | -2.6181 | 101 | 101 |
| block_end | end | 10% | knn | 5.9186 | 6.8597 | -0.7900 | 101 | 101 |
| block_end | end | 10% | linear_interpolation | 3.4473 | 4.1538 | 0.3437 | 101 | 101 |
| block_end | end | 10% | random_forest | 8.7605 | 10.0709 | -2.8582 | 101 | 101 |
| block_end | end | 10% | spline_interpolation | 5.2391 | 6.2332 | -0.4780 | 101 | 101 |
| block_end | end | 10% | time_interpolation | 3.4473 | 4.1538 | 0.3437 | 101 | 101 |
| block_end | end | 20% | cubic_interpolation | 4.1828 | 4.5838 | 0.2258 | 202 | 202 |
| block_end | end | 20% | decision_tree | 4.9268 | 5.6425 | -0.1732 | 202 | 202 |
| block_end | end | 20% | forward_fill | 5.5124 | 6.3678 | -0.4942 | 202 | 202 |
| block_end | end | 20% | knn | 5.2854 | 6.1607 | -0.3986 | 202 | 202 |
| block_end | end | 20% | linear_interpolation | 5.5318 | 6.6875 | -0.6479 | 202 | 202 |
| block_end | end | 20% | random_forest | 4.8834 | 5.6314 | -0.1685 | 202 | 202 |
| block_end | end | 20% | spline_interpolation | 8.3969 | 8.9561 | -1.9556 | 202 | 202 |
| block_end | end | 20% | time_interpolation | 5.5318 | 6.6875 | -0.6479 | 202 | 202 |
| block_end | end | 30% | cubic_interpolation | 5.0029 | 6.1929 | -0.9075 | 302 | 302 |
| block_end | end | 30% | decision_tree | 5.5311 | 6.7525 | -1.2678 | 302 | 302 |
| block_end | end | 30% | forward_fill | 5.4791 | 6.6979 | -1.2312 | 302 | 302 |
| block_end | end | 30% | knn | 11.4994 | 12.8899 | -7.2637 | 302 | 302 |
| block_end | end | 30% | linear_interpolation | 5.4043 | 6.5802 | -1.1535 | 302 | 302 |
| block_end | end | 30% | random_forest | 5.9756 | 7.2152 | -1.5892 | 302 | 302 |
| block_end | end | 30% | spline_interpolation | 4.8486 | 5.9726 | -0.7742 | 302 | 302 |
| block_end | end | 30% | time_interpolation | 5.4043 | 6.5802 | -1.1535 | 302 | 302 |
| block_end | end | 40% | cubic_interpolation | 9.5956 | 11.1944 | -2.3486 | 403 | 403 |
| block_end | end | 40% | decision_tree | 8.4857 | 10.0647 | -1.7068 | 403 | 403 |
| block_end | end | 40% | forward_fill | 11.0101 | 12.5944 | -3.2385 | 403 | 403 |
| block_end | end | 40% | knn | 11.4460 | 12.9318 | -3.4686 | 403 | 403 |
| block_end | end | 40% | linear_interpolation | 6.8261 | 8.3215 | -0.8504 | 403 | 403 |
| block_end | end | 40% | random_forest | 11.4494 | 12.9626 | -3.4899 | 403 | 403 |
| block_end | end | 40% | spline_interpolation | 10.3644 | 12.1292 | -2.9312 | 403 | 403 |
| block_end | end | 40% | time_interpolation | 6.8261 | 8.3215 | -0.8504 | 403 | 403 |
| block_end | end | 50% | cubic_interpolation | 6.3027 | 8.2675 | -0.3457 | 504 | 504 |
| block_end | end | 50% | decision_tree | 8.4771 | 10.7083 | -1.2575 | 504 | 504 |
| block_end | end | 50% | forward_fill | 9.3483 | 11.7349 | -1.7111 | 504 | 504 |
| block_end | end | 50% | knn | 8.5669 | 10.8827 | -1.3316 | 504 | 504 |
| block_end | end | 50% | linear_interpolation | 5.2375 | 7.0389 | 0.0246 | 504 | 504 |
| block_end | end | 50% | random_forest | 8.9477 | 11.3091 | -1.5179 | 504 | 504 |
| block_end | end | 50% | spline_interpolation | 6.4615 | 8.4590 | -0.4087 | 504 | 504 |
| block_end | end | 50% | time_interpolation | 5.2375 | 7.0389 | 0.0246 | 504 | 504 |
| block_end | end | 60% | cubic_interpolation | 8.1166 | 9.5544 | -0.7330 | 605 | 605 |
| block_end | end | 60% | decision_tree | 6.7400 | 7.9274 | -0.1930 | 605 | 605 |
| block_end | end | 60% | forward_fill | 6.8690 | 8.9755 | -0.5293 | 605 | 605 |
| block_end | end | 60% | knn | 6.8733 | 8.0746 | -0.2377 | 605 | 605 |
| block_end | end | 60% | linear_interpolation | 4.9650 | 6.0693 | 0.3007 | 605 | 605 |
| block_end | end | 60% | random_forest | 6.9570 | 8.0532 | -0.2312 | 605 | 605 |
| block_end | end | 60% | spline_interpolation | 10.6070 | 12.5410 | -1.9857 | 605 | 605 |
| block_end | end | 60% | time_interpolation | 4.9650 | 6.0693 | 0.3007 | 605 | 605 |
| block_end | end | 70% | cubic_interpolation | 10.9486 | 13.3992 | -2.7937 | 706 | 706 |
| block_end | end | 70% | decision_tree | 5.8695 | 6.9267 | -0.0138 | 706 | 706 |
| block_end | end | 70% | forward_fill | 5.8994 | 7.2303 | -0.1047 | 706 | 706 |
| block_end | end | 70% | knn | 6.2982 | 8.2131 | -0.4254 | 706 | 706 |
| block_end | end | 70% | linear_interpolation | 5.2253 | 6.0540 | 0.2256 | 706 | 706 |
| block_end | end | 70% | random_forest | 5.9896 | 7.5376 | -0.2005 | 706 | 706 |
| block_end | end | 70% | spline_interpolation | 13.5750 | 16.3927 | -4.6782 | 706 | 706 |
| block_end | end | 70% | time_interpolation | 5.2253 | 6.0540 | 0.2256 | 706 | 706 |
| block_end | end | 80% | cubic_interpolation | 4.0472 | 5.7523 | 0.2535 | 806 | 806 |
| block_end | end | 80% | decision_tree | 5.5063 | 6.8896 | -0.0708 | 806 | 806 |
| block_end | end | 80% | forward_fill | 5.5918 | 7.8095 | -0.3759 | 806 | 806 |
| block_end | end | 80% | knn | 5.5218 | 7.2594 | -0.1889 | 806 | 806 |
| block_end | end | 80% | linear_interpolation | 4.4828 | 5.4898 | 0.3201 | 806 | 806 |
| block_end | end | 80% | random_forest | 5.5398 | 7.5897 | -0.2995 | 806 | 806 |
| block_end | end | 80% | spline_interpolation | 4.4920 | 6.4914 | 0.0494 | 806 | 806 |
| block_end | end | 80% | time_interpolation | 4.4828 | 5.4898 | 0.3201 | 806 | 806 |
| block_middle | middle | 10% | cubic_interpolation | 0.8615 | 1.0260 | -9.4641 | 101 | 101 |
| block_middle | middle | 10% | decision_tree | 1.7562 | 1.8873 | -34.4083 | 101 | 101 |
| block_middle | middle | 10% | forward_fill | 0.6767 | 0.7474 | -4.5524 | 101 | 101 |
| block_middle | middle | 10% | knn | 3.5129 | 4.0007 | -158.1061 | 101 | 101 |
| block_middle | middle | 10% | linear_interpolation | 0.4913 | 0.5870 | -2.4255 | 101 | 101 |
| block_middle | middle | 10% | random_forest | 1.4109 | 1.4461 | -19.7880 | 101 | 101 |
| block_middle | middle | 10% | spline_interpolation | 0.8615 | 1.0260 | -9.4641 | 101 | 101 |
| block_middle | middle | 10% | time_interpolation | 0.4913 | 0.5870 | -2.4255 | 101 | 101 |
| block_middle | middle | 20% | cubic_interpolation | 1.3420 | 1.5821 | -4.3600 | 202 | 202 |
| block_middle | middle | 20% | decision_tree | 1.3539 | 1.4459 | -3.4771 | 202 | 202 |
| block_middle | middle | 20% | forward_fill | 2.1429 | 2.2442 | -9.7854 | 202 | 202 |
| block_middle | middle | 20% | knn | 5.3844 | 6.5678 | -91.3706 | 202 | 202 |
| block_middle | middle | 20% | linear_interpolation | 1.1449 | 1.2988 | -2.6120 | 202 | 202 |
| block_middle | middle | 20% | random_forest | 2.0892 | 2.1888 | -9.2589 | 202 | 202 |
| block_middle | middle | 20% | spline_interpolation | 1.3420 | 1.5821 | -4.3600 | 202 | 202 |
| block_middle | middle | 20% | time_interpolation | 1.1449 | 1.2988 | -2.6120 | 202 | 202 |
| block_middle | middle | 30% | cubic_interpolation | 3.9194 | 4.8003 | -13.3868 | 302 | 302 |
| block_middle | middle | 30% | decision_tree | 4.6283 | 4.8847 | -13.8973 | 302 | 302 |
| block_middle | middle | 30% | forward_fill | 5.9705 | 6.1031 | -22.2562 | 302 | 302 |
| block_middle | middle | 30% | knn | 6.5494 | 7.9183 | -38.1467 | 302 | 302 |
| block_middle | middle | 30% | linear_interpolation | 4.0555 | 4.3002 | -10.5455 | 302 | 302 |
| block_middle | middle | 30% | random_forest | 5.1650 | 5.3134 | -16.6271 | 302 | 302 |
| block_middle | middle | 30% | spline_interpolation | 3.9194 | 4.8003 | -13.3868 | 302 | 302 |
| block_middle | middle | 30% | time_interpolation | 4.0555 | 4.3002 | -10.5455 | 302 | 302 |
| block_middle | middle | 40% | cubic_interpolation | 9.9783 | 11.0953 | -16.3760 | 403 | 403 |
| block_middle | middle | 40% | decision_tree | 7.4715 | 7.9315 | -7.8793 | 403 | 403 |
| block_middle | middle | 40% | forward_fill | 3.6737 | 4.0426 | -1.3067 | 403 | 403 |
| block_middle | middle | 40% | knn | 6.8407 | 8.2296 | -8.5592 | 403 | 403 |
| block_middle | middle | 40% | linear_interpolation | 5.3133 | 5.8414 | -3.8162 | 403 | 403 |
| block_middle | middle | 40% | random_forest | 2.7545 | 3.0057 | -0.2751 | 403 | 403 |
| block_middle | middle | 40% | spline_interpolation | 9.9783 | 11.0953 | -16.3760 | 403 | 403 |
| block_middle | middle | 40% | time_interpolation | 5.3133 | 5.8414 | -3.8162 | 403 | 403 |
| block_middle | middle | 50% | cubic_interpolation | 1.2192 | 1.7261 | 0.7966 | 504 | 504 |
| block_middle | middle | 50% | decision_tree | 11.3762 | 11.9797 | -8.7979 | 504 | 504 |
| block_middle | middle | 50% | forward_fill | 2.8546 | 4.1145 | -0.1558 | 504 | 504 |
| block_middle | middle | 50% | knn | 7.3239 | 9.5087 | -5.1729 | 504 | 504 |
| block_middle | middle | 50% | linear_interpolation | 5.4614 | 6.3855 | -1.7838 | 504 | 504 |
| block_middle | middle | 50% | random_forest | 2.8978 | 4.2895 | -0.2562 | 504 | 504 |
| block_middle | middle | 50% | spline_interpolation | 1.2192 | 1.7261 | 0.7966 | 504 | 504 |
| block_middle | middle | 50% | time_interpolation | 5.4614 | 6.3855 | -1.7838 | 504 | 504 |
| block_middle | middle | 60% | cubic_interpolation | 4.3577 | 5.3804 | -0.3936 | 605 | 605 |
| block_middle | middle | 60% | decision_tree | 7.6090 | 8.3067 | -2.3217 | 605 | 605 |
| block_middle | middle | 60% | forward_fill | 3.3930 | 4.7624 | -0.0919 | 605 | 605 |
| block_middle | middle | 60% | knn | 7.2402 | 9.5580 | -3.3979 | 605 | 605 |
| block_middle | middle | 60% | linear_interpolation | 4.0808 | 4.7870 | -0.1031 | 605 | 605 |
| block_middle | middle | 60% | random_forest | 3.4830 | 4.6429 | -0.0378 | 605 | 605 |
| block_middle | middle | 60% | spline_interpolation | 4.3577 | 5.3804 | -0.3936 | 605 | 605 |
| block_middle | middle | 60% | time_interpolation | 4.0808 | 4.7870 | -0.1031 | 605 | 605 |
| block_middle | middle | 70% | cubic_interpolation | 12.3579 | 13.6447 | -5.8872 | 706 | 706 |
| block_middle | middle | 70% | decision_tree | 14.7660 | 15.6544 | -8.0654 | 706 | 706 |
| block_middle | middle | 70% | forward_fill | 3.8792 | 5.4544 | -0.1006 | 706 | 706 |
| block_middle | middle | 70% | knn | 6.5564 | 8.8730 | -1.9124 | 706 | 706 |
| block_middle | middle | 70% | linear_interpolation | 6.6070 | 7.9146 | -1.3173 | 706 | 706 |
| block_middle | middle | 70% | random_forest | 3.8917 | 5.4297 | -0.0906 | 706 | 706 |
| block_middle | middle | 70% | spline_interpolation | 12.3579 | 13.6447 | -5.8872 | 706 | 706 |
| block_middle | middle | 70% | time_interpolation | 6.6070 | 7.9146 | -1.3173 | 706 | 706 |
| block_middle | middle | 80% | cubic_interpolation | 7.6603 | 8.9431 | -1.0885 | 806 | 806 |
| block_middle | middle | 80% | decision_tree | 15.4217 | 16.6105 | -6.2049 | 806 | 806 |
| block_middle | middle | 80% | forward_fill | 4.6316 | 6.3931 | -0.0673 | 806 | 806 |
| block_middle | middle | 80% | knn | 5.9011 | 7.1825 | -0.3471 | 806 | 806 |
| block_middle | middle | 80% | linear_interpolation | 6.8624 | 8.2591 | -0.7813 | 806 | 806 |
| block_middle | middle | 80% | random_forest | 4.6382 | 6.3858 | -0.0648 | 806 | 806 |
| block_middle | middle | 80% | spline_interpolation | 7.6603 | 8.9431 | -1.0885 | 806 | 806 |
| block_middle | middle | 80% | time_interpolation | 6.8624 | 8.2591 | -0.7813 | 806 | 806 |
| block_start | start | 10% | cubic_interpolation | 1.1022 | 1.2203 | 0.2573 | 101 | 101 |
| block_start | start | 10% | decision_tree | 3.0884 | 3.2330 | -4.2136 | 101 | 101 |
| block_start | start | 10% | forward_fill | 1.2386 | 1.4759 | -0.0865 | 101 | 101 |
| block_start | start | 10% | knn | 3.6896 | 3.8251 | -6.2981 | 101 | 101 |
| block_start | start | 10% | linear_interpolation | 0.9636 | 1.2281 | 0.2477 | 101 | 101 |
| block_start | start | 10% | random_forest | 2.9422 | 3.2652 | -4.3177 | 101 | 101 |
| block_start | start | 10% | spline_interpolation | 1.0886 | 1.3436 | 0.0996 | 101 | 101 |
| block_start | start | 10% | time_interpolation | 0.9636 | 1.2281 | 0.2477 | 101 | 101 |
| block_start | start | 20% | cubic_interpolation | 1.6762 | 1.7713 | 0.0624 | 202 | 202 |
| block_start | start | 20% | decision_tree | 2.1274 | 2.6818 | -1.1491 | 202 | 202 |
| block_start | start | 20% | forward_fill | 2.3393 | 2.6579 | -1.1111 | 202 | 202 |
| block_start | start | 20% | knn | 2.3690 | 2.7151 | -1.2029 | 202 | 202 |
| block_start | start | 20% | linear_interpolation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| block_start | start | 20% | random_forest | 1.9660 | 2.5405 | -0.9287 | 202 | 202 |
| block_start | start | 20% | spline_interpolation | 2.1933 | 2.3259 | -0.6166 | 202 | 202 |
| block_start | start | 20% | time_interpolation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| block_start | start | 30% | cubic_interpolation | 5.8913 | 6.8477 | -10.7939 | 302 | 302 |
| block_start | start | 30% | decision_tree | 2.2223 | 2.4596 | -0.5216 | 302 | 302 |
| block_start | start | 30% | forward_fill | 3.0183 | 3.3915 | -1.8930 | 302 | 302 |
| block_start | start | 30% | knn | 2.1096 | 2.6192 | -0.7254 | 302 | 302 |
| block_start | start | 30% | linear_interpolation | 2.1272 | 2.3947 | -0.4423 | 302 | 302 |
| block_start | start | 30% | random_forest | 2.6217 | 2.9311 | -1.1610 | 302 | 302 |
| block_start | start | 30% | spline_interpolation | 7.7047 | 8.7130 | -18.0946 | 302 | 302 |
| block_start | start | 30% | time_interpolation | 2.1272 | 2.3947 | -0.4423 | 302 | 302 |
| block_start | start | 40% | cubic_interpolation | 7.2939 | 8.5596 | -14.5553 | 403 | 403 |
| block_start | start | 40% | decision_tree | 1.7834 | 2.1787 | -0.0078 | 403 | 403 |
| block_start | start | 40% | forward_fill | 2.9323 | 3.3907 | -1.4409 | 403 | 403 |
| block_start | start | 40% | knn | 3.7309 | 4.4225 | -3.1524 | 403 | 403 |
| block_start | start | 40% | linear_interpolation | 1.8038 | 2.1093 | 0.0554 | 403 | 403 |
| block_start | start | 40% | random_forest | 1.8653 | 2.1825 | -0.0113 | 403 | 403 |
| block_start | start | 40% | spline_interpolation | 10.6173 | 12.0995 | -30.0816 | 403 | 403 |
| block_start | start | 40% | time_interpolation | 1.8038 | 2.1093 | 0.0554 | 403 | 403 |
| block_start | start | 50% | cubic_interpolation | 1.4492 | 1.7988 | 0.4541 | 504 | 504 |
| block_start | start | 50% | decision_tree | 2.5220 | 3.2788 | -0.8136 | 504 | 504 |
| block_start | start | 50% | forward_fill | 3.5791 | 4.1150 | -1.8567 | 504 | 504 |
| block_start | start | 50% | knn | 3.0347 | 3.6581 | -1.2575 | 504 | 504 |
| block_start | start | 50% | linear_interpolation | 1.4386 | 1.9513 | 0.3576 | 504 | 504 |
| block_start | start | 50% | random_forest | 2.1421 | 2.5204 | -0.0717 | 504 | 504 |
| block_start | start | 50% | spline_interpolation | 1.8363 | 2.2186 | 0.1696 | 504 | 504 |
| block_start | start | 50% | time_interpolation | 1.4386 | 1.9513 | 0.3576 | 504 | 504 |
| block_start | start | 60% | cubic_interpolation | 1.5243 | 1.8189 | 0.4898 | 605 | 605 |
| block_start | start | 60% | decision_tree | 3.0477 | 3.7020 | -1.1134 | 605 | 605 |
| block_start | start | 60% | forward_fill | 4.0896 | 4.6341 | -2.3116 | 605 | 605 |
| block_start | start | 60% | knn | 5.2965 | 6.2930 | -5.1070 | 605 | 605 |
| block_start | start | 60% | linear_interpolation | 1.5972 | 1.8882 | 0.4502 | 605 | 605 |
| block_start | start | 60% | random_forest | 3.5368 | 4.0132 | -1.4837 | 605 | 605 |
| block_start | start | 60% | spline_interpolation | 1.6913 | 1.9643 | 0.4050 | 605 | 605 |
| block_start | start | 60% | time_interpolation | 1.5972 | 1.8882 | 0.4502 | 605 | 605 |
| block_start | start | 70% | cubic_interpolation | 3.5094 | 4.7387 | -2.3956 | 706 | 706 |
| block_start | start | 70% | decision_tree | 5.5201 | 6.0777 | -4.5857 | 706 | 706 |
| block_start | start | 70% | forward_fill | 3.9994 | 4.5389 | -2.1154 | 706 | 706 |
| block_start | start | 70% | knn | 10.4015 | 10.8611 | -16.8381 | 706 | 706 |
| block_start | start | 70% | linear_interpolation | 5.1465 | 5.8430 | -4.1626 | 706 | 706 |
| block_start | start | 70% | random_forest | 6.2160 | 6.7149 | -5.8183 | 706 | 706 |
| block_start | start | 70% | spline_interpolation | 7.4183 | 8.8242 | -10.7748 | 706 | 706 |
| block_start | start | 70% | time_interpolation | 5.1465 | 5.8430 | -4.1626 | 706 | 706 |
| block_start | start | 80% | cubic_interpolation | 23.7657 | 27.8532 | -45.7205 | 806 | 806 |
| block_start | start | 80% | decision_tree | 6.3137 | 6.8921 | -1.8607 | 806 | 806 |
| block_start | start | 80% | forward_fill | 4.2559 | 4.7930 | -0.3835 | 806 | 806 |
| block_start | start | 80% | knn | 13.2312 | 14.0470 | -10.8830 | 806 | 806 |
| block_start | start | 80% | linear_interpolation | 5.2599 | 6.0752 | -1.2227 | 806 | 806 |
| block_start | start | 80% | random_forest | 6.1285 | 6.7067 | -1.7088 | 806 | 806 |
| block_start | start | 80% | spline_interpolation | 32.9873 | 36.9107 | -81.0472 | 806 | 806 |
| block_start | start | 80% | time_interpolation | 5.2599 | 6.0752 | -1.2227 | 806 | 806 |
| random | none | 10% | cubic_interpolation | 0.0472 | 0.0829 | 0.9998 | 101 | 101 |
| random | none | 10% | decision_tree | 0.5146 | 0.7248 | 0.9845 | 101 | 101 |
| random | none | 10% | forward_fill | 0.1587 | 0.2867 | 0.9976 | 101 | 101 |
| random | none | 10% | knn | 0.1668 | 0.2770 | 0.9977 | 101 | 101 |
| random | none | 10% | linear_interpolation | 0.0626 | 0.0983 | 0.9997 | 101 | 101 |
| random | none | 10% | random_forest | 0.6229 | 0.8123 | 0.9806 | 101 | 101 |
| random | none | 10% | spline_interpolation | 0.0470 | 0.0828 | 0.9998 | 101 | 101 |
| random | none | 10% | time_interpolation | 0.0626 | 0.0983 | 0.9997 | 101 | 101 |
| random | none | 20% | cubic_interpolation | 0.0635 | 0.1052 | 0.9997 | 202 | 202 |
| random | none | 20% | decision_tree | 0.5546 | 0.7300 | 0.9855 | 202 | 202 |
| random | none | 20% | forward_fill | 0.1635 | 0.2588 | 0.9982 | 202 | 202 |
| random | none | 20% | knn | 0.1573 | 0.2641 | 0.9981 | 202 | 202 |
| random | none | 20% | linear_interpolation | 0.0730 | 0.1185 | 0.9996 | 202 | 202 |
| random | none | 20% | random_forest | 0.7003 | 0.9443 | 0.9758 | 202 | 202 |
| random | none | 20% | spline_interpolation | 0.0635 | 0.1052 | 0.9997 | 202 | 202 |
| random | none | 20% | time_interpolation | 0.0730 | 0.1185 | 0.9996 | 202 | 202 |
| random | none | 30% | cubic_interpolation | 0.0879 | 0.1789 | 0.9991 | 302 | 302 |
| random | none | 30% | decision_tree | 0.5385 | 0.6956 | 0.9866 | 302 | 302 |
| random | none | 30% | forward_fill | 0.1820 | 0.2989 | 0.9975 | 302 | 302 |
| random | none | 30% | knn | 0.1719 | 0.2838 | 0.9978 | 302 | 302 |
| random | none | 30% | linear_interpolation | 0.0834 | 0.1401 | 0.9995 | 302 | 302 |
| random | none | 30% | random_forest | 0.7200 | 0.9390 | 0.9756 | 302 | 302 |
| random | none | 30% | spline_interpolation | 0.0879 | 0.1789 | 0.9991 | 302 | 302 |
| random | none | 30% | time_interpolation | 0.0834 | 0.1401 | 0.9995 | 302 | 302 |
| random | none | 40% | cubic_interpolation | 0.0909 | 0.1726 | 0.9992 | 403 | 403 |
| random | none | 40% | decision_tree | 0.5749 | 0.7864 | 0.9827 | 403 | 403 |
| random | none | 40% | forward_fill | 0.2157 | 0.3499 | 0.9966 | 403 | 403 |
| random | none | 40% | knn | 0.2044 | 0.3206 | 0.9971 | 403 | 403 |
| random | none | 40% | linear_interpolation | 0.0950 | 0.1596 | 0.9993 | 403 | 403 |
| random | none | 40% | random_forest | 0.7380 | 1.0012 | 0.9719 | 403 | 403 |
| random | none | 40% | spline_interpolation | 0.0908 | 0.1724 | 0.9992 | 403 | 403 |
| random | none | 40% | time_interpolation | 0.0950 | 0.1596 | 0.9993 | 403 | 403 |
| random | none | 50% | cubic_interpolation | 0.0998 | 0.2110 | 0.9988 | 504 | 504 |
| random | none | 50% | decision_tree | 0.6088 | 0.8548 | 0.9797 | 504 | 504 |
| random | none | 50% | forward_fill | 0.2415 | 0.3979 | 0.9956 | 504 | 504 |
| random | none | 50% | knn | 0.3731 | 0.9634 | 0.9742 | 504 | 504 |
| random | none | 50% | linear_interpolation | 0.1020 | 0.1809 | 0.9991 | 504 | 504 |
| random | none | 50% | random_forest | 0.8259 | 1.0885 | 0.9670 | 504 | 504 |
| random | none | 50% | spline_interpolation | 0.0997 | 0.2109 | 0.9988 | 504 | 504 |
| random | none | 50% | time_interpolation | 0.1020 | 0.1809 | 0.9991 | 504 | 504 |
| random | none | 60% | cubic_interpolation | 0.1230 | 0.2369 | 0.9985 | 605 | 605 |
| random | none | 60% | decision_tree | 0.7182 | 1.0240 | 0.9714 | 605 | 605 |
| random | none | 60% | forward_fill | 0.2741 | 0.4235 | 0.9951 | 605 | 605 |
| random | none | 60% | knn | 0.4981 | 1.1123 | 0.9663 | 605 | 605 |
| random | none | 60% | linear_interpolation | 0.1276 | 0.2484 | 0.9983 | 605 | 605 |
| random | none | 60% | random_forest | 0.7644 | 0.9842 | 0.9736 | 605 | 605 |
| random | none | 60% | spline_interpolation | 0.1232 | 0.2371 | 0.9985 | 605 | 605 |
| random | none | 60% | time_interpolation | 0.1276 | 0.2484 | 0.9983 | 605 | 605 |
| random | none | 70% | cubic_interpolation | 0.2138 | 0.4691 | 0.9941 | 706 | 706 |
| random | none | 70% | decision_tree | 0.6636 | 0.9730 | 0.9748 | 706 | 706 |
| random | none | 70% | forward_fill | 0.4076 | 0.7183 | 0.9863 | 706 | 706 |
| random | none | 70% | knn | 1.1861 | 3.1064 | 0.7432 | 706 | 706 |
| random | none | 70% | linear_interpolation | 0.1774 | 0.3320 | 0.9971 | 706 | 706 |
| random | none | 70% | random_forest | 0.8077 | 1.1028 | 0.9676 | 706 | 706 |
| random | none | 70% | spline_interpolation | 0.2140 | 0.4692 | 0.9941 | 706 | 706 |
| random | none | 70% | time_interpolation | 0.1774 | 0.3320 | 0.9971 | 706 | 706 |
| random | none | 80% | cubic_interpolation | 0.1939 | 0.3446 | 0.9968 | 806 | 806 |
| random | none | 80% | decision_tree | 0.6881 | 0.9997 | 0.9733 | 806 | 806 |
| random | none | 80% | forward_fill | 0.5416 | 0.9838 | 0.9741 | 806 | 806 |
| random | none | 80% | knn | 1.5467 | 3.4818 | 0.6762 | 806 | 806 |
| random | none | 80% | linear_interpolation | 0.1785 | 0.3145 | 0.9974 | 806 | 806 |
| random | none | 80% | random_forest | 0.9121 | 1.2356 | 0.9592 | 806 | 806 |
| random | none | 80% | spline_interpolation | 0.1936 | 0.3443 | 0.9968 | 806 | 806 |
| random | none | 80% | time_interpolation | 0.1785 | 0.3145 | 0.9974 | 806 | 806 |

---

## Random missing (`random`)

### Random missing — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | spline_interpolation | 0.0470 | 0.0828 | 0.9998 | 101 | 101 |
| 10% | cubic_interpolation | 0.0472 | 0.0829 | 0.9998 | 101 | 101 |
| 10% | linear_interpolation | 0.0626 | 0.0983 | 0.9997 | 101 | 101 |
| 10% | time_interpolation | 0.0626 | 0.0983 | 0.9997 | 101 | 101 |
| 10% | forward_fill | 0.1587 | 0.2867 | 0.9976 | 101 | 101 |
| 10% | knn | 0.1668 | 0.2770 | 0.9977 | 101 | 101 |
| 10% | decision_tree | 0.5146 | 0.7248 | 0.9845 | 101 | 101 |
| 10% | random_forest | 0.6229 | 0.8123 | 0.9806 | 101 | 101 |
| 20% | spline_interpolation | 0.0635 | 0.1052 | 0.9997 | 202 | 202 |
| 20% | cubic_interpolation | 0.0635 | 0.1052 | 0.9997 | 202 | 202 |
| 20% | linear_interpolation | 0.0730 | 0.1185 | 0.9996 | 202 | 202 |
| 20% | time_interpolation | 0.0730 | 0.1185 | 0.9996 | 202 | 202 |
| 20% | knn | 0.1573 | 0.2641 | 0.9981 | 202 | 202 |
| 20% | forward_fill | 0.1635 | 0.2588 | 0.9982 | 202 | 202 |
| 20% | decision_tree | 0.5546 | 0.7300 | 0.9855 | 202 | 202 |
| 20% | random_forest | 0.7003 | 0.9443 | 0.9758 | 202 | 202 |
| 30% | linear_interpolation | 0.0834 | 0.1401 | 0.9995 | 302 | 302 |
| 30% | time_interpolation | 0.0834 | 0.1401 | 0.9995 | 302 | 302 |
| 30% | spline_interpolation | 0.0879 | 0.1789 | 0.9991 | 302 | 302 |
| 30% | cubic_interpolation | 0.0879 | 0.1789 | 0.9991 | 302 | 302 |
| 30% | knn | 0.1719 | 0.2838 | 0.9978 | 302 | 302 |
| 30% | forward_fill | 0.1820 | 0.2989 | 0.9975 | 302 | 302 |
| 30% | decision_tree | 0.5385 | 0.6956 | 0.9866 | 302 | 302 |
| 30% | random_forest | 0.7200 | 0.9390 | 0.9756 | 302 | 302 |
| 40% | spline_interpolation | 0.0908 | 0.1724 | 0.9992 | 403 | 403 |
| 40% | cubic_interpolation | 0.0909 | 0.1726 | 0.9992 | 403 | 403 |
| 40% | linear_interpolation | 0.0950 | 0.1596 | 0.9993 | 403 | 403 |
| 40% | time_interpolation | 0.0950 | 0.1596 | 0.9993 | 403 | 403 |
| 40% | knn | 0.2044 | 0.3206 | 0.9971 | 403 | 403 |
| 40% | forward_fill | 0.2157 | 0.3499 | 0.9966 | 403 | 403 |
| 40% | decision_tree | 0.5749 | 0.7864 | 0.9827 | 403 | 403 |
| 40% | random_forest | 0.7380 | 1.0012 | 0.9719 | 403 | 403 |
| 50% | spline_interpolation | 0.0997 | 0.2109 | 0.9988 | 504 | 504 |
| 50% | cubic_interpolation | 0.0998 | 0.2110 | 0.9988 | 504 | 504 |
| 50% | linear_interpolation | 0.1020 | 0.1809 | 0.9991 | 504 | 504 |
| 50% | time_interpolation | 0.1020 | 0.1809 | 0.9991 | 504 | 504 |
| 50% | forward_fill | 0.2415 | 0.3979 | 0.9956 | 504 | 504 |
| 50% | knn | 0.3731 | 0.9634 | 0.9742 | 504 | 504 |
| 50% | decision_tree | 0.6088 | 0.8548 | 0.9797 | 504 | 504 |
| 50% | random_forest | 0.8259 | 1.0885 | 0.9670 | 504 | 504 |
| 60% | cubic_interpolation | 0.1230 | 0.2369 | 0.9985 | 605 | 605 |
| 60% | spline_interpolation | 0.1232 | 0.2371 | 0.9985 | 605 | 605 |
| 60% | linear_interpolation | 0.1276 | 0.2484 | 0.9983 | 605 | 605 |
| 60% | time_interpolation | 0.1276 | 0.2484 | 0.9983 | 605 | 605 |
| 60% | forward_fill | 0.2741 | 0.4235 | 0.9951 | 605 | 605 |
| 60% | knn | 0.4981 | 1.1123 | 0.9663 | 605 | 605 |
| 60% | decision_tree | 0.7182 | 1.0240 | 0.9714 | 605 | 605 |
| 60% | random_forest | 0.7644 | 0.9842 | 0.9736 | 605 | 605 |
| 70% | linear_interpolation | 0.1774 | 0.3320 | 0.9971 | 706 | 706 |
| 70% | time_interpolation | 0.1774 | 0.3320 | 0.9971 | 706 | 706 |
| 70% | cubic_interpolation | 0.2138 | 0.4691 | 0.9941 | 706 | 706 |
| 70% | spline_interpolation | 0.2140 | 0.4692 | 0.9941 | 706 | 706 |
| 70% | forward_fill | 0.4076 | 0.7183 | 0.9863 | 706 | 706 |
| 70% | decision_tree | 0.6636 | 0.9730 | 0.9748 | 706 | 706 |
| 70% | random_forest | 0.8077 | 1.1028 | 0.9676 | 706 | 706 |
| 70% | knn | 1.1861 | 3.1064 | 0.7432 | 706 | 706 |
| 80% | linear_interpolation | 0.1785 | 0.3145 | 0.9974 | 806 | 806 |
| 80% | time_interpolation | 0.1785 | 0.3145 | 0.9974 | 806 | 806 |
| 80% | spline_interpolation | 0.1936 | 0.3443 | 0.9968 | 806 | 806 |
| 80% | cubic_interpolation | 0.1939 | 0.3446 | 0.9968 | 806 | 806 |
| 80% | forward_fill | 0.5416 | 0.9838 | 0.9741 | 806 | 806 |
| 80% | decision_tree | 0.6881 | 0.9997 | 0.9733 | 806 | 806 |
| 80% | random_forest | 0.9121 | 1.2356 | 0.9592 | 806 | 806 |
| 80% | knn | 1.5467 | 3.4818 | 0.6762 | 806 | 806 |

### Random missing — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.1587 | 0.1635 | 0.1820 | 0.2157 | 0.2415 | 0.2741 | 0.4076 | 0.5416 |
| linear_interpolation | 0.0626 | 0.0730 | 0.0834 | 0.0950 | 0.1020 | 0.1276 | 0.1774 | 0.1785 |
| time_interpolation | 0.0626 | 0.0730 | 0.0834 | 0.0950 | 0.1020 | 0.1276 | 0.1774 | 0.1785 |
| cubic_interpolation | 0.0472 | 0.0635 | 0.0879 | 0.0909 | 0.0998 | 0.1230 | 0.2138 | 0.1939 |
| spline_interpolation | 0.0470 | 0.0635 | 0.0879 | 0.0908 | 0.0997 | 0.1232 | 0.2140 | 0.1936 |
| knn | 0.1668 | 0.1573 | 0.1719 | 0.2044 | 0.3731 | 0.4981 | 1.1861 | 1.5467 |
| decision_tree | 0.5146 | 0.5546 | 0.5385 | 0.5749 | 0.6088 | 0.7182 | 0.6636 | 0.6881 |
| random_forest | 0.6229 | 0.7003 | 0.7200 | 0.7380 | 0.8259 | 0.7644 | 0.8077 | 0.9121 |

### Random missing — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.2867 | 0.2588 | 0.2989 | 0.3499 | 0.3979 | 0.4235 | 0.7183 | 0.9838 |
| linear_interpolation | 0.0983 | 0.1185 | 0.1401 | 0.1596 | 0.1809 | 0.2484 | 0.3320 | 0.3145 |
| time_interpolation | 0.0983 | 0.1185 | 0.1401 | 0.1596 | 0.1809 | 0.2484 | 0.3320 | 0.3145 |
| cubic_interpolation | 0.0829 | 0.1052 | 0.1789 | 0.1726 | 0.2110 | 0.2369 | 0.4691 | 0.3446 |
| spline_interpolation | 0.0828 | 0.1052 | 0.1789 | 0.1724 | 0.2109 | 0.2371 | 0.4692 | 0.3443 |
| knn | 0.2770 | 0.2641 | 0.2838 | 0.3206 | 0.9634 | 1.1123 | 3.1064 | 3.4818 |
| decision_tree | 0.7248 | 0.7300 | 0.6956 | 0.7864 | 0.8548 | 1.0240 | 0.9730 | 0.9997 |
| random_forest | 0.8123 | 0.9443 | 0.9390 | 1.0012 | 1.0885 | 0.9842 | 1.1028 | 1.2356 |

### Random missing — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.9976 | 0.9982 | 0.9975 | 0.9966 | 0.9956 | 0.9951 | 0.9863 | 0.9741 |
| linear_interpolation | 0.9997 | 0.9996 | 0.9995 | 0.9993 | 0.9991 | 0.9983 | 0.9971 | 0.9974 |
| time_interpolation | 0.9997 | 0.9996 | 0.9995 | 0.9993 | 0.9991 | 0.9983 | 0.9971 | 0.9974 |
| cubic_interpolation | 0.9998 | 0.9997 | 0.9991 | 0.9992 | 0.9988 | 0.9985 | 0.9941 | 0.9968 |
| spline_interpolation | 0.9998 | 0.9997 | 0.9991 | 0.9992 | 0.9988 | 0.9985 | 0.9941 | 0.9968 |
| knn | 0.9977 | 0.9981 | 0.9978 | 0.9971 | 0.9742 | 0.9663 | 0.7432 | 0.6762 |
| decision_tree | 0.9845 | 0.9855 | 0.9866 | 0.9827 | 0.9797 | 0.9714 | 0.9748 | 0.9733 |
| random_forest | 0.9806 | 0.9758 | 0.9756 | 0.9719 | 0.9670 | 0.9736 | 0.9676 | 0.9592 |

---

## Block missing (`block`)

### Block missing — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | linear_interpolation | 1.0285 | 1.1880 | -1.6311 | 101 | 101 |
| 10% | time_interpolation | 1.0285 | 1.1880 | -1.6311 | 101 | 101 |
| 10% | cubic_interpolation | 1.1604 | 1.3978 | -2.6421 | 101 | 101 |
| 10% | spline_interpolation | 1.1604 | 1.3978 | -2.6421 | 101 | 101 |
| 10% | forward_fill | 1.5435 | 1.7084 | -4.4409 | 101 | 101 |
| 10% | random_forest | 1.8446 | 1.9509 | -6.0949 | 101 | 101 |
| 10% | knn | 2.6173 | 3.0283 | -16.0955 | 101 | 101 |
| 10% | decision_tree | 2.9869 | 3.1589 | -17.6018 | 101 | 101 |
| 20% | linear_interpolation | 1.4765 | 1.6968 | -2.6787 | 202 | 202 |
| 20% | time_interpolation | 1.4765 | 1.6968 | -2.6787 | 202 | 202 |
| 20% | forward_fill | 1.6054 | 1.8330 | -3.2929 | 202 | 202 |
| 20% | decision_tree | 2.0627 | 2.2444 | -5.4362 | 202 | 202 |
| 20% | knn | 2.1354 | 2.5753 | -7.4734 | 202 | 202 |
| 20% | random_forest | 2.4682 | 2.6161 | -7.7439 | 202 | 202 |
| 20% | cubic_interpolation | 4.2442 | 5.0983 | -32.2091 | 202 | 202 |
| 20% | spline_interpolation | 4.2442 | 5.0983 | -32.2091 | 202 | 202 |
| 30% | linear_interpolation | 3.4286 | 4.0453 | 0.3980 | 302 | 302 |
| 30% | time_interpolation | 3.4286 | 4.0453 | 0.3980 | 302 | 302 |
| 30% | random_forest | 3.9860 | 6.0331 | -0.3389 | 302 | 302 |
| 30% | forward_fill | 4.1018 | 6.5393 | -0.5729 | 302 | 302 |
| 30% | knn | 5.7174 | 6.9792 | -0.7917 | 302 | 302 |
| 30% | cubic_interpolation | 7.7599 | 9.5520 | -2.3562 | 302 | 302 |
| 30% | spline_interpolation | 7.7599 | 9.5520 | -2.3562 | 302 | 302 |
| 30% | decision_tree | 9.7856 | 10.9263 | -3.3914 | 302 | 302 |
| 40% | linear_interpolation | 2.9308 | 3.6053 | 0.7248 | 403 | 403 |
| 40% | time_interpolation | 2.9308 | 3.6053 | 0.7248 | 403 | 403 |
| 40% | knn | 5.0333 | 6.6578 | 0.0617 | 403 | 403 |
| 40% | random_forest | 6.6848 | 9.0632 | -0.7389 | 403 | 403 |
| 40% | forward_fill | 7.3827 | 10.0695 | -1.1464 | 403 | 403 |
| 40% | decision_tree | 13.8825 | 15.4907 | -4.0798 | 403 | 403 |
| 40% | cubic_interpolation | 27.7372 | 31.8543 | -20.4801 | 403 | 403 |
| 40% | spline_interpolation | 27.7372 | 31.8543 | -20.4801 | 403 | 403 |
| 50% | linear_interpolation | 5.4362 | 7.0441 | 0.1425 | 504 | 504 |
| 50% | time_interpolation | 5.4362 | 7.0441 | 0.1425 | 504 | 504 |
| 50% | cubic_interpolation | 6.0174 | 7.4492 | 0.0410 | 504 | 504 |
| 50% | spline_interpolation | 6.0174 | 7.4492 | 0.0410 | 504 | 504 |
| 50% | decision_tree | 6.9406 | 7.6609 | -0.0143 | 504 | 504 |
| 50% | knn | 6.9655 | 8.5127 | -0.2524 | 504 | 504 |
| 50% | random_forest | 8.0585 | 10.6314 | -0.9534 | 504 | 504 |
| 50% | forward_fill | 8.2467 | 10.9793 | -1.0833 | 504 | 504 |
| 60% | linear_interpolation | 5.3499 | 6.8720 | 0.1376 | 605 | 605 |
| 60% | time_interpolation | 5.3499 | 6.8720 | 0.1376 | 605 | 605 |
| 60% | knn | 5.9034 | 7.2391 | 0.0430 | 605 | 605 |
| 60% | random_forest | 6.5787 | 7.6620 | -0.0721 | 605 | 605 |
| 60% | decision_tree | 6.6370 | 7.5778 | -0.0486 | 605 | 605 |
| 60% | forward_fill | 6.7044 | 9.1770 | -0.5379 | 605 | 605 |
| 60% | cubic_interpolation | 12.8316 | 15.8642 | -3.5960 | 605 | 605 |
| 60% | spline_interpolation | 12.8316 | 15.8642 | -3.5960 | 605 | 605 |
| 70% | forward_fill | 3.5043 | 4.8567 | -0.0586 | 706 | 706 |
| 70% | random_forest | 3.6055 | 4.7794 | -0.0252 | 706 | 706 |
| 70% | linear_interpolation | 5.7381 | 7.0407 | -1.2248 | 706 | 706 |
| 70% | time_interpolation | 5.7381 | 7.0407 | -1.2248 | 706 | 706 |
| 70% | knn | 7.3758 | 9.6727 | -3.1991 | 706 | 706 |
| 70% | cubic_interpolation | 10.1423 | 11.1737 | -4.6034 | 706 | 706 |
| 70% | spline_interpolation | 10.1423 | 11.1737 | -4.6034 | 706 | 706 |
| 70% | decision_tree | 12.6597 | 13.5111 | -7.1929 | 706 | 706 |
| 80% | linear_interpolation | 4.7975 | 6.1094 | 0.1660 | 806 | 806 |
| 80% | time_interpolation | 4.7975 | 6.1094 | 0.1660 | 806 | 806 |
| 80% | knn | 5.0900 | 6.3753 | 0.0918 | 806 | 806 |
| 80% | forward_fill | 5.3337 | 7.4566 | -0.2424 | 806 | 806 |
| 80% | random_forest | 5.3337 | 7.3957 | -0.2222 | 806 | 806 |
| 80% | decision_tree | 5.8292 | 6.6972 | -0.0022 | 806 | 806 |
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
| knn | 2.6173 | 2.1354 | 5.7174 | 5.0333 | 6.9655 | 5.9034 | 7.3758 | 5.0900 |
| decision_tree | 2.9869 | 2.0627 | 9.7856 | 13.8825 | 6.9406 | 6.6370 | 12.6597 | 5.8292 |
| random_forest | 1.8446 | 2.4682 | 3.9860 | 6.6848 | 8.0585 | 6.5787 | 3.6055 | 5.3337 |

### Block missing — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 1.7084 | 1.8330 | 6.5393 | 10.0695 | 10.9793 | 9.1770 | 4.8567 | 7.4566 |
| linear_interpolation | 1.1880 | 1.6968 | 4.0453 | 3.6053 | 7.0441 | 6.8720 | 7.0407 | 6.1094 |
| time_interpolation | 1.1880 | 1.6968 | 4.0453 | 3.6053 | 7.0441 | 6.8720 | 7.0407 | 6.1094 |
| cubic_interpolation | 1.3978 | 5.0983 | 9.5520 | 31.8543 | 7.4492 | 15.8642 | 11.1737 | 28.3087 |
| spline_interpolation | 1.3978 | 5.0983 | 9.5520 | 31.8543 | 7.4492 | 15.8642 | 11.1737 | 28.3087 |
| knn | 3.0283 | 2.5753 | 6.9792 | 6.6578 | 8.5127 | 7.2391 | 9.6727 | 6.3753 |
| decision_tree | 3.1589 | 2.2444 | 10.9263 | 15.4907 | 7.6609 | 7.5778 | 13.5111 | 6.6972 |
| random_forest | 1.9509 | 2.6161 | 6.0331 | 9.0632 | 10.6314 | 7.6620 | 4.7794 | 7.3957 |

### Block missing — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -4.4409 | -3.2929 | -0.5729 | -1.1464 | -1.0833 | -0.5379 | -0.0586 | -0.2424 |
| linear_interpolation | -1.6311 | -2.6787 | 0.3980 | 0.7248 | 0.1425 | 0.1376 | -1.2248 | 0.1660 |
| time_interpolation | -1.6311 | -2.6787 | 0.3980 | 0.7248 | 0.1425 | 0.1376 | -1.2248 | 0.1660 |
| cubic_interpolation | -2.6421 | -32.2091 | -2.3562 | -20.4801 | 0.0410 | -3.5960 | -4.6034 | -16.9062 |
| spline_interpolation | -2.6421 | -32.2091 | -2.3562 | -20.4801 | 0.0410 | -3.5960 | -4.6034 | -16.9062 |
| knn | -16.0955 | -7.4734 | -0.7917 | 0.0617 | -0.2524 | 0.0430 | -3.1991 | 0.0918 |
| decision_tree | -17.6018 | -5.4362 | -3.3914 | -4.0798 | -0.0143 | -0.0486 | -7.1929 | -0.0022 |
| random_forest | -6.0949 | -7.7439 | -0.3389 | -0.7389 | -0.9534 | -0.0721 | -0.0252 | -0.2222 |

---

## Block na početku (`block_start`)

### Block na početku — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | linear_interpolation | 0.9636 | 1.2281 | 0.2477 | 101 | 101 |
| 10% | time_interpolation | 0.9636 | 1.2281 | 0.2477 | 101 | 101 |
| 10% | spline_interpolation | 1.0886 | 1.3436 | 0.0996 | 101 | 101 |
| 10% | cubic_interpolation | 1.1022 | 1.2203 | 0.2573 | 101 | 101 |
| 10% | forward_fill | 1.2386 | 1.4759 | -0.0865 | 101 | 101 |
| 10% | random_forest | 2.9422 | 3.2652 | -4.3177 | 101 | 101 |
| 10% | decision_tree | 3.0884 | 3.2330 | -4.2136 | 101 | 101 |
| 10% | knn | 3.6896 | 3.8251 | -6.2981 | 101 | 101 |
| 20% | linear_interpolation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| 20% | time_interpolation | 0.6991 | 0.8889 | 0.7639 | 202 | 202 |
| 20% | cubic_interpolation | 1.6762 | 1.7713 | 0.0624 | 202 | 202 |
| 20% | random_forest | 1.9660 | 2.5405 | -0.9287 | 202 | 202 |
| 20% | decision_tree | 2.1274 | 2.6818 | -1.1491 | 202 | 202 |
| 20% | spline_interpolation | 2.1933 | 2.3259 | -0.6166 | 202 | 202 |
| 20% | forward_fill | 2.3393 | 2.6579 | -1.1111 | 202 | 202 |
| 20% | knn | 2.3690 | 2.7151 | -1.2029 | 202 | 202 |
| 30% | knn | 2.1096 | 2.6192 | -0.7254 | 302 | 302 |
| 30% | linear_interpolation | 2.1272 | 2.3947 | -0.4423 | 302 | 302 |
| 30% | time_interpolation | 2.1272 | 2.3947 | -0.4423 | 302 | 302 |
| 30% | decision_tree | 2.2223 | 2.4596 | -0.5216 | 302 | 302 |
| 30% | random_forest | 2.6217 | 2.9311 | -1.1610 | 302 | 302 |
| 30% | forward_fill | 3.0183 | 3.3915 | -1.8930 | 302 | 302 |
| 30% | cubic_interpolation | 5.8913 | 6.8477 | -10.7939 | 302 | 302 |
| 30% | spline_interpolation | 7.7047 | 8.7130 | -18.0946 | 302 | 302 |
| 40% | decision_tree | 1.7834 | 2.1787 | -0.0078 | 403 | 403 |
| 40% | linear_interpolation | 1.8038 | 2.1093 | 0.0554 | 403 | 403 |
| 40% | time_interpolation | 1.8038 | 2.1093 | 0.0554 | 403 | 403 |
| 40% | random_forest | 1.8653 | 2.1825 | -0.0113 | 403 | 403 |
| 40% | forward_fill | 2.9323 | 3.3907 | -1.4409 | 403 | 403 |
| 40% | knn | 3.7309 | 4.4225 | -3.1524 | 403 | 403 |
| 40% | cubic_interpolation | 7.2939 | 8.5596 | -14.5553 | 403 | 403 |
| 40% | spline_interpolation | 10.6173 | 12.0995 | -30.0816 | 403 | 403 |
| 50% | linear_interpolation | 1.4386 | 1.9513 | 0.3576 | 504 | 504 |
| 50% | time_interpolation | 1.4386 | 1.9513 | 0.3576 | 504 | 504 |
| 50% | cubic_interpolation | 1.4492 | 1.7988 | 0.4541 | 504 | 504 |
| 50% | spline_interpolation | 1.8363 | 2.2186 | 0.1696 | 504 | 504 |
| 50% | random_forest | 2.1421 | 2.5204 | -0.0717 | 504 | 504 |
| 50% | decision_tree | 2.5220 | 3.2788 | -0.8136 | 504 | 504 |
| 50% | knn | 3.0347 | 3.6581 | -1.2575 | 504 | 504 |
| 50% | forward_fill | 3.5791 | 4.1150 | -1.8567 | 504 | 504 |
| 60% | cubic_interpolation | 1.5243 | 1.8189 | 0.4898 | 605 | 605 |
| 60% | linear_interpolation | 1.5972 | 1.8882 | 0.4502 | 605 | 605 |
| 60% | time_interpolation | 1.5972 | 1.8882 | 0.4502 | 605 | 605 |
| 60% | spline_interpolation | 1.6913 | 1.9643 | 0.4050 | 605 | 605 |
| 60% | decision_tree | 3.0477 | 3.7020 | -1.1134 | 605 | 605 |
| 60% | random_forest | 3.5368 | 4.0132 | -1.4837 | 605 | 605 |
| 60% | forward_fill | 4.0896 | 4.6341 | -2.3116 | 605 | 605 |
| 60% | knn | 5.2965 | 6.2930 | -5.1070 | 605 | 605 |
| 70% | cubic_interpolation | 3.5094 | 4.7387 | -2.3956 | 706 | 706 |
| 70% | forward_fill | 3.9994 | 4.5389 | -2.1154 | 706 | 706 |
| 70% | linear_interpolation | 5.1465 | 5.8430 | -4.1626 | 706 | 706 |
| 70% | time_interpolation | 5.1465 | 5.8430 | -4.1626 | 706 | 706 |
| 70% | decision_tree | 5.5201 | 6.0777 | -4.5857 | 706 | 706 |
| 70% | random_forest | 6.2160 | 6.7149 | -5.8183 | 706 | 706 |
| 70% | spline_interpolation | 7.4183 | 8.8242 | -10.7748 | 706 | 706 |
| 70% | knn | 10.4015 | 10.8611 | -16.8381 | 706 | 706 |
| 80% | forward_fill | 4.2559 | 4.7930 | -0.3835 | 806 | 806 |
| 80% | linear_interpolation | 5.2599 | 6.0752 | -1.2227 | 806 | 806 |
| 80% | time_interpolation | 5.2599 | 6.0752 | -1.2227 | 806 | 806 |
| 80% | random_forest | 6.1285 | 6.7067 | -1.7088 | 806 | 806 |
| 80% | decision_tree | 6.3137 | 6.8921 | -1.8607 | 806 | 806 |
| 80% | knn | 13.2312 | 14.0470 | -10.8830 | 806 | 806 |
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
| knn | 3.6896 | 2.3690 | 2.1096 | 3.7309 | 3.0347 | 5.2965 | 10.4015 | 13.2312 |
| decision_tree | 3.0884 | 2.1274 | 2.2223 | 1.7834 | 2.5220 | 3.0477 | 5.5201 | 6.3137 |
| random_forest | 2.9422 | 1.9660 | 2.6217 | 1.8653 | 2.1421 | 3.5368 | 6.2160 | 6.1285 |

### Block na početku — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 1.4759 | 2.6579 | 3.3915 | 3.3907 | 4.1150 | 4.6341 | 4.5389 | 4.7930 |
| linear_interpolation | 1.2281 | 0.8889 | 2.3947 | 2.1093 | 1.9513 | 1.8882 | 5.8430 | 6.0752 |
| time_interpolation | 1.2281 | 0.8889 | 2.3947 | 2.1093 | 1.9513 | 1.8882 | 5.8430 | 6.0752 |
| cubic_interpolation | 1.2203 | 1.7713 | 6.8477 | 8.5596 | 1.7988 | 1.8189 | 4.7387 | 27.8532 |
| spline_interpolation | 1.3436 | 2.3259 | 8.7130 | 12.0995 | 2.2186 | 1.9643 | 8.8242 | 36.9107 |
| knn | 3.8251 | 2.7151 | 2.6192 | 4.4225 | 3.6581 | 6.2930 | 10.8611 | 14.0470 |
| decision_tree | 3.2330 | 2.6818 | 2.4596 | 2.1787 | 3.2788 | 3.7020 | 6.0777 | 6.8921 |
| random_forest | 3.2652 | 2.5405 | 2.9311 | 2.1825 | 2.5204 | 4.0132 | 6.7149 | 6.7067 |

### Block na početku — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -0.0865 | -1.1111 | -1.8930 | -1.4409 | -1.8567 | -2.3116 | -2.1154 | -0.3835 |
| linear_interpolation | 0.2477 | 0.7639 | -0.4423 | 0.0554 | 0.3576 | 0.4502 | -4.1626 | -1.2227 |
| time_interpolation | 0.2477 | 0.7639 | -0.4423 | 0.0554 | 0.3576 | 0.4502 | -4.1626 | -1.2227 |
| cubic_interpolation | 0.2573 | 0.0624 | -10.7939 | -14.5553 | 0.4541 | 0.4898 | -2.3956 | -45.7205 |
| spline_interpolation | 0.0996 | -0.6166 | -18.0946 | -30.0816 | 0.1696 | 0.4050 | -10.7748 | -81.0472 |
| knn | -6.2981 | -1.2029 | -0.7254 | -3.1524 | -1.2575 | -5.1070 | -16.8381 | -10.8830 |
| decision_tree | -4.2136 | -1.1491 | -0.5216 | -0.0078 | -0.8136 | -1.1134 | -4.5857 | -1.8607 |
| random_forest | -4.3177 | -0.9287 | -1.1610 | -0.0113 | -0.0717 | -1.4837 | -5.8183 | -1.7088 |

---

## Block u sredini (`block_middle`)

### Block u sredini — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | linear_interpolation | 0.4913 | 0.5870 | -2.4255 | 101 | 101 |
| 10% | time_interpolation | 0.4913 | 0.5870 | -2.4255 | 101 | 101 |
| 10% | forward_fill | 0.6767 | 0.7474 | -4.5524 | 101 | 101 |
| 10% | cubic_interpolation | 0.8615 | 1.0260 | -9.4641 | 101 | 101 |
| 10% | spline_interpolation | 0.8615 | 1.0260 | -9.4641 | 101 | 101 |
| 10% | random_forest | 1.4109 | 1.4461 | -19.7880 | 101 | 101 |
| 10% | decision_tree | 1.7562 | 1.8873 | -34.4083 | 101 | 101 |
| 10% | knn | 3.5129 | 4.0007 | -158.1061 | 101 | 101 |
| 20% | linear_interpolation | 1.1449 | 1.2988 | -2.6120 | 202 | 202 |
| 20% | time_interpolation | 1.1449 | 1.2988 | -2.6120 | 202 | 202 |
| 20% | cubic_interpolation | 1.3420 | 1.5821 | -4.3600 | 202 | 202 |
| 20% | spline_interpolation | 1.3420 | 1.5821 | -4.3600 | 202 | 202 |
| 20% | decision_tree | 1.3539 | 1.4459 | -3.4771 | 202 | 202 |
| 20% | random_forest | 2.0892 | 2.1888 | -9.2589 | 202 | 202 |
| 20% | forward_fill | 2.1429 | 2.2442 | -9.7854 | 202 | 202 |
| 20% | knn | 5.3844 | 6.5678 | -91.3706 | 202 | 202 |
| 30% | cubic_interpolation | 3.9194 | 4.8003 | -13.3868 | 302 | 302 |
| 30% | spline_interpolation | 3.9194 | 4.8003 | -13.3868 | 302 | 302 |
| 30% | linear_interpolation | 4.0555 | 4.3002 | -10.5455 | 302 | 302 |
| 30% | time_interpolation | 4.0555 | 4.3002 | -10.5455 | 302 | 302 |
| 30% | decision_tree | 4.6283 | 4.8847 | -13.8973 | 302 | 302 |
| 30% | random_forest | 5.1650 | 5.3134 | -16.6271 | 302 | 302 |
| 30% | forward_fill | 5.9705 | 6.1031 | -22.2562 | 302 | 302 |
| 30% | knn | 6.5494 | 7.9183 | -38.1467 | 302 | 302 |
| 40% | random_forest | 2.7545 | 3.0057 | -0.2751 | 403 | 403 |
| 40% | forward_fill | 3.6737 | 4.0426 | -1.3067 | 403 | 403 |
| 40% | linear_interpolation | 5.3133 | 5.8414 | -3.8162 | 403 | 403 |
| 40% | time_interpolation | 5.3133 | 5.8414 | -3.8162 | 403 | 403 |
| 40% | knn | 6.8407 | 8.2296 | -8.5592 | 403 | 403 |
| 40% | decision_tree | 7.4715 | 7.9315 | -7.8793 | 403 | 403 |
| 40% | cubic_interpolation | 9.9783 | 11.0953 | -16.3760 | 403 | 403 |
| 40% | spline_interpolation | 9.9783 | 11.0953 | -16.3760 | 403 | 403 |
| 50% | cubic_interpolation | 1.2192 | 1.7261 | 0.7966 | 504 | 504 |
| 50% | spline_interpolation | 1.2192 | 1.7261 | 0.7966 | 504 | 504 |
| 50% | forward_fill | 2.8546 | 4.1145 | -0.1558 | 504 | 504 |
| 50% | random_forest | 2.8978 | 4.2895 | -0.2562 | 504 | 504 |
| 50% | linear_interpolation | 5.4614 | 6.3855 | -1.7838 | 504 | 504 |
| 50% | time_interpolation | 5.4614 | 6.3855 | -1.7838 | 504 | 504 |
| 50% | knn | 7.3239 | 9.5087 | -5.1729 | 504 | 504 |
| 50% | decision_tree | 11.3762 | 11.9797 | -8.7979 | 504 | 504 |
| 60% | forward_fill | 3.3930 | 4.7624 | -0.0919 | 605 | 605 |
| 60% | random_forest | 3.4830 | 4.6429 | -0.0378 | 605 | 605 |
| 60% | linear_interpolation | 4.0808 | 4.7870 | -0.1031 | 605 | 605 |
| 60% | time_interpolation | 4.0808 | 4.7870 | -0.1031 | 605 | 605 |
| 60% | cubic_interpolation | 4.3577 | 5.3804 | -0.3936 | 605 | 605 |
| 60% | spline_interpolation | 4.3577 | 5.3804 | -0.3936 | 605 | 605 |
| 60% | knn | 7.2402 | 9.5580 | -3.3979 | 605 | 605 |
| 60% | decision_tree | 7.6090 | 8.3067 | -2.3217 | 605 | 605 |
| 70% | forward_fill | 3.8792 | 5.4544 | -0.1006 | 706 | 706 |
| 70% | random_forest | 3.8917 | 5.4297 | -0.0906 | 706 | 706 |
| 70% | knn | 6.5564 | 8.8730 | -1.9124 | 706 | 706 |
| 70% | linear_interpolation | 6.6070 | 7.9146 | -1.3173 | 706 | 706 |
| 70% | time_interpolation | 6.6070 | 7.9146 | -1.3173 | 706 | 706 |
| 70% | cubic_interpolation | 12.3579 | 13.6447 | -5.8872 | 706 | 706 |
| 70% | spline_interpolation | 12.3579 | 13.6447 | -5.8872 | 706 | 706 |
| 70% | decision_tree | 14.7660 | 15.6544 | -8.0654 | 706 | 706 |
| 80% | forward_fill | 4.6316 | 6.3931 | -0.0673 | 806 | 806 |
| 80% | random_forest | 4.6382 | 6.3858 | -0.0648 | 806 | 806 |
| 80% | knn | 5.9011 | 7.1825 | -0.3471 | 806 | 806 |
| 80% | linear_interpolation | 6.8624 | 8.2591 | -0.7813 | 806 | 806 |
| 80% | time_interpolation | 6.8624 | 8.2591 | -0.7813 | 806 | 806 |
| 80% | cubic_interpolation | 7.6603 | 8.9431 | -1.0885 | 806 | 806 |
| 80% | spline_interpolation | 7.6603 | 8.9431 | -1.0885 | 806 | 806 |
| 80% | decision_tree | 15.4217 | 16.6105 | -6.2049 | 806 | 806 |

### Block u sredini — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.6767 | 2.1429 | 5.9705 | 3.6737 | 2.8546 | 3.3930 | 3.8792 | 4.6316 |
| linear_interpolation | 0.4913 | 1.1449 | 4.0555 | 5.3133 | 5.4614 | 4.0808 | 6.6070 | 6.8624 |
| time_interpolation | 0.4913 | 1.1449 | 4.0555 | 5.3133 | 5.4614 | 4.0808 | 6.6070 | 6.8624 |
| cubic_interpolation | 0.8615 | 1.3420 | 3.9194 | 9.9783 | 1.2192 | 4.3577 | 12.3579 | 7.6603 |
| spline_interpolation | 0.8615 | 1.3420 | 3.9194 | 9.9783 | 1.2192 | 4.3577 | 12.3579 | 7.6603 |
| knn | 3.5129 | 5.3844 | 6.5494 | 6.8407 | 7.3239 | 7.2402 | 6.5564 | 5.9011 |
| decision_tree | 1.7562 | 1.3539 | 4.6283 | 7.4715 | 11.3762 | 7.6090 | 14.7660 | 15.4217 |
| random_forest | 1.4109 | 2.0892 | 5.1650 | 2.7545 | 2.8978 | 3.4830 | 3.8917 | 4.6382 |

### Block u sredini — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 0.7474 | 2.2442 | 6.1031 | 4.0426 | 4.1145 | 4.7624 | 5.4544 | 6.3931 |
| linear_interpolation | 0.5870 | 1.2988 | 4.3002 | 5.8414 | 6.3855 | 4.7870 | 7.9146 | 8.2591 |
| time_interpolation | 0.5870 | 1.2988 | 4.3002 | 5.8414 | 6.3855 | 4.7870 | 7.9146 | 8.2591 |
| cubic_interpolation | 1.0260 | 1.5821 | 4.8003 | 11.0953 | 1.7261 | 5.3804 | 13.6447 | 8.9431 |
| spline_interpolation | 1.0260 | 1.5821 | 4.8003 | 11.0953 | 1.7261 | 5.3804 | 13.6447 | 8.9431 |
| knn | 4.0007 | 6.5678 | 7.9183 | 8.2296 | 9.5087 | 9.5580 | 8.8730 | 7.1825 |
| decision_tree | 1.8873 | 1.4459 | 4.8847 | 7.9315 | 11.9797 | 8.3067 | 15.6544 | 16.6105 |
| random_forest | 1.4461 | 2.1888 | 5.3134 | 3.0057 | 4.2895 | 4.6429 | 5.4297 | 6.3858 |

### Block u sredini — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -4.5524 | -9.7854 | -22.2562 | -1.3067 | -0.1558 | -0.0919 | -0.1006 | -0.0673 |
| linear_interpolation | -2.4255 | -2.6120 | -10.5455 | -3.8162 | -1.7838 | -0.1031 | -1.3173 | -0.7813 |
| time_interpolation | -2.4255 | -2.6120 | -10.5455 | -3.8162 | -1.7838 | -0.1031 | -1.3173 | -0.7813 |
| cubic_interpolation | -9.4641 | -4.3600 | -13.3868 | -16.3760 | 0.7966 | -0.3936 | -5.8872 | -1.0885 |
| spline_interpolation | -9.4641 | -4.3600 | -13.3868 | -16.3760 | 0.7966 | -0.3936 | -5.8872 | -1.0885 |
| knn | -158.1061 | -91.3706 | -38.1467 | -8.5592 | -5.1729 | -3.3979 | -1.9124 | -0.3471 |
| decision_tree | -34.4083 | -3.4771 | -13.8973 | -7.8793 | -8.7979 | -2.3217 | -8.0654 | -6.2049 |
| random_forest | -19.7880 | -9.2589 | -16.6271 | -0.2751 | -0.2562 | -0.0378 | -0.0906 | -0.0648 |

---

## Block na kraju (`block_end`)

### Block na kraju — detaljno (sortirano po rateu i MAE)

| missing_rate | method | MAE | RMSE | R² | missing | evaluated |
|-------------|--------|-----|------|-----|---------|-----------|
| 10% | linear_interpolation | 3.4473 | 4.1538 | 0.3437 | 101 | 101 |
| 10% | time_interpolation | 3.4473 | 4.1538 | 0.3437 | 101 | 101 |
| 10% | cubic_interpolation | 4.9709 | 5.9253 | -0.3356 | 101 | 101 |
| 10% | spline_interpolation | 5.2391 | 6.2332 | -0.4780 | 101 | 101 |
| 10% | decision_tree | 5.8625 | 6.6532 | -0.6838 | 101 | 101 |
| 10% | knn | 5.9186 | 6.8597 | -0.7900 | 101 | 101 |
| 10% | forward_fill | 8.4606 | 9.7525 | -2.6181 | 101 | 101 |
| 10% | random_forest | 8.7605 | 10.0709 | -2.8582 | 101 | 101 |
| 20% | cubic_interpolation | 4.1828 | 4.5838 | 0.2258 | 202 | 202 |
| 20% | random_forest | 4.8834 | 5.6314 | -0.1685 | 202 | 202 |
| 20% | decision_tree | 4.9268 | 5.6425 | -0.1732 | 202 | 202 |
| 20% | knn | 5.2854 | 6.1607 | -0.3986 | 202 | 202 |
| 20% | forward_fill | 5.5124 | 6.3678 | -0.4942 | 202 | 202 |
| 20% | linear_interpolation | 5.5318 | 6.6875 | -0.6479 | 202 | 202 |
| 20% | time_interpolation | 5.5318 | 6.6875 | -0.6479 | 202 | 202 |
| 20% | spline_interpolation | 8.3969 | 8.9561 | -1.9556 | 202 | 202 |
| 30% | spline_interpolation | 4.8486 | 5.9726 | -0.7742 | 302 | 302 |
| 30% | cubic_interpolation | 5.0029 | 6.1929 | -0.9075 | 302 | 302 |
| 30% | linear_interpolation | 5.4043 | 6.5802 | -1.1535 | 302 | 302 |
| 30% | time_interpolation | 5.4043 | 6.5802 | -1.1535 | 302 | 302 |
| 30% | forward_fill | 5.4791 | 6.6979 | -1.2312 | 302 | 302 |
| 30% | decision_tree | 5.5311 | 6.7525 | -1.2678 | 302 | 302 |
| 30% | random_forest | 5.9756 | 7.2152 | -1.5892 | 302 | 302 |
| 30% | knn | 11.4994 | 12.8899 | -7.2637 | 302 | 302 |
| 40% | linear_interpolation | 6.8261 | 8.3215 | -0.8504 | 403 | 403 |
| 40% | time_interpolation | 6.8261 | 8.3215 | -0.8504 | 403 | 403 |
| 40% | decision_tree | 8.4857 | 10.0647 | -1.7068 | 403 | 403 |
| 40% | cubic_interpolation | 9.5956 | 11.1944 | -2.3486 | 403 | 403 |
| 40% | spline_interpolation | 10.3644 | 12.1292 | -2.9312 | 403 | 403 |
| 40% | forward_fill | 11.0101 | 12.5944 | -3.2385 | 403 | 403 |
| 40% | knn | 11.4460 | 12.9318 | -3.4686 | 403 | 403 |
| 40% | random_forest | 11.4494 | 12.9626 | -3.4899 | 403 | 403 |
| 50% | linear_interpolation | 5.2375 | 7.0389 | 0.0246 | 504 | 504 |
| 50% | time_interpolation | 5.2375 | 7.0389 | 0.0246 | 504 | 504 |
| 50% | cubic_interpolation | 6.3027 | 8.2675 | -0.3457 | 504 | 504 |
| 50% | spline_interpolation | 6.4615 | 8.4590 | -0.4087 | 504 | 504 |
| 50% | decision_tree | 8.4771 | 10.7083 | -1.2575 | 504 | 504 |
| 50% | knn | 8.5669 | 10.8827 | -1.3316 | 504 | 504 |
| 50% | random_forest | 8.9477 | 11.3091 | -1.5179 | 504 | 504 |
| 50% | forward_fill | 9.3483 | 11.7349 | -1.7111 | 504 | 504 |
| 60% | linear_interpolation | 4.9650 | 6.0693 | 0.3007 | 605 | 605 |
| 60% | time_interpolation | 4.9650 | 6.0693 | 0.3007 | 605 | 605 |
| 60% | decision_tree | 6.7400 | 7.9274 | -0.1930 | 605 | 605 |
| 60% | forward_fill | 6.8690 | 8.9755 | -0.5293 | 605 | 605 |
| 60% | knn | 6.8733 | 8.0746 | -0.2377 | 605 | 605 |
| 60% | random_forest | 6.9570 | 8.0532 | -0.2312 | 605 | 605 |
| 60% | cubic_interpolation | 8.1166 | 9.5544 | -0.7330 | 605 | 605 |
| 60% | spline_interpolation | 10.6070 | 12.5410 | -1.9857 | 605 | 605 |
| 70% | linear_interpolation | 5.2253 | 6.0540 | 0.2256 | 706 | 706 |
| 70% | time_interpolation | 5.2253 | 6.0540 | 0.2256 | 706 | 706 |
| 70% | decision_tree | 5.8695 | 6.9267 | -0.0138 | 706 | 706 |
| 70% | forward_fill | 5.8994 | 7.2303 | -0.1047 | 706 | 706 |
| 70% | random_forest | 5.9896 | 7.5376 | -0.2005 | 706 | 706 |
| 70% | knn | 6.2982 | 8.2131 | -0.4254 | 706 | 706 |
| 70% | cubic_interpolation | 10.9486 | 13.3992 | -2.7937 | 706 | 706 |
| 70% | spline_interpolation | 13.5750 | 16.3927 | -4.6782 | 706 | 706 |
| 80% | cubic_interpolation | 4.0472 | 5.7523 | 0.2535 | 806 | 806 |
| 80% | linear_interpolation | 4.4828 | 5.4898 | 0.3201 | 806 | 806 |
| 80% | time_interpolation | 4.4828 | 5.4898 | 0.3201 | 806 | 806 |
| 80% | spline_interpolation | 4.4920 | 6.4914 | 0.0494 | 806 | 806 |
| 80% | decision_tree | 5.5063 | 6.8896 | -0.0708 | 806 | 806 |
| 80% | knn | 5.5218 | 7.2594 | -0.1889 | 806 | 806 |
| 80% | random_forest | 5.5398 | 7.5897 | -0.2995 | 806 | 806 |
| 80% | forward_fill | 5.5918 | 7.8095 | -0.3759 | 806 | 806 |

### Block na kraju — MAE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 8.4606 | 5.5124 | 5.4791 | 11.0101 | 9.3483 | 6.8690 | 5.8994 | 5.5918 |
| linear_interpolation | 3.4473 | 5.5318 | 5.4043 | 6.8261 | 5.2375 | 4.9650 | 5.2253 | 4.4828 |
| time_interpolation | 3.4473 | 5.5318 | 5.4043 | 6.8261 | 5.2375 | 4.9650 | 5.2253 | 4.4828 |
| cubic_interpolation | 4.9709 | 4.1828 | 5.0029 | 9.5956 | 6.3027 | 8.1166 | 10.9486 | 4.0472 |
| spline_interpolation | 5.2391 | 8.3969 | 4.8486 | 10.3644 | 6.4615 | 10.6070 | 13.5750 | 4.4920 |
| knn | 5.9186 | 5.2854 | 11.4994 | 11.4460 | 8.5669 | 6.8733 | 6.2982 | 5.5218 |
| decision_tree | 5.8625 | 4.9268 | 5.5311 | 8.4857 | 8.4771 | 6.7400 | 5.8695 | 5.5063 |
| random_forest | 8.7605 | 4.8834 | 5.9756 | 11.4494 | 8.9477 | 6.9570 | 5.9896 | 5.5398 |

### Block na kraju — RMSE (°C)

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | 9.7525 | 6.3678 | 6.6979 | 12.5944 | 11.7349 | 8.9755 | 7.2303 | 7.8095 |
| linear_interpolation | 4.1538 | 6.6875 | 6.5802 | 8.3215 | 7.0389 | 6.0693 | 6.0540 | 5.4898 |
| time_interpolation | 4.1538 | 6.6875 | 6.5802 | 8.3215 | 7.0389 | 6.0693 | 6.0540 | 5.4898 |
| cubic_interpolation | 5.9253 | 4.5838 | 6.1929 | 11.1944 | 8.2675 | 9.5544 | 13.3992 | 5.7523 |
| spline_interpolation | 6.2332 | 8.9561 | 5.9726 | 12.1292 | 8.4590 | 12.5410 | 16.3927 | 6.4914 |
| knn | 6.8597 | 6.1607 | 12.8899 | 12.9318 | 10.8827 | 8.0746 | 8.2131 | 7.2594 |
| decision_tree | 6.6532 | 5.6425 | 6.7525 | 10.0647 | 10.7083 | 7.9274 | 6.9267 | 6.8896 |
| random_forest | 10.0709 | 5.6314 | 7.2152 | 12.9626 | 11.3091 | 8.0532 | 7.5376 | 7.5897 |

### Block na kraju — R²

| method | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|------|------|------|------|------|------|------|------|
| forward_fill | -2.6181 | -0.4942 | -1.2312 | -3.2385 | -1.7111 | -0.5293 | -0.1047 | -0.3759 |
| linear_interpolation | 0.3437 | -0.6479 | -1.1535 | -0.8504 | 0.0246 | 0.3007 | 0.2256 | 0.3201 |
| time_interpolation | 0.3437 | -0.6479 | -1.1535 | -0.8504 | 0.0246 | 0.3007 | 0.2256 | 0.3201 |
| cubic_interpolation | -0.3356 | 0.2258 | -0.9075 | -2.3486 | -0.3457 | -0.7330 | -2.7937 | 0.2535 |
| spline_interpolation | -0.4780 | -1.9556 | -0.7742 | -2.9312 | -0.4087 | -1.9857 | -4.6782 | 0.0494 |
| knn | -0.7900 | -0.3986 | -7.2637 | -3.4686 | -1.3316 | -0.2377 | -0.4254 | -0.1889 |
| decision_tree | -0.6838 | -0.1732 | -1.2678 | -1.7068 | -1.2575 | -0.1930 | -0.0138 | -0.0708 |
| random_forest | -2.8582 | -0.1685 | -1.5892 | -3.4899 | -1.5179 | -0.2312 | -0.2005 | -0.2995 |

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
| block | none | 10% | linear_interpolation | 1.0285 | 1.1880 | -1.6311 |
| block | none | 20% | linear_interpolation | 1.4765 | 1.6968 | -2.6787 |
| block | none | 30% | linear_interpolation | 3.4286 | 4.0453 | 0.3980 |
| block | none | 40% | linear_interpolation | 2.9308 | 3.6053 | 0.7248 |
| block | none | 50% | linear_interpolation | 5.4362 | 7.0441 | 0.1425 |
| block | none | 60% | linear_interpolation | 5.3499 | 6.8720 | 0.1376 |
| block | none | 70% | forward_fill | 3.5043 | 4.8567 | -0.0586 |
| block | none | 80% | linear_interpolation | 4.7975 | 6.1094 | 0.1660 |
| block_start | start | 10% | linear_interpolation | 0.9636 | 1.2281 | 0.2477 |
| block_start | start | 20% | linear_interpolation | 0.6991 | 0.8889 | 0.7639 |
| block_start | start | 30% | knn | 2.1096 | 2.6192 | -0.7254 |
| block_start | start | 40% | decision_tree | 1.7834 | 2.1787 | -0.0078 |
| block_start | start | 50% | linear_interpolation | 1.4386 | 1.9513 | 0.3576 |
| block_start | start | 60% | cubic_interpolation | 1.5243 | 1.8189 | 0.4898 |
| block_start | start | 70% | cubic_interpolation | 3.5094 | 4.7387 | -2.3956 |
| block_start | start | 80% | forward_fill | 4.2559 | 4.7930 | -0.3835 |
| block_middle | middle | 10% | linear_interpolation | 0.4913 | 0.5870 | -2.4255 |
| block_middle | middle | 20% | linear_interpolation | 1.1449 | 1.2988 | -2.6120 |
| block_middle | middle | 30% | cubic_interpolation | 3.9194 | 4.8003 | -13.3868 |
| block_middle | middle | 40% | random_forest | 2.7545 | 3.0057 | -0.2751 |
| block_middle | middle | 50% | cubic_interpolation | 1.2192 | 1.7261 | 0.7966 |
| block_middle | middle | 60% | forward_fill | 3.3930 | 4.7624 | -0.0919 |
| block_middle | middle | 70% | forward_fill | 3.8792 | 5.4544 | -0.1006 |
| block_middle | middle | 80% | forward_fill | 4.6316 | 6.3931 | -0.0673 |
| block_end | end | 10% | linear_interpolation | 3.4473 | 4.1538 | 0.3437 |
| block_end | end | 20% | cubic_interpolation | 4.1828 | 4.5838 | 0.2258 |
| block_end | end | 30% | spline_interpolation | 4.8486 | 5.9726 | -0.7742 |
| block_end | end | 40% | linear_interpolation | 6.8261 | 8.3215 | -0.8504 |
| block_end | end | 50% | linear_interpolation | 5.2375 | 7.0389 | 0.0246 |
| block_end | end | 60% | linear_interpolation | 4.9650 | 6.0693 | 0.3007 |
| block_end | end | 70% | linear_interpolation | 5.2253 | 6.0540 | 0.2256 |
| block_end | end | 80% | cubic_interpolation | 4.0472 | 5.7523 | 0.2535 |