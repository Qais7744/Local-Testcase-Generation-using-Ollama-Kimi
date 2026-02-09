"""Command-line interface for blast_testgen."""

import sys
import argparse
from pathlib import Path

from .orchestrator import TestGenerator
from .ollama_client import OllamaClient


def create_parser() -> argparse.ArgumentParser:
    """Create CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="blast_testgen",
        description="Generate pytest test cases using local LLM via Ollama"
    )
    
    parser.add_argument(
        "source",
        help="Path to Python source file"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Output path for generated tests (default: test_<source>.py)"
    )
    
    parser.add_argument(
        "-f", "--function",
        help="Generate tests for specific function only"
    )
    
    parser.add_argument(
        "--host",
        default="http://localhost:11434",
        help="Ollama server URL (default: http://localhost:11434)"
    )
    
    parser.add_argument(
        "--model",
        default="codellama",
        help="Model to use (default: codellama)"
    )
    
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check if Ollama is available"
    )
    
    parser.add_argument(
        "--list-models",
        action="store_true",
        help="List available Ollama models"
    )
    
    return parser


def main():
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Initialize client
    client = OllamaClient(host=args.host, model=args.model)
    
    # Handle check command
    if args.check:
        if client.is_available():
            print(f"✅ Ollama is running at {args.host}")
            sys.exit(0)
        else:
            print(f"❌ Ollama not available at {args.host}")
            print("   Run: ollama serve")
            sys.exit(1)
    
    # Handle list-models command
    if args.list_models:
        try:
            models = client.list_models()
            print("Available models:")
            for model in models:
                print(f"  - {model}")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    # Generate tests
    generator = TestGenerator(ollama_host=args.host, model=args.model)
    
    print(f"🚀 Generating tests for: {args.source}")
    if args.function:
        print(f"   Target function: {args.function}")
    
    result = generator.generate_tests(
        source_path=args.source,
        target_function=args.function,
        output_path=args.output
    )
    
    if result["success"]:
        print(f"✅ Tests generated successfully!")
        print(f"   File: {result['test_file_path']}")
        print(f"   Functions tested: {', '.join(result['functions_tested'])}")
        sys.exit(0)
    else:
        print(f"❌ Generation failed: {result.get('error', 'Unknown error')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
