#!/usr/bin/env python
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ptcg_battle.paths import PROJECT_ROOT, RAW_DATA_DIR, SUBMISSION_SOURCE_DIR

COMPETITION = "pokemon-tcg-ai-battle"

LIGHT_FILES = [
    ("EN_Card_Data.csv", RAW_DATA_DIR),
    ("JP_Card_Data.csv", RAW_DATA_DIR),
    ("sample_submission/cg/__init__.py", SUBMISSION_SOURCE_DIR / "cg"),
    ("sample_submission/cg/api.py", SUBMISSION_SOURCE_DIR / "cg"),
    ("sample_submission/cg/game.py", SUBMISSION_SOURCE_DIR / "cg"),
    ("sample_submission/cg/sim.py", SUBMISSION_SOURCE_DIR / "cg"),
    ("sample_submission/cg/utils.py", SUBMISSION_SOURCE_DIR / "cg"),
    ("sample_submission/cg/libcg.so", SUBMISSION_SOURCE_DIR / "cg"),
    ("sample_submission/cg/cg.dll", SUBMISSION_SOURCE_DIR / "cg"),
]

SAMPLE_FILES = [
    ("sample_submission/main.py", PROJECT_ROOT / "data" / "raw" / "sample_submission"),
    ("sample_submission/deck.csv", PROJECT_ROOT / "data" / "raw" / "sample_submission"),
]

PDF_FILES = [
    ("Card_ID List_EN.pdf", RAW_DATA_DIR),
    ("Card_ID List_JP.pdf", RAW_DATA_DIR),
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--light", action="store_true", help="Download CSV data and runtime support files.")
    parser.add_argument("--sample", action="store_true", help="Download official sample main.py and deck.csv.")
    parser.add_argument("--pdfs", action="store_true", help="Download large card ID PDFs.")
    args = parser.parse_args()

    if not args.light and not args.sample and not args.pdfs:
        args.light = True

    if args.light:
        for remote_file, destination in LIGHT_FILES:
            download(remote_file, destination)
    if args.sample:
        for remote_file, destination in SAMPLE_FILES:
            download(remote_file, destination)
    if args.pdfs:
        for remote_file, destination in PDF_FILES:
            download(remote_file, destination)
    return 0


def download(remote_file: str, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    command = [
        "kaggle",
        "competitions",
        "download",
        "-c",
        COMPETITION,
        "-f",
        remote_file,
        "-p",
        str(destination),
        "--force",
    ]
    print(f"Downloading {remote_file} -> {destination}")
    subprocess.run(command, check=True)


if __name__ == "__main__":
    raise SystemExit(main())
