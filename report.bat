@echo off
cd /d "%~dp0"

echo === 0/4 Priprema podataka (7 dana) ===
python scripts\prepare_jena_7d.py
if errorlevel 1 (
    echo Greska pri pripremi jena_temperature_7d.csv
    exit /b 1
)

echo.
echo === 1/4 Build ===
call build.bat
if errorlevel 1 exit /b 1

echo.
echo === 2/4 Eksperiment (CSV rezultati) ===
if not exist diplomski.exe (
    echo Greska: diplomski.exe ne postoji.
    exit /b 1
)
diplomski.exe --experiment-all --source jena_quick
if errorlevel 1 exit /b 1

echo.
echo === 3/4 Grafovi i analiza (Python) ===
python scripts\report.py
if errorlevel 1 (
    echo.
    echo Python nije pronaden ili fale paketi.
    echo Instaliraj: pip install -r scripts\requirements.txt
    exit /b 1
)

echo.
echo === 4/6 Tablice rezultata (Python) ===
python scripts\generate_results_tables.py
if errorlevel 1 exit /b 1

echo.
echo === 5/6 Diplomski dokument za ChatGPT ===
python scripts\generate_thesis_doc_10_80.py
if errorlevel 1 exit /b 1

echo.
echo === 6/6 ChatGPT zip prilozi ===
python scripts\generate_changelog_for_chatgpt.py
python scripts\generate_chatgpt_zip.py
if errorlevel 1 exit /b 1

echo.
echo Sve spremno:
echo   results\experiment_results.csv       - tablice rezultata
echo   results\tablice\                   - sve tablice (CSV, Excel, MD)
echo   results\analysis.md                  - tekstualna analiza
echo   results\diplomski_dokument_10_80_za_chat.md - sazetak za ChatGPT
echo   results\chatgpt_prilozi.zip          - ZIP za slanje ChatGPT-u
echo   results\chatgpt_prompt_za_nadopunu.md - prompt za kopiranje
echo   results\grafovi_pregled.html         - vizualni pregled
echo   slike i videa\2026\diplomski-grafovi\ - PNG grafovi
pause
