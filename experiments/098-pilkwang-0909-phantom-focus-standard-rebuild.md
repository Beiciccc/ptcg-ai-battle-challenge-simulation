# 098 Pilkwang 0909 Phantom Focus Standard Rebuild

Date: 2026-07-10 UTC

Package: `artifacts/submissions/s098-pilkwang-0909-phantom-focus-standard-rebuild.tar.gz`

Kaggle submission: `54513702`

Validation episode: `85132675`

Public score: 514.5

Status: complete

Summary:
- Rebuilt the Phantom Focus Transfer candidate with the standard 11-file
  package layout after the prior archive failed before validation.
- Local validation passed for the archive layout, entrypoint, 60-card deck,
  bare-namespace loading, and three smoke battles from the extracted root.
- The new validation episode completed successfully, but later score
  refreshes remained weak.

Validation:
- `python tools/package_submission.py --format tar.gz`
- `tar -tzf artifacts/submissions/s098-pilkwang-0909-phantom-focus-standard-rebuild.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85132675` completed.
- Latest refreshed public score was 514.5.
