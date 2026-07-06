# 078 Pilkwang 0704 Archaludon Anchor

Date: 2026-07-06 UTC

Package: `artifacts/submissions/s078-pilkwang-0704-archaludon-anchor.tar.gz`

Kaggle submission: `54379422`

Public score: 682.6

Status: complete

Summary:
- Tested the 2026-07-04 public meta snapshot's Archaludon Metal Tempo anchor.
- This was selected after the Library-Out complement underperformed, because
  the snapshot described the anchor as a near-top field-weighted reference.
- The public score stayed below guard range, so the next slot spent only one
  more probe on the distinct pressure profile before returning to known guards.

Validation:
- `python tools/check_submission_entrypoint.py private/candidates/s078-pilkwang-0704-archaludon-anchor/main.py`
- `python tools/check_deck.py private/candidates/s078-pilkwang-0704-archaludon-anchor/deck.csv`
- `python tools/package_submission.py --source private/candidates/s078-pilkwang-0704-archaludon-anchor --name s078-pilkwang-0704-archaludon-anchor`
- `python tools/smoke_battle.py --agent private/candidates/s078-pilkwang-0704-archaludon-anchor/main.py --deck private/candidates/s078-pilkwang-0704-archaludon-anchor/deck.csv --games 1 --max-steps 400`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 682.6.
