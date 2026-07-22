from pathlib import Path

from cg.api import Observation, OptionType, SelectType, to_observation_class


def read_deck_csv() -> list[int]:
    candidates = [
        Path("deck.csv"),
        Path(__file__).with_name("deck.csv"),
        Path("/kaggle_simulations/agent/deck.csv"),
    ]
    for path in candidates:
        if path.exists():
            return [int(line.strip()) for line in path.read_text().splitlines() if line.strip()]
    raise FileNotFoundError("deck.csv was not found in the submission directory.")


def agent(obs_dict: dict) -> list[int]:
    obs: Observation = to_observation_class(obs_dict)
    if obs.select is None:
        return read_deck_csv()

    if obs.select.maxCount == 0 or not obs.select.option:
        return []

    if obs.select.type == SelectType.MAIN:
        selected = _select_main_action(obs)
        if selected:
            return selected

    if obs.select.type == SelectType.YES_NO:
        selected = _first_option_of_type(obs, OptionType.YES)
        if selected:
            return selected

    return _fallback_selection(obs)


def _select_main_action(obs: Observation) -> list[int]:
    priorities = [
        OptionType.ATTACK,
        OptionType.ABILITY,
        OptionType.EVOLVE,
        OptionType.ATTACH,
        OptionType.PLAY,
        OptionType.RETREAT,
        OptionType.END,
    ]
    for option_type in priorities:
        selected = _first_option_of_type(obs, option_type)
        if selected:
            return selected
    return []


def _first_option_of_type(obs: Observation, option_type: OptionType) -> list[int]:
    for index, option in enumerate(obs.select.option):
        if option.type == option_type:
            return [index]
    return []


def _fallback_selection(obs: Observation) -> list[int]:
    select = obs.select
    count = select.minCount
    if count == 0 and select.type == SelectType.MAIN:
        count = 1
    count = min(count, select.maxCount, len(select.option))
    return list(range(count))
