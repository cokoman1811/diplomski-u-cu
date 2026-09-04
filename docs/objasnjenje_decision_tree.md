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

## Korak 5 — čemu stablo

Imamo popis grešaka na poznatim mjestima.  
Rupa nema grešku, jer nema stvarnu temperaturu.

Želimo pravilo:

> ako rupa izgleda kao neka poznata mjesta,  
> uzmi njihovu grešku i dodaj je na crtu rupe.

To pravilo spremamo kao **stablo pitanja** (da / ne).

Bez stabla bi za svaku rupu iznova pretraživali sve poznate točke.  
Stablo je gotov upitnik: rupa samo odgovara i dobije broj.

---

## Korak 6 — što je stablo

Binarno stablo. Svaki unutarnji čvor je pitanje.

```
                 [pitanje]
                 /        \
              DA /          \ NE
               /              \
           [pitanje]         [LIST]
            /      \
        [LIST]    [LIST]
```

**List nije temperatura.**  
List je **greška crte**, npr. `+1.2`.

Kad dođeš do lista, račun je:

```
temperatura rupe = ravna crta te rupe + broj na listu
```

---

## Korak 7 — kako se stablo pravi (trening)

Samo poznate točke. Rupe još čekaju.

1. Sve poznate točke stavi u jednu hrpu. To je korijen.
2. Nađi da/ne pitanje koje tu hrpu dobro raspolovi  
   (npr. „jesi li u sredini rupe?”).
3. DA ide lijevo, NE ide desno.
4. Ponovi na svakoj novoj hrpi.
5. Kad je hrpa mala ili imaš dovoljno pitanja, stani.  
   Ta hrpa postane **list**.  
   Na list napiši **prosjek grešaka** u toj hrpi.

Sada stablo postoji u memoriji.  
Nije spremljeno u datoteku.  
Poznate temperature se nisu promijenile.

---

## Korak 8 — kako rupa dobije broj (predikcija)

Tek sada dolaze rupe. Svaka rupa **posebno**.

1. Za tu rupu izračunaj ravnu crtu (korak 2).
2. Kreni od vrha stabla.
3. Odgovaraj na pitanja (da = lijevo, ne = desno).
4. Kad dođeš do lista, uzmi taj broj.
5. Zbroji: crta + list.

Druga rupa krene **opet od vrha** istog stabla.  
Može pasti u drugi list, jer ima drugačiju situaciju.

---

## Korak 9 — mali brojevi, 5 mjesta

Niz:

```
mjesto:  1     2     3     4     5
T:       10    ?     ?     16    18
```

Poznata: 10, 16, 18.  
Rupe: mjesto 2 i 3.

**Gradnja** (samo 10, 16, 18) napravi npr. ovako malo stablo:

```
        [jesi li bliže desnom rubu?]
         /                         \
   DA /                               \ NE
     /                                 \
LIST: +0.5                         LIST: 0.0
```

**Rupa 2**

- crta između 10 i 16, bliže lijevom → crta ≈ 12
- pitanje: bliže desnom? **NE** → list `0.0`
- rezultat: 12 + 0 = **12**

**Rupa 3**

- crta između 10 i 16, bliže desnom → crta ≈ 14
- pitanje: bliže desnom? **DA** → list `+0.5`
- rezultat: 14 + 0.5 = **14.5**

Isto stablo. Dvije rupe. Dva broja.

---

## Korak 10 — što zapamtiti

| | Gradnja | Predikcija |
|--|---------|------------|
| tko | poznate točke | samo rupe |
| što | pravi se stablo | prolazi se gotovo stablo |
| izlaz | pitanja + listovi (greške) | temperatura = crta + list |

Jedna rečenica:

> Od poznatih točaka naučim koliko ravna crta griješi. To spremim kao pitanja. Svaka rupa prođe ta pitanja i dodam tu grešku na njezinu crtu.
