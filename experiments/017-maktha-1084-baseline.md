# 017 Maktha 1084 Baseline

Date: 2026-06-20

Local generated package (not committed): `artifacts/submissions/s017-maktha-1084-baseline.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/459cf970d9ff-2a541d7bf3d9/main.py), [deck.csv](../agent_zoo/sources/459cf970d9ff-2a541d7bf3d9/deck.csv)

Source SHA256: main.py `459cf970d9ffc28fcb13473cff216750f17d53a35fa990fcab1805e00e78a848`; deck.csv `2a541d7bf3d9e6b36037123f53f4dfef6348223f79fd27095dafc602a5357c19`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53864132`

Public score: 673.0

Status: complete

Summary:
- Tested the public 1084.5 baseline candidate from the latest Code list.
- Used its Mega Lucario policy and deck extraction from the public notebook.
- Selected it as the first 2026-06-20 exploratory run before restoring
  high-scoring latest-two guard submissions.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s017-maktha-1084-baseline`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 673.0.
