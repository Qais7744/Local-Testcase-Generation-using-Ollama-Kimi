#!/usr/bin/env python3
"""
Script to push Project2 to GitHub repository
Uses GitPython library or subprocess
"""

import subprocess
import os
import sys

PROJECT_PATH = r"C:\Users\Hp\Downloads\Selenium2PlaywrightConvertToLocalLLM"
REPO_URL = "https://github.com/Qais7744/Selenium2PlaywrightConvertToLocalLLM.git"

def run_command(cmd, cwd=None):
    """Run a command and return output"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd or PROJECT_PATH,
            capture_output=True,
            text=True
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def main():
    print("=" * 60)
    print("Pushing Project2 to GitHub Repository")
    print("=" * 60)
    print(f"Project: {PROJECT_PATH}")
    print(f"Repository: {REPO_URL}")
    print("=" * 60)
    
    # Check if git is available
    print("\n[1/7] Checking if git is available...")
    code, stdout, stderr = run_command("git --version", cwd=PROJECT_PATH)
    if code != 0:
        print("[X] Git is not installed or not in PATH")
        print("Please install Git from: https://git-scm.com/download/win")
        print("\nAlternative: Run these commands manually in Git Bash:")
        print(f"cd {PROJECT_PATH}")
        print("git init")
        print("git add .")
        print('git commit -m "Initial commit: Selenium2Playwright Converter"')
        print(f"git remote add origin {REPO_URL}")
        print("git push -u origin main")
        return 1
    
    print(f"[OK] Git found: {stdout.strip()}")
    
    # Initialize git
    print("\n[2/7] Initializing git repository...")
    code, stdout, stderr = run_command("git init", cwd=PROJECT_PATH)
    if code != 0:
        print(f"[X] Error: {stderr}")
    else:
        print(f"[OK] {stdout.strip()}")
    
    # Add all files
    print("\n[3/7] Adding files to git...")
    code, stdout, stderr = run_command("git add .", cwd=PROJECT_PATH)
    if code != 0:
        print(f"[X] Error: {stderr}")
    else:
        print("[OK] All files added")
    
    # Commit
    print("\n[4/7] Committing changes...")
    commit_msg = """Initial commit: Selenium2Playwright Converter with Local LLM

- Add Selenium to Playwright code converter
- Support Ollama, LM Studio, Hugging Face LLMs  
- Add CLI and Python API
- Include examples and tests
- Add comprehensive documentation with diagrams"""
    
    code, stdout, stderr = run_command(f'git commit -m "{commit_msg}"', cwd=PROJECT_PATH)
    if code != 0:
        if "nothing to commit" in stderr.lower():
            print("[!] Nothing to commit (already committed)")
        else:
            print(f"[X] Error: {stderr}")
    else:
        print(f"[OK] {stdout.strip()}")
    
    # Add remote
    print("\n[5/7] Adding remote repository...")
    
    # First check if remote already exists
    code, stdout, stderr = run_command("git remote -v", cwd=PROJECT_PATH)
    if "origin" in stdout:
        print("[!] Remote 'origin' already exists, updating...")
        run_command("git remote remove origin", cwd=PROJECT_PATH)
    
    code, stdout, stderr = run_command(f"git remote add origin {REPO_URL}", cwd=PROJECT_PATH)
    if code != 0:
        print(f"[X] Error: {stderr}")
    else:
        print("[OK] Remote added")
    
    # Check branch name
    print("\n[6/7] Checking branch name...")
    code, stdout, stderr = run_command("git branch --show-current", cwd=PROJECT_PATH)
    branch = stdout.strip() if stdout else "main"
    print(f"[OK] Current branch: {branch}")
    
    # Push
    print("\n[7/7] Pushing to GitHub...")
    print("[!] This will push to GitHub. You may need to enter credentials...")
    
    code, stdout, stderr = run_command(f"git push -u origin {branch}", cwd=PROJECT_PATH)
    if code != 0:
        print(f"[X] Push failed: {stderr}")
        print("\n[TROUBLESHOOTING]")
        print("1. Check your internet connection")
        print("2. Verify GitHub repository exists: https://github.com/Qais7744/Selenium2PlaywrightConvertToLocalLLM")
        print("3. You may need to authenticate with GitHub")
        print("\nAlternative: Use GitHub Desktop or VS Code to push")
    else:
        print(f"[OK] {stdout.strip()}")
        print("\n" + "=" * 60)
        print("SUCCESS! Project pushed to GitHub!")
        print("=" * 60)
        print(f"\nView repository: {REPO_URL}")
    
    return 0 if code == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
