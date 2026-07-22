from __future__ import annotations

import hashlib
import math
from collections import defaultdict
from typing import Any

from pokemon_benchmark.option_feature_rows import base_features, option_features


FEATURE_SCHEMA_VERSION = "pilot-state-v2.1"


def _as_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None or value == "":
            return default
        out = float(value)
        return out if math.isfinite(out) else default
    except Exception:
        return default


def _as_int(value: Any, default: int = 0) -> int:
    try:
        if value is None or value == "":
            return default
        return int(value)
    except Exception:
        return default


def _clip(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _bucket(value: int, cuts: tuple[int, ...]) -> str:
    for cut in cuts:
        if value <= cut:
            return f"le{cut}"
    return f"gt{cuts[-1]}"


def _ids(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(_as_int(item, -1)) for item in value]
    text = str(value or "")
    return [part for part in text.split("|") if part]


def _add_numeric(features: dict[str, float], name: str, value: Any, scale: float, limit: float = 3.0) -> None:
    features[f"num:{name}"] = _clip(_as_float(value) / scale, -limit, limit)


def _add_categorical(features: dict[str, float], name: str, value: Any) -> None:
    features[f"cat:{name}={value}"] = 1.0


def row_feature_map(row: dict[str, Any]) -> dict[str, float]:
    """Return train/serve-stable state-option features for one legal option."""
    out: dict[str, float] = {"bias": 1.0}
    context = str(row.get("context", ""))
    option_type = str(row.get("option_type", ""))
    card_id = str(_as_int(row.get("option_card_id"), -1))
    attack_id = str(_as_int(row.get("option_attack_id"), -1))
    own_active = str(_as_int(row.get("own_active_id"), -1))
    opp_active = str(_as_int(row.get("opp_active_id"), -1))
    turn = _as_int(row.get("turn"), 0)
    turn_bucket = _bucket(turn, (1, 2, 4, 7, 11, 16))
    own_deck_bucket = _bucket(_as_int(row.get("own_deck_count"), 0), (5, 10, 20, 30, 40))
    opp_deck_bucket = _bucket(_as_int(row.get("opp_deck_count"), 0), (5, 10, 20, 30, 40))
    decision_family = str(row.get("decision_family", ""))
    game_phase = str(row.get("game_phase", ""))
    opponent_belief = str(row.get("opponent_belief_top", ""))
    belief_bucket = _bucket(int(_as_float(row.get("opponent_belief_confidence"), 0.0) * 10), (2, 4, 6, 8))

    categorical = {
        "context": context,
        "option_type": option_type,
        "option_signature": row.get("option_signature", ""),
        "card": card_id,
        "attack": attack_id,
        "option_area": _as_int(row.get("option_area"), -1),
        "in_play_area": _as_int(row.get("option_in_play_area"), -1),
        "energy_type": row.get("option_energy_type", ""),
        "target_player": _as_int(row.get("option_target_player"), -1),
        "own_active": own_active,
        "opp_active": opp_active,
        "turn_bucket": turn_bucket,
        "own_deck_bucket": own_deck_bucket,
        "opp_deck_bucket": opp_deck_bucket,
        "first_player": _as_int(row.get("first_player"), -1),
        "energy_attached": _as_int(row.get("energy_attached"), 0),
        "supporter_played": _as_int(row.get("supporter_played"), 0),
        "stadium_played": _as_int(row.get("stadium_played"), 0),
        "retreated": _as_int(row.get("retreated"), 0),
    }
    if decision_family or "decision_family" in row:
        categorical["decision_family"] = decision_family
        categorical["game_phase"] = game_phase
        categorical["opponent_belief"] = opponent_belief
        categorical["belief_bucket"] = belief_bucket
        categorical["forced_choice"] = _as_int(row.get("forced_choice"), 0)
        categorical["critical_choice"] = _as_int(row.get("critical_choice"), 0)
    for name, value in categorical.items():
        _add_categorical(out, name, value)

    interactions = {
        "context_type": f"{context}|{option_type}",
        "context_card": f"{context}|{card_id}",
        "context_attack": f"{context}|{attack_id}",
        "type_turn": f"{option_type}|{turn_bucket}",
        "card_turn": f"{card_id}|{turn_bucket}",
        "card_own_active": f"{card_id}|{own_active}",
        "card_opp_active": f"{card_id}|{opp_active}",
        "card_deck_pressure": f"{card_id}|{own_deck_bucket}|{opp_deck_bucket}",
        "type_energy_used": f"{option_type}|{categorical['energy_attached']}",
        "type_supporter_used": f"{option_type}|{categorical['supporter_played']}",
    }
    if decision_family or "decision_family" in row:
        interactions.update(
            {
                "family_type": f"{decision_family}|{option_type}",
                "family_card": f"{decision_family}|{card_id}",
                "family_phase_type": f"{decision_family}|{game_phase}|{option_type}",
                "belief_type": f"{opponent_belief}|{option_type}",
                "belief_card": f"{opponent_belief}|{card_id}",
                "belief_active_option": f"{opponent_belief}|{opp_active}|{card_id}",
            }
        )
    for name, value in interactions.items():
        _add_categorical(out, name, value)

    numeric_scales = {
        "turn": 10.0,
        "turn_action_count": 10.0,
        "n_options": 10.0,
        "min_count": 5.0,
        "max_count": 5.0,
        "option_pos": 10.0,
        "own_active_hp": 300.0,
        "own_active_max_hp": 300.0,
        "own_active_damage": 300.0,
        "own_active_energy_count": 4.0,
        "own_bench_count": 5.0,
        "own_hand_count": 10.0,
        "own_deck_count": 60.0,
        "own_discard_count": 30.0,
        "own_prize_unknown_count": 6.0,
        "opp_active_hp": 300.0,
        "opp_active_max_hp": 300.0,
        "opp_active_damage": 300.0,
        "opp_active_energy_count": 4.0,
        "opp_bench_count": 5.0,
        "opp_hand_count": 10.0,
        "opp_deck_count": 60.0,
        "opp_discard_count": 30.0,
        "opp_prize_unknown_count": 6.0,
    }
    for name, scale in numeric_scales.items():
        _add_numeric(out, name, row.get(name), scale)
    if decision_family or "decision_family" in row:
        _add_numeric(out, "impact_weight", row.get("impact_weight"), 2.0)
        _add_numeric(out, "opponent_belief_confidence", row.get("opponent_belief_confidence"), 1.0)
        _add_numeric(out, "opponent_belief_entropy", row.get("opponent_belief_entropy"), 1.0)

    own_hp = _as_float(row.get("own_active_hp"))
    own_max = max(1.0, _as_float(row.get("own_active_max_hp"), 1.0))
    opp_hp = _as_float(row.get("opp_active_hp"))
    opp_max = max(1.0, _as_float(row.get("opp_active_max_hp"), 1.0))
    out["num:own_hp_ratio"] = _clip(own_hp / own_max, 0.0, 1.0)
    out["num:opp_hp_ratio"] = _clip(opp_hp / opp_max, 0.0, 1.0)
    out["num:deck_count_gap"] = _clip(
        (_as_float(row.get("own_deck_count")) - _as_float(row.get("opp_deck_count"))) / 60.0,
        -1.0,
        1.0,
    )
    out["num:prize_gap"] = _clip(
        (_as_float(row.get("own_prize_unknown_count")) - _as_float(row.get("opp_prize_unknown_count"))) / 6.0,
        -1.0,
        1.0,
    )

    for zone in ("own_active_ids", "own_bench_ids", "own_hand_ids", "own_discard_ids", "own_energy_ids"):
        for card in _ids(row.get(zone)):
            _add_categorical(out, zone, card)
            _add_categorical(out, f"{zone}_option", f"{card}|{card_id}")
    for zone in ("opp_active_ids", "opp_bench_ids", "opp_discard_ids", "opp_energy_ids"):
        for card in _ids(row.get(zone)):
            _add_categorical(out, zone, card)
            _add_categorical(out, f"{zone}_option", f"{card}|{card_id}")
    return out


def live_option_row(obs_dict: dict[str, Any], option: dict[str, Any], option_pos: int) -> dict[str, Any]:
    current = obs_dict.get("current") or {}
    select = obs_dict.get("select") or {}
    row = {
        "current_compact": current,
        "player": current.get("yourIndex", 0),
        "step_idx": current.get("turnActionCount", 0),
        "context": select.get("context", ""),
        "min_count": select.get("minCount", 0),
        "max_count": select.get("maxCount", 0),
        "n_options": len(select.get("option") or []),
    }
    features = base_features(row)
    features.update(option_features(option, option_pos, current=current, your_index=_as_int(current.get("yourIndex"), 0)))
    return features


def hashed_feature_map(features: dict[str, float], dimension: int) -> dict[int, float]:
    out: dict[int, float] = defaultdict(float)
    for name, value in features.items():
        if not value:
            continue
        digest = hashlib.sha256(name.encode("utf-8")).digest()
        index = int.from_bytes(digest[:8], "big") % dimension
        sign = 1.0 if digest[8] & 1 else -1.0
        out[index] += sign * float(value)
    return dict(out)


def linear_score(weights: list[float], features: dict[str, float]) -> float:
    vector = hashed_feature_map(features, len(weights))
    return sum(weights[index] * value for index, value in vector.items())


def sigmoid(value: float) -> float:
    if value >= 0:
        z = math.exp(-min(value, 40.0))
        return 1.0 / (1.0 + z)
    z = math.exp(max(value, -40.0))
    return z / (1.0 + z)
