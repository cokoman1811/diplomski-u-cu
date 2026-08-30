# Sadrzaj dokumenta `Diplomski-Toni_Jakelic_azurirano.docx`

SVEUČILIŠTE U SPLITU
FAKULTET ELEKTROTEHNIKE, STROJARSTVA I BRODOGRADNJE
DIPLOMSKI RAD
INTERPOLACIJA PODATAKA POMOĆU STROJNOG UČENJA
Toni Jakelić
Split, lipanj 2026.
SVEUČILIŠTE U SPLITU
FAKULTET ELEKTROTEHNIKE, STROJARSTVA I BRODOGRADNJE
Sveučilišni diplomski studij:	Računarstvo
Smjer/Usmjerenje:	Računarstvo
Oznaka programa:	120
Akademska godina:	2025./2026.
Ime i prezime:	Toni Jakelić
Broj indeksa:	0023144502
ZADATAK DIPLOMSKOG RADA
Naslov:	INTERPOLACIJA PODATAKA POMOĆU STROJNOG UČENJA
Zadatak:	U radu je potrebno istražiti i implementirati metode za interpolaciju odnosno imputaciju nedostajućih vrijednosti u temperaturnom vremenskom nizu. Potrebno je usporediti klasične interpolacijske metode s metodama strojnog učenja, uključujući KNN, Decision Tree i Random Forest. Nad odabranim skupom podataka potrebno je umjetno generirati nedostajuće vrijednosti u random i block scenarijima, provesti evaluaciju pomoću metrika MAE, RMSE i R² te prikazati i komentirati dobivene rezultate kroz tablice i grafove.
Prijava rada:	dd.mm.yyyy.
Rok za predaju rada:	20.08.2026.
Predsjednik
Odbora za diplomski rad:	Mentor:
prof. dr. sc.______________		     Josip Vasilj
IZJAVA
Ovom izjavom potvrđujem da sam diplomski rad s naslovom „Interpolacija podataka pomoću strojnog učenja” pod mentorstvom Josipa Vasilja pisao samostalno, primijenivši znanja i vještine stečene tijekom studiranja na Fakultetu elektrotehnike, strojarstva i brodogradnje, kao i metodologiju znanstveno-istraživačkog rada te uz korištenje literature koja je navedena u radu. Spoznaje, stavove, zaključke, teorije i zakonitosti drugih autora koje sam izravno ili parafrazirajući naveo u diplomskom radu citirao sam i povezao s korištenim bibliografskim jedinicama.
Student
Toni Jakelić

## UVOD

Razvoj mjernih sustava i dostupnost velikih količina podataka omogućili su detaljniju analizu pojava koje se mijenjaju kroz vrijeme. Takvi podaci često se prikazuju kao vremenski nizovi, odnosno kao slijed mjerenja poredanih prema vremenu nastanka. Čest primjer vremenskog niza predstavljaju meteorološka mjerenja, u kojima se temperatura i njezine promjene mogu jasno pratiti na dnevnoj, sezonskoj i godišnjoj razini. U stvarnim mjernim sustavima podaci nisu uvijek potpuni. Vrijednosti mogu nedostajati zbog kvara senzora, prekida komunikacije, nepravilnog spremanja podataka ili drugih tehničkih problema. Nedostajuće vrijednosti mogu otežati daljnju analizu, prikaz podataka i primjenu metoda strojnog učenja. Zbog toga je potrebno primijeniti postupke interpolacije i imputacije, kojima se pokušavaju procijeniti vrijednosti koje nedostaju.
Naslov rada, „Interpolacija podataka pomoću strojnog učenja”, odnosi se na problem procjene nedostajućih vrijednosti u temperaturnom vremenskom nizu. U ovom radu nedostajuće vrijednosti se ne popunjavaju samo jednostavnim matematičkim pravilima, nego i metodama koje iz postojećih podataka pokušavaju prepoznati obrasce ponašanja temperature. Cilj ovog diplomskog rada je istražiti, implementirati i usporediti više metoda za imputaciju nedostajućih vrijednosti u vremenskom nizu temperature. U radu se uspoređuju klasične metode, poput forward fill metode, linearne interpolacije, vremenske interpolacije, kubne interpolacije i spline interpolacije, s metodama strojnog učenja, uključujući napredni KNN, Decision Tree i Random Forest.
Kao skup podataka koristi se Jena Climate Dataset, iz kojeg se izdvaja temperaturna komponenta vremenskog niza. Kako bi se metode mogle objektivno usporediti, iz originalnog niza umjetno se uklanjaju vrijednosti, a zatim se provjerava koliko ih pojedina metoda može dobro rekonstruirati. Takav pristup omogućuje da se svaka metoda testira u istim uvjetima, uz poznate stvarne vrijednosti koje tijekom imputacije ostaju skrivene. Programska implementacija izvedena je modularno, uz odvojene korake učitavanja podataka, stvaranja maske, primjene metoda i evaluacije. U završnom dijelu rada prikazuju se rezultati, tumačenje ponašanja metoda i zaključak o tome u kojim uvjetima jednostavne interpolacijske metode mogu biti jednako korisne ili korisnije od složenijih metoda strojnog učenja.

## KORIŠTENI PODACI

Za eksperimentalni dio rada odabran je Jena Climate Dataset. Riječ je o meteorološkom vremenskom nizu s mjerenjima prikupljenima na meteorološkoj stanici Max Planck Institute for Biogeochemistry u Jeni, Njemačka. Skup podataka prikladan je za obradu vremenskih nizova jer sadrži više meteoroloških značajki zabilježenih kroz dulje vremensko razdoblje.

### Jena Climate Dataset

Opis Jena Climate skupa podataka preuzet je iz službenog Keras primjera za obradu vremenskih nizova. Keras se u ovom radu ne koristi u programskoj implementaciji, nego služi samo kao izvor za osnovne informacije o skupu podataka. Prema tom izvoru, Jena Climate Dataset sadrži meteorološka mjerenja prikupljena od 10. siječnja 2009. do 31. prosinca 2016. godine, a mjerenja su zabilježena svakih 10 minuta. [1]
Skup podataka obuhvaća više meteoroloških značajki, uključujući temperaturu, tlak zraka, relativnu vlažnost, tlak vodene pare, deficit tlaka vodene pare, specifičnu vlažnost, gustoću zraka, brzinu vjetra, maksimalnu brzinu vjetra i smjer vjetra. U ovom radu iz skupa se izdvaja temperaturna komponenta jer je cilj analizirati i rekonstruirati nedostajuće vrijednosti temperature. [1]

### Odabir temperature kao ciljne varijable

Ciljna varijabla je temperatura jer predstavlja prirodan vremenski niz s izraženim dnevnim i sezonskim obrascima. U kratkim vremenskim intervalima temperatura se najčešće mijenja postupno, zbog čega je prikladna za usporedbu klasičnih interpolacijskih metoda i metoda strojnog učenja. Svaki zapis u promatranom nizu ima vremensku oznaku i pripadnu vrijednost temperature, a cilj je rekonstruirati upravo one temperaturne vrijednosti koje su umjetno uklonjene iz niza.

### Struktura vremenskog niza

Nakon učitavanja podataka, iz skupa se izdvaja vremenska oznaka i vrijednost temperature. Vremenska oznaka pokazuje kada je mjerenje nastalo i koristi se za očuvanje kronološkog redoslijeda mjerenja, dok se temperatura koristi kao glavna varijabla nad kojom se provode eksperimenti. U pojednostavljenom obliku, svaki redak podataka sadrži jednu vremensku oznaku i pripadnu vrijednost temperature. Temperatura je numerička vrijednost koja se rekonstruira kada se umjetno ukloni iz niza. Kada se u eksperimentu ukloni 40 % vrijednosti, dio temperaturnih vrijednosti zamjenjuje se oznakom NaN, dok se maskom označava koja su mjesta uklonjena i koriste se za evaluaciju.
Slika - Primjer vremenskog niza s 40 % umjetno uklonjenih vrijednosti. Izvor: vlastita izrada prema pripremljenim podacima.

### Priprema podataka za eksperiment

Priprema podataka obuhvaća učitavanje CSV datoteke, pretvorbu vremenske oznake u oblik prikladan za obradu, izdvajanje temperaturnog stupca i provjeru kronološkog redoslijeda mjerenja. Budući da se radi o vremenskom nizu, važno je da podaci ostanu poredani prema vremenu nastanka jer redoslijed mjerenja izravno utječe na postupak rekonstrukcije nedostajućih vrijednosti. Nakon učitavanja, vremenska oznaka koristi se ne samo za očuvanje redoslijeda, nego i za izvođenje dodatnih informacija koje mogu biti korisne u daljnjoj obradi. Za metode strojnog učenja iz vremenske oznake mogu se izvesti dodatne značajke, primjerice položaj mjerenja u nizu, sat u danu i dan u godini. Te značajke pomažu modelima da bolje iskoriste vremenski kontekst, jer temperatura u određenom satu dana ili razdoblju godine može imati drugačije očekivane vrijednosti. Primjerice, temperature izmjerene tijekom noći često se razlikuju od temperatura izmjerenih tijekom dana, dok se vrijednosti u zimskom razdoblju mogu značajno razlikovati od vrijednosti u ljetnom razdoblju. Zbog toga dodatne vremenske značajke mogu pomoći metodama strojnog učenja da preciznije povežu poznate uzorke s nedostajućim vrijednostima koje je potrebno rekonstruirati.

### Umjetno uklanjanje vrijednosti

Kako bi se metode mogle objektivno usporediti, u radu se koriste umjetno uklonjene vrijednosti. Najprije se uzima poznati temperaturni niz, a zatim se dio vrijednosti namjerno uklanja i označava kao nedostajući podatak. Prednost ovakvog pristupa je u tome što su originalne vrijednosti i dalje poznate. Nakon što metoda rekonstruira nedostajuće vrijednosti, rekonstruirani niz može se usporediti s originalnim nizom i može se izračunati koliko je metoda pogriješila. U radu se koriste dva osnovna scenarija uklanjanja vrijednosti. Random missing scenarij uklanja pojedinačne vrijednosti na nasumičnim pozicijama, pa oko svake praznine često postoje poznate vrijednosti. Block missing scenarij uklanja kontinuirani blok uzastopnih vrijednosti, što je teži slučaj jer u sredini bloka nema poznatih mjerenja na koja se metoda može neposredno osloniti. Takav scenarij može predstavljati situaciju u kojoj senzor određeno vrijeme nije bilježio podatke ili je bio u kvaru. Za praćenje umjetno uklonjenih vrijednosti koristi se maska. Maska je polje iste duljine kao temperaturni niz: vrijednost 1 označava da je podatak na toj poziciji umjetno uklonjen, a vrijednost 0 označava da je podatak ostao poznat. Evaluacija se provodi samo na mjestima gdje je maska jednaka 1, jer se upravo na tim mjestima provjerava koliko je metoda dobro rekonstruirala poznatu, ali privremeno skrivenu vrijednost.
Slika - Tok pripreme podataka za eksperiment i evaluaciju metoda. Izvor: vlastita izrada prema implementaciji projekta.
Prikazani tok pokazuje da originalni niz ostaje sačuvan, dok se za potrebe eksperimenta stvara njegova oštećena kopija. Metode rade samo nad oštećenim nizom, a maska omogućuje da se pogreška računa isključivo na mjestima koja su namjerno uklonjena.

## PROGRAMSKA IMPLEMENTACIJA


### Struktura projekta

Projekt je organiziran modularno kako bi svaki dio obrade imao jasno definiranu ulogu. Budući da rad uključuje učitavanje podataka, umjetno stvaranje nedostajućih vrijednosti, više metoda imputacije, evaluaciju i spremanje rezultata, takvu logiku nije praktično držati u jednoj datoteci. Zato je projekt podijeljen na više programskih cjelina koje se mogu zasebno razvijati i provjeravati. Datoteke zaglavlja s nastavkom .h koriste se za deklaracije struktura i funkcija, dok se datoteke s nastavkom .c koriste za njihovu stvarnu implementaciju. Takva podjela olakšava organizaciju projekta jer se iz naziva modula može jasno vidjeti koji dio posla obavlja: učitavanje podataka, preprocessing, interpolaciju, metode strojnog učenja, evaluaciju ili pokretanje eksperimenta.
Ovakva struktura olakšava usporedbu više metoda jer se svaka metoda može razvijati i testirati kao zasebna funkcionalna cjelina. Promjena jedne metode ne zahtijeva mijenjanje ostatka projekta, pa je manja mogućnost pogreške i jednostavnije je dodati novu metodu ili prilagoditi postojeću. Nakon implementacije izrađeni su testovi za najvažnije module. Provjerava se učitavanje podataka, stvaranje maske, ponašanje klasičnih interpolacijskih metoda, rad KNN i ostalih metoda strojnog učenja te ispravnost evaluacijskih metrika. Testovi pomažu provjeriti da se nakon promjene jednog modula ostatak projekta i dalje ponaša očekivano.

### Series struktura

Središnji oblik podataka u projektu predstavlja struktura Series. Ona služi za pohranu temperaturnog vremenskog niza i pripadnih vremenskih značajki potrebnih za izvođenje metoda imputacije. Budući da je programska implementacija izrađena u programskom jeziku C, podaci se eksplicitno spremaju u zasebna polja odgovarajućih tipova. Na taj način struktura Series objedinjuje broj mjerenja, vrijednosti temperature, vremenske oznake i dodatne značajke izvedene iz vremena.
Slika - Prikaz Series strukture kao C objekta. Izvor: vlastita izrada prema implementaciji projekta.
Struktura Series sadrži broj uzoraka n, polje temperature temp, vremensku oznaku epoch te izvedene značajke hour i yday. Polje temp sadrži vrijednosti temperature i predstavlja glavnu varijablu koja se rekonstruira, dok se polje epoch koristi za očuvanje stvarnog vremenskog redoslijeda mjerenja. Značajke hour i yday predstavljaju sat u danu i dan u godini te se koriste kao dodatni vremenski opis svakog uzorka. Ovakva struktura omogućuje da klasične interpolacijske metode koriste redoslijed i vremensku udaljenost između mjerenja, dok metode strojnog učenja mogu koristiti dodatne vremenske značajke. Primjerice, KNN, Decision Tree i Random Forest mogu pri procjeni temperature uzeti u obzir u kojem se satu dana ili dijelu godine pojedino mjerenje nalazi.

### Učitavanje i priprema podataka

Učitavanje podataka započinje čitanjem pripremljene CSV datoteke koja sadrži vremenske oznake i vrijednosti temperature. Za potrebe rada koristi se temperaturni niz izdvojen iz Jena Climate skupa podataka, a u projektu se može koristiti i manji demonstracijski skup podataka za brže testiranje osnovne funkcionalnosti. Tijekom učitavanja izdvajaju se potrebni stupci, ponajprije vremenska oznaka i temperatura. Vremenska oznaka pretvara se u oblik prikladan za obradu u programu te se iz nje izvode dodatne značajke poput sata u danu i dana u godini. Na taj način se iz jedne vremenske oznake dobiva više informacija koje mogu biti korisne metodama strojnog učenja. Nakon učitavanja provjerava se je li niz ispravan i ima li dovoljan broj uzoraka za izvođenje eksperimenta. Pripremljeni niz predstavlja originalne podatke nad kojima se zatim umjetno stvaraju nedostajuće vrijednosti. Originalni niz se ne mijenja tijekom imputacije jer se kasnije koristi kao referenca za evaluaciju rekonstruiranih vrijednosti.

### Preprocessing i maska nedostajućih vrijednosti

Preprocessing dio projekta zadužen je za umjetno stvaranje nedostajućih vrijednosti. Umjesto korištenja skupa podataka u kojem stvarne vrijednosti već nedostaju i nisu poznate, u ovom radu se iz poznatog temperaturnog niza namjerno uklanja dio vrijednosti. Time nastaje oštećeni niz, dok originalni niz ostaje sačuvan za kasniju provjeru točnosti rekonstrukcije. Oštećeni niz može se promatrati kao kopija originalnog niza u kojoj su odabrane vrijednosti zamijenjene oznakom NaN. Uz oštećeni niz stvara se i maska, odnosno polje iste duljine kao temperaturni niz. Vrijednost 1 u maski označava da je podatak na toj poziciji umjetno uklonjen, dok vrijednost 0 označava da je podatak ostao poznat. Maska ima važnu ulogu u evaluaciji jer određuje na kojim se pozicijama računa pogreška. Vrijednost 1 označava mjesta na kojima su temperature namjerno uklonjene iz originalnog niza, pa se upravo na tim mjestima uspoređuju originalna i rekonstruirana temperatura. Time se provjerava ono što je metoda stvarno trebala procijeniti, a ne cijeli niz koji već sadrži velik broj poznatih vrijednosti. U projektu se koriste dva načina stvaranja nedostajućih vrijednosti. Random missing scenarij uklanja pojedinačne vrijednosti na nasumičnim pozicijama, pa opisuje manje prekide ili pojedinačne pogreške u mjerenju. Block missing scenarij uklanja veći uzastopni blok vrijednosti i bolje opisuje situaciju u kojoj senzor određeno vrijeme nije bilježio podatke, primjerice zbog kvara, prekida komunikacije ili problema u spremanju mjerenja. Glavni eksperiment prikazan je za 40 % umjetno uklonjenih vrijednosti jer taj udio jasno pokazuje razlike među metodama, a ipak ostavlja dovoljno poznatih podataka za rekonstrukciju.

### Implementacija klasičnih metoda

Klasične metode implementirane su kao skup funkcija koje nad istim oštećenim temperaturnim nizom stvaraju rekonstruirani izlazni niz. Ulaz u svaku metodu je niz u kojem su pojedine vrijednosti označene kao NaN, dok je izlaz novi niz u kojem se te vrijednosti zamjenjuju procjenama. Poznate vrijednosti pritom se zadržavaju, kako bi se mijenjale samo vrijednosti koje su stvarno nedostajale. Forward fill metoda prolazi kroz niz i svaku nedostajuću vrijednost popunjava zadnjom prethodno poznatom temperaturom. Linearna interpolacija pronalazi lijevu i desnu poznatu vrijednost oko praznine te vrijednosti između njih računa kao ravnomjernu promjenu. Vremenska interpolacija koristi isti princip, ali umjesto samog rednog broja uzorka uzima u obzir stvarnu vremensku oznaku. Kubna i spline interpolacija koriste zakrivljene funkcije za procjenu nedostajućih vrijednosti te mogu bolje pratiti nelinearne promjene u nizu. Njihovo ograničenje je veća osjetljivost na rubne slučajeve i dulje blokove nedostajućih podataka. Pomični prosjek za svaku prazninu prikuplja poznata mjerenja unutar prozora od šest uzoraka lijevo i desno te računa njihov prosjek; kada unutar tog prozora nema nijednog poznatog mjerenja, što se događa u unutrašnjosti duljih blokova, vrijednost se popunjava posljednjom poznatom temperaturom. U završnom eksperimentu uspoređeno je šest klasičnih metoda: forward fill, linearna interpolacija, vremenska interpolacija, kubna interpolacija, spline interpolacija i pomični prosjek.

### Značajke za metode strojnog učenja

Sve metode strojnog učenja dijele isti skup ulaznih značajki, pa razlika u njihovim rezultatima proizlazi iz modela, a ne iz različito pripremljenih ulaza. Za svaku točku niza računa se jedanaest značajki. Njih šest opisuje prazninu u kojoj se točka nalazi: posljednja poznata vrijednost s lijeve strane, prva poznata vrijednost s desne strane, udaljenost do svakog od tih rubova, relativan položaj točke unutar praznine te linearna procjena dobivena spajanjem dvaju rubova. Preostalih pet opisuje vrijeme mjerenja: normaliziran položaj u nizu te sat u danu i dan u godini, svaki prikazan sinusnom i kosinusnom komponentom.
Značajke o praznini presudne su za razumijevanje rezultata. Bez njih model vidi samo kada je mjerenje obavljeno, ali ne i kolika je temperatura bila neposredno prije i poslije praznine, iako upravo taj podatak nosi gotovo svu informaciju u ovako gusto uzorkovanom nizu. Pri računanju značajki za poznatu točku ta se točka izostavlja iz vlastitog susjedstva, kako model ne bi mogao naučiti odgovor iz same sebe.
Sve metode strojnog učenja uče odstupanje od linearne procjene, a ne samu temperaturu. Model dakle predviđa koliko linearna procjena griješi, a konačna vrijednost dobiva se zbrajanjem te procjene i naučenog odstupanja. Takva postavka daje modelu dobru polaznu točku: ako ne nauči ništa korisno, rezultat ostaje jednak linearnoj interpolaciji umjesto da bude znatno lošiji. Na kraju se svaka procjena ograničava na raspon poznatih temperatura u nizu, čime se sprječavaju vrijednosti izvan smislenog opsega.

### Implementacija KNN i napredne KNN metode

Obje KNN izvedbe implementirane su zasebno jer rješavaju različit problem. Osnovni KNN za svaku prazninu binarnim traženjem pronalazi najbližu poznatu točku lijevo i najbližu desno te ih ponderira inverznom udaljenošću. Uz jednog susjeda sa svake strane taj je izračun matematički istovjetan linearnoj interpolaciji, jer se omjer težina 1/d₁ i 1/d₂ svodi na d₂/(d₁+d₂). Osnovni KNN time nije suparnik linearnoj interpolaciji nego njezino poopćenje, pa u tablicama rezultata daje istu vrijednost. Sat u danu i dan u godini izostavljeni su iz mjere udaljenosti jer na sedmodnevnom prozoru dan u godini poprima samo osam različitih vrijednosti, a mjerenja su pokazala da njihovo uključivanje rezultat pogoršava.
Napredni KNN ne traži susjede po položaju nego po sličnosti situacije u kojoj se praznina nalazi. Svaka se točka opisuje s pet veličina: relativnim položajem unutar praznine, logaritmiranim udaljenostima do lijevog i desnog poznatog ruba te sinusnom i kosinusnom komponentom sata u danu. Logaritam se koristi zato što udaljenosti do rubova variraju od jednog do nekoliko stotina uzoraka, pa bi bez njega duge praznine potpuno prevladale u mjeri udaljenosti. Za svaku nedostajuću vrijednost pronalazi se dvanaest poznatih točaka s najsličnijim opisom, a njihova odstupanja od linearne procjene ponderiraju se inverznom udaljenošću u tom prostoru. Dobiveni prosjek dodaje se linearnoj procjeni, pa metoda zapravo uči u kojim se situacijama linearna procjena sustavno vara.

### Implementacija Decision Tree metode

Decision Tree metoda implementirana je kao stablo čvorova u kojem se podaci postupno dijele prema zadanim pravilima. Svaki unutarnji čvor sadrži pravilo podjele, odnosno odabranu značajku i prag prema kojem se uzorak usmjerava u lijevu ili desnu granu stabla. Završni čvorovi nazivaju se listovi i u njima se nalazi konačna vrijednost predikcije. Izgradnja stabla temelji se na traženju podjele koja najbolje razdvaja poznate uzorke. Za svaku značajku uzorci se najprije sortiraju po njezinoj vrijednosti, nakon čega se jednim prolaskom kroz sortirani niz i uz pomoć kumulativnih zbrojeva ocjenjuju svi mogući pragovi, a odabire se onaj s najmanjom kvadratnom pogreškom. Postupak se ponavlja dok se ne dosegne dubina osam ili dok u čvoru ne ostane manje od četiri uzorka. Stablo pritom ne uči samu temperaturu nego njezino odstupanje od linearne procjene, uz jedanaest ranije opisanih značajki. Kod procjene nedostajuće vrijednosti uzorak prolazi kroz naučeno stablo do odgovarajućeg lista, a vrijednost tog lista dodaje se linearnoj procjeni. Značajke se računaju unaprijed za cijeli niz i pohranjuju u matricu, pa se isti izračun ne ponavlja u svakom čvoru.

### Implementacija Random Forest metode

Random Forest metoda proširuje ideju stabla odlučivanja tako da koristi 24 stabla umjesto jednog. Svako se stablo uči na nasumično odabranom skupu poznatih uzoraka s ponavljanjem, zbog čega pojedina stabla nisu jednaka i mogu dati različite procjene za istu nedostajuću vrijednost. Drugi izvor raznolikosti je odabir značajki: u svakom se čvoru razmatra nasumičnih sedam od jedanaest dostupnih značajki umjesto svih. Bez tog ograničenja sva bi stabla birala vrlo slične podjele, pa bi njihovo prosječenje donijelo malo. Stabla u šumi smiju biti dublja od pojedinačnog stabla, do dubine deset, jer se njihova sklonost pretjeranom prilagođavanju podacima djelomično poništava prosječenjem, uz uvjet da svaki list sadrži najmanje četiri uzorka. Kao i pojedinačno stablo, šuma uči odstupanje od linearne procjene, pa se konačna imputirana temperatura dobiva zbrajanjem linearne procjene i prosjeka odstupanja svih stabala. Prednost metode je veća stabilnost u odnosu na jedno stablo, dok su ograničenja veća složenost i teže objašnjenje pojedinačne odluke.

### Implementacija neuronske mreže

Neuronska mreža implementirana je izravno u programskom jeziku C, bez vanjskih biblioteka, kako bi ostala usporediva s ostatkom sustava. Riječ je o višeslojnom perceptronu s jedanaest ulaza, dva skrivena sloja od 24 i 12 neurona te jednim izlazom. U skrivenim slojevima kao aktivacijska funkcija koristi se tangens hiperbolni, dok je izlaz linearan jer se predviđa realan broj, a ne razred.
Prije učenja svaka se ulazna značajka standardizira oduzimanjem prosjeka i dijeljenjem standardnom devijacijom, pri čemu se te veličine računaju isključivo na poznatim točkama kako podaci o uklonjenim vrijednostima ne bi procurili u model. Izlazna veličina, odstupanje od linearne procjene, također se skalira jer je reda nekoliko desetinki stupnja, a mreža stabilnije uči na veličinama reda jedan. Početne težine postavljaju se Xavierovom inicijalizacijom, a težine izlaznog sloja dodatno se umanjuju kako bi mreža na početku učenja predviđala odstupanje blizu nule. Polazna točka učenja time je čista linearna interpolacija, pa je mreža može popraviti, ali teško i pogoršati.
Učenje se provodi kroz 200 prolazaka nad nasumično promiješanim poznatim uzorcima, u serijama po 32 uzorka. Gradijenti se računaju propagacijom pogreške unatrag, a težine se osvježavaju Adam optimizatorom. [16] Stopa učenja počinje na 0,01 i kosinusno se gasi kroz prolaske, čime se završna faza učenja stabilizira. Nakon učenja mreža za svaku nedostajuću točku predviđa odstupanje, koje se dodaje linearnoj procjeni i ograničava na raspon poznatih temperatura.

### Eksperimentalni modul

Eksperimentalni modul predstavlja dio programa koji povezuje sve glavne korake rada u jednu cjelinu. On učitava pripremljeni temperaturni niz, stvara nedostajuće vrijednosti prema odabranom scenariju, pokreće sve metode i sprema dobivene rezultate. Bez tog modula svaku bi metodu trebalo ručno pokretati i zasebno uspoređivati, što bi bilo sporije i podložnije pogreškama. Središnja ideja eksperimentalnog modula je osigurati jednaku usporedbu metoda, tako da sve metode dobivaju isti oštećeni niz, isti udio nedostajućih vrijednosti i istu masku. Nakon što metoda rekonstruira vrijednosti, rezultat se evaluira usporedbom s originalnim nizom. Na taj način razlike u rezultatima proizlaze iz samih metoda, a ne iz različito pripremljenih ulaznih podataka. Modul se može koristiti za usporedbeni način rada, kada se analizira jedan scenarij i jedan udio nedostajućih vrijednosti, ili za širi eksperimentalni postupak, kada se pokreće više scenarija i više razina nedostajućih vrijednosti. Time se isti programski sustav može koristiti za brzu provjeru jedne metode, ali i za generiranje rezultata potrebnih za tablice i grafove u diplomskom radu.

### Spremanje rezultata u CSV datoteke

Nakon izvođenja eksperimenata rezultati se spremaju u CSV datoteke. CSV format je prikladan jer je jednostavan, čitljiv i može se otvoriti u različitim alatima za pregled i obradu podataka. Glavni C program zadužen je za izvođenje metoda, računanje evaluacijskih metrika i spremanje rezultata. Generirane CSV datoteke koriste se za pregled dobivenih vrijednosti, usporedbu metoda te pripremu tablica i grafičkih prikaza u diplomskom radu.

### Pipeline projekta

Pipeline projekta prikazuje redoslijed glavnih koraka, od učitavanja ulaznih temperaturnih podataka do spremanja rezultata. U prikazanom primjeru eksperiment se odnosi na slučaj s 40 % umjetno uklonjenih vrijednosti temperature. Nakon učitavanja izdvaja se temperaturni niz, stvaraju se nedostajuće vrijednosti i označavaju mjesta za evaluaciju. Zatim se nad istim oštećenim nizom pokreću metode imputacije, a dobivene rekonstrukcije uspoređuju se s originalnim vrijednostima pomoću evaluacijskih metrika.
Slika - Pipeline projekta za eksperiment s 40 % nedostajućih vrijednosti. Izvor: vlastita izrada prema implementaciji projekta.
Dijagram sažima opisani postupak i pokazuje kako se pojedini dijelovi projekta nastavljaju jedan na drugi: ulazni podaci, priprema niza, stvaranje maske, pokretanje metoda te zapisivanje rezultata za daljnju analizu.

### EKSPERIMENTALNI POSTUPAK


#### Scenariji nedostajućih vrijednosti

U eksperimentu je korišteno pet scenarija umjetnog uklanjanja temperaturnih vrijednosti. Scenarij random simulira pojedinačne nasumične nedostatke u nizu. Funkcija create_missing_values() nasumično odabire pozicije za uklanjanje, uz očuvanje prve i zadnje vrijednosti. Scenarij block uklanja jedan kontinuirani blok na nasumično odabranoj poziciji. Scenariji block_start, block_middle i block_end uklanjaju blok fiksne duljine na početku, u sredini odnosno na kraju niza. Duljina bloka izračunava se kao round(missing_rate × n). Svi scenariji koriste istu masku: vrijednost 1 označava umjetno uklonjeno mjesto, a evaluacija se provodi isključivo na tim pozicijama.

#### Različite razine nedostajućih vrijednosti

Testirani su missing rateovi od 10 %, 20 %, 30 %, 40 %, 50 %, 60 %, 70 % i 80 %. Manji postotak ostavlja više poznatih vrijednosti i olakšava rekonstrukciju, dok veći postotak smanjuje broj poznatih uzoraka i povećava težinu problema. Proširenjem do 80 % provjerava se koliko su metode stabilne u izrazito nepovoljnim uvjetima, kada je većina vrijednosti u nizu umjetno uklonjena. Na tjednom prozoru od 1008 zapisa to znači redom 101, 202, 302, 403, 504, 605, 706 i 806 uklonjenih vrijednosti. Broj stvarno uklonjenih i evaluiranih vrijednosti zapisan je u stupcima number_of_missing_values i number_of_evaluated_values u glavnoj CSV datoteci rezultata.

#### Evaluacijske metrike

Za usporedbu metoda korištene su regresijske metrike pogreške. Budući da metode u ovom radu rekonstruiraju numeričku vrijednost temperature, evaluacija se temelji na razlici između stvarne i rekonstruirane temperature. Evaluacija se ne računa nad cijelim nizom, nego samo nad vrijednostima koje su umjetno uklonjene i označene maskom. Takav način računanja pogreške usmjerava evaluaciju samo na skrivene vrijednosti koje je metoda trebala rekonstruirati. U nastavku su opisane metrike MAE, RMSE i R². Kod svih metrika uspoređuje se stvarna vrijednost temperature s rekonstruiranom vrijednosti, a n označava broj evaluiranih točaka.

##### MAE - srednja apsolutna pogreška

MAE (engl. Mean Absolute Error) označava srednju apsolutnu pogrešku. Računa se tako da se za svaku umjetno uklonjenu vrijednost izračuna apsolutna razlika između stvarne temperature i rekonstruirane temperature, a zatim se izračuna srednja vrijednost tih razlika. Budući da se ne gleda predznak pogreške, jednako se uzimaju u obzir previsoke i preniske procjene. [2]
Formula za MAE je:
MAE = prosjek apsolutnih pogrešaka
Niža MAE vrijednost znači da su rekonstruirane vrijednosti u prosjeku bliže stvarnim temperaturama. Budući da se MAE izražava u istoj mjernoj jedinici kao i temperatura, odnosno u stupnjevima Celzija, njezina interpretacija je jednostavna i intuitivna. Zbog toga je ova metrika korisna kada se želi jasno prikazati prosječna veličina pogreške rekonstrukcije.

##### RMSE - korijen srednje kvadratne pogreške

RMSE (engl. Root Mean Squared Error) označava korijen srednje kvadratne pogreške. Računa se tako da se pogreške najprije kvadriraju, zatim se izračuna njihov prosjek, a na kraju se uzima korijen dobivene vrijednosti. Zbog kvadriranja, veće pogreške imaju jači utjecaj na konačni rezultat nego manje pogreške. [3]
Formula za RMSE je:
RMSE = korijen prosjeka kvadriranih pogrešaka
RMSE je koristan kada se želi posebno naglasiti metoda koja ponekad napravi veće odstupanje. Kod temperaturnih podataka to je važno jer metoda može imati dobar prosjek, ali povremeno napraviti veliku pogrešku u nagloj promjeni temperature ili u duljem bloku nedostajućih vrijednosti.

##### R² - koeficijent determinacije

R² (koeficijent determinacije) koristi se kao dodatna mjera kvalitete rekonstrukcije. Ova metrika pokazuje koliko rekonstruirane vrijednosti dobro prate promjene u originalnom temperaturnom nizu. Najbolja moguća vrijednost je 1, što znači da su rekonstruirane vrijednosti savršeno usklađene sa stvarnim vrijednostima. [4]
Formula za R² može se zapisati kao:
R² = 1 - SSE / SST
U formuli SSE označava zbroj kvadriranih pogrešaka, odnosno ukupnu kvadratnu razliku između stvarnih i rekonstruiranih vrijednosti. SST označava ukupnu varijabilnost stvarnih vrijednosti temperature, odnosno koliko se stvarne vrijednosti razlikuju od svoje srednje vrijednosti. Ako je SSE mali u odnosu na SST, R² će biti bliže vrijednosti 1. Veća R² vrijednost znači da rekonstruirane vrijednosti bolje prate promjene originalnog temperaturnog niza. Ipak, u ovom radu su MAE i RMSE važnije za glavnu interpretaciju jer izravno pokazuju veličinu pogreške u stupnjevima Celzija. R² je korisna dopunska metrika, ali može biti manje intuitivna jer ne govori koliko stupnjeva metoda prosječno griješi, nego koliko dobro prati ukupne promjene u nizu.

#### Struktura rezultata u CSV datotekama

Glavna datoteka experiment_results.csv sadrži sažete rezultate svih eksperimenata. U njoj se nalaze stupci scenario, block_position, missing_rate, method, mae, rmse, r2, number_of_missing_values i number_of_evaluated_values. Ti stupci omogućuju usporedbu metoda po scenariju, postotku nedostajućih vrijednosti i evaluacijskim metrikama. Datoteke oblika reconstruction_{method}_{scenario}_{rate}.csv sadrže rekonstrukciju po svakoj točki vremenskog niza. U njima se nalaze index, timestamp, original_temperature, damaged_temperature, reconstructed_temperature, mask, scenario, block_position, missing_rate i method. Takva struktura omogućuje izradu grafova na kojima se uspoređuju originalni niz, oštećeni niz i rekonstruirani niz. Pomoćne datoteke mae_by_method.csv i error_vs_missing_rate.csv sadrže iste rezultate u obliku prikladnom za dodatnu analizu i grafički prikaz. Vizualni pregled grafova sprema se u results/grafovi_pregled.html.

## TEORIJSKA POZADINA I POVEZANA ISTRAŽIVANJA


### Vremenski nizovi i temperaturni podaci

Vremenski niz je skup podataka u kojem su vrijednosti poredane prema vremenu nastanka. Svaka vrijednost u takvom nizu povezana je s određenom vremenskom oznakom. Kod temperaturnih podataka to znači da svako mjerenje ima dvije osnovne informacije: vrijeme mjerenja i izmjerenu temperaturu.
Slika - Izvadak temperaturnog vremenskog niza iz Jena Climate skupa podataka. Izvor: vlastita izrada prema pripremljenim podacima.
Za razliku od običnog skupa podataka, kod vremenskog niza redoslijed vrijednosti ima vrlo važnu ulogu. Temperatura izmjerena u jednom trenutku obično je povezana s temperaturama koje su izmjerene neposredno prije i poslije nje, pa se vrijednosti ne mogu promatrati bez vremenskog konteksta. Primjer temperaturnog vremenskog niza može se prikazati kao niz mjerenja u pravilnim vremenskim razmacima. Ako se temperatura mjeri svakih deset minuta, tada se svako sljedeće mjerenje nadovezuje na prethodno, a može se očekivati da se temperatura između dva bliska mjerenja u većini slučajeva mijenja postupno. Temperaturni podaci imaju određene specifičnosti jer često pokazuju dnevne i sezonske obrasce. Vrijednosti temperature mogu se razlikovati između dana i noći, ali i između različitih godišnjih doba. Osim toga, temperatura se u kratkim vremenskim intervalima najčešće ne mijenja naglo, što je čini pogodnom za primjenu metoda interpolacije i imputacije. U ovom radu temperaturni niz promatra se kao jednodimenzionalni vremenski niz. Glavna vrijednost koja se analizira je temperatura, dok se vremenska oznaka koristi za očuvanje redoslijeda mjerenja i za izvođenje dodatnih značajki, poput sata u danu i dana u godini, što je posebno korisno kod metoda strojnog učenja.

### Nedostajući podaci u vremenskim nizovima

Nedostajući podaci predstavljaju vrijednosti koje bi trebale postojati u skupu podataka, ali iz nekog razloga nisu zabilježene ili nisu dostupne. U vremenskim nizovima to znači da za određeni trenutak ne postoji pripadna izmjerena vrijednost. Kod temperaturnih podataka to znači da za određeni vremenski trenutak nije poznata temperatura. Razlozi nastanka nedostajućih podataka mogu biti različiti, primjerice kvar senzora, prekid napajanja, gubitak komunikacije, pogreška pri spremanju podataka ili nepravilno očitanje. U meteorološkim mjerenjima takvi problemi nisu neuobičajeni jer se podaci često prikupljaju automatski i kroz dulje vremensko razdoblje. Nedostajuće vrijednosti mogu se pojaviti na različite načine. Ponekad nedostaje samo nekoliko pojedinačnih vrijednosti raspoređenih kroz niz, što se može promatrati kao nasumično nedostajanje podataka. U drugim slučajevima može nedostajati cijeli blok uzastopnih vrijednosti, primjerice ako senzor određeno vrijeme nije bilježio podatke. Razlika između pojedinačnih nedostajućih vrijednosti i blokova važna je za odabir metode popunjavanja. Ako nedostaje samo jedna vrijednost, često postoje poznate vrijednosti neposredno prije i poslije nje, pa je procjena jednostavnija. Ako nedostaje cijeli blok vrijednosti, metoda se mora osloniti na udaljenije poznate vrijednosti ili na obrasce naučene iz ostatka niza. Nedostajući podaci mogu otežati daljnju analizu, prikaz grafa, treniranje modela strojnog učenja i usporedbu različitih metoda, pa ih je prije analize često potrebno nadopuniti na način koji najbolje odgovara stvarnom ponašanju podataka. [13]

### Imputacija i interpolacija

Imputacija je opći naziv za postupak popunjavanja nedostajućih vrijednosti u skupu podataka. Cilj imputacije nije samo zamijeniti prazno mjesto bilo kojom vrijednošću, nego što bolje procijeniti vrijednost koja bi se stvarno mogla nalaziti na tom mjestu. U ovom radu imputacija se primjenjuje na nedostajuće vrijednosti temperature. Interpolacija je jedan oblik imputacije i najčešće se koristi kada postoje poznate vrijednosti prije i poslije nedostajuće vrijednosti. Tada se procjenjuje vrijednost koja bi se nalazila između njih. Primjerice, ako je temperatura u 10:00 jednaka 18 °C, a u 10:20 jednaka 20 °C, vrijednost u 10:10 može se procijeniti kao vrijednost između te dvije poznate točke. [14]
U širem pristupu imputaciji ne moraju se koristiti samo neposredno susjedna mjerenja. Mogu se koristiti i povijesni podaci, primjerice vrijednosti iz prethodnih dana, mjeseci ili godina. Takvi podaci mogu pomoći u prepoznavanju ponavljajućih obrazaca, poput sličnih temperatura u istom dijelu dana ili u istom razdoblju godine. Razlika između imputacije i interpolacije može se jednostavno objasniti tako da je interpolacija popunjavanje vrijednosti između poznatih točaka, dok je imputacija širi pojam koji obuhvaća sve načine popunjavanja nedostajućih vrijednosti, uključujući metode strojnog učenja.

### Klasične metode imputacije i interpolacije


#### Forward fill

Forward fill koristi posljednje dostupno mjerenje kao zamjenu za svaku sljedeću prazninu u nizu. Ako temperatura u određenom trenutku nedostaje, vrijednost se prenosi iz zadnjeg poznatog uzorka sve dok se ne pojavi novo mjerenje. Upravo zbog tako jednostavnog pravila ova metoda je korisna kao početna referenca pri usporedbi složenijih postupaka. [5]
Slika - Prikaz forward fill metode. Izvor: vlastita izrada prema implementaciji projekta.
U praksi se forward fill najbolje ponaša kod vrlo kratkih prekida, kada se u nekoliko susjednih mjerenja ne očekuje veća promjena temperature. U takvoj situaciji prenošenje posljednje poznate vrijednosti može dati sasvim prihvatljivu procjenu bez dodatnog modeliranja podataka.
Problem se pojavljuje čim tijekom praznine postoji izraženiji rast ili pad temperature. Metoda tada nastavlja ponavljati staru vrijednost i ne prati promjenu koja se stvarno dogodila. Zbog toga se kod duljih blokova, prijelaza između dana i noći ili bržih temperaturnih promjena pogreška može brzo povećati.

#### Linearna i vremenska interpolacija

Linearna interpolacija određuje vrijednosti unutar praznine na temelju dviju najbližih poznatih točaka. Između njih pretpostavlja ravnomjernu promjenu, pa se svaka nedostajuća temperatura smješta na odgovarajuće mjesto duž pravca koji spaja poznata mjerenja. Takav pristup dobro odgovara dijelovima vremenskog niza u kojima nema naglih promjena. [6]
Slika - Prikaz linearne interpolacije. Izvor: vlastita izrada prema implementaciji projekta.
Ova je metoda jednostavna za primjenu i rezultat se može lako protumačiti jer izravno ovisi o poznatim vrijednostima s lijeve i desne strane praznine. Kod kraćih prekida u temperaturnom nizu, primjerice unutar nekoliko desetaka minuta, takva pretpostavka često je razumna jer se temperatura uglavnom mijenja postupno.
Kod duljih praznina ili naglih promjena pretpostavka ravnomjernog kretanja može postati previše pojednostavljena, pa linearna interpolacija više ne mora dobro pratiti stvarni oblik niza. Vremenska interpolacija polazi od iste ideje, ali položaj nedostajuće točke određuje prema stvarnom proteklom vremenu, a ne samo prema rednom broju uzorka. [6] To je važno kada mjerenja nisu jednako razmaknuta: procjena se tada prirodno približava onoj poznatoj vrijednosti kojoj je vremenski bliža. Ipak, i vremenska interpolacija pretpostavlja postupnu promjenu između poznatih točaka, pa joj dugi prekidi i nagle temperaturne promjene ostaju zahtjevni slučajevi.
Slika - Prikaz vremenske interpolacije. Izvor: vlastita izrada prema implementaciji projekta.

#### Kubna i spline interpolacija

Kubna interpolacija koristi polinom trećeg stupnja i zato između poznatih točaka ne mora stvarati ravnu liniju. Krivulja može pratiti blaže promjene nagiba, što je korisno kada se temperatura mijenja glatko, ali ne potpuno jednoliko. Kod kraćih i srednje dugih praznina takav oblik ponekad bolje opisuje lokalni tijek niza od linearne interpolacije. S druge strane, veća fleksibilnost znači i veću osjetljivost na raspored poznatih točaka, šum i rubove niza. U nepovoljnim slučajevima polinom može između mjerenja napraviti nerealno veliko odstupanje, osobito kada nedostaje dulji kontinuirani blok. [7]
Slika - Prikaz kubne interpolacije pomoću polinoma trećeg stupnja. Izvor: vlastita izrada prema implementaciji projekta.
Spline interpolacija vremenski niz promatra kroz više manjih intervala, pri čemu se na svakom od njih koristi lokalna polinomska funkcija. Prijelazi između tih dijelova određuju se tako da rekonstrukcija ostane glatka, pa se metoda ne oslanja na jedan polinom za cijeli promatrani raspon. Takav lokalni pristup može dobro pratiti postupne promjene temperature i dati prirodniji oblik krivulje od ravne interpolacije. Kada je praznina duga i unutar nje nema dovoljno poznatih točaka, prednost lokalnog modeliranja se smanjuje i procjena može znatno odstupiti od stvarnog niza. [8]
Slika - Prikaz spline interpolacije. Izvor: vlastita izrada prema implementaciji projekta.

#### Pomični prosjek

Pomični prosjek koristi skup okolnih poznatih mjerenja umjesto samo jedne susjedne vrijednosti. Za svaku prazninu odabire se prozor određene širine, a procjena se dobiva iz prosjeka dostupnih temperatura unutar tog prozora. Time se lokalne oscilacije ublažavaju, pa metoda daje zaglađeniju rekonstrukciju. [9]
Slika - Prikaz metode pomičnog prosjeka. Izvor: vlastita izrada prema implementaciji projekta.
Takvo zaglađivanje može biti korisno kada su susjedne temperature slične i kada se želi smanjiti utjecaj kratkotrajnog šuma. Istodobno se mogu izgubiti stvarni vrhovi i padovi signala, osobito ako se u blizini praznine dogodila brza promjena. Rezultat također snažno ovisi o širini prozora: premalen prozor daje nestabilniju procjenu, dok prevelik može previše izravnati temperaturni niz.
U završnom eksperimentu pomični prosjek uspoređen je zajedno s ostalim metodama, uz prozor od šest uzoraka s obje strane praznine, što pri desetominutnom razmaku odgovara jednom satu. Njegovo se ponašanje jasno razdvaja po scenarijima. Kod pojedinačno raspoređenih praznina daje osrednji rezultat jer zaglađivanje uklanja i stvarne promjene signala, a ne samo šum. U unutrašnjosti duljih blokova unutar prozora nema nijednog poznatog mjerenja, pa se metoda svodi na zadržavanje posljednje poznate vrijednosti i daje gotovo iste rezultate kao forward fill.

### Metode strojnog učenja za imputaciju podataka

Metode strojnog učenja u ovom radu koriste poznate dijelove temperaturnog niza kako bi procijenile vrijednosti koje su umjetno uklonjene. Za razliku od jednostavnih interpolacijskih metoda, one mogu istodobno koristiti više izvora informacija: vrijednosti na rubovima praznine i udaljenost do njih, položaj mjerenja u nizu te sat u danu i dan u godini. Opći postupak sastoji se od izdvajanja poznatih uzoraka, izračuna značajki, učenja odnosa između značajki i temperature te predikcije nedostajućih vrijednosti. Sve metode strojnog učenja u ovom radu uče odstupanje od linearne procjene umjesto same temperature, pa im je linearna interpolacija zajednička polazna točka koju pokušavaju popraviti.
Slika - Opći proces imputacije metodama strojnog učenja. Izvor: vlastita izrada prema implementaciji projekta.

#### KNN metoda

KNN (engl. k-nearest neighbors) procjenjuje nedostajuću temperaturu traženjem k poznatih uzoraka koji su joj najsličniji prema odabranim značajkama. U ovom radu sličnost se može temeljiti na položaju u nizu, satu u danu i danu u godini. Nakon odabira najbližih uzoraka njihove temperaturne vrijednosti koriste se za izračun procjene nedostajuće točke. [10]
Slika - Prikaz KNN metode za imputaciju nedostajuće temperature. Izvor: vlastita izrada prema implementaciji projekta.
KNN nema unaprijed zadan oblik funkcije kojom bi temperatura morala slijediti određeni trend, nego se oslanja na stvarne primjere iz skupa podataka. To mu omogućuje korištenje ponavljajućih vremenskih obrazaca, ali kvaliteta procjene izravno ovisi o tome jesu li značajke dobro odabrane i međusobno usporedive. Ako jedna značajka dominira zbog skale ili ako k nije dobro postavljen, među susjedima se mogu pronaći uzorci koji numerički izgledaju blizu, ali temperaturno nisu dovoljno slični.

#### Napredna KNN metoda

Napredna KNN varijanta mijenja ono što se uspoređuje. Umjesto da traži mjerenja obavljena u blizini nedostajuće točke, ona traži mjerenja koja su se nalazila u sličnoj situaciji. Situacija se opisuje relativnim položajem točke unutar praznine, udaljenostima do poznatih vrijednosti s njezine lijeve i desne strane te satom u danu prikazanim cikličkim komponentama. Ciklički prikaz posebno je važan za vrijeme. Primjerice, 23:00 i 00:00 nalaze se jedan sat jedno od drugoga, iako ih obične numeričke vrijednosti 23 i 0 prikazuju kao vrlo udaljene. Sinusna i kosinusna komponenta uklanjaju taj umjetni prekid i povezuju kraj ciklusa s njegovim početkom.
Slika - Prikaz sinusne i kosinusne komponente za cikličko vrijeme. Izvor: vlastita izrada prema implementaciji projekta.
Druga bitna razlika je u tome što napredna varijanta ne procjenjuje samu temperaturu, nego odstupanje od jednostavne linearne procjene. Time polazi od pretpostavke da je linearna procjena dobra osnova i pokušava naučiti u kojim se situacijama ona sustavno vara i za koliko. Pri završnom izračunu susjedi nemaju jednaku težinu: uzorci čija je situacija sličnija više utječu na rezultat, dok udaljeniji imaju manji doprinos.

**TABLICA 1**

| Element usporedbe | Osnovni KNN | Napredni KNN |
|---|---|---|
| Što se uspoređuje | blizina u samom nizu | sličnost situacije u kojoj je praznina |
| Ulazne veličine | položaj mjerenja u nizu | relativan položaj u praznini, udaljenost do oba ruba, sat u danu |
| Odabir susjeda | po jedan poznati susjed sa svake strane praznine | dvanaest poznatih točaka s najsličnijom situacijom |
| Što se procjenjuje | sama temperatura | odstupanje od linearne procjene |
| Težine susjeda | inverzna udaljenost u nizu | inverzna udaljenost u prostoru opisa situacije |
| Cilj | pouzdana lokalna procjena | popravak linearne procjene ondje gdje ona griješi |

Tablica - Usporedba osnovne i napredne KNN metode.

#### Decision Tree metoda

Decision Tree, odnosno stablo odlučivanja, gradi predikciju nizom uzastopnih podjela podataka. Svaki čvor provjerava jednu značajku i prag, primjerice pripada li mjerenje određenom dijelu dana ili godine, a uzorak se ovisno o rezultatu usmjerava u jednu od grana. U završnim listovima nalaze se vrijednosti koje se koriste za procjenu temperature. [11]
U implementaciji ovog rada stablo se uči na poznatim temperaturnim uzorcima i njihovim vremenskim značajkama. Za nedostajuću točku izračunaju se iste značajke, nakon čega ona prolazi kroz već izgrađena pravila sve do odgovarajućeg lista. Vrijednost tog lista postaje procjena temperature.
Slika - Dijagram rada Decision Tree metode. Izvor: vlastita izrada prema implementaciji projekta.
Stablo je relativno lako pratiti jer se put do predikcije može zapisati kao niz konkretnih odluka. Ta preglednost se smanjuje kada stablo postane vrlo duboko, a tada raste i opasnost da se model previše prilagodi podacima na kojima je treniran. U tom slučaju rezultat na poznatim uzorcima može biti dobar, dok se skrivene ili nove vrijednosti procjenjuju slabije.

#### Random Forest metoda

Random Forest ne oslanja se na jedno stablo, nego kombinira predikcije većeg broja stabala odlučivanja. [12] Svako stablo uči na nešto drugačijem uzorku poznatih podataka, pa njihove procjene nisu potpuno jednake. Konačna temperatura dobiva se prosjekom tih predikcija, čime se smanjuje utjecaj pogreške jednog pojedinačnog stabla.
Slika - Dijagram rada Random Forest metode. Izvor: vlastita izrada prema implementaciji projekta.
Za imputaciju temperature svako stablo koristi vremenske značajke kako bi procijenilo nedostajuću vrijednost, a konačan rezultat nastaje njihovim prosjekom. U odnosu na jedno stablo takav skup modela obično daje stabilnije procjene, osobito kada pojedina stabla reagiraju različito na šum ili specifične uzorke u podacima.
Cijena te stabilnosti je veća složenost. Potrebno je izgraditi i izvršiti više stabala, a konačnu predikciju teže je objasniti jednim jednostavnim pravilom jer nastaje kombinacijom više modela.

#### Neuronska mreža

Neuronska mreža procjenjuje temperaturu nizom težinskih zbrajanja ulaznih značajki i nelinearnih preslikavanja. Ulazne vrijednosti prolaze kroz jedan ili više skrivenih slojeva, u kojima svaki neuron računa težinski zbroj svojih ulaza i na njega primjenjuje nelinearnu funkciju, a izlazni sloj taj rezultat pretvara u konačnu procjenu. [15]
Za razliku od stabala odlučivanja, koja prostor značajki dijele pravokutnim rezovima, mreža može naučiti glatke i postupne prijelaze. To načelno odgovara temperaturi, koja se mijenja kontinuirano. Učenje se provodi postupnim smanjivanjem pogreške: mreža za poznate uzorke usporedi svoju procjenu sa stvarnom vrijednošću, propagacijom unatrag izračuna koliko je svaka težina pridonijela toj pogrešci i pomakne težine u smjeru koji pogrešku smanjuje.
Cijena te fleksibilnosti je potreba za većom količinom podataka i osjetljivost na postavke učenja, poput broja neurona, stope učenja i broja prolazaka kroz podatke. Mreža također ne nudi objašnjenje pojedinačne procjene, jer je ona posljedica velikog broja težina koje se ne mogu pročitati kao skup razumljivih pravila.

## REZULTATI

U ovom poglavlju prikazani su rezultati eksperimenata nad temperaturnim vremenskim nizom iz Jena Climate skupa podataka. Provedeno je ukupno 440 kombinacija, odnosno svih pet scenarija, osam missing rateova od 10 % do 80 % i jedanaest metoda imputacije. Svaka je kombinacija ponovljena nad 20 međusobno neovisnih tjednih prozora izdvojenih iz različitih dijelova godine, pa ukupan broj pojedinačnih izvođenja iznosi 8800. Cilj nije samo odrediti koja metoda ima najmanju pogrešku, nego pokazati u kojim uvjetima pojedine metode zadržavaju dobru rekonstrukciju, a u kojim uvjetima njihove pogreške rastu.
Rezultati iz datoteke experiment_results.csv analizirani su kroz MAE, RMSE i R². Za MAE i RMSE manje vrijednosti znače manju pogrešku rekonstrukcije, dok je kod R² poželjnija veća vrijednost. Svaka vrijednost u tablicama koje slijede prosjek je 20 ponavljanja, čime zaključci prestaju ovisiti o jednom slučajno odabranom tjednu i jednoj slučajnoj maski. Linearna interpolacija, vremenska interpolacija i KNN daju nad ovim nizom brojčano istovjetne rezultate, pa se pri određivanju najbolje metode navode zajedno kao izjednačene umjesto da se proizvoljno odabere jedna od njih. U glavnom dijelu rada zadržane su MAE tablice i sažetak najboljih metoda, a RMSE i R² prikazani su grafički kako bi usporedba ostala pregledna bez ponavljanja gotovo jednakih tablica.

**TABLICA 2**

| scenarij | pozicija | rate | najbolja metoda | MAE | RMSE | R² |
|---|---|---|---|---|---|---|
| random | none | 10 % | spline | 0,0721 | 0,1114 | 0,9990 |
| random | none | 20 % | spline | 0,0821 | 0,1321 | 0,9985 |
| random | none | 30 % | cubic | 0,0923 | 0,1511 | 0,9981 |
| random | none | 40 % | cubic | 0,1055 | 0,1745 | 0,9974 |
| random | none | 50 % | linear / time / knn | 0,1184 | 0,1850 | 0,9972 |
| random | none | 60 % | linear / time / knn | 0,1381 | 0,2257 | 0,9957 |
| random | none | 70 % | linear / time / knn | 0,1684 | 0,2747 | 0,9938 |
| random | none | 80 % | linear / time / knn | 0,2116 | 0,3424 | 0,9902 |
| block | none | 10 % | neural_net | 2,1311 | 2,5063 | -0,6337 |
| block | none | 20 % | neural_net | 2,5198 | 3,1131 | -0,3658 |
| block | none | 30 % | neural_net | 3,7507 | 4,4459 | -1,1276 |
| block | none | 40 % | random_forest | 2,8163 | 3,5018 | -0,6697 |
| block | none | 50 % | random_forest | 3,0882 | 3,8701 | -0,2135 |
| block | none | 60 % | neural_net | 3,7285 | 4,5471 | -0,7923 |
| block | none | 70 % | decision_tree | 3,7657 | 4,5868 | -1,1037 |
| block | none | 80 % | decision_tree | 3,5502 | 4,4147 | -0,5277 |
| block_start | start | 10 % | cubic | 2,0883 | 2,4984 | -0,4797 |
| block_start | start | 20 % | knn_upgraded | 2,7903 | 3,4767 | -0,4325 |
| block_start | start | 30 % | linear / time / knn | 3,1027 | 3,8831 | -0,4297 |
| block_start | start | 40 % | linear / time / knn | 3,1895 | 3,8872 | -0,5076 |
| block_start | start | 50 % | linear / time / knn | 3,0703 | 3,8144 | -0,2076 |
| block_start | start | 60 % | linear / time / knn | 3,5792 | 4,3585 | -0,5799 |
| block_start | start | 70 % | linear / time / knn | 3,9971 | 4,8378 | -1,0472 |
| block_start | start | 80 % | linear / time / knn | 3,6322 | 4,5405 | -0,5088 |
| block_middle | middle | 10 % | knn_upgraded | 2,4864 | 2,9165 | -0,7950 |
| block_middle | middle | 20 % | neural_net | 2,4173 | 3,0136 | -0,3261 |
| block_middle | middle | 30 % | decision_tree | 2,9535 | 3,6183 | -0,9175 |
| block_middle | middle | 40 % | neural_net | 3,3719 | 4,0516 | -1,0600 |
| block_middle | middle | 50 % | knn_upgraded | 3,2569 | 3,9244 | -0,4088 |
| block_middle | middle | 60 % | linear / time / knn | 3,2926 | 4,0603 | -0,4461 |
| block_middle | middle | 70 % | knn_upgraded | 3,9330 | 4,7945 | -1,0048 |
| block_middle | middle | 80 % | decision_tree | 3,6115 | 4,5303 | -0,4314 |
| block_end | end | 10 % | knn_upgraded | 2,2315 | 2,7191 | -0,5752 |
| block_end | end | 20 % | knn_upgraded | 2,5292 | 3,0747 | -0,3597 |
| block_end | end | 30 % | linear / time / knn | 2,6552 | 3,2323 | -0,6430 |
| block_end | end | 40 % | linear / time / knn | 2,8122 | 3,4494 | -0,3589 |
| block_end | end | 50 % | knn_upgraded | 2,9683 | 3,7025 | -0,4941 |
| block_end | end | 60 % | knn_upgraded | 3,1501 | 3,8980 | -0,5832 |
| block_end | end | 70 % | linear / time / knn | 3,1762 | 3,9139 | -0,2615 |
| block_end | end | 80 % | linear / time / knn | 3,2232 | 3,9508 | -0,2344 |

Tablica - Najbolja metoda po scenariju i missing rateu prema MAE metrici.
Iz Tablice 5-1 vidi se da nijedna metoda ne dominira kroz sve uvjete. Linearna interpolacija, zajedno s vremenskom interpolacijom i KNN-om, ima najmanji MAE u 15 od 40 kombinacija scenarija i missing ratea, ponajprije pri višim udjelima nedostajućih vrijednosti u random scenariju te u scenarijima block_start i block_end. Metode strojnog učenja najbolje su u 20 kombinacija, sve do jedne na kontinuiranim blokovima: napredni KNN u osam, neuronska mreža u šest, stablo odlučivanja u četiri i slučajna šuma u dvije. Kubnoj i spline interpolaciji pripada preostalih pet kombinacija, i to samo pri najnižim missing rateovima.

### Rezultati za random missing scenarij

U random missing scenariju uklonjene točke nisu povezane u jedan blok, nego su raspršene po vremenskom nizu. Zbog toga se oko većine praznina zadržavaju poznata mjerenja s obje strane, što interpolacijskim metodama daje povoljne uvjete za rekonstrukciju.
Spline interpolacija ima najmanji MAE pri 10 % i 20 % nedostajućih vrijednosti, s 0,0721 i 0,0821, a kubna interpolacija pri 30 % i 40 %, s 0,0923 i 0,1055. Od 50 % nadalje prvo mjesto preuzima linearna interpolacija, zajedno s vremenskom interpolacijom i KNN-om. Čak i pri 80 % ona zadržava MAE 0,2116, RMSE 0,3424 i R² 0,9902, pa se random scenarij pokazuje daleko manje zahtjevnim od scenarija s kontinuiranim blokovima.

**TABLICA 3**

| metoda | 10 % | 20 % | 30 % | 40 % | 50 % | 60 % | 70 % | 80 % |
|---|---|---|---|---|---|---|---|---|
| forward_fill | 0,1771 | 0,1903 | 0,2121 | 0,2453 | 0,2808 | 0,3343 | 0,4246 | 0,5769 |
| linear | 0,0802 | 0,0887 | 0,0960 | 0,1067 | 0,1184 | 0,1381 | 0,1684 | 0,2116 |
| time | 0,0802 | 0,0887 | 0,0960 | 0,1067 | 0,1184 | 0,1381 | 0,1684 | 0,2116 |
| cubic | 0,0721 | 0,0821 | 0,0923 | 0,1055 | 0,1219 | 0,1466 | 0,1812 | 0,2356 |
| spline | 0,0721 | 0,0821 | 0,0923 | 0,1055 | 0,1220 | 0,1466 | 0,1812 | 0,2357 |
| moving_average | 0,1941 | 0,1990 | 0,2080 | 0,2199 | 0,2342 | 0,2549 | 0,2955 | 0,3761 |
| knn | 0,0802 | 0,0887 | 0,0960 | 0,1067 | 0,1184 | 0,1381 | 0,1684 | 0,2116 |
| knn_upgraded | 0,0871 | 0,0993 | 0,1109 | 0,1264 | 0,1479 | 0,1673 | 0,1907 | 0,2272 |
| decision_tree | 0,0857 | 0,0974 | 0,1044 | 0,1188 | 0,1352 | 0,1642 | 0,2007 | 0,2666 |
| random_forest | 0,0796 | 0,0892 | 0,0969 | 0,1079 | 0,1202 | 0,1403 | 0,1714 | 0,2193 |
| neural_net | 0,0913 | 0,1019 | 0,1109 | 0,1326 | 0,1504 | 0,1835 | 0,2274 | 0,2964 |

Tablica - MAE vrijednosti za scenarij random missing pri missing rateovima od 10 % do 80 %.
Slika - Pregled MAE vrijednosti po metodama za scenarij random missing.
Usporedba MAE-a po metodama pokazuje jasnu prednost interpolacijskih postupaka u random scenariju. Linearna interpolacija ima najmanju pogrešku u četiri od osam promatranih missing rateova, dok se pri nižim rateovima ističu kubna i spline interpolacija. Metode strojnog učenja drže se vrlo blizu, ali nijedna od njih ne preuzima prvo mjesto.
Pri najvećem testiranom udjelu od 80 % razlika među metodama i dalje je velika: linear završava na MAE 0,2116, dok forward_fill doseže 0,5769.
Slika - Promjena MAE vrijednosti kroz missing rateove za scenarij random missing.
S porastom missing ratea prosječni MAE svih metoda raste s 0,1000 pri 10 % na 0,2790 pri 80 %. Unatoč tom rastu, linearna interpolacija pri 80 % ostaje na samo 0,2116, što potvrđuje da pojedinačno raspoređene praznine i dalje ostavljaju dovoljno lokalnih informacija za dobru rekonstrukciju.
Slika - Promjena RMSE vrijednosti kroz missing rateove za scenarij random missing.
RMSE slijedi isti opći smjer kao MAE, ali jače kažnjava veća pojedinačna odstupanja. Prosjek svih metoda raste s 0,1498 na 0,4487 između 10 % i 80 % missing ratea, dok linearna interpolacija pri 80 % ostvaruje RMSE 0,3424.
Slika - Promjena R² vrijednosti kroz missing rateove za scenarij random missing.
R² u random scenariju ostaje vrlo visok za najbolje metode i pri velikom broju uklonjenih vrijednosti. Prosjek svih metoda smanjuje se s 0,9979 pri 10 % na 0,9816 pri 80 %, a linearna interpolacija na 80 % postiže 0,9902. To znači da njezina rekonstrukcija i dalje vrlo dobro prati oblik originalnog temperaturnog niza.

### Rezultati za block missing scenarij

Kod block missing scenarija uklanja se jedan kontinuirani dio niza. Unutar takve praznine nema poznatih mjerenja, pa se metode moraju oslanjati na rubove bloka ili na obrasce naučene iz ostatka podataka. Zbog toga je ovaj slučaj zahtjevniji od random missing scenarija.
Prvo mjesto u ovom scenariju pripada isključivo metodama strojnog učenja. Neuronska mreža najbolja je pri 10 %, 20 %, 30 % i 60 %, slučajna šuma pri 40 % i 50 %, a stablo odlučivanja pri 70 % i 80 %. Prednost je pritom vrlo mala: pri 10 % neuronska mreža ostvaruje MAE 2,1311 naspram 2,1669 linearne interpolacije. Na 80 % linearna interpolacija završava s MAE 3,5617, RMSE 4,4259 i R² -0,5369.

**TABLICA 4**

| metoda | 10 % | 20 % | 30 % | 40 % | 50 % | 60 % | 70 % | 80 % |
|---|---|---|---|---|---|---|---|---|
| forward_fill | 3,4311 | 3,2575 | 4,7738 | 4,0476 | 4,0175 | 5,7158 | 4,2738 | 5,0784 |
| linear | 2,1669 | 2,5336 | 3,7564 | 2,8349 | 3,0897 | 3,7336 | 3,7852 | 3,5617 |
| time | 2,1669 | 2,5336 | 3,7564 | 2,8349 | 3,0897 | 3,7336 | 3,7852 | 3,5617 |
| cubic | 2,2159 | 6,7633 | 9,1979 | 11,4708 | 12,4437 | 21,3524 | 16,9042 | 29,3598 |
| spline | 2,2159 | 6,7633 | 9,1979 | 11,4708 | 12,4437 | 21,3970 | 16,9042 | 29,4213 |
| moving_average | 3,1873 | 3,1532 | 4,6951 | 3,9736 | 3,9649 | 5,6654 | 4,2395 | 5,0404 |
| knn | 2,1669 | 2,5336 | 3,7564 | 2,8349 | 3,0897 | 3,7336 | 3,7852 | 3,5617 |
| knn_upgraded | 2,1504 | 2,5281 | 3,7551 | 2,8223 | 3,0903 | 3,7346 | 3,7799 | 3,5544 |
| decision_tree | 2,1369 | 2,5355 | 3,7704 | 2,8276 | 3,0915 | 3,7402 | 3,7657 | 3,5502 |
| random_forest | 2,1507 | 2,5299 | 3,7656 | 2,8163 | 3,0882 | 3,7481 | 3,7718 | 3,5510 |
| neural_net | 2,1311 | 2,5198 | 3,7507 | 2,8297 | 3,0885 | 3,7285 | 3,7822 | 3,5561 |

Tablica - MAE vrijednosti za scenarij block missing pri missing rateovima od 10 % do 80 %.
Slika - Pregled MAE vrijednosti po metodama za scenarij block missing.
Kod kontinuiranog bloka razlike među metodama postaju izraženije nego u random scenariju, ali se sve upotrebljive metode grupiraju vrlo blizu jedna drugoj. Linearna interpolacija i četiri metode strojnog učenja na 80 % razlikuju se za manje od 0,02 °C, dok kubna interpolacija u istoj postavci doseže 29,3598.
Slika - Promjena MAE vrijednosti kroz missing rateove za scenarij block missing.
Prosječni MAE svih metoda raste s 2,3746 pri 10 % na 8,5270 pri 80 %. Takav porast pokazuje koliko kontinuirana praznina smanjuje količinu lokalnih informacija dostupnih za rekonstrukciju, ali i koliko na prosjek utječu metode koje se na blokovima raspadaju. Najbolja metoda na 80 % je stablo odlučivanja s MAE 3,5502.
Slika - Promjena RMSE vrijednosti kroz missing rateove za scenarij block missing.
Kod RMSE-a razlika se dodatno povećava jer ova metrika snažnije reagira na veća odstupanja. Prosječna vrijednost raste s 2,8159 na 10,0162, dok linearna interpolacija pri 80 % zadržava RMSE 4,4259.
Slika - Promjena R² vrijednosti kroz missing rateove za scenarij block missing.
Za R² se ne dobiva jednoličan trend kao kod MAE-a i RMSE-a. Prosjek pada s -1,2378 pri 10 % na -33,9368 pri 80 %, no taj pad gotovo u cijelosti proizlazi iz kubne i spline interpolacije. Najbolja pojedinačna metoda pri 80 % je stablo odlučivanja s R² -0,5277, što pokazuje da prosjek snažno snižavaju slabije metode.

### Rezultati za block_start, block_middle i block_end scenarije

Tri dodatna block scenarija razlikuju se samo po položaju uklonjenog kontinuiranog dijela: na početku, u sredini ili na kraju niza. Usporedba tih slučajeva omogućuje provjeru koliko dostupnost poznatih mjerenja prije i poslije praznine utječe na rezultat.

#### Block_start

U block_start scenariju nedostajući dio nalazi se na početku niza, pa metode nemaju poznate vrijednosti prije praznine. Rezultati pri nižim rateovima nisu jednolični: na 10 % najmanji MAE ima kubna interpolacija s 2,0883, a na 20 % napredni KNN s 2,7903. Od 30 % do 80 % najbolja je linearna interpolacija, koja pri 80 % ostvaruje MAE 3,6322, RMSE 4,5405 i R² -0,5088.

**TABLICA 5**

| metoda | 10 % | 20 % | 30 % | 40 % | 50 % | 60 % | 70 % | 80 % |
|---|---|---|---|---|---|---|---|---|
| forward_fill | 3,2454 | 3,4633 | 3,8785 | 4,2018 | 4,4899 | 4,5089 | 4,5190 | 4,5077 |
| linear | 2,1935 | 2,8362 | 3,1027 | 3,1895 | 3,0703 | 3,5792 | 3,9971 | 3,6322 |
| time | 2,1935 | 2,8362 | 3,1027 | 3,1895 | 3,0703 | 3,5792 | 3,9971 | 3,6322 |
| cubic | 2,0883 | 4,6230 | 5,2982 | 7,7071 | 7,0279 | 11,3422 | 9,5612 | 10,8286 |
| spline | 2,3357 | 5,6963 | 6,9550 | 10,7131 | 10,0062 | 15,8351 | 13,3992 | 15,0115 |
| moving_average | 3,0268 | 3,3169 | 3,8130 | 4,1368 | 4,4217 | 4,4693 | 4,4992 | 4,4819 |
| knn | 2,1935 | 2,8362 | 3,1027 | 3,1895 | 3,0703 | 3,5792 | 3,9971 | 3,6322 |
| knn_upgraded | 2,1801 | 2,7903 | 3,1379 | 3,2904 | 3,1737 | 3,6654 | 4,0605 | 3,7887 |
| decision_tree | 2,4108 | 3,0008 | 3,3207 | 3,4974 | 3,3272 | 3,8827 | 4,1595 | 3,9284 |
| random_forest | 2,2469 | 2,8921 | 3,2191 | 3,3091 | 3,1894 | 3,7472 | 4,0886 | 3,8540 |
| neural_net | 2,2066 | 2,9052 | 3,1169 | 3,2257 | 3,0949 | 3,6427 | 4,0425 | 3,6481 |

Tablica - MAE vrijednosti za scenarij block_start pri missing rateovima od 10 % do 80 %.
Slika - Pregled MAE vrijednosti po metodama za scenarij block_start.
Raspored MAE vrijednosti u block_start scenariju pokazuje da linearna interpolacija pobjeđuje u šest od osam rateova. Pri 80 % razlika prema slabijim metodama posebno je vidljiva: linear ima MAE 3,6322, dok spline interpolacija završava na 15,0115.
Slika - Promjena MAE vrijednosti kroz missing rateove za scenarij block_start.
Prosječni MAE u ovom scenariju ne raste potpuno pravilno s missing rateom, ali se ukupno povećava s 2,3928 pri 10 % na 5,5405 pri 80 %. Na najvišem rateu linearna interpolacija ostaje najbolja s vrijednošću 3,6322.
Slika - Promjena RMSE vrijednosti kroz missing rateove za scenarij block_start.
Sličan obrazac vidi se i kod RMSE-a. Prosjek svih metoda iznosi 2,8145 pri 10 % i 6,6268 pri 80 %, dok linearna interpolacija na 80 % postiže znatno nižih 4,5405.
Slika - Promjena R² vrijednosti kroz missing rateove za scenarij block_start.
R² dodatno pokazuje nestabilnost pojedinih metoda na rubnom bloku. Prosječna vrijednost mijenja se s -0,7416 pri 10 % na -5,2812 pri 80 %, pa prosjek nije dobar pokazatelj ponašanja najbolje metode. Linearna interpolacija na 80 % ostvaruje R² -0,5088.

#### Block_middle

Block_middle uklanja kontinuirani dio iz sredine niza. Za razliku od rubnih scenarija, ovdje su poznata mjerenja dostupna i prije i poslije praznine, što linearnim i vremenskim interpolacijama daje jasniju osnovu za procjenu.
Pri 10 % i 50 % najmanji MAE ima napredni KNN, s 2,4864 i 3,2569, pri 20 % i 40 % neuronska mreža, s 2,4173 i 3,3719, a pri 30 % i 80 % stablo odlučivanja, s 2,9535 i 3,6115. Napredni KNN najbolji je i pri 70 %. Linearna interpolacija prvo mjesto zauzima jedino pri 60 %, s 3,2926, a na 80 % ostvaruje MAE 3,6322 i RMSE 4,5532.

**TABLICA 6**

| metoda | 10 % | 20 % | 30 % | 40 % | 50 % | 60 % | 70 % | 80 % |
|---|---|---|---|---|---|---|---|---|
| forward_fill | 3,3713 | 3,6248 | 4,4178 | 3,4973 | 4,1161 | 4,0337 | 4,3486 | 5,5145 |
| linear | 2,4936 | 2,4287 | 2,9642 | 3,3800 | 3,2633 | 3,2926 | 3,9484 | 3,6322 |
| time | 2,4936 | 2,4287 | 2,9642 | 3,3800 | 3,2633 | 3,2926 | 3,9484 | 3,6322 |
| cubic | 2,8902 | 7,0993 | 7,5157 | 9,2167 | 13,4306 | 11,0021 | 19,5858 | 24,9233 |
| spline | 2,8902 | 7,0993 | 7,5157 | 9,2167 | 13,4306 | 11,0021 | 19,5858 | 24,9233 |
| moving_average | 3,1420 | 3,5030 | 4,3349 | 3,4675 | 4,0500 | 3,9999 | 4,3156 | 5,4578 |
| knn | 2,4936 | 2,4287 | 2,9642 | 3,3800 | 3,2633 | 3,2926 | 3,9484 | 3,6322 |
| knn_upgraded | 2,4864 | 2,4231 | 2,9657 | 3,3730 | 3,2569 | 3,2985 | 3,9330 | 3,6241 |
| decision_tree | 2,5238 | 2,4272 | 2,9535 | 3,3739 | 3,2622 | 3,2947 | 3,9613 | 3,6115 |
| random_forest | 2,4939 | 2,4256 | 2,9625 | 3,3784 | 3,2658 | 3,3012 | 3,9432 | 3,6163 |
| neural_net | 2,4911 | 2,4173 | 2,9640 | 3,3719 | 3,2800 | 3,3139 | 3,9508 | 3,6280 |

Tablica - MAE vrijednosti za scenarij block_middle pri missing rateovima od 10 % do 80 %.
Slika - Pregled MAE vrijednosti po metodama za scenarij block_middle.
U sedam od osam postavki block_middle scenarija najmanji MAE postiže neka od metoda strojnog učenja, no njihova prednost pred linearnom interpolacijom nigdje ne prelazi 0,03 °C. Pri 80 % pogreška linearne interpolacije iznosi 3,6322, dok kubna u istom slučaju raste na 24,9233.
Slika - Promjena MAE vrijednosti kroz missing rateove za scenarij block_middle.
Povećanjem količine uklonjenih podataka prosječni MAE svih metoda raste s 2,7063 pri 10 % na 7,8359 pri 80 %. Linearna interpolacija na 80 % s MAE 3,6322 ostaje blizu najboljeg rezultata, ali je i taj rezultat osjetno slabiji nego u random scenariju.
Slika - Promjena RMSE vrijednosti kroz missing rateove za scenarij block_middle.
RMSE potvrđuje isti problem s velikim središnjim blokom: prosjek raste s 3,1729 na 9,2519. Linearna interpolacija na 80 % ostvaruje RMSE 4,5532.
Slika - Promjena R² vrijednosti kroz missing rateove za scenarij block_middle.
Prosječni R² u block_middle scenariju ostaje negativan kroz promatrane krajnje točke i mijenja se s -1,7596 pri 10 % na -14,8726 pri 80 %. Linearna interpolacija je pri 80 % znatno bolja od prosjeka, ali R² -0,4499 pokazuje da je rekonstrukcija velikog središnjeg bloka i dalje zahtjevna.

#### Block_end

U block_end scenariju kontinuirana praznina nalazi se na kraju niza. Što je missing rate veći, to veći dio završnog ponašanja temperature treba procijeniti bez ijednog poznatog mjerenja nakon praznine, pa ovaj položaj postaje posebno nepovoljan.
Najbolja metoda izmjenjuje se između dva pristupa: napredni KNN pobjeđuje pri 10 %, 20 %, 50 % i 60 %, a linearna interpolacija pri 30 %, 40 %, 70 % i 80 %. Pri 80 % prosječni MAE svih metoda doseže 5,9575.

**TABLICA 7**

| metoda | 10 % | 20 % | 30 % | 40 % | 50 % | 60 % | 70 % | 80 % |
|---|---|---|---|---|---|---|---|---|
| forward_fill | 3,5266 | 3,0373 | 2,9232 | 3,2711 | 4,7663 | 4,8022 | 3,5122 | 4,3384 |
| linear | 2,2360 | 2,5602 | 2,6552 | 2,8122 | 3,0938 | 3,2528 | 3,1762 | 3,2232 |
| time | 2,2360 | 2,5602 | 2,6552 | 2,8122 | 3,0938 | 3,2528 | 3,1762 | 3,2232 |
| cubic | 2,8200 | 4,3268 | 4,9419 | 7,4638 | 7,8997 | 10,0488 | 23,8038 | 14,0329 |
| spline | 3,3231 | 5,6416 | 6,5507 | 10,2407 | 10,7038 | 14,6728 | 35,0891 | 19,9462 |
| moving_average | 3,3288 | 2,9462 | 2,8771 | 3,2289 | 4,7041 | 4,7516 | 3,4882 | 4,3037 |
| knn | 2,2360 | 2,5602 | 2,6552 | 2,8122 | 3,0938 | 3,2528 | 3,1762 | 3,2232 |
| knn_upgraded | 2,2315 | 2,5292 | 2,6745 | 2,8247 | 2,9683 | 3,1501 | 3,2731 | 3,2579 |
| decision_tree | 2,3154 | 2,7030 | 2,7768 | 2,9264 | 3,1401 | 3,2171 | 3,3991 | 3,4093 |
| random_forest | 2,2696 | 2,6628 | 2,7065 | 2,8842 | 3,0636 | 3,1812 | 3,3540 | 3,2577 |
| neural_net | 2,2468 | 2,6860 | 2,7204 | 2,8351 | 3,1202 | 3,2511 | 3,2612 | 3,3167 |

Tablica - MAE vrijednosti za scenarij block_end pri missing rateovima od 10 % do 80 %.
Slika - Pregled MAE vrijednosti po metodama za scenarij block_end.
Kod block_end scenarija nema jedne metode koja dominira kroz cijeli raspon; linearna interpolacija i napredni KNN dijele pobjede po četiri. Na 80 % MAE linearne interpolacije iznosi 3,2232, dok spline raste na 19,9462.
Slika - Promjena MAE vrijednosti kroz missing rateove za scenarij block_end.
Prosječni MAE se s 2,6155 pri 10 % povećava na 5,9575 pri 80 %. Linearna interpolacija i u tom slučaju ostaje najbolja s MAE 3,2232.
Slika - Promjena RMSE vrijednosti kroz missing rateove za scenarij block_end.
RMSE pokazuje još izraženiji rast pogreške na završnom bloku: prosjek ide s 3,1141 pri 10 % na 7,0167 pri 80 %. Linearna interpolacija na 80 % postiže RMSE 3,9508, znatno manje od prosjeka ostalih metoda.
Slika - Promjena R² vrijednosti kroz missing rateove za scenarij block_end.
Kod R² se prosječna vrijednost s povećanjem ratea snažno pogoršava: od -1,2259 pri 10 % do -27,4797 pri 80 %. Čak i najbolja metoda na 80 %, linearna interpolacija, ima R² -0,2344, što potvrđuje da je završni blok te veličine vrlo teško rekonstruirati.

### Utjecaj missing ratea na pogrešku

Kada se svi scenariji promatraju zajedno, veći missing rate uglavnom znači i veću pogrešku. Prosječni MAE raste s 2,0378 pri 10 % na 5,6280 pri 80 %, a prosječni RMSE s 2,4134 na 6,6721. Najmanji utjecaj povećanja ratea vidi se u random scenariju, gdje oko uklonjenih točaka često ostaju poznata mjerenja. Kontinuirani blokovi puno su osjetljiviji: na 80 % prosječni MAE iznosi 8,5270 za block i 7,8359 za block_middle. R² ne prati missing rate tako pravilno kao MAE i RMSE jer njegova vrijednost ovisi i o varijabilnosti stvarnih temperatura na maskiranim pozicijama. Negativni rezultati zato su česti u block scenarijima, osobito za forward fill, pomični prosjek te kubnu i spline interpolaciju. Od ukupno 440 kombinacija, 352 ima R² manji od nule.

### Vizualna rekonstrukcija vremenskog niza

Rekonstrukcijski prikazi služe za vizualnu provjeru onoga što se vidi u numeričkim metrikama. Originalni temperaturni niz uspoređen je s rekonstrukcijom, a maskirane pozicije označene su crvenim točkama. Prikazana je linearna interpolacija pri 20 % missing ratea za svih pet scenarija jer je ta metoda kroz cijeli eksperiment bila najstabilnija. Svi prikazi odnose se na prvi od 20 tjednih prozora, pa metrike navedene uz njih opisuju taj konkretni tjedan i očekivano odstupaju od prosjeka u tablicama.
Slika - Vizualna rekonstrukcija linearnom interpolacijom za scenarij random missing pri 20 % missing ratea.
U random missing scenariju uklonjene točke raspršene su po cijelom nizu, pa linearna interpolacija za većinu njih ima poznata mjerenja s obje strane. Na prikazu se zato rekonstruirana linija može usporediti s originalom upravo na pojedinačnim označenim pozicijama. Dobivene metrike potvrđuju vrlo dobru rekonstrukciju: MAE iznosi 0,0730, RMSE 0,1185, a R² 0,9996.
Slika - Vizualna rekonstrukcija linearnom interpolacijom za scenarij block missing pri 20 % missing ratea.
Kod običnog block scenarija maskirane točke čine jednu kontinuiranu prazninu. Linearna interpolacija tada mora povezati poznate vrijednosti na rubovima bloka, pa je zadatak osjetno zahtjevniji nego kod pojedinačnih random praznina.
Pri 20 % missing ratea dobiveni su MAE 1,4765, RMSE 1,6968 i R² -2,6787. Rekonstrukcija i dalje prati glavni tijek niza, ali je odstupanje primjetno veće nego u random scenariju.
Slika - Vizualna rekonstrukcija linearnom interpolacijom za scenarij block_start pri 20 % missing ratea.
U block_start scenariju nedostaje početni dio niza, što znači da linearna interpolacija nema poznatu vrijednost s lijeve strane praznine. Vizualni prikaz zato predstavlja rubni slučaj u kojem metoda raspolaže informacijama uglavnom iz dijela niza nakon bloka.
Metrike za taj slučaj iznose: MAE 0,6991, RMSE 0,8889, a R² 0,7639. Pozitivan R² pokazuje da rekonstrukcija na uklonjenom početnom dijelu u ovom tjednu ipak prati stvarne vrijednosti, iako je pogreška veća nego u random scenariju.
Slika - Vizualna rekonstrukcija linearnom interpolacijom za scenarij block_middle pri 20 % missing ratea.
Kod block_middle scenarija praznina je smještena između poznatih dijelova niza, pa postoje rubne vrijednosti i prije i poslije bloka. Ipak, duljina kontinuirane praznine i dalje može dovesti do značajnog odstupanja unutar njezina središta. Za prikazani slučaj MAE iznosi 1,1449, RMSE 1,2988 i R² -2,6120. Negativan R² pokazuje da rekonstruirane promjene na maskiranim točkama ne prate dovoljno dobro stvarnu varijabilnost.
Slika - Vizualna rekonstrukcija linearnom interpolacijom za scenarij block_end pri 20 % missing ratea.
U block_end scenariju uklonjen je završni dio vremenskog niza, pa nakon praznine nema poznatih mjerenja koja bi ograničila rekonstrukciju s desne strane. Time se jasno vidi razlika između interpolacije unutar niza i procjene na njegovu rubu. Pri 20 % missing ratea linearna interpolacija ostvaruje MAE 5,5318, RMSE 6,6875 i R² -0,6479. Od svih pet prikaza ovo je najslabiji rezultat, jer se bez desnog ruba posljednja poznata vrijednost produljuje kroz cijeli uklonjeni dio.

### Najbolja metoda po scenariju

Ako se kao kriterij uzme broj najboljih MAE rezultata, linearna interpolacija vodi s 15 pobjeda u 40 kombinacija, no te pobjede dijeli s vremenskom interpolacijom i KNN-om jer sve tri metode daju brojčano istovjetne vrijednosti. Time_interpolation i linear_interpolation podudaraju se zato što su mjerenja u korištenom Jena nizu raspoređena u pravilnim razmacima od 10 minuta, a KNN im se pridružuje jer u konačnoj izvedbi obuhvaća prazninu s obje strane i teži po inverznoj udaljenosti. Metode strojnog učenja zajedno imaju 20 pobjeda, sve odreda na kontinuiranim blokovima, pri čemu prednjači napredni KNN s osam. Kubna i spline interpolacija najbolje su samo pri najnižim rateovima u random scenariju te pri 10 % u block_start scenariju, a na duljim blokovima im pogreška naglo raste jer polinom trećeg stupnja izvan poznatih točaka divergira. Zbog izjednačenosti prve tri metode zbroj pobjeda po recima Tablice 5-7 veći je od 40.

**TABLICA 8**

| metoda | prosječni MAE | prosječni RMSE | prosječni R² | std MAE | pobjede po MAE |
|---|---|---|---|---|---|
| linear | 2,5121 | 3,0835 | -0,2785 | 1,2775 | 15 |
| time | 2,5121 | 3,0835 | -0,2785 | 1,2775 | 15 |
| knn | 2,5121 | 3,0835 | -0,2785 | 1,2775 | 15 |
| knn_upgraded | 2,5232 | 3,0950 | -0,2723 | 1,2793 | 8 |
| neural_net | 2,5354 | 3,1142 | -0,2935 | 1,2723 | 6 |
| random_forest | 2,5440 | 3,1107 | -0,2846 | 1,2950 | 2 |
| decision_tree | 2,5853 | 3,1533 | -0,3079 | 1,3063 | 4 |
| moving_average | 3,2492 | 3,8783 | -1,0181 | 1,6330 | 0 |
| forward_fill | 3,3238 | 3,9482 | -1,0765 | 1,6315 | 0 |
| cubic | 8,5056 | 10,0054 | -28,1000 | 7,3684 | 3 |
| spline | 9,8159 | 11,3137 | -38,2037 | 8,3513 | 2 |

Tablica - Sažetak rezultata po metodama kroz svih 40 kombinacija scenarija i missing ratea.

## TUMAČENJE REZULTATA

Tumačenje rezultata povezuje dobivene numeričke vrijednosti s načinom rada pojedinih metoda. Posebno je važno naglasiti da složenija metoda ne mora automatski biti bolja. Kod pravilno uzorkovanog temperaturnog niza jednostavne interpolacijske metode često dobro koriste lokalni vremenski redoslijed i poznate vrijednosti oko praznine.

### Usporedba klasičnih i metoda strojnog učenja

Rezultati pokazuju da su linearna interpolacija i metode strojnog učenja u ovom eksperimentu vrlo blizu jedne drugima. Linearna i vremenska interpolacija imaju najniži prosječni MAE od 2,5121 i standardnu devijaciju MAE od 1,2775, a odmah iza njih slijede napredni KNN s 2,5232, neuronska mreža s 2,5354, slučajna šuma s 2,5440 i stablo odlučivanja s 2,5853. Razlika između prvog i petog mjesta iznosi manje od 0,08 °C, pa se nijedna od tih metoda ne može proglasiti uvjerljivo boljom. Jasno zaostaju samo pomični prosjek i forward fill, s 3,2492 i 3,3238, te kubna i spline interpolacija, koje s 8,5056 i 9,8159 na duljim blokovima potpuno gube stabilnost. Da metode strojnog učenja ne ostvaruju veću prednost može se objasniti pravilnim 10-minutnim uzorkovanjem, u kojem susjedne vrijednosti već sadrže gotovo svu informaciju potrebnu za rekonstrukciju.

### Ponašanje metoda kod random missing scenarija

Random missing scenarij najpovoljniji je za interpolacijske metode jer su uklonjene vrijednosti pojedinačno raspoređene kroz niz. Spline i kubna interpolacija postižu najbolji MAE pri 10 % do 40 %, s vrijednostima od 0,0721 do 0,1055. Od 50 % do 80 % najbolja postaje linearna interpolacija, ali i tada pogreške ostaju vrlo male. Na random scenariju R² za najbolje metode ostaje iznad 0,99 i pri 80 % missing ratea. To znači da rekonstruirane vrijednosti i dalje dobro prate promjene originalnog temperaturnog niza, iako je većina vrijednosti umjetno uklonjena.

### Ponašanje metoda kod block missing scenarija

Block missing scenariji stvaraju teži problem jer unutar uklonjenog bloka nema poznatih vrijednosti. Linearna interpolacija ondje daje solidan rezultat jer izravno povezuje poznate vrijednosti na rubovima bloka, ali je metode strojnog učenja u običnom block scenariju nadmašuju u svih osam rateova. Prednost je pritom sitna i na 80 % iznosi 0,0115 °C, što nije dovoljno da bi se govorilo o praktično značajnoj razlici. Znatno je važnije koje metode ondje potpuno zakažu: kubna i spline interpolacija na 80 % dosežu MAE od približno 29 °C jer polinom trećeg stupnja izvan poznatih točaka divergira, dok forward fill i pomični prosjek ostaju oko 5 °C jer unutar bloka nemaju nijednog poznatog susjeda i svode se na zadržavanje posljednje vrijednosti.

### Ponašanje metoda kod block_start, block_middle i block_end scenarija

Pozicija bloka značajno utječe na rezultate. Block_start i block_end scenariji imaju problem jer se blok nalazi na rubu niza, pa metode nemaju poznate vrijednosti s obje strane praznine. Block_middle je povoljniji za interpolaciju pri nižim rateovima jer su poznate vrijednosti dostupne prije i poslije bloka. Pri 80 % missing ratea najveći prosječni MAE ima obični block scenarij, 8,5270, a odmah iza njega block_middle s 7,8359. Ti prosjeci ipak više govore o metodama koje se raspadaju nego o težini samog scenarija, jer se najbolje metode u sva tri block scenarija na 80 % zadržavaju između 3,2 i 3,7 °C.

### Prednosti i ograničenja KNN metode

U završnom eksperimentu obje su KNN izvedbe zasebno vrednovane. Osnovni KNN, registriran kao knn, traži poznate susjede s obje strane praznine i teži ih po inverznoj udaljenosti, zbog čega daje brojčano iste vrijednosti kao linearna interpolacija. Napredni KNN, registriran kao knn_upgraded, ne uspoređuje uzorke po položaju nego po obilježjima same praznine, primjerice po relativnom položaju unutar nje i udaljenosti do poznatih rubova, te uči odstupanje od linearne procjene. Takav pristup daje mu prednost upravo ondje gdje osnovni KNN nema što dodati: napredni KNN najbolja je metoda u osam od 40 kombinacija, sve na kontinuiranim blokovima, s prosječnim MAE 2,5232 naspram 2,5121 osnovne izvedbe. Razlika je premala da bi se jedna izvedba mogla proglasiti boljom, ali pokazuje da dodatne značajke pomažu točno u onim uvjetima u kojima linearna procjena nema dovoljno oslonca.

### Prednosti i ograničenja Decision Tree i Random Forest metode

Decision Tree i Random Forest mogu naučiti nelinearne odnose između ulaznih značajki i temperature. U pojedinim slučajevima ostvaruju najbolji rezultat, primjerice stablo odlučivanja u block scenariju pri 70 % i 80 % te slučajna šuma u istom scenariju pri 40 % i 50 %. Prosječni MAE za stablo odlučivanja iznosi 2,5853, a za slučajnu šumu 2,5440, što ih smješta unutar 0,08 °C od linearne interpolacije. Obje su metode dakle konkurentne, ali ni jedna ne donosi prednost koja bi opravdala njihovu složenost na ovako pravilno uzorkovanom nizu. Njihova stvarna vrijednost pokazuje se tek na kontinuiranim blokovima, gdje linearna procjena nema dovoljno oslonca.

### Ograničenja rada

Glavno ograničenje rada je korištenje jedne meteorološke varijable iz Jena Climate skupa podataka. Eksperiment se provodi nad 20 tjednih prozora od po 1008 zapisa, odnosno sedam dana mjerenja u 10-minutnim intervalima, raspoređenih kroz godinu radi sezonske pokrivenosti. Zaključci se stoga odnose na temperaturu pravilno uzorkovanu u kratkim intervalima i ne moraju vrijediti za nizove s nepravilnim razmacima ili duljim razdobljima. Nedostajuće vrijednosti su umjetno generirane, što omogućuje objektivnu evaluaciju jer su stvarne vrijednosti poznate, ali ne obuhvaća sve moguće uzroke i oblike stvarnih nedostajućih podataka. Naposljetku, razlike među pet najboljih metoda manje su od 0,08 °C, pa poredak među njima treba uzimati s oprezom bez formalne provjere statističke značajnosti.

### Uloga metoda strojnog učenja

Iako jednostavna linearna interpolacija ostaje ukupno najbolja, razlika prema metodama strojnog učenja svela se na nekoliko stotinki stupnja, a na kontinuiranim blokovima prednost prelazi na stranu strojnog učenja. Njihova je prednost u tome što mogu koristiti više ulaznih značajki, primjerice sat u danu, dan u godini, položaj mjerenja u nizu te udaljenost do poznatih vrijednosti s obje strane praznine, i na temelju njih učiti odstupanje od jednostavne linearne procjene. Takav pristup može biti korisniji kod većih i raznolikijih skupova podataka, nepravilnih vremenskih razmaka ili situacija u kojima vrijednost ne ovisi samo o najbližim poznatim mjerenjima, nego i o širem kontekstu vremenskog niza.

## ZAKLJUČAK

U ovom radu implementiran je i testiran sustav za imputaciju nedostajućih temperaturnih vrijednosti u vremenskom nizu. Iz Jena Climate skupa podataka izdvojena je temperatura, zatim su umjetno stvorene nedostajuće vrijednosti u pet scenarija: random, block, block_start, block_middle i block_end. Na taj je način bilo moguće provjeriti ponašanje metoda u jednostavnijim slučajevima, ali i u težim slučajevima u kojima nedostaje velik kontinuirani dio niza.
Konačni doprinos rada nije samo implementacija pojedinih metoda, nego i usporedbeni eksperimentalni okvir u kojem se iste metode testiraju nad istim oštećenim nizovima i istim maskama. Provedeno je ukupno 440 kombinacija, što uključuje jedanaest metoda, pet scenarija i missing rateove od 10 % do 80 %, a svaka je kombinacija ponovljena nad 20 neovisnih tjednih prozora, ukupno 8800 izvođenja. Rezultati su vrednovani metrikama MAE, RMSE i R² samo na pozicijama koje su umjetno uklonjene.
Rezultati pokazuju da jednostavnije metode nisu nužno lošije od složenijih metoda strojnog učenja. Linearna interpolacija pokazala se kao najstabilniji ukupni pristup jer ostvaruje najbolji MAE u najvećem broju kombinacija i ima najniži prosječni MAE, ali je prednost pred najboljim metodama strojnog učenja manja od 0,08 °C i na kontinuiranim blokovima nestaje. Vremenska interpolacija daje iste rezultate kao linearna interpolacija jer su mjerenja u korištenom nizu ravnomjerno raspoređena u 10-minutnim intervalima, a isto vrijedi i za osnovni KNN jer obuhvaća prazninu s obje strane.
Kubna i spline interpolacija pokazale su se vrlo dobrima kod random missing scenarija pri nižim missing rateovima, ali na kontinuiranim blokovima daju daleko najveće pogreške od svih promatranih metoda. Metode strojnog učenja, uključujući napredni KNN, stablo odlučivanja, slučajnu šumu i neuronsku mrežu, najbolje su u 20 od 40 kombinacija, gotovo isključivo na kontinuiranim blokovima, i kroz cijeli su skup jednako stabilne kao linearna interpolacija.
Posebno je vidljivo da oblik nedostajućih vrijednosti snažno utječe na kvalitetu rekonstrukcije. Random missing scenarij ostaje najlakši jer su uklonjene vrijednosti najčešće okružene poznatim mjerenjima. Block scenariji, osobito pri visokim missing rateovima, znatno su zahtjevniji jer metode tada nemaju dovoljno lokalnih oslonaca unutar uklonjenog dijela niza.
Budući rad mogao bi uključiti dulje vremenske nizove, više meteoroloških varijabli, stvarne nedostajuće podatke te formalnu provjeru statističke značajnosti razlika među vodećim metodama, budući da su one u ovom eksperimentu manje od 0,08 °C.
LITERATURA
Keras Team: “Timeseries forecasting for weather prediction”, Keras Code Examples, 2020., zadnja izmjena 2023., s Interneta, https://keras.io/examples/timeseries/timeseries_weather_forecasting/.
scikit-learn developers: “mean_absolute_error”, scikit-learn documentation, s Interneta, https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html.
scikit-learn developers: “root_mean_squared_error”, scikit-learn documentation, s Interneta, https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html.
scikit-learn developers: “r2_score”, scikit-learn documentation, s Interneta, https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html.
pandas development team: “pandas.DataFrame.ffill”, pandas documentation, s Interneta, https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ffill.html.
pandas development team: “pandas.DataFrame.interpolate”, pandas documentation, s Interneta, https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html.
SciPy community: “scipy.interpolate.CubicSpline”, SciPy documentation, s Interneta, https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html.
SciPy community: “scipy.interpolate.UnivariateSpline”, SciPy documentation, s Interneta, https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html.
pandas development team: “pandas.core.window.rolling.Rolling.mean”, pandas documentation, s Interneta, https://pandas.pydata.org/docs/reference/api/pandas.core.window.rolling.Rolling.mean.html.
scikit-learn developers: “KNeighborsRegressor”, scikit-learn documentation, s Interneta, https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html.
scikit-learn developers: “DecisionTreeRegressor”, scikit-learn documentation, s Interneta, https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html.
scikit-learn developers: “RandomForestRegressor”, scikit-learn documentation, s Interneta, https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html.
Little, R. J. A.; Rubin, D. B.: “Statistical Analysis with Missing Data”, 3rd ed., Wiley, Hoboken, NJ, 2019., s Interneta, https://doi.org/10.1002/9781119482260.
Moritz, S.; Bartz-Beielstein, T.: “imputeTS: Time Series Missing Value Imputation in R”, The R Journal, vol. 9, no. 1, pp. 207–218, 2017., s Interneta, https://doi.org/10.32614/RJ-2017-009.
Goodfellow, I.; Bengio, Y.; Courville, A.: “Deep Learning”, MIT Press, Cambridge, MA, 2016., s Interneta, https://www.deeplearningbook.org/.https://doi.org/10.32614/RJ-2017-009
Kingma, D. P.; Ba, J.: “Adam: A Method for Stochastic Optimization”, 3rd International Conference on Learning Representations (ICLR), San Diego, CA, 2015., s Interneta, https://arxiv.org/abs/1412.6980.https://doi.org/10.32614/RJ-2017-009
PRILOZI
Kazalo slika i tablica
Kazalo slika
Slika 2-1 Primjer vremenskog niza s 40 % umjetno uklonjenih vrijednosti. Izvor: vlastita izrada prema pripremljenim podacima.	3
Slika 2-2 Tok pripreme podataka za eksperiment i evaluaciju metoda. Izvor: vlastita izrada prema implementaciji projekta.	5
Slika 3-1 Prikaz Series strukture kao C objekta. Izvor: vlastita izrada prema implementaciji projekta.	7
Slika 3-2 Pipeline projekta za eksperiment s 40 % nedostajućih vrijednosti. Izvor: vlastita izrada prema implementaciji projekta.	12
Slika 4-1 Izvadak temperaturnog vremenskog niza iz Jena Climate skupa podataka. Izvor: vlastita izrada prema pripremljenim podacima.	16
Slika 4-2 Prikaz forward fill metode. Izvor: vlastita izrada prema implementaciji projekta.	19
Slika 4-3 Prikaz linearne interpolacije. Izvor: vlastita izrada prema implementaciji projekta.	20
Slika 4-4 Prikaz vremenske interpolacije. Izvor: vlastita izrada prema implementaciji projekta.	21
Slika 4-5 Prikaz kubne interpolacije pomoću polinoma trećeg stupnja. Izvor: vlastita izrada prema implementaciji projekta.	22
Slika 4-6 Prikaz spline interpolacije. Izvor: vlastita izrada prema implementaciji projekta.	22
Slika 4-7 Prikaz metode pomičnog prosjeka. Izvor: vlastita izrada prema implementaciji projekta.	23
Slika 4-8 Opći proces imputacije metodama strojnog učenja. Izvor: vlastita izrada prema implementaciji projekta.	24
Slika 4-9 Prikaz KNN metode za imputaciju nedostajuće temperature. Izvor: vlastita izrada prema implementaciji projekta.	25
Slika 4-10 Prikaz sinusne i kosinusne komponente za cikličko vrijeme. Izvor: vlastita izrada prema implementaciji projekta.	26
Slika 4-11 Dijagram rada Decision Tree metode. Izvor: vlastita izrada prema implementaciji projekta.	27
Slika 4-12 Dijagram rada Random Forest metode. Izvor: vlastita izrada prema implementaciji projekta.	28
Slika 5-1 Pregled MAE vrijednosti po metodama za scenarij random missing.	32
Slika 5-2 Promjena MAE vrijednosti kroz missing rateove za scenarij random missing.	32
Slika 5-3 Promjena RMSE vrijednosti kroz missing rateove za scenarij random missing.	33
Slika 5-4 Promjena R² vrijednosti kroz missing rateove za scenarij random missing.	33
Slika 5-5 Pregled MAE vrijednosti po metodama za scenarij block missing.	35
Slika 5-6 Promjena MAE vrijednosti kroz missing rateove za scenarij block missing.	35
Slika 5-7 Promjena RMSE vrijednosti kroz missing rateove za scenarij block missing.	36
Slika 5-8 Promjena R² vrijednosti kroz missing rateove za scenarij block missing.	36
Slika 5-9 Pregled MAE vrijednosti po metodama za scenarij block_start.	38
Slika 5-10 Promjena MAE vrijednosti kroz missing rateove za scenarij block_start.	38
Slika 5-11 Promjena RMSE vrijednosti kroz missing rateove za scenarij block_start.	39
Slika 5-12 Promjena R² vrijednosti kroz missing rateove za scenarij block_start.	39
Slika 5-13 Pregled MAE vrijednosti po metodama za scenarij block_middle.	41
Slika 5-14 Promjena MAE vrijednosti kroz missing rateove za scenarij block_middle.	41
Slika 5-15 Promjena RMSE vrijednosti kroz missing rateove za scenarij block_middle.	42
Slika 5-16 Promjena R² vrijednosti kroz missing rateove za scenarij block_middle.	42
Slika 5-17 Pregled MAE vrijednosti po metodama za scenarij block_end.	43
Slika 5-18 Promjena MAE vrijednosti kroz missing rateove za scenarij block_end.	44
Slika 5-19 Promjena RMSE vrijednosti kroz missing rateove za scenarij block_end.	45
Slika 5-20 Promjena R² vrijednosti kroz missing rateove za scenarij block_end.	45
Slika 5-21 Vizualna rekonstrukcija linearnom interpolacijom za scenarij random missing pri 20 % missing ratea.	46
Slika 5-22 Vizualna rekonstrukcija linearnom interpolacijom za scenarij block missing pri 20 % missing ratea.	47
Slika 5-23 Vizualna rekonstrukcija linearnom interpolacijom za scenarij block_start pri 20 % missing ratea.	47
Slika 5-24 Vizualna rekonstrukcija linearnom interpolacijom za scenarij block_middle pri 20 % missing ratea.	48
Slika 5-25 Vizualna rekonstrukcija linearnom interpolacijom za scenarij block_end pri 20 % missing ratea.	48
Kazalo tablica
Tablica 4-1 Usporedba osnovne i napredne KNN metode.	26
Tablica 5-1 Najbolja metoda po scenariju i missing rateu prema MAE metrici.	30
Tablica 5-2 MAE vrijednosti za scenarij random missing pri missing rateovima od 10% do 80%.	31
Tablica 5-3 MAE vrijednosti za scenarij block missing pri missing rateovima od 10 % do 80 %.	34
Tablica 5-4 MAE vrijednosti za scenarij block_start pri missing rateovima od 10 % do 80 %.	37
Tablica 5-5 MAE vrijednosti za scenarij block_middle pri missing rateovima od 10 % do 80 %.	40
Tablica 5-6 MAE vrijednosti za scenarij block_end pri missing rateovima od 10 % do 80 %.	43
Tablica 5-7 Sažetak rezultata po metodama kroz svih 40 kombinacija scenarija i missing ratea.	49
Pokretanje programa
Program se pokreće iz naredbenog retka. Cijeli eksperiment može se pokrenuti naredbom diplomski.exe --experiment-all ili skriptom report.bat, koja pokreće izgradnju programa, eksperiment, pripremu grafova i HTML pregled rezultata.
Struktura projekta
Osnovna struktura projekta uključuje mape data, src, tests i results. Mapa data sadrži ulazne podatke, src sadrži C implementaciju, tests sadrži testove, a results izlazne CSV datoteke i pripremljene rezultate.
Primjer CSV rezultata
Primjer retka iz datoteke experiment_results.csv sadrži scenario, block_position, missing_rate, method, mae, rmse, r2, number_of_missing_values i number_of_evaluated_values. Ti stupci omogućuju usporedbu metoda po scenariju, postotku nedostajućih vrijednosti i evaluacijskim metrikama.
Popis oznaka i kratica
U nastavku su navedene oznake i kratice korištene u radu. Popis se može proširiti tijekom daljnjeg pisanja rada ako se uvedu dodatni pojmovi ili alati.
Tablica P- Popis oznaka i kratica korištenih u radu.

**TABLICA 9**

| Oznaka / kratica | Značenje u radu |
|---|---|
| ML | Strojno učenje (engl. Machine Learning). |
| KNN | k-nearest neighbors; metoda koja traži k najsličnijih poznatih primjera. |
| DT | Decision Tree; stablo odlučivanja. |
| RF | Random Forest; skup više stabala odlučivanja. |
| MAE | Mean Absolute Error; srednja apsolutna pogreška. |
| RMSE | Root Mean Squared Error; korijen srednje kvadratne pogreške. |
| R² | Koeficijent determinacije. |
| NaN | Not a Number; oznaka za nedostajuću numeričku vrijednost. |
| CSV | Comma-Separated Values; tekstualni format za spremanje tabličnih podataka. |
| CLI | Command Line Interface; pokretanje programa putem naredbenog retka. |
| timestamp | Vremenska oznaka mjerenja. |
| mask | Pomoćni niz koji označava umjetno uklonjene vrijednosti. |
| damaged | Oštećeni niz s umjetno uklonjenim vrijednostima. |
| reconstructed | Niz nakon rekonstrukcije nedostajućih vrijednosti. |
| MLP | Multilayer Perceptron; višeslojni perceptron, ovdje korištena neuronska mreža. |
| Adam | Adaptive Moment Estimation; postupak osvježavanja težina pri učenju mreže. |
| rezidual | Odstupanje stvarne vrijednosti od linearne procjene. |

SAŽETAK/ABSTRACT I KLJUČNE RIJEČI/KEYWORDS
Sažetak
U radu se ispituje koliko različiti postupci mogu pouzdano rekonstruirati nedostajuće temperature u vremenskom nizu. Eksperimenti su provedeni na temperaturnoj komponenti skupa Jena Climate, pri čemu su poznate vrijednosti namjerno uklanjane prema scenarijima random, block, block_start, block_middle i block_end. Uspoređeno je jedanaest metoda: forward fill, linearna, vremenska, kubna i spline interpolacija, pomični prosjek, osnovni i napredni KNN, Decision Tree, Random Forest te neuronska mreža. Missing rate mijenjan je od 10 % do 80 %, a svaka je kombinacija ponovljena nad 20 neovisnih tjednih prozora kako zaključci ne bi ovisili o jednom razdoblju. Pogreška je računata samo na uklonjenim pozicijama pomoću MAE, RMSE i R². U cjelokupnoj usporedbi linearna interpolacija ostala je najstabilnija, ali su razlike prema najboljim metodama strojnog učenja manje od 0,08 °C, a na kontinuiranim blokovima prednost prelazi na njihovu stranu.
Ključne riječi
Interpolacija podataka, imputacija, vremenski nizovi, strojno učenje, KNN, Random Forest, neuronska mreža
Title in English
Data Interpolation Using Machine Learning
Abstract
This thesis examines how reliably different methods can reconstruct missing temperature values in a time series. Experiments were carried out on the temperature component of the Jena Climate Dataset, with known values deliberately removed using the random, block, block_start, block_middle, and block_end scenarios. Eleven methods were compared: forward fill, linear, time, cubic and spline interpolation, moving average, basic and advanced KNN, Decision Tree, Random Forest, and a neural network. Missing rates ranged from 10% to 80%, and every combination was repeated over 20 independent weekly windows so that the conclusions would not depend on a single period. MAE, RMSE, and R² were calculated only at the removed positions. Across the complete set of experiments linear interpolation remained the most stable approach, but its margin over the best machine learning methods is below 0.08 °C, and on continuous blocks the advantage shifts to them.
Keywords
Data interpolation, imputation, time series, machine learning, KNN, Random Forest, neural network