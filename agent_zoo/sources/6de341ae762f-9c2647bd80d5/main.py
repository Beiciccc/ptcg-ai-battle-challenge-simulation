import os
from pathlib import Path

from cg.api import AreaType, Card, Observation, OptionType, Pokemon, SelectContext, to_observation_class


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
                return cards[:60]
    return []


def get_card(obs: Observation, area: AreaType, index: int, player_index: int) -> Pokemon | Card | None:
    try:
        player = obs.current.players[player_index]
        if area == AreaType.DECK:
            return obs.select.deck[index]
        if area == AreaType.HAND:
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
        if area == AreaType.LOOKING:
            return obs.current.looking[index]
    except Exception:
        return None
    return None


def active_pokemon(obs: Observation) -> Pokemon | None:
    active = obs.current.players[obs.current.yourIndex].active
    return active[0] if active and active[0] is not None else None


def score_option(obs: Observation, option) -> int:
    context = obs.select.context
    if context == SelectContext.MAIN:
        if option.type == OptionType.ATTACH:
            score = 1000
            card = get_card(obs, option.area, option.index, obs.current.yourIndex)
            if card is not None and card.id == 1159:
                return 2100 if option.inPlayArea == AreaType.ACTIVE else 0
            return score
        if option.type == OptionType.EVOLVE:
            return 800
        if option.type == OptionType.PLAY:
            score = 600
            card = get_card(obs, AreaType.HAND, option.index, obs.current.yourIndex)
            active = active_pokemon(obs)
            if card is None:
                return score
            if card.id == 1147:
                if active is not None and active.hp < active.maxHp and len(active.energies) >= 3:
                    return 2000
                return 0
            if card.id == 1212:
                if active is not None and active.hp < active.maxHp:
                    return 1500
                return 0
            if card.id == 1224:
                return 1400
            if card.id == 1264:
                return 1300
            return score
        if option.type == OptionType.ABILITY:
            return 400
        if option.type == OptionType.ATTACK:
            return 100
        if option.type == OptionType.RETREAT:
            return -1
        if option.type == OptionType.END:
            return 0
        return 0

    score = 2000
    if option.type == OptionType.CARD:
        card = get_card(obs, option.area, option.index, option.playerIndex)
        if card is not None:
            if context in {SelectContext.EVOLVE, SelectContext.TO_BENCH, SelectContext.TO_FIELD}:
                score += 500
            if isinstance(card, Pokemon):
                if option.playerIndex != obs.current.yourIndex:
                    score += 500 if option.area == AreaType.ACTIVE else 100
                    score += len(card.energies) * 50
                else:
                    score += card.hp
    elif option.type == OptionType.YES:
        score += 100
    elif option.type == OptionType.NUMBER and option.number is not None:
        score += option.number
    return score


def agent(obs_dict: dict) -> list[int]:
    obs: Observation = to_observation_class(obs_dict)
    if obs.select is None:
        return read_deck_csv()

    select = obs.select
    scores = [score_option(obs, option) for option in select.option]
    sorted_options = sorted(range(len(scores)), key=lambda index: scores[index], reverse=True)

    output = []
    for index in sorted_options[: select.maxCount]:
        if scores[index] >= 0 or len(output) < select.minCount:
            output.append(index)

    if len(output) < select.minCount:
        return list(range(min(select.minCount, len(select.option))))
    return output
