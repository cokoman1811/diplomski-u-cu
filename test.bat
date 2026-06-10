@echo off
cd /d "%~dp0"

if not exist tests.exe (
    call build.bat
    if errorlevel 1 exit /b 1
)

tests.exe %*
