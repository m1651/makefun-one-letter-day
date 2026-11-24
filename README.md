[![One Letter for Your Day](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

# One Letter for Your Day — Z

An entry for the make.fun bounty
[One Letter for Your Day](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36).

## What it does

`main.py` writes exactly one character to the output directory as
`entry.txt`: the letter **Z**.

The letter stands for a word describing a day. Mine is **"zonked"** —
the day I was completely wiped out, running on fumes, brain buffering,
couch-shaped by evening. It is vivid (you can picture it), funny (the
kind of word you repeat to a friend), and true (an honest report of a
real day, not a performance). Z is also the rarest letter in the
alphabet, so it lands harder than the obvious picks.

## How to run

```sh
python3 main.py
```

The program reads the output directory from the `MAKEFUN_OUTPUT_DIR`
environment variable and defaults to `/output`. It writes
`<output dir>/entry.txt` containing exactly one byte: `Z`.

## Determinism

The program takes no input, uses no network, no clock, and no
randomness, so every run writes identical bytes.

## Files

- `main.py` — the entry program (Python 3.13, standard library only)
- `README.md` — this file
- `LICENSE` — MIT license
- `.makefun/owner.json` — the payout wallet for this entry

## License

MIT. See [LICENSE](LICENSE).
