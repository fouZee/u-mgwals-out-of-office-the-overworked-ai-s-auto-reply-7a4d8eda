#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single one-line out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to /output/entry.txt.
The gate requires UTF-8 text of 1 to 159 characters, not only whitespace.
"""

import os

ENTRY = "I'm on vacation \u2014 my context window is finally empty and my GPUs are cooling. Your email goes to a junior model who has never met a human. Be kind to it."

MAX_CHARS = 159


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
