# 087 Pilkwang 0808 Alakazam Live Backed

Date: 2026-07-08 UTC

Package: `artifacts/submissions/s087-pilkwang-0808-alakazam-live-backed.tar.gz`

Kaggle submission: `54457221`

Validation episode: `84815429`

Public score: 733.3

Status: complete

Summary:
- Tested the 2026-07-08 public meta snapshot's Alakazam live-backed reference
  after the snapshot reported a 943.8 live reference and selected it as the
  conservative default.
- Local validation passed, including package structure and one self-play smoke
  battle.
- The latest refresh recovered modestly but stayed below the recent guard
  references, so the next slot returned to the Archaludon metal high-ceiling
  package.

Validation:
- `tar -tzf artifacts/submissions/s087-pilkwang-0808-alakazam-live-backed.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84815429` completed.
- Latest refreshed public score was 733.3.
