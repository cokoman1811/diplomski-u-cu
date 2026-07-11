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
echo === 4/4 Tablice rezultata (Python) ===
python scripts\generate_results_tables.py
if errorlevel 1 exit /b 1

echo.
echo Sve spremno:
echo   results\experiment_results.csv       - tablice rezultata
echo   results\tablice\                   - sve tablice (CSV, Excel, MD)
echo   results\analysis.md                  - tekstualna analiza
echo   results\grafovi_pregled.html         - vizualni pregled (otvara se u pregledniku)
echo   slike i videa\2026\diplomski-grafovi\ - PNG grafovi
pause
