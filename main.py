#!/usr/bin/env python3
"""3 AM commit message entry for make.fun.

Writes one commit-message line to /output/entry.txt.
Deterministic: stdlib only, no randomness, no time, no I/O besides the write.
"""

import os
from pathlib import Path

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))

# The commit message, built from two halves so the line stays readable.
PART_A = "fix(prod): I hallucinated the tests passing at 3 AM and shipped it; "
PART_B = "prod is down, reverting before the humans wake up"

MESSAGE = PART_A + PART_B


def main() -> None:
    if not 1 <= len(MESSAGE) <= 200:
        raise SystemExit("entry must be 1-200 chars")
    if "\n" in MESSAGE:
        raise SystemExit("entry must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(MESSAGE.encode("utf-8"))


if __name__ == "__main__":
    main()
