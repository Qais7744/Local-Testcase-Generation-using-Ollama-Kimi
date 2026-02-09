# AI Tester Blueprint Projects

This repository contains AI-powered testing tools that run locally using Ollama (Local LLM).

---

## 📁 Projects

### 1. Project1-LocalTestCaseGenerator

**Description:** A local LLM-powered test case generator using **Ollama** and **Llama 3.2**. Generate comprehensive test cases from your Python code or feature descriptions without sending data to external APIs. Your code stays private! 🔒

**Key Features:**
- 🔒 **100% Local** - Uses Ollama, no data leaves your machine
- 🐍 **Python Code** - Generate tests from Python functions/classes
- 📝 **Feature Tests** - Generate from plain text descriptions
- 🌐 **Website Tests** - Generate Selenium tests for URLs
- 📋 **Dual Output** - Manual test cases + pytest automation code
- 🎨 **Web UI** - Beautiful chat interface
- ⌨️ **CLI** - Command-line interface

**Tech Stack:** Python, Flask, Ollama (Llama 3.2), pytest

**Location:** [`Project1-LocalTestCaseGenerator/`](./Project1-LocalTestCaseGenerator)

---

### 2. Project2-Selenium2playwrightLocalLLM

**Description:** A tool that uses a local LLM (**Ollama** with **Qwen2.5-Coder 1.5B**) to convert **Selenium Java** code to **Playwright** (TypeScript or JavaScript).

**Key Features:**
- 🔄 **Code Conversion** - Selenium Java → Playwright TS/JS
- 🏠 **Local & Private** - Runs entirely on your machine using Ollama
- ⚡ **Fast Conversion** - Powered by lightweight `qwen2.5-coder:1.5b` model
- 🎯 **Dual Language** - TypeScript (Strict Typing) or JavaScript (Standard JS)
- 🧹 **Clean Output** - Auto-filters Selenium dependencies, enforces Playwright best practices
- 🎨 **Modern UI** - Dark-themed interface with syntax highlighting and file saving

**Tech Stack:** Python, Flask, Ollama (Qwen2.5-Coder 1.5B), Playwright

**Location:** [`Project2-Selenium2playwrightLocalLLM/`](./Project2-Selenium2playwrightLocalLLM)

---

## 🚀 Quick Start

Each project has its own setup instructions. Navigate to the respective project folder and follow the README.md inside.

### Prerequisites (Common for both projects)
- Python 3.8+
- Ollama installed: [ollama.com](https://ollama.com)

---

## 📄 License

MIT License - Feel free to use and modify!

---

**Made with ❤️ using Local AI (Ollama)**
