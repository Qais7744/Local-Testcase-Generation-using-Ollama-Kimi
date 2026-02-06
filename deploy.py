#!/usr/bin/env python3
"""
Production Deployment Script for BLAST Testcase Generator
Runs the web app on a fixed port with production settings.
"""

import sys
import os
import argparse
from waitress import serve

sys.path.insert(0, '.')

from blast_testgen.web_app import app


def main():
    parser = argparse.ArgumentParser(
        description='BLAST Testcase Generator - Production Deployment'
    )
    parser.add_argument(
        '--host',
        default='0.0.0.0',
        help='Host to bind to (default: 0.0.0.0 - accessible from network)'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=5000,
        help='Port to bind to (default: 5000)'
    )
    parser.add_argument(
        '--threads',
        type=int,
        default=4,
        help='Number of worker threads (default: 4)'
    )
    
    args = parser.parse_args()
    
    # Import here to get the client model info
    from blast_testgen.web_app import client
    
    print("""
=============================================================
              BLAST Testcase Generator - Production
=============================================================
  Server: http://{host}:{port}
  Model: {model}
  Threads: {threads}
=============================================================
  Press Ctrl+C to stop
=============================================================
    """.format(
        host=args.host,
        port=args.port,
        model=client.model,
        threads=args.threads
    ))
    
    try:
        serve(
            app,
            host=args.host,
            port=args.port,
            threads=args.threads,
            channel_timeout=300,
            ident='BLAST-Testcase-Generator/1.0'
        )
    except KeyboardInterrupt:
        print("\n\n[!] Server stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n[ERROR] Server error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
