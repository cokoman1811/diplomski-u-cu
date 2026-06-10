# Česta pitanja — C verzija

Kratka objašnjenja pojmova i dijelova koda u diplomskom projektu (C).
Ovdje se zapisuju pitanja koja se ponavljaju tijekom rada na kodu.

---

## Sadržaj

1. [Što je `Metrics`?](#1-što-je-metrics)
2. [Što je `ok` u `print_metric_row`?](#2-što-je-ok-u-print_metric_row)
3. [Kako se pokreće projekt?](#3-kako-se-pokreće-projekt)
4. [Gdje su testovi?](#4-gdje-su-testovi)
5. [Zašto funkcije idu u `.h` i `.c`?](#5-zašto-funkcije-idu-u-h-i-c)
6. [Što što radi — što pročitati](#6-što-što-radi--što-pročitati)
7. [Automatski Git sync](#7-automatski-git-sync)
8. [Česte greške](#8-česte-greške)
9. [Što je `Series`?](#9-što-je-series)

---

## 1. Što je `Metrics`?

**Datoteka:** `src/evaluation.h`

```c
typedef struct {
    double mae;
    double rmse;
    double r2;
    size_t count; /* broj tocaka koristenih u evaluaciji */
} Metrics;
```

### Nije CSV i nije datoteka

`Metrics` je **struktura u memoriji** — mali objekt koji drži rezultat evaluacije jedne metode.
Ne sprema se automatski u datoteku; `main.c` ga samo ispiše u terminal.

### Što znače polja?

| Polje | Značenje |
|-------|----------|
| `mae` | Mean Absolute Error — prosječna apsolutna pogreška (niže = bolje) |
| `rmse` | Root Mean Square Error — korijen prosječne kvadratne pogreške (niže = bolje) |
| `r2` | Koeficijent determinacije — koliko dobro rekonstrukcija prati original (bliže 1 = bolje) |
| `count` | Na koliko je točaka računata metrika |

### Odakle dolazi?

Funkcija `evaluate_reconstruction()` u `src/evaluation.c` usporedi:
- **original** — pravi temperaturni niz
- **reconstructed** — niz nakon imputacije/interpolacije

Metrike se računaju **samo na mjestima gdje je vrijednost umjetno obrisana** (`mask[i] == 1`),
ne na cijelom nizu.

### Primjer u terminalu

```
  metoda                        MAE       RMSE         R2
  ------------------------------------------------------------
  forward_fill                 1.2345     1.5678     0.8901
```

Svaki redak = jedan `Metrics` objekt za jednu metodu.

---

## 2. Što je `ok` u `print_metric_row`?

**Datoteka:** `src/main.c`

```c
static void print_metric_row(const char *name, Metrics m, int ok);
```

`ok` je **flag uspjeha metode** (0 ili 1), ne provjera svake pojedinačne točke.

| `ok` | Značenje | Ispis |
|------|----------|-------|
| `1` | Metoda je uspjela | MAE, RMSE, R² iz `Metrics` |
| `0` | Metoda nije mogla raditi | `[preskoceno: premalo poznatih tocaka]` |

### Kada je `ok = 0`?

Npr. `cubic_interpolation` i `spline_interpolation` trebaju **barem 4 poznate točke**.
Ako ih nema dovoljno, metoda vrati grešku i `main.c` pozove:

```c
print_metric_row("cubic_interpolation", (Metrics){0}, 0);
```

Isto vrijedi za `knn_imputation` ako nema nijedne poznate vrijednosti.

Za `forward_fill`, `linear_interpolation` i `time_interpolation` uvijek se šalje `ok = 1`
jer te metode gotovo uvijek mogu raditi.

---

## 3. Kako se pokreće projekt?

C se mora **kompajlirati** prije pokretanja (za razliku od Pythona).

```powershell
cd "diplomski u cu"
.\build.bat                              # napravi diplomski.exe i tests.exe
.\diplomski.exe --compare                # pokreni eksperiment
.\run.bat --compare --source demo --city Split   # isto, s automatskim buildom
```

### Zašto `--compare`?

Trenutno je to **jedina naredba** u C verziji. Pokreće cijeli eksperiment:
učitaj podatke → umjetno obriši dio vrijednosti → usporedi metode → ispiši tablicu.

### Korisni argumenti

| Argument | Zadano | Opis |
|----------|--------|------|
| `--source` | `jena_quick` | `demo` \| `jena_quick` \| `processed` |
| `--city` | `Split` | Grad (samo za `demo`) |
| `--missing-rate` | `0.4` | Udio umjetno obrisanih vrijednosti |

---

## 4. Gdje su testovi?

```
tests/run_tests.c    ← svi testovi (jedna datoteka, mini-harness)
test.bat             ← pokretanje testova
tests.exe            ← generira se buildom (nije u gitu)
```

```powershell
.\build.bat
.\test.bat
```

Testovi provjeravaju: KNN, preprocessing, interpolacije, metrike, učitavanje demo CSV-a.

---

## 5. Zašto funkcije idu u `.h` i `.c`?

U ovom projektu svaki modul ima par datoteka:

```
src/
├── evaluation.h    ← deklaracija (što postoji, kako se zove)
├── evaluation.c    ← implementacija (što funkcija stvarno radi)
├── interpolation.h
├── interpolation.c
└── ...
```

### Deklaracija vs implementacija

| | `.h` (header) | `.c` (source) |
|---|---------------|---------------|
| Uloga | **objava** funkcije | **tijelo** funkcije |
| Sadrži | potpis + komentar | kod unutra `{ ... }` |
| Analogija | sadržaj jelovnika u restoranu | kuhar koji kuha jelo |

**Deklaracija** (u `.h`) = „ova funkcija postoji, evo kako je zoveš i što prima“:

```c
/* evaluation.h */
Metrics evaluate_reconstruction(const double *original, const double *reconstructed,
                                const int *mask, size_t n);
```

**Implementacija** (u `.c`) = stvarni kod:

```c
/* evaluation.c */
#include "evaluation.h"

Metrics evaluate_reconstruction(const double *original, const double *reconstructed,
                                const int *mask, size_t n) {
    Metrics m = {NAN, NAN, NAN, 0};
    /* ... ostatak logike ... */
    return m;
}
```

`.c` datoteka **mora** uključiti svoj `.h` na vrhu (`#include "evaluation.h"`).

### Zašto to treba?

`main.c` želi pozvati `evaluate_reconstruction`, ali ne zna gdje je napisana.
Dovoljno mu je pročitati **deklaraciju** iz `evaluation.h`:

```c
/* main.c */
#include "evaluation.h"

/* ... negdje u kodu: */
Metrics m = evaluate_reconstruction(s.temp, out, mask, n);
```

Kompajler pri buildu spoji sve `.c` datoteke u jedan program — `main.c` zna *što* pozvati
(iz `.h`), a `evaluation.c` zna *kako* to napraviti (iz `.c`).

### Pravilo za novu funkciju

Kad dodaješ novu funkciju koju koriste i druge datoteke:

1. **Deklariraj** u `.h` (potpis + kratki komentar)
2. **Napiši** tijelo u `.c`
3. U datotekama koje je pozivaju dodaj `#include "ime.h"`

### Kada **ne** ide u `.h`?

Funkcije koje koristiš **samo u jednoj** `.c` datoteci mogu ostati privatne — stavi `static`:

```c
/* main.c — samo za ispis tablice, nitko drugi je ne zove */
static void print_metric_row(const char *name, Metrics m, int ok) {
    /* ... */
}
```

`static` = funkcija je vidljiva samo u toj datoteci → **ne treba** deklaracija u `.h`.

Isto vrijedi za pomoćne funkcije unutar modula, npr. u `interpolation.c`:

```c
static void fill_remaining_gaps(double *out, size_t n) {
    /* koristi je samo interpolation.c */
}
```

### Što još ide u `.h`?

Osim deklaracija funkcija, header često sadrži:

- **strukture** koje dijele više datoteka (`Metrics`, `Series`)
- **`#ifndef` / `#define` / `#endif`** — štiti od dvostrukog uključivanja

```c
#ifndef EVALUATION_H
#define EVALUATION_H
/* ... sadržaj ... */
#endif
```

### Pregled modula u projektu

| Header (`.h`) | Source (`.c`) | Što nudi drugima |
|---------------|---------------|------------------|
| `series.h` | `dataset.c` | `Series`, učitavanje CSV-a |
| `preprocessing.h` | `preprocessing.c` | `create_missing_values` |
| `interpolation.h` | `interpolation.c` | forward, linear, time, cubic, spline |
| `ml_methods.h` | `ml_methods.c` | `knn_imputation` |
| `evaluation.h` | `evaluation.c` | `Metrics`, `evaluate_reconstruction` |
| — | `main.c` | samo `main`, ostalo je `static` |

### Ukratko

- **`.h`** = „ugovor“ — što modul nudi ostatku programa
- **`.c`** = „rad“ — kako se to izvodi
- Funkciju koju zove više datoteka: **deklaracija u `.h`, kod u `.c`**
- Funkciju koju zove samo jedna `.c`: **`static` u toj `.c`, bez `.h`**

---

## 6. Što što radi — što pročitati

Kratka mapa projekta: koja datoteka za što služi i redoslijed čitanja.

| Datoteka / modul | Što radi |
|------------------|----------|
| `main.c` | Što program radi od početka do kraja |
| `series.h` | Kako su podaci spremljeni u C-u |
| `dataset.c` | Kako se CSV učita |
| `preprocessing` | Kako se umjetno brišu vrijednosti |
| `evaluation` | Kako se računaju MAE / RMSE / R² |
| `interpolation` / `ml_methods` | Kako se rupe popunjavaju |
| `tests` | Što sve mora raditi |

### Preporučeni redoslijed

```
main.c  →  series.h  →  dataset.c  →  preprocessing  →  evaluation
    →  interpolation / ml_methods  →  tests
```

### Tok u jednoj rečenici

```
CSV → Series → ošteti niz → popuni rupe → usporedi s originalom → ispiši metrike
```

Sve to je u funkciji `run_compare()` u `main.c`.

### Minimalno (ako imaš malo vremena)

1. `main.c`
2. `preprocessing.c`
3. `interpolation.c`

To pokriva većinu logike.

---

## 7. Automatski Git sync

Promjene se **same ne šalju** na GitHub dok ne pokreneš sync ili dok agent ne završi rad.

### Ručno (bilo kad)

```powershell
.\git-sync.bat
# ili s porukom:
.\git-sync.bat -CommitMessage "Dodani testovi i FAQ"
```

Skripta `scripts/git-sync.ps1` radi: `git add` → `commit` → `push` na
`https://github.com/cokoman1811/diplomski-u-cu.git`

### Automatski (nakon rada agenta u Cursoru)

U projektu je Cursor hook (`.cursor/hooks.json`):
kad **agent završi** zadatak (`stop` event), pokrene se tihi sync na GitHub.

Ako sync padne (nema interneta, git auth), agent se ne blokira — promjene ostaju lokalno.

### U chatu

Možeš reći agentu: **„uploadaj na git“** ili **„pokreni git-sync“**.

### Napomena

- `.exe`, `build/` i sl. **ne idu** na git (vidi `.gitignore`)
- Za prvi push trebaš biti prijavljen na GitHub (`gh auth login` ili git credential)

---

## 8. Česte greške

### `gcc nije pronaden`

**Uzrok:** MinGW nije u PATH-u.

**Rješenje:**

```powershell
winget install -e --id BrechtSanders.WinLibs.POSIX.UCRT
```

Zatvori i ponovo otvori terminal. `build.bat` automatski traži gcc i u WinGet mapi ako nije u PATH-u.

---

### `Greska: ne mogu otvoriti datoteku: data/...`

**Uzrok:** Program pokrenut iz krive mape (relativne putanje `data/...`).

**Rješenje:** Pokreni iz korijena projekta:

```powershell
cd "diplomski u cu"
.\run.bat --compare
```

Ili koristi `run.bat` / `build.bat` — oni sami rade `cd` u pravu mapu.

---

### `[preskoceno: premalo poznatih tocaka]`

**Uzrok:** `cubic_interpolation`, `spline_interpolation` ili `knn_imputation` nisu mogli raditi — premalo poznatih vrijednosti u nizu.

**Rješenje:** Normalno na vrlo malim nizovima. Na demo/Jena 48h obično ne bi trebalo. Smanji `--missing-rate` ili koristi veći dataset.

---

### Testovi padaju nakon izmjene koda

**Rješenje:**

```powershell
.\build.bat
.\test.bat
```

Provjeri koji `[FAIL]` red ispisuje `tests.exe` i usporedi s `tests/run_tests.c`.

---

### Git sync ne radi / `push` odbijen

**Uzrok:** Nisi prijavljen na GitHub ili nema interneta.

**Rješenje:**

```powershell
gh auth login
.\git-sync.bat
```

Promjene ostaju lokalno u commitu čak i ako push padne.

---

### Cursor taskovi (Build / Test) ne rade

**Rješenje:** `Terminal` → `Run Task...` → odaberi **Build** ili **Test**.
Taskovi su u `.vscode/tasks.json`. Zahtijevaju PowerShell/CMD u korijenu projekta.

---

## 9. Što je `Series`?

**Datoteka:** `src/series.h` (definicija), `src/dataset.c` (funkcije)

```c
typedef struct {
    size_t n;
    double *temp;
    long long *epoch;
    int *hour;
    int *yday;
} Series;
```

### Što je to?

`Series` je glavna struktura projekta — **temperaturni vremenski niz** u C-u.
Odgara Python `pd.Series` s vremenskim indeksom, ali ovdje su podaci u paralelnim poljima.

Svi elementi na istom indeksu `i` (od `0` do `n-1`) opisuju **jedno mjerenje**.

### Što znače polja?

| Polje | Tip | Značenje |
|-------|-----|----------|
| `n` | `size_t` | Broj mjerenja u nizu |
| `temp[i]` | `double` | Temperatura; `NAN` = nedostaje |
| `epoch[i]` | `long long` | Vrijeme u sekundama od 1970-01-01 (UTC) |
| `hour[i]` | `int` | Sat u danu (0–23); značajka za KNN |
| `yday[i]` | `int` | Dan u godini (1–366); značajka za KNN |

### Primjer u glavi

Za 3 mjerenja:

```
i=0: temp=9.2,  epoch=..., hour=0,  yday=1
i=1: temp=9.0,  epoch=..., hour=1,  yday=1
i=2: temp=NAN,  epoch=..., hour=2,  yday=1   ← nedostaje
```

### Funkcije uz `Series`

| Funkcija | Datoteka | Što radi |
|----------|----------|----------|
| `series_alloc` | `dataset.c` | Alocira memoriju za `n` elemenata |
| `series_free` | `dataset.c` | Oslobađa memoriju |
| `series_load_csv` | `dataset.c` | Učitava niz iz CSV-a u `Series` |

### Gdje se koristi?

- `main.c` — `Series s;` pa `series_load_csv(&s, ...)`
- `ml_methods.c` — KNN koristi `hour`, `yday` i poziciju kao značajke
- `interpolation.c` — uglavnom `temp`; `time_interpolation` koristi i `epoch`

### Ukratko

`Series` = tablica temperatura + vrijeme + pomoćne značajke za ML, sve usklađeno po indeksu `i`.

---

## Kako dodati novo pitanje

Kopiraj predložak:

```markdown
## N. Naslov pitanja?

**Datoteka:** `src/ime.c` ili `src/ime.h`

Kratko objašnjenje...

### Dodatno (tablica, primjer koda, itd.)
```

Dodaj ga na kraj datoteke i ažuriraj sadržaj na vrhu.
