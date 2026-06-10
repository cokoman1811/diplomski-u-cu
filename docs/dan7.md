# Dan 7 — Naprednija KNN funkcija (`knn_upgraded`)

**Datum:** 2026-06-11  
**Autor:** Toni Jakelić  
**Tema dana:** rad na naprednijoj KNN funkciji za imputaciju temperature

Drugi dan rada na ML dijelu. Nastavak Dana 6 — cilj je imati **dvije KNN varijante**
(osnovnu i upgraded) za usporedbu u diplomskom radu, bez brisanja postojećeg koda.

---

## Što je napravljeno

- [x] Novi modul **`knn_upgraded.c`** / **`knn_upgraded.h`** (osnovni KNN netaknut)
- [x] Cikličke značajke za `hour` i `yday` (sin/cos)
- [x] Normalizirana pozicija `index / (n - 1)`
- [x] Podesive težine značajki (`KnnUpgradedConfig`)
- [x] Težinski prosjek susjeda `1 / (distance + epsilon)`
- [x] Usporedba u **`main.c --compare`**: `knn_imputation` vs `knn_upgraded`
- [x] Test **`test_knn_upgraded()`** u `tests/run_tests.c`
- [x] Build i testovi prolaze

---

## Problem osnovne KNN verzije

Osnovni KNN (`knn_methods.c`) koristi **sirove** vrijednosti značajki:

| Značajka | Problem |
|----------|---------|
| `position` (indeks 0–287) | Dominira udaljenost jer ima veći numerički raspon od sata (0–23) |
| `hour` | **Ciklička** — sat 23 i sat 0 su blizu, ali \|23 − 0\| = 23 |
| `yday` | **Ciklička** — 365. dan i 1. dan su blizu, ali \|365 − 1\| = 364 |

Dodatno: osnovni KNN daje **jednaki prosjek** svih k susjeda — bliski i daleki
susjedi imaju isti utjecaj.

Na malom nizu (demo Split, 12 zapisa) to daje loš MAE jer pozicija „pobjeđuje“
nad satom i danom.

---

## Zašto normalizacija pozicije?

```c
position_norm = index / (n - 1)   /* raspon [0, 1] */
```

Bez normalizacije indeks 287 i indeks 0 imaju udaljenost 287, dok sat 10 i sat 11
imaju udaljenost 1. Pozicija dominira i KNN traži „slične indekse“, a ne nužno
„slično vrijeme dana“.

Normalizacija stavlja sve značajke u usporediv raspon prije množenja težinama.

---

## Zašto sin/cos za hour i yday?

**Hour je ciklička značajka** — 23:00 i 00:00 su jedan sat razlike, ne 23 sata.

**Yday je ciklička značajka** — kraj godine i početak godine su blizu u kalendaru.

Obična normalizacija `hour/24` i `(yday-1)/365` **ne hvata** tu cikličnost:
udaljenost između 23/24 ≈ 0.96 i 0/24 = 0 je ~0.96, iako su sati susjedni.

Rješenje — mapiranje na krug:

```c
hour_sin = sin(2π * hour / 24)
hour_cos = cos(2π * hour / 24)

yday_sin = sin(2π * (yday - 1) / 365)
yday_cos = cos(2π * (yday - 1) / 365)
```

Dva susjedna sata daju bliske točke na krugu → mala euklidska udaljenost u
(sin, cos) prostoru.

---

## Težinski prosjek susjeda

Osnovni KNN: `out[i] = (T₁ + T₂ + … + Tₖ) / k` — svi susjedi jednako.

Upgraded KNN:

```c
weight = 1 / (distance + epsilon)
out[i] = Σ(weight_j * T_j) / Σ(weight_j)
```

Bliži susjedi (manja udaljenost u prostoru značajki) imaju **veći utjecaj** na
predikciju. `epsilon` sprječava dijeljenje s nulom kad je susjed vrlo blizak.

---

## Što nova funkcija prima i vraća

```c
int knn_imputation_upgraded(
    const Series *series,      /* znacajke: hour[i], yday[i], epoch[i] */
    const double *temp,        /* damaged niz s NaN — NE mijenja se */
    const KnnUpgradedConfig *cfg,  /* NULL = zadane vrijednosti */
    double *out                /* popunjeni rezultat */
);
```

| Parametar | Značenje |
|-----------|----------|
| `series` | Vremenski niz sa značajkama po indeksu |
| `temp` | Ulaz s rupe (NaN) — original `s.temp` ostaje netaknut |
| `cfg` | k, težine značajki, epsilon (opcionalno) |
| `out` | Izlaz: poznate vrijednosti kopirane, NaN popunjeni |
| **povrat** | `0` = uspjeh, `1` = greška |

Tok unutar funkcije:

1. Kopira `temp` → `out`
2. Za svaku NaN poziciju traži k najbližih **poznatih** temperatura
3. Udaljenost računa u 5D prostoru (position, hour_sin/cos, yday_sin/cos)
4. Predikcija = težinski prosjek temperatura susjeda
5. `fill_remaining_gaps()` ako nešto ostane NaN

---

## Razlika od osnovne KNN funkcije

| | `knn_imputation` | `knn_imputation_upgraded` |
|--|------------------|---------------------------|
| Pozicija | sirovi indeks | `index / (n-1)` |
| Hour | sirovi sat 0–23 | sin/cos (ciklički) |
| Yday | sirovi dan 1–365 | sin/cos (ciklički) |
| Težine značajki | implicitno 1:1:1 | `weight_position`, `weight_hour`, `weight_yday` |
| Predikcija | jednostavan prosjek | `1/(d+ε)` težinski prosjek |
| k | fiksno (npr. 5) | adaptivno na malom nizu (k≤3 ili k≤2) |
| Config | samo `n_neighbors` | `KnnUpgradedConfig` struct |

---

## Testovi (`test_knn_upgraded`)

U `tests/run_tests.c`, mali niz od 8 satnih zapisa s 2 NaN rupe:

| Provjera | Što testira |
|----------|-------------|
| `knn_imputation_upgraded uspjeh` | funkcija vraća 0 |
| `nema NaN nakon imputacije` | sve rupe popunjene |
| `poznate vrijednosti nepromijenjene` | indeksi bez NaN ostaju isti |
| `NaN na poziciji 2/4 popunjen` | eksplicitno da su rupe popunjene |
| `rupa ~ 12 / ~ 14` | razumna predikcija na malom nizu |
| `original i dalje ima NaN` | damaged niz nije mutiran |

Paralelno postoji `test_knn()` za osnovnu verziju — ista struktura provjera.

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

### Jena 48h (288 zapisa)

| Metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| linear_interpolation | 0.0620 | 0.0920 | 0.9980 |
| knn_imputation | 0.1102 | 0.1591 | 0.9941 |
| **knn_upgraded** | **0.1068** | **0.1541** | **0.9944** |
| rf_imputation | 0.2136 | 0.2921 | 0.9801 |

Upgraded KNN je bolji od osnovnog na oba niza; interpolacija i dalje pobjeđuje
na ovom eksperimentu — to je valjan zaključak za rad.

---

## Što moram shvatiti (checklist)

- [ ] Zašto hour/yday trebaju sin/cos, a ne samo /24 i /365
- [ ] Što radi `KnnUpgradedConfig` i zašto `weight_hour = 2.0` po defaultu
- [ ] Razlika jednostavnog i težinskog prosjeka susjeda
- [ ] Zašto `temp` (damaged) ulazi, a `s.temp` (original) služi za evaluaciju

---

## Što pročitati (~1 h)

```
1. src/knn_methods.c      → osnovni KNN (usporedba)
2. src/knn_upgraded.c     → cikličke značajke + težinski prosjek
3. src/knn_upgraded.h     → KnnUpgradedConfig
4. tests/run_tests.c      → test_knn_upgraded()
5. src/main.c             → run_compare(), red knn_upgraded
```

```powershell
.\build.bat
.\test.bat
.\run.bat --compare --source demo --city Split
```

---

## Datoteke Dana 7

| Datoteka | Uloga |
|----------|--------|
| `src/knn_upgraded.h` | API, `KnnUpgradedConfig` |
| `src/knn_upgraded.c` | Napredni KNN s cikličkim značajkama |
| `src/main.c` | Red `knn_upgraded` u tablici |
| `tests/run_tests.c` | `test_knn_upgraded()` |

---

## Sljedeći korak (Dan 8 — plan)

- Grafovi ili export rezultata u CSV
- CLI za KNN parametre (`--knn-k`, težine)
- Kratki odlomak u radu: „Usporedba osnovnog i poboljšanog KNN-a“
