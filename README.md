# Diplomski — C verzija

C (C99) implementacija eksperimenta za usporedbu klasičnih i strojno-učenih
metoda imputacije nedostajućih vrijednosti u temperaturnim vremenskim nizovima.

Ovo je C inačica glavnog (Python) diplomskog rada koji se nalazi u korijenskoj mapi.
Sve metode (interpolacija, KNN, metrike) pisane su ručno, bez vanjskih biblioteka.

## Sadržaj

```
diplomski c/
├── src/
│   ├── series.h / dataset.c    # struktura niza, učitavanje CSV-a, parsiranje datuma
│   ├── preprocessing.*         # umjetno uklanjanje vrijednosti (RNG)
│   ├── interpolation.*         # forward fill, linear, time, cubic, spline
│   ├── knn_methods.*           # KNN imputacija (osnovna)
│   ├── knn_upgraded.*          # KNN imputacija (poboljsana)
│   ├── rf_methods.*            # Random Forest imputacija (minimalna)
│   ├── evaluation.*            # MAE, RMSE, R²
│   ├── experiment.*            # eksperimentalni sloj, CSV export
│   └── main.c                  # CLI
├── data/                       # kopije ulaznih CSV podataka
├── Makefile                    # build (Linux/macOS/MinGW)
├── build.bat                   # build na Windowsu (gcc)
└── run.bat                     # build + pokretanje na Windowsu
```

## Build i pokretanje

Pokretati iz ove mape (`diplomski c`) jer se podaci čitaju relativno (`data/...`).

### Windows (gcc / MinGW-w64)

```powershell
cd "diplomski c"
.\build.bat
.\diplomski.exe --compare
.\diplomski.exe --compare --source demo --city Split
.\diplomski.exe --compare --missing-rate 0.3
.\diplomski.exe --compare --scenario block --missing-rate 0.2 --export
.\diplomski.exe --experiment
.\diplomski.exe --experiment --source jena_quick
```

> Treba `gcc` u PATH-u: `winget install -e --id BrechtSanders.WinLibs.POSIX.UCRT`

### Linux / macOS

```bash
cd "diplomski c"
make
./diplomski --compare
```

## Argumenti

| Argument | Zadano | Opis |
|----------|--------|------|
| `--compare` | — | pokreni usporedbu metoda |
| `--scenario` | `random` | `random` \| `block` (samo uz `--compare`) |
| `--export` | — | spremi reconstruction CSV za linear (uz `--compare`) |
| `--experiment` | — | puni eksperiment → CSV u `results/` |
| `--source` | `jena_quick` | `jena_quick` \| `processed` \| `demo` |
| `--city` | `Split` | grad (samo za `demo`) |
| `--missing-rate` | `0.4` | udio uklonjenih vrijednosti (`--compare` only) |

## Implementirane metode (usporedba)

Klasične: `forward_fill`, `linear_interpolation`, `time_interpolation`,
`cubic_interpolation`, `spline_interpolation`.

ML: `knn` (upgraded), `decision_tree`, `random_forest`.

## Eksperiment (`--experiment`)

Pokreće sve metode za scenarije **random** i **block** missing te missing rateove
10%, 20%, 30%, 40%, 50%. Rezultati se spremaju u `results/`:

- `experiment_results.csv` — glavna tablica metrika
- `mae_by_method.csv`, `error_vs_missing_rate.csv` — podaci za grafove
- `reconstruction_linear_interpolation_*_0.20.csv` — original vs damaged vs reconstructed (linear)

## Izvještaj za diplomski (`report.bat`)

```powershell
pip install -r scripts/requirements.txt
.\report.bat
```

| Izlaz | Sadržaj |
|-------|---------|
| `results/experiment_results.csv` | Tablice metrika |
| `results/analysis.md` | Tekstualna analiza + nacrt zaključka |
| `slike i videa/2026/diplomski-grafovi/*.png` | Grafovi za Word |

Samo grafove iz postojećeg CSV-a: `python scripts/report.py`
