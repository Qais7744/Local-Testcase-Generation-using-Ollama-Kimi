#!/usr/bin/env python3
"""
Push files to GitHub using GitHub API
No git installation required!
"""

import requests
import base64
import os
import json

# GitHub API Configuration
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")  # User should set this
REPO_OWNER = "Qais7744"
REPO_NAME = "Selenium2PlaywrightConvertToLocalLLM"
PROJECT_PATH = r"C:\Users\Hp\Downloads\Selenium2PlaywrightConvertToLocalLLM"

def get_all_files(directory):
    """Get all files in directory recursively"""
    files = []
    for root, dirs, filenames in os.walk(directory):
        # Skip .git folder
        dirs[:] = [d for d in dirs if d != '.git']
        
        for filename in filenames:
            filepath = os.path.join(root, filename)
            relpath = os.path.relpath(filepath, directory)
            files.append((relpath, filepath))
    return files

def create_or_update_file(token, owner, repo, path, content, message):
    """Create or update a file in the repository"""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Check if file exists to get SHA
    sha = None
    get_response = requests.get(url, headers=headers)
    if get_response.status_code == 200:
        sha = get_response.json().get("sha")
    
    # Prepare data
    data = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode()
    }
    if sha:
        data["sha"] = sha
    
    response = requests.put(url, headers=headers, json=data)
    return response.status_code, response.json() if response.text else {}

def main():
    print("=" * 60)
    print("Push to GitHub via API")
    print("=" * 60)
    
    if not GITHUB_TOKEN:
        print("\n[X] GITHUB_TOKEN not set!")
        print("\nPlease set your GitHub Personal Access Token:")
        print("1. Go to https://github.com/settings/tokens")
        print("2. Generate new token (classic)")
        print("3. Select 'repo' scope")
        print("4. Copy the token")
        print("\nThen run:")
        print("set GITHUB_TOKEN=ghp_your_token_here")
        print("python push_via_api.py")
        return 1
    
    # Verify token
    print("\n[1/4] Verifying GitHub token...")
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get("https://api.github.com/user", headers=headers)
    if response.status_code != 200:
        print(f"[X] Invalid token: {response.json()}")
        return 1
    user = response.json()["login"]
    print(f"[OK] Authenticated as: {user}")
    
    # Check repository exists
    print("\n[2/4] Checking repository...")
    repo_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
    response = requests.get(repo_url, headers=headers)
    if response.status_code == 404:
        print(f"[!] Repository not found, creating...")
        create_url = "https://api.github.com/user/repos"
        data = {
            "name": REPO_NAME,
            "description": "Selenium to Playwright converter using Local LLM",
            "private": False,
            "auto_init": False
        }
        response = requests.post(create_url, headers=headers, json=data)
        if response.status_code != 201:
            print(f"[X] Failed to create repo: {response.json()}")
            return 1
        print("[OK] Repository created")
    else:
        print(f"[OK] Repository exists: {REPO_OWNER}/{REPO_NAME}")
    
    # Get all files
    print("\n[3/4] Scanning files...")
    files = get_all_files(PROJECT_PATH)
    print(f"[OK] Found {len(files)} files")
    
    # Push files
    print("\n[4/4] Pushing files to GitHub...")
    print("(This may take a while for many files)\n")
    
    success = 0
    failed = 0
    
    for i, (relpath, filepath) in enumerate(files, 1):
        # Skip certain files
        if relpath.startswith('.git') or relpath == 'push_via_api.py':
            continue
        
        try:
            with open(filepath, 'rb') as f:
                content = f.read()
            
            # Try to decode as text, fallback to base64
            try:
                content_str = content.decode('utf-8')
            except:
                content_str = base64.b64encode(content).decode()
            
            status, result = create_or_update_file(
                GITHUB_TOKEN,
                REPO_OWNER,
                REPO_NAME,
                relpath,
                content_str,
                f"Add {relpath}"
            )
            
            if status in [200, 201]:
                print(f"[{i}/{len(files)}] [OK] {relpath}")
                success += 1
            else:
                print(f"[{i}/{len(files)}] [X] {relpath}: {result.get('message', 'Unknown error')}")
                failed += 1
                
        except Exception as e:
            print(f"[{i}/{len(files)}] [X] {relpath}: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total files: {len(files)}")
    print(f"Success: {success}")
    print(f"Failed: {failed}")
    print(f"\nRepository URL: https://github.com/{REPO_OWNER}/{REPO_NAME}")
    
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
