# Stablo — korak po korak

Čitaj **samo jedan korak**. Kad ga skužiš, idi na sljedeći. Ako nešto nije jasno, pitaj taj korak.

Kod je u `src/decision_tree.c`, ali sada nam ne treba.

---

## Korak 1 — što uopće radimo

Imamo niz temperatura. Neka mjesta fale. Zovemo ih **rupama**.

Primjer:

```
mjesto:      1     2     3     4     5
temperatura: 10    ?     ?     16    17
```

Znamo 10, 16 i 17.  
Ne znamo mjesta 2 i 3.

**Zadatak:** smisliti broj umjesto svakog `?`.

To je sve što metoda radi. Još nema stabla.

---

## Korak 2 — prva procjena, bez stabla

Za rupu pogledamo **zadnju poznatu prije** i **prvu poznatu poslije**.

Između njih povučemo **ravnu crtu**.

```
10 --------?--------?-------- 16
```

Ako je `?` točno na pola puta, crta kaže **13**.

To se zove linearna interpolacija.  
Stablo još ne postoji. Ovo je samo prva procjena.

---

## Korak 3 — crta zna griješiti

U stvarnosti temperatura nije uvijek ravna crta.  
Podne je često toplije nego što crta kaže.

Dakle:

```
crta kaže:     13
stvarnost:     možda 15
greška crte:   +2
```

Kad je rupa, **stvarnost ne znamo**. Zato grešku ne možemo izravno izračunati na rupi.

---

## Korak 4 — gdje grešku IPACK možemo izračunati

Na **poznatim** mjestima temperaturu znamo.

Tamo možemo napraviti isto: povući crtu između susjeda (bez te točke) i usporediti sa stvarnom temperaturom.

Primjer. Znamo da je na mjestu 4 bilo **16**.  
Susjedi su 10 i 17. Crta kaže 15.  
Greška = 16 − 15 = **+1**.

To radimo za **svako poznato** mjesto.  
Dobijemo popis: *u takvoj-i-takvoj situaciji crta je griješila za toliko*.

---

## Korak 5 — imamo tablicu, ne stablo

Nakon koraka 4 imaš samo ovo. Još uvijek **nema stabla**.

| poznato mjesto | situacija | greška crte |
|----------------|-----------|-------------|
| A | uz rub rupe | 0 |
| B | uz rub rupe | 0 |
| C | sredina rupe | +2 |
| D | sredina rupe | +2 |

Čita se: kad je crta rasla kroz **sredinu** rupe, bila je 2 preniska.  
Kad je točka bila **uz rub**, crta je pogodila.

Rupa još uvijek nema svoj red u tablici. Njoj fali temperatura, pa ne možemo izračunati njezinu grešku.

---

## Korak 6 — što želimo napraviti s rupom

Rupa ima situaciju (npr. „ja sam u sredini rupe”), ali nema grešku.

Gledamo tablicu i kažemo:

> sredina rupe u tablici ima grešku +2,  
> pa i ovoj rupi dodajem +2 na crtu.

Ako je crta rupe rekla 13:

```
13 + 2 = 15
```

To je cijela ideja. Stablo je samo način da se ovo gledanje u tablicu pretvori u da/ne pitanja.

---

## Korak 7 — zašto pitanja, a ne gledanje u tablicu

Tablicu možeš svaki put pregledati očima.  
Kod to radi pitanjem koje dijeli redove u dvije skupine:

> Jesi li u sredini rupe?

- **DA** → skupina C i D, greška +2
- **NE** → skupina A i B, greška 0

To pitanje + te dvije skupine **jesu** stablo. Ništa više.

```
          Jesi li u sredini rupe?
           /                    \
        DA /                      \ NE
          /                        \
    skupina +2                  skupina 0
    (to zovemo LIST)            (to zovemo LIST)
```

**List** = skupina redova iz tablice, s jednim brojem: njihovim prosjekom greške.

Nije ladica u koju spremaš rupe.  
Nije temperatura.  
To je samo natpis na skupini: „ovdje crta obično griješi za +2”.

---

## Korak 8 — rupa samo odgovori na pitanje

Rupa **ne ulazi u tablicu**.  
Ne uči ništa novo.

1. Povuci njezinu ravnu crtu (korak 2). Recimo 13.
2. Pitaj: jesi li u sredini rupe?
3. Ako DA, uzmi natpis **+2**.
4. Upiši 13 + 2 = **15**.

Druga rupa: crta 14, nije u sredini → uzme **0** → ostane **14**.

Isto pitanje. Isti listovi. Druga rupa, drugi zbroj.

---

## Korak 9 — kad ima više pitanja

Ako tablica ima puno redova, jedno pitanje nije dovoljno.  
Svaku skupinu opet raspoloviš novim pitanjem. To postane dublje stablo.

Za početak ti **nije potrebno**. Dovoljno je zapamtiti:

- tablica grešaka na poznatim mjestima
- pitanje dijeli tablicu u skupine
- skupina ima natpis (list)
- rupa odgovori na pitanje i uzme natpis
- temperatura = crta + natpis

---

## Korak 10 — što zapamtiti

Poznate točke → naprave tablicu grešaka → od tablice nastanu pitanja.  
Rupe → ne pune tablicu → samo odgovaraju na pitanja.

```
temperatura rupe = ravna crta + greška iz lista
```
