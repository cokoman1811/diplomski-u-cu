# Agenti — GitHub sync i pisanje dokumentacije

**Autor:** Toni Jakelić  
**Vrsta rada:** popratna infrastruktura (Cursor agenti + skripte)  
**Trajanje:** ~3 dana (vikendi i urezani između faza implementacije)

> Ovo **nije** znanstveni dio diplomskog, ali je važan za rad na projektu:
> automatski backup na GitHub i sustavni dnevni zapisi (`dan*.md`).

---

## Zašto agenti

Tijekom diplomskog radilo se u **Cursoru** s AI agentima. Dva ponavljajuća zadatka
nisu bila jezgro teme (imputacija), ali su trošila vrijeme:

1. **Ručni git add / commit / push** nakon svake sesije
2. **Pisanje i održavanje dokumentacije** (dnevnik rada, FAQ, raspored)

Za to su postavljeni posebni agenti i skripte — nekoliko dana rada na postavci i doradi.

---

## Dan A — Agent za GitHub push (8.–9. lipnja 2026.)

**Kada:** vikend nakon Dana 2 (paralelno s pripremom Dana 3)  
**Cilj:** Sigurnosna kopija koda na GitHub bez ručnog rada nakon svake sesije.

### Što je napravljeno

- [x] `scripts/git-sync.ps1` — `git add` → `commit` → `pull` → `push`
- [x] `git-sync.bat` — pokretanje jednom naredbom na Windowsu
- [x] Cursor hook (`.cursor/hooks.json`) — automatski sync **nakon završetka agenta**
- [x] `.cursor/hooks/git-sync-after-agent.ps1` — hook skripta (ne blokira agenta ako nema mreže)
- [x] Dokumentacija u `docs/cesta_pitanja.md` (odjeljak Git sync)
- [x] Zadatak u `.vscode/tasks.json` za ručni sync iz Cursora

### Kako radi

```
Agent završi zadatak (Cursor stop event)
        ↓
git-sync-after-agent.ps1
        ↓
scripts/git-sync.ps1  →  GitHub remote
```

Ručno:
```powershell
.\git-sync.bat
.\git-sync.bat -CommitMessage "Opis promjene"
```

### Datoteke

| Datoteka | Uloga |
|----------|--------|
| `scripts/git-sync.ps1` | Glavna sync logika |
| `git-sync.bat` | Windows wrapper |
| `.cursor/hooks.json` | Registracija hooka |
| `.cursor/hooks/git-sync-after-agent.ps1` | Poziv nakon agenta |

Prvi put spomenuto u [dan0.md](dan0.md); dorada u [dan3.md](dan3.md) i [dan6.md](dan6.md).

---

## Dan B — Agent za pisanje dokumentacije (14.–15. lipnja 2026.)

**Kada:** vikend između Dana 7 i Dana 8 (ML faza → Decision Tree)  
**Cilj:** Sustavni dnevni zapisi i FAQ umjesto raspršenih bilješki.

### Što je napravljeno

- [x] Dnevni format `docs/danN.md` — cilj, što napravljeno, datoteke, sljedeći korak
- [x] `docs/progress.md` — tablica svih dana
- [x] `docs/cesta_pitanja.md` — FAQ za C verziju (metrike, Series, tok programa, greške)
- [x] `CHANGELOG.md` — promjene po datumu
- [x] `KORACI.md` — visoka razina koraka projekta
- [x] Prenos zapisa dan0–dan5 iz Python referentnog projekta

### Kako se koristi agent za dokumentaciju

Na kraju (ili početku) radnog dana agent dobije zadatak u stilu:

> „Napiši dnevni izvještaj Dana N — što je napravljeno, koje datoteke, sljedeći korak."

Agent generira `danN.md` i ažurira `progress.md`. **Kod** i **dokumentacija** su odvojeni —
agent za dokumentaciju ne mijenja nužno `src/`, agent za implementaciju ne piše nužno cijeli rad.

---

## Dan C — Raspored i izvještaj (19.–20. lipnja 2026., uz Dan 11–12)

**Kada:** uz dovršetak eksperimentalnog sloja  
**Cilj:** Jedan dokument za mentora — koliko dana, koje faze, što slijedi.

### Što je napravljeno

- [x] `docs/raspored.md` — 18-dnevni plan (implementacija + pisanje rada)
- [x] `docs/dan9.md`–`dan17.md` — eksperimenti, grafovi, plan pisanja
- [x] `scripts/report.py` + `report.bat` — automatska analiza i grafovi
- [x] `results/analysis.md` — tekstualni nalazi za poglavlje Rezultati

---

## Sažetak vremena

| Popratni dan | Datum | Fokus | ~sati |
|--------------|-------|-------|-------|
| **A** | 8.–9.6. | GitHub agent + hook | 4–6 h |
| **B** | 14.–15.6. | Dokumentacija + FAQ | 4–6 h |
| **C** | 19.–20.6. | Raspored + report (uz dan 11–12) | 3–4 h |

**Ukupno:** ~12–16 h kroz 3 razdoblja — ne zamjenjuje implementaciju metoda,
ali objašnjava zašto repozitorij ima hookove, bogatu `docs/` mapu i dnevne zapise.

---

## Napomena za diplomski rad

U poglavlju **Implementacija** ili **Prilog** možeš jednom rečenicom spomenuti:

> „Razvoj je vođen uz verzioniranje na GitHubu (automatski sync nakon sesija u Cursoru)
> i dnevne tehničke zapise radi reproducibilnosti i praćenja napretka."

Agenti **nisu** predmet istraživanja — alat za organizaciju rada.

---

## Povezano

- [raspored.md](raspored.md) — glavni kalendar
- [progress.md](progress.md) — status po danima
- [cesta_pitanja.md](cesta_pitanja.md) — Git sync u praksi
