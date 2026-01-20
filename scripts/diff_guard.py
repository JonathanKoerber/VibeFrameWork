#!/usr/bin/env python3
import subprocess, sys

MAX_FILES = 4
MAX_LINES = 150

def main():
    out = subprocess.check_output(
        ["git", "diff", "--cached", "--numstat"], text=True
    ).strip()
    if not out:
        return 0
    files = 0
    lines = 0
    for line in out.splitlines():
        add_str, del_str, path = line.split("\t")
        add = int(add_str) if add_str.isdigit() else 0
        delete = int(del_str) if del_str.isdigit() else 0
        files += 1
        lines += add + delete
    if files > MAX_FILES or lines > MAX_LINES:
        print(f"Diff too large: {files} files, {lines} lines (limit {MAX_FILES} files, {MAX_LINES} lines)")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
