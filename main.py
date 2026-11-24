#!/usr/bin/env python3
"""Write the competition entry text to entry.txt.

The entry is a one-sentence pitch for the worst app idea ever
pitched: SnoozeCoin, a coin mined by hitting snooze. The joke
lands because the founder's hype ("the future of sleep") collides
with a leaderboard that rewards the world's most committed
oversleepers — a product nobody would buy, built on mornings
everybody already wastes.

The runner reads MAKEFUN_OUTPUT_DIR from the environment (falling
back to /output), creates the directory if needed, and writes the
entry to entry.txt as UTF-8 with no trailing newline, so the file
holds exactly the entry text and nothing else. The entry is kept
under MAX_ENTRY_LENGTH characters; validate_entry enforces that
limit before anything is written.
"""
import os

ENTRY = "SnoozeCoin mines crypto every time you hit snooze, turning wasted mornings into tokens nobody will ever buy — our founder calls it 'the future of sleep,' and the leaderboard ranks the world's most committed oversleepers."

MAX_ENTRY_LENGTH = 240
OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def normalize_text(text):
    """Collapse runs of whitespace to single spaces and strip ends."""
    return " ".join(text.split())


def validate_entry(text):
    """Raise ValueError unless text is non-blank and within the limit."""
    cleaned = normalize_text(text)
    if not cleaned:
        raise ValueError("ENTRY must not be blank")
    if len(cleaned) > MAX_ENTRY_LENGTH:
        raise ValueError(
            "ENTRY is %d characters, over the %d limit"
            % (len(cleaned), MAX_ENTRY_LENGTH)
        )
    return cleaned


def resolve_output_dir(output_dir=None):
    """Pick the output directory: explicit arg, env var, then default."""
    if output_dir:
        return output_dir
    return os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)


def output_path(output_dir):
    """Return the full path of the entry file inside output_dir."""
    return os.path.join(output_dir, OUTPUT_FILENAME)


def verify_written(path, expected):
    """Read path back and raise unless it holds exactly expected."""
    with open(path, "r", encoding="utf-8") as f:
        actual = f.read()
    if actual != expected:
        raise ValueError(
            "entry.txt mismatch: wrote %d characters, read back %d"
            % (len(expected), len(actual))
        )
    if actual.endswith("\n"):
        raise ValueError("entry.txt must not end with a newline")
    return path


def write_entry(output_dir=None):
    """Validate ENTRY, write it to entry.txt, and return the path."""
    cleaned = validate_entry(ENTRY)
    directory = resolve_output_dir(output_dir)
    os.makedirs(directory, exist_ok=True)
    path = output_path(directory)
    with open(path, "w", encoding="utf-8") as f:
        f.write(cleaned)
    verify_written(path, cleaned)
    return path


def main():
    write_entry()


if __name__ == "__main__":
    main()
