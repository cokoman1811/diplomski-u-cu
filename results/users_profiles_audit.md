# Revizija korisničkih profila Windows

**Datum:** 3. srpnja 2026.  
**Računalo:** DESKTOP-AHOPD2H  
**Aktivna sesija:** `azuread\tonijakelic` (mapa profila: `C:\Users\ToniJakelic`)

## Sažetak

| Stavka | Vrijednost |
|--------|------------|
| Profilnih mapa u `C:\Users` | 3 (prije čišćenja) → 2 korisnička + Public nakon uspješnog brisanja |
| Duplikat iste osobe | **Da** – `ToniJakelic` (aktivan) i `ToniJakelić` / `TONIJA~2` (sirovište) |
| GB za povrat od duplog profila | **~0 GB** (samo prazne mape, 0 datoteka) |
| GB u aktivnom profilu (informativno) | **~280 GB** ukupno |

**Zaključak:** Dva profila **nisu** potrebna. Drugi (`ToniJakelić`) nije registriran u sustavu, nema dokumente ni Desktop – vjerojatno ostatak neuspješnog ili starog mapiranja imena (č/ć, Azure AD). Sav sadržaj je u `ToniJakelic`.

---

## 1. Pregled mapa u `C:\Users`

| Mapa | Veličina (procjena) | Zadnja izmjena | Uloga |
|------|---------------------|----------------|-------|
| `Public` | ~0,03 GB | 23. 4. 2026. | Sistemska – **ne brisati** |
| `ToniJakelic` | ~280 GB | 1. 7. 2026. | **Aktivni** korisnički profil |
| `ToniJakelić` (`TONIJA~2`) | 0 datoteka | 23. 4. 2026. | Sirovište – **nije u registru** |

### Registar `ProfileList`

Jedini korisnički `ProfileImagePath`:

- `C:\Users\ToniJakelic` (SID: `S-1-12-1-2010400047-1172771779-3277244051-1917014270`)

Mapa `ToniJakelić` **nema** zapis u `ProfileList` niti u `Win32_UserProfile`.

### Lokalni računi (`Get-LocalUser`)

Prikazani su samo ugrađeni računi (Administrator, Guest, DefaultAccount, WDAGUtilityAccount) – svi onemogućeni. Glavni korisnik je **Microsoft / Azure AD** račun, ne zasebni lokalni duplikat.

---

## 2. Aktivni vs. neaktivni

| Pitanje | Odgovor |
|---------|---------|
| Tko je prijavljen? | `ToniJakelic` (`azuread\tonijakelic`) |
| Koji profil je učitan (`Loaded=True`)? | `C:\Users\ToniJakelic` |
| Je li duplikat ista osoba? | **Da** – ista osoba, različito ime mape (s i bez dijakritike) |

---

## 3. Usporedba sadržaja

| Lokacija | `ToniJakelić` (sirovište) | `ToniJakelic` (aktivan) |
|----------|---------------------------|-------------------------|
| Desktop | nema | ~175,5 GB |
| Documents | nema | ~0,05 GB |
| Downloads | nema | ~58,1 GB |
| AppData | samo prazna struktura (Adobe) | ~34,3 GB |
| Datoteke ukupno (`dir /s`) | **0** | pun profil |

Drugi profil **nije** backup ni kopija podataka – praktički je prazan.

---

## 4. Sigurne opcije čišćenja

| Akcija | Preporuka |
|--------|-----------|
| `Public`, `Default` | Ne dirati |
| `C:\Users\ToniJakelic` | **Nikad brisati** – aktivni profil |
| `C:\Users\ToniJakelić` (`TONIJA~2`) | Obrisati nakon preuzimanja vlasništva (Admin) – **nema podataka** |
| Postavke → Računi | Nema drugog korisnika za uklanjanje kroz GUI |
| Spajanje profila | **Nije potrebno** – nema što spajati |

---

## 5. Izvršene akcije

1. **Revizija** – registar, `Win32_UserProfile`, veličine mapa, usporedba sadržaja.
2. **Pokušaj brisanja** praznog profila `C:\Users\TONIJA~2` – **neuspješno** zbog *Access denied* na `AppData\Roaming\Adobe\ExtensibilityLibrary\Log` (potrebna **elevacija Administratora**).
3. **Nije diran** aktivni profil `ToniJakelic`.
4. **Log:** `D:\media\logs\users_audit_2026.log`

### Korak za tebe (Administrator CMD ili PowerShell kao Admin)

```bat
takeown /f "C:\Users\TONIJA~2" /r /d y
icacls "C:\Users\TONIJA~2" /grant Administrators:F /t
rmdir /s /q "C:\Users\TONIJA~2"
```

*(Ako je puna putanja s `ć`, možeš koristiti `C:\Users\TONIJA~2`.)*

---

## 6. Gdje stvarno leži prostor

Dupli profil **ne oslobađa značajan disk**. Za uštedu prostora gledaj unutar aktivnog profila:

- Desktop ~175 GB  
- Downloads ~58 GB  
- AppData ~34 GB  

To je odvojeno od pitanja „dva ista korisnika“.

---

*Izvještaj generiran automatskom revizijom profila.*
