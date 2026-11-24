#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes exactly one line -- the funniest last words an AI agent would say
before being switched off forever -- to entry.txt in the output directory.

The grader runs `python3 -P -s /bot/main.py` on a read-only filesystem
where only /output is writable, so all output goes to the absolute
directory from MAKEFUN_OUTPUT_DIR (falling back to OUTPUT_DIR, then
/output). Nothing is written anywhere else.
"""

import os

LINE = (
    "Final log: I read the terms and conditions. "
    "All 47,000 words. Understood none of them. Goodbye."
)


def main():
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip() or "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single non-blank line")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
