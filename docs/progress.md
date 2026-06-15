# Progress — po danima

Dnevni log napretka. Svaki dan ima svoju datoteku.  
**Puni raspored:** [raspored.md](raspored.md) (18 radnih dana + popratni agenti)  
**Agenti (git, dokumentacija):** [agents_i_dokumentacija.md](agents_i_dokumentacija.md)

| Dan | Datum | Tema | Datoteka |
|-----|-------|------|----------|
| 0 | 2026-06-05 | Priprema projekta, git, struktura | [dan0.md](dan0.md) |
| 1 | 2026-06-06 | Učitavanje podataka (Jena Climate) | [dan1.md](dan1.md) |
| 2 | 2026-06-07 | Degradacija, interpolacija, evaluacija | [dan2.md](dan2.md) |
| 3 | 2026-06-09 | Centralni data loader, testovi, run.bat | [dan3.md](dan3.md) |
| 4 | 2026-06-10 | Klasične interpolacijske metode | [dan4.md](dan4.md) |
| 5 | 2026-06-11 | KNN imputacija (Python ref.) | [dan5.md](dan5.md) |
| 6 | 2026-06-12 | Testovi, FAQ, RF, osnovni KNN (C) | [dan6.md](dan6.md) |
| 7 | 2026-06-13 | KNN upgraded, razumijevanje ML (C) | [dan7.md](dan7.md) |
| 8 | 2026-06-16 | Decision Tree imputacija (C) | [dan8.md](dan8.md) |
| 9 | 2026-06-17 | Eksperimentalni sloj, block missing, CSV | [dan9.md](dan9.md) |
| 10 | 2026-06-18 | Skalabilni experiment, compare scenariji | [dan10.md](dan10.md) |
| 11 | 2026-06-19 | Grafovi i analiza (report.py) | [dan11.md](dan11.md) |
| 12 | 2026-06-20 | Pregled rezultata, priprema za pisanje | [dan12.md](dan12.md) |
| 13 | 2026-06-23 | Uvod + literatura | [dan13.md](dan13.md) |
| 14 | 2026-06-24 | Teorija + metodologija | [dan14.md](dan14.md) |
| 15 | 2026-06-25 | Poglavlje Implementacija | [dan15.md](dan15.md) |
| 16 | 2026-06-26 | Poglavlje Rezultati | [dan16.md](dan16.md) |
| 17 | 2026-06-27 | Zaključak, sažetak, obrana | [dan17.md](dan17.md) |

---

## Trenutni status

**Zadnji završeni dan (kod): Dan 11** — grafovi, `analysis.md`, `report.bat`  
**Sljedeći korak: Dan 12** — pregled materijala, zatim pisanje rada (dani 13–17)

### Faze

| Faza | Dani | Status |
|------|------|--------|
| Podaci i klasične metode | 0–5 | ✅ gotovo |
| ML metode | 6–8 | ✅ gotovo |
| Eksperimenti i izvještaj | 9–11 | ✅ gotovo |
| Priprema za tekst | 12 | 📋 sljedeće |
| Pisanje diplomskog | 13–17 | 📋 planirano |
| **Popratno — agenti** | A, B, C | ✅ vidi [agents_i_dokumentacija.md](agents_i_dokumentacija.md) |

### Popratni rad (agenti)

| Dan | Kada | Što |
|-----|------|-----|
| A | 8.–9.6. | GitHub push agent — `git-sync.ps1`, Cursor hook |
| B | 14.–15.6. | Dokumentacija — `dan*.md`, FAQ, progress |
| C | 19.–20.6. | Raspored, `report.py`, `analysis.md` |

### Pokretanje

```powershell
.\build.bat
.\test.bat
.\diplomski.exe --experiment --source jena_quick
python scripts/report.py
# ili sve odjednom:
.\report.bat
```

### Izlazi za diplomski

| Mapa / datoteka | Sadržaj |
|-----------------|---------|
| `results/experiment_results.csv` | Tablice metrika |
| `results/analysis.md` | Analiza + nacrt zaključka |
| `figures/*.png` | Grafovi za Word |

---

## Python referenca (dan0–dan5)

Zapisi `dan0`–`dan5` uključuju i rad iz Python referentnog projekta (`dan5`).
