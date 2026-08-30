#!/usr/bin/env python3
"""Sprema samostalni grafovi_pregled.html s ugradenim PNG-ovima."""

from __future__ import annotations

import base64
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IZVOR = ROOT / "results" / "grafovi_pregled.html"
ODREDISTE = Path.home() / "Desktop" / "grafovi_pregled.html"

html = IZVOR.read_text(encoding="utf-8")


def ugradi(match: re.Match[str]) -> str:
    rel = match.group(1)
    put = (IZVOR.parent / rel).resolve()
    if not put.exists():
        return match.group(0)
    b64 = base64.b64encode(put.read_bytes()).decode("ascii")
    return f"src='data:image/png;base64,{b64}'"


html = re.sub(r"src='([^']+\.png)'", ugradi, html)
ODREDISTE.write_text(html, encoding="utf-8")
print(f"spremljeno: {ODREDISTE} ({ODREDISTE.stat().st_size / 1_048_576:.1f} MB)")
