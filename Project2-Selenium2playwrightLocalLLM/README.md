# 🔄 Project2 - Selenium to Playwright Converter (Ollama + Qwen2.5-Coder)

> **File:** `README.md` | **Project:** Selenium Java to Playwright Converter

This tool uses a local LLM (**Ollama** with **Qwen2.5-Coder 1.5B**) to convert **Selenium Java** code to **Playwright** (TypeScript or JavaScript). Runs entirely on your machine - no data leaves your computer! 🔒

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
| Qwen2.5-Coder Model | 1.5b | `ollama pull qwen2.5-coder:1.5b` |

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
cd Project2-Selenium2playwrightLocalLLM
```

### Step 2: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 3: Pull Required Model (One-time)
```powershell
ollama pull qwen2.5-coder:1.5b
```

---

## ▶️ How to Run (Start Server)

### Method 1: Direct Python (Recommended)
```powershell
cd tools
python app.py
```
Server will start on: **http://localhost:5000**

### Method 2: From Project Root
```powershell
python tools/app.py
```

### Method 3: With Custom Port
```powershell
cd tools
python app.py
# Edit last line in app.py to change port: app.run(debug=True, port=8080)
```

### Verify Server is Running
Open browser and go to: **http://localhost:5000**

Or use PowerShell:
```powershell
python -c "import requests; print(requests.get('http://127.0.0.1:5000').status_code)"
# Expected output: 200
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

### Method 5: All Python Processes Kill Karo (⚠️ Caution)
```powershell
taskkill /F /IM python.exe
```

---

## 📝 Usage

### Web Interface
1. Browser khol: http://localhost:5000
2. **Language Select** karo:
   - TypeScript (with strict typing)
   - JavaScript (standard JS)
3. **Selenium Java Code** paste karo left side mein
4. **"Initialize Conversion"** button dabao
5. Converted **Playwright Code** right side mein dekho
6. **Save** button se file download karo

### Example Input (Selenium Java)
```java
WebDriver driver = new ChromeDriver();
driver.get("https://example.com");
WebElement element = driver.findElement(By.id("username"));
element.sendKeys("testuser");
element.submit();
```

### Example Output (Playwright TypeScript)
```typescript
import { test, expect } from '@playwright/test';

test('login test', async ({ page }) => {
  await page.goto('https://example.com');
  await page.fill('#username', 'testuser');
  await page.click('button[type="submit"]');
});
```

---

## 🔌 API Examples

### Convert Code via API
```powershell
python -c "
import requests
import json

payload = {
    'source_code': '''WebDriver driver = new ChromeDriver();
driver.get(\"https://example.com\");
WebElement element = driver.findElement(By.id(\"username\"));
element.sendKeys(\"testuser\");''',
    'language': 'typescript'  # or 'javascript'
}

r = requests.post('http://127.0.0.1:5000/convert', json=payload)
result = r.json()
print('Status:', result.get('status'))
print('Converted Code:', result.get('converted_code'))
"
```

### Save Converted Code
```powershell
python -c "
import requests

payload = {
    'converted_code': '''import { test } from '@playwright/test';
test(\"example\", async ({ page }) => {
  await page.goto(\"https://example.com\");
});''',
    'filename': 'test.spec.ts'
}

r = requests.post('http://127.0.0.1:5000/save', json=payload)
print(r.json())
"
```

---

## 📁 Project Structure

```
Project2-Selenium2playwrightLocalLLM/
│
├── 📄 README.md              # This file
├── 📄 requirements.txt       # Python dependencies
├── 📄 .gitignore            # Git ignore rules
│
├── 📁 tools/                # Backend code
│   ├── app.py              # Flask web server
│   ├── converter_engine.py # LLM conversion logic
│   └── llm_handshake.py    # Ollama client
│
├── 📁 templates/            # HTML templates
│   └── index.html          # Main UI
│
├── 📁 static/               # CSS, JS files
│   └── style.css           # UI styling
│
├── 📁 generated/            # Saved conversions
│   └── (converted files saved here)
│
└── 📁 architecture/         # Documentation
    └── conversion_sop.md   # Conversion guidelines
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Ollama not running" | Run `ollama serve` in terminal |
| "Module not found" | Run `pip install -r requirements.txt` |
| "Port 5000 already in use" | Kill existing server or change port in `app.py` |
| "Model not found" | Run `ollama pull qwen2.5-coder:1.5b` |
| Conversion is slow | Normal hai, LLM processing chal raha hai |
| Output quality poor | Try breaking large files into smaller chunks |

---

## 🎯 Features

| Feature | Description |
|---------|-------------|
| 🏠 **100% Local** | No data sent to cloud |
| ⚡ **Fast** | Uses lightweight 1.5B model |
| 🎯 **Dual Language** | TypeScript & JavaScript support |
| 🧹 **Clean Output** | Auto-removes Selenium dependencies |
| 🎨 **Modern UI** | Dark theme with syntax highlighting |
| 💾 **Save Feature** | Download converted files |

---

## 📄 License

MIT License - Feel free to use and modify!

---

**Made with ❤️ using Local AI (Ollama + Qwen2.5-Coder)**
