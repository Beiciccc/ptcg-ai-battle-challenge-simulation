#!/usr/bin/env python
from __future__ import annotations

import argparse
import subprocess

COMPETITION = "pokemon-tcg-ai-battle"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--competition", default=COMPETITION)
    args = parser.parse_args()

    command = ["kaggle", "competitions", "submissions", "-c", args.competition]
    return subprocess.run(command, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
