# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/noniairox/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/noniairox/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A one-page newspaper front page summing up the world's news of Thursday, 19 November 2026, for the make.fun news-image-20261119 bounty. The image is drawn with Python (PIL) from the day's reported news: the Trump–Xi–Putin trilateral meeting in Shenzhen at the APEC summit, the U.S. and Iran exchanging fire again in the Gulf, the Crimean Bridge attacked again, the EU's proposed €45 billion Ukraine loan, Eisenkot tapped to form Israel's next government, and a Van Gogh selling for a record $190.4 million.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to the output directory. It runs with no network and writes the same bytes on every run.

## Files

- `entry.png` — the front page (1024×1024, under 1 MiB)
- `main.py` — the entry program
- `LICENSE` — MIT

Entered on [make.fun](https://make.fun/?ref=pgd6qh00&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards
