# Program Files (x86) – izvještaj čišćenja (2026-07-03)

## Sažetak
- **Skenirano:** `C:\Program Files (x86)` (mape > 20 MB prije premještanja).
- **Premješteno na D:** igre (Blizzard, Epic), periferija (Razer, Realtek), Blackmagic; **junction** na starim putanjama radi launchera.
- **Oslobođeno na C:** ~**570 GB** (slobodan prostor C: ~206 GB → ~776 GB).
- **Log:** `D:\media\logs\programfiles_x86_2026.log`

---

## 1. Premješteno na D: (junction na izvornoj putanji)

| Što | Od (C:) | Na (D:) | ~GB na D: |
|-----|---------|---------|-----------|
| Overwatch | `C:\Program Files (x86)\Overwatch` | `D:\Games\Blizzard\Overwatch` | 71,41 |
| Hearthstone | `C:\Program Files (x86)\Hearthstone` | `D:\Games\Blizzard\Hearthstone` | 12,69 |
| Battle.net | `C:\Program Files (x86)\Battle.net` | `D:\Games\Blizzard\Battle.net` | 2,22 |
| Epic Games Launcher | `C:\Program Files (x86)\Epic Games` | `D:\Games\Epic Games` | 1,76 |
| Razer (Synapse stub) | `C:\Program Files (x86)\Razer` | `D:\Programs\Periferija\Razer` | 0,01 |
| Realtek audio/NIC | `C:\Program Files (x86)\Realtek` | `D:\Programs\Periferija\Realtek` | 0,01 |
| Blackmagic Design | `C:\Program Files (x86)\Blackmagic Design` | `D:\Programs\Blackmagic Design` | 0,58 |
| MSI Center (djelomično) | `C:\Program Files (x86)\MSI` | `D:\Programs\Periferija\MSI` | 0,65 |

**Ukupno premještenih podataka na D:** ~**89,3 GB** (fizički više nisu na C: osim MSI ostataka).

**Napomena – MSI:** Većina (~0,65 GB) je na D:; ~**0,03 GB** još stoji na C: jer su MSI usluge držale datoteke otvorenima. Junction nije kreiran. **Preporuka:** reboot → ponovno pokrenuti `D:\media\logs\msi_junction.ps1` kao administrator ili MSI Center deinstalirati i ponovno instalirati s ciljem `D:\Programs\Periferija\MSI`.

**Napomena – Battle.net:** Tijekom premještanja zatvoren je Battle.net/Agent (zaključani procesi). Ponovno pokreni Battle.net launcher.

**Logitech G HUB** nije u (x86) – nalazi se u `C:\Program Files\Logitech` (64-bit). Za potpuno „sve periferije na D“ treba isti postupak u običnom Program Files (prioritetni zadatak).

**Riot Games** – nije pronađen u (x86).

---

## 2. Sken – što je ostalo na C: u (x86) (> 20 MB ili bitno)

| Mapa | ~GB | Zadnja aktivnost (heuristika) | Odluka |
|------|-----|-------------------------------|--------|
| Microsoft (Edge, WebView…) | 4,75 | 2026-07-02 | **Zadržati** (preglednik / Windows ekosustav) |
| Citrix Workspace | 1,71 | 2026-07-02 | **Zadržati** ako koristiš remote posao; inače vidi uninstall #5 |
| OneBrowser | 0,65 | 2025-08-25 | **Predloženo uklanjanje** (#1) |
| Google (Chrome updater stub) | 0,43 | 2026-07-03 | **Zadržati** |
| dotnet | 0,15 | 2026-03-03 | **Zadržati** |
| Common Files | 0,13 | 2026-07-03 | **Zadržati** |
| AMD | 0,11 | 2024-08-15 | **Zadržati** (drajveri) |
| BraveSoftware | 0,07 | 2026-07-02 | **Zadržati** ako koristiš Brave |
| Windows Kits | 0,05 | 2025-01-31 | **Zadržati** (dev) |
| Lavasoft | 0,03 | 2025-08-25 | **Predloženo uklanjanje** (#2) |
| MSI (ostatak) | 0,03 | 2026-07-03 | Dovršiti junction ili #6 |

Mape ispod 20 MB: Adobe, Autodesk, EasyAntiCheat_EOS, EternalCast, Internet Explorer, Ubisoft (prazno), Windows komponente – većinom **zadržati** ili uninstall po listi.

**VC++ redistributables:** samo 2015–2022 (x86/x64) – **ne uklanjati** (potrebni igrama i aplikacijama).

---

## 3. Predloženo deinstaliranje (treba tvoj **DA**)

Odgovori brojevima npr. „DA 1,2,4“ – **ništa se ne deinstalira automatski** osim ako ne potvrdiš.

1. **OneBrowser** (~0,65 GB) – nepoznati/Chromium browser, zadnja aktivnost kolovoz 2025.
2. **Lavasoft** (Web Companion / ostaci, ~0,03 GB) – često neželjeni softver, neaktivno 10+ mjeseci.
3. **EternalCast** (~0,01 GB) – mali nepoznati launcher; neaktivno.
4. **Autodesk App Manager + Featured Apps** (~0,02 GB u mapi) – samo ako **ne** koristiš Autodesk proizvode.
5. **Citrix Workspace 2603** (~1,7 GB u mapi + registar) – **samo ako više ne radiš preko Citrixa** (pažljivo – posao).
6. **MSI Center SDK / ostatak na C:** – alternativa: reboot + junction ili reinstall na D: (bolje nego brisati ako koristiš MSI ploču).

**Već uklonjeno ranije (ne dirati):** Fortnite, OBS.

**Ne predlažem:** duplikate VC++, Microsoft Edge/WebView, Windows mape u (x86).

---

## 4. Zadržano na C: (brzina / sustav)

- Microsoft Edge + WebView2 (x86 kopije)
- Google / Brave updateri
- dotnet, Common Files, AMD, Windows Kits, EasyAntiCheat_EOS
- Citrix (dok ne potvrdiš #5)

---

## 5. GB oslobođeno na C:

| Metrika | Vrijednost |
|---------|------------|
| Slobodno prije | ~206 GB |
| Slobodno poslije | ~776 GB |
| **Procjena oslobođeno** | **~570 GB** |

(D: slobodno ~586 GB nakon premještanja.)

---

## 6. Sljedeći koraci (opcionalno)

- Restart računala → dovršiti **MSI junction** (`D:\media\logs\msi_junction.ps1` kao admin).
- Pokrenuti Battle.net / Epic – provjera igara s junction putanjama.
- **Logitech** (`C:\Program Files\Logitech`) premjestiti na `D:\Programs\Periferija\Logitech` u zasebnoj akciji.
- Citrix na D: samo ako želiš i podržava custom install – inače ostaje na C: (nije gaming SSD prioritet ako ga koristiš).

---
*Generirano: 2026-07-03*
