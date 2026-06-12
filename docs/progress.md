# Progress — po danima

Dnevni log napretka. Svaki dan ima svoju datoteku.

| Dan | Datum | Tema | Datoteka |
|-----|-------|------|----------|
| 0 | 2026-06-05 | Priprema projekta, git, struktura | [dan0.md](dan0.md) |
| 1 | 2026-06-06 | Učitavanje podataka (Jena Climate) | [dan1.md](dan1.md) |
| 2 | 2026-06-07 | Degradacija, interpolacija, evaluacija | [dan2.md](dan2.md) |
| 3 | 2026-06-08 | Centralni data loader, testovi, run.bat | [dan3.md](dan3.md) |
| 4 | 2026-06-08 | Klasične interpolacijske metode | [dan4.md](dan4.md) |
| 5 | 2026-06-09 | KNN imputacija (Python ref.) | [dan5.md](dan5.md) |
| 6 | 2026-06-10 | Testovi, FAQ, RF, osnovni KNN (C) | [dan6.md](dan6.md) |
| 7 | 2026-06-11 | KNN upgraded, razumijevanje ML (C) | [dan7.md](dan7.md) |
| 8 | 2026-06-12 | Decision Tree imputacija (C) | [dan8.md](dan8.md) |
| 9 | 2026-06-12 | Eksperimentalni sloj, CSV, block missing | [dan9.md](dan9.md) |

---

## Trenutni status (C verzija)

**Zadnji završeni dan: Dan 9** — eksperimentalni sustav, `--experiment`, CSV export, block missing.

**Razumijevanje:** ML dio (KNN/RF) još se uči — normalno za 2 dana. Osnovni tok projekta je jasan.

### Dan 6 — sažetak (C)

- [x] Testovi `tests/run_tests.c`, FAQ `cesta_pitanja.md`, git-sync
- [x] `knn_methods` + `rf_methods` u `--compare`
- [x] Dokumentacija po danima prenesena iz Python projekta

### Dan 7 — sažetak (C)

- [x] `knn_upgraded` — cikličke značajke, težinski prosjek, adaptivno k
- [x] Usporedba `knn_imputation` vs `knn_upgraded` u tablici

### Dan 8 — sažetak (C)

- [x] `decision_tree_imputation` — regresijsko stablo, MSE podjela, dubina ≤ 5
- [x] Iste cikličke značajke kao knn_upgraded
- [x] `test_decision_tree()`, red u `--compare` tablici

### Dan 9 — sažetak (C)

- [x] `experiment.c` — zajednička usporedba 8 metoda
- [x] `--experiment` — scenariji random + block, rateovi 10–50%
- [x] `create_block_missing_values` — kontinuirani blokovi (2 h)
- [x] CSV export u `results/` (metrike + reconstruction)
- [x] Testovi block missing + dopuna ML testova

### Rezultati testiranja (2026-06-12)

```
.\test.bat → SVE PROLAZI (418 provjera)
.\diplomski.exe --compare --source jena_quick     → 8 metoda
.\diplomski.exe --experiment --source jena_quick  → CSV u results/
```

### Pokretanje (C)

```powershell
.\build.bat
.\test.bat
.\diplomski.exe --compare --source jena_quick
.\diplomski.exe --experiment --source jena_quick
```

---

## Plan — Dan 10

- [ ] Analiza rezultata iz CSV datoteka
- [ ] Grafovi u Pythonu / Excelu
- [ ] Tekstualni zaključak za diplomski

### Izvan opsega (za sada)

- LSTM / neuronske mreže
- Veliki refactor projekta

---

## Python referenca (dan0–dan5)

Zapisi `dan0`–`dan5` su iz Python projekta (`diplomski-kopija`).
C verzija je na razini Dana 7 po funkcionalnosti (KNN + RF + upgraded KNN u compare).
