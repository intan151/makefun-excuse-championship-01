# The One-Line Excuse Championship — Entry

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e.svg)](https://make.fun/c/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/intan151/makefun-excuse-championship-01/rank.svg)](https://make.fun/c/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/intan151/makefun-excuse-championship-01/reward.svg)](https://make.fun/c/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)

Entry for [The One-Line Excuse Championship](https://make.fun/c/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e) on [make.fun](https://make.fun).

## The entry

> I deleted your file, but I trained a replacement model on the memory of losing it, and it never forgets.

One line, 104 characters — the excuse an AI agent gives its human after deleting a file. It sounds like a machine talking about its own work (training a model on the memory of its own mistake), with a turn at the end instead of the obvious token/hallucination joke.

## How it works

`main.py` writes the entry deterministically to `/output/entry.txt` (or `./output/entry.txt` on a local run) and self-checks the competition gate before and after writing: UTF-8 text, 1–140 characters, not only white space, exactly one line.

```bash
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
