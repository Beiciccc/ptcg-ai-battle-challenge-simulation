# 107 LLCC Crustle AttackFix

Date: 2026-07-12 UTC

Local generated package (not committed): `artifacts/submissions/s107-llcc-crustle-attackfix.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/c32e65488f71-fbe6ab599922/main.py), [deck.csv](../agent_zoo/sources/c32e65488f71-fbe6ab599922/deck.csv)

Source SHA256: main.py `c32e65488f71fb2978ac308ae9b812891aa28276b13e1966d0edaeb1a80ab98d`; deck.csv `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54593777`

Validation episode: `85508912`

Public score: 964.3

Status: complete

Summary:
- Tested the LLCC Crustle AttackFix variant after a public roster update
  supplied current matchup evidence.
- The candidate keeps the Stable deck and narrows the Metal Defender and
  Raging Hammer overrides to opposing Crustle.
- Local validation passed for the 11-file archive layout, bare-namespace
  loading, entrypoint, 60-card deck, and three smoke battles.
- Later score refreshes recovered into the mid-900 range and made this the
  strongest result of the 2026-07-12 cycle.

Validation:
- `tar -tzf artifacts/submissions/s107-llcc-crustle-attackfix.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85508912` completed.
- Latest refreshed public score was 964.3.
