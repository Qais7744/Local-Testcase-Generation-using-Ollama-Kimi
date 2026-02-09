"""Test generation orchestrator - coordinates parsing, prompting, and output."""

import re
from pathlib import Path
from typing import Optional, Dict, Any

from .ollama_client import OllamaClient
from .code_parser import CodeAnalyzer
from .prompts import build_test_prompt


class TestGenerator:
    """Main orchestrator for test generation workflow."""
    
    def __init__(self, ollama_host: Optional[str] = None, model: Optional[str] = None):
        self.client = OllamaClient(host=ollama_host, model=model)
        self.analyzer = CodeAnalyzer()
    
    def generate_tests(
        self,
        source_path: str,
        target_function: Optional[str] = None,
        output_path: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate tests for a source file.
        
        Args:
            source_path: Path to source code file
            target_function: Specific function to test (optional)
            output_path: Where to save tests (optional)
            
        Returns:
            Dict with test_file_path, test_content, functions_tested, success
        """
        # Read source code
        try:
            code = self.analyzer.read_file(source_path)
        except FileNotFoundError as e:
            return {"success": False, "error": str(e)}
        
        # Validate Python syntax
        is_valid, error = self.analyzer.validate_python(code)
        if not is_valid:
            return {"success": False, "error": f"Invalid syntax: {error}"}
        
        # Determine what to test
        if target_function:
            test_code = self.analyzer.get_function_code(code, target_function)
            if not test_code:
                return {
                    "success": False, 
                    "error": f"Function '{target_function}' not found"
                }
            functions_to_test = [target_function]
        else:
            test_code = code
            functions = self.analyzer.extract_functions(code)
            functions_to_test = [f["name"] for f in functions]
        
        if not functions_to_test:
            return {"success": False, "error": "No functions found to test"}
        
        # Build prompt
        prompt = build_test_prompt(test_code, target_function)
        
        # Generate tests via Ollama
        try:
            response = self.client.generate(prompt)
            generated_code = self._extract_code(response.get("response", ""))
        except Exception as e:
            return {"success": False, "error": f"Generation failed: {e}"}
        
        # Determine output path
        if not output_path:
            source = Path(source_path)
            output_path = source.parent / f"test_{source.name}"
        
        # Write test file
        try:
            output_path = Path(output_path)
            output_path.write_text(generated_code, encoding="utf-8")
        except Exception as e:
            return {"success": False, "error": f"Failed to write file: {e}"}
        
        return {
            "success": True,
            "test_file_path": str(output_path),
            "test_content": generated_code,
            "functions_tested": functions_to_test
        }
    
    def _extract_code(self, response: str) -> str:
        """
        Extract clean Python code from LLM response.
        Removes markdown code blocks if present.
        """
        # Try to extract from markdown code block
        code_block_pattern = r"```python\n(.*?)\n```"
        match = re.search(code_block_pattern, response, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        # Try generic code block
        code_block_pattern = r"```\n(.*?)\n```"
        match = re.search(code_block_pattern, response, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        # Return as-is if no code blocks found
        return response.strip()
