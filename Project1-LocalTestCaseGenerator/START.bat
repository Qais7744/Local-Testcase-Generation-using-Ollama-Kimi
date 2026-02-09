@echo off
chcp 65001 >nul
title BLAST Testcase Generator
cls

echo ============================================
echo    BLAST Testcase Generator - Server
echo ============================================
echo.

:: Check if Ollama is running
echo [1/3] Checking Ollama...
python -c "from blast_testgen.ollama_client import OllamaClient; c=OllamaClient(); exit(0 if c.is_available() else 1)" >nul 2>&1
if errorlevel 1 (
    echo     ❌ Ollama is NOT running!
    echo.
    echo     Please start Ollama first:
    echo         ollama serve
    echo.
    pause
    exit /b 1
)
echo     ✅ Ollama is running

:: Check dependencies
echo.
echo [2/3] Checking dependencies...
python -c "import flask, waitress" >nul 2>&1
if errorlevel 1 (
    echo     📦 Installing dependencies...
    python -m pip install -q -r requirements.txt
)
echo     ✅ Dependencies ready

:: Start server
echo.
echo [3/3] Starting server...
echo.
echo ============================================
echo  🌐 Open browser: http://localhost:5000
echo  ⏹️  Press Ctrl+C to stop
echo ============================================
echo.

python deploy.py --host 127.0.0.1 --port 5000

echo.
echo Server stopped.
pause
