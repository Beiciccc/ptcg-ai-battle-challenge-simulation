from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import unicodedata

import pandas as pd

from ptcg_battle.cards import (
    CARD_ID_COL,
    CARD_NAME_COL,
    CATEGORY_COL,
    RULE_COL,
    one_row_per_card,
    read_english_cards,
    stage_column,
)
from ptcg_battle.paths import EN_CARD_DATA


@dataclass(frozen=True)
class DeckValidationResult:
    card_count: int
    errors: tuple[str, ...]
    warnings: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.errors


def read_deck(path: str | Path) -> list[int]:
    deck_path = Path(path)
    if not deck_path.exists():
        raise FileNotFoundError(f"Missing deck file: {deck_path}")

    cards: list[int] = []
    for line_number, raw_line in enumerate(deck_path.read_text().splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        try:
            cards.append(int(line))
        except ValueError as exc:
            raise ValueError(f"Invalid card id on line {line_number}: {line}") from exc
    return cards


def load_default_card_data(path: str | Path = EN_CARD_DATA) -> pd.DataFrame:
    return read_english_cards(path)


def validate_deck(deck: list[int], card_data: pd.DataFrame) -> DeckValidationResult:
    errors: list[str] = []
    warnings: list[str] = []

    if len(deck) != 60:
        errors.append(f"Deck must contain 60 cards; found {len(deck)}.")

    compact = one_row_per_card(card_data)
    known_ids = set(compact[CARD_ID_COL].astype(int))
    unknown = sorted(set(deck).difference(known_ids))
    if unknown:
        errors.append(f"Deck contains unknown card ids: {unknown[:10]}.")

    if errors:
        return DeckValidationResult(len(deck), tuple(errors), tuple(warnings))

    by_id = compact.set_index(CARD_ID_COL, drop=False)
    stage_col = stage_column(compact.columns)
    counts = Counter(deck)
    counts_by_name: Counter[str] = Counter()
    ace_spec_count = 0
    basic_pokemon_count = 0

    for card_id, count in counts.items():
        row = by_id.loc[card_id]
        name = str(row[CARD_NAME_COL])
        counts_by_name[name] += count

        if _is_ace_spec(row):
            ace_spec_count += count
        if _is_basic_pokemon(row, stage_col):
            basic_pokemon_count += count

    for name, count in counts_by_name.items():
        if count <= 4:
            continue
        matching_rows = compact[compact[CARD_NAME_COL] == name]
        if not any(_is_basic_energy(row, stage_col) for _, row in matching_rows.iterrows()):
            errors.append(f"More than 4 copies of non-basic-energy card: {name} ({count}).")

    if ace_spec_count > 1:
        errors.append(f"Deck contains more than 1 ACE SPEC card ({ace_spec_count}).")

    if basic_pokemon_count == 0:
        warnings.append("Deck appears to contain no Basic Pokemon.")

    return DeckValidationResult(len(deck), tuple(errors), tuple(warnings))


def _text(value: object) -> str:
    if value is None or pd.isna(value):
        return ""
    return str(value).strip()


def _key(value: object) -> str:
    text = unicodedata.normalize("NFKD", _text(value))
    return text.encode("ascii", "ignore").decode("ascii").lower()


def _is_basic_energy(row: pd.Series, stage_col: str) -> bool:
    stage = _key(row.get(stage_col))
    category = _key(row.get(CATEGORY_COL))
    name = _key(row.get(CARD_NAME_COL))
    return (
        stage == "basic energy"
        or category == "basic energy"
        or (name.startswith("basic ") and "energy" in name)
    )


def _is_basic_pokemon(row: pd.Series, stage_col: str) -> bool:
    stage = _key(row.get(stage_col))
    category = _key(row.get(CATEGORY_COL))
    return (stage == "basic" and "pokemon" in category) or stage == "basic pokemon"


def _is_ace_spec(row: pd.Series) -> bool:
    return "ace spec" in _key(row.get(RULE_COL))
