# 000 Baseline

Date: 2026-06-17

Local generated package (not committed): `artifacts/submissions/baseline.zip`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/4a8dcb45a05a-e92d5717fd04/main.py), [deck.csv](../agent_zoo/sources/4a8dcb45a05a-e92d5717fd04/deck.csv)

Source SHA256: main.py `4a8dcb45a05a99244321844cc6d9330126f80ac74c7a3e05933fc7df6591eb08`; deck.csv `e92d5717fd04865b0b528307df7a9d9aecc2c7b917bfbd5042fe58e3d1f26997`

Reproducibility: exact source snapshot; Kaggle runtime required

Status: prepared, not submitted

Summary:
- Uses the sample 60-card deck.
- Uses a deterministic fallback selection policy.
- Includes deck validation and packaging checks.

Validation:
- `python tools/check_deck.py submission/deck.csv`
- `python tools/package_submission.py --name baseline`
- `pytest -q`
