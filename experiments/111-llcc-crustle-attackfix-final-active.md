# 111 LLCC Crustle AttackFix Final Active

Date: 2026-07-12 UTC

Package: `artifacts/submissions/s111-llcc-crustle-attackfix-final-active.tar.gz`

Kaggle submission: `54594245`

Validation episode: `85511889`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the leading LLCC Crustle AttackFix package as the second final
  active profile after experiment 107 exceeded 960.
- Local validation passed for the 11-file archive layout, bare-namespace
  loading, entrypoint, 60-card deck, and three smoke battles.
- The validation episode completed successfully and the first public score
  opened at 600.0.

Validation:
- `tar -tzf artifacts/submissions/s111-llcc-crustle-attackfix-final-active.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85511889` completed.
- First public score was 600.0.
