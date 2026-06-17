#!/usr/bin/env python
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ptcg_battle.deck import load_default_card_data, read_deck, validate_deck
from ptcg_battle.packaging import build_submission_zip
from ptcg_battle.paths import EN_CARD_DATA, SUBMISSION_SOURCE_DIR, SUBMISSIONS_DIR


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="baseline", help="Output zip name without extension.")
    parser.add_argument("--source", default=str(SUBMISSION_SOURCE_DIR), help="Submission source directory.")
    parser.add_argument("--allow-missing-cg", action="store_true", help="Build without submission/cg support files.")
    parser.add_argument("--skip-deck-check", action="store_true", help="Skip deck validation.")
    args = parser.parse_args()

    source = Path(args.source)
    if not args.skip_deck_check:
        deck = read_deck(source / "deck.csv")
        cards = load_default_card_data(EN_CARD_DATA)
        deck_result = validate_deck(deck, cards)
        for warning in deck_result.warnings:
            print(f"warning: {warning}")
        if not deck_result.ok:
            for error in deck_result.errors:
                print(f"error: {error}")
            return 1

    output = SUBMISSIONS_DIR / f"{args.name}.zip"
    package = build_submission_zip(
        source,
        output,
        require_support_files=not args.allow_missing_cg,
    )
    print(f"package: {package.path}")
    print(f"files: {package.file_count}")
    print(f"support files: {'yes' if package.has_support_files else 'no'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
