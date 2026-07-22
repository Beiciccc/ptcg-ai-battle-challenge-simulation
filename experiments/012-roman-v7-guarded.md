# 012 Roman V7 Guarded

Date: 2026-06-19

Local generated package (not committed): `artifacts/submissions/s012-roman-v7-guarded.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/99d17e097d2e-fd2fc062ffc2/main.py), [deck.csv](../agent_zoo/sources/99d17e097d2e-fd2fc062ffc2/deck.csv)

Source SHA256: main.py `99d17e097d2e3ffddefe958679e9ee0441e41c239084883863ad0dbaef8670a6`; deck.csv `fd2fc062ffc23c5a4f77f30c05d2fc1d08a7bade73e1dc67e1dd547192fd46b3`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53827461`

Public score: 748.4

Status: complete

Summary:
- Kept the retuned Mega Lucario deck from experiment 011.
- Updated the policy with the public V7 guard changes: low-deck draw
  suppression, setup bench scoring, discard scoring, and damage-counter target
  handling.
- Submitted this as the first 2026-06-19 candidate because the public Code
  list showed a V7 title with a 960+ leaderboard claim.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s012-roman-v7-guarded`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 748.4.
