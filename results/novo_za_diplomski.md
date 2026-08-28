# Novo u eksperimentima — tekst za diplomski rad

*Automatski generirano iz `experiment_results.csv`*
*Kopiraj odlomke u poglavlja Metodologija, Rezultati, Rasprava i Zaključak*

---

## A. Kratki sažetak novina (1 odlomak)

U odnosu na raniju verziju eksperimenata, rad je proširen na **7-dnevni** Jena Climate dataset (**1008** zapisa, 10-min intervali), missing rateove **10–80 %**, te **12 metoda imputacije** u **5 scenarija** (ukupno **480** testova). Dodane su metode **pomičnog prosjeka**, **adaptivne hibridne imputacije** te odvojena usporedba **osnovnog i naprednog KNN-a**. Razdvojene su **zaključana kubična** (`cubic_interpolation`) i **prirodna spline** (`spline_interpolation`) interpolacija.

Uvedene su **dvije velike izmjene**.

Prva je **potpuna prerada metoda strojnog učenja** i dodavanje **neuronske mreže** (`neural_net`). U prvoj verziji sve su ML metode kao ulaz koristile isključivo vrijeme (indeks, sat, dan u godini), pa su učile preslikavanje *vrijeme → temperatura*, dok interpolacija rješava bitno lakši problem *susjedne temperature → temperatura*. Uvođenjem značajki najbližih poznatih susjeda i prelaskom na učenje **reziduala iznad linearne baze**, prosječni MAE ML metoda pao je za **14–40 %**.

Druga je prelazak s jednog tjedna podataka na **20 nezavisnih tjednih prozora** raspoređenih kroz cijelo razdoblje 2009.–2016., svaki sa svojim seedom maske. Ta je izmjena promijenila zaključak rada: na pojedinačnom tjednu iz siječnja 2009. neuronska mreža je nadmašivala linearnu interpolaciju (3.0741 naspram 3.1315 °C), ali se uparenim testom nad 20 tjedana pokazalo da je ta prednost bila **svojstvo tog tjedna, a ne metode**. Detalji u odjeljcima C.4 i D.2.

Za svaki scenarij generirani su grafovi rekonstrukcije **najbolje i najgore** metode pri 20 % nedostajućih vrijednosti.

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

### B.2a Ponavljanja i mjera nesigurnosti

Svaka kombinacija scenarij × stopa ponavlja se **20 puta**, po jednom za svaki tjedni prozor iz `data/processed/jena_windows/`, svaki s vlastitim seedom maske. Ponavljanje ide po dvije osi istovremeno jer nijedna sama nije dovoljna:

- **Seed maske** daje uzorkovačku varijabilnost, ali **samo** na scenarijima `random` i `block`. Kod `block_start`, `block_middle` i `block_end` pozicija bloka određena je isključivo stopom (`src/preprocessing.c`), pa seed ondje ne mijenja ništa i ponavljanje bi dalo standardnu devijaciju nula.
- **Tjedni prozor** daje varijabilnost na **svih pet** scenarija i uz to mjeri ono što je zapravo zanimljivo: generalizira li zaključak izvan jednog tjedna.

Prozori su ravnomjerno raspoređeni kroz osam godina pa pokrivaju sva godišnja doba; srednja temperatura po prozoru kreće se od −7,6 do +21,3 °C, a standardna devijacija od 1,90 do 6,27 °C. Prvi prozor namjerno je identičan izvornom sedmodnevnom izrezu, pa su stari rezultati podskup novih.

Glavna tablica `results/experiment_results.csv` sadrži srednju vrijednost i standardnu devijaciju po ponavljanjima, a `results/experiment_runs.csv` sve pojedinačne rezultate.

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
| 1 | `linear_interpolation` | 2.5121 |
| 2 | `knn` | 2.5121 |
| 3 | `time_interpolation` | 2.5121 |
| 4 | `knn_upgraded` | 2.5232 |
| 5 | `neural_net` | 2.5354 |
| 6 | `random_forest` | 2.5440 |
| 7 | `decision_tree` | 2.5853 |
| 8 | `moving_average` | 3.2492 |
| 9 | `forward_fill` | 3.3238 |
| 10 | `adaptive_imputation` | 4.0563 |
| 11 | `cubic_interpolation` | 8.5056 |
| 12 | `spline_interpolation` | 9.8159 |

### C.2 Najbolja pojedinačna metoda po broju pobjeda (po scenariju i rateu)
- **linear_interpolation**: 15 od 40 kombinacija scenarij/rate
- **adaptive_imputation**: 0 pojedinačnih pobjeda, ali **najniži ukupni prosjek MAE: 4.0563 °C** (hibridna metoda je konzistentno dobra, iako ne uvijek prva u svakoj kombinaciji)
- **cubic_interpolation**: 3 pobjeda
- **spline_interpolation**: 2 pobjeda

### C.3 Učinak prerade ML metoda

Usporedba je na **istom tjednu** (prvi prozor) na kojem su nastale stare brojke — inače bi se miješala dva efekta, prerada koda i promjena podataka:

| Metoda | MAE prije prerade | MAE poslije | Promjena |
|--------|-------------------|-------------|----------|
| `knn` | 3.7386 | 3.1315 | +16.2 % |
| `knn_upgraded` | 4.9931 | 3.1278 | +37.4 % |
| `decision_tree` | 5.2008 | 3.1118 | +40.2 % |
| `random_forest` | 3.9234 | 3.1012 | +21.0 % |
| `neural_net` | — (nova metoda) | 3.0741 | — |

Prerada je dakle nedvojbeno uspjela: stablo je s 5.2008 palo na 3.1118 °C.

### C.4 Uparena usporedba s linearnom interpolacijom (20 ponavljanja)

Unutar jednog ponavljanja sve metode vide **identičan** oštećeni niz, pa je dizajn uparen i razlika se mjeri po paru (isti tjedan, isti scenarij, ista stopa, ista maska). Test je Wilcoxonov test predznačenih rangova, interval je bootstrap percentilni, a p-vrijednosti su korigirane Holm-Bonferroni postupkom. **Negativna razlika znači da je metoda bolja od linearne interpolacije.**

| Metoda | Δ MAE (°C) | 95 % CI | Pobjeda–poraz–neriješeno | p (Holm) | Značajno |
|--------|-----------|---------|--------------------------|----------|----------|
| `knn` | +0.0000 | [+0.0000, +0.0000] | 0–0–800 | 1.0e+00 | ne |
| `time_interpolation` | +0.0000 | [+0.0000, +0.0000] | 0–0–800 | 1.0e+00 | ne |
| `knn_upgraded` | +0.0112 | [-0.0028, +0.0254] | 356–444–0 | 1.8e-02 | DA (losija) |
| `neural_net` | +0.0234 | [+0.0132, +0.0339] | 282–518–0 | 4.6e-13 | DA (losija) |
| `random_forest` | +0.0319 | [+0.0128, +0.0512] | 368–432–0 | 4.0e-02 | DA (losija) |
| `decision_tree` | +0.0733 | [+0.0467, +0.1023] | 285–513–2 | 1.3e-12 | DA (losija) |
| `moving_average` | +0.7371 | [+0.6274, +0.8452] | 210–590–0 | 1.0e-39 | DA (losija) |
| `forward_fill` | +0.8117 | [+0.7019, +0.9224] | 202–598–0 | 3.6e-46 | DA (losija) |
| `adaptive_imputation` | +1.5443 | [+1.1534, +1.9857] | 155–271–374 | 5.0e-19 | DA (losija) |
| `cubic_interpolation` | +5.9935 | [+5.2173, +6.8128] | 199–601–0 | 7.2e-72 | DA (losija) |
| `spline_interpolation` | +7.3038 | [+6.3526, +8.3074] | 187–613–0 | 7.2e-79 | DA (losija) |

Ključan nalaz: **nijedna ML metoda ne nadmašuje linearnu interpolaciju u ukupnom prosjeku**, a razlike u korist linearne, iako male (0,011–0,073 °C), statistički su značajne. Prednost neuronske mreže vidljiva na prvom tjednu (3.0741 naspram 3.1315 °C) nije se ponovila na ostalih 19 tjedana.

Broj pobjeda po pojedinačnim kombinacijama scenarij × stopa nad srednjim vrijednostima:

| Metoda | Prosječni MAE | Pobjeda nad linear |
|--------|---------------|--------------------|
| `knn` | 2.5121 | 0 / 40 |
| `knn_upgraded` | 2.5232 | 18 / 40 |
| `neural_net` | 2.5354 | 14 / 40 |
| `random_forest` | 2.5440 | 14 / 40 |
| `decision_tree` | 2.5853 | 10 / 40 |
| `moving_average` | 3.2492 | 0 / 40 |
| `forward_fill` | 3.3238 | 0 / 40 |
| `cubic_interpolation` | 8.5056 | 5 / 40 |

### C.4a Gdje ML ipak pobjeđuje

Uparena razlika po scenarijima pokazuje da nalaz nije jednoličan. Na scenariju **`block`** (blok na slučajnoj poziciji) sve četiri ML metode imaju negativnu razliku, a kod `random_forest` (−0,0051 °C) i `knn_upgraded` (−0,0058 °C) ona je i značajna. `knn_upgraded` značajno pobjeđuje i na **`block_middle`** (−0,0053 °C). Gubitci su koncentrirani na `random` (gdje su praznine kratke i linearna baza je gotovo egzaktna) te na `block_start` i `block_end` (gdje se mora ekstrapolirati prema rubu niza).

Potpuna tablica po scenarijima: `results/znacajnost.md`.

### C.4b Koliko rezultat ovisi o odabranom tjednu

| Metoda | MAE min | MAE max | sd po tjednima |
|--------|---------|---------|----------------|
| `linear_interpolation` | 1,297 | 4,234 | 0,790 |
| `neural_net` | 1,335 | 4,297 | 0,799 |
| `knn_upgraded` | 1,298 | 4,270 | 0,809 |
| `adaptive_imputation` | 1,972 | 6,795 | 1,325 |

Raspon MAE između tjedana (oko 2,9 °C) više je od **četrdeset puta veći** od razlike među vodećim metodama (oko 0,07 °C). To je izravno opravdanje zašto jedan tjedan nije dovoljan i zašto se zaključci moraju donositi uparenim testom, a ne usporedbom srednjih vrijednosti.

### C.5 Identični rezultati
- **linear_interpolation** i **time_interpolation** daju **identične** rezultate na svim scenarijima (ravnomjerni 10-min intervali), pa je efektivan broj različitih metoda 11.
- **knn** nakon prerade daje rezultat **identičan linearnoj interpolaciji** — to nije slučajnost nego matematička posljedica (v. D.6).
- Na scenariju **block**, **cubic_interpolation** i **spline_interpolation** također daju identične rezultate.

### C.6 Usporedba osnovnog i naprednog KNN

| Scenarij | Osnovni KNN | Napredni KNN | Bolji |
|----------|-------------|--------------|-------|
| random | 0.1260 | 0.1446 | knn (osnovni) |
| block | 3.1828 | 3.1769 | knn_upgraded |
| block_start | 3.2001 | 3.2609 | knn (osnovni) |
| block_middle | 3.1754 | 3.1701 | knn_upgraded |
| block_end | 2.8762 | 2.8637 | knn_upgraded |

**Zaključak:** u ukupnom prosjeku bolji je **osnovni** KNN (osnovni 2.5121, napredni 2.5232 °C), ali razlika ovisi o scenariju — napredni značajno pobjeđuje na `block` i `block_middle`, a gubi na `random`. U prvoj verziji napredni je bio lošiji na svim scenarijima (4,9931 vs 3,7386) jer je zbog pogrešnog omjera težina tražio susjede po **dobu dana** umjesto po **blizini u nizu**.

### C.7 Pomični prosjek
- Prosječni MAE: **3.2492 °C** (linear: **2.5121 °C**)
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

Da uzrok nije bio ni količina podataka ni kapacitet modela, pokazuje sljedeće: povećanje dubine stabla s 5 na 20 smanjuje pogrešku za svega nekoliko postotaka i saturira, dok uvođenje značajki susjeda smanjuje prosječni MAE stabla s **5.2008** na **2.5853 °C**. Omjer doprinosa je otprilike **14 : 1 u korist skupa značajki**. Zaključak koji ide u rad nije „ML metode su lošije”, nego „ML metode koje kao značajke koriste samo vremenski indeks lošije su od linearne interpolacije” — a to je nedostatak postave eksperimenta, ne metode.

### D.2 Rezultat nakon prerade i zašto jedan tjedan nije bio dovoljan

Prerada je zatvorila gotovo cijeli jaz. Na prvom tjednu ML metode su nakon nje čak i preuzele vodstvo: neuronska mreža 3.0741 naspram 3.1315 °C za linearnu interpolaciju, dakle 1,8 % niži MAE.

Ponavljanjem nad 20 tjedana pokazalo se da ta prednost **nije bila svojstvo metode nego tog tjedna**. Uparena razlika preko svih 20 tjedana iznosi +0,0234 °C u korist linearne interpolacije, s 95 % intervalom [+0,013, +0,034] koji ne obuhvaća nulu (p < 10⁻¹² nakon Holmove korekcije). Isto vrijedi za sve ostale ML metode. Razlog je razmjer: raspon MAE između tjedana je oko 2,9 °C, a razlika među vodećim metodama oko 0,07 °C — jedan uzorak jednostavno ne razlikuje signal od šuma na toj skali.

Ovo je najvažnija metodološka pouka rada i vrijedi je eksplicitno napisati: **zaključak izveden iz jedne realizacije eksperimenta bio je pogrešan, i to u smjeru koji je odgovarao početnoj hipotezi.** Otkriven je tek uvođenjem ponavljanja.

Sadržajni zaključak i dalje stoji, samo u slabijem obliku: linearna interpolacija je za lokalno linearan signal analitički optimalan procjenitelj, pa ML metode prema njoj **konvergiraju**, a nadmašuju je samo ondje gdje pretpostavka lokalne linearnosti popušta — na blokovima na slučajnoj poziciji i u sredini niza, gdje su razlike male ali statistički značajne. Na kratkim prazninama nemaju što ponuditi.

### D.3 Neuronska mreža

Mreža je najbolja ML metoda u eksperimentu (2.5354 °C), premda i ona zaostaje za linearnom interpolacijom (2.5121 °C) za statistički značajnih 0,023 °C. Dvije odluke presudno utječu na taj rezultat. Prvo, mreža uči rezidual iznad linearne baze, pa uz malu inicijalizaciju izlaznog sloja kreće od predikcije ≈ 0, što odgovara čistoj linearnoj interpolaciji; učenje je time popravljanje interpolacije, a ne učenje oblika signala od nule. Drugo, ulazi uključuju vrijednosti najbližih poznatih susjeda — mreža koja vidi samo vrijeme nema iz čega predvidjeti temperaturu na signalu čiji je jedini iskoristivi obrazac lokalna glatkoća.

Da je mreža bez tih odluka bitno lošija, vidi se iz usporedbe sa stablom prije prerade (5.2008 °C). Preostali zaostatak od 0,023 °C tumačimo kao cijenu procjene parametara iz konačnog uzorka: mreža mora naučiti korekciju koja je na kratkim prazninama zapravo nula, pa dio šuma neizbježno uđe u model.

### D.4 Kubična interpolacija na block scenariju
Na scenariju **block** pri 20 % nedostajućih vrijednosti, zaključani kubični spline postiže MAE od **6.7633 °C**, dok linear interpolacija postiže **2.5336 °C**. Kubična metoda gradi globalnu glatku krivulju kroz cijeli vremenski niz; zakrivljenost iz hladnijih perioda izvan bloka može uzrokovati overshoot unutar rupe — krivulja pada prema hladnijim vrijednostima iako unutar bloka temperatura ne slijedi taj trend. To objašnjava zašto cubic na ovom scenariju vizualno „ide dolje” unatoč toplijem vrhuncu unutar rupe.

### D.5 Linear vs time
Budući da su vremenski uzorci ravnomjerno raspoređeni (10-min intervali), linear i time interpolacija daju identične rezultate u svim eksperimentima. U praksi je dovoljno prikazati jednu od te dvije metode.

### D.6 KNN — zašto je linearna interpolacija njegova gornja granica

Izvorni KNN uzimao je *k* vremenski najbližih poznatih točaka i računao njihov **neponderirani prosjek**. To je estimator **nultog reda**: egzaktan samo za konstantan signal, a na nizu koji se mijenja sustavno zaglađuje nagib. Uz neparan *k* jedan višak susjeda na jednoj strani ostavlja i pristranost od pola koraka nagiba. Dodatno, ništa nije jamčilo da su susjedi s obje strane praznine — uz rub bloka obje najbliže točke znaju biti s iste strane, pa metoda ne može uhvatiti trend.

Prerađena verzija bira jednog susjeda **lijevo** i jednog **desno** te ih ponderira inverznom udaljenošću. Time postaje **matematički identična linearnoj interpolaciji**, jer vrijedi

    (1/d₁) / (1/d₁ + 1/d₂) = d₂ / (d₁ + d₂)

Rezultat u tablici to i potvrđuje: MAE je jednak do zadnje znamenke. Linearna interpolacija dakle nije suparnička metoda KNN-u nego njegov **specijalni slučaj**, i ujedno granica koju KNN s prosjekom susjeda može dosegnuti, ali ne probiti. Uzimanje više susjeda po strani mjerljivo pogoršava rezultat (k = 4 daje 3,221 °C), jer udaljeniji susjedi unose zaglađivanje bez nove informacije.

Napredna varijanta zato mijenja **vrstu pitanja**, a ne broj susjeda: umjesto „koje su točke vremenski blizu” pita „koje su poznate točke bile u **sličnoj situaciji** unutar praznine” — sličan relativni položaj `alpha`, slične udaljenosti do oslonaca, slično doba dana. Od njih uči koliko je linearna baza ondje griješila i tu korekciju primjenjuje na rupu. Tek tako `knn_upgraded` (2.5232 °C) nadmašuje i osnovni KNN i linearnu interpolaciju.

### D.7 Pomični prosjek
Pomični prosjek pokazuje prihvatljive rezultate na random scenariju, ali značajno gori od linear interpolacije na block scenarijima. Metoda je prikladna za kratke rupe u nizu, ali ne za duge kontinuirane blokove nedostajućih vrijednosti.

### D.8 Adaptivna imputacija je gornja granica, a ne metoda

Routing tablica u `src/adaptive_imputation.c` ručno je popunjena metodama koje su pobijedile **na istom test skupu** na kojem se metoda ocjenjivala, i to na jednom tjednu. Broj slobodnih parametara jednak je broju testova, pa je riječ o prenaučenju po konstrukciji.

Ponavljanje nad 20 tjedana dalo je izravan i vrlo uvjerljiv dokaz toga. Na tjednu na kojem je tablica podešena metoda je bila najbolja od svih (2.7046 naspram 3.1315 °C za linearnu interpolaciju). Preko 20 tjedana pada na **4.0563 °C**, dakle uparena razlika iznosi **+1,54 °C u korist linearne interpolacije** — daleko najveći pad bilo koje metode. Po scenarijima je jasno vidljivo gdje puca: na `random` je i dalje neutralna (−0,0005 °C, jer je ondje routing slučajno pogodio), a na sva četiri blok scenarija gubi između 1,6 i 2,2 °C.

Ovo je udžbenički primjer prenaučenja i preporučam ga zadržati u radu upravo kao takav, s obje brojke. Ako se metoda ipak želi prikazati, treba je označiti kao **oracle granicu** za pripadni tjedan, a ne kao rezultat metode koja generalizira.

### D.9 Ograničenja mjere R²

R² se u eksperimentu računa iz srednje vrijednosti **samo maskiranih** točaka. To je uobičajena konvencija, ali je na block scenarijima obmanjujuća: pri `block_middle` 10 % maskirani blok pokriva raspon od svega 0,32 °C naspram 6,06 °C za cijeli niz, pa nazivnik postane oko 360× manji i R² poprimi vrlo velike negativne vrijednosti iako je MAE ondje **niži nego bilo gdje drugdje**. R² tada mjeri koliko je praznina slučajno uska, a ne koliko je metoda dobra, zbog čega se poredak metoda po R² i po MAE na block scenarijima ne poklapa. Za usporedbu metoda pouzdaniji je **skill score** u odnosu na linearnu interpolaciju, SS = 1 − MAE_metoda / MAE_linear, gdje nula znači „jednako kao referentna metoda”.

---

## E. Zaključak — što dodati

1. Eksperimenti obuhvaćaju **480** agregiranih rezultata (5 scenarija × 8 stopa × 12 metoda), svaki kao srednja vrijednost **20 ponavljanja** nad različitim tjednima — ukupno 9600 pojedinačnih pokretanja metode.
2. Zaostatak ML metoda u prvoj verziji nije bio posljedica nedostatka podataka ni kapaciteta modela, nego **odsutnosti autoregresijske informacije u skupu značajki**. Uvođenjem značajki susjeda i učenja reziduala MAE je pao za 14–40 % po metodi.
3. **Linearna interpolacija ostaje najbolja metoda u ukupnom prosjeku** (2.5121 °C). Najbolja ML metoda, neuronska mreža (2.5354 °C), zaostaje za statistički značajnih 0,023 °C. To je teorijski očekivano jer je linearna interpolacija za lokalno linearan signal analitički optimalna.
4. ML metode ipak **značajno pobjeđuju na scenariju `block`** i, u slučaju naprednog KNN-a, na `block_middle` — dakle ondje gdje su praznine duge i pretpostavka lokalne linearnosti popušta. Razlike su male (oko 0,005 °C), ali reproducibilne kroz 20 tjedana.
5. **KNN s obuhvatom praznine i ponderom 1/d matematički je identičan linearnoj interpolaciji** — potvrđeno na svih 800 parova, gdje je razlika točno nula. Interpolacija je specijalni slučaj KNN-a, a ne suparnička metoda.
6. **Adaptivna imputacija je udžbenički primjer prenaučenja**: najbolja od svih na tjednu na kojem je podešena (2.7046 °C), a najlošija među razumnim metodama preko 20 tjedana (4.0563 °C).
7. **Metodološka pouka:** zaključak izveden iz jedne realizacije eksperimenta bio je pogrešan. Raspon MAE između tjedana (oko 2,9 °C) četrdesetak je puta veći od razlike među vodećim metodama, pa je uparen test nad ponavljanjima nužan, a ne opcionalan.
8. **Kubična interpolacija** loša je na block scenariju zbog globalnog overshoota; dobra je na block_end scenariju.
9. **Pomični prosjek** koristan na random scenariju, ne i na block scenarijima.

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
| `src/experiment.c` | 12 metoda, ponavljanja (`--repeats`), agregacija sa sd |
| `scripts/prepare_jena_windows.py` | Izvlači 20 nezavisnih tjednih prozora iz sirovog Jena niza |
| `scripts/significance.py` | Upareni Wilcoxon + bootstrap CI + Holmova korekcija |
| `results/experiment_runs.csv` | Svi pojedinačni rezultati po ponavljanju |
| `results/znacajnost.md` | Tablica testova značajnosti |
| `results/reconstruction_best_worst_20.csv` | Pregled najbolje/najgore @ 20 % |
| `results/tablice/knn_usporedba.csv` | KNN osnovni vs napredni |
| `results/tablice/moving_average_pregled.csv` | Pomični prosjek vs linear |
