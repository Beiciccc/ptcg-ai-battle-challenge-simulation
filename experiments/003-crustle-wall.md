# 003 Crustle Wall

Date: 2026-06-17

Local generated package (not committed): `artifacts/submissions/s003-crustle-wall.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/c642b891c09b-9c2647bd80d5/main.py), [deck.csv](../agent_zoo/sources/c642b891c09b-9c2647bd80d5/deck.csv)

Source SHA256: main.py `c642b891c09baa8a86f0b19122418ce64f89896646863db0298202144daf77c6`; deck.csv `9c2647bd80d51bfd9cf89c74026e6a53607903b94cae9c235fad0c2128aad3aa`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53783789`

Public score: 741.4

Status: complete

Summary:
- Switched from the sample Mega Abomasnow deck to a Crustle wall deck.
- Added light card-specific handling for Hero's Cape, Jumbo Ice Cream, Cook,
  and Buddy-Buddy Poffin.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s003-crustle-wall`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 741.4, making this a clear improvement over
  the sample-deck baseline.
