# 112 LLCC Crustle AttackFix Current Probe

Date: 2026-07-13 UTC

Package: `artifacts/submissions/s112-llcc-crustle-attackfix-current-probe.tar.gz`

Kaggle submission: `54626397`

Validation episode: `85657801`

Public score: 600.0

Status: complete

Summary:
- Re-submitted LLCC Crustle AttackFix as the current-day anchor after no newer
  evidence-backed public payload appeared.
- Local validation passed for the 11-file archive layout, bare-namespace
  loading, entrypoint, 60-card deck, and three smoke battles.
- The validation episode completed successfully and the first public score
  opened at 600.0.

Validation:
- `tar -tzf artifacts/submissions/s112-llcc-crustle-attackfix-current-probe.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85657801` completed.
- First public score was 600.0.
