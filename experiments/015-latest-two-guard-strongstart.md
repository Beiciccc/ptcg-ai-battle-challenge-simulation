# 015 Latest Two Guard Strong Start

Date: 2026-06-19

Local generated package (not committed): `artifacts/submissions/s015-latest-two-guard-strongstart.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/ccffdb6e8565-fd2fc062ffc2/main.py), [deck.csv](../agent_zoo/sources/ccffdb6e8565-fd2fc062ffc2/deck.csv)

Source SHA256: main.py `ccffdb6e85658dedf21dd3f9829b97bc29a1a2a30e986f79054d86796bfdab12`; deck.csv `fd2fc062ffc23c5a4f77f30c05d2fc1d08a7bade73e1dc67e1dd547192fd46b3`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53827828`

Public score: 694.3

Status: complete

Summary:
- Restored the retuned Strong Start policy and deck from experiment 011.
- Submitted it as the first latest-two guard after the exploratory 2026-06-19
  runs underperformed.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s015-latest-two-guard-strongstart`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 694.3.
