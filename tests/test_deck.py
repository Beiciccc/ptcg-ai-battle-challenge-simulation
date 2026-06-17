from pathlib import Path

import pandas as pd

from ptcg_battle.deck import read_deck, validate_deck


def test_read_deck_ignores_blank_lines(tmp_path: Path) -> None:
    path = tmp_path / "deck.csv"
    path.write_text("1\n\n2\n")

    assert read_deck(path) == [1, 2]


def test_validate_deck_rejects_short_deck() -> None:
    cards = pd.DataFrame(
        [
            {"Card ID": 1, "Card Name": "Basic Water Energy", "Stage": "Basic Energy", "Category": "", "Rule": ""},
        ]
    )

    result = validate_deck([1], cards)

    assert not result.ok
    assert "60 cards" in result.errors[0]


def test_validate_deck_allows_many_basic_energy() -> None:
    cards = pd.DataFrame(
        [
            {"Card ID": 1, "Card Name": "Basic Water Energy", "Stage": "Basic Energy", "Category": "", "Rule": ""},
        ]
    )

    result = validate_deck([1] * 60, cards)

    assert result.ok
