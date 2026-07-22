# 020 Reroll Crustle Specific

Date: 2026-06-20

Local generated package (not committed): `artifacts/submissions/s020-reroll-crustle-specific.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/6de341ae762f-9c2647bd80d5/main.py), [deck.csv](../agent_zoo/sources/6de341ae762f-9c2647bd80d5/deck.csv)

Source SHA256: main.py `6de341ae762f15a7d926f5359e783e189bf25d5a0cff5ec69f78a954d0bdb6d3`; deck.csv `9c2647bd80d51bfd9cf89c74026e6a53607903b94cae9c235fad0c2128aad3aa`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53864421`

Public score: 783.2

Status: complete

Summary:
- Restored the Crustle-specific policy and Crustle wall deck from experiment
  010.
- Submitted it as the first final latest-two guard slot.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s020-reroll-crustle-specific`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 783.2.
