"""Write a one-line horror entry to the output file.

The line is a single sentence under 200 characters for the
one-line-one-chill competition. The output file holds exactly
the 94 bytes of LINE — no trailing newline, no extra whitespace.
"""

import os

LINE = "I found my own obituary in tomorrow's newspaper, and the photo was taken from inside my house."


def main():
    output_path = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {output_path}")


if __name__ == "__main__":
    main()
