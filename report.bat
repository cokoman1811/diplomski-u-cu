@echo off
cd /d "%~dp0"

set REPEATS=20

echo === 0/7 Priprema podataka (7 dana + %REPEATS% tjednih prozora) ===
python scripts\prepare_jena_7d.py
if errorlevel 1 (
    echo Greska pri pripremi jena_temperature_7d.csv
    exit /b 1
)
if not exist "data\processed\jena_windows\window_00.csv" (
    python scripts\prepare_jena_windows.py %REPEATS%
    if errorlevel 1 exit /b 1
)

echo.
echo === 1/7 Build ===
call build.bat
if errorlevel 1 exit /b 1

echo.
echo === 2/7 Eksperiment (%REPEATS% ponavljanja, CSV rezultati) ===
if not exist diplomski.exe (
    echo Greska: diplomski.exe ne postoji.
    exit /b 1
)
diplomski.exe --experiment-all --source jena_quick --repeats %REPEATS%
if errorlevel 1 exit /b 1

echo.
echo === 3/7 Testovi znacajnosti (upareni) ===
python scripts\significance.py
if errorlevel 1 exit /b 1

echo.
echo === 4/7 Grafovi i analiza (Python) ===
python scripts\report.py
if errorlevel 1 (
    echo.
    echo Python nije pronaden ili fale paketi.
    echo Instaliraj: pip install -r scripts\requirements.txt
    exit /b 1
)

echo.
echo === 5/7 Tablice rezultata (Python) ===
python scripts\generate_results_tables.py
if errorlevel 1 exit /b 1

echo.
echo === 6/7 Dokumentacija za diplomski i ChatGPT ===
python scripts\generate_changelog_for_chatgpt.py
python scripts\generate_thesis_doc_10_80.py
if errorlevel 1 exit /b 1

echo.
echo === 7/7 ChatGPT zip prilozi ===
python scripts\generate_changelog_for_chatgpt.py
python scripts\generate_chatgpt_zip.py
if errorlevel 1 exit /b 1

echo.
echo Sve spremno:
echo   results\experiment_results.csv       - tablice rezultata (srednja vrijednost + sd)
echo   results\experiment_runs.csv          - svi pojedinacni rezultati po ponavljanju
echo   results\znacajnost.md                - upareni testovi znacajnosti
echo   results\tablice\                   - sve tablice (CSV, Excel, MD)
echo   results\analysis.md                  - tekstualna analiza
echo   results\novo_za_diplomski.md            - tekst novina za diplomski
echo   results\diplomski_dokument_10_80_za_chat.md - sazetak za ChatGPT
echo   results\chatgpt_prilozi.zip          - ZIP za slanje ChatGPT-u
echo   results\chatgpt_prompt_za_nadopunu.md - prompt za kopiranje
echo   results\grafovi_pregled.html         - vizualni pregled
echo   slike i videa\2026\diplomski-grafovi\ - PNG grafovi
pause
