# 010 Resubmit Crustle Specific

Date: 2026-06-18

Local generated package (not committed): `artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/6de341ae762f-9c2647bd80d5/main.py), [deck.csv](../agent_zoo/sources/6de341ae762f-9c2647bd80d5/deck.csv)

Source SHA256: main.py `6de341ae762f15a7d926f5359e783e189bf25d5a0cff5ec69f78a954d0bdb6d3`; deck.csv `9c2647bd80d51bfd9cf89c74026e6a53607903b94cae9c235fad0c2128aad3aa`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53791955`

Public score: 885.6

Status: complete

Summary:
- Restored the previous Crustle-specific policy and Crustle wall deck.
- Submitted it as a latest-window wall candidate because the original run had
  reached 766.6 after public games.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s010-resubmit-crustle-specific`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 885.6.
