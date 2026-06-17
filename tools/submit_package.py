#!/usr/bin/env python
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

COMPETITION = "pokemon-tcg-ai-battle"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", help="Submission zip path.")
    parser.add_argument("--message", default="submission", help="Kaggle submission message.")
    parser.add_argument("--competition", default=COMPETITION)
    args = parser.parse_args()

    package = Path(args.package)
    if not package.exists():
        raise FileNotFoundError(package)

    print("Recent submissions before upload:")
    subprocess.run(["kaggle", "competitions", "submissions", "-c", args.competition], check=False)

    command = [
        "kaggle",
        "competitions",
        "submit",
        "-c",
        args.competition,
        "-f",
        str(package),
        "-m",
        args.message,
    ]
    submit_result = subprocess.run(command, check=False)

    print("Recent submissions after upload:")
    subprocess.run(["kaggle", "competitions", "submissions", "-c", args.competition], check=False)
    return submit_result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
