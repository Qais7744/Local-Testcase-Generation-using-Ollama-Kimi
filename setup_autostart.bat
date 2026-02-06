@echo off
echo ==========================================
echo   BLAST Auto-Start Setup
echo ==========================================
echo.

:: Get the current directory
set "SCRIPT_DIR=%~dp0"
set "VBS_PATH=%SCRIPT_DIR%start_background.vbs"
set "STARTUP_DIR=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

echo [1/3] Checking files...
if not exist "%VBS_PATH%" (
    echo [ERROR] start_background.vbs not found!
    pause
    exit /b 1
)
echo     ✓ Found start_background.vbs

echo.
echo [2/3] Creating shortcut...
echo     Source: %VBS_PATH%
echo     Target: %STARTUP_DIR%\BLAST-Server.lnk

:: Create shortcut using PowerShell
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%STARTUP_DIR%\BLAST-Server.lnk'); $Shortcut.TargetPath = '%VBS_PATH%'; $Shortcut.WorkingDirectory = '%SCRIPT_DIR%'; $Shortcut.IconLocation = '%SystemRoot%\System32\SHELL32.dll,14'; $Shortcut.Save()"

echo     ✓ Shortcut created

echo.
echo [3/3] Verifying setup...
if exist "%STARTUP_DIR%\BLAST-Server.lnk" (
    echo     ✓ Auto-start configured successfully!
    echo.
    echo ==========================================
    echo The BLAST server will now start
    echo automatically when Windows boots.
    echo.
    echo To start now: double-click start_background.vbs
    echo To remove: delete from Startup folder
    echo ==========================================
) else (
    echo     ✗ Failed to create shortcut
)

echo.
pause
