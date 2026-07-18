# 137 Pilkwang Archaludon Metal Tempo Latest-Engine Control

Date: 2026-07-18 UTC

Package: `artifacts/submissions/s137-pilkwang-archaludon-metal-tempo-latest-engine-control.tar.gz`

Kaggle submission: `54797464`

Validation episode: `86610533`

Public episodes: `86611145`, `86611689`

Public score: 796.4

Status: complete

Summary:
- Migrated the reproducible Archaludon Metal Tempo strategy from experiment
  078 to the official July 17 engine update.
- Preserved the parent `main.py` and `deck.csv` bytes to isolate the runtime
  update from strategy changes.
- Used this run as a latest-engine control for a strategy family that had only
  older-engine leaderboard observations.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck return
- Candidate smoke battles completed in 155, 135, and 112 steps
- Archive-root smoke battle completed in 101 steps
- Main SHA-256: `a4c53101be301c181bd477204a72c0e5cba65fddd34d8cd0ec4d36e4b41c9518`
- Deck SHA-256: `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Archive SHA-256: `2961dba7de0143aa9d43fe7dbc92209a0f2c4e57c182b8792308f6533539a1c9`

Result:
- Kaggle validation episode `86610533` completed normally in 106 steps with
  no runtime, timeout, or invalid-action errors.
- The first two observed public battles completed as wins.
- The public score rose from the 600.0 baseline through 713.9, 795.8, and
  870.6 before later movement reached the current 796.4.
- This remains a high-variance result and requires comparison with the other
  current latest-engine profiles before selecting the final pair.
