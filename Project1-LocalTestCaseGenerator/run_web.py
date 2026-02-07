#!/usr/bin/env python3
"""Entry point to run the Web UI for BLAST Testcase Generator."""

import sys
import argparse

# Add current directory to path
sys.path.insert(0, '.')

from blast_testgen.web_app import run_web_app


def main():
    parser = argparse.ArgumentParser(
        description='BLAST Testcase Generator Web UI'
    )
    parser.add_argument(
        '--host', 
        default='127.0.0.1',
        help='Host to bind to (default: 127.0.0.1)'
    )
    parser.add_argument(
        '--port', 
        type=int, 
        default=5000,
        help='Port to bind to (default: 5000)'
    )
    parser.add_argument(
        '--debug', 
        action='store_true',
        help='Enable debug mode'
    )
    
    args = parser.parse_args()
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║           🚀 BLAST Testcase Generator - Web UI                ║
╠══════════════════════════════════════════════════════════════╣
║  Model: llama3.2 (via Ollama)                                ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    run_web_app(host=args.host, port=args.port, debug=args.debug)


if __name__ == '__main__':
    main()
