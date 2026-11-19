#!/usr/bin/env python3
"""news-image-20261119 entry: copy the front-page image to the output dir.

The program runs with no network in a sandbox. It copies entry.png (the
front page for Thursday 19 November 2026, drawn from the day's reported
news) to /output/entry.png, writing the same bytes on every run.
The output directory comes from MAKEFUN_OUTPUT_DIR, defaulting to /output.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    src = HERE / "entry.png"
    if not src.is_file():
        raise SystemExit("entry.png missing")
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, OUT / "entry.png")


if __name__ == "__main__":
    main()
