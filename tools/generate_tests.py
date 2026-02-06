#!/usr/bin/env python3
"""
Layer 3 Tool: Generate Tests
Deterministic script for test generation.
Usage: python tools/generate_tests.py <code_file> [output_file]
"""

import sys
import json
import argparse

sys.path.insert(0, '.')

from blast_testgen.ollama_client import OllamaClient
from blast_testgen.prompts import build_test_prompt
from blast_testgen.code_parser import CodeAnalyzer


def main():
    parser = argparse.ArgumentParser(description='Generate pytest tests from code file')
    parser.add_argument('input', help='Input Python file')
    parser.add_argument('-o', '--output', help='Output file (default: stdout)')
    parser.add_argument('-f', '--function', help='Target specific function')
    parser.add_argument('--model', default='llama3.2', help='Ollama model')
    args = parser.parse_args()
    
    # Read input
    try:
        with open(args.input, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {args.input}"}))
        sys.exit(1)
    
    # Validate
    analyzer = CodeAnalyzer()
    is_valid, error = analyzer.validate_python(code)
    if not is_valid:
        print(json.dumps({"error": f"Invalid Python: {error}"}))
        sys.exit(1)
    
    # Check Ollama
    client = OllamaClient(model=args.model)
    if not client.is_available():
        print(json.dumps({
            "error": "Ollama not available",
            "hint": "Run: ollama serve"
        }))
        sys.exit(1)
    
    # Generate
    try:
        prompt = build_test_prompt(code, args.function)
        response = client.generate(prompt, temperature=0.2, num_predict=2048)
        
        result = {
            "success": True,
            "generated_tests": response.get('response', ''),
            "model": args.model,
            "input_file": args.input
        }
        
        output = json.dumps(result, indent=2)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"Tests written to: {args.output}")
        else:
            print(output)
            
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)


if __name__ == '__main__':
    main()
