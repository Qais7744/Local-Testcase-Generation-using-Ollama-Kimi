# 🧪 Local Test Case Generator

> **AI-Powered Test Case Generation using Local LLMs (Ollama + Llama 3.2)**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-orange.svg)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Generate comprehensive test cases from Python code or feature descriptions **without sending data to external APIs**. Your code stays private and secure! 🔒

<p align="center">
  <img src="https://img.shields.io/badge/Manual%20Test%20Cases-✓-brightgreen" alt="Manual Test Cases">
  <img src="https://img.shields.io/badge/pytest%20Automation-✓-blue" alt="pytest Automation">
  <img src="https://img.shields.io/badge/100%25%20Local-✓-purple" alt="100% Local">
</p>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [▶️ Usage](#-usage)
- [🏗️ System Architecture](#️-system-architecture)
- [📁 Project Structure](#-project-structure)
- [🔧 Configuration](#-configuration)
- [🐛 Troubleshooting](#-troubleshooting)
- [📄 License](#-license)

---

## ✨ Features

### 🎯 Core Capabilities

| Feature | Input | Output | Speed |
|---------|-------|--------|-------|
| **🐍 Python Code Testing** | `def add(a, b): return a+b` | Manual + pytest | ⚡ Instant |
| **📝 Feature Testing** | "Login with email, password" | Test scenarios | ⚡ Instant |
| **🌐 Website Testing** | "google.com" | UI test cases | ⚡ Instant |
| **🔒 100% Private** | Local processing | No cloud | 🛡️ Secure |

---

## 🚀 Quick Start

### One-Command Start (Windows)
```powershell
cd Project1-LocalTestCaseGenerator
.\START.bat
```

### Manual Start
```powershell
# Terminal 1 - Start Ollama
ollama serve

# Terminal 2 - Start Web Server
cd Project1-LocalTestCaseGenerator
python deploy.py
```

### Access the App
Open browser: **http://localhost:5000**

---

## 📦 Installation

### Prerequisites

| Requirement | Version | Install Command |
|------------|---------|-----------------|
| Python | 3.8+ | [Download](https://python.org/downloads) |
| Ollama | Latest | [Download](https://ollama.com/download) |
| Llama 3.2 | latest | `ollama pull llama3.2` |

### Step-by-Step Setup

```powershell
# 1. Clone the repository
git clone https://github.com/Qais7744/Local-Testcase-Generation-using-Ollama-Kimi.git
cd Local-Testcase-Generation-using-Ollama-Kimi

# 2. Navigate to project
cd Project1-LocalTestCaseGenerator

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Pull the LLM model (one-time)
ollama pull llama3.2

# 5. Start the application
.\START.bat
```

---

## ▶️ Usage

### 🌐 Web Interface

1. **Open** http://localhost:5000 in your browser
2. **Select Input Type:**
   - 🐍 **Python Code** - Paste function/class code
   - 📝 **Feature Description** - Write plain text requirements
   - 🌐 **Website URL** - Enter domain (e.g., `google.com`)
3. **Click** "Generate" or press `Ctrl + Enter`
4. **View Results:**
   - 📋 Manual Test Cases (TC_001, TC_002...)
   - 🧪 pytest Automation Code

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CLIENT LAYER                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                      │
│  │   Web UI     │  │   CLI Tool   │  │  API Client  │                      │
│  │  (Browser)   │  │  (Terminal)  │  │   (Code)     │                      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                      │
└─────────┼─────────────────┼─────────────────┼───────────────────────────────┘
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          API LAYER (Flask)                                  │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │  Routes                    Controllers               Middleware       │ │
│  │  GET  /                    render_template()       CORS               │ │
│  │  GET  /api/health          health_check()          Error Handler      │ │
│  │  POST /api/generate        generate_tests()        Request Validator  │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       BUSINESS LOGIC LAYER                                  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │   Input Router  │  │  Test Generator │  │  Output Parser  │             │
│  │  detect_type()  │  │  build_tests()  │  │  parse_json()   │             │
│  └────────┬────────┘  └────────┬────────┘  └─────────────────┘             │
│           │                    │                                            │
│           └────────────────────┘                                            │
│                            │                                                │
└────────────────────────────┼────────────────────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      INFRASTRUCTURE LAYER                                   │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │  Ollama Client  │  │  Code Parser    │  │  Prompt Builder │             │
│  │  ─────────────  │  │  ────────────   │  │  ─────────────  │             │
│  │  generate()     │  │  parse_python() │  │  build_prompt() │             │
│  └────────┬────────┘  └─────────────────┘  └─────────────────┘             │
│           │                                                                 │
└───────────┼─────────────────────────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         LLM LAYER (Local)                                   │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                                                                       │ │
│  │    ┌───────────────┐          ┌───────────────┐                      │ │
│  │    │   Ollama      │◄────────►│  Llama 3.2    │                      │ │
│  │    │   Server      │          │    Model      │                      │ │
│  │    │   :11434      │          │               │                      │ │
│  │    └───────────────┘          └───────────────┘                      │ │
│  │                                                                       │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
Project1-LocalTestCaseGenerator/
│
├── 📄 README.md                 # Project documentation
├── 📄 requirements.txt          # Python dependencies
├── 📄 SETUP_GUIDE.md           # Detailed setup instructions
├── 📄 DEPLOYMENT.md            # Production deployment guide
├── 📄 BLAST.md                 # B.L.A.S.T. protocol documentation
├── 📄 LICENSE                  # MIT License
│
├── 🚀 Quick Start Scripts
│   ├── START.bat               # One-click Windows start
│   ├── start_server.bat        # Server starter
│   ├── start_background.vbs    # Background mode (no window)
│   └── setup_autostart.bat     # Windows boot setup
│
├── 📦 Main Package (blast_testgen/)
│   ├── web_app.py              # Flask web application
│   ├── ollama_client.py        # Ollama LLM client
│   ├── orchestrator.py         # Business logic orchestrator
│   ├── code_parser.py          # Python code analyzer
│   ├── prompts.py              # LLM prompt templates
│   ├── cli.py                  # Command-line interface
│   │
│   ├── 🎨 static/              # CSS, JS assets
│   │   ├── style.css
│   │   └── chat.js
│   │
│   └── 🖼️ templates/           # HTML templates
│       └── chat.html
│
├── 🛠️ Tools (tools/)
│   ├── verify_ollama.py        # Ollama connection checker
│   ├── generate_tests.py       # Standalone test generator
│   └── validate_code.py        # Code validation utility
│
├── 📋 Architecture (architecture/)
│   ├── SOP-001-TestGeneration.md
│   ├── SOP-002-CodeValidation.md
│   └── SOP-003-OllamaIntegration.md
│
├── ⚛️ Frontend (frontend/)
│   ├── src/
│   │   ├── components/         # React components
│   │   ├── pages/              # Page components
│   │   └── services/           # API services
│   └── public/
│
├── 🧪 Tests (tests/)           # Sample test files
├── 🔧 Configs
│   ├── deploy.py               # Production server
│   ├── run_web.py              # Development server
│   └── run.py                  # Simple runner
│
└── 📁 .tmp/                    # Temporary files
```

---

## 🔧 Configuration

### Custom Port
```powershell
# Run on port 8080
python deploy.py --port 8080
```

### Network Access
```powershell
# Allow access from other devices
python deploy.py --host 0.0.0.0
```

### Change Model
Edit `blast_testgen/ollama_client.py`:
```python
DEFAULT_MODEL = "gemma3:1b"  # Lighter/faster model
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `Ollama not available` | Run `ollama serve` |
| `Module not found` | Run `pip install -r requirements.txt` |
| `Port 5000 in use` | Kill process or use different port |
| `Model not found` | Run `ollama pull llama3.2` |

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](Project1-LocalTestCaseGenerator/LICENSE) file for details.

---

<p align="center">
  <b>Made with ❤️ using Local AI</b><br>
  <sub>Keep your code private. Test smarter. 🚀</sub>
</p>

---

## 📞 Support

- 📧 **Issues:** [GitHub Issues](https://github.com/Qais7744/Local-Testcase-Generation-using-Ollama-Kimi/issues)
- 📖 **Documentation:** Check `Project1-LocalTestCaseGenerator/SETUP_GUIDE.md`
