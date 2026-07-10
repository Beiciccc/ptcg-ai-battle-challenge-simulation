# 097 LLCC Meta A Stable Reroll

Date: 2026-07-10 UTC

Package: `artifacts/submissions/s097-llcc-meta-a-stable-reroll.tar.gz`

Kaggle submission: `54513582`

Validation episode: `85131722`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the LLCC Meta A Stable package after experiment 091 remained
  the strongest recent confirmed anchor.
- Local validation passed, including archive structure, entrypoint and deck
  checks, and three smoke battles with distinct seeds.
- The validation episode completed successfully, but the first public score
  opened well below the package's prior results.

Validation:
- `tar -tzf artifacts/submissions/s097-llcc-meta-a-stable-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `85131722` completed.
- First public score was 600.0.
