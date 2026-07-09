# 093 Pilkwang 0909 Phantom Focus Transfer

Date: 2026-07-09 UTC

Package: `artifacts/submissions/s093-pilkwang-0909-phantom-focus-transfer.tar.gz`

Kaggle submission: `54481871`

Validation episode: n/a

Public score: n/a

Status: error

Summary:
- Tested the 2026-07-09 public meta snapshot's Phantom Focus Transfer profile.
- Local validation passed, including archive root structure, entrypoint check,
  deck validation, and one smoke battle from the extracted package directory.
- Kaggle returned an ERROR row with no validation episode, so the next slot
  should avoid this exact package path and use a known-complete profile.

Validation:
- `tar -tzf artifacts/submissions/s093-pilkwang-0909-phantom-focus-transfer.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle submission `54481871` returned status ERROR.
- No validation episode was available from the Kaggle episodes endpoint.
