"""Dad Joke Showdown — make.fun entry.

Writes one dad joke to /output/entry.txt, delivered straight-faced:
the speaker's wife told them to stop making umbrella jokes, so the
rest of the jokes are rain-checked for a drier day. The pun lands at
the end, as a dad joke should.
"""

import os

ENTRY = (
    "My wife told me to stop making umbrella jokes, so I said fine "
    "\u2014 I'll rain-check the rest of them for a drier day."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
