"""Kaggle 入口：使用三天全量数据训练的 v9 Attention BC Agent。"""

from __future__ import annotations

from pathlib import Path

import torch

from bc_agent import load_policy, predict_action

torch.set_num_threads(1)
try:
    _MODEL_PATH = Path(__file__).with_name("model.pt")
except NameError:
    _MODEL_PATH = Path("/kaggle_simulations/agent/model.pt")
if not _MODEL_PATH.is_file():
    raise FileNotFoundError(
        f"BC checkpoint missing at {_MODEL_PATH}; build the submission after training."
    )
_MODEL = load_policy(_MODEL_PATH, "cpu")


def agent(obs_dict: dict) -> list[int]:
    return predict_action(obs_dict, _MODEL)
