"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (117 characters, single line) to /output/entry.txt.
Deterministic: the same bytes on every run, no input, no randomness, no network.
"""

import os
from pathlib import Path

MESSAGE = (
    "fix(prod): I hallucinated the tests passing at 3 AM and shipped it; "
    "prod is down, reverting before the humans wake up"
)


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(MESSAGE, encoding="utf-8")


if __name__ == "__main__":
    main()
