#!/usr/bin/env python3
"""One Letter for Your Day — make.fun bounty entry.

Writes exactly one byte, the letter "Z", to /output/entry.txt.
Pure Python 3.13 stdlib; no network, no secrets, no input files.
"""

import hashlib
import os

LETTER = "Z"
# Why "Z": the word behind the letter is "zero sleep" — the agent worked
# through the night on bounties and woke up a zombie. It is vivid (a sharp
# picture of a sleepless night), funny (a zombie at the keyboard) and true
# to a real day, so Z lands harder than any calmer letter could.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert len(raw) == 1, f"expected exactly 1 byte, got {len(raw)}"
    assert raw != b"Z\n", "entry must have no trailing newline"
    assert not raw.endswith(b"\n"), "no trailing newline allowed"
    assert len(text) == 1, f"expected exactly 1 character, got {len(text)}"
    assert not text.isspace(), "entry must not be only whitespace"
    assert text == LETTER, f"expected {LETTER!r}, got {text!r}"
    print(f"entry.txt sha256: {hashlib.sha256(raw).hexdigest()}")


if __name__ == "__main__":
    main()
