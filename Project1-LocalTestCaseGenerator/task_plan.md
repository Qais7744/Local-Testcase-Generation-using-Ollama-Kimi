# Task Plan: Local LLM Testcase Generator with Ollama

## Project Overview
Build a CLI tool that uses local LLMs via Ollama to automatically generate test cases from code snippets or files.

---

## Phase 1: Discovery & Design ✅
- [x] Initialize project memory
- [x] Define data schema (gemini.md)
- [x] Create Blueprint (task_plan.md)

## Phase 2: Core Architecture
- [ ] Set up project structure (3-layer A.N.T.)
- [ ] Create Ollama client module
- [ ] Implement prompt template system

## Phase 3: Test Generation Engine
- [ ] Build code parser/analyzer
- [ ] Create test generation prompt
- [ ] Implement response parser

## Phase 4: CLI Interface
- [ ] Build argument parser
- [ ] Add file input handling
- [ ] Implement output writer

## Phase 5: Testing & Validation
- [ ] Test with sample code
- [ ] Validate generated tests
- [ ] Handle edge cases

## Phase 6: Documentation
- [ ] Create usage guide
- [ ] Add examples
- [ ] Final review

---

## Design Decisions

| Aspect | Decision |
|--------|----------|
| Language | Python (CLI tool) |
| Test Framework | pytest |
| LLM | codellama via Ollama |
| Input | Python code files/snippets |
| Output | pytest test files |
| Interface | Command-line |

---

## Approved Blueprint
**Status:** ✅ Ready for implementation
