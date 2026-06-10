# Dan 6 — Testovi, dokumentacija, RF, razumijevanje osnova (C)

**Datum:** 2026-06-10  
**Autor:** Toni Jakelić  
**Fokus:** stabilizacija projekta + prvi ML koraci, bez velikog refactora

Prvi dan rada na ML dijelu C verzije. Cilj nije bio „savladati sve odjednom“, nego
postaviti temelje da se KNN i RF mogu usporediti s interpolacijom.

---

## Što je napravljeno

### Infrastruktura i dokumentacija
- [x] Test suite: **`tests/run_tests.c`** (40 provjera), `test.bat`, `make test`
- [x] FAQ: **`docs/cesta_pitanja.md`** (Metrics, Series, .h/.c, git-sync, greške…)
- [x] Prenesena dokumentacija po danima (`dan0`–`dan5`, `progress.md`, `KORACI.md`)
- [x] `git-sync.bat`, Cursor hook, `CHANGELOG.md`, `.vscode/tasks.json`
- [x] Preimenovano `ml_methods` → **`knn_methods`** (samo KNN u tom modulu)

### KNN (osnovni)
- [x] Pregled **`knn_methods.c`** — logika ostala ista
- [x] Komentari u **`.h`** i **`.c`** (zašto KNN, ulazi, test)
- [x] KNN već u **`main.c --compare`**
- [x] Test **`test_knn()`**

### Random Forest (minimalna verzija)
- [x] Novi modul **`rf_methods.c`** / **`.h`** — `rf_imputation()`
- [x] RF u **`main.c --compare`**
- [x] Test **`test_rf()`**

---

## Što sam taj dan radio na razumijevanju (i što je bilo teško)

| Tema | Status | Bilješka |
|------|--------|----------|
| Tok `main.c` → `--compare` | ✅ početak | CSV → Series → damaged → metode → metrike |
| `Series` struktura | ✅ | `temp`, `epoch`, `hour`, `yday` — paralelna polja |
| `.h` vs `.c` (jelovnik/kuhinja) | ✅ | `series.h` + `dataset.c` |
| `Metrics`, `ok` flag | ✅ | nije CSV, nego struct u memoriji |
| KNN algoritam detaljno | 🟡 | ideja jasna, implementacija još spora |
| Random Forest | 🟡 | znam da postoji u tablici, unutrašnjost tek površno |

**Normalno je da jedan dan ne „sjedne“ sve** — Dan 6 je bio postavljanje sustava, ne finalno razumijevanje KNN-a.

---

## Rezultati testiranja (2026-06-10)

```powershell
.\build.bat
.\test.bat          # 35/35 → kasnije 40/40 nakon dan7
.\run.bat --compare --source demo --city Split
```

**`--compare` demo Split (bez knn_upgraded):** 7 metoda — klasične + knn + rf.

| Metoda | MAE (demo) |
|--------|------------|
| linear_interpolation | 0.0900 |
| knn_imputation | 0.5360 |
| rf_imputation | 0.4106 |

KNN loš na malom nizu — očekivano, tema za Dan 7.

---

## Datoteke Dana 6

| Datoteka | Uloga |
|----------|--------|
| `tests/run_tests.c` | Automatski testovi |
| `docs/cesta_pitanja.md` | FAQ za učenje |
| `src/knn_methods.*` | Osnovni KNN |
| `src/rf_methods.*` | Minimalni Random Forest |
| `scripts/git-sync.ps1` | Backup na GitHub |

---

## Sljedeći dan

→ [Dan 7 — KNN upgraded + dublje razumijevanje](dan7.md)
