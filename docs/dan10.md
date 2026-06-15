# Dan 10 — Skalabilni eksperiment i compare scenariji

**Datum:** 2026-06-18  
**Autor:** Toni Jakelić  
**Tema dana:** refaktor eksperimentalnog sloja, block u `--compare`, linear reconstruction export

---

## 1. Cilj dana

Poboljšati eksperimentalni sloj da bude **skalabilan** i spreman za grafove u diplomskom:
- jedna tablica metoda umjesto duplog koda,
- `--compare --scenario block|random`,
- export reconstruction CSV za **linear_interpolation** (najbolja metoda u rezultatima).

---

## 2. Što je napravljeno

- [x] `EXP_METHOD_TABLE` — sve metode na jednom mjestu u `experiment.c`
- [x] `exp_create_damage()` — zajednička funkcija za random i block
- [x] `exp_run_compare()` — compare logika premještena iz `main.c`
- [x] `exp_export_reconstruction()` — generički export po imenu metode
- [x] `EXP_RECON_EXPORT_METHODS[]` — lista metoda za CSV (lako proširiti)
- [x] CLI: `--scenario block`, `--export`
- [x] Datoteke: `reconstruction_linear_interpolation_{scenario}_{rate}.csv`

---

## 3. Pokretanje

```powershell
.\diplomski.exe --compare --scenario block --missing-rate 0.2 --export
.\diplomski.exe --compare --scenario random --missing-rate 0.2 --export
```

---

## 4. Sljedeći dan

Dan 11 — Python skripta za grafove i automatsku analizu (`scripts/report.py`).
