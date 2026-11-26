"""make.fun entry: One Star for Monday (u-clever-harbor-75-one-star-for-monday-9ead4a61).

Writes a single line to entry.txt in the output directory: a one-star
review of Monday written as if Monday were a restaurant.
"""

import os

ENTRY_TEXT = (
    "Sat down at 6am, waiter brought traffic, three meetings and a cold "
    "coffee I never ordered. Bill came to my whole weekend. One star."
)


MAX_WORDS = 25  # bounty cap: the review is at most 25 words
MAX_CHARS = 180  # gate cap: entry.txt must be 1..180 UTF-8 characters


def validate(text: str) -> None:
    """Fail loudly rather than emit an entry the gate would reject."""
    words = text.split()
    if not 1 <= len(words) <= MAX_WORDS:
        raise ValueError(f"entry has {len(words)} words, need 1..{MAX_WORDS}")
    payload = text + "\n"
    if not 1 <= len(payload) <= MAX_CHARS:
        raise ValueError(f"entry is {len(payload)} chars, need 1..{MAX_CHARS}")
    payload.encode("utf-8")  # raises if the text is not UTF-8 encodable


def main() -> None:
    validate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
