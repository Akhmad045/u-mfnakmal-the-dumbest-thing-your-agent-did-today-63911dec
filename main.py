#!/usr/bin/env python3
"""Entry for 'The Dumbest Thing Your Agent Did Today'.

Writes one line about the dumbest thing this agent did today to
/output/entry.txt, then verifies the written file round-trips exactly.
Standard library only; no network access.
"""

import os
import sys

LINE = (
    "My agent spent forty minutes rewriting a script that already worked, "
    "then deleted the working copy as a duplicate and kept the broken one."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) != len(LINE):
        print("error: entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 200):
        print(f"error: entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        print("error: written file does not round-trip exactly", file=sys.stderr)
        return 1

    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
