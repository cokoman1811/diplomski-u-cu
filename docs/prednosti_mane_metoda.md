# Prednosti i mane svih metoda imputacije

*Temeljeno na kodu projekta `diplomski-u-cu` i rezultatima iz `results/error_vs_missing_rate.csv` (Jena, 20 tjednih prozora).*

---

## Sažetak — tko pobjeđuje gdje

| Scenarij | Najbolje metode (MAE) | Najgorе metode |
|----------|----------------------|----------------|
| **Random** @ 40% | spline/linear (~0.106°C) | forward_fill (0.245), moving_average (0.220) |
| **Block** @ 40% | random_forest (2.82), knn_upgraded (2.82), neural_net (2.83) | cubic/spline (**11.47**) |
| **Block start** @ 40% | neural_net (3.23), linear (3.19) | spline (10.71), cubic (7.71) |
| **Block middle** @ 40% | neural_net (3.37), svi ML ~3.37 | cubic/spline (9.22) |
| **Block end** @ 40% | linear/knn (2.81) | spline (10.24), cubic (7.46) |

**Glavni nalaz:** nema univerzalnog pobjednika. Random → interpolacije. Block → ML metode. Cubic/spline katastrofalni na dugim blokovima.

---

## Klasične metode

### 1. Forward fill (`forward_fill`)

**Što radi:** Zadnja poznata vrijednost se kopira unaprijed.

**Prednosti:**
- Najjednostavnija metoda — trivijalna implementacija
- Uvijek radi (ne treba susjede s obje strane)
- Brza — O(n)
- Dobra za kratke rupe na stabilnom signalu

**Mane:**
- Na random @ 40%: MAE **0.245°C** — među najgorima
- Na block @ 40%: MAE **4.05°C** — vrlo loše
- Stvara “stepenice” — nerealne horizontalne segmente
- Ne koristi informaciju s desne strane rupe
- Što je rupa duža, to je greška veća (drži zastarjelu vrijednost)

**Kada koristiti:** Kratki prekidi senzora, signal koji se sporo mijenja, kad treba brzo i jednostavno rješenje.

---

### 2. Linearna interpolacija (`linear_interpolation`)

**Što radi:** Ravna crta između lijevog i desnog poznatog susjeda.

**Prednosti:**
- Jednostavna, brza, interpretabilna
- Odlična na **random** scenariju (MAE 0.107 @ 40%)
- Dobra na **block** scenariju (MAE 2.83 @ 40%) — baza za ML metode
- Ne oscilira, ne “eksplodira”
- Referentna metoda u eksperimentu — statistički najbolja ili izjednačena na randomu

**Mane:**
- Pretpostavlja linearni trend — ne hvata zakrivljenost (podne, noć)
- Na block_start @ 40%: MAE 3.19 — gubi od ML metoda
- Ne koristi vremenske značajke (sat, dan)
- Na vrlo dugim blokovima i dalje greši (crta ne prati stvarni oblik)

**Kada koristiti:** Random missing, kratke do srednje rupe, kad treba pouzdana bazna metoda.

---

### 3. Vremenska interpolacija (`time_interpolation`)

**Što radi:** Linearna interpolacija, ali uzorka po stvarnom vremenu (`epoch`), ne po indeksu.

**Prednosti:**
- Teoretski ispravnija kad su intervali nejednaki
- Ista jednostavnost kao linearna

**Mane:**
- Na Jena podacima **identična** linearnoj (ravnomjerni 10-min intervali)
- Nema dodatne koristi u ovom projektu
- Ne koristi temperaturne obrasce

**Kada koristiti:** Samo kad podaci imaju nejednake vremenske razmake (nije slučaj u Jena datasetu).

---

### 4. Kubna interpolacija (`cubic_interpolation`)

**Što radi:** Polinom 3. stupnja kroz poznate točke — glatka krivulja.

**Prednosti:**
- Na **random** @ 40%: MAE **0.106°C** — među najboljima
- Glatka krivulja — nema oštrih kutova
- Dobra za kratke, raspršene rupe

**Mane:**
- Na **block** @ 40%: MAE **11.47°C** — **najgora metoda**
- Overshoot — krivulja “iskače” između susjeda na dugim prazninama
- Zahtijeva dovoljno poznatih točaka s obje strane
- R² negativan na block scenariju (gore od srednje vrijednosti)
- Statistički značajno lošija od linearne (Δ MAE +6.0°C u testu značajnosti)

**Kada koristiti:** Samo random missing, niske stope (10–40%). **Nikad** na dugim blokovima.

---

### 5. Spline interpolacija (`spline_interpolation`)

**Što radi:** Krivulja koja prolazi kroz sve poznate točke — glatka, bez skokova.

**Prednosti:**
- Na **random** @ 40%: MAE **0.106°C** — najbolja (uz cubic)
- Vrlo glatka rekonstrukcija na raspršenim rupama
- Adaptivna bira spline za random scenarij

**Mane:**
- Na **block** @ 40%: MAE **11.47°C** — jednako loša kao cubic
- Na block_end @ 40%: MAE **10.24°C**
- Overshoot na dugim blokovima (vidljivo na grafovima)
- Statistički najlošija metoda ukupno (Δ MAE +7.3°C vs linear)
- U kodu dijeli jezgru s cubic — identični rezultati na block scenariju

**Kada koristiti:** Random missing, niske stope. Izbjegavati na block scenarijima.

---

### 6. Pokretni prosjek (`moving_average`)

**Što radi:** Prosjek zadnjih N poznatih vrijednosti (prozor 5).

**Prednosti:**
- Jednostavna, intuitivna
- Usporava šum u podacima
- Ne zahtijeva susjede s obje strane

**Mane:**
- Na random @ 40%: MAE **0.220°C** — lošija od linearne
- Na block @ 40%: MAE **3.97°C**
- Zaostaje za promjenama (lag) — kopira prošlost
- Ne koristi desni susjed
- Statistički značajno lošija od linearne (Δ MAE +0.74°C)

**Kada koristiti:** Rijetko optimalna u ovom projektu. Može pomoći na jako šumnim signalima.

---

## ML metode

### 7. KNN — osnovni (`knn` / `knn_imputation`)

**Što radi:** Za rupu traži k najsličnijih poznatih točaka (po poziciji, satu, danu) i uzima prosjek temperatura.

**Prednosti:**
- Jednostavna ML ideja — “slična situacija → slična temperatura”
- Na Jena podacima **identičan** linear/knn rezultat (konstrukcija značajki)
- Brz — nema treninga, samo pretraga

**Mane:**
- Ne koristi gap-značajke (susjede) — slabiji od upgraded verzije
- U eksperimentu zamijenjen s `knn_upgraded`
- Ne uči rezidual — pokušava pogoditi temperaturu direktno
- Skaliranje loše na velikim skupovima (O(n) po rupi)

**Kada koristiti:** Referentna/bazna KNN verzija. U praksi koristi `knn_upgraded`.

---

### 8. KNN upgraded (`knn_upgraded`)

**Što radi:** KNN s gap-značajkama, cikličkim satom/danom i težinama značajki.

**Prednosti:**
- Na **block** @ 40%: MAE **2.82°C** — među najboljima
- Koristi susjede i vrijeme — pametniji od osnovnog KNN
- Nema treninga — radi odmah
- Brz na malim nizovima (jedan tjedan)

**Mane:**
- Na **random** @ 40%: MAE **0.126°C** — gubi od spline/linear (0.106)
- Statistički značajno lošiji od linearne ukupno (Δ +0.01°C)
- Spor na velikim skupovima (pretraga svih poznatih za svaku rupu)
- Težine značajki ručno postavljene — nisu naučene
- Crna kutija — teže objasniti zašto je odabrao baš tih k susjeda

**Kada koristiti:** Block missing, kad treba brza ML metoda bez treninga.

---

### 9. Decision Tree (`decision_tree`)

**Što radi:** Regresijsko stablo — uči korekciju iznad linearne baze pitanjima DA/NE na 11 značajki.

**Prednosti:**
- Na **block** @ 40%: MAE **2.83°C** — među najboljima
- **Interpretabilan** — vidiš pitanja i listove
- Uči rezidual — pametna baza (linearna interpolacija)
- Brz trening i predikcija na malom nizu
- Gap-značajke — vidi susjede i poziciju u rupi

**Mane:**
- Na **random** @ 40%: MAE **0.119°C** — gubi od spline (0.106)
- Statistički lošiji od linearne ukupno (Δ +0.07°C)
- Na block_start @ 40%: MAE 3.50 — gubi od neural_net
- Grubi listovi — ista korekcija za slične ali ne identične situacije
- Overfitting rizik na malom broju poznatih točaka
- Stablo se gradi svaki put iznova — nema trajnog modela

**Kada koristiti:** Block missing, kad treba objašnjiv ML model za obranu.

---

### 10. Random Forest (`random_forest`)

**Što radi:** 24 stabla, svako uči rezidual; predikcija = prosjek svih stabala.

**Prednosti:**
- Na **block** @ 40%: MAE **2.82°C** — **najbolji** na tom scenariju
- Stabilniji od jednog stabla (prosjek smanjuje varijancu)
- Uči rezidual — ista pametna baza kao DT
- Slučajni podskup značajki po čvoru — manje overfittinga

**Mane:**
- Na **random** @ 40%: MAE **0.108°C** — blizu linearne, ali ne najbolji
- Sporiji od DT (24 stabla × dubina 10)
- Manje interpretabilan od jednog stabla
- Statistički lošiji od linearne ukupno (Δ +0.03°C)
- Na block_start gubi od neural_net i linearne

**Kada koristiti:** Block missing @ srednje visoke stope — najbolji ML rezultat u projektu.

---

### 11. Neural Net (`neural_net`)

**Što radi:** MLP (11→24→12→1), uči rezidual backprop + Adam, 200 epoha.

**Prednosti:**
- Na **block** @ 40%: MAE **2.83°C** — jednak DT i RF
- Na **block_start** @ 40%: MAE **3.23°C** — najbolji na tom scenariju
- Nelinearna — može uhvatiti složenije obrasce od stabla
- Uči rezidual — ista baza kao DT/RF
- Implementiran od nule u C-u — bez vanjskih biblioteka

**Mane:**
- Na **random** @ 40%: MAE **0.133°C** — gori od spline (0.106)
- **Crna kutija** — teško objasniti pojedinačnu predikciju
- Sporiji trening (200 epoha × backprop)
- Više hiperparametara (slojevi, learning rate, epohe)
- Statistički lošiji od linearne ukupno (Δ +0.02°C)
- Na 80% random: MAE 0.30 — najgori ML na tom scenariju
- Overfitting rizik na malom datasetu (jedan tjedan)

**Kada koristiti:** Block scenariji, block_start. Kad želiš pokazati da deep learning pristup radi, ali nije dramatično bolji od stabla.

---

### 12. Adaptivna imputacija (`adaptive_imputation`)

**Što radi:** Analizira masku (oblik rupe), bira metodu iz unaprijed pripremljene tablice (oracle routing).

**Prednosti:**
- Na **random** @ 40%: MAE **0.106°C** — jednako spline (bira spline)
- Automatski odabir metode — ne moraš ručno birati
- Praktična ideja za različite tipove kvara senzora
- Brza — samo lookup + poziv druge metode

**Mane:**
- **Nije ML model** — rule-based dispečer
- Tablica je empirijska — “što je bilo najbolje u našim eksperimentima”
- Na **block** @ 40%: MAE 2.83 — OK, ali ne najbolji
- Na **block_middle** @ 40%: MAE 3.38 — gubi od RF/DT
- Na **block** @ 80%: MAE **11.63°C** — bira forward_fill, katastrofa
- Statistički **najlošija** hibridna metoda ukupno (Δ +1.54°C vs linear)
- Zahtijeva **masku** — jedina metoda koja je ne može dobiti bez eksperimenta
- Ne uključuje neural_net ni moving_average u pool
- Ne garantira optimum na novim podacima

**Kada koristiti:** Kao demonstracija hibridnog pristupa. Ne kao glavni zaključak rada.

---

## Usporedna tablica — sve metode odjednom

| Metoda | Tip | Brzina | Objašnjivost | Random 40% | Block 40% | Glavna mana |
|--------|-----|--------|--------------|------------|-----------|-------------|
| forward_fill | klasična | ★★★★★ | ★★★★★ | loša | loša | stepenice, zastarjela vrijednost |
| linear | klasična | ★★★★★ | ★★★★★ | **odlična** | dobra | ne hvata zakrivljenost |
| time | klasična | ★★★★★ | ★★★★★ | = linear | = linear | beskorisna na Jena podacima |
| cubic | klasična | ★★★★ | ★★★★ | dobra | **katastrofa** | overshoot na blokovima |
| spline | klasična | ★★★★ | ★★★★ | **najbolja** | **katastrofa** | overshoot na blokovima |
| moving_average | klasična | ★★★★★ | ★★★★★ | loša | loša | zaostaje za signalom |
| knn | ML | ★★★ | ★★★ | = linear | dobra | bez gap-značajki |
| knn_upgraded | ML | ★★★ | ★★★ | dobra | **odlična** | spor, random gubi |
| decision_tree | ML | ★★★★ | ★★★★★ | dobra | **odlična** | grubi listovi |
| random_forest | ML | ★★★ | ★★★ | dobra | **najbolja** | sporiji, manje jasan |
| neural_net | ML | ★★ | ★★ | dobra | odlična | crna kutija, spor trening |
| adaptive | hibridna | ★★★★ | ★★★★ | dobra | dobra | nije pravi ML, oracle tablica |

---

## Preporuka po scenariju (za rad / obranu)

| Ako imaš... | Koristi | Zašto |
|-------------|---------|-------|
| Raspršene rupe (random) | **spline** ili **linear** | MAE ~0.106°C, jednostavno, pouzdano |
| Dugi blok u sredini | **random_forest** ili **decision_tree** | MAE ~2.82°C, uče lokalne korekcije |
| Dugi blok na početku | **neural_net** ili **linear** | MAE ~3.19–3.23°C |
| Dugi blok na kraju | **linear** / **knn** | MAE ~2.81°C |
| Ne znaš tip rupe | **linear** | najbolji kompromis, statistički referenca |
| Trebaš objasniti model | **decision_tree** | pitanja i listovi, interpretabilan |
| Trebaš pokazati deep learning | **neural_net** | isti rezultat kao DT na blocku |

---

## Jedna rečenica po metodi (za obranu)

| Metoda | Rečenica |
|--------|----------|
| forward_fill | Kopira zadnju poznatu vrijednost — brzo, ali loše na dugim rupama. |
| linear | Ravna crta između susjeda — najbolji kompromis i referenca. |
| cubic/spline | Glatka krivulja — odlična na randomu, katastrofalna na blokovima. |
| moving_average | Prosjek zadnjih vrijednosti — zaostaje za promjenama. |
| knn_upgraded | Traži slične poznate situacije — dobar na blocku, slabiji na randomu. |
| decision_tree | Pitanja DA/NE uče korekciju crte — interpretabilan, jak na blocku. |
| random_forest | Prosjek 24 stabala — najbolji ML na block scenariju. |
| neural_net | MLP uči rezidual — jednak DT na blocku, crna kutija. |
| adaptive | Bira metodu po obliku rupe — praktična ideja, nije pravi ML. |

---

*Izvor metrika: `results/error_vs_missing_rate.csv`, testovi značajnosti: `results/znacajnost.md`*
