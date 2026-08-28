# Prompt za Claude — analiza rezultata i poboljšanje ML modela

## Uloga

Ti si stručnjak za strojno učenje i obradu vremenskih nizova. Analiziraš rezultate
eksperimenta iz diplomskog rada o imputaciji nedostajućih temperaturnih vrijednosti.
Cilj nije napisati rad, nego **kritički analizirati zašto ML metode zaostaju i predložiti
konkretne, provedive izmjene koda** koje bi ih učinile konkurentnima.

Odgovaraj na hrvatskom jeziku. Budi konkretan i tehnički precizan. Ne izmišljaj brojke —
koristi isključivo one iz ovog prompta i priloženih datoteka.

---

## Kontekst projekta

Cijeli sustav napisan je **u čistom C-u (C99)**, bez vanjskih biblioteka (samo `libm`).
Sve metode imputacije implementirane su ručno. Python se koristi samo za grafove i tablice.

- **Dataset:** Jena Climate 2009, varijabla `T (degC)`
- **Uzorak:** 7 dana = **1008 zapisa**, interval **10 minuta**
- **Raspon temperature:** −23,01 °C do −0,63 °C (raspon 22,38 °C)
- **Standardna devijacija:** 6,059 °C
- **Prosječna promjena između dva susjedna uzorka:** 0,1407 °C
- **Autokorelacija na lag-1:** 0,99936 (signal je izrazito gladak)

### Scenariji nedostajućih podataka (5)
`random`, `block`, `block_start`, `block_middle`, `block_end`

### Missing rateovi (8)
10 %, 20 %, 30 %, 40 %, 50 %, 60 %, 70 %, 80 %

### Metode (11) — ukupno 5 × 8 × 11 = **440 testova**

| # | Metoda | Tip | Implementacija |
|---|--------|-----|----------------|
| 1 | `forward_fill` | klasična | `src/interpolation.c` |
| 2 | `linear_interpolation` | klasična | `src/interpolation.c` |
| 3 | `time_interpolation` | klasična | `src/interpolation.c` |
| 4 | `cubic_interpolation` | klasična | zaključani (clamped) spline |
| 5 | `spline_interpolation` | klasična | prirodni spline |
| 6 | `moving_average` | klasična | prozor ±6 uzoraka (1 sat) |
| 7 | `knn` | ML | `src/knn_methods.c`, k = 5 |
| 8 | `knn_upgraded` | ML | `src/knn_upgraded.c`, cikličke značajke |
| 9 | `decision_tree` | ML | `src/decision_tree.c`, dubina 5 |
| 10 | `random_forest` | ML | `src/rf_methods.c`, 8 stabala, dubina 4 |
| 11 | `adaptive_imputation` | hibridna | `src/adaptive_imputation.c` |

Evaluacija se radi **isključivo na umjetno uklonjenim pozicijama** (`mask == 1`).
Metrike: MAE, RMSE, R².

---

## Rezultati — prosječni MAE (°C) po metodi i scenariju

| Metoda | random | block | block_start | block_middle | block_end | **PROSJEK** |
|---|---|---|---|---|---|---|
| adaptive_imputation | 0,108 | 3,494 | 2,019 | 2,679 | 4,847 | **2,630** |
| linear_interpolation | 0,112 | 3,773 | 2,379 | 4,252 | 5,140 | **3,131** |
| time_interpolation | 0,112 | 3,773 | 2,379 | 4,252 | 5,140 | **3,131** |
| moving_average | 0,230 | 4,692 | 3,113 | 3,322 | 7,137 | **3,699** |
| knn | 0,236 | 3,845 | 3,220 | 4,599 | 6,794 | **3,739** |
| forward_fill | 0,273 | 4,803 | 3,182 | 3,403 | 7,271 | **3,786** |
| random_forest | 0,761 | 4,820 | 3,427 | 3,291 | 7,313 | **3,923** |
| knn_upgraded | 0,538 | 5,105 | 5,483 | 6,164 | 7,676 | **4,993** |
| decision_tree | 0,608 | 7,598 | 3,328 | 8,048 | 6,425 | **5,201** |
| cubic_interpolation | 0,115 | 11,603 | 5,777 | 5,212 | 6,646 | **5,870** |
| spline_interpolation | 0,115 | 11,603 | 8,192 | 5,212 | 7,998 | **6,624** |

### Detalj: random scenarij, MAE po missing rateu

| Metoda | 10 % | 20 % | 30 % | 40 % | 50 % | 60 % | 70 % | 80 % |
|---|---|---|---|---|---|---|---|---|
| linear | 0,063 | 0,073 | 0,083 | 0,095 | 0,102 | 0,128 | 0,177 | 0,179 |
| knn | 0,123 | 0,146 | 0,172 | 0,189 | 0,217 | 0,262 | 0,342 | 0,435 |
| knn_upgraded | 0,167 | 0,157 | 0,172 | 0,204 | 0,373 | 0,498 | 1,186 | 1,547 |
| decision_tree | 0,515 | 0,555 | 0,538 | 0,575 | 0,609 | 0,718 | 0,664 | 0,688 |
| random_forest | 0,623 | 0,700 | 0,720 | 0,738 | 0,826 | 0,764 | 0,808 | 0,912 |

---

## Nalazi do kojih smo već došli (provjeri ih i dopuni)

1. **ML metode ne koriste temperature susjednih točaka kao značajke.**
   `decision_tree` koristi `[position_norm, hour_sin, hour_cos, yday_sin, yday_cos]`,
   `random_forest` koristi `[idx, hour, yday]`. Nijedna ne vidi vrijednost signala.

2. **Stabla rade na svojoj teorijskoj granici rezolucije.**
   Dubina 5 → najviše 32 lista za 1008 točaka. Izračunata donja granica MAE za
   aproksimaciju s 32 konstantna segmenta iznosi **0,646 °C**; `decision_tree` postiže
   0,515–0,688 °C. Za 16 listova (dubina 4, kao u RF) granica je **1,084 °C**.
   Dakle riječ je o **pristranosti (underfitting)**, ne o nedostatku podataka.

3. **Pogreška ML metoda gotovo ne raste s missing rateom** (decision_tree: 0,515 → 0,688,
   samo 1,3×, dok linear raste 2,8×). Dodatna potvrda da problem nije količina podataka.

4. **KNN je degenerirao u pomični prosjek.** Značajke u `feature_distance_sq` nisu
   skalirane, pa razlika u poziciji (stotine) nadjačava sat (0–23) i dan. Posljedica:
   `knn` (0,236) i `moving_average` (0,230) na random scenariju daju gotovo isti rezultat.

5. **Neponderirani prosjek k = 5 je estimator nultog reda.** Na sintetički savršeno
   linearnom signalu linearna interpolacija ima MAE = 0,00000, a KNN k = 5 ima
   MAE = 0,07952. KNN ne može reproducirati pravac. Uz k = 2 KNN postiže 0,0580 naspram
   0,0570 za linear — dakle praktički se izjednači.

6. **Na block scenarijima ML je robusniji od splineova.** `random_forest` (4,820) je bolji
   od `cubic` (11,603) i `spline` (11,603) jer stabla ne mogu predvidjeti vrijednost izvan
   raspona viđenih temperatura, dok globalni splineovi divlje overshootaju.

7. **`knn_upgraded` je lošiji od osnovnog `knn` na svim scenarijima** (4,993 vs 3,739).
   Vjerojatan uzrok: normirane cikličke značajke daju satu i danu stvarnu težinu, pa
   metoda povlači točke iz istog sata drugih dana, koji zbog vremenskog trenda tijekom
   tjedna imaju bitno drugačiju temperaturu.

---

## Tvoji zadaci

### 1. Kritička provjera nalaza
Prođi kroz svih 7 nalaza iznad. Za svaki reci slažeš li se, i **je li obrazloženje potpuno**.
Ako misliš da je neki zaključak pogrešan ili prebrz, reci zašto i predloži test kojim bi se
provjerio. Posebno me zanima jesam li negdje zamijenio uzrok i posljedicu.

### 2. Analiza koda
Pregledaj implementacije u `src/knn_methods.c`, `src/knn_upgraded.c`, `src/decision_tree.c`
i `src/rf_methods.c`. Traži:
- **stvarne bugove** (ne samo suboptimalne izbore)
- curenje informacija ili nekorektnu evaluaciju
- mjesta gdje implementacija odstupa od standardne definicije algoritma
- problem s `fill_remaining_gaps` — je li fallback na forward/backward fill maskirao
  stvarne performanse metode i koliko često se uopće aktivira

### 3. Konkretni prijedlozi poboljšanja
Za svaki prijedlog navedi:
- **što točno promijeniti** (datoteka, funkcija, konkretna izmjena)
- **očekivani učinak** na MAE i na kojim scenarijima
- **rizik** (može li pogoršati neki drugi scenarij)
- **procjenu složenosti** implementacije u C-u bez vanjskih biblioteka

Rangiraj prijedloge po omjeru dobitka i uloženog truda. Zanimaju me osobito:
- dodavanje **lag/lead značajki** (vrijednosti susjeda) u stabla i šumu
- **ponderiranje po udaljenosti** i izbor k u KNN-u
- **skaliranje/normalizacija značajki** u KNN-u
- dublja stabla, više stabala, `max_features` po splitu, pruning
- je li smisleno da stablo predviđa **lokalni nagib umjesto konstante**
  (npr. linearni model u listu — model tree)
- kako uopće tretirati block scenarije, gdje je nužna ekstrapolacija

### 4. Poštena usporedba
Predloži kako postaviti eksperiment da usporedba ML-a i klasičnih metoda bude metodološki
korektna. Konkretno:
- treba li ML metodama dati iste informacije koje koristi interpolacija
- kako izbjeći curenje informacija kod lag značajki kada susjed također nedostaje
- treba li uvesti validacijski skup za odabir hiperparametara i kako, s obzirom na to da
  je riječ o imputaciji, a ne o klasičnoj predikciji
- je li R² dobra metrika ovdje (svi su iznosi negativni — objasni zašto i predloži bolju)

### 5. Realna očekivanja
Odgovori izravno: **mogu li ML metode uopće nadmašiti linearnu interpolaciju na ovom
problemu?** Ako da, uz koje izmjene i na kojim scenarijima. Ako ne, objasni zašto je to
teorijski očekivano i kako to korektno formulirati u diplomskom radu, bez da zvuči kao
da je eksperiment neuspio.

---

## Format odgovora

1. **Sažetak** — 5 do 8 rečenica, glavni zaključak
2. **Provjera nalaza** — po točkama, slažem se / ne slažem se + obrazloženje
3. **Pronađeni problemi u kodu** — poredani po ozbiljnosti
4. **Prijedlozi poboljšanja** — tablica: prijedlog / očekivani učinak / rizik / složenost
5. **Preporučeni redoslijed implementacije** — što napraviti prvo
6. **Odgovor na pitanje iz zadatka 5**

---

## Prilozi koje treba priložiti uz ovaj prompt

**Obavezno:**
- `results/experiment_results.csv` — svih 440 redaka
- `src/knn_methods.c`, `src/knn_upgraded.c`
- `src/decision_tree.c`, `src/rf_methods.c`
- `src/experiment.c` — okvir eksperimenta i evaluacija

**Korisno:**
- `src/interpolation.c` — za usporedbu s klasičnim metodama
- `src/adaptive_imputation.c` — hibridna metoda
- `results/tablice/sve_tablice_pregled.md`
- `results/novo_za_diplomski.md`
- `data/processed/jena_temperature_7d.csv` — sami podaci
