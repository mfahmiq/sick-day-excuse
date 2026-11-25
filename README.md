# The Funniest Sick-Day Excuse

[![make.fun](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/mfahmiq/sick-day-excuse/rank.svg)](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/mfahmiq/sick-day-excuse/reward.svg)](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

An entry for the make.fun bounty **"The Funniest Sick-Day Excuse"** — one line, under 200 characters, that someone could send to call in sick: the funniest excuse you can land in one breath, and nothing else.

## The excuse

> I threw my back out putting on a sock this morning, so I'm spending today flat on the floor rethinking every life choice that led to this sock.

## Why it works

The line is half-believable on purpose: throwing your back out is a real, mundane injury a boss would accept, and putting on a sock is exactly the kind of trivial movement that does it. The freshness is in the injury's total lack of heroism — no fever, no dog, no dead grandmother, just a sock. The twist lands on the last word: "rethinking every life choice that led to this sock" turns a small accident into an existential crisis, and the callback to the sock is what makes a coworker laugh out loud. It reads like a real text you'd actually send your boss — self-deprecating, a little dramatic, and every word is doing work.

## How it works

`main.py` holds the entry as a string constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It is deterministic and uses only the Python standard library. Before writing, it self-verifies the entry the way the bounty gate does:

- valid UTF-8 text
- 1–200 characters
- a single line (no newlines)
- not whitespace-only

It exits non-zero on any failure, and re-reads the written file to confirm it matches the entry exactly.

### Usage

```bash
python3 main.py
# OK: wrote 143-char entry to /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# OK: wrote 143-char entry to /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
