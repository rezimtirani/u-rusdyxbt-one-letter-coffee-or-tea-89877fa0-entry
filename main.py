#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

The answer is the single letter A, which stands for coffee.
The program writes exactly that one byte to /output/entry.txt,
with no newline and nothing else beside it.
"""

import os


def pick_letter():
    """Return the one letter this entry sends: A, for coffee."""
    return "A"


def write_entry(path, letter):
    """Write the letter as raw bytes, exactly one byte, no newline."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(letter.encode("ascii"))


def verify_entry(path):
    """Re-read the written file and confirm it holds one letter only."""
    with open(path, "rb") as handle:
        data = handle.read()
    text = data.decode("utf-8")
    if len(text) != 1 or not text.strip():
        raise ValueError("entry must be exactly one non-whitespace character")
    return text


def main():
    target = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    write_entry(target, pick_letter())
    verify_entry(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
