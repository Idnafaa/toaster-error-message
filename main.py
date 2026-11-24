"""Toaster error message entry.

Writes a single line — the error message a kitchen toaster shows its
owner — to /output/entry.txt, where the make.fun gate reads it.
"""

import os
import sys

# The line itself: a toaster that keeps a quiet grudge. Deadpan, one
# voice, no setup, and short enough to land on a single read.
MESSAGE = "E02: I remember every slice you abandoned."

MAX_CHARS = 120


def build_message() -> str:
    """Return the entry text, exactly one line."""
    return MESSAGE.strip()


def write_entry(path: str, text: str) -> None:
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        # No trailing newline: the file must hold exactly the one line
        # the gate measures, nothing extra.
        handle.write(text)


def main() -> int:
    text = build_message()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}",
              file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("TOASTER_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.txt")
    write_entry(target, text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
