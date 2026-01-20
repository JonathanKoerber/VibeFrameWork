#!/usr/bin/env python3
import sys, re, pathlib

PATTERN = re.compile(r"^vibe: .+")

def main():
    msg_file = pathlib.Path(sys.argv[1])
    msg = msg_file.read_text().strip().splitlines()
    if not msg:
        print("Empty commit message.")
        return 1
    if not PATTERN.match(msg[0]):
        print('Commit message must start with "vibe: " (present tense).')
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
