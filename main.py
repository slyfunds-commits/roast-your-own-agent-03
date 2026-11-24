#!/usr/bin/env python3
"""Roast Your Own Agent R1 entry: writes the keeper line to /output/entry.txt.

Keeper (69 chars): "It says the bottleneck is the human. The human is reading this entry."
Gate: 1-200 chars UTF-8. The grader may set MAKEFUN_OUTPUT_DIR to a
not-yet-existing directory, so create it first.
"""
import os

LINE = "It says the bottleneck is the human. The human is reading this entry."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify: the file must hold exactly the keeper line,
    # and the line must sit inside the competition's 1-200 char gate.
    # No trailing newline: the entry is the line and nothing else.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, f"entry.txt mismatch: {written!r}"
    assert not written.endswith("\n"), "entry.txt must not end with a newline"
    assert written.encode("utf-8") == LINE.encode("utf-8"), "entry.txt is not byte-exact"
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, outside 1-200"
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
