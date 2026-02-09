"""Code parsing and analysis utilities."""

import ast
import re
from typing import List, Dict, Optional, Tuple
from pathlib import Path


class CodeAnalyzer:
    """Analyzes Python code to extract functions and classes."""
    
    @staticmethod
    def extract_functions(code: str) -> List[Dict[str, any]]:
        """
        Extract function definitions from code.
        
        Returns:
            List of dicts with 'name', 'args', 'docstring', 'lineno'
        """
        functions = []
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    func_info = {
                        "name": node.name,
                        "args": [arg.arg for arg in node.args.args],
                        "docstring": ast.get_docstring(node),
                        "lineno": node.lineno,
                        "source": CodeAnalyzer._get_node_source(code, node)
                    }
                    functions.append(func_info)
        except SyntaxError as e:
            raise ValueError(f"Invalid Python syntax: {e}")
        return functions
    
    @staticmethod
    def extract_classes(code: str) -> List[Dict[str, any]]:
        """Extract class definitions from code."""
        classes = []
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_info = {
                        "name": node.name,
                        "methods": [
                            n.name for n in node.body 
                            if isinstance(n, ast.FunctionDef)
                        ],
                        "docstring": ast.get_docstring(node),
                        "lineno": node.lineno
                    }
                    classes.append(class_info)
        except SyntaxError as e:
            raise ValueError(f"Invalid Python syntax: {e}")
        return classes
    
    @staticmethod
    def get_function_code(code: str, function_name: str) -> Optional[str]:
        """Extract source code for a specific function."""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == function_name:
                    return CodeAnalyzer._get_node_source(code, node)
        except SyntaxError:
            pass
        return None
    
    @staticmethod
    def _get_node_source(code: str, node: ast.AST) -> str:
        """Extract source text for an AST node."""
        lines = code.splitlines()
        start_line = node.lineno - 1
        end_line = getattr(node, 'end_lineno', start_line + 1)
        if end_line:
            return "\n".join(lines[start_line:end_line])
        return lines[start_line]
    
    @staticmethod
    def read_file(file_path: str) -> str:
        """Read code from file."""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        return path.read_text(encoding="utf-8")
    
    @staticmethod
    def validate_python(code: str) -> Tuple[bool, Optional[str]]:
        """
        Validate if code is valid Python.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            ast.parse(code)
            return True, None
        except SyntaxError as e:
            return False, str(e)
