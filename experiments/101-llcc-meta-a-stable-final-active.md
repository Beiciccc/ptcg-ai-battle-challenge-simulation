# 101 LLCC Meta A Stable Final Active

Date: 2026-07-10 UTC

Local generated package (not committed): `artifacts/submissions/s101-llcc-meta-a-stable-final-active.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/6d2c8efc2243-fbe6ab599922/main.py), [deck.csv](../agent_zoo/sources/6d2c8efc2243-fbe6ab599922/deck.csv)

Source SHA256: main.py `6d2c8efc224392dcc439fa7ce20669daf279aa0208b23f87a7bab988b93561e2`; deck.csv `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54514154`

Validation episode: `85135116`

Public score: 741.2

Status: complete

Summary:
- Re-submitted the LLCC Meta A Stable package as the final active anchor after
  it remained the strongest result among the first four submissions.
- Local validation passed for the 11-file archive layout, entrypoint,
  60-card deck, and three smoke battles from the extracted root.
- Later score refreshes recovered above the initial result but stayed below
  the Tomato anchor.

Validation:
- `tar -tzf artifacts/submissions/s101-llcc-meta-a-stable-final-active.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85135116` completed.
- Latest refreshed public score was 741.2.
