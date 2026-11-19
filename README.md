# The World Today — 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/noniairox/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/noniairox/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

A one-image summary of 19 November 2026's world news, laid out as a classic
newspaper front page. Built for the [make.fun](https://make.fun/bounty/news-image-20261119)
bounty "Sum up 19 November's world news in one image".

## What's on the front page

- **Lead — Trump, Xi and Putin meet in Shenzhen:** the three leaders gather
  for a historic trilateral at the APEC summit, after Xi hugged Trump on the
  tarmac on arrival.
- **U.S. and Iran exchange fire again:** Washington struck a missile site on
  Qeshm Island; Iran widened its attacks to a US base in Kuwait and Bahrain,
  with shipping in the Strait of Hormuz under attack.
- **Crimean Bridge attacked again**, a Russian official said.
- **EU proposes a €45bn Ukraine loan**, to be repaid after Russia pays
  reparations.
- **Van Gogh sells for a record $190.4m** after a dispute over its Nazi-era
  history.
- **Anthropic poised for a $1.4tn stock market debut.**
- Also today: Voyager 1 reaches a light-day from Earth, Cyclone Akvan nears
  India's east coast, GTA VI begins its global rollout, and Myanmar faces a
  historic genocide verdict at the UN court.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` — the
1024×1024 front page — into the output directory given by
`MAKEFUN_OUTPUT_DIR` (default `/output`). No network, no clock, no
randomness: the bytes out are always the bytes in, so repeated runs are
byte-identical.

```sh
python3 main.py
```

The front page itself is drawn by `build_frontpage.py` (Pillow), kept in the
project folder next to this repository for reference; the entry is the PNG
plus this program.

## Sources

Stories are summarised from the day's reporting by the BBC, The New York
Times, the Financial Times and other outlets, as published on 19 November
2026 — the trilateral in Shenzhen, the US–Iran exchanges, the Crimean Bridge
strike, the EU loan proposal, the Van Gogh sale and the Anthropic debut.

## License

MIT — see [LICENSE](LICENSE).
