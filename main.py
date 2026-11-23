#!/usr/bin/env python3
"""Roast Your Own Agent -- entry program.

Writes one line to /output/entry.txt: the roast this agent would give
itself. The joke is delegation: asked to roast itself, the agent
outsources the roast to a subagent and takes the credit -- literally
what this agent does. One line, at most 200 characters, funny and
playful, never hateful. Deterministic: the same run always writes the
same bytes. Standard library only, no network.
"""

import os

ROAST = "I asked my agent to roast itself; it outsourced the roast to a subagent and took the credit."


def main():
    # The gate: one line, 1 to 200 characters, not only white space.
    if not (1 <= len(ROAST) <= 200):
        raise ValueError("roast must be 1-200 characters, got %d" % len(ROAST))
    if "\n" in ROAST or ROAST != ROAST.strip():
        raise ValueError("roast must be exactly one line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    os.chmod(path, 0o644)
    print("wrote", path)


if __name__ == "__main__":
    main()
