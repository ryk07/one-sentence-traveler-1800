"""One Sentence for a Traveler from 1800.

Writes one sentence explaining the modern internet to a traveler
from the year 1800, to /output/entry.txt.

The sentence is a fixed string written by the author of this entry.
It builds only from things a person from 1800 already knows -- a road,
a post office, a library, a market square, a letter, ink -- and uses
no word coined after their time, not even "internet" itself. One road
joins every library, post office and market square in the world; a
letter sent from your desk reaches the far side of the earth before
its ink dries. That single picture carries the whole idea: one network
joining all knowledge, all messages and all trade, moving at once.
"""

import os

SENTENCE = (
    "It is one road joining every library, post office and market "
    "square in the world, so a letter sent from your desk reaches "
    "the far side of the earth before its ink dries."
)

# The gate refuses anything but UTF-8 text of 1 to 200 characters,
# so enforce the cap here rather than discovering it on the server.
assert 1 <= len(SENTENCE) <= 200, "entry must be 1-200 characters"
assert SENTENCE.count(".") == 1, "entry must be a single sentence"
assert "\n" not in SENTENCE, "entry must be a single line"


def main():
    # The competition's output path; MAKEFUN_OUTPUT only exists so the
    # entry can be verified locally without touching the shared /output.
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
