# Dan 8 — Decision Tree imputacija

**Datum:** 2026-06-16  
**Autor:** Toni Jakelić  
**Tema dana:** dodavanje Decision Tree metode za imputaciju temperature

---

## 1. Cilj dana

Dodati **Decision Tree** kao novu ML metodu za popunjavanje nedostajućih temperatura.
Metoda se uklapa u postojeći tok (`damaged` → imputacija → `evaluate_reconstruction`) i
pojavljuje se u `--compare` tablici uz KNN i ostale metode.

---

## 2. Zašto Decision Tree ima smisla u radu

| Pristup | Ideja |
|---------|-------|
| **KNN** | Traži k najsličnija poznata mjerenja i uzima prosjek |
| **Decision Tree** | Uči **pravila** iz poznatih podataka (npr. „ako je sat ≤ 12, temp ≈ X”) |
| **Random Forest** (već u projektu) | Proširenje — više stabala + prosjek (manje overfittinga) |

Decision Tree je dobar korak između KNN-a i Random Foresta: jednostavan za objasniti,
a ipak ML metoda koja koristi značajke vremena.

---

## 3. Koje značajke koristi

Iste **napredne cikličke značajke** kao `knn_upgraded` (usporedivost ML metoda):

| Indeks | Značajka | Formula |
|--------|----------|---------|
| 0 | position_norm | `index / (n - 1)` |
| 1 | hour_sin | `sin(2π · hour / 24)` |
| 2 | hour_cos | `cos(2π · hour / 24)` |
| 3 | yday_sin | `sin(2π · (yday-1) / 365)` |
| 4 | yday_cos | `cos(2π · (yday-1) / 365)` |

Hour i yday su cikličke — sin/cos hvata blizinu 23:00↔00:00 i 365.↔1. dan.

---

## 4. Kako metoda radi

```
1. Kopiraj damaged → out
2. Prikupi indekse poznatih (ne-NaN) temperatura
3. Na tim indeksima izgradi regresijsko stablo:
   - čvor: feature <= threshold → lijevo, inače desno
   - list: prosječna temperatura uzoraka u listu
   - kriterij podjele: minimalna suma kvadratnih pogrešaka (MSE)
4. Za svaku NaN poziciju: predikcija = prolaz kroz stablo
5. fill_remaining_gaps() ako nešto ostane NaN
```

**Ograničenja stabla:**
- maks. dubina: **5**
- min. uzoraka u listu: **3**

---

## 5. Što funkcija prima i vraća

```c
int decision_tree_imputation(
    const Series *series,   /* hour, yday, epoch po indeksu */
    const double *temp,     /* damaged niz s NaN — ne mijenja se */
    double *out             /* popunjeni rezultat */
);
```

| Povrat | Značenje |
|--------|----------|
| `0` | Uspjeh |
| `!= 0` | Greška (nema poznatih vrijednosti ili malloc) |

---

## 6. Prednosti metode

- Jednostavna za objasniti na obrani („ako je uvjet, idi lijevo/desno”)
- Može učiti **nelinearna** pravila (npr. različit prosjek po dijelu dana)
- Koristi sat i dan u godini kao značajke, ne samo susjede u nizu
- Jedno stablo — malo koda, bez vanjskih biblioteka

---

## 7. Mane metode

- Jedno stablo lako **overfita** na malo podataka
- Osjetljivo na dubinu stabla i broj uzoraka u listu
- Nestabilno ako je premalo poznatih vrijednosti
- Zato **Random Forest** (već u projektu) ima smisla kao poboljšanje — prosjek više stabala

---

## 8. Testovi (`test_decision_tree`)

U `tests/run_tests.c`, mali niz od 8 satnih zapisa:

| Provjera | Što testira |
|----------|-------------|
| `decision_tree_imputation uspjeh` | povrat 0 |
| `nema NaN nakon imputacije` | sve rupe popunjene |
| `poznate vrijednosti nepromijenjene` | indeksi bez NaN ostaju isti |
| `NaN na poziciji 2/4 popunjen` | eksplicitno popunjavanje rupa |
| `original i dalje ima NaN` | ulazni `temp` nije mutiran |

---

## Što je napravljeno

- [x] Novi modul `src/decision_tree.h` / `src/decision_tree.c`
- [x] Regresijsko stablo s MSE podjelom, dubina ≤ 5, min. 3 u listu
- [x] Cikličke značajke (kao knn_upgraded)
- [x] `test_decision_tree()` u `tests/run_tests.c`
- [x] Red `decision_tree` u `main.c --compare`
- [x] `build.bat` ažuriran za testove

---

## Datoteke

| Datoteka | Promjena |
|----------|----------|
| `src/decision_tree.h` | API |
| `src/decision_tree.c` | implementacija stabla |
| `src/main.c` | compare tablica |
| `tests/run_tests.c` | testovi |
| `build.bat` | link decision_tree u tests.exe |

---

## Decision Tree vs KNN

| | KNN | Decision Tree |
|--|-----|---------------|
| Učenje | nema eksplicitnog modela | gradi stablo pravila |
| Predikcija | prosjek k susjeda | prolaz kroz stablo do lista |
| Značajke | udaljenost u prostoru značajki | uvjeti feature ≤ threshold |
| Složenost | O(n) po NaN | O(dubina) po NaN nakon treniranja |

---

## Rezultati `--compare` (seed 42, 40% mask)

### Demo Split (12 zapisa)

| Metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| linear_interpolation | 0.0900 | 0.1037 | 0.9186 |
| knn_upgraded | 0.2522 | 0.2797 | 0.4072 |
| **decision_tree** | **0.3100** | **0.3931** | **-0.17** |
| rf_imputation | 0.4106 | 0.5052 | -0.93 |

### Jena 48h (288 zapisa)

| Metoda | MAE | RMSE | R² |
|--------|-----|------|-----|
| linear_interpolation | 0.0620 | 0.0920 | 0.9980 |
| knn_imputation | 0.1102 | 0.1591 | 0.9941 |
| **decision_tree** | **0.1693** | **0.2320** | **0.9874** |
| rf_imputation | 0.2136 | 0.2921 | 0.9801 |

Na malom nizu jedno stablo može overfitati; RF (više stabala) je lošiji ovdje jer koristi
sirove značajke — Dan 9 može uskladiti RF s cikličkim značajkama.

## Testirano

```powershell
.\build.bat
.\test.bat   # 51/51 SVE PROLAZI
.\run.bat --compare --source demo --city Split
.\run.bat --compare --source jena_quick
```

---

## Sljedeći korak (Dan 9 — plan)

- Poboljšati / dokumentirati Random Forest kao proširenje Decision Tree-a
- Export rezultata `--compare` u CSV
- CLI parametri za dubinu stabla (opcionalno)

---

## Dnevni izvještaj — Dan 8

**Napravljeno:** Decision Tree imputacija temperature — nova ML metoda u C projektu.

**Datoteke:** `decision_tree.h/c` (novo), `main.c`, `run_tests.c`, `build.bat`, `dan8.md`.

**Kako radi:** Trenira jedno regresijsko stablo na poznatim temperaturama i značajkama
vremena; za svaku NaN poziciju predviđa temperaturu prolaskom kroz stablo do lista
(prosjek temperature u tom listu).

**Razlika od KNN-a:** KNN ne gradi model — traži slične primjere. Decision Tree uči
pravila podjele prostora značajki.

**Testovi:** Svi prolaze (uključujući `test_decision_tree`).

**Sljedeće:** Random Forest kao ensemble više stabala — logičan nastavak Dana 8.
