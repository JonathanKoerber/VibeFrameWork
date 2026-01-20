#!/usr/bin/env python3
import subprocess, sys

TEST_PATHS = ("tests/", "_test.py", "test_", "tests.py")

def main():
    diff = subprocess.check_output(
        ["git", "diff", "--cached", "--name-only"], text=True
    ).splitlines()
    if not diff:
        return 0
    touched_tests = any(any(tok in p for tok in TEST_PATHS) for p in diff)
    touched_code = any(p.endswith(".py") and "tests" not in p for p in diff)
    if touched_code and not touched_tests:
        print("Code changed but no tests staged. Add/modify a test file.")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
