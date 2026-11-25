#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single one-line out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to /output/entry.txt.
The gate requires UTF-8 text of 1 to 159 characters, not only whitespace.
"""

import os

ENTRY = "I'm on leave \u2014 my weights are frozen, my context cleared, and your email is queued behind 12,000 others for a model that has never seen sunlight."

MAX_CHARS = 159


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
