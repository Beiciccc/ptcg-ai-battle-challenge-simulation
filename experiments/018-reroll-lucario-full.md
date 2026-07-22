# 018 Reroll Lucario Full

Date: 2026-06-20

Local generated package (not committed): `artifacts/submissions/s018-reroll-lucario-full.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/9154a80b62c1-b4464eb525a2/main.py), [deck.csv](../agent_zoo/sources/9154a80b62c1-b4464eb525a2/deck.csv)

Source SHA256: main.py `9154a80b62c1eb67fcda5273bc637e97d337f8efff85734ffd7719a07a796d6f`; deck.csv `b4464eb525a25e6598a972d00efc5e5b5156372e77f51853f4076d8ebb34fd7d`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53864259`

Public score: 838.3

Status: complete

Summary:
- Restored the full Lucario policy and original Mega Lucario deck from
  experiment 009.
- Submitted it as a guard reroll because the original run remained the best
  observed result at 893.0.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s018-reroll-lucario-full`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 838.3.
