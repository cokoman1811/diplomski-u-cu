#!/usr/bin/env python3
"""
Cita .docx i ispisuje strukturu rada: naslove, opseg, tablice i slike.

Koristenje:
    python scripts/procitaj_word.py                  # nade prvi .docx u projektu
    python scripts/procitaj_word.py put/do/rada.docx

Ispis je namijenjen brzom pregledu prije detaljne provjere sadrzaja.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import docx
except ImportError:
    sys.exit("Nedostaje python-docx. Instaliraj: python -m pip install python-docx")

from docx.document import Document as DocxDocument
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

ROOT = Path(__file__).resolve().parent.parent


def nadi_docx() -> Path:
    kandidati = [p for p in ROOT.rglob("*.docx")
                 if not p.name.startswith("~$") and ".git" not in p.parts]
    if not kandidati:
        sys.exit(f"Nema nijednog .docx u {ROOT}. Dodaj rad u projekt pa ponovi.")
    kandidati.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return kandidati[0]


def blokovi(parent: DocxDocument):
    """Vraca odlomke i tablice u redoslijedu u kojem se pojavljuju u dokumentu."""
    body = parent.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, parent)
        elif child.tag == qn("w:tbl"):
            yield Table(child, parent)


def razina_naslova(p: Paragraph) -> int | None:
    ime = (p.style.name or "").lower()
    m = re.match(r"(?:heading|naslov)\s*(\d+)", ime)
    if m:
        return int(m.group(1))
    if ime in ("title", "naslov"):
        return 0
    return None


def main() -> None:
    put = Path(sys.argv[1]) if len(sys.argv) > 1 else nadi_docx()
    if not put.exists():
        sys.exit(f"Ne postoji: {put}")

    d = docx.Document(str(put))

    naslovi: list[tuple[int, str, int]] = []
    tablice: list[tuple[int, Table, str]] = []
    n_rijeci = 0
    n_odlomaka = 0
    tekuci = "(prije prvog naslova)"

    for blok in blokovi(d):
        if isinstance(blok, Paragraph):
            t = blok.text.strip()
            lvl = razina_naslova(blok)
            if lvl is not None and t:
                naslovi.append((lvl, t, n_rijeci))
                tekuci = t
            elif t:
                n_odlomaka += 1
                n_rijeci += len(t.split())
        else:
            tablice.append((len(tablice) + 1, blok, tekuci))

    n_slika = len(d.inline_shapes)

    print("=" * 84)
    print(f"DATOTEKA: {put.relative_to(ROOT) if ROOT in put.parents else put}")
    print("=" * 84)
    print(f"  rijeci u tekstu (bez tablica): {n_rijeci}")
    print(f"  odlomaka:                      {n_odlomaka}")
    print(f"  naslova:                       {len(naslovi)}")
    print(f"  tablica:                       {len(tablice)}")
    print(f"  slika (inline):                {n_slika}")

    print()
    print("=" * 84)
    print("STRUKTURA (u zagradi kumulativni broj rijeci do tog naslova)")
    print("=" * 84)
    if not naslovi:
        print("  Nema odlomaka sa stilom Heading/Naslov.")
        print("  Vjerojatno su naslovi rucno formatirani, pa strukturu ne mogu iscitati.")
    for lvl, t, w in naslovi:
        print(f"  {'    ' * lvl}{t}   ({w})")

    print()
    print("=" * 84)
    print("TABLICE")
    print("=" * 84)
    for i, tbl, gdje in tablice:
        r, c = len(tbl.rows), len(tbl.columns)
        zaglavlje = " | ".join(cl.text.strip() for cl in tbl.rows[0].cells) if r else ""
        if len(zaglavlje) > 96:
            zaglavlje = zaglavlje[:93] + "..."
        print(f"  [{i}] {r}x{c}   pod naslovom: {gdje}")
        print(f"       zaglavlje: {zaglavlje}")


if __name__ == "__main__":
    main()
