# 077 Pilkwang 0704 LibraryOut Complement

Date: 2026-07-06 UTC

Package: `artifacts/submissions/s077-pilkwang-0704-libraryout-complement.tar.gz`

Kaggle submission: `54379313`

Public score: 600.0

Status: complete

Summary:
- Tested the 2026-07-04 public meta snapshot's Great Tusk / Crustle
  Library-Out complement profile.
- The public snapshot framed this profile as a portfolio complement for a
  wider field with Marnie/Munkidori, Starmie, and smaller stress archetypes.
- The public score stayed weak, so the next slot should prefer a stronger
  anchor profile rather than expanding this complement line immediately.

Validation:
- `python tools/check_submission_entrypoint.py private/candidates/s077-pilkwang-0704-libraryout-complement/main.py`
- `python tools/check_deck.py private/candidates/s077-pilkwang-0704-libraryout-complement/deck.csv`
- `python tools/package_submission.py --source private/candidates/s077-pilkwang-0704-libraryout-complement --name s077-pilkwang-0704-libraryout-complement`
- `python tools/smoke_battle.py --agent private/candidates/s077-pilkwang-0704-libraryout-complement/main.py --deck private/candidates/s077-pilkwang-0704-libraryout-complement/deck.csv --games 1 --max-steps 400`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Public score was 600.0.
