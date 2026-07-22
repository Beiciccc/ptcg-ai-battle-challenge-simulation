# 007 Strong Start Lucario

Date: 2026-06-18

Local generated package (not committed): `artifacts/submissions/s007-strongstart-lucario.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/ccffdb6e8565-b4464eb525a2/main.py), [deck.csv](../agent_zoo/sources/ccffdb6e8565-b4464eb525a2/deck.csv)

Source SHA256: main.py `ccffdb6e85658dedf21dd3f9829b97bc29a1a2a30e986f79054d86796bfdab12`; deck.csv `b4464eb525a25e6598a972d00efc5e5b5156372e77f51853f4076d8ebb34fd7d`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53791680`

Public score: 757.1

Status: complete

Summary:
- Adopted the public Strong Start Crustle-aware Lucario policy.
- Kept the original Mega Lucario deck list.
- Search remained disabled for safety.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s007-strongstart-lucario`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 757.1.
