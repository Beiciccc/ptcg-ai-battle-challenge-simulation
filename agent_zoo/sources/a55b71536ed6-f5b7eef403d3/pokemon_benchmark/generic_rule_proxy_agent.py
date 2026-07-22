from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

from cg.api import (
    AreaType,
    Card,
    CardType,
    OptionType,
    Pokemon,
    SelectContext,
    all_card_data,
    to_observation_class,
)


_CARD_TABLE = {card.cardId: card for card in all_card_data()}


def _read_deck() -> list[int]:
    candidates = [Path("deck.csv"), Path("/kaggle_simulations/agent/deck.csv")]
    for path in candidates:
        if not path.exists():
            continue
        cards = [
            int(line.strip())
            for line in path.read_text(encoding="utf-8-sig").splitlines()
            if line.strip()
        ]
        if len(cards) == 60:
            return cards
    return []


def _safe_get(seq: Any, index: int) -> Any | None:
    try:
        if seq is None or index is None or index < 0 or index >= len(seq):
            return None
        return seq[index]
    except Exception:
        return None


def _card_data(card_or_id: Any) -> Any | None:
    cid = getattr(card_or_id, "id", card_or_id)
    return _CARD_TABLE.get(cid)


def _is_pokemon_card(card: Any) -> bool:
    if isinstance(card, Pokemon):
        return True
    data = _card_data(card)
    return bool(data is not None and data.cardType == CardType.POKEMON)


def _max_hp(card: Any) -> int:
    data = _card_data(card)
    return int(getattr(data, "hp", getattr(card, "hp", 0)) or 0)


def _damage_on(pokemon: Pokemon) -> int:
    return max(0, _max_hp(pokemon) - int(getattr(pokemon, "hp", 0) or 0))


def _prize_value(pokemon: Pokemon) -> int:
    data = _card_data(pokemon)
    if data is None:
        return 1
    if getattr(data, "megaEx", False):
        return 3
    if getattr(data, "ex", False):
        return 2
    return 1


def _structural_value(card: Any) -> float:
    data = _card_data(card)
    if data is None:
        return 0.0
    if data.cardType == CardType.POKEMON:
        score = float(getattr(data, "hp", 0) or 0)
        score += 80 if getattr(data, "basic", False) else 0
        score += 130 if getattr(data, "stage1", False) else 0
        score += 190 if getattr(data, "stage2", False) else 0
        score += 240 if getattr(data, "ex", False) else 0
        score += 320 if getattr(data, "megaEx", False) else 0
        score += 25 * len(getattr(data, "attacks", []) or [])
        score += 20 * len(getattr(data, "skills", []) or [])
        return score
    name = str(getattr(data, "name", "")).lower()
    score = 50.0
    if data.cardType == CardType.SUPPORTER:
        score += 220
    elif data.cardType == CardType.ITEM:
        score += 180
    elif data.cardType == CardType.TOOL:
        score += 120
    elif data.cardType == CardType.STADIUM:
        score += 100
    elif data.cardType in {CardType.BASIC_ENERGY, CardType.SPECIAL_ENERGY}:
        score += 80
    if any(word in name for word in ["ball", "gear", "perrin", "cheren"]):
        score += 120
    if any(word in name for word in ["switch", "patch", "trumpet", "energy switch"]):
        score += 110
    if any(word in name for word in ["devotion", "training", "mischief", "move", "bargain"]):
        score += 70
    return score


class GenericRuleProxy:
    def __init__(self, obs: Any):
        self.obs = obs
        self.state = obs.current
        self.select = obs.select
        self.context = self.select.context
        self.my_index = self.state.yourIndex
        self.op_index = 1 - self.my_index
        self.me = self.state.players[self.my_index]
        self.opponent = self.state.players[self.op_index]
        self.field_counts = Counter(p.id for p in self.me.active + self.me.bench if p is not None)
        self.hand_counts = Counter(c.id for c in self.me.hand)

    def get_card(self, area: AreaType, index: int, player_index: int | None = None) -> Any | None:
        player_index = self.my_index if player_index is None else player_index
        player = self.state.players[player_index]
        if area == AreaType.HAND:
            return _safe_get(player.hand, index)
        if area == AreaType.DISCARD:
            return _safe_get(player.discard, index)
        if area == AreaType.ACTIVE:
            return _safe_get(player.active, index)
        if area == AreaType.BENCH:
            return _safe_get(player.bench, index)
        if area == AreaType.PRIZE:
            return _safe_get(player.prize, index)
        if area == AreaType.DECK:
            return _safe_get(getattr(self.select, "deck", None), index)
        if area == AreaType.STADIUM:
            return _safe_get(getattr(self.state, "stadium", None), index)
        if area == AreaType.LOOKING:
            return _safe_get(getattr(self.state, "looking", None), index)
        return None

    def board(self, player_index: int) -> list[Any]:
        player = self.state.players[player_index]
        return [p for p in player.active + player.bench if p is not None]

    def score_pokemon_target(self, pokemon: Pokemon, opponent: bool) -> float:
        score = 1000 * _prize_value(pokemon)
        score += _damage_on(pokemon) * 8
        score += len(getattr(pokemon, "energies", []) or []) * 130
        score += len(getattr(pokemon, "tools", []) or []) * 70
        score += _max_hp(pokemon) * 0.4
        data = _card_data(pokemon)
        if data is not None:
            score += 180 if getattr(data, "stage2", False) else 0
            score += 120 if getattr(data, "stage1", False) else 0
            score += 240 if getattr(data, "ex", False) else 0
            score += 340 if getattr(data, "megaEx", False) else 0
        return score if opponent else score * 0.25

    def score_setup(self, card: Any, active: bool) -> float:
        if not _is_pokemon_card(card):
            return 0.0
        data = _card_data(card)
        cid = getattr(card, "id", 0)
        duplicate_penalty = 80 * self.field_counts[cid]
        basic_bonus = 180 if data is not None and getattr(data, "basic", False) else 0
        active_bonus = 80 if active else 0
        return 500 + _structural_value(card) + basic_bonus + active_bonus - duplicate_penalty

    def score_card_choice(self, option: Any) -> float:
        card = self.get_card(option.area, option.index, getattr(option, "playerIndex", self.my_index))
        if card is None:
            return 0.0
        if self.context == SelectContext.SETUP_ACTIVE_POKEMON:
            return self.score_setup(card, active=True)
        if self.context == SelectContext.SETUP_BENCH_POKEMON:
            return self.score_setup(card, active=False)
        if self.context in {SelectContext.SWITCH, SelectContext.TO_ACTIVE} and isinstance(card, Pokemon):
            return 900 + len(getattr(card, "energies", []) or []) * 90 + _max_hp(card) * 0.2
        if self.context == SelectContext.TO_BENCH:
            return self.score_setup(card, active=False)
        if self.context == SelectContext.TO_HAND:
            return 300 + _structural_value(card) - 70 * self.hand_counts[getattr(card, "id", 0)]
        if self.context == SelectContext.ATTACH_FROM and isinstance(card, Pokemon):
            return self.score_energy_target(card, option.area == AreaType.ACTIVE)
        if self.context == SelectContext.DISCARD:
            return self.score_discard(card)
        if self.context in {SelectContext.DAMAGE_COUNTER, SelectContext.DAMAGE_COUNTER_ANY, SelectContext.DAMAGE}:
            if isinstance(card, Pokemon):
                return self.score_pokemon_target(card, getattr(option, "playerIndex", self.my_index) == self.op_index)
        if self.context in {SelectContext.HEAL, SelectContext.REMOVE_DAMAGE_COUNTER} and isinstance(card, Pokemon):
            return _damage_on(card) * 20 + len(getattr(card, "energies", []) or []) * 35
        if self.context in {SelectContext.EVOLVES_FROM, SelectContext.EVOLVES_TO} and isinstance(card, Pokemon):
            return 600 + len(getattr(card, "energies", []) or []) * 70 + _structural_value(card)
        return _structural_value(card)

    def score_discard(self, card: Any) -> float:
        data = _card_data(card)
        cid = getattr(card, "id", 0)
        if data is not None and data.cardType in {CardType.BASIC_ENERGY, CardType.SPECIAL_ENERGY}:
            return 65 if self.hand_counts[cid] >= 2 else -40
        if _is_pokemon_card(card):
            return 40 if self.field_counts[cid] >= 1 or self.hand_counts[cid] >= 2 else -90
        return 80 if self.hand_counts[cid] >= 2 else 10

    def score_play(self, option: Any) -> float:
        card = self.get_card(AreaType.HAND, option.index, self.my_index)
        if card is None:
            return 0.0
        data = _card_data(card)
        if data is None:
            return 0.0
        if data.cardType == CardType.POKEMON:
            return self.score_setup(card, active=False)
        if data.cardType == CardType.SUPPORTER and getattr(self.state, "supporterPlayed", False):
            return -1.0
        if data.cardType == CardType.STADIUM and getattr(self.state, "stadium", []):
            current = _safe_get(getattr(self.state, "stadium", []), 0)
            if current is not None and getattr(current, "id", None) == getattr(card, "id", None):
                return -1.0
        return 2500 + _structural_value(card)

    def score_attach(self, option: Any) -> float:
        card = self.get_card(AreaType.HAND, option.index, self.my_index)
        target = self.get_card(option.inPlayArea, option.inPlayIndex, self.my_index)
        if card is None or not isinstance(target, Pokemon):
            return 0.0
        data = _card_data(card)
        if data is not None and data.cardType == CardType.TOOL:
            return 3300 + self.score_pokemon_target(target, opponent=False)
        return self.score_energy_target(target, option.inPlayArea == AreaType.ACTIVE)

    def score_energy_target(self, pokemon: Pokemon, active: bool) -> float:
        data = _card_data(pokemon)
        energy_count = len(getattr(pokemon, "energies", []) or [])
        score = 4200 + (350 if active else 0) - energy_count * 90
        if data is not None:
            score += 140 if getattr(data, "ex", False) else 0
            score += 220 if getattr(data, "megaEx", False) else 0
            score += 45 * len(getattr(data, "attacks", []) or [])
        return score

    def score_evolve(self, option: Any) -> float:
        target = self.get_card(option.inPlayArea, option.inPlayIndex, self.my_index)
        evolve_card = self.get_card(AreaType.HAND, option.index, self.my_index)
        if not isinstance(target, Pokemon):
            return 0.0
        return 5200 + len(getattr(target, "energies", []) or []) * 120 + _structural_value(evolve_card)

    def score_ability(self, option: Any) -> float:
        card = self.get_card(option.area, option.index, self.my_index)
        if card is None:
            return 0.0
        return 6500 + _structural_value(card)

    def score_attack(self, option: Any) -> float:
        active = _safe_get(self.me.active, 0)
        if not isinstance(active, Pokemon):
            return 0.0
        targets = self.board(self.op_index)
        target_score = max([self.score_pokemon_target(p, opponent=True) for p in targets] or [0.0])
        energy_count = len(getattr(active, "energies", []) or [])
        attack_bonus = 75 * int(getattr(option, "attackId", 0) or 0)
        return 2200 + target_score * 0.15 + energy_count * 120 + (attack_bonus % 500)

    def score_option(self, option: Any) -> float:
        opt_type = option.type
        if opt_type == OptionType.NUMBER:
            return float(getattr(option, "number", 0) or 0)
        if opt_type == OptionType.YES:
            return 100.0 if self.context == SelectContext.IS_FIRST else 20.0
        if opt_type == OptionType.NO:
            return 0.0
        if opt_type == OptionType.END:
            return -100.0
        if opt_type == OptionType.CARD:
            return self.score_card_choice(option)
        if opt_type == OptionType.PLAY:
            return self.score_play(option)
        if opt_type == OptionType.ATTACH:
            return self.score_attach(option)
        if opt_type == OptionType.EVOLVE:
            return self.score_evolve(option)
        if opt_type == OptionType.ABILITY:
            return self.score_ability(option)
        if opt_type == OptionType.RETREAT:
            return 600.0
        if opt_type == OptionType.ATTACK:
            return self.score_attack(option)
        return 0.0

    def choose(self) -> list[int]:
        options = list(getattr(self.select, "option", []) or [])
        n = len(options)
        min_count = max(0, min(int(getattr(self.select, "minCount", 0) or 0), n))
        max_count = max(min_count, min(int(getattr(self.select, "maxCount", min_count) or min_count), n))
        if n == 0 or max_count == 0:
            return []
        scores = [self.score_option(option) for option in options]
        ranked = sorted(range(n), key=lambda i: scores[i], reverse=True)
        chosen: list[int] = []
        seen: set[int] = set()
        for idx in ranked:
            if idx in seen:
                continue
            if scores[idx] > 0 or len(chosen) < min_count:
                chosen.append(idx)
                seen.add(idx)
            if len(chosen) >= max_count:
                break
        for idx in range(n):
            if len(chosen) >= min_count:
                break
            if idx not in seen:
                chosen.append(idx)
                seen.add(idx)
        return chosen


def _fallback(obs_dict: dict[str, Any]) -> list[int]:
    try:
        if obs_dict.get("select") is None:
            return _read_deck()
        select = obs_dict.get("select") or {}
        options = select.get("option") or []
        min_count = int(select.get("minCount") or 0)
        return list(range(max(0, min(min_count, len(options)))))
    except Exception:
        return []


def agent(obs_dict: dict[str, Any], config: Any = None) -> list[int]:
    try:
        if obs_dict.get("select") is None:
            return _read_deck()
        obs = to_observation_class(obs_dict)
        return GenericRuleProxy(obs).choose()
    except Exception:
        return _fallback(obs_dict)
