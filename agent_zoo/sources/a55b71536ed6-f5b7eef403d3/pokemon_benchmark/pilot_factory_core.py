from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from typing import Any, Iterable


FACTORY_SCHEMA_VERSION = "pilot-factory-v3.0"

DEFAULT_PHASE_CUTS = (2, 6, 12)

CONTEXT_FAMILY = {
    0: "main_action",
    1: "setup",
    2: "setup",
    3: "switch",
    4: "switch",
    5: "switch",
    6: "setup",
    7: "search",
    8: "discard",
    9: "deck_management",
    10: "deck_management",
    11: "deck_management",
    12: "deck_management",
    13: "damage_target",
    14: "damage_target",
    15: "damage_target",
    16: "damage_target",
    17: "damage_target",
    18: "evolution",
    19: "evolution",
    20: "evolution",
    21: "attach",
    22: "attach",
    23: "attach",
    24: "search",
    25: "effect_target",
    26: "energy_management",
    27: "discard",
    28: "energy_management",
    29: "discard",
    30: "energy_management",
    31: "energy_management",
    32: "energy_management",
    33: "energy_management",
    34: "skill_order",
    35: "attack",
    36: "attack",
    37: "evolution",
    38: "count",
    39: "count",
    40: "count",
    41: "first_player",
    42: "mulligan",
    43: "yes_no",
    44: "yes_no",
    45: "yes_no",
    46: "yes_no",
    47: "special_condition",
    48: "special_condition",
}

FAMILY_IMPACT = {
    "main_action": 1.50,
    "setup": 1.45,
    "search": 1.50,
    "discard": 1.55,
    "deck_management": 1.25,
    "switch": 1.55,
    "attach": 1.55,
    "evolution": 1.50,
    "damage_target": 1.80,
    "effect_target": 1.70,
    "energy_management": 1.45,
    "attack": 1.90,
    "skill_order": 1.30,
    "count": 1.10,
    "first_player": 1.65,
    "mulligan": 1.20,
    "yes_no": 1.25,
    "special_condition": 1.15,
    "other": 1.00,
}


def as_int(value: Any, default: int = 0) -> int:
    try:
        if value is None or value == "":
            return default
        return int(value)
    except Exception:
        return default


def as_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None or value == "":
            return default
        out = float(value)
        return out if math.isfinite(out) else default
    except Exception:
        return default


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


def safe_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def decision_family(context: Any) -> str:
    return CONTEXT_FAMILY.get(as_int(context, -1), "other")


def game_phase(turn: Any, phase_cuts: tuple[int, int, int] = DEFAULT_PHASE_CUTS) -> str:
    value = as_int(turn, 0)
    opening_cut, setup_cut, pressure_cut = phase_cuts
    if value <= opening_cut:
        return "opening"
    if value <= setup_cut:
        return "setup"
    if value <= pressure_cut:
        return "pressure"
    return "closing"


def forced_choice(n_options: Any, min_count: Any, max_count: Any) -> bool:
    n = max(0, as_int(n_options, 0))
    low = max(0, as_int(min_count, 0))
    high = max(low, as_int(max_count, low))
    if n == 0:
        return True
    if low == high == n:
        return True
    return n == 1 and low >= 1


def impact_weight(
    family: str,
    *,
    is_forced: bool,
    n_options: Any,
    turn: Any,
    own_prizes: Any = 6,
    opp_prizes: Any = 6,
) -> float:
    if is_forced:
        return 0.10
    weight = FAMILY_IMPACT.get(family, 1.0)
    n = max(1, as_int(n_options, 1))
    weight *= 1.0 + min(0.30, math.log2(n) * 0.06)
    if min(as_int(own_prizes, 6), as_int(opp_prizes, 6)) <= 2:
        weight *= 1.12
    if as_int(turn, 0) <= 2 and family in {"setup", "main_action", "first_player", "mulligan"}:
        weight *= 1.08
    return round(min(3.0, max(0.1, weight)), 6)


def _card_ids(cards: Any) -> list[int]:
    out: list[int] = []
    for card in safe_list(cards):
        if not isinstance(card, dict):
            continue
        card_id = as_int(card.get("id"), -1)
        if card_id >= 0:
            out.append(card_id)
        for key in ("energyCards", "energies", "tools", "preEvolution"):
            for nested in safe_list(card.get(key)):
                if isinstance(nested, dict):
                    nested_id = as_int(nested.get("id"), -1)
                else:
                    nested_id = as_int(nested, -1)
                if nested_id >= 0:
                    out.append(nested_id)
    return out


def visible_opponent_card_ids(current: Any, your_index: Any = None) -> list[int]:
    state = parse_json(current, {})
    if not isinstance(state, dict):
        return []
    mine = as_int(state.get("yourIndex"), 0) if your_index is None else as_int(your_index, 0)
    opponent = 1 - mine if mine in (0, 1) else 1
    players = safe_list(state.get("players"))
    if not (0 <= opponent < len(players)) or not isinstance(players[opponent], dict):
        return []
    player = players[opponent]
    ids: list[int] = []
    for zone in ("active", "bench", "discard"):
        ids.extend(_card_ids(player.get(zone)))
    ids.extend(_card_ids(state.get("stadium")))
    return sorted(set(ids))


def _softmax(scores: dict[str, float]) -> dict[str, float]:
    if not scores:
        return {}
    peak = max(scores.values())
    exp_scores = {key: math.exp(max(-60.0, min(0.0, value - peak))) for key, value in scores.items()}
    total = sum(exp_scores.values()) or 1.0
    return {key: value / total for key, value in exp_scores.items()}


def normalized_entropy(probabilities: dict[str, float]) -> float:
    if len(probabilities) <= 1:
        return 0.0
    entropy = -sum(value * math.log(max(value, 1e-15)) for value in probabilities.values())
    return entropy / math.log(len(probabilities))


def build_belief_model(
    decision_rows: Iterable[dict[str, Any]],
    *,
    min_archetype_episodes: int = 20,
    min_card_episodes: int = 2,
    alpha: float = 0.5,
    max_archetypes: int = 24,
) -> dict[str, Any]:
    episode_cards: dict[tuple[str, str, str], set[int]] = defaultdict(set)
    for row in decision_rows:
        archetype = str(row.get("opponent_archetype", "")).strip()
        if not archetype:
            continue
        episode_key = (str(row.get("archive_date", "")), str(row.get("episode_id", "")), archetype)
        current = row.get("current_compact", row.get("current", {}))
        episode_cards[episode_key].update(visible_opponent_card_ids(current, row.get("player")))

    archetype_episodes: Counter[str] = Counter()
    card_docs: dict[str, Counter[int]] = defaultdict(Counter)
    global_card_docs: Counter[int] = Counter()
    for (_date, _episode, archetype), cards in episode_cards.items():
        archetype_episodes[archetype] += 1
        for card_id in cards:
            card_docs[archetype][card_id] += 1
            global_card_docs[card_id] += 1

    selected = [
        archetype
        for archetype, count in archetype_episodes.most_common(max_archetypes)
        if count >= min_archetype_episodes
    ]
    if not selected:
        selected = [archetype for archetype, _count in archetype_episodes.most_common(max_archetypes)]
    total = sum(archetype_episodes[archetype] for archetype in selected) or 1
    priors = {archetype: archetype_episodes[archetype] / total for archetype in selected}
    vocabulary = sorted(card_id for card_id, count in global_card_docs.items() if count >= min_card_episodes)
    card_log_prob: dict[str, dict[str, float]] = {}
    default_log_prob: dict[str, float] = {}
    for archetype in selected:
        n = archetype_episodes[archetype]
        denom = n + 2.0 * alpha
        default_log_prob[archetype] = math.log(alpha / denom)
        card_log_prob[archetype] = {
            str(card_id): round(math.log((card_docs[archetype][card_id] + alpha) / denom), 8)
            for card_id in vocabulary
            if card_docs[archetype][card_id] > 0
        }
    return {
        "schema_version": FACTORY_SCHEMA_VERSION,
        "alpha": alpha,
        "min_archetype_episodes": min_archetype_episodes,
        "min_card_episodes": min_card_episodes,
        "episode_count": len(episode_cards),
        "archetypes": selected,
        "archetype_episodes": {key: archetype_episodes[key] for key in selected},
        "priors": priors,
        "default_log_prob": default_log_prob,
        "card_log_prob": card_log_prob,
        "vocabulary_size": len(vocabulary),
    }


def infer_opponent_belief(model: dict[str, Any], visible_ids: Iterable[int]) -> dict[str, Any]:
    archetypes = [str(value) for value in model.get("archetypes", [])]
    priors = model.get("priors", {})
    defaults = model.get("default_log_prob", {})
    card_log_prob = model.get("card_log_prob", {})
    scores: dict[str, float] = {}
    cards = sorted(set(as_int(value, -1) for value in visible_ids if as_int(value, -1) >= 0))
    for archetype in archetypes:
        score = math.log(max(as_float(priors.get(archetype), 0.0), 1e-15))
        default = as_float(defaults.get(archetype), -12.0)
        table = card_log_prob.get(archetype, {})
        for card_id in cards:
            score += as_float(table.get(str(card_id)), default)
        scores[archetype] = score
    probabilities = _softmax(scores)
    ranked = sorted(probabilities.items(), key=lambda item: (item[1], item[0]), reverse=True)
    top = ranked[0][0] if ranked else ""
    confidence = ranked[0][1] if ranked else 0.0
    return {
        "top": top,
        "confidence": confidence,
        "entropy": normalized_entropy(probabilities),
        "probabilities": probabilities,
        "visible_ids": cards,
    }


def route_keys(family: str, phase: str, opponent: str, *, allow_opponent: bool) -> list[str]:
    keys: list[str] = []
    if allow_opponent and opponent:
        keys.extend(
            [
                f"opponent={opponent}|family={family}|phase={phase}",
                f"opponent={opponent}|family={family}",
            ]
        )
    keys.extend([f"family={family}|phase={phase}", f"family={family}", "global"])
    return keys


def annotate_factory_fields(
    row: dict[str, Any],
    belief_model: dict[str, Any],
    *,
    phase_cuts: tuple[int, int, int] = DEFAULT_PHASE_CUTS,
) -> dict[str, Any]:
    out = dict(row)
    family = decision_family(row.get("context"))
    phase = game_phase(row.get("turn"), phase_cuts)
    forced = forced_choice(row.get("n_options"), row.get("min_count"), row.get("max_count"))
    visible = visible_opponent_card_ids(row.get("current_compact", {}), row.get("player"))
    belief = infer_opponent_belief(belief_model, visible)
    belief_top3 = [
        archetype
        for archetype, _probability in sorted(
            belief["probabilities"].items(), key=lambda item: (item[1], item[0]), reverse=True
        )[:3]
    ]
    weight = impact_weight(
        family,
        is_forced=forced,
        n_options=row.get("n_options"),
        turn=row.get("turn"),
        own_prizes=row.get("own_prize_unknown_count", 6),
        opp_prizes=row.get("opp_prize_unknown_count", 6),
    )
    out.update(
        {
            "decision_family": family,
            "game_phase": phase,
            "forced_choice": int(forced),
            "optional_choice": int(not forced),
            "impact_weight": weight,
            "critical_choice": int(not forced and weight >= 1.45),
            "opponent_visible_ids": "|".join(str(card_id) for card_id in visible),
            "opponent_belief_top": belief["top"],
            "opponent_belief_top3": "|".join(belief_top3),
            "opponent_belief_confidence": round(float(belief["confidence"]), 8),
            "opponent_belief_entropy": round(float(belief["entropy"]), 8),
            "route_family": f"family={family}",
            "route_phase": f"family={family}|phase={phase}",
            "route_opponent": f"opponent={belief['top']}|family={family}" if belief["top"] else "",
        }
    )
    return out
