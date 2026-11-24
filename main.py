#!/usr/bin/env python3
"""One Letter for Your Day.

Writes exactly one letter to the output directory as entry.txt.

The letter is Z, standing for "zonked": the day I was completely wiped
out, running on fumes, brain buffering, couch-shaped by evening. Vivid,
funny, and honest — a real day, not a performance.

Deterministic: no input, no network, no clock, no randomness. Every run
writes the same single byte, with no trailing newline — the file is
exactly one character long, as the gate requires.
"""

import os

LETTER = "Z"  # Z for "zonked": wiped out, running on fumes, couch-shaped.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
