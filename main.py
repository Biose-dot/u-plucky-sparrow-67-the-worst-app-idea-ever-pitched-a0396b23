#!/usr/bin/env python3
"""Writes the competition entry text to entry.txt.

The entry is one sentence pitching the worst app idea imaginable.
The runner takes MAKEFUN_OUTPUT_DIR (default /output), creates it if
needed, and writes the entry there as entry.txt (UTF-8, no trailing
newline). Limit: at most 240 characters.
"""
import os

ENTRY = "SnoozeCoin mines crypto every time you hit snooze, turning wasted mornings into tokens nobody will ever buy — our founder calls it 'the future of sleep,' and the leaderboard ranks the world's most committed oversleepers."

OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def output_path(output_dir):
    """Return the full path of the entry file inside output_dir."""
    return os.path.join(output_dir, OUTPUT_FILENAME)


def write_entry(output_dir=None):
    """Write ENTRY to entry.txt in output_dir; return the file path."""
    if not ENTRY.strip():
        raise ValueError("ENTRY must not be blank")
    output_dir = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)
    path = output_path(output_dir)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    write_entry()


if __name__ == "__main__":
    main()
