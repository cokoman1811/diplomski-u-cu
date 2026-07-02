# Kandidati za premještaj s C: na D: (skeniranje samo za čitanje)

**Datum skena:** 2026-07-03  
**Profil:** `C:\Users\ToniJakelic`  
**Stanje diskova:** C: ~953 GB ukupno, **~53 GB slobodno** (~94% popunjeno); D: ~1863 GB ukupno, **~595 GB slobodno**

> **Napomena:** Ništa nije premješteno niti brisano tijekom ovog skena.

---

## Već riješeno / ne treba duplo premještati

| Putanja | Veličina | Kategorija | Napomena |
|---------|----------|------------|----------|
| `Desktop\media` → **junction** na `D:\media` | ~552 GB na **D:** | Video/Muzika | Glavna medijateka je već na sporijem disku; na C: ostaje samo junction (~0 B). **Ne broji se** kao dodatni kandidat za kopiranje. |

---

## Prioritetni kandidati (sortirano po veličini i jednostavnosti)

### 1. Steam biblioteka — **~233 GB** | Igre | **Srednje**

- **Putanja:** `C:\steam`
- **Oslobođeno na C:** ~233 GB
- **Kako:** Steam → *Settings* → *Storage* → dodaj `D:\Games\Steam` (ili slično) → premjesti instalirane igre; ili u Steamu desni klik na igru → *Install folder* → *Move*. Alternativa: cijeli folder kopirati na D: i ažurirati `libraryfolders.vdf`.
- **Igre u biblioteci (iz `libraryfolders.vdf`):** m.in. veliki naslovi (Witcher 3 ~110 GB, Cyberpunk ~64 GB, itd. — provjeri u Steam klijentu).

### 2. Desktop backup medija — **~159 GB** | Video/Muzika | **Lako**

- **Putanja:** `C:\Users\ToniJakelic\Desktop\media_ON_C_backup_20260624`
- **Oslobođeno na C:** ~159 GB
- **Kako:** Premjesti cijeli folder na npr. `D:\media\_backup_20260624` (robocopy ili Explorer). Nakon provjere da je sve na D:, obriši s C: (ručno). **Provjeri duplikate** s `D:\media` prije brisanja — backup može djelomično preklapati već premještenu medijateku.

### 3. Epic Games (Fortnite + launcher) — **~79 GB** | Igre | **Srednje**

- **Putanja:** `C:\Program Files\Epic Games` (Fortnite ~78 GB; Genshin Impact ~0,35 GB)
- **Oslobođeno na C:** ~79 GB
- **Kako:** Epic Games Launcher → *Settings* → *Manage Game Installations* → promijeni lokaciju na D: i premjesti Fortnite. Za već instalirano: kopija foldera + promjena putanje u launcheru ili reinstalacija na D:.

### 4. Overwatch — **~71 GB** | Igre | **Srednje**

- **Putanja:** `C:\Program Files (x86)\Overwatch`
- **Oslobođeno na C:** ~71 GB
- **Kako:** Battle.net → *Settings* → *Game Install/Update* → *Game Install Location* na D:; koristi *Relocate* za instalirane igre gdje je dostupno.

### 5. Desktop — slike i video (stari skup) — **~88 GB** | Video | **Lako**

- **Putanja:** `C:\Users\ToniJakelic\Desktop\Slike_i_videa_vece_od_100MB_prije_30_06_2025`
- **Oslobođeno na C:** ~88 GB
- **Kako:** Premjesti na `D:\media\...` (npr. podmapa po godini) ili spoji s postojećom strukturom na D:. Junction na Desktop **nije** potreban osim ako želiš brzi pristup.

### 6. Downloads — **~59 GB** | Preuzimanja | **Lako**

- **Putanja:** `C:\Users\ToniJakelic\Downloads`
- **Oslobođeno na C:** do ~59 GB (ovisno što zadržiš)
- **Kako:** *Settings* → *System* → *Storage* → *Change where new content is saved* (New documents/downloads → D:), ili desni klik na mapu Downloads → *Properties* → *Location* → `D:\Downloads`. Veliki sadržaj:
  - `Grid-1-2-3` folder + dupli zipovi: **~21 GB** (VDI VM diskovi)
  - ISO slike (Ubuntu, Win11 x2, Office): **~21 GB**
  - `DaVinci_Resolve_19.1.2_Windows.zip`: **~2,3 GB** (nakon instalacije može na D: ili brisanje ako instaliran)

### 7. Riot Games (VALORANT) — **~30 GB** | Igre | **Srednje**

- **Putanja:** `C:\Riot Games` (VALORANT ~11–12 GB prikazano u podmapama; ukupno skenirano ~30 GB na C: — uključuje cache/patch)
- **Oslobođeno na C:** ~30 GB
- **Kako:** Riot Client → postavke instalacije / premještaj putem opcije za lokaciju igre na D: (ili reinstalacija na D:). VALORANT zahtijeva Vanguard na C: (mali dio).

### 8. Koš za smeće — **~20 GB** | Otpad | **Lako** (brisanje, ne premještaj)

- **Putanja:** `C:\$Recycle.Bin`
- **Oslobođeno na C:** ~20 GB
- **Kako:** Isprazni Recycle Bin. Nije premještaj na D:, ali brzo oslobađa prostor.

### 9. VirtualBox VM — **~10 GB** | VM | **Srednje**

- **Putanja:** `C:\Users\ToniJakelic\VirtualBox VMs\Ubuntu\Ubuntu.vdi` (~9,2 GB)
- **Oslobođeno na C:** ~10 GB
- **Kako:** VirtualBox → *File* → *Preferences* → *Default Machine Folder* na `D:\VirtualBox VMs`; zatim premjesti VM (ili `VBoxManage movemedium`). Dodatni VDI u Downloads (`Grid-1-2-3`): vidi točku 6.

### 10. Hearthstone — **~13 GB** | Igre | **Srednje**

- **Putanja:** `C:\Program Files (x86)\Hearthstone`
- **Oslobođeno na C:** ~13 GB
- **Kako:** Battle.net relocate / nova instalacijska lokacija na D:.

### 11. CapCut cache — **~7,4 GB** | AppData cache | **Lako–srednje**

- **Putanja:** `C:\Users\ToniJakelic\AppData\Local\CapCut` (Apps ~3,2 GB, User Data ~3,5 GB)
- **Oslobođeno na C:** ~7 GB
- **Kako:** U CapCut postavkama cache/projekt folder na D: ako postoji; inače premjesti `User Data` na D: i symlink (`mklink /J`). Cache se može i očistiti ako nije potreban.

### 12. Blackmagic DaVinci Resolve — **~3,8 GB** | Dev/Video alat | **Srednje–teško**

- **Putanja:** `C:\Program Files\Blackmagic Design`
- **Oslobođeno na C:** ~4 GB
- **Kako:** Deinstalacija s C: + reinstalacija na D:; cache u `ProgramData\Blackmagic Design` (~0,7 GB) također premjestiti/čistiti.

### 13. Autodesk — **~7,5 GB** (zbroj) | CAD cache | **Srednje**

- **Putanje:** `C:\Autodesk\WI` (~3,7 GB), `C:\Program Files\Autodesk` (~3,8 GB), AppData lokalno/roaming (~0,5 GB)
- **Oslobođeno na C:** ~7–8 GB
- **Kako:** Autodesk Desktop App / postavke projekata i cache na D:; ne dirati licence bez backupa.

### 14. Google (Chrome) lokalni podaci — **~4,2 GB** | Cache | **Lako**

- **Putanja:** `C:\Users\ToniJakelic\AppData\Local\Google`
- **Oslobođeno na C:** 1–4 GB (ovisno što je cache)
- **Kako:** Chrome → clear cache; ili profil na D: (teže). Samo cache = brzo oslobađanje.

### 15. NVIDIA LocalLow — **~1,4 GB** | Cache | **Lako**

- **Putanja:** `C:\Users\ToniJakelic\AppData\LocalLow\NVIDIA`
- **Oslobođeno na C:** ~1,4 GB
- **Kako:** Shader cache može se očistiti u NVIDIA Control Panel / GeForce Experience (ponovno preuzimanje shadera u igrama).

### 16. Adobe — **~1,2 GB** | Cache | **Lako**

- **Putanje:** Roaming + Local Adobe (~0,9 GB)
- **Oslobođeno na C:** ~1 GB
- **Kako:** Creative Cloud cache/media cache folder na D: u postavkama aplikacija.

### 17. Minecraft — **~0,5 GB** | Igre | **Lako**

- **Putanja:** `AppData\Roaming\.minecraft`
- **Kako:** Launcher profil / symlink svijetova na D: ako naraste.

---

## Nije značajno nađeno (kategorije iz zadatka)

| Kategorija | Rezultat |
|------------|----------|
| GOG, Xbox (`C:\XboxGames`) | Zanemarivo / nema |
| Docker | ~0,02 GB (`AppData\Local\Docker`) |
| WSL / Ubuntu paketi | Nema velikih WSL diskova na C: u skenu |
| Android SDK, Gradle, Maven, pip, conda, Unity, Unreal | Nije pronađeno >0,5 GB |
| npm | Roaming ~0,46 GB |
| Visual Studio / .nuget | Nema velikih cacheova u profilu |
| OneDrive lokalni cache | ~0 GB |
| Hyper-V | Zanemarivo u ProgramData |
| Veliki dev (Android Studio, JetBrains) | `AppData\Local\Programs` ~3,7 GB ukupno (razni alati) — opcionalno kasnije |

---

## Sistemski fajlovi (samo spomen, tradeoff)

| Datoteka | Veličina | Napomena |
|----------|----------|----------|
| `C:\hiberfil.sys` | ~12,5 GB | Uklanja se `powercfg /hibernate off` (gubi se hibernacija). |
| `C:\pagefile.sys` | ~4,8 GB | Može se smanjiti ili premjestiti na D: (*System* → *Advanced* → Performance → Virtual memory) — **utječe na performanse** ako je C: SSD a D: HDD. |

---

## Procjena ukupnog potencijala (bez duplog brojanja medija na D:)

| Scenarij | Otprilike GB na C: |
|----------|-------------------|
| Samo **top igre + backup + desktop video + Downloads** | **~680–720 GB** |
| Uključujući koš (~20 GB brisanje) | **+20 GB** |
| Steam + Epic + Overwatch + Riot + Hearthstone + medijski backupi + Downloads | Realan plan u fazama |

**Preporučeni redoslijed:** (1) isprazni koš, (2) premjesti `media_ON_C_backup` i `Slike_i_videa...` na D:, (3) očisti/premjesti Downloads, (4) Steam na D:, (5) Battle.net/Epic igre, (6) VirtualBox + CapCut.

---

## Isključeno iz preporuke

- `diplomski-u-cu` — zanemariva veličina (~0 GB).
- `Desktop\media` — već junction na `D:\media`.

