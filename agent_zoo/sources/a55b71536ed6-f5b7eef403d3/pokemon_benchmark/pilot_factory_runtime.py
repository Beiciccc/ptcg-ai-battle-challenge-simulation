from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

from pokemon_benchmark.generic_rule_proxy_agent import GenericRuleProxy, _fallback
from pokemon_benchmark.pilot_factory_core import (
    FACTORY_SCHEMA_VERSION,
    annotate_factory_fields,
    route_keys,
)
from pokemon_benchmark.pilot_state_features import FEATURE_SCHEMA_VERSION, linear_score, live_option_row, row_feature_map

try:
    from cg.api import to_observation_class
except Exception:  # pragma: no cover - supplied by CABT SDK at runtime.
    to_observation_class = None


def _sigmoid(value: float) -> float:
    if value >= 0:
        z = math.exp(-min(value, 40.0))
        return 1.0 / (1.0 + z)
    z = math.exp(max(value, -40.0))
    return z / (1.0 + z)


def _asset_path(name: str) -> Path:
    candidates = [
        Path(name),
        Path("/kaggle_simulations/agent") / name,
        Path(__file__).resolve().parents[1] / name,
    ]
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(name)


def _read_deck() -> list[int]:
    cards = [
        int(line.strip())
        for line in _asset_path("deck.csv").read_text(encoding="utf-8-sig").splitlines()
        if line.strip()
    ]
    if len(cards) != 60:
        raise ValueError(f"deck.csv contains {len(cards)} cards, expected 60")
    return cards


class PilotFactoryAgent:
    def __init__(self, model_path: str | Path | None = None) -> None:
        path = Path(model_path) if model_path else _asset_path("pilot_factory_model.json")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("factory_schema_version") != FACTORY_SCHEMA_VERSION:
            raise ValueError(
                f"Factory schema mismatch: model={payload.get('factory_schema_version')} runtime={FACTORY_SCHEMA_VERSION}"
            )
        if payload.get("feature_schema_version") != FEATURE_SCHEMA_VERSION:
            raise ValueError(
                f"Feature schema mismatch: model={payload.get('feature_schema_version')} runtime={FEATURE_SCHEMA_VERSION}"
            )
        self.payload = payload
        self.experts = payload.get("experts", {})
        if "global" not in self.experts:
            raise ValueError("Pilot Factory model has no global expert")
        self.belief_model = payload.get("belief_model", {})
        self.phase_cuts = tuple(int(value) for value in payload.get("phase_cuts", [2, 6, 12]))
        runtime = payload.get("runtime", {})
        self.belief_min_confidence = float(runtime.get("belief_min_confidence", 0.55))
        self.expert_weight = max(0.0, float(runtime.get("expert_weight", 0.70)))
        self.global_weight = max(0.0, float(runtime.get("global_weight", 0.20)))
        self.rule_weight = max(0.0, float(runtime.get("rule_weight", 0.10)))
        self.selection_threshold_offset = float(runtime.get("selection_threshold_offset", 0.0))
        self.min_margin = max(0.0, float(runtime.get("min_margin", 0.08)))
        self.max_optional = max(1, int(runtime.get("max_optional", 8)))
        total = self.expert_weight + self.global_weight + self.rule_weight
        if total <= 0:
            self.expert_weight, self.global_weight, self.rule_weight = 0.0, 0.0, 1.0
        else:
            self.expert_weight /= total
            self.global_weight /= total
            self.rule_weight /= total
        self.deck = _read_deck()
        self.last_route = ""
        self.last_belief = ""
        self.last_belief_confidence = 0.0

    def _route(self, row: dict[str, Any]) -> str:
        allow_opponent = float(row.get("opponent_belief_confidence", 0.0) or 0.0) >= self.belief_min_confidence
        for key in route_keys(
            str(row.get("decision_family", "other")),
            str(row.get("game_phase", "opening")),
            str(row.get("opponent_belief_top", "")),
            allow_opponent=allow_opponent,
        ):
            if key in self.experts:
                return key
        return "global"

    @staticmethod
    def _expert_score(expert: dict[str, Any], row: dict[str, Any]) -> float:
        raw = linear_score([float(value) for value in expert.get("weights", [])], row_feature_map(row))
        return _sigmoid(raw)

    def choose(self, obs_dict: dict[str, Any]) -> list[int]:
        if obs_dict.get("select") is None:
            return list(self.deck)
        if to_observation_class is None:
            return _fallback(obs_dict)
        try:
            select = obs_dict.get("select") or {}
            raw_options = list(select.get("option") or [])
            n = len(raw_options)
            min_count = max(0, min(int(select.get("minCount") or 0), n))
            max_count = max(min_count, min(int(select.get("maxCount") or min_count), n))
            if n == 0 or max_count == 0:
                return []

            obs = to_observation_class(obs_dict)
            typed_options = list(getattr(obs.select, "option", []) or []) if obs.select is not None else []
            generic = GenericRuleProxy(obs)
            rule_scores = [generic.score_option(option) for option in typed_options]
            max_abs_rule = max([abs(value) for value in rule_scores] or [1.0]) or 1.0

            annotated_rows: list[dict[str, Any]] = []
            for index, option in enumerate(raw_options):
                row = live_option_row(obs_dict, option, index)
                row["current_compact"] = obs_dict.get("current") or {}
                row["player"] = (obs_dict.get("current") or {}).get("yourIndex", 0)
                row = annotate_factory_fields(row, self.belief_model, phase_cuts=self.phase_cuts)
                annotated_rows.append(row)
            route = self._route(annotated_rows[0])
            expert = self.experts[route]
            global_expert = self.experts["global"]
            expert_weight = 0.0 if route == "global" else self.expert_weight
            global_weight = self.global_weight + (self.expert_weight if route == "global" else 0.0)
            normalization = expert_weight + global_weight + self.rule_weight
            normalization = normalization or 1.0

            scored: list[tuple[float, float, float, float, int]] = []
            for index, row in enumerate(annotated_rows):
                expert_score = self._expert_score(expert, row)
                global_score = self._expert_score(global_expert, row)
                rule = rule_scores[index] / max_abs_rule if index < len(rule_scores) else 0.0
                rule_probability = (rule + 1.0) / 2.0
                blended = (
                    expert_weight * expert_score
                    + global_weight * global_score
                    + self.rule_weight * rule_probability
                ) / normalization
                scored.append((blended, expert_score, global_score, rule, index))
            scored.sort(key=lambda item: (item[0], item[1], item[2], -item[4]), reverse=True)

            threshold = max(
                0.0,
                min(1.0, float(expert.get("selection_threshold", 0.5)) + self.selection_threshold_offset),
            )
            best = scored[0][0]
            chosen: list[int] = []
            for blended, expert_score, global_score, _rule, index in scored:
                if len(chosen) < min_count:
                    chosen.append(index)
                    continue
                if len(chosen) >= min(max_count, self.max_optional):
                    break
                learned = expert_score if route != "global" else global_score
                if learned >= threshold and blended >= best - self.min_margin:
                    chosen.append(index)
            if not chosen and scored:
                chosen.append(scored[0][4])
            self.last_route = route
            self.last_belief = str(annotated_rows[0].get("opponent_belief_top", ""))
            self.last_belief_confidence = float(annotated_rows[0].get("opponent_belief_confidence", 0.0) or 0.0)
            return chosen[:max_count]
        except Exception:
            return _fallback(obs_dict)


def make_agent(model_path: str | Path | None = None):
    factory = PilotFactoryAgent(model_path)

    def agent(obs_dict: dict[str, Any], config: Any = None) -> list[int]:
        return factory.choose(obs_dict)

    return agent
