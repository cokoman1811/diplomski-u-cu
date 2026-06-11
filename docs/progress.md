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

---

## Trenutni status (C verzija)

**Zadnji završeni dan: Dan 8** — `decision_tree_imputation`, 9 metoda u `--compare`.

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

### Rezultati testiranja (2026-06-12)

```
.\test.bat → SVE PROLAZI
.\run.bat --compare --source demo --city Split   → 9 metoda (+ decision_tree)
.\run.bat --compare --source jena_quick          → 9 metoda
```

### Pokretanje (C)

```powershell
.\build.bat
.\test.bat
.\run.bat --compare --source demo --city Split
.\run.bat --compare --source jena_quick
```

---

## Plan — Dan 9

- [ ] Random Forest kao proširenje Decision Tree-a (dokumentacija / usporedba)
- [ ] Export tablice rezultata u CSV (za grafove)
- [ ] CLI parametri (`--knn-k`, dubina stabla)

### Izvan opsega (za sada)

- LSTM / neuronske mreže
- Veliki refactor projekta

---

## Python referenca (dan0–dan5)

Zapisi `dan0`–`dan5` su iz Python projekta (`diplomski-kopija`).
C verzija je na razini Dana 7 po funkcionalnosti (KNN + RF + upgraded KNN u compare).
