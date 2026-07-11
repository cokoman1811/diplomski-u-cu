# Prompt za ChatGPT — nadopuna diplomskog rada

## Uloga
Ti si asistent za pisanje diplomskog rada na hrvatskom jeziku. Diplomski rad je **već napisan** — tvoj zadatak je samo nadopuniti poglavlja 5–7 novim rezultatima, tablicama i grafovima.

## Važno
- **Ne izmišljaj brojke** — koristi isključivo priložene CSV/MD datoteke
- Ne piši rad ispočetka; zadrži postojeći stil i strukturu
- Svaki graf: naslov (Slika X.), kratko tumačenje (2–4 rečenice) s konkretnim brojevima
- Numeriraj slike kontinuirano u poglavlju Rezultati

## Kontekst eksperimenta (ažurirano)
- **Dataset:** Jena Climate, temperatura, **7 dana** (1008 zapisa, 10-min intervali)
- **Scenariji:** random, block, block_start, block_middle, block_end
- **Missing rateovi:** 10 %, 20 %, 30 %, 40 %, 50 %, 60 %, 70 %, 80 %
- **Metode (11):**
  1. forward_fill
  2. linear_interpolation
  3. time_interpolation
  4. cubic_interpolation (zaključani spline)
  5. spline_interpolation (prirodni spline)
  6. **moving_average** (pomični prosjek, prozor 6 = 1 sat) — NOVO
  7. **knn** (osnovni KNN, k=5) — NOVO u eksperimentu
  8. **knn_upgraded** (napredni KNN: cikličke značajke, težinski prosjek) — NOVO u eksperimentu
  9. decision_tree
  10. random_forest
  11. **adaptive_imputation** (hibridna metoda — automatski bira najbolju metodu)
- **Ukupno testova:** 5 scenarija × 8 rateova × 11 metoda = **440**

## Što napraviti

### 1. Tablice
- Dodaj/ažuriraj tablice za sve missing rateove (10–80 %)
- Uključi sažetak po metodama iz `sve_tablice_pregled.md`
- Istakni da **adaptive_imputation** ima najniži prosječni MAE

### 2. Usporedba KNN (obavezno)
- Usporedi **knn** (osnovni) i **knn_upgraded** (napredni) u istom eksperimentalnom okviru
- Na random scenariju: koji je bolji pri kojim rateovima?
- Na block scenarijima: objasni zašto oba KNN-a padaju pri visokim rateovima
- Navedi konkretne MAE/R² vrijednosti iz CSV-a

### 3. Pomični prosjek (obavezno)
- Objasni metodu: za svaku rupu uzima prosjek poznatih vrijednosti u prozoru ±6 uzoraka (1 sat)
- Usporedi s forward_fill i linear_interpolation
- Kada je dobar, a kada loš (block scenariji)?

### 4. Grafovi
Umetni PNG grafove iz zipa:
- `mae_overview_{scenario}.png` — pregled MAE po metodama
- `mae_vs_rate_{scenario}_all.png` — MAE vs missing rate
- `rmse_vs_rate_{scenario}_all.png`, `r2_vs_rate_{scenario}_all.png`
- `mae_by_method_{scenario}_20.png` — usporedba pri 20 %

### 5. Zaključak budućeg rada
Spomeni kao budući rad (ne kao implementirano):
- Dulji vremenski nizovi
- Više meteoroloških varijabli
- Stvarni nedostajući podaci (ne umjetno uklanjanje)

## Ključne tvrdnje (provjeri u CSV-u prije pisanja)
- adaptive_imputation pobjeđuje sve pojedinačne metode u prosjeku
- linear/time dominiraju na random scenariju pri visokim rateovima
- block_end i block_middle najteži scenariji pri 70–80 %
- KNN na block scenarijima značajno gori od interpolacije

## Izlaz
- Ažurirani Word dokument s tablicama, grafovima i tumačenjima
- Kratki PDF pregled (ako možeš)
