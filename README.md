# BLAST Test Generator

A local LLM-powered test case generator using Ollama. Generate pytest test cases from your Python code without sending data to external APIs.

## Features

- 🔒 **100% Local** - Uses Ollama, no data leaves your machine
- 🐍 **Python-focused** - Optimized for Python code and pytest
- ⚡ **Fast** - Leverages local GPU/CPU for generation
- 📝 **Comprehensive** - Generates normal, edge case, and error tests
- 📦 **Simple** - Easy CLI interface

## Prerequisites

1. **Python 3.8+**
2. **Ollama** installed and running: [ollama.com](https://ollama.com)
3. **Code Llama** model (or any code-capable model):
   ```bash
   ollama pull codellama
   ```

## Installation

```bash
# Clone or download this project
cd blast_testgen

# Install dependencies
pip install -r requirements.txt

# Verify setup
python -m blast_testgen.cli validate
```

## Quick Start

### 1. Validate Setup
```bash
python -m blast_testgen.cli validate
```

### 2. Generate Tests for a Single File
```bash
python -m blast_testgen.cli generate my_module.py
```

This creates `tests/test_my_module.py` with generated test cases.

### 3. Generate Tests for Specific Function
```bash
python -m blast_testgen.cli generate my_module.py -f calculate_total
```

### 4. Batch Generate for a Directory
```bash
python -m blast_testgen.cli batch src/
```

## CLI Reference

```
blast-testgen [--host URL] [--model MODEL] <command>

Commands:
  validate              Check Ollama setup
  generate <file>       Generate tests for a file
    -o, --output        Output path for test file
    -f, --function      Target specific function
  batch <directory>     Generate tests for all .py files

Options:
  --host URL            Ollama host (default: http://localhost:11434)
  --model MODEL         Model name (default: codellama)
```

## Architecture

This project follows the **B.L.A.S.T.** protocol with 3-layer A.N.T. architecture:

```
┌─────────────────────────────────────┐
│  UI Layer (CLI)                     │
│  blast_testgen/cli.py               │
├─────────────────────────────────────┤
│  Logic Layer (Orchestrator)         │
│  blast_testgen/orchestrator.py      │
│  blast_testgen/code_parser.py       │
│  blast_testgen/prompts.py           │
├─────────────────────────────────────┤
│  Tool Layer (Ollama Client)         │
│  blast_testgen/ollama_client.py     │
└─────────────────────────────────────┘
```

## Example

Input (`calculator.py`):
```python
def add(a, b):
    """Add two numbers."""
    return a + b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Generated Output (`tests/test_calculator.py`):
```python
import pytest
from calculator import add, divide

def test_add_normal():
    """Test add with normal integer inputs."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_add_edge_cases():
    """Test add with edge cases."""
    assert add(0, 0) == 0
    assert add(-5, -5) == -10

def test_divide_normal():
    """Test divide with valid inputs."""
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    """Test divide raises ValueError on zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Ollama is not running" | Run `ollama serve` in a terminal |
| "Model not found" | Run `ollama pull codellama` |
| Timeout errors | Reduce file size or increase Ollama timeout |
| Poor test quality | Try a different model like `deepseek-coder` |

## License

MIT
