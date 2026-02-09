# 🚀 Project1 - Local Test Case Generator (Ollama + Llama 3.2)

> **File:** `README.md` | **Project:** Local TestCase Generator via Ollama

A **local LLM-powered** test case generator using **Ollama** and **Llama 3.2**. Generate comprehensive test cases from your Python code or feature descriptions without sending data to external APIs. Your code stays private! 🔒

---

## 📋 Table of Contents
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [How to Run (Start Server)](#-how-to-run-start-server)
- [How to Stop (Kill Server)](#-how-to-stop-kill-server)
- [Usage](#-usage)
- [API Examples](#-api-examples)
- [Project Structure](#-project-structure)
- [Troubleshooting](#-troubleshooting)

---

## ✅ Prerequisites

Before running this project, ensure you have:

| Requirement | Version | Check Command |
|------------|---------|---------------|
| Python | 3.8+ | `python --version` |
| Ollama | Latest | [Download from ollama.com](https://ollama.com) |
| Llama 3.2 Model | latest | `ollama pull llama3.2` |

### Verify Ollama is Running
```powershell
# Check if Ollama server is running
python -c "import requests; print(requests.get('http://localhost:11434/api/tags').status_code)"
# Expected output: 200
```

---

## 📦 Installation

### Step 1: Navigate to Project Directory
```powershell
cd Project1-LocalTestCaseGenerator
```

### Step 2: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 3: Pull Required Model (One-time)
```powershell
ollama pull llama3.2
```

---

## ▶️ How to Run (Start Server)

### Method 1: Using Batch File (Windows - Recommended)
```powershell
.\START.bat
```
This will:
1. ✅ Check if Ollama is running
2. ✅ Install dependencies if missing
3. ✅ Start Flask server on `http://localhost:5000`

### Method 2: Manual Start
```powershell
# Terminal 1 - Start Ollama (if not running)
ollama serve

# Terminal 2 - Start Flask Server
python deploy.py --host 127.0.0.1 --port 5000
```

### Method 3: Development Mode (Auto-reload)
```powershell
python run_web.py
```

### Verify Server is Running
Open browser and go to: **http://localhost:5000**

Or use curl/PowerShell:
```powershell
python -c "import requests; print(requests.get('http://127.0.0.1:5000/api/health').json())"
```

---

## ⏹️ How to Stop (Kill Server)

### Method 1: Terminal Mein (Recommended)
Jis terminal mein server chal raha hai, wahan press karo:
```
Ctrl + C
```

### Method 2: PowerShell Se (Port 5000 Band Karo)
```powershell
# Find and kill process on port 5000
$port = 5000
$proc = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
if ($proc) { taskkill /F /PID $proc }
```

### Method 3: Task Manager Se
1. `Ctrl + Shift + Esc` dabao
2. "Details" tab pe jao
3. `python.exe` dhoondo
4. Right click → "End Task"

### Method 4: Command Prompt Se
```cmd
# Find PID using port 5000
netstat -ano | findstr :5000

# Kill using PID (replace 1234 with actual PID)
taskkill /F /PID 1234
```

---

## 📝 Usage

### Web Interface
1. Browser khol: http://localhost:5000
2. Input type select karo:
   - 🐍 **Python Code** - Function ya class paste karo
   - 📝 **Feature Description** - Plain text mein feature likho
   - 🌐 **Website URL** - Example: `google.com`
3. "Generate" button dabao
4. Output dekho:
   - 📋 Manual Test Cases
   - 🧪 pytest Automation Code

---

## 🔌 API Examples

### Health Check
```powershell
python -c "
import requests
r = requests.get('http://127.0.0.1:5000/api/health')
print(r.json())
"
```

### Generate Tests from Python Code
```powershell
python -c "
import requests
import json

payload = {
    'code': '''def login(username, password):
    if not username or not password:
        raise ValueError(\"Required\")
    return {\"token\": \"abc123\"}'''
}

r = requests.post('http://127.0.0.1:5000/api/generate', json=payload)
result = r.json()
print('Manual Tests:', result.get('manual_tests'))
print('Pytest Code:', result.get('pytest_code'))
"
```

### Generate Tests from Feature Description
```powershell
python -c "
import requests

payload = {
    'code': 'Registration page with email, password, confirm password fields'
}

r = requests.post('http://127.0.0.1:5000/api/generate', json=payload)
print(r.json())
"
```

### Generate Tests from Website URL
```powershell
python -c "
import requests

payload = {
    'code': 'app.vwo.com'
}

r = requests.post('http://127.0.0.1:5000/api/generate', json=payload)
print(r.json())
"
```

---

## 📁 Project Structure

```
Project1-LocalTestCaseGenerator/
│
├── 📄 README.md              # This file
├── 📄 requirements.txt       # Python dependencies
├── 📄 START.bat             # One-click server start (Windows)
│
├── 📁 blast_testgen/        # Main Python package
│   ├── 📁 static/           # CSS, JS files
│   │   ├── style.css
│   │   └── chat.js
│   ├── 📁 templates/        # HTML templates
│   │   └── chat.html
│   ├── cli.py              # Command-line interface
│   ├── web_app.py          # Flask web server
│   ├── ollama_client.py    # Ollama API client
│   ├── orchestrator.py     # Business logic
│   ├── code_parser.py      # Python code analysis
│   └── prompts.py          # LLM prompt templates
│
├── 📁 tools/                # Utility scripts
│   ├── verify_ollama.py    # Connection checker
│   ├── generate_tests.py   # Standalone generator
│   └── validate_code.py    # Code validator
│
├── 📁 architecture/         # SOP documentation
│   ├── SOP-001-TestGeneration.md
│   ├── SOP-002-CodeValidation.md
│   └── SOP-003-OllamaIntegration.md
│
└── 📁 tests/                # Sample test files
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Ollama not running" | Run `ollama serve` in terminal |
| "Module not found" | Run `pip install -r requirements.txt` |
| "Port 5000 already in use" | Kill existing server: `taskkill /F /IM python.exe` |
| "Request timed out" | Use shorter input or simpler code |
| "Model not found" | Run `ollama pull llama3.2` |
| Slow generation | Input is too complex, try shorter code |

---

## 🤝 Contributing

This project follows the **B.L.A.S.T.** protocol:
- **B** - Blueprint (Planning)
- **L** - Link (Connectivity)
- **A** - Architect (3-layer build)
- **S** - Stylize (Refinement)
- **T** - Trigger (Deployment)

---

## 📄 License

MIT License - Feel free to use and modify!

---

**Made with ❤️ using Local AI (Ollama + Llama 3.2)**
