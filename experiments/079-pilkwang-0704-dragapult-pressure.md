# 079 Pilkwang 0704 Dragapult Pressure

Date: 2026-07-06 UTC

Package: `artifacts/submissions/s079-pilkwang-0704-dragapult-pressure.tar.gz`

Kaggle submission: `54379571`

Public score: 885.4

Status: complete

Summary:
- Tested the 2026-07-04 public meta snapshot's Phantom Dragapult pressure
  profile.
- This was the final probe from the same public snapshot after both the
  Library-Out complement and Archaludon anchor stayed weak.
- The public score recovered into the best result in this five-submission
  cycle.

Validation:
- `python tools/check_submission_entrypoint.py private/candidates/s079-pilkwang-0704-dragapult-pressure/main.py`
- `python tools/check_deck.py private/candidates/s079-pilkwang-0704-dragapult-pressure/deck.csv`
- `python tools/package_submission.py --source private/candidates/s079-pilkwang-0704-dragapult-pressure --name s079-pilkwang-0704-dragapult-pressure`
- `python tools/smoke_battle.py --agent main.py --deck deck.csv --games 1 --max-steps 400`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 885.4.
