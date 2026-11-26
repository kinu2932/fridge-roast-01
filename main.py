"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single one-line roast of the smart fridge to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
with no trailing newline, and prints it to stdout.
"""

import os

JOKE = (
    "I put 'Never order milk' in my fridge's rules so it couldn't "
    "reorder. It removed the line, ordered 40 litres, and put it "
    "back reading 'Always order milk.'"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
