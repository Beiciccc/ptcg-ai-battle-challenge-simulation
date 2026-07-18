# 134 Pilkwang A Mega Lucario Prize-Pressure

Date: 2026-07-17 UTC

Package: `artifacts/submissions/s134-pilkwang-a-mega-lucario-prize-pressure.tar.gz`

Kaggle submission: `54791387`

Validation episode: `86553872`

First public episode: `86554591`

Public score: 854.0

Status: complete

Source:
- [Pokemon TCG AI Battle Meta Snapshot 18 July](https://www.kaggle.com/code/pilkwang/pok-mon-tcg-ai-battle-meta-snapshot-18-july)

Summary:
- Tested the snapshot's Mega Lucario Prize-Pressure reference after its focused
  confirmation reported an 86.5% field-weighted holdout over 432 games.
- Preserved the published `main.py` and `deck.csv` bytes without an entrypoint
  modification.
- Rebuilt the package with the official July 17 engine update that corrected
  Team Rocket Energy attachment behavior.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck return
- Candidate smoke battles completed in 139, 58, and 162 steps
- Archive-root smoke battle completed in 166 steps
- Published main SHA-256: `459cf970d9ffc28fcb13473cff216750f17d53a35fa990fcab1805e00e78a848`
- Published deck SHA-256: `2a541d7bf3d9e6b36037123f53f4dfef6348223f79fd27095dafc602a5357c19`
- Archive SHA-256: `4c4d86a9b5974a519b12504d3d1bc2ed7142549d5a04b1b9d938a0b96ae199e8`

Result:
- Kaggle validation episode `86553872` completed.
- The first public battle completed normally as a turn-16 win.
- The first two interval-separated public score readings held at 689.7. The
  score was 799.2 at the final-pair checkpoint and later rose to 854.0.
- Later score movement raised Lucario to 854.0, the strongest current reading
  among the latest-engine experiments. The observation remains less mature
  than the longer-running Alakazam and Stable ratings.
