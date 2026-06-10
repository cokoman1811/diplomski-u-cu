# Dan 7 — KNN upgraded + dublje razumijevanje ML dijela (C)

**Datum:** 2026-06-11  
**Autor:** Toni Jakelić  
**Fokus:** popraviti KNN greške, usporediti dvije KNN varijante, shvatiti zašto ML ponekad gori od interpolacije

Drugi dan rada na ML dijelu. Nastavak Dana 6 — nije završetak projekta, nego
**učvršćivanje razumijevanja** jer KNN/RF nisu intuitivni kao linear interpolacija.

---

## Što je napravljeno

- [x] Analiza mana osnovnog KNN-a (1:1:1 značajke, loš rezultat na malom nizu)
- [x] Novi modul **`knn_upgraded.c`** / **`.h`**
  - normalizirane značajke (pozicija, hour, yday)
  - podesive težine (`KnnUpgradedConfig`)
  - težinski prosjek susjeda (bliži = veći utjecaj)
  - adaptivno k na malom nizu (k=2 ili 3)
- [x] Usporedba u **`main.c --compare`**: `knn_imputation` vs `knn_upgraded`
- [x] Test **`test_knn_upgraded()`**
- [x] Proširen FAQ i README

---

## Zašto smo napravili `knn_upgraded`?

Osnovni KNN (`knn_methods.c`) koristi **sirove** vrijednosti značajki:
- pozicija 0–287 dominira nad satom 0–23
- svi susjedi jednako važe u prosjeku
- k=5 fiksno — previše za 12 zapisa (demo Split)

Upgraded verzija to popravlja **bez mijenjanja** originalnog KNN-a — možeš u radu
usporediti „prije i poslije“.

---

## Rezultati — usporedba KNN varijanti

Isti eksperiment: seed 42, 40% obrisanih, evaluacija samo na maski.

### Demo Split (12 zapisa)

| Metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| linear_interpolation | 0.0900 | 0.1037 | 0.9186 |
| knn_imputation | 0.5360 | 0.6441 | -2.1430 |
| **knn_upgraded** | **0.2488** | **0.2765** | **0.4208** |
| rf_imputation | 0.4106 | 0.5052 | -0.9336 |

**Zaključak:** upgraded KNN je **puno bolji** od osnovnog na malom nizu, ali i dalje
ispod linear interpolacije. To je OK za diplomski — pokazuješ zašto treba paziti na značajke.

### Jena 48h (288 zapisa)

| Metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| linear_interpolation | 0.0620 | 0.0920 | 0.9980 |
| knn_imputation | 0.1102 | 0.1591 | 0.9941 |
| **knn_upgraded** | **0.1068** | **0.1541** | **0.9944** |
| rf_imputation | 0.2136 | 0.2921 | 0.9801 |

**Zaključak:** na većem nizu KNN upgraded je malo bolji od osnovnog; interpolacija
i dalje pobjeđuje na ovom eksperimentu.

---

## Što moram shvatiti (checklist za sebe)

Označi kad stvarno možeš objasniti naglas:

- [ ] **Zašto KNN uz interpolaciju?** — ML gleda slična mjerenja u cijelom nizu, ne samo susjede
- [ ] **Što je `Series`?** — tablica: `temp[i]`, `hour[i]`, `yday[i]` za isto mjerenje `i`
- [ ] **Što ulazi u KNN?** — `series` (značajke), `temp` (damaged), `k`, `out`
- [ ] **Zašto poznate vrijednosti ostaju?** — učimo/predviđamo samo NaN mjesta
- [ ] **Gdje se uspoređuje?** — `main.c` → `run_compare()` → tablica MAE/RMSE/R²
- [ ] **Zašto je osnovni KNN loš na demo Splitu?** — malo podataka + neskalirane značajke
- [ ] **Što upgraded popravlja?** — normalizacija, težine, težinski prosjek, manje k
- [ ] **Razlika KNN vs RF?** — KNN = prosjek susjeda; RF = prosjek više stabala odluka

---

## Što pročitati (redoslijed, ~1 h)

```
1. docs/cesta_pitanja.md  → točke 1, 5, 6, 9 (Metrics, .h/.c, Series, KNN)
2. src/main.c             → run_compare() — cijeli tok
3. src/knn_methods.c      → osnovni KNN (122 linije)
4. src/knn_upgraded.c     → što je drugačije
5. tests/run_tests.c      → test_knn() i test_knn_upgraded()
```

Pokreni uz čitanje:

```powershell
.\run.bat --compare --source demo --city Split
.\run.bat --compare --source jena_quick
```

---

## Testirano (2026-06-11)

```powershell
.\build.bat
.\test.bat
```

**Rezultat:** 40/40 — SVE PROLAZI

---

## Što još NIJE gotovo (nije problem)

- [ ] CLI parametri (`--knn-k`, `--knn-hour-weight`) — opcionalno
- [ ] Poboljšati RF (više stabala, random features)
- [ ] Grafovi usporedbe
- [ ] Potpuno „sjedanje“ KNN/RF u glavu — **u tijeku, normalno traje**

---

## Datoteke Dana 7

| Datoteka | Uloga |
|----------|--------|
| `src/knn_upgraded.h` | `KnnUpgradedConfig`, API |
| `src/knn_upgraded.c` | Poboljšani KNN |
| `src/main.c` | Red `knn_upgraded` u tablici |
| `tests/run_tests.c` | `test_knn_upgraded()` |

---

## Poruka sebi (ako opet „ne klikne“)

> Ne moraš danas znati svaku liniju KNN-a. Dovoljno je znati:
> **ulaz → što metoda radi → izlaz → metrika na maski.**
> Detalji implementacije dolaze s ponavljanjem i testovima.

## Sljedeći korak (Dan 8 — plan)

- Grafovi ili export rezultata u CSV
- CLI za KNN parametre
- Kratki odlomak u radu: „Usporedba osnovnog i poboljšanog KNN-a“
