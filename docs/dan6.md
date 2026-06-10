# Dan 6 — KNN komentari + Random Forest (C)

**Datum:** 2026-06-10  
**Autor:** Toni Jakelić

Učvršćen ML dio C verzije: KNN dokumentiran, dodana minimalna RF imputacija.

## Što je napravljeno

- [x] Pregled i komentari u **`src/knn_methods.c`** / **`.h`**
- [x] KNN već u **`main.c --compare`** (bez refactora)
- [x] Test **`test_knn()`** — uspjeh, poznate iste, bez NaN u izlazu
- [x] Novi modul **`src/rf_methods.c`** / **`.h`** — `rf_imputation()`
  - 8 stabala, dubina do 4, bootstrap uzorak poznatih vrijednosti
  - značajke: pozicija, hour, yday
- [x] RF u **`main.c --compare`**
- [x] Test **`test_rf()`**

## TODO (RF — kasnije, nije blokirajuće)

- Više stabala / dubina (trenutno fiksno u `#define`)
- Slučajan odabir podskupa značajki po čvoru (pravi RF detalj)
- OOB (out-of-bag) procjena kvalitete
- Parametar `n_trees` kroz CLI

## Testirano

```powershell
.\build.bat
.\test.bat
.\run.bat --compare --source demo --city Split
```
