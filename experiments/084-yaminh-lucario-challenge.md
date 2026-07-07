# 084 Yaminh Lucario Challenge

Date: 2026-07-07 UTC

Package: `artifacts/submissions/s084-yaminh-lucario-challenge.tar.gz`

Kaggle submission: `54410567`

Validation episode: `84493517`

Public score: 710.9

Status: complete

Summary:
- Tested a newly refreshed public Lucario/Fighting candidate after two
  current-meta rerolls opened low.
- The candidate passed local package and smoke validation, including a
  one-game self-play smoke battle.
- The latest refresh stayed below the leading guard packages, so the next slot
  returned to the Archaludon metal high-ceiling package.

Validation:
- `tar -tzf artifacts/submissions/s084-yaminh-lucario-challenge.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 800`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84493517` completed.
- Latest refreshed public score was 710.9.
