#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email — make.fun entry.

Writes a single original one-liner to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
"""

from pathlib import Path

ENTRY = (
    "Somewhere, an unsent email is sitting in on this meeting and thinking: "
    "'I could have done this in two sentences.'"
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
