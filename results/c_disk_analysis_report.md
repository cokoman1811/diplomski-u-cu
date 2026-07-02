# Analiza diska C: — sažetak

**Datum:** 2026-07-03 01:10  
**Detaljan log (svaki korak, naredbe, mane):** [c_disk_analysis_log.txt](./c_disk_analysis_log.txt)

## Stanje diska

| Disk | Zauzeto | Slobodno |
|------|---------|----------|
| **C:** | ~897 GB | ~56 GB |
| **D:** | ~1239 GB | ~624 GB |

Na C: je ostalo vrlo malo slobodnog prostora.

## Što najviše zauzima C:

1. **Users** (~366 GB) — profil, backup medija, VM, Downloads  
2. **steam** (~233 GB) — Steam igre  
3. **Program Files** (~98 + ~98 GB)  
4. **Windows** (~36 GB)  
5. **Koš za smeće** (~20 GB)

## Mediji i duplikati

- **Desktop\media** je **junction** na **D:\media** (~488 GB). To **nije** dupla kopija na C: — ista je lokacija na D:.
- Na Desktopu postoje **backup mape na C:** koje **jesu** stvarni trošak prostora:
  - media_ON_C_backup_20260624: **~158.63 GB**
  - Slike_i_videa_vece_od_100MB_prije_30_06_2025: **~90.45 GB**
- Velike datoteke u profilu uglavnom su iz tih backup mapa, filmova i **Downloads** (ISO, VDI, zip).

## Preporuke (prioritet)

1. **Isprazni Recycle Bin** — ~**20 GB**  
2. **Nakon provjere D:\media**, ukloni ili premjesti backup **media_ON_C_backup_20260624** — ~**158.63 GB**  
3. Isto za **Slike_i_videa_vece_od_100MB_prije_30_06_2025** ako sadržaj više ne treba na C: — ~**90.45 GB**  
4. **Downloads** — obriši/premjesti nepotrebne ISO/VDI/zip (Win11, Ubuntu, Office, Grid, DaVinci) — procjena **~30–50 GB**  
5. **Steam** igre premjesti na D: ako želiš — do **~233 GB** (opcionalno)  
6. **Temp / node_modules** — mali dobitak (~1–4 GB)

**Realna procjena** oslobađanja na C: bez diranja Steama: **~100 GB+** ako očistiš backup mape, koš i Downloads.

## Ograničenja analize (mane)

- Analiza je **read-only**; nije pokrenuta s admin pravima — dio sistemskih mapa može biti potcenjen.  
- Rekurzivno brojanje **prati junction** pa Desktop izgleda velik iako je medij na D:.  
- OneDrive placeholderi nisu posebno razdvojeni.  
- Usporedba medija C/D temelji se na uzorku datoteka, ne na punom hash-u diska.

Za transparentnost: svaki korak **a–k** u log datoteci sadrži **što**, **zašto**, **naredbu**, **output**, **mane** i **nalaz**.
