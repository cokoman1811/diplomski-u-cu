# Changelog — diplomski u cu (C verzija)

Kratki popis promjena po datumu.

## 2026-06-12 (Dan 9)

- Dodan `experiment.c` / `.h` — zajednička usporedba 8 metoda, CSV export
- CLI `--experiment` — scenariji random + block, missing rateovi 10–50%
- `create_block_missing_values` u `preprocessing.c` — kontinuirani blokovi (2 h)
- `main.c` koristi `exp_run_methods` za `--compare` (8 metoda)
- Test `test_block_missing()`, dopuna `test_rf()`
- Mapa `results/` za CSV izlaz
- Dokumentacija `docs/dan9.md`

## 2026-06-08 – 2026-06-15 (popratno)

- `docs/agents_i_dokumentacija.md` — dnevnik rada na Cursor agentima
- Dan A: GitHub push (`git-sync.ps1`, hook)
- Dan B: agent za pisanje `dan*.md`, FAQ, progress
- `docs/raspored.md` — 18-dnevni plan rada

## 2026-06-12 (Dan 8)

- `decision_tree_imputation` — regresijsko stablo za imputaciju

## 2026-06-11 (Dan 7)

- Dodan `knn_upgraded.c` / `.h` — normalizacija, težine, težinski prosjek
- Usporedba `knn_imputation` vs `knn_upgraded` u `--compare`
- Test `test_knn_upgraded()`
- Ažurirani `docs/dan6.md`, `docs/dan7.md`, `docs/progress.md`

## 2026-06-10 (Dan 6)

- KNN: komentari u `knn_methods.c` / `.h`, test dokumentiran
- Dodan `rf_methods.c` / `.h` — minimalna Random Forest imputacija
- `main.c --compare`: red `rf_imputation`
- Test `test_rf()` u `run_tests.c`
- Ažuriran `docs/dan6.md`

## 2026-06-10 (ranije)

- Preimenovano `ml_methods` → `knn_methods` (samo KNN; RF ide u zasebni modul)
- Dodan `docs/dan6.md` — predložak za sljedeći radni dan
- Dodan `.vscode/tasks.json` — Build, Test, Compare, Git sync iz Cursora
- Proširen `docs/cesta_pitanja.md` — odjeljak „Česte greške“
- Dodan `CHANGELOG.md`
- Prenesena dokumentacija po danima (`docs/dan0.md`–`dan5.md`, `progress.md`, `KORACI.md`)

## 2026-06-10 (ranije u sesiji)

- Dodani testovi: `tests/run_tests.c`, `test.bat`, `make test`
- Dodan `docs/cesta_pitanja.md` — FAQ za C verziju
- Dodan git auto-sync: `scripts/git-sync.ps1`, `git-sync.bat`, Cursor hook
- `build.bat` — gradi i `diplomski.exe` i `tests.exe`, auto-pronalazi gcc iz WinGeta

## 2026-06-09 (inicijalni commit)

- C99 implementacija cijelog pipelinea: CSV, preprocessing, 5 interpolacija, KNN, evaluacija
- CLI `main.c` s `--compare`
- Podaci: demo CSV + Jena 48h processed
- `Makefile`, `build.bat`, `run.bat`, `README.md`
