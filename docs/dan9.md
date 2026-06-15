# Dan 9 — Eksperimentalni sloj i priprema rezultata za diplomski

**Datum:** 2026-06-17  
**Autor:** Toni Jakelić  
**Tema dana:** prebacivanje projekta iz skupa metoda u eksperimentalni sustav

---

## 1. Cilj dana

Projekt više nije samo kolekcija implementiranih metoda — postao je **eksperimentalni sustav**
koji omogućuje:

- usporedbu svih metoda na istom oštećenom nizu,
- pokretanje na više **missing rateova** (10%–50%),
- dva **scenarija** nedostajućih vrijednosti (random i block),
- spremanje rezultata u **CSV** za tablice i grafove u diplomskom radu.

Nove ML metode se ne dodaju; fokus je na evaluaciji i dokumentiranju postojećih.

---

## 2. Koje metode se uspoređuju

### Klasične interpolacijske metode

| Metoda | Opis |
|--------|------|
| `forward_fill` | Zadnja poznata vrijednost |
| `linear_interpolation` | Linearna interpolacija po indeksu |
| `time_interpolation` | Linearna interpolacija po vremenu (epoch) |
| `cubic_interpolation` | Kubična interpolacija |
| `spline_interpolation` | Prirodni kubični spline |

### ML metode

| Metoda | Implementacija | Opis |
|--------|----------------|------|
| `knn` | `knn_imputation_upgraded` | KNN s cikličkim značajkama i težinama |
| `decision_tree` | `decision_tree_imputation` | Regresijsko stablo |
| `random_forest` | `rf_imputation` | Prosjek predikcija više stabala |

> Napomena: osnovni `knn_imputation` ostaje u kodu, ali u eksperimentu se koristi
> poboljšana verzija pod imenom `knn` jer je reprezentativnija ML metoda.

---

## 3. Scenariji nedostajućih vrijednosti

### Random missing (`create_missing_values`)

- Vrijednosti se uklanjaju **nasumično** po nizu (Fisher-Yates shuffle).
- Prva i zadnja vrijednost ostaju poznate (rubni oslonci za interpolaciju).
- `mask[i] = 1` označava umjetno uklonjenu vrijednost.

### Block missing (`create_block_missing_values`)

- Uklanja se **kontinuirani blok** vrijednosti (npr. kvar senzora).
- Zadana veličina bloka: **12 uzoraka** = 2 sata pri 10-minutnom intervalu (Jena dataset).
- Blokovi se nasumično postavljaju bez preklapanja.
- Ista pravila za rubove i masku kao kod random scenarija.

---

## 4. Zašto su missing rateovi 10%, 20%, 30%, 40%, 50% korisni

Ovi udio pokazuju kako metode rade kad nedostaje **sve više podataka**:

| Rate | Značenje |
|------|----------|
| 10% | blagi gubitak — većina metoda još dobro radi |
| 20% | umjeren gubitak |
| 30% | značajan gubitak |
| 40% | težak scenarij (dosadašnji zadani rate u `--compare`) |
| 50% | ekstreman — pola podataka nedostaje |

Krivulja pogreške po rateu (MAE/RMSE vs missing rate) pokazuje **robusnost** metode
i pomaže u zaključku diplomskog rada.

---

## 5. Što se sprema u CSV

Glavna datoteka: `results/experiment_results.csv`

```text
scenario,missing_rate,method,mae,rmse,r2,count
random,0.20,knn,1.2345,1.5678,0.9123,58
```

| Stupac | Značenje |
|--------|----------|
| `scenario` | `random` ili `block` |
| `missing_rate` | udio uklonjenih vrijednosti (0.10–0.50) |
| `method` | naziv metode |
| `mae` | Mean Absolute Error |
| `rmse` | Root Mean Squared Error |
| `r2` | koeficijent determinacije |
| `count` | broj maskiranih točaka u evaluaciji |

Dodatne datoteke za grafove:

| Datoteka | Sadržaj |
|----------|---------|
| `results/mae_by_method.csv` | method, mae, scenario, missing_rate |
| `results/error_vs_missing_rate.csv` | missing_rate, method, mae, rmse, r2 |
| `results/reconstruction_random_forest_random_0.20.csv` | index, original, damaged, reconstructed, mask |
| `results/reconstruction_random_forest_block_0.20.csv` | isto, block scenarij |

---

## 6. Zašto je block missing važan

Random missing je akademski čist scenarij, ali u praksi senzori često **ne rade određeno
vrijeme** — npr. 2 sata zaredom. Tada:

- forward fill daje ravnu liniju (loše),
- linear/time interpolacija mora „premostiti“ veliku rupu,
- ML metode mogu koristiti značajke vremena (sat, dan u godini) za bolju procjenu.

Block missing je **realističniji** scenarij za zaključak o tome kada ML metode imaju smisla.

---

## 7. Kako će se rezultati koristiti u diplomskom

1. **Tablice rezultata** — iz `experiment_results.csv` (npr. MAE po metodi za 20% random).
2. **Graf original vs damaged vs reconstructed** — iz reconstruction CSV-a (Python/Excel).
3. **Graf MAE po metodama** — stupčasti graf iz `mae_by_method.csv`.
4. **Graf error vs missing rate** — linijski graf iz `error_vs_missing_rate.csv`.
5. **Usporedba metoda** — klasične vs ML po scenariju i rateu.
6. **Zaključak** — kada ML metode imaju smisla (npr. block missing, viši rate).

---

## 8. Pokretanje

```powershell
.\build.bat
.\test.bat

# Brza usporedba (jedan rate, random scenarij)
.\diplomski.exe --compare
.\diplomski.exe --compare --source demo --city Split --missing-rate 0.3

# Puni eksperiment (svi scenariji i rateovi → CSV)
.\diplomski.exe --experiment
.\diplomski.exe --experiment --source jena_quick
```

---

## 9. Datoteke dodane / promijenjene

| Datoteka | Promjena |
|----------|----------|
| `src/experiment.c`, `src/experiment.h` | Novi eksperimentalni sloj |
| `src/preprocessing.c`, `src/preprocessing.h` | `create_block_missing_values` |
| `src/main.c` | `--experiment`, zajednički `exp_run_methods` |
| `tests/run_tests.c` | testovi block missing + RF provjera |
| `results/` | mapa za CSV izlaz |

---

## 10. Dnevni izvještaj

### Što je napravljeno

- Eksperimentalni sloj (`experiment.c`) koji pokreće svih 8 metoda na istom damaged nizu.
- CLI naredba `--experiment` za automatski puni eksperiment.
- Block missing scenarij (`create_block_missing_values`).
- CSV export: `experiment_results.csv`, `mae_by_method.csv`, `error_vs_missing_rate.csv`,
  reconstruction CSV za Random Forest.
- Testovi za block missing i dopuna RF testa.
- Dokumentacija Dana 9.

### Metode u usporedbi

`forward_fill`, `linear_interpolation`, `time_interpolation`, `cubic_interpolation`,
`spline_interpolation`, `knn`, `decision_tree`, `random_forest`

### Missing rateovi

0.10, 0.20, 0.30, 0.40, 0.50

### Scenariji

`random`, `block` (block_size = 12)

### Rezultati

`results/experiment_results.csv` i ostale CSV datoteke u mapi `results/`

### Testovi

`.\test.bat` → SVE PROLAZI (418 provjera)

### Sljedeći korak

1. Analizirati rezultate iz CSV datoteka.
2. Napraviti grafove u Pythonu ili Excelu.
3. Napisati tekstualni zaključak za diplomski rad.

### TODO (kasnije, izvan Dana 9)

Vidi [dan10.md](dan10.md) i [dan11.md](dan11.md) — implementirano u sljedećim danima.

- CLI parametri za block_size i seed po scenariju.
- Export reconstruction za dodatne metode.
