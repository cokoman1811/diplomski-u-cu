@echo off
cd /d "%~dp0"

echo === 1/3 Build ===
call build.bat
if errorlevel 1 exit /b 1

echo.
echo === 2/3 Eksperiment (CSV rezultati) ===
if not exist diplomski.exe (
    echo Greska: diplomski.exe ne postoji.
    exit /b 1
)
diplomski.exe --experiment-all --source jena_quick
if errorlevel 1 exit /b 1

echo.
echo === 3/3 Grafovi i analiza (Python) ===
python scripts\report.py
if errorlevel 1 (
    echo.
    echo Python nije pronaden ili fale paketi.
    echo Instaliraj: pip install -r scripts\requirements.txt
    exit /b 1
)

echo.
echo Sve spremno:
echo   results\experiment_results.csv       - tablice rezultata
echo   results\analysis.md                  - tekstualna analiza
echo   results\grafovi_pregled.html         - vizualni pregled (otvara se u pregledniku)
echo   slike i videa\2026\diplomski-grafovi\ - PNG grafovi
pause
