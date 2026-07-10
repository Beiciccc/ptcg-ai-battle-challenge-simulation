# 098 Pilkwang 0909 Phantom Focus Standard Rebuild

Date: 2026-07-10 UTC

Package: `artifacts/submissions/s098-pilkwang-0909-phantom-focus-standard-rebuild.tar.gz`

Kaggle submission: `54513702`

Validation episode: `85132675`

Public score: 600.0

Status: complete

Summary:
- Rebuilt the Phantom Focus Transfer candidate with the standard 11-file
  package layout after the prior archive failed before validation.
- Local validation passed for the archive layout, entrypoint, 60-card deck,
  bare-namespace loading, and three smoke battles from the extracted root.
- The new validation episode completed successfully, isolating the earlier
  failure to the submission package or creation path.

Validation:
- `python tools/package_submission.py --format tar.gz`
- `tar -tzf artifacts/submissions/s098-pilkwang-0909-phantom-focus-standard-rebuild.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85132675` completed.
- First public score was 600.0.
