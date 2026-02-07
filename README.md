# 🚀 AI-Tester-BluePrint-Projects

A comprehensive collection of AI-powered testing tools and automation frameworks. This repository serves as a centralized hub for various testing utilities built with modern AI technologies.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Qais7744/AI-Tester-BluePrint-Projects)](https://github.com/Qais7744/AI-Tester-BluePrint-Projects)

---

## 📚 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
- [Repository Structure](#repository-structure)
- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)

---

## 🎯 Overview

This repository contains multiple testing automation projects that leverage AI technologies like Local LLMs (Ollama), Machine Learning, and intelligent test generation algorithms. Each project is designed to solve specific testing challenges while maintaining privacy and efficiency.

### Key Features Across Projects:

- 🔒 **100% Local AI** - No data sent to external APIs
- 🤖 **LLM-Powered** - Uses Ollama with models like Llama 3.2
- 📝 **Auto Test Generation** - Generate test cases from code/descriptions
- 🧪 **pytest Integration** - Complete automation code generation
- 🌐 **Web UI** - Modern React/Material-UI interfaces
- ⚡ **Fast & Efficient** - Optimized for local execution

---

## 📁 Projects

### Project 1: Local Test Case Generator via Ollama with Kimi

**Location:** `Project1-LocalTestCaseGenerator/`

A local LLM-powered test case generator using Ollama and Llama 3.2. Generate comprehensive test cases from Python code or feature descriptions without sending data to external APIs.

#### Features:
- ✅ **Dual Output** - Manual test cases + pytest code
- ✅ **Multiple Input Types** - Python code, feature text, website URLs
- ✅ **Modern Web UI** - React + Material-UI interface
- ✅ **Flask Backend** - RESTful API architecture
- ✅ **3-Layer Architecture** - BLAST Protocol (Blueprint, Link, Architect, Stylize, Trigger)

#### Tech Stack:
- **Backend:** Python, Flask, Ollama
- **Frontend:** React, Material-UI, PrismJS
- **AI Model:** Llama 3.2 (3.2B parameters)
- **Architecture:** A.N.T. 3-Layer (Architecture, Navigation, Tools)

[📖 Read Project 1 Documentation](Project1-LocalTestCaseGenerator/README.md)

---

### Project 2: (Coming Soon)

**Status:** 🚧 In Planning

Future project placeholder for additional testing tools.

**Ideas:**
- API Testing Automation
- UI Testing with Computer Vision
- Test Data Generator
- Performance Testing Suite

---

## 🗂️ Repository Structure

```
AI-Tester-BluePrint-Projects/
│
├── 📁 Project1-LocalTestCaseGenerator/     # Current Project
│   ├── 📁 blast_testgen/                   # Main Python package
│   │   ├── 📁 static/                      # CSS, JS files
│   │   ├── 📁 templates/                   # HTML templates
│   │   ├── cli.py                          # CLI interface
│   │   ├── web_app.py                      # Flask web server
│   │   ├── ollama_client.py                # Ollama API client
│   │   └── ...
│   ├── 📁 frontend/                        # React frontend
│   │   ├── 📁 src/
│   │   │   ├── 📁 components/              # React components
│   │   │   ├── 📁 pages/                   # Page components
│   │   │   └── ...
│   │   └── package.json
│   ├── 📁 architecture/                    # SOPs & Documentation
│   ├── 📁 tools/                           # Utility scripts
│   ├── 📁 tests/                           # Sample tests
│   ├── deploy.py                           # Production server
│   ├── requirements.txt                    # Python dependencies
│   └── README.md                           # Project 1 Docs
│
├── 📄 .gitignore                           # Git ignore rules
├── 📄 README.md                            # This file
└── 📄 LICENSE                              # MIT License
```

---

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/Qais7744/AI-Tester-BluePrint-Projects.git
cd AI-Tester-BluePrint-Projects
```

### 2. Navigate to Desired Project

```bash
cd Project1-LocalTestCaseGenerator
```

### 3. Setup & Run

Follow the specific project README for detailed setup instructions.

**Quick Start for Project 1:**
```bash
# Install dependencies
pip install -r requirements.txt

# Start Ollama (in separate terminal)
ollama serve

# Start the application
python deploy.py

# Open browser
http://localhost:5000
```

---

## 📋 Prerequisites

### System Requirements:
- **OS:** Windows 10/11, Linux, macOS
- **Python:** 3.8 or higher
- **Node.js:** 16+ (for React frontend - optional)
- **RAM:** 8GB minimum, 16GB recommended
- **GPU:** Optional (for faster LLM inference)

### Required Software:
1. **Python 3.8+** - [Download](https://python.org)
2. **Ollama** - [Download](https://ollama.com)
3. **Git** - [Download](https://git-scm.com)

### AI Models:
Pull required models via Ollama:
```bash
ollama pull llama3.2
ollama pull gemma3:1b  # Optional - lighter model
```

---

## 🔧 Installation

### Step 1: Install Ollama
```bash
# Download from https://ollama.com
# Or use command line:
curl -fsSL https://ollama.com/install.sh | sh
```

### Step 2: Pull AI Models
```bash
ollama pull llama3.2
```

### Step 3: Install Python Dependencies
```bash
cd Project1-LocalTestCaseGenerator
pip install -r requirements.txt
```

### Step 4: (Optional) Setup React Frontend
```bash
cd Project1-LocalTestCaseGenerator/frontend
npm install
npm run build
cd ..
```

---

## 💻 Usage

### Running Project 1

#### Option A: Production Mode
```bash
cd Project1-LocalTestCaseGenerator
python deploy.py
```

#### Option B: Development Mode
```bash
# Terminal 1 - Start Ollama
ollama serve

# Terminal 2 - Start Flask
python run_web.py --debug
```

#### Option C: Using Batch Script (Windows)
```bash
START.bat
```

### Access Application
- **Web UI:** http://localhost:5000
- **API Health:** http://localhost:5000/api/health

---

## 🏗️ Architecture

### BLAST Protocol

All projects in this repository follow the **B.L.A.S.T.** development protocol:

| Phase | Description | Status |
|-------|-------------|--------|
| **B** - Blueprint | Vision & Logic Planning | ✅ Complete |
| **L** - Link | Connectivity & Integration | ✅ Complete |
| **A** - Architect | 3-Layer Build | ✅ Complete |
| **S** - Stylize | Refinement & UI | ✅ Complete |
| **T** - Trigger | Deployment | ✅ Complete |

### A.N.T. 3-Layer Architecture

```
┌─────────────────────────────────────┐
│  UI Layer (Presentation)            │
│  - React / Flask Templates          │
│  - User Interface                   │
├─────────────────────────────────────┤
│  Logic Layer (Navigation)           │
│  - Orchestrator                     │
│  - Code Parser                      │
│  - Prompt Templates                 │
├─────────────────────────────────────┤
│  Tool Layer (External)              │
│  - Ollama Client                    │
│  - LLM Integration                  │
└─────────────────────────────────────┘
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute:
- 🐛 Report bugs via GitHub Issues
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit pull requests
- 🧪 Add test cases

### Contribution Guidelines:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 🗺️ Roadmap

### Q1 2026
- [x] Project 1: Local Test Case Generator
- [ ] Project 2: API Testing Automation (Planned)
- [ ] Enhanced Documentation

### Q2 2026
- [ ] Project 3: UI Testing with Computer Vision
- [ ] Docker Support
- [ ] CI/CD Integration

### Q3 2026
- [ ] Project 4: Performance Testing Suite
- [ ] Multi-language Support
- [ ] Cloud Deployment Options

---

## 📊 Stats

![GitHub Repo Stats](https://github-readme-stats.vercel.app/api?username=Qais7744&show_icons=true&theme=dark)

---

## 🙏 Acknowledgments

- **Ollama** - Local LLM runtime
- **Meta AI** - Llama 3.2 model
- **React Team** - Frontend framework
- **Flask Team** - Backend framework
- **Material-UI** - UI components

---

## 📞 Support

### Getting Help:
- 📖 [Setup Guide](Project1-LocalTestCaseGenerator/SETUP_GUIDE.md)
- 🐛 [GitHub Issues](https://github.com/Qais7744/AI-Tester-BluePrint-Projects/issues)
- 💬 Discussions (coming soon)

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

## ⭐ Star History

If you find this project useful, please consider giving it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=Qais7744/AI-Tester-BluePrint-Projects&type=Date)](https://star-history.com/#Qais7744/AI-Tester-BluePrint-Projects&Date)

---

**Made with ❤️ and AI (Ollama + Llama 3.2)**

[🔝 Back to Top](#ai-tester-blueprint-projects)
