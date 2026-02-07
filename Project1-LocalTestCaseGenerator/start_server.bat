@echo off
echo ==========================================
echo   BLAST Testcase Generator - Server
echo ==========================================
echo.

:: Change to script directory
cd /d "%~dp0"

:: Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found! Please install Python 3.8+
    pause
    exit /b 1
)

:: Install/update dependencies
echo [1/3] Checking dependencies...
python -m pip install -q -r requirements.txt

:: Check Ollama
echo [2/3] Checking Ollama connection...
python -c "from blast_testgen.ollama_client import OllamaClient; c = OllamaClient(); print('    Ollama: ' + ('✓ Running' if c.is_available() else '✗ Not running'))" 2>nul

echo.
echo [3/3] Starting server...
echo ------------------------------------------
echo URL: http://localhost:5000
echo     http://127.0.0.1:5000
echo.
echo To access from other devices on network:
echo     http://%COMPUTERNAME%:5000
echo     http://%COMPUTERNAME%.local:5000
echo ------------------------------------------
echo Press Ctrl+C to stop
echo.

:: Start the server
python deploy.py --host 0.0.0.0 --port 5000

pause
