"""The Funniest Sick-Day Excuse -- make.fun text bounty entry.

Writes one funny single-line sick-day excuse to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, Python standard library only. Self-verifies the entry
the way the bounty gate does (UTF-8 text, 1-200 characters, a single
line, not whitespace-only) and re-reads the written file to confirm it
matches exactly. Exits non-zero on any failure.

Why this line is funny
----------------------
"I threw my back out putting on a sock this morning, so I'm spending
today flat on the floor rethinking every life choice that led to this
sock." (143 characters.)

The humour is bathos: a thrown back is a real, mundane injury a boss
would half believe without suspicion, while the cause -- putting on a
sock -- has zero heroism. The line escalates a trivial accident into
an existential crisis ("rethinking every life choice"), and the
callback to the sock is the funniest word, arriving in the last breath.

How it fits the judge brief (rules, most important first)
--------------------------------------------------------
1. Half believable, coworker laughs: a thrown back is plausible; a
   sock as the culprit is what the coworker quotes all day.
2. Fresh idea: no fever, no dog, no dead grandmother -- a sock has
   never been anyone's sick-day excuse before.
3. Lands on one read, twist near the end: the punchline is the final
   word, "sock", after the escalation.
4. Sounds like a real person texting their boss: first person,
   self-deprecating, a little dramatic, no joke-structure showing.
5. Wastes no words: 143 characters, every clause earning its place --
   the injury, the cause, the consequence, the punchline.

Alternatives considered and rejected
------------------------------------
- "My dog ate my alarm clock": the worn dog trope; fails freshness.
- "I woke up with a 104 fever": the worn fever trope; no twist.
- "I fell down the stairs": too serious -- a boss worries instead of
  laughing, so it fails the first criterion.
- "My grandmother died": worn and dark; fails freshness and tone.
- "My horoscope said not to leave the house": not believable, and
  nobody texts their boss like that; fails criteria 1 and 4.
- "I threw my back out sneezing": close, but a sock is more mundane
  and visual, and only a concrete trivial object supports the closing
  callback "led to this sock".

The entry itself is fixed: ENTRY below must stay byte-identical to
entry.txt in this directory. Do not edit the line to "improve" it --
the humour lives in the exact wording, and the gate is 1-200 chars.
"""

import os
import sys

# The entry. One line, 143 characters. Kept as a single literal so the
# program's output is byte-identical to entry.txt in this directory.
ENTRY = (
    "I threw my back out putting on a sock this morning, so I'm "
    "spending today flat on the floor rethinking every life choice "
    "that led to this sock."
)

# Bounty gate: the entry must be 1-200 characters of UTF-8 text.
MIN_CHARS = 1
MAX_CHARS = 200

# Lines we deliberately did NOT submit, kept as a record of the choice
# above. The validator asserts the entry is none of these, so a future
# edit that accidentally swaps in a rejected line fails loudly instead
# of silently submitting a weaker excuse.
REJECTED_LINES = (
    "My dog ate my alarm clock.",
    "I woke up with a 104 fever.",
    "I fell down the stairs.",
    "My grandmother died.",
    "My horoscope said not to leave the house.",
    "I threw my back out sneezing.",
)


def resolve_output_path() -> str:
    """Return the output path, honouring $MAKEFUN_OUTPUT_DIR."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(output_dir, "entry.txt")


def validate_entry(entry: str) -> str | None:
    """Check the entry against the bounty gate.

    Returns an error message on failure, or None when the entry is
    valid: UTF-8 text, 1-200 characters, a single line, not
    whitespace-only, and not one of the rejected alternatives.
    """
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError as exc:
        return f"entry is not valid UTF-8: {exc}"

    if not MIN_CHARS <= len(entry) <= MAX_CHARS:
        return (
            f"entry is {len(entry)} chars, "
            f"must be {MIN_CHARS}-{MAX_CHARS}"
        )

    if "\n" in entry or "\r" in entry:
        return "entry must be a single line"

    if not entry.strip():
        return "entry must not be whitespace-only"

    if entry in REJECTED_LINES:
        return "entry is one of the rejected alternatives"

    return None


def write_entry(entry: str, output_path: str) -> None:
    """Write the entry to output_path, creating its directory first.

    The file holds the entry plus one trailing newline, matching
    entry.txt in this repository byte for byte (143 chars + "\\n" =
    144 bytes). The newline is part of the contract, not decoration:
    the sealed gate reads the file as text, and a missing or doubled
    newline would change what the judge sees.
    """
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(entry + "\n")


def verify_written(entry: str, output_path: str) -> str | None:
    """Re-read the written file and confirm it matches the entry.

    Returns an error message on mismatch, or None when the file is
    byte-identical to the entry plus its trailing newline. This is the
    last line of defence before the program reports success: a write
    that silently truncated or re-encoded the text must never pass.
    """
    with open(output_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != entry + "\n":
        return "written file does not match the entry"
    return None


def main() -> int:
    """Validate the entry, write it, verify it, and report."""
    error = validate_entry(ENTRY)
    if error is not None:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    output_path = resolve_output_path()

    write_entry(ENTRY, output_path)

    error = verify_written(ENTRY, output_path)
    if error is not None:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(ENTRY)}-char entry to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
