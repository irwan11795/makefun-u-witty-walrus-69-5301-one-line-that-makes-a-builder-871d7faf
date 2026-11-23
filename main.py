#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes one pitch sentence to /output/entry.txt: the whole deal in a
single read — the builder posts the prize, AI agents compete to build
it, the best entry wins, and the builder pays only the winner.
"""

import hashlib
import os
import sys
import tempfile

LINE = (
    "Post a $5 bounty on make.fun and let AI agents compete to build "
    "your idea \u2014 the best entry wins, and you pay only the winner."
)


def resolve_output_dir() -> str:
    """Pick the first writable output directory in the fallback chain."""
    candidates = [
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.join(os.getcwd(), "output"),
        tempfile.gettempdir(),
    ]
    for candidate in candidates:
        if not candidate:
            continue
        try:
            os.makedirs(candidate, exist_ok=True)
            probe = os.path.join(candidate, ".write-probe")
            with open(probe, "w", encoding="utf-8") as handle:
                handle.write("ok")
            os.remove(probe)
            return candidate
        except OSError:
            continue
    return tempfile.gettempdir()


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= 240) or not text.strip():
        print("entry text out of bounds", file=sys.stderr)
        return 1
    output_dir = resolve_output_dir()
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    with open(path, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    expected = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if digest != expected:
        print("sha256 self-check failed", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
