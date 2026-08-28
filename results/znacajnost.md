# Testovi znacajnosti (upareni)

Referenca: `linear_interpolation`. Ponavljanja: **20** tjednih prozora, svaki sa svojim seedom maske.

Dizajn je uparen: unutar jednog ponavljanja sve metode dobivaju identican osteceni niz, pa se usporeduju razlike po paru. Test je Wilcoxonov test predznacenih rangova, interval je bootstrap percentilni 95 %, a p-vrijednosti su korigirane Holm-Bonferroni postupkom.

Negativna razlika znaci da je metoda **bolja** od reference.

| Metoda | Δ MAE (°C) | 95 % CI | Pobjeda–poraz–nerijeseno | p (Holm) | Znacajno |
|--------|-----------|---------|--------------------------|----------|----------|
| `knn` | +0.0000 | [+0.0000, +0.0000] | 0–0–800 | 1.00e+00 | ne |
| `time_interpolation` | +0.0000 | [+0.0000, +0.0000] | 0–0–800 | 1.00e+00 | ne |
| `knn_upgraded` | +0.0112 | [-0.0028, +0.0254] | 356–444–0 | 1.80e-02 | DA (losija) |
| `neural_net` | +0.0234 | [+0.0132, +0.0339] | 282–518–0 | 4.57e-13 | DA (losija) |
| `random_forest` | +0.0319 | [+0.0128, +0.0512] | 368–432–0 | 4.05e-02 | DA (losija) |
| `decision_tree` | +0.0733 | [+0.0467, +0.1023] | 285–513–2 | 1.31e-12 | DA (losija) |
| `moving_average` | +0.7371 | [+0.6274, +0.8452] | 210–590–0 | 1.05e-39 | DA (losija) |
| `forward_fill` | +0.8117 | [+0.7019, +0.9224] | 202–598–0 | 3.61e-46 | DA (losija) |
| `adaptive_imputation` | +1.5443 | [+1.1534, +1.9857] | 155–271–374 | 5.04e-19 | DA (losija) |
| `cubic_interpolation` | +5.9935 | [+5.2173, +6.8128] | 199–601–0 | 7.15e-72 | DA (losija) |
| `spline_interpolation` | +7.3038 | [+6.3526, +8.3074] | 187–613–0 | 7.23e-79 | DA (losija) |

## Po scenarijima

| Scenarij | `neural_net` | `random_forest` | `decision_tree` | `knn_upgraded` | `adaptive_imputation` |
|---|---|---|---|---|---|
| random | +0.0358 \* | +0.0021 \* | +0.0206 \* | +0.0186 \* | -0.0005 |
| block | -0.0094 | -0.0051 \* | -0.0055 | -0.0058 \* | +1.6246 \* |
| block_start | +0.0352 \* | +0.1182 \* | +0.2409 \* | +0.0608 | +1.8206 \* |
| block_middle | +0.0017 | -0.0020 | +0.0006 | -0.0053 \* | +2.2176 \* |
| block_end | +0.0535 \* | +0.0463 \* | +0.1097 \* | -0.0125 | +2.0590 \* |

\* = znacajno na razini 0,05 nakon Holmove korekcije
