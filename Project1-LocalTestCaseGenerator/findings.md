# Findings & Research

## Discovery Answers (Phase 1: Blueprint)

### 1. North Star
Local LLM Testcase generator based on User input with proper Templates stored in code, using Ollama API with open source model **llama3.2**.

### 2. Integrations
- **Ollama** - Local LLM server
- Model: `llama3.2` (open source)

### 3. Source of Truth
NA - Direct user input processing

### 4. Delivery Payload
**UI Chat Interface** where:
- User enters input in a chat UI
- Ollama takes the input
- System generates and displays testcases

### 5. Behavioral Rules
- User enters input
- System processes via Local LLM (Ollama)
- System returns generated testcases as output
- Simple input → output flow

---

## Ollama Integration
- Local LLM server running on `http://localhost:11434`
- REST API for text generation
- Model: `llama3.2` (as per requirements)
- Endpoint: `POST /api/generate`

## Test Generation Approach
1. User enters code/requirements in chat UI
2. Frontend sends to backend API
3. Backend builds prompt with stored templates
4. Ollama generates testcases
5. Display results in chat UI

## Key Constraints
- Ollama must be running locally
- Model needs to be pulled before use (`ollama pull llama3.2`)
- Generated tests need validation

## Prompt Strategy
Use stored templates with user input for consistent test generation.

## Phase 2: Link - Integration Test Results

### Ollama Connection ✅
- Server: Running on `http://localhost:11434`
- Response Time: < 1s for health check
- Available Models: llama3.2:latest, gemma3:1b, llama3.2:3b

### Test Generation Validation ✅
Sample input: `def add(a, b): return a + b`
Generated output:
- ✅ Valid Python syntax
- ✅ pytest compatible
- ✅ Multiple test cases (normal, negative, zero)
- ✅ Docstrings included
- ✅ Import statements present
