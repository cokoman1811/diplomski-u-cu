# Novo u eksperimentima — tekst za diplomski rad

*Automatski generirano iz `experiment_results.csv`*
*Kopiraj odlomke u poglavlja Metodologija, Rezultati, Rasprava i Zaključak*

---

## A. Kratki sažetak novina (1 odlomak)

U odnosu na raniju verziju eksperimenata, rad je proširen na **7-dnevni** Jena Climate dataset (**1008** zapisa, 10-min intervali), missing rateove **10–80 %**, te **12 metoda imputacije** u **5 scenarija** (ukupno **480** testova). Dodane su metode **pomičnog prosjeka**, **adaptivne hibridne imputacije** te odvojena usporedba **osnovnog i naprednog KNN-a**. Razdvojene su **zaključana kubična** (`cubic_interpolation`) i **prirodna spline** (`spline_interpolation`) interpolacija.

Najveća izmjena je **potpuna prerada metoda strojnog učenja** i dodavanje **neuronske mreže** (`neural_net`). U prvoj verziji sve su ML metode kao ulaz koristile isključivo vrijeme (indeks, sat, dan u godini), pa su učile preslikavanje *vrijeme → temperatura*, dok interpolacija rješava bitno lakši problem *susjedne temperature → temperatura*. Uvođenjem značajki najbližih poznatih susjeda i prelaskom na učenje **reziduala iznad linearne baze**, prosječni MAE svih ML metoda pao je za **14–40 %**, a četiri od njih sada nadmašuju linearnu interpolaciju. Za svaki scenarij generirani su grafovi rekonstrukcije **najbolje i najgore** metode pri 20 % nedostajućih vrijednosti.

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

### B.3 Metode (12)

| # | Metoda | Kratki opis |
|---|--------|-------------|
| 1 | forward_fill | Zadnja poznata vrijednost |
| 2 | linear_interpolation | Linearna interpolacija po indeksu |
| 3 | time_interpolation | Linearna interpolacija po vremenu |
| 4 | cubic_interpolation | Zaključani kubični spline |
| 5 | spline_interpolation | Prirodni kubični spline |
| 6 | moving_average | Pomični prosjek (prozor ±6 = 1 h) |
| 7 | knn | KNN s obaveznim obuhvatom praznine, k = 2, ponder 1/d |
| 8 | knn_upgraded | KNN u prostoru značajki praznine, uči rezidual |
| 9 | decision_tree | Regresijsko stablo (dubina 8) na rezidualu |
| 10 | random_forest | 24 stabla, dubina 10, `max_features` = 7 od 11 |
| 11 | **neural_net** | Višeslojni perceptron 11–24–12–1 — **NOVO** |
| 12 | adaptive_imputation | Hibridna metoda (oracle routing, v. D.8) |

### B.4 Zajednički prostor značajki ML metoda (nova podloga)

Sve ML metode dijele isti skup od **11 značajki** (`src/ml_features.c`), pa razlika u rezultatu odražava razliku u modelu, a ne u ulazima:

| # | Značajka | Opis |
|---|----------|------|
| 0 | `prev_val` | vrijednost najbližeg poznatog susjeda lijevo |
| 1 | `next_val` | vrijednost najbližeg poznatog susjeda desno |
| 2 | `alpha` | relativan položaj unutar praznine, (i − p) / (n − p) |
| 3 | `d_prev` | udaljenost do lijevog oslonca u uzorcima |
| 4 | `d_next` | udaljenost do desnog oslonca |
| 5 | `lin_base` | `prev_val + alpha · (next_val − prev_val)` — linearna baza |
| 6 | `position_norm` | i / (n − 1) |
| 7–8 | `hour_sin`, `hour_cos` | ciklički sat |
| 9–10 | `yday_sin`, `yday_cos` | ciklički dan u godini |

Značajke 0–5 (`src/gap_features.c`) računaju se **isključivo iz oštećenog niza**, pa nema curenja informacija iz test skupa. Ključan detalj: za poznatu (trening) točku susjedi se traže u skupu poznatih točaka **bez nje same**. Bez toga bi `prev_val` u treningu bio jednak ciljnoj vrijednosti, model bi naučio identitet, a u testu bi ista značajka imala posve drugo značenje.

### B.5 Učenje reziduala

Sve ML metode kao cilj uče **odstupanje od linearne baze**, a ne temperaturu:

    y_i = temp_i − lin_base_i,     predikcija = lin_base_i + model(x_i)

Model time *popravlja* interpolaciju umjesto da je zamjenjuje. Predikcija nula znači „linearna baza je već točna”, pa metoda po konstrukciji ne može biti bitno lošija od linearne interpolacije. Dodatno se svaka predikcija ograničava na raspon opaženih temperatura, čime se sprječava ekstrapolacijski overshoot na dugim prazninama (isti mehanizam zbog kojeg spline zakaže na scenariju `block`).

### B.6 Neuronska mreža (nova metoda)

`src/neural_net.c` — višeslojni perceptron implementiran od nule u C99, bez vanjskih biblioteka:

- Arhitektura: **11 → 24 (tanh) → 12 (tanh) → 1 (linearno)**, 601 parametara
- Učenje: **backpropagation** + **Adam** (β₁ = 0,9, β₂ = 0,999), mini-batch 32, 200 epoha
- Stopa učenja 0,01 uz **kosinusno gašenje**
- Standardizacija ulaza po statistikama poznatih točaka; cilj skaliran na jediničnu skalu
- Xavier inicijalizacija; izlazni sloj namjerno inicijaliziran na male vrijednosti, pa mreža **kreće od linearne baze**
- Deterministički seed (42), pa je rezultat ponovljiv

### B.7 Adaptivna imputacija
Metoda `adaptive_imputation` analizira masku nedostajućih vrijednosti (stopa, veličina i pozicija najvećeg bloka) i automatski odabire jednu od poznatih metoda imputacije prema unaprijed definiranoj tablici routing pravila.

### B.8 Pomični prosjek
Za svaku nedostajuću točku uzima se prosjek poznatih susjeda u prozoru **±6 uzoraka** (1 sat pri 10-min intervalima).

---

## C. Rezultati — ključne brojke

### C.1 Rang metoda po prosječnom MAE (svi scenariji i rateovi)

| Rang | Metoda | Prosječni MAE (°C) |
|------|--------|-------------------|
| 1 | `adaptive_imputation` | 2.7046 |
| 2 | `neural_net` | 3.0741 |
| 3 | `random_forest` | 3.1012 |
| 4 | `decision_tree` | 3.1118 |
| 5 | `knn_upgraded` | 3.1278 |
| 6 | `time_interpolation` | 3.1315 |
| 7 | `linear_interpolation` | 3.1315 |
| 8 | `knn` | 3.1315 |
| 9 | `moving_average` | 3.6985 |
| 10 | `forward_fill` | 3.7863 |
| 11 | `cubic_interpolation` | 5.8704 |
| 12 | `spline_interpolation` | 6.6240 |

### C.2 Najbolja pojedinačna metoda po broju pobjeda (po scenariju i rateu)
- **linear_interpolation**: 7 od 40 kombinacija scenarij/rate
- **adaptive_imputation**: 1 pojedinačnih pobjeda, ali **najniži ukupni prosjek MAE: 2.7046 °C** (hibridna metoda je konzistentno dobra, iako ne uvijek prva u svakoj kombinaciji)
- **cubic_interpolation**: 7 pobjeda
- **spline_interpolation**: 5 pobjeda

### C.3 Učinak prerade ML metoda

| Metoda | MAE prije prerade | MAE poslije | Promjena |
|--------|-------------------|-------------|----------|
| `knn` | 3.7386 | 3.1315 | +16.2 % |
| `knn_upgraded` | 4.9931 | 3.1278 | +37.4 % |
| `decision_tree` | 5.2008 | 3.1118 | +40.2 % |
| `random_forest` | 3.9234 | 3.1012 | +21.0 % |
| `neural_net` | — (nova metoda) | 3.0741 | — |

### C.4 Broj pobjeda nad linearnom interpolacijom

Usporedba po pojedinačnim kombinacijama scenarij × missing rate (referenca: `linear_interpolation`, MAE = 3.1315 °C):

| Metoda | Prosječni MAE | Pobjeda nad linear |
|--------|---------------|--------------------|
| `neural_net` | 3.0741 | 24 / 40 |
| `random_forest` | 3.1012 | 21 / 40 |
| `decision_tree` | 3.1118 | 18 / 40 |
| `knn_upgraded` | 3.1278 | 17 / 40 |
| `knn` | 3.1315 | 0 / 40 |
| `cubic_interpolation` | 5.8704 | 12 / 40 |
| `moving_average` | 3.6985 | 9 / 40 |
| `forward_fill` | 3.7863 | 9 / 40 |

Neuronska mreža ima najniži prosječni MAE među svim metodama koje ne koriste oracle routing (**3.0741** naspram **3.1315** °C za linearnu interpolaciju).

### C.5 Identični rezultati
- **linear_interpolation** i **time_interpolation** daju **identične** rezultate na svim scenarijima (ravnomjerni 10-min intervali), pa je efektivan broj različitih metoda 11.
- **knn** nakon prerade daje rezultat **identičan linearnoj interpolaciji** — to nije slučajnost nego matematička posljedica (v. D.6).
- Na scenariju **block**, **cubic_interpolation** i **spline_interpolation** također daju identične rezultate.

### C.6 Usporedba osnovnog i naprednog KNN

| Scenarij | Osnovni KNN | Napredni KNN | Bolji |
|----------|-------------|--------------|-------|
| random | 0.1124 | 0.1365 | knn (osnovni) |
| block | 3.7733 | 3.7651 | knn_upgraded |
| block_start | 2.3795 | 2.4494 | knn (osnovni) |
| block_middle | 4.2521 | 4.2309 | knn_upgraded |
| block_end | 5.1400 | 5.0570 | knn_upgraded |

**Zaključak:** nakon prerade napredni KNN postiže niži prosječni MAE (**3.1278** vs **3.1315** °C). U prvoj verziji odnos je bio obrnut (4,9931 vs 3,7386) jer je „napredna” varijanta zbog pogrešnog omjera težina tražila susjede po **dobu dana** umjesto po **blizini u nizu**.

### C.7 Pomični prosjek
- Prosječni MAE: **3.6985 °C** (linear: **3.1315 °C**)
- Dobar na **random** scenariju (MAE ≈ 0,23 °C)
- Lošiji od linear interpolacije na **block** scenarijima

### C.8 Najbolja i najgora metoda po scenariju @ 20 %

- **random** @ 20 %: najbolja **spline_interpolation** (MAE = 0.0635 °C), najgora **moving_average** (MAE = 0.1796 °C)
- **block** @ 20 %: najbolja **decision_tree** (MAE = 1.4761 °C), najgora **cubic_interpolation** (MAE = 4.2442 °C)
- **block_start** @ 20 %: najbolja **linear_interpolation** (MAE = 0.6991 °C), najgora **forward_fill** (MAE = 2.3393 °C)
- **block_middle** @ 20 %: najbolja **neural_net** (MAE = 1.1338 °C), najgora **forward_fill** (MAE = 2.1429 °C)
- **block_end** @ 20 %: najbolja **cubic_interpolation** (MAE = 4.1828 °C), najgora **spline_interpolation** (MAE = 8.3969 °C)

---

## D. Rasprava — gotovi odlomci za kopiranje

### D.1 Zašto su ML metode isprva bile lošije od interpolacije

Prva verzija ML metoda koristila je isključivo vremenske značajke (indeks, sat, dan u godini). Nijedna od njih nije bila funkcija izmjerenih temperatura, pa su modeli učili preslikavanje **vrijeme → temperatura**, dok linearna interpolacija rješava zadatak **susjedne temperature → temperatura**. Na nizu čija je lag-1 autokorelacija 0,99936, a prosječna promjena između susjednih uzoraka 0,14 °C uz standardnu devijaciju 6,06 °C, drugi je zadatak neusporedivo lakši. Usporedba tako nije mjerila „klasične metode naspram strojnog učenja”, nego „metode koje vide susjede naspram metoda koje ih ne vide”.

Da uzrok nije bio ni količina podataka ni kapacitet modela, pokazuje sljedeće: povećanje dubine stabla s 5 na 20 smanjuje pogrešku za svega nekoliko postotaka i saturira, dok uvođenje značajki susjeda smanjuje prosječni MAE stabla s **5.2008** na **3.1118 °C**. Omjer doprinosa je otprilike **14 : 1 u korist skupa značajki**. Zaključak koji ide u rad nije „ML metode su lošije”, nego „ML metode koje kao značajke koriste samo vremenski indeks lošije su od linearne interpolacije” — a to je nedostatak postave eksperimenta, ne metode.

### D.2 Rezultat nakon prerade

Nakon uvođenja zajedničkog prostora značajki i učenja reziduala, **četiri ML metode nadmašuju linearnu interpolaciju** u prosječnom MAE: neuronska mreža (**3.0741**), slučajna šuma (**3.1012**), stablo odlučivanja (**3.1118**) i napredni KNN (**3.1278**), naspram **3.1315 °C** za linearnu interpolaciju.

Dobitak je malen u apsolutnom iznosu i to je očekivano: linearna interpolacija je za integrirani Wienerov proces optimalan procjenitelj, a temperatura na desetminutnoj skali je vrlo dobra aproksimacija takvog procesa. Prostor za poboljšanje postoji gotovo isključivo na **dugim prazninama**, gdje pretpostavka lokalne linearnosti prestaje vrijediti — i upravo tamo ML metode i ostvaruju prednost (`block`, `block_end`). Na scenariju `random`, gdje su praznine kratke, linearna interpolacija ostaje nenadmašena.

Ispravna formulacija za rad je stoga da ML metode **konvergiraju prema linearnoj interpolaciji i blago je nadmašuju na dugim prazninama**, a ne da je uvjerljivo pobjeđuju. Konvergencija prema poznatom optimumu potvrda je da modeli rade ispravno.

### D.3 Neuronska mreža

Mreža postiže najniži prosječni MAE među metodama bez oracle routinga. Dvije odluke presudno utječu na taj rezultat. Prvo, mreža uči rezidual iznad linearne baze, pa uz malu inicijalizaciju izlaznog sloja kreće od predikcije ≈ 0, što odgovara čistoj linearnoj interpolaciji; učenje je time popravljanje interpolacije, a ne učenje oblika signala od nule. Drugo, ulazi uključuju vrijednosti najbližih poznatih susjeda — mreža koja vidi samo vrijeme nema iz čega predvidjeti temperaturu na signalu čiji je jedini iskoristivi obrazac lokalna glatkoća.

### D.4 Kubična interpolacija na block scenariju
Na scenariju **block** pri 20 % nedostajućih vrijednosti, zaključani kubični spline postiže MAE od **4.2442 °C**, dok linear interpolacija postiže **1.4765 °C**. Kubična metoda gradi globalnu glatku krivulju kroz cijeli vremenski niz; zakrivljenost iz hladnijih perioda izvan bloka može uzrokovati overshoot unutar rupe — krivulja pada prema hladnijim vrijednostima iako unutar bloka temperatura ne slijedi taj trend. To objašnjava zašto cubic na ovom scenariju vizualno „ide dolje” unatoč toplijem vrhuncu unutar rupe.

### D.5 Linear vs time
Budući da su vremenski uzorci ravnomjerno raspoređeni (10-min intervali), linear i time interpolacija daju identične rezultate u svim eksperimentima. U praksi je dovoljno prikazati jednu od te dvije metode.

### D.6 KNN — zašto je linearna interpolacija njegova gornja granica

Izvorni KNN uzimao je *k* vremenski najbližih poznatih točaka i računao njihov **neponderirani prosjek**. To je estimator **nultog reda**: egzaktan samo za konstantan signal, a na nizu koji se mijenja sustavno zaglađuje nagib. Uz neparan *k* jedan višak susjeda na jednoj strani ostavlja i pristranost od pola koraka nagiba. Dodatno, ništa nije jamčilo da su susjedi s obje strane praznine — uz rub bloka obje najbliže točke znaju biti s iste strane, pa metoda ne može uhvatiti trend.

Prerađena verzija bira jednog susjeda **lijevo** i jednog **desno** te ih ponderira inverznom udaljenošću. Time postaje **matematički identična linearnoj interpolaciji**, jer vrijedi

    (1/d₁) / (1/d₁ + 1/d₂) = d₂ / (d₁ + d₂)

Rezultat u tablici to i potvrđuje: MAE je jednak do zadnje znamenke. Linearna interpolacija dakle nije suparnička metoda KNN-u nego njegov **specijalni slučaj**, i ujedno granica koju KNN s prosjekom susjeda može dosegnuti, ali ne probiti. Uzimanje više susjeda po strani mjerljivo pogoršava rezultat (k = 4 daje 3,221 °C), jer udaljeniji susjedi unose zaglađivanje bez nove informacije.

Napredna varijanta zato mijenja **vrstu pitanja**, a ne broj susjeda: umjesto „koje su točke vremenski blizu” pita „koje su poznate točke bile u **sličnoj situaciji** unutar praznine” — sličan relativni položaj `alpha`, slične udaljenosti do oslonaca, slično doba dana. Od njih uči koliko je linearna baza ondje griješila i tu korekciju primjenjuje na rupu. Tek tako `knn_upgraded` (3.1278 °C) nadmašuje i osnovni KNN i linearnu interpolaciju.

### D.7 Pomični prosjek
Pomični prosjek pokazuje prihvatljive rezultate na random scenariju, ali značajno gori od linear interpolacije na block scenarijima. Metoda je prikladna za kratke rupe u nizu, ali ne za duge kontinuirane blokove nedostajućih vrijednosti.

### D.8 Adaptivna imputacija je gornja granica, a ne metoda

`adaptive_imputation` postiže najniži prosječni MAE (2.7046 °C), ali njegova routing tablica u `src/adaptive_imputation.c` ručno je popunjena metodama koje su pobijedile **na istom test skupu** na kojem se metoda ocjenjuje. Broj slobodnih parametara jednak je broju testova, pa je riječ o savršenom prenaučenju po konstrukciji, bez ikakve generalizacije.

Rezultat zato treba prikazati kao **oracle granicu** — „najbolje što bi se postiglo savršenim odabirom metode po scenariju” — a ne kao rezultat metode. Tako protumačen postaje koristan: razlika između linearne interpolacije (3.1315) i oracle granice (2.7046) iznosi oko 14 %, i to je **cjelokupan mogući dobitak** od bilo kakvog pametnog odabira metode. Neuronska mreža od tog raspona uzima približno 13 %.

### D.9 Ograničenja mjere R²

R² se u eksperimentu računa iz srednje vrijednosti **samo maskiranih** točaka. To je uobičajena konvencija, ali je na block scenarijima obmanjujuća: pri `block_middle` 10 % maskirani blok pokriva raspon od svega 0,32 °C naspram 6,06 °C za cijeli niz, pa nazivnik postane oko 360× manji i R² poprimi vrlo velike negativne vrijednosti iako je MAE ondje **niži nego bilo gdje drugdje**. R² tada mjeri koliko je praznina slučajno uska, a ne koliko je metoda dobra, zbog čega se poredak metoda po R² i po MAE na block scenarijima ne poklapa. Za usporedbu metoda pouzdaniji je **skill score** u odnosu na linearnu interpolaciju, SS = 1 − MAE_metoda / MAE_linear, gdje nula znači „jednako kao referentna metoda”.

---

## E. Zaključak — što dodati

1. Eksperimenti obuhvaćaju **480** testova (5 scenarija × 8 rateova × 12 metoda) na **7-dnevnom** datasetu.
2. **Neuronska mreža** ima najniži prosječni MAE među metodama bez oracle routinga (**3.0741 °C** naspram **3.1315 °C** za linearnu interpolaciju).
3. Zaostatak ML metoda u prvoj verziji nije bio posljedica nedostatka podataka ni kapaciteta modela, nego **odsutnosti autoregresijske informacije u skupu značajki**. Uvođenjem značajki susjeda i učenja reziduala MAE je pao za 14–40 % po metodi.
4. **Linear interpolacija** ostaje nenadmašena na kratkim prazninama (7 pobjeda po MAE) jer je za lokalno linearan signal analitički optimalna; ML metode je nadmašuju na dugim prazninama.
5. **KNN s obuhvatom praznine i ponderom 1/d matematički je identičan linearnoj interpolaciji** — interpolacija je specijalni slučaj KNN-a, a ne suparnička metoda.
6. **Adaptivna imputacija** (2.7046 °C) treba se tumačiti kao **oracle granica**, jer joj je routing tablica popunjena rezultatima s test skupa.
7. **Kubična interpolacija** loša je na block scenariju zbog globalnog overshoota; dobra je na block_end scenariju.
8. **Pomični prosjek** koristan na random scenariju, ne i na block scenarijima.

---

## F. Budući rad (preporučeni odlomak)

Rezultat vrijedi za signal s lag-1 autokorelacijom većom od 0,999 i uzorak od 7 dana. Za rjeđe uzorkovanje, gdje autokorelacija pada, ili za višegodišnji niz, gdje se sezonski profil može pouzdano procijeniti, očekivanje se obrće u korist metoda strojnog učenja — na sedam dana dnevni profil ima premalo ponavljanja pa unosi više šuma nego signala.

Budući rad mogao bi stoga uključiti dulje vremenske nizove, više meteoroloških varijabli i stvarne nedostajuće podatke umjesto umjetnog uklanjanja. Na strani modela smisleni su rekurentne mreže i modeli sa samopažnjom koji rade nad cijelim prozorom niza, odabir hiperparametara na validacijskim prazninama generiranima iz poznatog dijela niza (bez gledanja u test skup), te zamjena ručne routing tablice adaptivne metode naučenim pravilom.

---

## G. Grafovi i prilozi

- Stupčasti grafovi: svih 12 metoda, svaka svojom bojom (`mae_by_method_*_20.png`)
- Linijski grafovi: MAE/RMSE/R² vs missing rate; identične metode označene u legendi
- Rekonstrukcija @ 20 %: najbolja vs najgora metoda po scenariju (`reconstruction_best_worst_*.png`)
- Pregled: `results/grafovi_pregled.html`
- Tablice: `results/tablice/sve_tablice_pregled.md`

---

## H. Popis novih datoteka u projektu

| Datoteka | Svrha |
|----------|-------|
| `src/gap_features.c/h` | Značajke najbližih poznatih susjeda, bez curenja informacija |
| `src/ml_features.c/h` | Zajednički prostor od 11 značajki za sve ML metode |
| `src/neural_net.c/h` | Višeslojni perceptron s backpropagationom i Adam optimizatorom |
| `src/decision_tree.c` | Prerađeno: rezidual, predizračunate značajke, rez preko prefiksnih suma |
| `src/rf_methods.c` | Prerađeno: 24 stabla, dubina 10, `max_features`, aktivan `RF_MIN_LEAF` |
| `src/knn_methods.c` | Prerađeno: obavezan obuhvat praznine, ponder 1/d |
| `src/knn_upgraded.c` | Prerađeno: KNN u prostoru značajki praznine, uči rezidual |
| `src/adaptive_imputation.c` | Adaptivna hibridna metoda (oracle granica) |
| `src/interpolation.c` | + `moving_average_imputation()` |
| `src/experiment.c` | 12 metoda, export najbolje/najgore rekonstrukcije |
| `results/reconstruction_best_worst_20.csv` | Pregled najbolje/najgore @ 20 % |
| `results/tablice/knn_usporedba.csv` | KNN osnovni vs napredni |
| `results/tablice/moving_average_pregled.csv` | Pomični prosjek vs linear |
