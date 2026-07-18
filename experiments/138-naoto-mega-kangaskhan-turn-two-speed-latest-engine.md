# 138 Naoto Mega Kangaskhan Turn-Two Speed Latest-Engine

Date: 2026-07-18 UTC

Package: `artifacts/submissions/s138-naoto-mega-kangaskhan-turn-two-speed-latest-engine.tar.gz`

Kaggle submission: `54797740`

Validation episode: `86612649`

Public score: 600.0

Status: complete

Source:
- [Mega Kangaskhan ex: Turn-Two Speed Deck](https://www.kaggle.com/code/naoto714/en-mega-kangaskhan-ex-turn-two-speed-deck)

Summary:
- Tested the public Mega Kangaskhan Turn-Two Speed strategy as a distinct
  latest-engine strategy family.
- Preserved the published `main.py` and `deck.csv` bytes without an entrypoint
  modification.
- Rebuilt the package with the official July 17 engine update that corrected
  Team Rocket Energy attachment behavior.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck return
- Candidate smoke battles completed in 108, 159, and 145 steps with no fallback
- Archive-root smoke battle completed in 104 steps with no fallback
- Official replay completed in 116 steps; exact-byte replay checks reported no
  fallback, normalization repair, timeout, invalid action, or runtime error
- Main SHA-256: `101dfc2f5b8531a6157ced4c94a6453000a4d6dbce8320595559bab6b0066856`
- Deck SHA-256: `ac0c6d8134b084fb0c23bff6b9dcdcf58242d2853502a3dc468a3f61b0671c1b`
- Archive SHA-256: `c705f97897e876d4824e4e6fffdfbc2fdc0181a0a7cd5f69a6cc0635b8fb769e`

Result:
- Kaggle validation episode `86612649` completed normally with reward
  `[1, -1]` and both players in the DONE state.
- Two interval-separated official reads held at 600.0 before any public battle
  was recorded.
- The pre-public-battle score is retained as an initial observation rather than
  a mature estimate of the strategy's competitive strength.
