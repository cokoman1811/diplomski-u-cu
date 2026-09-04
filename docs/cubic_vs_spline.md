# Cubic vs spline — jednostavno objašnjenje

U radu postoje dvije metode:

- `cubic_interpolation` → u tekstu **cubic**
- `spline_interpolation` → u tekstu **spline**

Imena zvuče kao da su to dvije različite interpolacije. **Nisu.**

Obje su **kubični spline**.
Isti komadi, iste točke, ista rupa u sredini niza.
Razlikuju se samo u jednom pravilu na **prvoj i zadnjoj poznatoj točki cijelog niza**.

---

## 1. Što obje rade (30 sekundi)
image.png
Imaš temperaturni niz. Neke vrijednosti nedostaju (NaN).

1. Uzmeš sve **poznate** temperature.
2. Između svakog para uzastopnih poznatih točaka nacrtaš **kubni komad** (krivulja 3. stupnja).
3. Komadi se spajaju **glatko** (ne lome se kao pravci).
4. Rupu popuniš očitavanjem te krivulje.

Za **jednu rupu** trebam:

- lijevu poznatu točku (rub)
- desnu poznatu točku (rub)
- nagib s lijeve vanjske strane
- nagib s desne vanjske strane

Sredina rupe se **izračuna**. Ne unosiš točke iz sredine.

To vrijedi i za cubic i za spline.

---

## 2. Cijela razlika u jednoj rečenici

**Cubic** na kraju niza kaže: *„drži ovaj kut (nagib).”*

**Spline** na kraju niza kaže: *„ne savijaj se.”*

To je sve.

Unutar niza, daleko od krajeva, to pravilo se skoro ne osjeti. Zato u tablicama često imaju **isti MAE**.

---

## 3. Analogija: letvica i čavli

Zamisli savitljivu letvicu. Poznate temperature su čavli kroz koje letvica mora proći.

```
        čavao     čavao     čavao     čavao
          •---------•---------•---------•
        prvi                           zadnji
```

U sredini obje metode rade isto: letvica prolazi kroz čavle i spojevi su glatki.

Razlika je samo kako **držiš krajeve**.

### Cubic = zaključani spline

Kraj letvice stisneš u škripač **pod određenim kutom**.

Kut uzmeš iz prvih (odnosno zadnjih) poznatih mjerenja:
ako temperatura baš ulazi u taj čavao prema gore, cubic **mora** na rubu ići prema gore pod tim nagibom.

### Spline = prirodni spline

Krajeve **ne stisneš pod kutom**.
Samo ih pustiš da se **ne savijaju**.

Matematički: druga derivacija na rubu je nula:

```
S''(prva točka)  = 0
S''(zadnja točka) = 0
```

Ako nema savijanja, letvica na kraju izlazi **kao pravac**.

Zato se zove **prirodni** spline: kao da elastičnu letvicu na krajevima ne savijaš rukom.

---

## 4. Nagib i savijanje (dva broja, ne miješaj ih)

Na jednoj točki krivulja ima dva svojstva:

| što | značenje | pitanje |
|---|---|---|
| **nagib** \(S'\) | gore ili dolje, koliko strmo | *Kojim kutom letvica prolazi kroz čavao?* |
| **savijanje** \(S''\) | mijenja li se taj kut | *Savija li se letvica baš na tom čavlu?* |

Cubic na rubu zadaje **nagib**.
Spline na rubu zadaje **savijanje = 0**.

Nisu isto.

Primjer:

- Auto ide uzbrdo → to je nagib.
- Auto još ubrzava uspon, volan se okreće → to je savijanje.

Cubic kaže: *„na izlazu iz tunela volan mora biti u ovom položaju.”*
Spline kaže: *„na izlazu iz tunela prestani okretati volan.”*

---

## 5. Sličica koju trebaš vidjeti

Zamislite prvu poznatu temperaturu u 12:40 = 12 °C.
Lijevo od nje nema mjerenja (rupa na početku).
Desno ima normalan niz.

```
  RUPA (nema mjerenja)          POZNATO (iste krivulje)
 <---------------------- 12:40 ---------------------->
                         RUB

 cubic:   strmo ulazi u 12:40, jer je kut zaključan
 spline:  pliće ulazi u 12:40, jer se na rubu ne savija

 desno od 12:40:  cubic = spline
```

Ako je rupa **u podne**, a ne u 12:40 na početku dana, obje metode vide iste unutarnje čavle i daju isti rezultat.

---

## 6. Kad se to vidi u tvom eksperimentu

| scenarij | gdje je rupa | cubic vs spline |
|---|---|---|
| random | po cijelom nizu, uglavnom unutra | skoro isto |
| block, block_middle | u sredini | skoro isto |
| **block_start** | na početku niza | **tu se razlikuju** |
| **block_end** | na kraju niza | **tu se razlikuju** |

Rubno pravilo je kao uputa samo za prvi i zadnji čavao.
Čim si dva-tri komada unutra, obje metode rade iste spojeve.

Zato nije čudno da u većini tablica piše isti broj. To nije greška. To je očekivano.

---

## 7. Što cubic i spline NISU

Ovo su česte zabune. Ništa od ovoga nije razlika:

- spline **nije** „više točaka”, a cubic „manje točaka”
- spline **nije** linearna interpolacija
- cubic **nije** jedan polinom kroz točno 4 temperature
- ne unosiš 4 točke u sredini rupe da bi dobio nagib
- razlika **nije** u formuli kojom se računa rupa u sredini dana

U kodu je to doslovno ista funkcija, drugi prekidač:

```c
cubic_interpolation  →  cubic_spline_impl(..., SPLINE_CLAMPED)
spline_interpolation →  cubic_spline_impl(..., SPLINE_NATURAL)
```

`CLAMPED` = zaključaj nagib na rubu.
`NATURAL` = na rubu savijanje = 0.

---

## 8. Mini primjer brojkama

Poznato od 12:40 nadalje:

```
12:40 = 12.0 °C     ← prva poznata (RUB)
12:50 = 13.5 °C
13:00 = 15.5 °C
...
```

Rupa prije 12:40.

Na samom rubu (12:40) obje **moraju** proći kroz 12.0. To nije sporeno.

Što jest sporeno:

- cubic: „u 12:40 nagib mora biti onaj koji vidim iz 12:40, 12:50, 13:00”
- spline: „u 12:40 ne savijaj se (y2 = 0)”

Zato lijevo od 12:40 krivulje nisu iste.
Desno, kroz poznate točke, jesu (ili skoro jesu).

Između dvije poznate unutarnje točke, npr. 13:00 i 13:10, obje daju otprilike **15,96 °C**. Razlika je na trećoj decimali. Za diplomski: **isto**.

---

## 9. Rečenice za obranu

Kratka:

> Cubic i spline u radu su isti kubični spline. Cubic na krajevima niza zadaje nagib (zaključani spline), a spline na krajevima zadaje da je zakrivljenost nula (prirodni spline). Unutar niza daju iste vrijednosti.

Ako pitaju „zašto onda obje metode”:

> Da se vidi utjecaj rubnog uvjeta. Na random i block_middle razlika je zanemariva. Na block_start i block_end, gdje rupa sjedi na rubu niza, razlika se vidi.

Ako pitaju „što je prirodni spline”:

> Druga derivacija na prvom i zadnjem poznatom mjerenju je nula, pa se krivulja na rubu ponaša kao pravac. Analogija je letvica kojoj krajeve ne savijaš.

---

## 10. Pamti ovu shemu

```
                 CUBIC                         SPLINE
            (zaključani spline)           (prirodni spline)

  unutra     isti kubni komadi             isti kubni komadi
  spojevi    glatki                        glatki
  rupa u     ista krivulja                 ista krivulja
  sredini

  na RUBU    zadaješ NAGIB                 zadaješ: ne savijaj
             (kut letvice)                 (y'' = 0)
```

Ako zapneš, pitaj se samo ovo:

**Držim li na zadnjem čavlu kut, ili samo zabranjujem savijanje?**

- kut → cubic
- ne savijaj → spline
