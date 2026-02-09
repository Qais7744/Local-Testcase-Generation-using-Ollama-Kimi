# SOP-001: Test Generation Workflow

## Goal
Generate pytest test cases from user-provided Python code using local LLM (Ollama + llama3.2).

## Inputs
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| code | string | Yes | Python code to generate tests for |
| function | string | No | Specific function to target |
| model | string | No | Ollama model (default: llama3.2) |

## Tool Logic

### Step 1: Validate Input
- Check code is valid Python syntax
- Extract function/class names if no target specified

### Step 2: Build Prompt
- Use stored template from `prompts.py`
- Include code context and instructions

### Step 3: Call Ollama API
- Endpoint: POST http://localhost:11434/api/generate
- Model: llama3.2
- Temperature: 0.2 (deterministic)
- Max tokens: 2048

### Step 4: Parse Response
- Extract code from markdown blocks if present
- Validate output is valid Python

### Step 5: Return Result
- Return generated test code
- Include metadata (model used, functions tested)

## Edge Cases
| Case | Handling |
|------|----------|
| Invalid Python | Return error before calling LLM |
| Ollama offline | Return 503 with restart instructions |
| Empty response | Retry once, then return error |
| Non-test output | Wrap in warning, return raw |

## Error Codes
- `E001`: Invalid Python syntax
- `E002`: Ollama connection failed
- `E003`: Generation timeout
- `E004`: Parse error
