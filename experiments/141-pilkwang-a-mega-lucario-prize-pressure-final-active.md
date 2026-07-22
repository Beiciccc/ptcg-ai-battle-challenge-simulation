# 141 Pilkwang A Mega Lucario Prize-Pressure Final Active

Date: 2026-07-18 UTC

Local generated package (not committed): `artifacts/submissions/s141-pilkwang-a-mega-lucario-prize-pressure-final-active.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/459cf970d9ff-2a541d7bf3d9/main.py), [deck.csv](../agent_zoo/sources/459cf970d9ff-2a541d7bf3d9/deck.csv)

Source SHA256: main.py `459cf970d9ffc28fcb13473cff216750f17d53a35fa990fcab1805e00e78a848`; deck.csv `2a541d7bf3d9e6b36037123f53f4dfef6348223f79fd27095dafc602a5357c19`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54798297`

Validation episode: `86618120`

First public episode: `86618785`

Public score: 736.4

Status: complete

Source:
- [Pokemon TCG AI Battle Meta Snapshot 18 July](https://www.kaggle.com/code/pilkwang/pok-mon-tcg-ai-battle-meta-snapshot-18-july)

Summary:
- Re-submitted the exact latest-engine archive from experiment 134 as the
  final active profile.
- Kept Mega Lucario Prize-Pressure because its prior fixed-engine run completed
  nine public battles with a 7-2 record and reached 854.0.
- Preserved the package bytes so the new observation changes only the active
  submission window.

Validation:
- Exact-byte match with experiment 134
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck return
- Archive-root smoke battles completed in 133, 139, and 141 steps
- Official replay completed in 122 steps with no platform error, timeout, or
  invalid-action signal
- Main SHA-256: `459cf970d9ffc28fcb13473cff216750f17d53a35fa990fcab1805e00e78a848`
- Deck SHA-256: `2a541d7bf3d9e6b36037123f53f4dfef6348223f79fd27095dafc602a5357c19`
- Archive SHA-256: `4c4d86a9b5974a519b12504d3d1bc2ed7142549d5a04b1b9d938a0b96ae199e8`

Result:
- Kaggle validation episode `86618120` completed normally in 122 steps with
  reward `[-1, 1]` and both players in the DONE state.
- The first public battle completed as a win and raised the score from the
  600.0 baseline to 736.4.
- The final active pair is Search-Augmented Alakazam followed by Mega Lucario
  Prize-Pressure.
- Final audit checkpoint: `2026-07-18 03:59 UTC`.
