"""Prompt templates for test generation."""

from typing import Optional


# Universal prompt for any input (code or text)
COMBINED_TEST_GENERATION_PROMPT = """You are a QA Test Engineer. Generate test cases based on this input:

INPUT:
```
{user_input}
```

Analyze the input and generate:

If it's CODE (Python function/class):
- Test the function with different inputs
- Include positive and negative test cases
- Test edge cases (empty, None, invalid types)
- Generate pytest code

If it's TEXT (feature/requirement/story):
- Create manual test cases with steps
- Include UI/functional scenarios
- Positive and negative scenarios
- Still generate pytest code skeleton

Output format (STRICT JSON):
{{
  "manual_test_cases": [
    {{"id": "TC_001", "title": "...", "type": "POSITIVE", "steps": ["..."], "expected": "..."}}
  ],
  "pytest_code": "import pytest\\ndef test_...():\\n    ..."
}}

Rules:
- Generate 2-4 test cases maximum
- Keep steps short (1-2 lines each)
- POSITIVE for success cases, NEGATIVE for failures
- pytest_code should be simple and runnable
- If input is unclear, create generic validation tests

Return ONLY valid JSON. No markdown, no explanations."""


def build_test_prompt(user_input: str, target_function: Optional[str] = None) -> str:
    """Build a prompt for test generation."""
    return COMBINED_TEST_GENERATION_PROMPT.format(user_input=user_input)
