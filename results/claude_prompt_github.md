# Prompt za Claude — analiza repozitorija i poboljšanje ML modela

> Zalijepi cijeli tekst ispod ove linije u Claude, uz pristup repozitoriju
> `https://github.com/cokoman1811/diplomski-u-cu`

---

Analiziraj moj GitHub repozitorij `cokoman1811/diplomski-u-cu`.

## Uloga i cilj

Ti si stručnjak za strojno učenje i obradu vremenskih nizova. Ovo je kod za diplomski rad
o imputaciji nedostajućih temperaturnih vrijednosti, napisan **u čistom C-u (C99), bez
vanjskih biblioteka** (samo `libm`). Python se koristi isključivo za grafove i tablice.

Problem koji istražujem: **metode strojnog učenja daju osjetno lošije rezultate od
jednostavne linearne interpolacije.** Tvoj zadatak je utvrditi zašto i predložiti konkretne
izmjene koda koje bi ML metode učinile konkurentnima.

Odgovaraj na hrvatskom jeziku. Budi tehnički precizan i kritičan. **Ne izmišljaj brojke** —
sve vrijednosti izračunaj ili pročitaj iz datoteka u repozitoriju.

---

## Datoteke koje trebaš pročitati

### Prioritet 1 — implementacije ML metoda
```
src/knn_methods.c        KNN, k = 5
src/knn_upgraded.c       napredni KNN s cikličkim značajkama
src/decision_tree.c      stablo odlučivanja, dubina 5
src/rf_methods.c         slučajna šuma, 8 stabala, dubina 4
```

### Prioritet 2 — okvir eksperimenta i evaluacija
```
src/experiment.c         generiranje maski, petlja eksperimenta, izvoz rezultata
src/experiment.h
src/evaluation.c         izračun MAE, RMSE, R²
src/series.h             struktura podataka
```

### Prioritet 3 — klasične metode za usporedbu
```
src/interpolation.c      forward_fill, linear, time, cubic, spline, moving_average
src/adaptive_imputation.c   hibridna metoda koja bira strategiju prema maski
```

### Prioritet 4 — podaci i rezultati
```
results/experiment_results.csv        440 redaka, svi rezultati
results/tablice/sve_tablice_pregled.md
results/novo_za_diplomski.md          dosadašnji zaključci
data/processed/jena_temperature_7d.csv   ulazni podaci, 1008 zapisa
```

### Ignoriraj
Datoteke koje nisu vezane uz diplomski: `results/c_disk_*`, `results/program*`,
`results/users_profiles_audit.md`, `results/move_to_d_*`, `results/autocad-*`,
`results/_pf_scan.csv`, `results/_uninstall_reg.json`, `scripts/organize-media-*`.

---

## Kontekst eksperimenta

- **Dataset:** Jena Climate 2009, varijabla `T (degC)`
- **Uzorak:** 7 dana = 1008 zapisa, interval 10 minuta
- **Scenariji (5):** `random`, `block`, `block_start`, `block_middle`, `block_end`
- **Missing rateovi (8):** 10 % do 80 %
- **Metode (11):** forward_fill, linear, time, cubic, spline, moving_average, knn,
  knn_upgraded, decision_tree, random_forest, adaptive_imputation
- **Ukupno:** 5 × 8 × 11 = 440 testova
- Evaluacija se radi **samo na umjetno uklonjenim pozicijama** (`mask == 1`)

Svojstva signala koja sam izmjerio (provjeri ih):
autokorelacija lag-1 = 0,99936; prosječna promjena između susjednih uzoraka = 0,1407 °C;
standardna devijacija = 6,059 °C; raspon = 22,38 °C.

---

## Rezultati — prosječni MAE (°C)

Izračunaj ovu tablicu sam iz `results/experiment_results.csv` i **usporedi s mojim
vrijednostima**; ako se ne poklapaju, javi.

| Metoda | random | block | block_start | block_middle | block_end | PROSJEK |
|---|---|---|---|---|---|---|
| adaptive_imputation | 0,108 | 3,494 | 2,019 | 2,679 | 4,847 | **2,630** |
| linear_interpolation | 0,112 | 3,773 | 2,379 | 4,252 | 5,140 | **3,131** |
| moving_average | 0,230 | 4,692 | 3,113 | 3,322 | 7,137 | **3,699** |
| knn | 0,236 | 3,845 | 3,220 | 4,599 | 6,794 | **3,739** |
| forward_fill | 0,273 | 4,803 | 3,182 | 3,403 | 7,271 | **3,786** |
| random_forest | 0,761 | 4,820 | 3,427 | 3,291 | 7,313 | **3,923** |
| knn_upgraded | 0,538 | 5,105 | 5,483 | 6,164 | 7,676 | **4,993** |
| decision_tree | 0,608 | 7,598 | 3,328 | 8,048 | 6,425 | **5,201** |
| cubic_interpolation | 0,115 | 11,603 | 5,777 | 5,212 | 6,646 | **5,870** |
| spline_interpolation | 0,115 | 11,603 | 8,192 | 5,212 | 7,998 | **6,624** |

Ključno zapažanje: **sve četiri ML metode lošije su od linearne interpolacije u prosjeku**,
a na random scenariju razlika je dramatična (linear 0,112 naspram random_forest 0,761).

---

## Hipoteze do kojih sam došao — provjeri ih u kodu

1. **ML metode ne koriste vrijednosti susjednih točaka kao značajke.** Čini mi se da
   `decision_tree` koristi samo `[position_norm, hour_sin, hour_cos, yday_sin, yday_cos]`,
   a `random_forest` samo `[idx, hour, yday]`. Nijedna ne vidi samu temperaturu susjeda.

2. **Stabla su ograničena rezolucijom.** Dubina 5 daje najviše 32 lista za 1008 točaka.
   Izračunao sam da je donja granica MAE za aproksimaciju s 32 konstantna segmenta
   0,646 °C, a `decision_tree` postiže 0,515–0,688 °C. Dakle underfitting, ne nedostatak
   podataka. Provjeri taj izračun.

3. **Pogreška ML metoda gotovo ne raste s missing rateom.** decision_tree ide od 0,515
   pri 10 % do 0,688 pri 80 % (1,3×), dok linear raste 2,8×. Potvrda da problem nije
   količina podataka nego pristranost modela.

4. **KNN je degenerirao u pomični prosjek.** Značajke u `feature_distance_sq` nisu
   skalirane, pa razlika u poziciji (stotine) nadjačava sat (0–23) i dan. Posljedica:
   `knn` (0,236) i `moving_average` (0,230) daju gotovo isti rezultat na random scenariju.

5. **Neponderirani prosjek k = 5 je estimator nultog reda.** Na sintetički savršeno
   linearnom signalu linearna interpolacija ima MAE = 0,00000, a KNN k = 5 ima 0,07952 —
   KNN ne može reproducirati pravac. S k = 2 KNN postiže 0,0580 naspram 0,0570 za linear.

6. **Na block scenarijima ML je robusniji od splineova**, jer stabla ne mogu predvidjeti
   vrijednost izvan raspona viđenih temperatura, dok globalni splineovi overshootaju.

7. **`knn_upgraded` je lošiji od osnovnog `knn` na svim scenarijima** (4,993 vs 3,739).
   Sumnjam da normirane cikličke značajke daju satu i danu preveliku težinu, pa metoda
   povlači točke iz istog sata drugih dana koje imaju bitno drugačiju temperaturu.

---

## Zadaci

### 1. Provjera hipoteza
Prođi kroz svih 7 hipoteza. Za svaku reci **slažeš li se, na temelju čega u kodu**, i je li
obrazloženje potpuno. Ako je neki zaključak pogrešan ili prebrz, reci zašto. Posebno me
zanima jesam li negdje zamijenio uzrok i posljedicu.

### 2. Pregled koda — traži stvarne probleme
Ne zanimaju me stilske primjedbe. Traži:
- **bugove** u implementaciji algoritama
- odstupanja od standardne definicije KNN-a, stabla odlučivanja i slučajne šume
- **curenje informacija** ili nekorektnu evaluaciju u `src/experiment.c`
- funkciju `fill_remaining_gaps` koja postoji u sve četiri ML datoteke: radi forward/backward
  fill nad onim što metoda nije popunila. **Koliko se često aktivira i maskira li stvarne
  performanse metode?** Ovo mi je najsumnjivije mjesto.
- je li usporedba metoda uopće poštena s obzirom na to koje informacije koja metoda dobiva

### 3. Konkretni prijedlozi poboljšanja
Za svaki prijedlog navedi: **datoteku i funkciju**, točnu izmjenu, očekivani učinak na MAE
i na kojim scenarijima, rizik pogoršanja drugdje, te složenost implementacije u C-u bez
vanjskih biblioteka. Rangiraj po omjeru dobitka i uloženog truda.

Zanimaju me osobito:
- dodavanje **lag/lead značajki** (vrijednosti susjeda) u stabla i šumu
- **ponderiranje po udaljenosti** i izbor k u KNN-u
- **skaliranje značajki** u KNN-u
- dublja stabla, više stabala, `max_features` po splitu, pruning
- **model tree** — linearni model u listu umjesto konstante
- kako tretirati block scenarije, gdje je nužna ekstrapolacija

### 4. Metodološka korektnost
- Trebaju li ML metode dobiti iste informacije koje koristi interpolacija?
- Kako izbjeći curenje informacija kod lag značajki **kada susjed također nedostaje**?
- Treba li validacijski skup za hiperparametre i kako ga postaviti kod imputacije?
- **Zašto su svi R² negativni** (provjeri u CSV-u) i je li R² uopće dobra metrika ovdje?
  Predloži bolju.

### 5. Realna očekivanja
Odgovori izravno: **mogu li ML metode uopće nadmašiti linearnu interpolaciju na ovom
problemu?** Ako da — uz koje izmjene i na kojim scenarijima. Ako ne — objasni zašto je to
teorijski očekivano i kako to korektno formulirati u diplomskom radu, a da ne zvuči kao
neuspio eksperiment.

---

## Format odgovora+                    
Ako predlažeš izmjenu koda, napiši **konkretan C kod** koji se uklapa u postojeći stil
(C99, bez vanjskih biblioteka, `Series` struktura iz `src/series.h`).
