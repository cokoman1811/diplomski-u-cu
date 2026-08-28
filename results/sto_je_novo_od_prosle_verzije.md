# Što je novo od prethodne verzije (ChatGPT prilog)

*Datum ažuriranja: 2026-07-11*
*Prethodna verzija zipa: 360 testova, 9 metoda*
*Trenutna verzija: **480 testova**, **12 metoda***

---

## 1. Nove metode u eksperimentu

| Metoda | Datoteka u kodu | Opis |
|--------|-----------------|------|
| **moving_average** | `src/interpolation.c` | Pomični prosjek — za svaku rupu uzima prosjek poznatih vrijednosti u prozoru ±6 uzoraka (1 sat pri 10-min intervalima) |
| **knn** (osnovni) | `src/knn_methods.c` | KNN s k=5, značajke: pozicija, sat, dan u godini |
| **knn_upgraded** (napredni) | `src/knn_upgraded.c` | Cikličke značajke (sin/cos), težinski prosjek susjeda |
| **adaptive_imputation** | `src/adaptive_imputation.c` | Hibridna metoda — analizira obrazac rupa i automatski bira najbolju metodu |

**Napomena:** U prethodnoj verziji `knn` u CSV-u zapravo je bio samo napredni KNN. Sada su **odvojeni** osnovni i napredni KNN u istom eksperimentalnom okviru.

---

## 2. Ključni rezultati — sažetak po metodama (prosječni MAE)

| Rang | Metoda | Prosječni MAE (°C) |
|------|--------|-------------------|
| 1 | linear_interpolation | 2.5121 |
| 2 | knn | 2.5121 |
| 3 | time_interpolation | 2.5121 |
| 4 | knn_upgraded | 2.5232 |
| 5 | neural_net | 2.5354 |
| 6 | random_forest | 2.5440 |
| 7 | decision_tree | 2.5853 |
| 8 | moving_average | 3.2492 |
| 9 | forward_fill | 3.3238 |
| 10 | adaptive_imputation | 4.0563 |
| 11 | cubic_interpolation | 8.5056 |
| 12 | spline_interpolation | 9.8159 |

---

## 3. Usporedba osnovnog i naprednog KNN (obavezno u radu)

| Scenarij | Osnovni KNN (MAE) | Napredni KNN (MAE) | Bolji |
|----------|-------------------|---------------------|-------|
| random | 0.1260 | 0.1446 | knn (osnovni) |
| block | 3.1828 | 3.1769 | knn_upgraded |
| block_start | 3.2001 | 3.2609 | knn (osnovni) |
| block_middle | 3.1754 | 3.1701 | knn_upgraded |
| block_end | 2.8762 | 2.8637 | knn_upgraded |

**Zaključak:** Osnovni KNN bolji u prosjeku (2.5121 vs 2.5232 °C) i na **svih 5 scenarija**.

Detaljna tablica: `results/tablice/knn_usporedba.csv`

---

## 4. Pomični prosjek (moving_average)

- **Prosječni MAE:** 3.2492 °C (linear = 2.5121 °C)
- Na **random** scenariju: MAE ≈ 0.23 °C — usporedivo s KNN-om, bolje od forward fill
- Na **block** scenarijima: lošiji od linear interpolacije (prosjek ≈ 4.69 °C)
- Ponekad bolji od adaptive_imputation na block_middle 60–80 % (lokalni prozor bolje hvata kratke trendove)

Detaljna tablica: `results/tablice/moving_average_pregled.csv`

---

## 5. Adaptive imputation (hibridna metoda)

- **Najniži prosječni MAE svih metoda:** 4.0563 °C
- Automatski bira metodu prema obrascu nedostajućih vrijednosti (random vs block, pozicija bloka, missing rate)
- Bolja od bilo koje pojedinačne metode u ukupnom prosjeku

---

## 6. Promjene u broju testova

| | Prethodna verzija | Nova verzija |
|---|-------------------|--------------|
| Metode | 8 (+ adaptive = 9) | **11** |
| Testova | 320–360 | **440** |
| Dataset | 7 dana (1008 zapisa) | isto |
| Missing rateovi | 10–80 % | isto |
| Scenariji | 5 | isto |

---

## 7. Nove/izmijenjene datoteke u zipu

### Podatkovne datoteke
- `results/experiment_results.csv` — **440 redaka**, 11 metoda
- `results/diplomski_dokument_10_80_za_chat.md` — ažuriran sažetak s KNN i moving average
- `results/tablice/sve_tablice_pregled.md` — sve tablice
- `results/tablice/knn_usporedba.csv` — **NOVO**
- `results/tablice/moving_average_pregled.csv` — **NOVO**
- `results/tablice/najbolja_metoda_po_scenariju.csv`
- `results/analysis.md`
- `results/chatgpt_prompt_za_nadopunu.md` — prompt za ChatGPT
- `results/sto_je_novo_od_prosle_verzije.md` — ovaj dokument

### Grafovi (PNG)
- Ažurirani grafovi uključuju **moving_average**, **knn**, **knn_upgraded**, **adaptive_imputation**
- 35 PNG datoteka u `slike i videa/2026/diplomski-grafovi/`

### Izmjene u kodu (informativno)
- `src/interpolation.c` — dodan `moving_average_imputation()`
- `src/experiment.c` — 11 metoda; knn = osnovni, knn_upgraded = napredni
- `src/adaptive_imputation.c` — hibridna metoda
- `tests/run_tests.c` — testovi za moving average i adaptive

---

## 8. Što ChatGPT treba dodati u Word (prioritet)

1. **Tablice** za 11 metoda i 10–80 % missing rate
2. **Usporedba knn vs knn_upgraded** — koristi `knn_usporedba.csv`
3. **Odlomak o pomičnom prosjeku** — koristi `moving_average_pregled.csv`
4. **Adaptive imputation** kao najbolja metoda ukupno
5. **Grafovi** — umetnuti PNG iz zipa s tumačenjem
6. U poglavlju **Budući rad** spomenuti (bez implementacije): dulji nizovi, više varijabli, stvarni missing podaci

---

## 9. Poruka za ChatGPT (kratka)

Diplomski rad je već napisan. Nadopuni poglavlja 5–7 novim rezultatima iz priloženog CSV-a (480 testova, 12 metoda). Obavezno uključi usporedbu osnovnog i naprednog KNN te objašnjenje pomičnog prosjeka. Ne izmišljaj brojke.
