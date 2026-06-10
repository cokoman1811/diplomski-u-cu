@echo off
cd /d "%~dp0"

set "GCC=gcc"
where gcc >nul 2>nul
if errorlevel 1 (
    for /d %%D in ("%LOCALAPPDATA%\Microsoft\WinGet\Packages\BrechtSanders.WinLibs.POSIX.UCRT_*") do (
        if exist "%%D\mingw64\bin\gcc.exe" set "GCC=%%D\mingw64\bin\gcc.exe"
    )
)
if /i "%GCC%"=="gcc" where gcc >nul 2>nul
if errorlevel 1 if not exist "%GCC%" (
    echo gcc nije pronaden. Instaliraj MinGW-w64 ili dodaj gcc u PATH.
    echo Npr.: winget install -e --id BrechtSanders.WinLibs.POSIX.UCRT
    exit /b 1
)

if not exist build mkdir build

echo Kompajliram diplomski.exe...
"%GCC%" -std=c99 -O2 -Wall -Wextra -Isrc src\*.c -o diplomski.exe -lm
if errorlevel 1 (
    echo Greska pri kompajliranju diplomski.exe.
    exit /b 1
)

echo Kompajliram tests.exe...
"%GCC%" -std=c99 -O2 -Wall -Wextra -Isrc tests\run_tests.c src\dataset.c src\evaluation.c src\interpolation.c src\knn_methods.c src\preprocessing.c -o tests.exe -lm
if errorlevel 1 (
    echo Greska pri kompajliranju tests.exe.
    exit /b 1
)

echo Gotovo: diplomski.exe, tests.exe
