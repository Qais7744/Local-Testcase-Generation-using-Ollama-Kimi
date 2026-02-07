# 🚀 BLAST Test Case Generator - Complete Setup Guide

## 📋 Table of Contents
1. [Quick Start (Recommended)](#quick-start)
2. [Manual Step-by-Step Setup](#manual-setup)
3. [Troubleshooting](#troubleshooting)
4. [Making It Run Always](#always-on)
5. [Common Commands](#commands)

---

## ⚡ Quick Start (Recommended)

### Step 1: Check if Ollama is Running

**In any terminal (Git Bash, PowerShell, or CMD):**
```bash
curl http://localhost:11434/api/tags
```

**If you see JSON output** → Ollama is running ✅  
**If connection error** → Start Ollama first (see Step 2)

### Step 2: Start Ollama (if not running)

**Git Bash:**
```bash
ollama serve
```

**Or in new terminal, just run:**
```bash
./START.bat
```

### Step 3: Open Browser
```
http://localhost:5000
```

---

## 🔧 Manual Step-by-Step Setup

### 1. Open Terminal

**Option A - Git Bash:**
```bash
# Right-click in folder → "Git Bash Here"
```

**Option B - PowerShell:**
```powershell
# Press Win + R, type "powershell", press Enter
cd "C:\Users\Hp\Downloads\AITesterBlueprint"
```

**Option C - CMD:**
```cmd
# Press Win + R, type "cmd", press Enter
cd "C:\Users\Hp\Downloads\AITesterBlueprint"
```

---

### 2. Check Ollama Status

**Git Bash:**
```bash
curl http://localhost:11434/api/tags
```

**PowerShell:**
```powershell
Invoke-RestMethod -Uri "http://localhost:11434/api/tags" -Method GET
```

**If you see error like:**
```
Failed to connect
```
→ Go to Step 3 to start Ollama

**If you see JSON with models:**
```json
{"models": [{"name": "llama3.2:latest"}]}
```
→ Skip to Step 4

---

### 3. Start Ollama Server

**Git Bash:**
```bash
ollama serve
```

**PowerShell:**
```powershell
ollama serve
```

**Note:** Keep this terminal window open! Minimize it if needed.

---

### 4. Start Web Server

**Open a NEW terminal (don't close Ollama terminal):**

**Git Bash:**
```bash
cd ~/Downloads/AITesterBlueprint
python deploy.py
```

**PowerShell:**
```powershell
cd "C:\Users\Hp\Downloads\AITesterBlueprint"
python deploy.py
```

**Or simply double-click:**
```
START.bat
```

---

### 5. Access the Application

Open your browser and go to:
```
http://localhost:5000
```

You should see the **Local Test Case Generator** interface!

---

## 🐛 Troubleshooting

### Problem 1: "Only one usage of each socket address"

**Error:**
```
Error: listen tcp 127.0.0.1:11434: bind: Only one usage...
```

**Solution:**
Ollama is already running. Just start the web server:
```bash
python deploy.py
```

---

### Problem 2: "pip is not recognized"

**Error:**
```
pip : The term 'pip' is not recognized
```

**Solution:**
```bash
python -m pip install -r requirements.txt
```

---

### Problem 3: "Module not found"

**Error:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
python -m pip install flask flask-cors waitress requests pytest
```

---

### Problem 4: Ollama is running but web server says "Ollama not available"

**Check:**
```bash
curl http://localhost:11434/api/tags
```

**If working:** Restart the Flask server

**If not working:** Kill and restart Ollama:

**Git Bash:**
```bash
taskkill //F //IM ollama.exe 2>/dev/null
ollama serve
```

**PowerShell:**
```powershell
Get-Process ollama | Stop-Process -Force
ollama serve
```

---

### Problem 5: Generation is slow

**Solutions:**

1. **Use a lighter model:**
```bash
ollama pull gemma3:1b
```

2. **Edit model in config:**
Open `blast_testgen/ollama_client.py` and change:
```python
DEFAULT_MODEL = "gemma3:1b"  # Instead of llama3.2
```

3. **Use simpler code examples** (shorter functions generate faster)

---

## 🔄 Making It Run Always

### Method 1: Simple Batch File

Double-click:
```
START.bat
```

This will:
1. Check Ollama
2. Install dependencies
3. Start the server
4. Show you the URL

---

### Method 2: Auto-Start on Windows Boot

**Step 1:** Run the setup script
```
Double-click: setup_autostart.bat
```

**Step 2:** Restart your computer

The server will now start automatically every time Windows boots!

---

### Method 3: Background Mode (No Window)

Double-click:
```
start_background.vbs
```

This runs the server silently in background.

**To stop:** Open Task Manager → Find "python.exe" → End Task

---

## 📚 Common Commands

### Check Ollama Models
```bash
ollama list
```

### Pull a New Model
```bash
ollama pull llama3.2
ollama pull gemma3:1b
```

### Check Server Health
```bash
curl http://localhost:5000/api/health
```

### Stop Ollama
**Git Bash:**
```bash
taskkill //F //IM ollama.exe
```

**PowerShell:**
```powershell
Get-Process ollama | Stop-Process -Force
```

### Stop Flask Server
Press `Ctrl + C` in the terminal where `deploy.py` is running.

---

## 🌐 Network Access (Other Devices)

If you want to access from phone or another computer:

### 1. Start with network access:
```bash
python deploy.py --host 0.0.0.0
```

### 2. Find your IP:
```bash
ipconfig
```

### 3. Access from other devices:
```
http://YOUR_IP:5000
```

Example:
```
http://192.168.1.100:5000
```

---

## 📝 Example Usage

### Test Case Generation Examples:

**Example 1: Simple Function**
```python
def add(a, b):
    return a + b
```

**Example 2: Login Function**
```python
def login(username, password):
    if not username or not password:
        raise ValueError("Required")
    return {"token": "abc123"}
```

**Example 3: Calculator**
```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```

Click **"Generate"** or press **Ctrl + Enter** to get:
- Manual test cases (TC_001, TC_002...)
- pytest automation code

---

## ✅ Quick Checklist

| Step | Command | Expected Result |
|------|---------|-----------------|
| 1 | `curl http://localhost:11434/api/tags` | JSON with models |
| 2 | `python deploy.py` | Server starts on port 5000 |
| 3 | Open browser → `http://localhost:5000` | See the web interface |
| 4 | Paste code → Click Generate | Test cases appear |

---

## 🆘 Still Having Issues?

1. **Check Python version:**
```bash
python --version
```
(Needs 3.8 or higher)

2. **Check all requirements:**
```bash
python -m pip list | grep -i flask
python -m pip list | grep -i ollama
```

3. **Restart everything:**
- Stop Ollama
- Stop Flask server
- Start Ollama fresh
- Start Flask server

---

**Ready to generate test cases!** 🚀
