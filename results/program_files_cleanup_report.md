# Izvještaj: Program Files audit i čišćenje (C:)

**Datum:** 2026-07-03  
**Korisnik:** ToniJakelić  
**Log:** `D:\media\logs\programfiles_audit_2026.log`  
**Sirovi podaci:** `C:\Users\ToniJakelić\Desktop\diplomski-u-cu\results\_pf_scan.csv`

---

## Sažetak

| Stavka | Vrijednost |
|--------|------------|
| **Oslobođeno na C: (premještaj)** | **~2,11 GB** (Epic Games launcher + Genshin/Epic mapa) |
| **Slobodno na C: (sada)** | **~604,5 GB** |
| **Slobodno na D:** | **~393 GB** |
| **Deinstalacije izvršene** | **0** (nije ništa deinstalirano bez odobrenja) |
| **Potencijalno uz predložene deinstalacije** | **~17 GB** (bez igara) / **~46 GB** (uključujući Riot/Valorant ako više ne igraš) |
| **Potencijalno uz premještaj igara na D:** | **~+114 GB** na C: (Overwatch + Hearthstone + Riot; Steam već na `D:\STEAM`) |

---

## Izvršeno: premještaj na D:

| Što | Stara lokacija (junction) | Nova lokacija na D: | Veličina |
|-----|---------------------------|---------------------|----------|
| Epic Games Launcher (x86) | `C:\Program Files (x86)\Epic Games` → junction | `D:\Games\Epic\Launcher-x86` | ~1,76 GB |
| Epic Games (x64, Genshin stub) | `C:\Program Files\Epic Games` → junction | `D:\Games\Epic\Games-x64` | ~0,35 GB |

**Napomene:**
- Junction (`mklink /J`) zadržava putanje koje očekuje launcher; podaci su fizički na D:.
- Duplikat `Epic Games.old_*` uklonjen s C: nakon kopije (admin).
- **Epic biblioteka igara:** u launcheru → Settings → Downloads → promijeni mapu instalacije na npr. `D:\Games\Epic\Library` za buduće instalacije (Fortnite je već obrisan).

---

## Već napravljeno (potvrđeno u audit-u)

| Stavka | Status |
|--------|--------|
| Fortnite | Nema u PF / uninstall ključevima |
| OBS | Nema u PF |
| AutoCAD 2025 | Mapa `AutoCAD 2025` **nije** prisutna; **~3,79 GB** Autodesk ostataka u `C:\Program Files\Autodesk` + registry unosi (deinstalacija u tijeku?) |
| Steam | **~71,5 GB** na `D:\STEAM` (premještaj u tijeku – OK) |

---

## Značajne instalacije (>0,5 GB u Program Files)

| Aplikacija | Lokacija | GB | Zadnja aktivnost (heuristika) | Preporuka |
|------------|----------|-----|-------------------------------|-----------|
| Overwatch | PF (x86) | 71,34 | 2026-06-30 (mapa) | **MOVE_TO_D** – Battle.net → Install location |
| Hearthstone | PF (x86) | 12,69 | 2026-06-30 | **MOVE_TO_D** – Battle.net |
| Microsoft (x86 runtime) | PF (x86) | 4,75 | 2024-08-15 | **KEEP** – komponente |
| Microsoft Office | PF | 4,73 | 2026-06-29 | **KEEP** |
| DaVinci Resolve | PF + x86 BM | ~4,38 | 2025-01-09 | **MOVE_TO_D** ili deinstalacija ako ne koristiš |
| Autodesk ostaci | PF | 3,79 | 2026-06-24 | **PROPOSE_UNINSTALL** nakon AutoCAD deinstalacije |
| Battle.net | PF (x86) | 2,22 | 2026-07-02 | **KEEP** (premjesti igre, ne cijeli client nužno) |
| Citrix Workspace | PF (x86) | 1,71 | 2026-06-24 | **KEEP** ako treba posao/VDI |
| Brave | PF | 1,49 | 2026-07-02 | **KEEP** |
| Google Chrome | PF | 1,19 | 2024-08-15 | **KEEP** |
| OneBrowser | PF (x86) | 0,65 | 2025-08-25 | **PROPOSE_UNINSTALL** (dupli browser) |
| WSL | PF | 0,63 | 2025-01-07 | **KEEP** |
| Git | PF | 0,40 | 2025-01-07 | **KEEP** |
| Oracle VirtualBox | PF | 0,21 | 2025-01-16 | **MOVE_TO_D** ili KEEP (mala) |
| Riot Vanguard | PF | 0,17 | 2026-07-03 | **KEEP** uz Valorant |

### Izvan Program Files (bitno za prostor)

| Aplikacija | Lokacija | GB | Zadnja aktivnost | Preporuka |
|------------|----------|-----|------------------|-----------|
| Riot Client + VALORANT | `C:\Riot Games` | 29,58 | 2024-11-01 (mapa) | **MOVE_TO_D** ili deinstalacija ako ne igraš |
| CapCut | AppData Local | 7,36 | 2025-04-19 | **PROPOSE_UNINSTALL** ako ne montiraš |
| Hearthstone Deck Tracker | AppData Local | 0,16 | – | **PROPOSE_UNINSTALL** uz HS ako ne treba |
| GenshinImpact (stub) | u Epic x64 mapi | ~0,35 | 2024-08-21 | **PROPOSE_UNINSTALL** ostatak |
| MSYS2 | `C:\msys64` | 0,95 | 2026-01-13 | **KEEP** (dev / diplomski) |

**Nije pronađeno u PF:** Valorant exe u PF (Riot koristi `C:\Riot Games`), Genshin puni client, CapCut u PF, Blizzard mapa osim Battle.net launchera.

---

## Zadržano (KEEP) – zašto

- **Windows / AMD / .NET / Defender / Common Files** – sustav
- **Git, WSL, MSYS2** – razvoj
- **Chrome, Brave, OneDrive, LGHUB, Zotero, Office** – alati koje vjerojatno koristiš
- **Citrix** – nedavno ažurirano (2026-06); ostavi ako koristiš remote posao
- **Overwatch / Hearthstone / Battle.net** – **nedavno korišteno** (30.06.2026.) → ne predlažem deinstalaciju, nego **premještaj na D:**
- **Steam** – već na D:

---

## Predloženo za deinstalaciju (PITAJ PRIJE – NIJE IZVRŠENO)

Odgovori **DA/NE** po broju (ili batch npr. „DA 1,3,4“).

1. **Autodesk ostaci** (~3,8 GB) – AutoCAD mapa otišla, registry i `C:\Program Files\Autodesk` još tu.  
2. **DaVinci Resolve + Control Panels** (~4,4 GB) – zadnja izmjena siječanj 2025.  
3. **CapCut** (~7,4 GB, AppData) – zadnja aktivnost travanj 2025.  
4. **OneBrowser** (~0,65 GB) – nepotreban dodatni Chromium browser.  
5. **Genshin Impact ostatak (Epic)** (~0,35 GB) – star stub, igra vjerojatno uklonjena.  
6. **Hearthstone Deck Tracker** (~0,16 GB) – samo ako ne igraš HS / ne koristiš tracker.  
7. **Riot Client + VALORANT + Vanguard** (~29,8 GB ukupno na C:) – **samo ako više ne igraš** (mapa Riot zadnji put studeni 2024.).

**Ukupno ako odobriš 1–6:** ~**16,4 GB**  
**Ukupno ako odobriš i 7:** ~**46 GB**

---

## Predloženo premještanje na D: (nije automatski – igre imaju own launcher)

| Prioritet | Što | GB | Kako |
|-----------|-----|-----|------|
| 1 | Overwatch | 71,34 | Battle.net → Settings → Game Install Location → `D:\Games\Blizzard\Overwatch` |
| 2 | Hearthstone | 12,69 | Isto preko Battle.net |
| 3 | Riot / Valorant | 29,58 | Riot Client → Settings → install directory → npr. `D:\Games\Riot` |
| 4 | DaVinci Resolve | 4,38 | Blackmagic installer nema jednostavan move – reinstall na D: ili ostavi |
| 5 | VirtualBox | 0,21 | Opcionalno; premještaj VM diskova na D: važniji od same aplikacije |

**Potencijal oslobađanja C: samo premještajem igara (3–5):** ~**114 GB** (plus Steam već na D:).

---

## Napomene o metodologiji

- Veličine: rekurzivno brojanje datoteka u mapama.
- „Zadnja aktivnost“: `LastWriteTime` mape + `InstallDate` iz registry Uninstall ključeva gdje postoji; nije 100% točno kao stvarno pokretanje.
- **Nijedna deinstalacija nije pokrenuta** (u skladu s „pitaj prije“).

---

## Sljedeći koraci (preporuka)

1. Potvrdi da Epic launcher radi (junction na D:).  
2. Odgovori na listu **1–7** za deinstalacije.  
3. Odluči hoćeš li **premjestiti** Overwatch / HS / Riot preko launchera (najveći dobitak na C:).  
4. Nakon AutoCAD deinstalacije: ako ostane Autodesk u registry-ju, pokreni **1** ili ručno „Autodesk Access“ cleanup.

