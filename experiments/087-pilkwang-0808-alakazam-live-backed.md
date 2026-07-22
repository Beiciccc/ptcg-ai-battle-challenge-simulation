# 087 Pilkwang 0808 Alakazam Live Backed

Date: 2026-07-08 UTC

Local generated package (not committed): `artifacts/submissions/s087-pilkwang-0808-alakazam-live-backed.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/46aae79654ec-0f8fb632ade2/main.py), [deck.csv](../agent_zoo/sources/46aae79654ec-0f8fb632ade2/deck.csv)

Source SHA256: main.py `46aae79654eca7d91e9a3c840d92e38d3ac6271b052379df43dc630163f68225`; deck.csv `0f8fb632ade2833645af8c6ffe2b282fe24e7446ee8b23f3e468b8410d8ea36c`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54457221`

Validation episode: `84815429`

Public score: 660.8

Status: complete

Summary:
- Tested the 2026-07-08 public meta snapshot's Alakazam live-backed reference
  after the snapshot reported a 943.8 live reference and selected it as the
  conservative default.
- Local validation passed, including package structure and one self-play smoke
  battle.
- The latest refresh stayed below the recent guard references, so the next
  slot returned to the Archaludon metal high-ceiling package.

Validation:
- `tar -tzf artifacts/submissions/s087-pilkwang-0808-alakazam-live-backed.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84815429` completed.
- Latest refreshed public score was 660.8.
