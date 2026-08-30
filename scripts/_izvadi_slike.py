"""Izvlaci ugradene slike iz .docx i ispisuje XML strukturu natpisa slike."""

import sys
import zipfile
from pathlib import Path

import docx
from docx.oxml.ns import qn

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
DOK = ROOT / "docs" / "Diplomski-Toni_Jakelic_azurirano.docx"
ODLAG = ROOT / "docs" / "_slike_iz_rada"
ODLAG.mkdir(exist_ok=True)

with zipfile.ZipFile(DOK) as z:
    media = [n for n in z.namelist() if n.startswith("word/media/")]
    print(f"ugradenih datoteka: {len(media)}")
    for n in sorted(media):
        info = z.getinfo(n)
        print(f"  {Path(n).name:<24}{info.file_size / 1024:>9.1f} kB")
        (ODLAG / Path(n).name).write_bytes(z.read(n))

d = docx.Document(str(DOK))
print("\nXML natpisa 'Dijagram rada Random Forest metode':")
for p in d.paragraphs:
    if p.text.strip().startswith("Slika") and "Random Forest" in p.text:
        xml = p._element.xml
        print(xml[:4000])
        break
