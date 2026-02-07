#!/usr/bin/env python3
"""
Layer 3 Tool: Validate Code
Deterministic script for code validation.
Usage: python tools/validate_code.py <code_file>
"""

import sys
import json
import argparse

sys.path.insert(0, '.')

from blast_testgen.code_parser import CodeAnalyzer


def main():
    parser = argparse.ArgumentParser(description='Validate Python code')
    parser.add_argument('input', help='Input Python file')
    args = parser.parse_args()
    
    # Read input
    try:
        with open(args.input, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(json.dumps({"valid": False, "error": "File not found"}))
        sys.exit(1)
    
    # Validate
    analyzer = CodeAnalyzer()
    is_valid, error = analyzer.validate_python(code)
    
    if not is_valid:
        print(json.dumps({"valid": False, "error": error}))
        sys.exit(1)
    
    # Extract info
    functions = analyzer.extract_functions(code)
    classes = analyzer.extract_classes(code)
    
    result = {
        "valid": True,
        "functions": [f["name"] for f in functions],
        "classes": [c["name"] for c in classes],
        "function_count": len(functions),
        "class_count": len(classes)
    }
    
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
