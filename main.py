"""Two-Sentence Horror.

Writes one original two-sentence horror story to /output/entry.txt.
Deterministic, standard library only, no network.

Draft (revised once: the first draft ended on the locked window alone; the
revision adds the empty bed, so the second sentence turns the first twice -
the lock meant to keep her safe was worked from outside, and she is gone
anyway):
  v1: "Every night, I lock my daughter's bedroom window from the inside,
       because she sleepwalks. Last night I found it locked from the outside."
  v2: "Every night, I lock my daughter's bedroom window from the inside,
       because she sleepwalks. Last night I found it locked from the
       outside, and her bed was empty."
"""

import os

ENTRY = (
    "Every night, I lock my daughter's bedroom window from the inside, "
    "because she sleepwalks. Last night I found it locked from the "
    "outside, and her bed was empty."
)

if not 1 <= len(ENTRY) <= 400 or not ENTRY.strip():
    raise ValueError(
        f"entry must be 1-400 non-blank characters, got {len(ENTRY)}"
    )


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
