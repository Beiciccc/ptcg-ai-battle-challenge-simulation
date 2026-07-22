# 013 Lucario Search 915

Date: 2026-06-19

Local generated package (not committed): `artifacts/submissions/s013-lucario-search-915.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/8026b86be33f-b4464eb525a2/main.py), [deck.csv](../agent_zoo/sources/8026b86be33f-b4464eb525a2/deck.csv)

Source SHA256: main.py `8026b86be33fdec0fcb60051c6adecf91a3ecd9cbbff539fb0a0c617d1601ad3`; deck.csv `b4464eb525a25e6598a972d00efc5e5b5156372e77f51853f4076d8ebb34fd7d`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53827594`

Public score: 858.4

Status: complete

Summary:
- Tested the public Lucario search baseline with bounded forward search enabled.
- Used the original Mega Lucario deck list from that notebook.
- Selected it because the public Code title reported a 915+ result and it
  offered a different high-scoring implementation from the retuned V7 policy.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s013-lucario-search-915`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 858.4.
