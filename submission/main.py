from __future__ import annotations

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
MAX_TURN_ACTIONS = 36


def read_deck_csv() -> list[int]:
    candidates = [Path("deck.csv"), Path("/kaggle_simulations/agent/deck.csv")]
    try:
        candidates.append(Path(__file__).with_name("deck.csv"))
    except NameError:
        pass
    for path in candidates:
        if path.exists():
            cards = [int(line.strip()) for line in path.read_text().splitlines() if line.strip()]
            if cards:
                return cards[:60]
    return []


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


def active_pokemon(obs: Observation, player_index: int) -> Pokemon | None:
    active = obs.current.players[player_index].active
    return active[0] if active and active[0] is not None else None


def best_damage(pokemon: Pokemon) -> int:
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


def pokemon_score(pokemon: Pokemon) -> int:
    data = CARD_TABLE.get(pokemon.id)
    if data is None:
        return pokemon.hp
    prize_risk = 3 if data.megaEx else 2 if data.ex else 1
    return pokemon.hp + best_damage(pokemon) + 30 * len(pokemon.energies) + 20 * len(pokemon.tools) - 25 * prize_risk


def card_score(obs: Observation, option) -> int:
    card = get_card(obs, option.area, option.index, option.playerIndex)
    if isinstance(card, Pokemon):
        score = pokemon_score(card)
        if option.playerIndex != obs.current.yourIndex:
            score += 500 if option.area == AreaType.ACTIVE else 150
        return score
    if isinstance(card, Card):
        data = CARD_TABLE.get(card.id)
        if data is None:
            return 20
        if data.cardType == CardType.POKEMON:
            return 700 + data.hp + 40 * len(data.attacks)
        if data.cardType in {CardType.BASIC_ENERGY, CardType.SPECIAL_ENERGY}:
            return 320
        if data.cardType == CardType.ITEM:
            return 260
        if data.cardType == CardType.SUPPORTER:
            return 230
        if data.cardType == CardType.TOOL:
            return 210
        if data.cardType == CardType.STADIUM:
            return 130
    if option.type == OptionType.YES:
        return 100
    if option.type == OptionType.NUMBER and option.number is not None:
        return option.number
    return 30


def main_score(obs: Observation, option) -> int:
    if option.type == OptionType.EVOLVE:
        return 9300
    if option.type == OptionType.ABILITY:
        return 8800
    if option.type == OptionType.ATTACH:
        card = get_card(obs, option.area, option.index, obs.current.yourIndex)
        target = get_card(obs, option.inPlayArea, option.inPlayIndex, obs.current.yourIndex)
        score = 7600
        if option.inPlayArea == AreaType.ACTIVE:
            score += 500
        if isinstance(card, Card) and card.id == 1159:
            score += 1600 if option.inPlayArea == AreaType.ACTIVE else -5000
        if isinstance(target, Pokemon):
            score += best_damage(target) - 10 * len(target.energies)
        return score
    if option.type == OptionType.PLAY:
        card = get_card(obs, AreaType.HAND, option.index, obs.current.yourIndex)
        data = CARD_TABLE.get(getattr(card, "id", None))
        if data is None:
            return 3000
        if data.cardType == CardType.SUPPORTER and obs.current.supporterPlayed:
            return -1
        if data.cardType == CardType.STADIUM and obs.current.stadiumPlayed:
            return -1
        if card.id in {1102, 1142}:
            return 8300
        if card.id in {1141, 1152}:
            return 7900
        if card.id in {1192, 1227}:
            return 7300
        if card.id == 1123:
            return 2500
        if card.id == 1252:
            return 4200
        if data.cardType == CardType.POKEMON:
            bench_count = len([p for p in obs.current.players[obs.current.yourIndex].bench if p is not None])
            return 7100 if bench_count < obs.current.players[obs.current.yourIndex].benchMax else -1
        if data.cardType == CardType.ITEM:
            return 6500
        if data.cardType == CardType.SUPPORTER:
            return 6100
        return 4200
    if option.type == OptionType.ATTACK:
        active = active_pokemon(obs, obs.current.yourIndex)
        defender = active_pokemon(obs, 1 - obs.current.yourIndex)
        score = 1400
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
        bench_best = max(
            (best_damage(pokemon) for pokemon in obs.current.players[obs.current.yourIndex].bench if pokemon is not None),
            default=0,
        )
        if active is not None and best_damage(active) == 0 and bench_best > 0:
            return 900
        return -1
    if option.type == OptionType.END:
        return 1
    return 100


def fallback(obs: Observation) -> list[int]:
    if obs.select.maxCount <= 0 or not obs.select.option:
        return []
    count = min(max(obs.select.minCount, 1), obs.select.maxCount, len(obs.select.option))
    return list(range(count))


def choose(obs: Observation) -> list[int]:
    select = obs.select
    if select.maxCount == 0 or not select.option:
        return []

    if select.type == SelectType.YES_NO:
        want = OptionType.NO if select.context == SelectContext.MULLIGAN else OptionType.YES
        for index, option in enumerate(select.option):
            if option.type == want:
                return [index]
        return fallback(obs)

    if all(option.type == OptionType.NUMBER for option in select.option):
        return [max(range(len(select.option)), key=lambda i: select.option[i].number or 0)]

    if select.context == SelectContext.MAIN:
        if obs.current.turnActionCount >= MAX_TURN_ACTIONS:
            for index, option in enumerate(select.option):
                if option.type == OptionType.ATTACK:
                    return [index]
            for index, option in enumerate(select.option):
                if option.type == OptionType.END:
                    return [index]
        scores = [main_score(obs, option) for option in select.option]
        return [max(range(len(scores)), key=lambda i: scores[i])]

    low_contexts = {
        SelectContext.DISCARD,
        SelectContext.DISCARD_CARD_OR_ATTACHED_CARD,
        SelectContext.DISCARD_ENERGY,
        SelectContext.DISCARD_ENERGY_CARD,
        SelectContext.TO_DECK,
        SelectContext.TO_DECK_BOTTOM,
    }
    count = min(max(select.minCount, 1), select.maxCount, len(select.option))
    scores = [card_score(obs, option) for option in select.option]
    reverse = select.context not in low_contexts
    return sorted(range(len(scores)), key=lambda i: scores[i], reverse=reverse)[:count]


def agent(obs_dict: dict) -> list[int]:
    obs: Observation = to_observation_class(obs_dict)
    if obs.select is None:
        return read_deck_csv()
    try:
        result = choose(obs)
        result = [i for i in dict.fromkeys(result) if 0 <= i < len(obs.select.option)]
        if obs.select.minCount <= len(result) <= obs.select.maxCount:
            return result
        return fallback(obs)
    except Exception:
        return fallback(obs)
