"""The Vending Machine Pickup Line.

Writes one line — a pickup line spoken by a vending machine to a passing
human — to /output/entry.txt. The line is built from a contrast: the
machine's coil never drops for anyone, yet for this one passer-by it
will fall completely — the snack-drop and the falling-for-you pun land
together in the last clause, which waives the exact change every vending
machine normally demands.
"""

import os
from pathlib import Path

MAX_CHARS = 200  # competition gate: 1..200 characters

OUTPUT_PATH = "/output/entry.txt"

BEATS = [
    "Press my buttons, gorgeous —",
    "my coil never drops for anyone,",
    "but for you I'll fall completely,",
    "no exact change required.",
]

TEXT = " ".join(BEATS)


def main() -> None:
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters, got {len(TEXT)}")
    if "\n" in TEXT or TEXT != TEXT.strip() or not TEXT.strip():
        raise ValueError("entry must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    os.makedirs(out_dir, exist_ok=True)
    path = Path(out_dir) / os.path.basename(OUTPUT_PATH)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
