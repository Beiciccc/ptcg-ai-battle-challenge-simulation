# 014 Yaroslav Lucario V2

Date: 2026-06-19

Local generated package (not committed): `artifacts/submissions/s014-yaroslav-lucario-v2.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/fddcbcde82cd-b4464eb525a2/main.py), [deck.csv](../agent_zoo/sources/fddcbcde82cd-b4464eb525a2/deck.csv)

Source SHA256: main.py `fddcbcde82cd7b5b4f6a1c1644ec544fc0d7916184f12280c60b34e06076b540`; deck.csv `b4464eb525a25e6598a972d00efc5e5b5156372e77f51853f4076d8ebb34fd7d`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53827710`

Public score: 681.2

Status: complete

Summary:
- Tested a public Lucario V2 crustle-aware policy using the original Mega
  Lucario deck list.
- Selected it as the last exploratory run before restoring high-scoring guard
  submissions, because public round-robin notes suggested it was competitive
  against the visible sample of public submissions.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s014-yaroslav-lucario-v2`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 681.2.
