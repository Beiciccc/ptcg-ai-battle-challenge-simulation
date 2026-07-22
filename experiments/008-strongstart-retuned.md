# 008 Strong Start Retuned

Date: 2026-06-18

Local generated package (not committed): `artifacts/submissions/s008-strongstart-retuned.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/ccffdb6e8565-fd2fc062ffc2/main.py), [deck.csv](../agent_zoo/sources/ccffdb6e8565-fd2fc062ffc2/deck.csv)

Source SHA256: main.py `ccffdb6e85658dedf21dd3f9829b97bc29a1a2a30e986f79054d86796bfdab12`; deck.csv `fd2fc062ffc23c5a4f77f30c05d2fc1d08a7bade73e1dc67e1dd547192fd46b3`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53791767`

Public score: 799.5

Status: complete

Summary:
- Kept the Strong Start Crustle-aware Lucario policy.
- Switched from the original Lucario list to the retuned anti-Crustle deck.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s008-strongstart-retuned`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 799.5, the best result in this batch so far.
