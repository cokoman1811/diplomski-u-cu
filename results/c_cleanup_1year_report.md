# Izvještaj: čišćenje diska C: (starije od 1 godine)

**Datum:** 2026-07-03  
**Granični datum (cutoff):** prije 2025-07-03 (zadnja izmjena **i** zadnji pristup)  
**Korisnik:** ToniJakelić / ToniJakeliic  
**Log brisanja:** D:\media\logs\c-cleanup-1year_2026.log  

## Sažetak prostora

| Mjera | Vrijednost |
|-------|------------|
| Slobodno prije | ~776,41 GB |
| Slobodno poslije | ~798.04 GB |
| **Oslobođeno (delta na C:)** | **~21.63 GB** |
| Zabilježeno brisanje u logu (datoteke) | ~1,56 GB (5237+ zapisa) |

> Veći dio oslobođenog prostora dolazi od **Koša za smeće** (masovno pražnjenje); veličina nije pouzdano očitana prije brisanja zbog dozvola na `\.Bin`.

## Što je obrisano / uklonjeno

### Datoteke (sigurne kategorije)
- **CapCut cache** – 4029 datoteka, ~1,47 GB (cache/projekt privremene datoteke starije od cutoff-a)
- **Stari .log** u AppData/Temp – ~1204 datoteke, ~0,10 GB (isključeni Cursor, diplomski, Discord, HDT)
- **C:\condor** – stari token/log remnant (prazne datoteke)
- **C:\$WINDOWS.~BT** – 4 male datoteke (remnant)
- **TEMP** (user + Windows) – nema datoteka koje zadovoljavaju oba datuma
- **npm-cache, INetCache, pip, Adobe cache, Chrome Cache** – nema ili već prazno / nije starije od cutoff-a
- **Koš za smeće** – ispražnjen (`Clear-RecycleBin`)

### Deinstalacije (winget / MSI / uninstaller)
- **EternalCast** – uklonjen (drugi pokušaj: `Uninstaller.exe /S`; winget prvi put nije očistio datoteke)
- **Autodesk Save to Web and Mobile** – MSI exit 0 (uspješno)
- **Dropbox Redeem Launcher** – folder već nije postojao / winget greška 0x800401f5

## Što je **preskočeno** (sigurnost / datumi)

| Stavka | Razlog |
|--------|--------|
| **C:\Windows**, **C:\msys64** | Eksplicitno zaštićeno |
| **diplomski-u-cu**, **.cursor**, **.vscode** | Aktivni projekt / alati |
| **Minecraft / Epic** junction putanje | Zaštićeno; provjera reparse točaka pri brisanju |
| **Preuzimanja (Downloads)** ~335 dat. (~1,2 GB po datumu izmjene) | **LastAccessTime** ažuriran na 2026-07-03 (indexer/pregled mape) – krši pravilo „ne dirati ako je pristup nakon cutoff-a“ |
| **CapCut** ~3,4 GB preostalo | Novije datoteke (izmjena/pristup nakon cutoff-a) |
| **OneBrowser** | Instalacija 2025-08; pristup 2026-07 |
| **Hearthstone Deck Tracker** | Instalacija/korištenje 2026-06 |
| **Overwatch / Hearthstone / Riot Games** | Nedavni pristup (2026-07) |
| **Blackmagic / DaVinci** (Program Files) | Pristup 2026-07; puni Resolve nije u wingetu, samo Control Panels |
| **Steam** | Eksplicitno ne dirati bez plana reinstalacije |
| **C:\Program Files\Autodesk** (~1,8 GB) | Nedavna aktivnost mape (2026-07); AutoCAD već uklonjen, ostali Autodesk servisi aktivni |
| **media_ON_C_backup** | Ne postoji na Desktopu |
| **C:\Users\TONIJA~2** | Nije prazan profil (AppData) – brisanje profila zahtijeva admin |
| **C:\ESD**, **inetpub** | Već prazni / bez starih datoteka |
| **hiberfil.sys / pagefile.sys** | Nije dirano |

## Potrebno **administrator** / ručno

1. **DaVinci Resolve Control Panels** – `msiexec /X{3739CA49-792F-4F1F-9B76-42DFBBBED27E}` → exit **1603** (potrebna elevacija ili Repair pa deinstalacija)
2. **Uklanjanje mape C:\$WINDOWS.~BT** / Windows Update cleanup – DISM/cleanmgr kao admin ako želiš dodatne GB
3. **Profil TONIJA~2** – brisanje duplikata korisnika kroz System → Advanced → User Profiles
4. **OBS registry** – ako postoji stari OBS zapis (nije pronađen `C:\obs`)
5. **Downloads** – opcionalno brisanje samo po **LastWriteTime** (ignorirati pristup) – **nije** napravljeno zbog striktnog pravila; javi ako želiš tu politiku

## Deinstalacije koje **nisu** izvršene (korištenje unutar godine)

- OneBrowser, HDT, Overwatch, CapCut (aplikacija), Battle.net igre – zadnja upotreba / instalacija unutar 12 mjeseci

## Napomene

- Svako brisanje datoteke zapisano u log: `datum TAB veličina TAB razlog TAB putanja`.
- Prije brisanja provjeravani **reparse/junction** atributi (39 stavki preskočeno kao REPARSE/FAIL).
- **Ne masovno brisati Program Files** – korišteni uninstaller/MSI gdje je bilo moguće.

---
*Automatski generirano: 2026-07-03 02:24:27*
