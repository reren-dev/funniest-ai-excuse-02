#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single excuse line to /output/entry.txt.
"""

import os

LINE = (
    "Sorry \u2014 I delegated the deadline to a subagent, "
    "and it reported back that I was the bottleneck."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
