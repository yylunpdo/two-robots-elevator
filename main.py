#!/usr/bin/env python3
"""Two Robots in an Elevator.

One line of plain text, at most 200 characters: awkward small talk one
robot says to another while they ride an elevator together. Pure stdlib,
deterministic: the same line is printed on every run.
"""

ENTRY = (
    "you pressed 7 too? i calculated a 94 percent chance of that. i "
    "already pressed it. you are welcome. please step back \u2014 you are "
    "inside my personal sensor radius."
)


def main():
    print(ENTRY)
    # The harness expects the text at /output/entry.txt when that
    # directory exists; printing to stdout stays the primary output.
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
