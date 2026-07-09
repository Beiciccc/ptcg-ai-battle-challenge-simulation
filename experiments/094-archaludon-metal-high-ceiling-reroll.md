# 094 Archaludon Metal High Ceiling Reroll

Date: 2026-07-09 UTC

Package: `artifacts/submissions/s094-archaludon-metal-high-ceiling-reroll.tar.gz`

Kaggle submission: `54481944`

Validation episode: `84959122`

Public score: 619.9

Status: complete

Summary:
- Re-submitted the Archaludon metal high-ceiling package after the 2026-07-09
  public snapshot package returned an ERROR row.
- Local validation passed, including package structure, deck validation, and
  one smoke battle from the extracted package directory.
- Latest refresh stayed below the current cycle leader, so the next slot used a
  different known-complete pressure profile.

Validation:
- `tar -tzf artifacts/submissions/s094-archaludon-metal-high-ceiling-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84959122` completed.
- Latest refreshed public score was 619.9.
