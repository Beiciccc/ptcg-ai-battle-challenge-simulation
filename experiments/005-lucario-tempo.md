# 005 Lucario Tempo

Date: 2026-06-17

Local generated package (not committed): `artifacts/submissions/s005-lucario-tempo.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/e5c24a4eb8b7-b4464eb525a2/main.py), [deck.csv](../agent_zoo/sources/e5c24a4eb8b7-b4464eb525a2/deck.csv)

Source SHA256: main.py `e5c24a4eb8b7e7ff0d9f9acd5aa59ea46e43bd2be14290e7bb4b8a9094ac4d72`; deck.csv `b4464eb525a25e6598a972d00efc5e5b5156372e77f51853f4076d8ebb34fd7d`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53784007`

Public score: 410.9

Status: complete

Summary:
- Switched to a Mega Lucario deck.
- Used a concise tempo policy with higher priority for evolution, abilities,
  key setup items, and energy attachment before attacking.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s005-lucario-tempo`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 410.9, below the Crustle variants.
