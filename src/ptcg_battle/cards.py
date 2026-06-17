from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

from ptcg_battle.paths import EN_CARD_DATA

CARD_ID_COL = "Card ID"
CARD_NAME_COL = "Card Name"
CATEGORY_COL = "Category"
RULE_COL = "Rule"

REQUIRED_EN_COLUMNS = {
    CARD_ID_COL,
    CARD_NAME_COL,
    "Expansion",
    "Collection No.",
    CATEGORY_COL,
    RULE_COL,
    "HP",
    "Type",
    "Move Name",
    "Cost",
    "Damage",
    "Effect Explanation",
}


def stage_column(columns: Iterable[str]) -> str:
    for column in columns:
        if column.startswith("Stage"):
            return column
    raise ValueError("Could not find stage/type column in card data.")


def read_english_cards(path: str | Path = EN_CARD_DATA) -> pd.DataFrame:
    card_path = Path(path)
    if not card_path.exists():
        raise FileNotFoundError(
            f"Missing card data: {card_path}. Run tools/download_assets.py first."
        )

    cards = pd.read_csv(card_path)
    missing = REQUIRED_EN_COLUMNS.difference(cards.columns)
    if missing:
        missing_text = ", ".join(sorted(missing))
        raise ValueError(f"Card data is missing required columns: {missing_text}")
    stage_column(cards.columns)
    return cards


def one_row_per_card(cards: pd.DataFrame) -> pd.DataFrame:
    return cards.drop_duplicates(subset=[CARD_ID_COL], keep="first").copy()


def summarize_cards(cards: pd.DataFrame) -> dict[str, int]:
    compact = one_row_per_card(cards)
    return {
        "rows": int(len(cards)),
        "unique_cards": int(compact[CARD_ID_COL].nunique()),
        "min_card_id": int(compact[CARD_ID_COL].min()),
        "max_card_id": int(compact[CARD_ID_COL].max()),
    }
