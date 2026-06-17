#!/usr/bin/env python
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ptcg_battle.deck import load_default_card_data, read_deck, validate_deck
from ptcg_battle.paths import EN_CARD_DATA


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("deck", help="Path to deck.csv")
    parser.add_argument("--cards", default=str(EN_CARD_DATA), help="Path to EN_Card_Data.csv")
    args = parser.parse_args()

    deck = read_deck(args.deck)
    cards = load_default_card_data(args.cards)
    result = validate_deck(deck, cards)

    print(f"cards: {result.card_count}")
    for warning in result.warnings:
        print(f"warning: {warning}")
    for error in result.errors:
        print(f"error: {error}")

    if result.ok:
        print("deck check: ok")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
