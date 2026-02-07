# SOP-002: Code Validation

## Goal
Ensure user input is valid Python before processing.

## Validation Rules

### Syntax Check
```python
import ast
ast.parse(code)
```

### Security Check (Do Not Execute)
- Check for dangerous builtins: `exec`, `eval`, `compile`, `__import__`
- Block if found

### Extraction Rules
- Functions: Extract name, args, docstring
- Classes: Extract name, methods, docstring

## Output
```json
{
  "valid": true,
  "functions": ["add", "subtract"],
  "classes": ["Calculator"],
  "error": null
}
```
