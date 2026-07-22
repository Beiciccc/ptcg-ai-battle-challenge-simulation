# 091 LLCC Meta A Stable Submit

Date: 2026-07-08 UTC

Local generated package (not committed): `artifacts/submissions/s091-llcc-meta-a-stable-submit.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/6d2c8efc2243-fbe6ab599922/main.py), [deck.csv](../agent_zoo/sources/6d2c8efc2243-fbe6ab599922/deck.csv)

Source SHA256: main.py `6d2c8efc224392dcc439fa7ce20669daf279aa0208b23f87a7bab988b93561e2`; deck.csv `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54457712`

Validation episode: `84817434`

Public score: 900.7

Status: complete

Summary:
- Tested the fresh LLCC Meta A Stable public-code candidate as the final slot
  after current rerolls stayed below the recent guard range.
- Local validation passed, including package structure, deck validation, and
  one smoke battle from the extracted package directory.
- Latest refresh remained the strongest result of the cycle, keeping this
  package as an active anchor.

Validation:
- `tar -tzf artifacts/submissions/s091-llcc-meta-a-stable-submit.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84817434` completed.
- Latest refreshed public score was 900.7.
