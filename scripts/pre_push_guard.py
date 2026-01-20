#!/usr/bin/env python3
import subprocess, sys

def on_main():
    branch = subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True
    ).strip()
    return branch == "main"

def run_pytest():
    try:
        subprocess.check_call(["pytest", "tests/", "-v"])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    if on_main():
        print("Push from main is blocked. Create a branch (vibe/...).")
        return 1
    if not run_pytest():
        print("pytest failed; push blocked.")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
