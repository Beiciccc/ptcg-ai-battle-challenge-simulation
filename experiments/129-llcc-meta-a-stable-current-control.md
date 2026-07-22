# 129 LLCC Meta A Stable Current Control

Date: 2026-07-16 UTC

Local generated package (not committed): `artifacts/submissions/s129-llcc-meta-a-stable-current-control.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/6d2c8efc2243-fbe6ab599922/main.py), [deck.csv](../agent_zoo/sources/6d2c8efc2243-fbe6ab599922/deck.csv)

Source SHA256: main.py `6d2c8efc224392dcc439fa7ce20669daf279aa0208b23f87a7bab988b93561e2`; deck.csv `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54748977`

Validation episode: `86204895`

Public score: 847.2

Status: complete

Summary:
- Re-submitted Stable LLCC as the third current-day strategy family after the
  Alakazam and Tomato observations showed substantial score movement.
- The archive bytes matched experiments 115, 119, and 124 exactly.
- The validation episode completed, and later public score refreshes rose
  substantially above its initial readings.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- Final top-level function: `agent`
- 60-card deck check
- Three seeded smoke battles completed in 135, 149, and 151 steps
- Archive SHA-256: `71b3b53a4f21116c05bf8462ac2c5163d2ef3028fc38db58f77004a2f3751e5f`

Result:
- Kaggle validation episode `86204895` completed.
- Current public score is 847.2.
