# Dan 11 — Grafovi i tekstualna analiza (Python)

**Datum:** 2026-06-19  
**Autor:** Toni Jakelić  
**Tema dana:** priprema materijala za poglavlje Rezultati u diplomskom

---

## 1. Cilj dana

Iz postojećih CSV rezultata automatski generirati:
- **grafove** (PNG) za umetanje u Word,
- **tekstualnu analizu** s tablicama i ključnim nalazima.

Zaključak se ne generira kao konačan tekst rada — samo **nacrt** u `analysis.md`.

---

## 2. Što je napravljeno

- [x] `scripts/report.py` — čita `experiment_results.csv`, crta grafove
- [x] `scripts/requirements.txt` — pandas, matplotlib
- [x] `report.bat` — build + experiment + report u jednom
- [x] `slike i videa/` — PNG grafikoni
- [x] `results/analysis.md` — sažetak, tablice, nalazi, nacrt zaključka

### Grafovi

| Datoteka | Sadržaj |
|----------|---------|
| `mae_by_method_random_20.png` | Stupčasti MAE, random 20% |
| `mae_by_method_block_20.png` | Stupčasti MAE, block 20% |
| `mae_vs_rate_random.png` | MAE vs missing rate |
| `mae_vs_rate_block.png` | MAE vs missing rate, block |
| `reconstruction_linear_*.png` | Original vs rekonstruirano |

---

## 3. Pokretanje

```powershell
pip install -r scripts/requirements.txt
.\report.bat
# ili samo:
python scripts/report.py
```

---

## 4. Sljedeći dan

Dan 12 — pregled i dorada grafova/tablica prije pisanja rada.
