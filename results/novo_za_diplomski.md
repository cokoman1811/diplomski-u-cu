# Novo u eksperimentima — tekst za diplomski rad

*Automatski generirano iz `experiment_results.csv`*
*Kopiraj odlomke u poglavlja Metodologija, Rezultati, Rasprava i Zaključak*

---

## A. Kratki sažetak novina (1 odlomak)

U odnosu na raniju verziju eksperimenata, rad je proširen na **7-dnevni** Jena Climate dataset (**1008** zapisa, 10-min intervali), missing rateove **10–80 %**, te **11 metoda imputacije** u **5 scenarija** (ukupno **440** testova). Dodane su metode **pomičnog prosjeka**, **adaptivne hibridne imputacije** te odvojena usporedba **osnovnog i naprednog KNN-a**. Razdvojene su **zaključana kubična** (`cubic_interpolation`) i **prirodna spline** (`spline_interpolation`) interpolacija. Za svaki scenarij generirani su grafovi rekonstrukcije **najbolje i najgore** metode pri 20 % nedostajućih vrijednosti.

---

## B. Metodologija — što dodati

### B.1 Dataset
- Izvor: Jena Climate Dataset (2009), temperatura `T (degC)`
- Period: **7 dana** (1008 uzoraka, interval 10 min)
- Datoteka: `data/processed/jena_temperature_7d.csv`

### B.2 Scenariji i missing rateovi
- Scenariji: `random`, `block`, `block_start`, `block_middle`, `block_end`
- Missing rateovi: **10 %, 20 %, 30 %, 40 %, 50 %, 60 %, 70 %, 80 %**
- Evaluacija isključivo na umjetno uklonjenim mjestima (`mask == 1`)

### B.3 Metode (11)

| # | Metoda | Kratki opis |
|---|--------|-------------|
| 1 | forward_fill | Zadnja poznata vrijednost |
| 2 | linear_interpolation | Linearna interpolacija po indeksu |
| 3 | time_interpolation | Linearna interpolacija po vremenu |
| 4 | cubic_interpolation | Zaključani kubični spline |
| 5 | spline_interpolation | Prirodni kubični spline |
| 6 | **moving_average** | Pomični prosjek (prozor ±6 = 1 h) — **NOVO** |
| 7 | **knn** | Osnovni KNN, k=5 — **NOVO u eksperimentu** |
| 8 | **knn_upgraded** | Napredni KNN (cikličke značajke) — **NOVO u eksperimentu** |
| 9 | decision_tree | Stablo odlučivanja |
| 10 | random_forest | Slučajna šuma |
| 11 | **adaptive_imputation** | Hibridna metoda — **NOVO** |

### B.4 Adaptivna imputacija (nova metoda)
Metoda `adaptive_imputation` analizira masku nedostajućih vrijednosti (stopa, veličina i pozicija najvećeg bloka) i automatski odabire jednu od poznatih metoda imputacije prema unaprijed definiranoj tablici routing pravila.

### B.5 Pomični prosjek (nova metoda)
Za svaku nedostajuću točku uzima se prosjek poznatih susjeda u prozoru **±6 uzoraka** (1 sat pri 10-min intervalima).

---

## C. Rezultati — ključne brojke

### C.1 Rang metoda po prosječnom MAE (svi scenariji i rateovi)

| Rang | Metoda | Prosječni MAE (°C) |
|------|--------|-------------------|
| 1 | `adaptive_imputation` | 2.6295 |
| 2 | `linear_interpolation` | 3.1315 |
| 3 | `time_interpolation` | 3.1315 |
| 4 | `moving_average` | 3.6985 |
| 5 | `knn` | 3.7387 |
| 6 | `forward_fill` | 3.7863 |
| 7 | `random_forest` | 3.9226 |
| 8 | `knn_upgraded` | 4.9931 |
| 9 | `decision_tree` | 5.2013 |
| 10 | `cubic_interpolation` | 5.8704 |
| 11 | `spline_interpolation` | 6.6240 |

### C.2 Najbolja pojedinačna metoda po broju pobjeda (po scenariju i rateu)
- **linear_interpolation**: 15 od 40 kombinacija scenarij/rate
- **adaptive_imputation**: 0 pojedinačnih pobjeda, ali **najniži ukupni prosjek MAE: 2.6295 °C** (hibridna metoda je konzistentno dobra, iako ne uvijek prva u svakoj kombinaciji)
- **cubic_interpolation**: 7 pobjeda
- **spline_interpolation**: 5 pobjeda

### C.3 Identični rezultati
- **linear_interpolation** i **time_interpolation** daju **identične** rezultate na svim scenarijima (ravnomjerni 10-min intervali).
- Na scenariju **block**, **cubic_interpolation** i **spline_interpolation** također daju identične rezultate.

### C.4 Usporedba osnovnog i naprednog KNN

| Scenarij | Osnovni KNN | Napredni KNN | Bolji |
|----------|-------------|--------------|-------|
| random | 0.2358 | 0.5381 | knn (osnovni) |
| block | 3.8452 | 5.1048 | knn (osnovni) |
| block_start | 3.2199 | 5.4829 | knn (osnovni) |
| block_middle | 4.5991 | 6.1636 | knn (osnovni) |
| block_end | 6.7937 | 7.6762 | knn (osnovni) |

**Zaključak:** Osnovni KNN postiže niži prosječni MAE (**3.7387** vs **4.9931** °C) na svih 5 scenarija. Napredne značajke (sin/cos, težinski prosjek) nisu poboljšale imputaciju na ovom skupu podataka.

### C.5 Pomični prosjek
- Prosječni MAE: **3.6985 °C** (linear: **3.1315 °C**)
- Dobar na **random** scenariju (MAE ≈ 0,23 °C)
- Lošiji od linear interpolacije na **block** scenarijima

### C.6 Najbolja i najgora metoda po scenariju @ 20 %

- **random** @ 20 %: najbolja **spline_interpolation** (MAE = 0.0635 °C), najgora **random_forest** (MAE = 0.7003 °C)
- **block** @ 20 %: najbolja **linear_interpolation** (MAE = 1.4765 °C), najgora **cubic_interpolation** (MAE = 4.2442 °C)
- **block_start** @ 20 %: najbolja **linear_interpolation** (MAE = 0.6991 °C), najgora **knn_upgraded** (MAE = 2.3690 °C)
- **block_middle** @ 20 %: najbolja **linear_interpolation** (MAE = 1.1449 °C), najgora **knn_upgraded** (MAE = 5.3844 °C)
- **block_end** @ 20 %: najbolja **cubic_interpolation** (MAE = 4.1828 °C), najgora **spline_interpolation** (MAE = 8.3969 °C)

---

## D. Rasprava — gotovi odlomci za kopiranje

### D.1 Adaptivna imputacija
Adaptivna hibridna metoda postigla je najniži prosječni MAE (**2.6295 °C**) među svim testiranim metodama, što potvrđuje hipotezu da nijedna pojedinačna metoda nije optimalna za sve obrasce nedostajućih podataka. Metoda automatski prepoznaje je li riječ o random ili block scenariju te odabire prikladnu strategiju imputacije.

### D.2 Kubična interpolacija na block scenariju
Na scenariju **block** pri 20 % nedostajućih vrijednosti, zaključani kubični spline postiže MAE od **4.2442 °C**, dok linear interpolacija postiže **1.4765 °C**. Kubična metoda gradi globalnu glatku krivulju kroz cijeli vremenski niz; zakrivljenost iz hladnijih perioda izvan bloka može uzrokovati overshoot unutar rupe — krivulja pada prema hladnijim vrijednostima iako unutar bloka temperatura ne slijedi taj trend. To objašnjava zašto cubic na ovom scenariju vizualno „ide dolje” unatoč toplijem vrhuncu unutar rupe.

### D.3 Linear vs time
Budući da su vremenski uzorci ravnomjerno raspoređeni (10-min intervali), linear i time interpolacija daju identične rezultate u svim eksperimentima. U praksi je dovoljno prikazati jednu od te dvije metode.

### D.4 KNN — osnovni vs napredni
U eksperimentu je provedena izravna usporedba osnovnog KNN-a (k=5, značajke: pozicija, sat, dan) i naprednog KNN-a (cikličke značajke, težinski prosjek). Rezultati pokazuju da je **osnovni KNN bolji** na svim scenarijima, što sugerira da dodatna složenost napredne varijante nije opravdana na kratkom 7-dnevnom nizu s jednom varijablom.

### D.5 Pomični prosjek
Pomični prosjek pokazuje prihvatljive rezultate na random scenariju, ali značajno gori od linear interpolacije na block scenarijima. Metoda je prikladna za kratke rupe u nizu, ali ne za duge kontinuirane blokove nedostajućih vrijednosti.

---

## E. Zaključak — što dodati

1. Eksperimenti obuhvaćaju **440** testova (5 scenarija × 8 rateova × 11 metoda) na **7-dnevnom** datasetu.
2. **Adaptivna imputacija** ima najniži prosječni MAE (**2.6295 °C**).
3. **Linear interpolacija** ostaje najstabilnija pojedinačna metoda (15 pobjeda po MAE).
4. **Osnovni KNN** nadmašuje napredni KNN na svim scenarijima.
5. **Kubična interpolacija** loša je na block scenariju zbog globalnog overshoota; dobra je na block_end scenariju.
6. **Pomični prosjek** koristan na random scenariju, ne i na block scenarijima.

---

## F. Budući rad (preporučeni odlomak)

Budući rad mogao bi uključiti dulje vremenske nizove, više meteoroloških varijabli i stvarne nedostajuće podatke (umjesto umjetnog uklanjanja). Također bi bilo korisno testirati lokalne umjesto globalnih spline metoda te proširiti adaptivnu imputaciju učenjem routing pravila iz podataka.

---

## G. Grafovi i prilozi

- Stupčasti grafovi: svih 11 metoda, svaka svojom bojom (`mae_by_method_*_20.png`)
- Linijski grafovi: MAE/RMSE/R² vs missing rate; identične metode označene u legendi
- Rekonstrukcija @ 20 %: najbolja vs najgora metoda po scenariju (`reconstruction_best_worst_*.png`)
- Pregled: `results/grafovi_pregled.html`
- Tablice: `results/tablice/sve_tablice_pregled.md`

---

## H. Popis novih datoteka u projektu

| Datoteka | Svrha |
|----------|-------|
| `src/adaptive_imputation.c` | Adaptivna hibridna metoda |
| `src/interpolation.c` | + `moving_average_imputation()` |
| `src/experiment.c` | 11 metoda, export najbolje/najgore rekonstrukcije |
| `results/reconstruction_best_worst_20.csv` | Pregled najbolje/najgore @ 20 % |
| `results/tablice/knn_usporedba.csv` | KNN osnovni vs napredni |
| `results/tablice/moving_average_pregled.csv` | Pomični prosjek vs linear |
