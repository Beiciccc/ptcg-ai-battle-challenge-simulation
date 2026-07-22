# 006 Lucario Full Policy

Date: 2026-06-17

Local generated package (not committed): `artifacts/submissions/s006-lucario-full-policy.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/d6f0aeb6de59-b4464eb525a2/main.py), [deck.csv](../agent_zoo/sources/d6f0aeb6de59-b4464eb525a2/deck.csv)

Source SHA256: main.py `d6f0aeb6de59840182b93f661b658f78e76fb31e7239a51368d21ab30c58c3c0`; deck.csv `b4464eb525a25e6598a972d00efc5e5b5156372e77f51853f4076d8ebb34fd7d`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53784094`

Public score: 870.3

Status: complete

Summary:
- Kept the Mega Lucario deck.
- Replaced the concise tempo policy with a fuller deck-specific public-rule
  implementation.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s006-lucario-full-policy`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 870.3, the best result in the first batch.
