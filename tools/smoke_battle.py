#!/usr/bin/env python
from __future__ import annotations

import argparse
import importlib.util
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "submission"))

from cg.game import battle_finish, battle_select, battle_start


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--games", type=int, default=1)
    parser.add_argument("--max-steps", type=int, default=800)
    parser.add_argument("--seed", type=int, default=20260617)
    parser.add_argument("--agent", default=str(ROOT / "submission" / "main.py"))
    parser.add_argument("--deck", default=str(ROOT / "submission" / "deck.csv"))
    args = parser.parse_args()

    random.seed(args.seed)
    agent = load_agent(Path(args.agent))
    deck = read_deck(Path(args.deck))

    completed = 0
    for game_index in range(args.games):
        obs, start_data = battle_start(deck, deck)
        if obs is None:
            raise RuntimeError(f"battle_start failed: {start_data.error}")
        try:
            for step in range(args.max_steps):
                selection = agent.agent(obs)
                obs = battle_select(selection)
                current = obs.get("current")
                if current and current.get("result", -1) != -1:
                    completed += 1
                    print(f"game {game_index + 1}: result={current['result']} steps={step + 1}")
                    break
            else:
                print(f"game {game_index + 1}: no result within {args.max_steps} steps")
        finally:
            battle_finish()

    print(f"completed: {completed}/{args.games}")
    return 0 if completed == args.games else 1


def load_agent(path: Path):
    spec = importlib.util.spec_from_file_location("submission_main", path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_deck(path: Path) -> list[int]:
    return [int(line.strip()) for line in path.read_text().splitlines() if line.strip()]


if __name__ == "__main__":
    raise SystemExit(main())
