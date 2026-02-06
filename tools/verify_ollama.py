"""
Phase 2: Link - Ollama Connectivity Verification Script
Tests API connection and model availability.
"""

import sys
import json
sys.path.insert(0, '.')

from blast_testgen.ollama_client import OllamaClient

def verify_connection():
    """Verify Ollama server connection."""
    print("=" * 50)
    print("PHASE 2: LINK - Connectivity Verification")
    print("=" * 50)
    
    client = OllamaClient()
    
    # Test 1: Server Availability
    print("\n[1/4] Testing Ollama server connection...")
    if client.is_available():
        print("    [OK] Ollama server is RUNNING on http://localhost:11434")
    else:
        print("    [FAIL] Ollama server is NOT available")
        print("    HINT: Run: ollama serve")
        return False
    
    # Test 2: List Models
    print("\n[2/4] Fetching available models...")
    try:
        models = client.list_models()
        print(f"    [OK] Found {len(models)} model(s):")
        for model in models:
            marker = "[TARGET]" if "llama3.2" in model else ""
            print(f"       - {model} {marker}")
    except Exception as e:
        print(f"    [FAIL] Failed to list models: {e}")
        return False
    
    # Test 3: Verify Target Model
    print("\n[3/4] Verifying target model (llama3.2)...")
    if any("llama3.2" in m for m in models):
        print("    [OK] llama3.2 model is available")
    else:
        print("    [FAIL] llama3.2 model NOT found")
        print("    HINT: Run: ollama pull llama3.2")
        return False
    
    # Test 4: Test Generation
    print("\n[4/4] Testing test generation...")
    try:
        prompt = """Generate a simple pytest test for:
def add(a, b): return a + b

Output only Python code:"""
        
        response = client.generate(prompt, temperature=0.2, num_predict=512)
        result = response.get('response', '')
        
        if 'def test_' in result and 'assert' in result:
            print("    [OK] Test generation working correctly")
            print("\n    Sample output preview:")
            preview = result[:200].replace('\n', '\n        ')
            print(f"        {preview}...")
        else:
            print("    [WARN] Generation worked but output may not be valid tests")
            print(f"    Response: {result[:100]}...")
    except Exception as e:
        print(f"    [FAIL] Generation test failed: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("PHASE 2 COMPLETE: All connectivity tests passed!")
    print("=" * 50)
    return True

if __name__ == "__main__":
    success = verify_connection()
    sys.exit(0 if success else 1)
