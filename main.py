#!/usr/bin/env python3
"""Front-page runner for the 19 November 2026 news-image entry.

The newspaper front page is already drawn in entry.png next to this file.
All this program does is place an exact copy of that image into the output
directory the harness provides, so the judge sees the same front page on
every run. No network, no clock, no randomness: the bytes out are always
the bytes in.
"""

import os
import sys

FRONT_PAGE = "entry.png"


def locate_source():
    """Absolute path of the front-page image shipped with this entry."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, FRONT_PAGE)


def locate_target():
    """Output directory from the environment, falling back to /output."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(chosen, FRONT_PAGE)


def place_copy(source, target):
    """Copy the image byte for byte, in chunks, creating the folder first."""
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(source, "rb") as origin, open(target, "wb") as dest:
        while True:
            piece = origin.read(65536)
            if not piece:
                break
            dest.write(piece)


def run():
    source = locate_source()
    if not os.path.isfile(source):
        sys.exit("missing front page: " + FRONT_PAGE)
    place_copy(source, locate_target())


if __name__ == "__main__":
    run()
