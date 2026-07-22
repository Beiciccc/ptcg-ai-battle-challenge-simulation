from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from pokemon_benchmark.common import now_iso, resolve_path, sha256_text, write_json
from pokemon_benchmark.table_io import read_table, write_table


OPTION_ROW_FIELDS = [
    "decision_id",
    "archive_date",
    "episode_id",
    "player",
    "team",
    "opponent_team",
    "archetype",
    "deck_hash",
    "opponent_archetype",
    "opponent_deck_hash",
    "reward",
    "is_winner",
    "evidence_source",
    "trajectory_teacher",
    "trajectory_opponent",
    "step_idx",
    "context",
    "min_count",
    "max_count",
    "n_options",
    "option_pos",
    "option_index",
    "option_type",
    "option_signature",
    "is_chosen",
    "label_count",
    "turn",
    "turn_action_count",
    "your_index",
    "first_player",
    "energy_attached",
    "supporter_played",
    "stadium_played",
    "retreated",
    "own_active_id",
    "own_active_hp",
    "own_active_max_hp",
    "own_active_damage",
    "own_active_energy_count",
    "own_bench_count",
    "own_hand_count",
    "own_deck_count",
    "own_discard_count",
    "own_prize_unknown_count",
    "own_active_ids",
    "own_bench_ids",
    "own_hand_ids",
    "own_discard_ids",
    "own_energy_ids",
    "opp_active_id",
    "opp_active_hp",
    "opp_active_max_hp",
    "opp_active_damage",
    "opp_active_energy_count",
    "opp_bench_count",
    "opp_hand_count",
    "opp_deck_count",
    "opp_discard_count",
    "opp_prize_unknown_count",
    "opp_active_ids",
    "opp_bench_ids",
    "opp_discard_ids",
    "opp_energy_ids",
    "option_area",
    "option_in_play_area",
    "option_in_play_index",
    "option_card_id",
    "option_attack_id",
    "option_energy_type",
    "option_target_player",
]


def parse_json(value: Any, default: Any) -> Any:
    if isinstance(value, (dict, list)):
        return value
    if value is None:
        return default
    try:
        if value != value:  # NaN
            return default
    except Exception:
        pass
    try:
        return json.loads(str(value))
    except Exception:
        return default


def as_int(value: Any, default: int = 0) -> int:
    try:
        if value is None or value == "":
            return default
        return int(value)
    except Exception:
        return default


def as_bool_int(value: Any) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)):
        return int(bool(value))
    if isinstance(value, str):
        return int(value.lower() in {"1", "true", "yes"})
    return 0


def as_text(value: Any, default: str = "") -> str:
    if value is None:
        return default
    try:
        if value != value:  # NaN
            return default
    except Exception:
        pass
    text = str(value)
    return text if text else default


def safe_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def first_card(cards: Any) -> dict[str, Any]:
    items = safe_list(cards)
    if items and isinstance(items[0], dict):
        return items[0]
    return {}


def card_energy_count(card: dict[str, Any]) -> int:
    energies = card.get("energies")
    if isinstance(energies, list):
        return len(energies)
    energy_cards = card.get("energyCards")
    if isinstance(energy_cards, list):
        return len(energy_cards)
    return 0


def card_ids(cards: Any) -> str:
    return "|".join(str(as_int(card.get("id"), -1)) for card in safe_list(cards) if isinstance(card, dict))


def energy_ids(cards: Any) -> str:
    values: list[str] = []
    for card in safe_list(cards):
        if not isinstance(card, dict):
            continue
        energies = safe_list(card.get("energyCards"))
        if not energies:
            energies = safe_list(card.get("energies"))
        for energy in energies:
            if isinstance(energy, dict):
                values.append(str(as_int(energy.get("id"), -1)))
            else:
                values.append(str(as_int(energy, -1)))
    return "|".join(values)


def player_features(player: dict[str, Any], prefix: str) -> dict[str, Any]:
    active = first_card(player.get("active"))
    hp = as_int(active.get("hp"), 0)
    max_hp = as_int(active.get("maxHp"), 0)
    return {
        f"{prefix}_active_id": as_int(active.get("id"), -1),
        f"{prefix}_active_hp": hp,
        f"{prefix}_active_max_hp": max_hp,
        f"{prefix}_active_damage": max(0, max_hp - hp) if max_hp else 0,
        f"{prefix}_active_energy_count": card_energy_count(active),
        f"{prefix}_bench_count": len(safe_list(player.get("bench"))),
        f"{prefix}_hand_count": as_int(player.get("handCount"), len(safe_list(player.get("hand")))),
        f"{prefix}_deck_count": as_int(player.get("deckCount"), 0),
        f"{prefix}_discard_count": len(safe_list(player.get("discard"))),
        f"{prefix}_prize_unknown_count": sum(1 for prize in safe_list(player.get("prize")) if prize is None),
        f"{prefix}_active_ids": card_ids(player.get("active")),
        f"{prefix}_bench_ids": card_ids(player.get("bench")),
        f"{prefix}_hand_ids": card_ids(player.get("hand")),
        f"{prefix}_discard_ids": card_ids(player.get("discard")),
        f"{prefix}_energy_ids": energy_ids(safe_list(player.get("active")) + safe_list(player.get("bench"))),
    }


def option_card_id(option: dict[str, Any]) -> int:
    for key in ("cardId", "card_id", "id"):
        if key in option:
            return as_int(option.get(key), -1)
    card = option.get("card")
    if isinstance(card, dict):
        return as_int(card.get("id"), -1)
    return -1


def option_attack_id(option: dict[str, Any]) -> int:
    for key in ("attackId", "attack_id", "attack"):
        if key in option:
            return as_int(option.get(key), -1)
    return -1


def card_from_area(current: dict[str, Any], *, player_index: int, area: int, index: int) -> dict[str, Any]:
    players = safe_list(current.get("players"))
    player = players[player_index] if 0 <= player_index < len(players) and isinstance(players[player_index], dict) else {}
    if area == 2:  # HAND
        cards = safe_list(player.get("hand"))
    elif area == 3:  # DISCARD
        cards = safe_list(player.get("discard"))
    elif area == 4:  # ACTIVE
        cards = safe_list(player.get("active"))
    elif area == 5:  # BENCH
        cards = safe_list(player.get("bench"))
    elif area == 6:  # PRIZE
        cards = safe_list(player.get("prize"))
    elif area == 7:  # STADIUM
        cards = safe_list(current.get("stadium"))
    elif area == 9:  # LOOKING
        cards = safe_list(current.get("looking"))
    else:
        cards = []
    if 0 <= index < len(cards) and isinstance(cards[index], dict):
        return cards[index]
    return {}


def resolve_option_card_id(option: dict[str, Any], current: dict[str, Any], your_index: int) -> int:
    direct = option_card_id(option)
    if direct >= 0:
        return direct
    opt_type = as_int(option.get("type"), -1)
    index = as_int(option.get("index"), -1)
    player_index = as_int(option.get("playerIndex"), your_index)
    if opt_type in {7, 8, 9}:  # PLAY / ATTACH / EVOLVE from hand
        card = card_from_area(current, player_index=your_index, area=2, index=index)
        return as_int(card.get("id"), -1)
    if opt_type == 10:  # ABILITY from board/stadium
        area = as_int(option.get("area"), -1)
        card = card_from_area(current, player_index=your_index, area=area, index=index)
        return as_int(card.get("id"), -1)
    if opt_type == 13:  # ATTACK from active Pokemon
        card = card_from_area(current, player_index=your_index, area=4, index=0)
        return as_int(card.get("id"), -1)
    if opt_type == 3:  # CARD selection context
        area = as_int(option.get("area"), -1)
        card = card_from_area(current, player_index=player_index, area=area, index=index)
        return as_int(card.get("id"), -1)
    return -1


def option_signature(option: dict[str, Any], resolved_card_id: int | None = None) -> str:
    card_id = option_card_id(option) if resolved_card_id is None else resolved_card_id
    salient = {
        "type": option.get("type", ""),
        "area": option.get("area", ""),
        "inPlayArea": option.get("inPlayArea", ""),
        "inPlayIndex": option.get("inPlayIndex", ""),
        "card": card_id,
        "attack": option_attack_id(option),
        "energy": option.get("energyType", option.get("energy", "")),
        "targetPlayer": option.get("targetPlayer", option.get("playerIndex", "")),
    }
    text = json.dumps(salient, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
    return sha256_text(text)[:16]


def option_features(option: Any, option_pos: int, current: dict[str, Any] | None = None, your_index: int = 0) -> dict[str, Any]:
    if not isinstance(option, dict):
        option = {}
    current = current or {}
    resolved_card_id = resolve_option_card_id(option, current, your_index)
    return {
        "option_pos": option_pos,
        "option_index": as_int(option.get("index"), option_pos),
        "option_type": str(option.get("type", "")),
        "option_signature": option_signature(option, resolved_card_id),
        "option_area": as_int(option.get("area"), -1),
        "option_in_play_area": as_int(option.get("inPlayArea"), -1),
        "option_in_play_index": as_int(option.get("inPlayIndex"), -1),
        "option_card_id": resolved_card_id,
        "option_attack_id": option_attack_id(option),
        "option_energy_type": str(option.get("energyType", option.get("energy", ""))),
        "option_target_player": as_int(option.get("targetPlayer", option.get("playerIndex")), -1),
    }


def base_features(row: dict[str, Any]) -> dict[str, Any]:
    current = parse_json(row.get("current_compact"), {})
    your_index = as_int(current.get("yourIndex"), as_int(row.get("player"), 0))
    opp_index = 1 - your_index if your_index in (0, 1) else 1
    players = safe_list(current.get("players"))
    own = players[your_index] if your_index < len(players) and isinstance(players[your_index], dict) else {}
    opp = players[opp_index] if opp_index < len(players) and isinstance(players[opp_index], dict) else {}
    features = {
        "archive_date": row.get("archive_date", ""),
        "episode_id": row.get("episode_id", ""),
        "player": as_int(row.get("player"), -1),
        "team": row.get("team", ""),
        "opponent_team": row.get("opponent_team", ""),
        "archetype": row.get("archetype", ""),
        "deck_hash": row.get("deck_hash", ""),
        "opponent_archetype": row.get("opponent_archetype", ""),
        "opponent_deck_hash": row.get("opponent_deck_hash", ""),
        "reward": as_int(row.get("reward"), 1),
        "is_winner": as_int(row.get("is_winner"), 1),
        "evidence_source": as_text(row.get("evidence_source"), "official_replay"),
        "trajectory_teacher": as_text(row.get("trajectory_teacher")),
        "trajectory_opponent": as_text(row.get("trajectory_opponent")),
        "step_idx": as_int(row.get("step_idx"), 0),
        "context": str(row.get("context", "")),
        "min_count": as_int(row.get("min_count"), 0),
        "max_count": as_int(row.get("max_count"), 0),
        "n_options": as_int(row.get("n_options"), 0),
        "turn": as_int(current.get("turn"), 0),
        "turn_action_count": as_int(current.get("turnActionCount"), 0),
        "your_index": your_index,
        "first_player": as_int(current.get("firstPlayer"), -1),
        "energy_attached": as_bool_int(current.get("energyAttached")),
        "supporter_played": as_bool_int(current.get("supporterPlayed")),
        "stadium_played": as_bool_int(current.get("stadiumPlayed")),
        "retreated": as_bool_int(current.get("retreated")),
    }
    features.update(player_features(own, "own"))
    features.update(player_features(opp, "opp"))
    return features


def dataframe_to_records(table: Any) -> list[dict[str, Any]]:
    if hasattr(table, "to_dict"):
        return table.to_dict(orient="records")
    return list(table)


def build_option_rows(
    decisions: list[dict[str, Any]],
    *,
    archetype_filter: set[str],
    deck_hash_filter: set[str] | None = None,
    team_filter: set[str] | None = None,
    max_decisions: int,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    archetype_counts: Counter[str] = Counter()
    option_type_counts: Counter[str] = Counter()
    decisions_seen = 0
    decisions_kept = 0
    skipped_archetype = 0
    skipped_deck_hash = 0
    skipped_team = 0
    skipped_no_options = 0

    for raw in decisions:
        decisions_seen += 1
        archetype = str(raw.get("archetype", ""))
        if archetype_filter and archetype not in archetype_filter:
            skipped_archetype += 1
            continue
        if deck_hash_filter and str(raw.get("deck_hash", "")) not in deck_hash_filter:
            skipped_deck_hash += 1
            continue
        if team_filter and str(raw.get("team", "")) not in team_filter:
            skipped_team += 1
            continue
        options = parse_json(raw.get("options"), [])
        if not isinstance(options, list) or not options:
            skipped_no_options += 1
            continue
        labels = set(as_int(x, -1) for x in parse_json(raw.get("label_indices"), []))
        decision_id = sha256_text(
            "|".join(
                [
                    str(raw.get("archive_date", "")),
                    str(raw.get("episode_id", "")),
                    str(raw.get("player", "")),
                    str(raw.get("step_idx", "")),
                    str(raw.get("context", "")),
                ]
            )
        )[:20]
        current = parse_json(raw.get("current_compact"), {})
        your_index = as_int(current.get("yourIndex"), as_int(raw.get("player"), 0))
        base = base_features(raw)
        decisions_kept += 1
        archetype_counts[archetype] += 1
        for pos, option in enumerate(options):
            out = dict(base)
            out["decision_id"] = decision_id
            out.update(option_features(option, pos, current=current, your_index=your_index))
            out["is_chosen"] = int(pos in labels)
            out["label_count"] = len(labels)
            option_type_counts[str(out["option_type"])] += 1
            rows.append(out)
        if max_decisions and decisions_kept >= max_decisions:
            break

    manifest = {
        "created_at": now_iso(),
        "decisions_seen": decisions_seen,
        "decisions_kept": decisions_kept,
        "option_rows": len(rows),
        "skipped_archetype": skipped_archetype,
        "skipped_deck_hash": skipped_deck_hash,
        "skipped_team": skipped_team,
        "skipped_no_options": skipped_no_options,
        "archetype_filter": sorted(archetype_filter),
        "deck_hash_filter": sorted(deck_hash_filter or set()),
        "team_filter": sorted(team_filter or set()),
        "archetype_decisions": dict(sorted(archetype_counts.items())),
        "option_type_rows": dict(sorted(option_type_counts.items())),
    }
    return rows, manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Expand compact CABT decisions into legal-option feature rows.")
    parser.add_argument("--decisions", required=True, help="DecisionStore directory or decisions parquet/csv path.")
    parser.add_argument("--out", required=True, help="Output directory or option_rows parquet/csv path.")
    parser.add_argument("--archetype", action="append", default=[], help="Optional archetype filter. Repeatable.")
    parser.add_argument("--deck-hash", action="append", default=[], help="Optional exact deck hash filter. Repeatable.")
    parser.add_argument("--team", action="append", default=[], help="Optional team display-ID filter. Repeatable.")
    parser.add_argument("--max-decisions", type=int, default=0, help="Optional cap after filtering.")
    parser.add_argument("--csv-sidecar-max-rows", type=int, default=20000)
    args = parser.parse_args()

    decision_path = resolve_path(args.decisions)
    if decision_path.is_dir():
        decision_path = decision_path / "decisions.parquet"
    out_path = resolve_path(args.out)
    if out_path.suffix.lower() not in {".parquet", ".csv"}:
        out_dir = out_path
        out_path = out_dir / "option_rows.parquet"
    else:
        out_dir = out_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    decisions = dataframe_to_records(read_table(decision_path))
    rows, manifest = build_option_rows(
        decisions,
        archetype_filter=set(args.archetype),
        deck_hash_filter=set(args.deck_hash),
        team_filter=set(args.team),
        max_decisions=args.max_decisions,
    )
    manifest.update(
        {
            "decision_path": str(decision_path),
            "out_path": str(out_path),
            "fields": OPTION_ROW_FIELDS,
        }
    )
    ordered_rows = [{field: row.get(field, "") for field in OPTION_ROW_FIELDS} for row in rows]
    write_table(out_path, ordered_rows, csv_sidecar_max_rows=args.csv_sidecar_max_rows)
    write_json(out_dir / "option_rows_manifest.json", manifest)
    print("OPTION_ROWS_DONE", json.dumps(manifest, sort_keys=True))


if __name__ == "__main__":
    main()
