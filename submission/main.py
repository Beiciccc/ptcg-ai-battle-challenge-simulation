from __future__ import annotations

import os
from pathlib import Path

from cg.api import (
    AreaType,
    Card,
    CardType,
    Observation,
    OptionType,
    Pokemon,
    SelectContext,
    SelectType,
    all_attack,
    all_card_data,
    to_observation_class,
)

CARD_TABLE = {card.cardId: card for card in all_card_data()}
ATTACK_TABLE = {attack.attackId: attack for attack in all_attack()}
MAX_TURN_ACTIONS = 38


def read_deck_csv() -> list[int]:
    candidates = [
        Path("deck.csv"),
        Path("/kaggle_simulations/agent/deck.csv"),
    ]
    try:
        candidates.append(Path(__file__).with_name("deck.csv"))
    except NameError:
        pass

    for path in candidates:
        if path.exists():
            cards = [int(line.strip()) for line in path.read_text().splitlines() if line.strip()]
            if cards:
                return cards
    return []


def decide(obs: Observation) -> list[int]:
    select = obs.select
    if select.maxCount == 0 or not select.option:
        return []

    if select.type == SelectType.YES_NO:
        return choose_yes_no(obs)

    if all(option.type == OptionType.NUMBER for option in select.option):
        return choose_largest_number(obs)

    if select.context == SelectContext.MAIN:
        return choose_main_action(obs)

    if select.context in {
        SelectContext.DISCARD,
        SelectContext.DISCARD_CARD_OR_ATTACHED_CARD,
        SelectContext.DISCARD_ENERGY_CARD,
        SelectContext.DISCARD_ENERGY,
        SelectContext.TO_DECK,
        SelectContext.TO_DECK_BOTTOM,
    }:
        return choose_low_value_cards(obs)

    if select.context in {
        SelectContext.SETUP_ACTIVE_POKEMON,
        SelectContext.SETUP_BENCH_POKEMON,
        SelectContext.SWITCH,
        SelectContext.TO_ACTIVE,
        SelectContext.TO_BENCH,
        SelectContext.TO_FIELD,
    }:
        return choose_high_value_cards(obs)

    if select.context in {
        SelectContext.TO_HAND,
        SelectContext.LOOK,
        SelectContext.TO_PRIZE,
        SelectContext.EVOLVES_FROM,
        SelectContext.EVOLVES_TO,
        SelectContext.EVOLVE,
    }:
        return choose_high_value_cards(obs)

    return choose_high_value_cards(obs)


def choose_main_action(obs: Observation) -> list[int]:
    if obs.current.turnActionCount >= MAX_TURN_ACTIONS:
        for index, option in enumerate(obs.select.option):
            if option.type == OptionType.ATTACK:
                return [index]
        for index, option in enumerate(obs.select.option):
            if option.type == OptionType.END:
                return [index]

    scores = [score_main_option(obs, option) for option in obs.select.option]
    return [max(range(len(scores)), key=lambda index: scores[index])]


def score_main_option(obs: Observation, option) -> float:
    if option.type == OptionType.EVOLVE:
        return 9000
    if option.type == OptionType.ABILITY:
        return 7600
    if option.type == OptionType.ATTACH:
        card = get_card(obs, option.area, option.index, obs.current.yourIndex)
        target = get_card(obs, option.inPlayArea, option.inPlayIndex, obs.current.yourIndex)
        score = 7000
        if isinstance(card, Card) and card.id == 1159 and option.inPlayArea != AreaType.ACTIVE:
            return -1
        if option.inPlayArea == AreaType.ACTIVE:
            score += 500
        if isinstance(card, Card) and card.id == 1159:
            score += 2500
        if isinstance(target, Pokemon):
            score += best_printed_damage(target) - 8 * len(target.energies)
        return score
    if option.type == OptionType.PLAY:
        card = get_card(obs, AreaType.HAND, option.index, obs.current.yourIndex)
        data = CARD_TABLE.get(getattr(card, "id", None))
        if data is None:
            return 3000
        if card.id in {1147, 1212}:
            active = active_pokemon(obs, obs.current.yourIndex)
            if active is None or active.hp >= active.maxHp:
                return -1
            return 6200
        if data.cardType == CardType.SUPPORTER and obs.current.supporterPlayed:
            return -1
        if data.cardType == CardType.STADIUM and obs.current.stadiumPlayed:
            return -1
        if data.cardType == CardType.POKEMON:
            bench_count = len([pokemon for pokemon in obs.current.players[obs.current.yourIndex].bench if pokemon is not None])
            return 6500 if bench_count < obs.current.players[obs.current.yourIndex].benchMax else -1
        if data.cardType == CardType.SUPPORTER:
            return 5900
        if data.cardType == CardType.STADIUM:
            return 3200
        return 5200
    if option.type == OptionType.ATTACK:
        score = 1400
        active = active_pokemon(obs, obs.current.yourIndex)
        defender = active_pokemon(obs, 1 - obs.current.yourIndex)
        if active is not None and defender is not None:
            damage = attack_damage(active, option.attackId, defender)
            score += damage
            if damage >= defender.hp:
                score += 5000
        return score
    if option.type == OptionType.RETREAT:
        if obs.current.retreated:
            return -1
        active = active_pokemon(obs, obs.current.yourIndex)
        bench_damage = max(
            (best_printed_damage(pokemon) for pokemon in obs.current.players[obs.current.yourIndex].bench if pokemon is not None),
            default=0,
        )
        if active is not None and best_printed_damage(active) == 0 and bench_damage > 0:
            return 800
        return -1
    if option.type == OptionType.END:
        return 1
    return 100


def choose_yes_no(obs: Observation) -> list[int]:
    want_yes = obs.select.context != SelectContext.MULLIGAN
    target = OptionType.YES if want_yes else OptionType.NO
    for index, option in enumerate(obs.select.option):
        if option.type == target:
            return [index]
    return fallback(obs)


def choose_largest_number(obs: Observation) -> list[int]:
    best = max(
        range(len(obs.select.option)),
        key=lambda index: obs.select.option[index].number if obs.select.option[index].number is not None else -1,
    )
    return [best]


def choose_high_value_cards(obs: Observation) -> list[int]:
    count = requested_count(obs)
    scores = [card_score(obs, option) for option in obs.select.option]
    return sorted(range(len(scores)), key=lambda index: scores[index], reverse=True)[:count]


def choose_low_value_cards(obs: Observation) -> list[int]:
    count = min(max(obs.select.minCount, 0), obs.select.maxCount, len(obs.select.option))
    scores = [card_score(obs, option) for option in obs.select.option]
    return sorted(range(len(scores)), key=lambda index: scores[index])[:count]


def requested_count(obs: Observation) -> int:
    if obs.select.maxCount <= 0 or not obs.select.option:
        return 0
    return min(max(obs.select.minCount, 1), obs.select.maxCount, len(obs.select.option))


def fallback(obs: Observation) -> list[int]:
    count = requested_count(obs)
    return list(range(count))


def legalize(choice: list[int], obs: Observation) -> list[int]:
    unique = []
    seen = set()
    for index in choice:
        if index in seen:
            continue
        if 0 <= index < len(obs.select.option):
            unique.append(index)
            seen.add(index)
    if obs.select.minCount <= len(unique) <= obs.select.maxCount:
        return unique
    return fallback(obs)


def get_card(obs: Observation, area, index, player_index):
    try:
        if area is None or index is None:
            return None
        player = obs.current.players[player_index]
        if area == AreaType.DECK and obs.select.deck is not None:
            return obs.select.deck[index]
        if area == AreaType.HAND and player.hand is not None:
            return player.hand[index]
        if area == AreaType.DISCARD:
            return player.discard[index]
        if area == AreaType.ACTIVE:
            return player.active[index]
        if area == AreaType.BENCH:
            return player.bench[index]
        if area == AreaType.PRIZE:
            return player.prize[index]
        if area == AreaType.STADIUM:
            return obs.current.stadium[index]
        if area == AreaType.LOOKING and obs.current.looking is not None:
            return obs.current.looking[index]
    except Exception:
        return None
    return None


def card_score(obs: Observation, option) -> float:
    if option.type == OptionType.ENERGY:
        return 100
    card = get_card(obs, option.area, option.index, option.playerIndex)
    if isinstance(card, Pokemon):
        return pokemon_score(card)
    if isinstance(card, Card):
        data = CARD_TABLE.get(card.id)
        if data is None:
            return 10
        if data.cardType == CardType.POKEMON:
            return 600 + data.hp + 30 * len(data.attacks)
        if data.cardType in {CardType.BASIC_ENERGY, CardType.SPECIAL_ENERGY}:
            return 250
        if data.cardType == CardType.SUPPORTER:
            return 220
        if data.cardType == CardType.ITEM:
            if card.id == 1086:
                return 500
            return 200
        if data.cardType == CardType.TOOL:
            return 180
        if data.cardType == CardType.STADIUM:
            return 120
    return 20


def pokemon_score(pokemon: Pokemon) -> float:
    data = CARD_TABLE.get(pokemon.id)
    if data is None:
        return pokemon.hp
    prize_risk = 3 if data.megaEx else 2 if data.ex else 1
    return pokemon.hp + best_printed_damage(pokemon) + 40 * len(pokemon.energies) + 15 * len(pokemon.tools) - 35 * prize_risk


def active_pokemon(obs: Observation, player_index: int) -> Pokemon | None:
    active = obs.current.players[player_index].active
    return active[0] if active and active[0] is not None else None


def best_printed_damage(pokemon: Pokemon) -> int:
    data = CARD_TABLE.get(pokemon.id)
    if data is None:
        return 0
    return max((ATTACK_TABLE[attack_id].damage for attack_id in data.attacks if attack_id in ATTACK_TABLE), default=0)


def attack_damage(attacker: Pokemon, attack_id: int, defender: Pokemon) -> int:
    attack = ATTACK_TABLE.get(attack_id)
    if attack is None:
        return 0
    damage = attack.damage
    attacker_data = CARD_TABLE.get(attacker.id)
    defender_data = CARD_TABLE.get(defender.id)
    if damage > 0 and attacker_data is not None and defender_data is not None:
        if defender_data.weakness is not None and defender_data.weakness == attacker_data.energyType:
            damage *= 2
        elif defender_data.resistance is not None and defender_data.resistance == attacker_data.energyType:
            damage = max(0, damage - 30)
    return damage


def agent(obs_dict: dict) -> list[int]:
    obs: Observation = to_observation_class(obs_dict)
    try:
        if obs.select is None:
            return read_deck_csv()

        choice = decide(obs)
        return legalize(choice, obs)
    except Exception:
        if obs.select is None:
            return read_deck_csv()
        return fallback(obs)
