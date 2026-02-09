# Selenium to Playwright Conversion Tool

This tool uses a local LLM (**Ollama** with **Qwen2.5-Coder 1.5B**) to convert Selenium Java code to **Playwright** (TypeScript or JavaScript).

## Features
-   **Local & Private**: Runs entirely on your machine using Ollama.
-   **Fast Conversion**: Powered by the lightweight `qwen2.5-coder:1.5b` model.
-   **Dual Language Support**: Choose between **TypeScript** (Strict Typing) and **JavaScript** (Standard JS).
-   **Clean Output**: Automatically filters out Selenium dependencies and enforces Playwright best practices.
-   **Modern UI**: Dark-themed interface with syntax highlighting and file saving.

## Prerequisites

1.  **Python 3.8+**: Ensure Python is installed.
2.  **Ollama**: Download and install from [ollama.com](https://ollama.com).
3.  **Active Internet Connection**: Required for initial model download.

## Setup Instructions

### 1. Install Dependencies
Open a terminal in this directory and run:
```bash
pip install -r requirements.txt
```

### 2. Setup AI Model
Ensure Ollama is running, then pull the model:
```bash
ollama pull qwen2.5-coder:1.5b
```

### 3. Run the Application
Start the Flask backend:
```bash
python tools/app.py
```
You should see output indicating the server is running on `http://localhost:5000`.

### 4. Access the UI
Open your web browser and navigate to:
[http://localhost:5000](http://localhost:5000)

## Usage
1.  **Select Language**: Choose **TypeScript** or **JavaScript** from the dropdown menu.
2.  **Input Code**: Paste your **Selenium Java** code into the left text area.
3.  **Convert**: Click **"Initialize Conversion"**.
4.  **Save**: Review the output and click the **Save** icon to download the file.
