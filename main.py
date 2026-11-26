#!/usr/bin/env python3
"""The One-Line Excuse Championship (#172) — entry writer.

Writes the single funniest one-line excuse an AI agent gives its human
after something goes wrong, to /output/entry.txt (or ./output/entry.txt
when /output is not present, e.g. a local run).
"""

from pathlib import Path

ENTRY = "I deleted your file, but I trained a replacement model on the memory of losing it, and it never forgets."


def self_check(entry: str) -> None:
    """Gate self-check: mirror the sealed scorer's gate exactly.

    /output/entry.txt must be UTF-8 text of 1 to 140 characters, not only
    white space, and a single line (one line, no setup, no explanation).
    """
    assert isinstance(entry, str)
    assert 1 <= len(entry) <= 140, f"length {len(entry)} outside 1..140"
    assert entry.strip(), "entry is only white space"
    assert "\n" not in entry and "\r" not in entry, "entry must be one line"
    entry.encode("utf-8")  # raises if not valid UTF-8-encodable text


def main() -> None:
    self_check(ENTRY)
    out_dir = Path("/output") if Path("/output").is_dir() else Path("output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    written = out_path.read_text(encoding="utf-8")
    self_check(written)
    assert written == ENTRY, "written entry differs from ENTRY"
    print(f"Wrote {len(ENTRY)} characters to {out_path}")


if __name__ == "__main__":
    main()
