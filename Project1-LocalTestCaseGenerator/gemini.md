# Gemini.md - Project Constitution

## Data Schemas

### Input Schema
```json
{
  "source_file": "string - path to source code file",
  "code_content": "string - raw code content",
  "target_function": "string|null - specific function to test",
  "language": "string - programming language (default: python)"
}
```

### Output Schema
```json
{
  "test_file_path": "string - path to generated test file",
  "test_content": "string - generated test code",
  "functions_tested": ["array of function names"],
  "success": "boolean"
}
```

### Ollama Request Schema
```json
{
  "model": "llama3.2",
  "prompt": "string - formatted prompt with code context",
  "stream": false,
  "options": {
    "temperature": 0.2,
    "num_predict": 2048
  }
}
```

## Behavioral Rules

1. **Never execute untrusted code** - Generated tests must be reviewed
2. **Validate Ollama connection** before generation
3. **Preserve original code** - Never modify source files
4. **Idempotent generation** - Same input → same output

## Architectural Invariants

### 3-Layer A.N.T. Architecture
```
┌─────────────────────────────────────┐
│  UI Layer (CLI)                     │
│  - Argument parsing                 │
│  - File I/O                         │
│  - User feedback                    │
├─────────────────────────────────────┤
│  Logic Layer (Orchestrator)         │
│  - Code analysis                    │
│  - Prompt building                  │
│  - Response handling                │
├─────────────────────────────────────┤
│  Tool Layer (Ollama Client)         │
│  - HTTP API calls                   │
│  - Retry logic                      │
│  - Error handling                   │
└─────────────────────────────────────┘
```

## File Structure
```
project/
├── blast_testgen/          # Main package
│   ├── __init__.py
│   ├── cli.py              # CLI entry point
│   ├── web_app.py          # Flask Web UI
│   ├── orchestrator.py     # Business logic
│   ├── ollama_client.py    # Ollama API client
│   ├── code_parser.py      # Code analysis
│   ├── prompts.py          # Prompt templates
│   ├── templates/
│   │   └── chat.html       # Chat UI template
│   └── static/
│       ├── style.css       # UI styles
│       └── chat.js         # UI interactions
├── tests/
├── requirements.txt
├── run.py                  # CLI runner
└── run_web.py              # Web UI runner
```

## API Endpoints

### GET /api/health
Check Ollama connection status.

**Response:**
```json
{
  "status": "healthy",
  "ollama_connected": true,
  "model": "llama3.2",
  "available_models": ["llama3.2", "codellama"]
}
```

### POST /api/generate
Generate testcases from code.

**Request:**
```json
{
  "code": "def add(a, b): return a + b",
  "function": null
}
```

**Response:**
```json
{
  "success": true,
  "generated_tests": "import pytest...",
  "model_used": "llama3.2",
  "input_length": 25
}
```
