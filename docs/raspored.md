# Raspored diplomskog rada — po danima

**Autor:** Toni Jakelić  
**Tema:** Interpolacija podataka pomoću strojnog učenja (C verzija)  
**Ukupno:** 18 radnih dana (implementacija + eksperimenti + pisanje rada)  
**+ ~3 popratna dana** — Cursor agenti (GitHub push, dokumentacija) — vidi [agents_i_dokumentacija.md](agents_i_dokumentacija.md)

> Cilj rasporeda: rad je ravnomjerno raspoređen kroz ~3 tjedna, s pauzama vikendom
> i jasnom podjelom na faze (podaci → metode → ML → eksperimenti → diplomski tekst).

---

## Pregled faza

| Faza | Dani | Kalendar (2026) | Što se radi |
|------|------|-----------------|-------------|
| **A — Priprema i podaci** | 0–3 | 5.–9. lipnja | Projekt, CSV, loader, testovi |
| **B — Klasične metode** | 4–5 | 10.–11. lipnja | Interpolacije, evaluacija |
| **C — ML metode** | 6–8 | 12.–13., 16. lipnja | KNN, RF, upgraded, Decision Tree |
| **D — Eksperimenti** | 9–12 | 17.–20. lipnja | Block missing, CSV, grafovi, analiza |
| **E — Diplomski tekst** | 13–17 | 23.–27. lipnja | Pisanje, korekture, obrana |
| **Rezerva** | 18 | 30. lipnja | Završne ispravke po feedbacku mentora |

---

## Detaljni raspored

### Tjedan 1 — Temelj projekta (5.–11. lipnja)

| Dan | Datum | Tema | Status |
|-----|-------|------|--------|
| **0** | čet 5.6. | Priprema projekta, git, struktura mape | ✅ [dan0.md](dan0.md) |
| **1** | pet 6.6. | Učitavanje podataka (Jena Climate) | ✅ [dan1.md](dan1.md) |
| **2** | sub 7.6. | Degradacija, osnovna interpolacija, evaluacija | ✅ [dan2.md](dan2.md) |
| **3** | pon 9.6. | Data loader, `run.bat`, prvi testovi | ✅ [dan3.md](dan3.md) |
| **4** | uto 10.6. | Klasične metode (linear, time, cubic, spline) | ✅ [dan4.md](dan4.md) |
| **5** | sri 11.6. | KNN u Pythonu (referenca), literatura | ✅ [dan5.md](dan5.md) |

*Vikend 8.–9.6.: agent za GitHub push (`git-sync`, Cursor hook) — [agents_i_dokumentacija.md](agents_i_dokumentacija.md)*

---

### Popratni rad — agenti (ne broje se u 18 dana teme, ali su u dnevniku)

| Razdoblje | Datum | Tema | Detalji |
|-----------|-------|------|---------|
| **Dan A** | 8.–9.6. | Agent za GitHub push | `git-sync.ps1`, hook nakon agent sesije |
| **Dan B** | 14.–15.6. | Agent za dokumentaciju | `dan*.md`, FAQ, `progress.md`, CHANGELOG |
| **Dan C** | 19.–20.6. | Raspored + izvještaj | `raspored.md`, `report.py`, `analysis.md` (uz dan 11–12) |

---

### Tjedan 2 — Strojno učenje (12.–13., 16.–20. lipnja)

| Dan | Datum | Tema | Status |
|-----|-------|------|--------|
| **6** | čet 12.6. | Osnovni KNN i Random Forest u C-u, testovi | ✅ [dan6.md](dan6.md) |
| **7** | pet 13.6. | KNN upgraded (cikličke značajke, težine) | ✅ [dan7.md](dan7.md) |
| **8** | pon 16.6. | Decision Tree imputacija | ✅ [dan8.md](dan8.md) |
| **9** | uto 17.6. | Block missing, `--experiment`, CSV export | ✅ [dan9.md](dan9.md) |
| **10** | sri 18.6. | Skalabilni `experiment.c`, `--scenario`, linear export | ✅ [dan10.md](dan10.md) |
| **11** | čet 19.6. | `report.py` — grafovi i `analysis.md` | ✅ [dan11.md](dan11.md) |
| **12** | pet 20.6. | Pregled rezultata, dorada grafova, provjera tablica | 📋 [dan12.md](dan12.md) |

*Vikend 14.–15.6.: agent za pisanje dokumentacije + ponavljanje teorije (DT, RF)*

---

### Tjedan 3 — Pisanje diplomskog (23.–30. lipnja)

| Dan | Datum | Tema | Status |
|-----|-------|------|--------|
| **13** | pon 23.6. | Uvod + pregled literature | 📋 [dan13.md](dan13.md) |
| **14** | uto 24.6. | Teorijska podloga + metodologija | 📋 [dan14.md](dan14.md) |
| **15** | sri 25.6. | Poglavlje Implementacija (dijagrami, opis modula) | 📋 [dan15.md](dan15.md) |
| **16** | čet 26.6. | Poglavlje Rezultati (tablice, slike iz `slike i videa/`) | 📋 [dan16.md](dan16.md) |
| **17** | pet 27.6. | Zaključak, sažetak, korekture, prezentacija | 📋 [dan17.md](dan17.md) |
| **18** | pon 30.6. | Rezerva — ispravke po mentoru, probna obrana | 📋 opcionalno |

*Vikend 21.–22.6.: pauza prije intenzivnog pisanja*

---

## Što je već gotovo (kod)

```
Dan 0–5   → podaci, klasične metode, evaluacija
Dan 6–8   → KNN, RF, upgraded KNN, Decision Tree
Dan 9–11  → eksperimenti, block missing, grafovi, analiza
Dan 12–17 → pisanje rada (tekst u Wordu)
```

**Kod je praktički gotov nakon Dana 11.** Dani 12–17 su za tekst, slike i obranu.

---

## Koliko sati po danu (realno)

| Tip dana | Sati | Primjer |
|----------|------|---------|
| Lakši dan | 2–3 h | literatura, dokumentacija |
| Srednji dan | 3–5 h | jedna metoda ili jedan modul |
| Teži dan | 5–6 h | ML metoda + testovi |
| Pisanje | 4–6 h | jedno poglavlje |

**Ukupno procijenjeno:** ~70–85 sati kroz 18 dana — uobičajeno za diplomski.

---

## Što još treba napraviti

### Dan 12 (kratko)
- [ ] Pokrenuti `.\report.bat` i provjeriti sve PNG-ove
- [ ] Usporediti tablice u `analysis.md` s `experiment_results.csv`
- [ ] Odlučiti koje 4–5 slika ide u rad

### Dani 13–17 (pisanje)
- [ ] Word/LaTeX predložak fakulteta
- [ ] Umetnuti tablice i slike iz `results/` i `slike i videa/`
- [ ] Prepisati nalaze iz `analysis.md` svojim riječima
- [ ] Prezentacija za obranu (8–12 slideova)

---

## Za mentora / dnevnik rada

Ako trebaš dokazivati kontinuitet, svaki dan ima zaseban `danN.md` s:
- ciljem dana,
- što je napravljeno,
- koje datoteke su mijenjane,
- što slijedi.

Raspored nije „sve u 10 dana" — implementacija traje **12 radnih dana** (5.–20. lipnja),
pisanje još **5 dana** (23.–27. lipnja), plus **~3 popratna dana** na agente i dokumentaciju
(vikendi 8.–9.6., 14.–15.6. i dio 19.–20.6.).
