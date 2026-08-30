#!/usr/bin/env python3
"""Sprema mapu za slanje: index.html + grafovi/*.png, bez ugradenih slika."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IZVOR = ROOT / "results" / "grafovi_pregled.html"
SLIKE = ROOT / "slike i videa" / "2026" / "diplomski-grafovi"
DESKTOP = Path.home() / "Desktop"
MAPA = DESKTOP / "grafovi_pregled"
ZIP_PUT = DESKTOP / "grafovi_pregled.zip"

if MAPA.exists():
    shutil.rmtree(MAPA)
MAPA.mkdir()
(MAPA / "grafovi").mkdir()

html = IZVOR.read_text(encoding="utf-8")


def preslozi(match: re.Match[str]) -> str:
    ime = Path(match.group(1)).name
    src = SLIKE / ime
    if src.exists():
        shutil.copy2(src, MAPA / "grafovi" / ime)
    return f"src='grafovi/{ime}'"


html = re.sub(r"src='([^']+\.png)'", preslozi, html)
(MAPA / "index.html").write_text(html, encoding="utf-8")

stari = DESKTOP / "grafovi_pregled.html"
if stari.exists():
    stari.unlink()

if ZIP_PUT.exists():
    ZIP_PUT.unlink()
shutil.make_archive(str(DESKTOP / "grafovi_pregled"), "zip", MAPA)

n_png = len(list((MAPA / "grafovi").glob("*.png")))
print(f"mapa {MAPA}  png={n_png}")
print(f"zip  {ZIP_PUT}  {ZIP_PUT.stat().st_size / 1_048_576:.1f} MB")
