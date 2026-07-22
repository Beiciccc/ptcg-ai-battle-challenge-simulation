# 131 LLCC Meta A Stable Final Active

Date: 2026-07-16 UTC

Local generated package (not committed): `artifacts/submissions/s131-llcc-meta-a-stable-final-active.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/6d2c8efc2243-fbe6ab599922/main.py), [deck.csv](../agent_zoo/sources/6d2c8efc2243-fbe6ab599922/deck.csv)

Source SHA256: main.py `6d2c8efc224392dcc439fa7ce20669daf279aa0208b23f87a7bab988b93561e2`; deck.csv `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54749353`

Validation episode: `86208000`

Public score: 892.6

Status: complete

Summary:
- Re-submitted Stable LLCC as the second final active profile after repeated
  current-day readings met the pre-defined replacement threshold.
- The archive bytes matched experiments 115, 119, 124, and 129 exactly.
- Later score refreshes recovered above the initial 600.0 readings.
- The latest two submissions now preserve the Tomato and Stable strategy
  families.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- Final top-level function: `agent`
- 60-card deck check
- Three seeded smoke battles completed in 102, 145, and 110 steps
- Archive SHA-256: `71b3b53a4f21116c05bf8462ac2c5163d2ef3028fc38db58f77004a2f3751e5f`

Result:
- Kaggle validation episode `86208000` completed.
- Latest refreshed public score is 892.6.
