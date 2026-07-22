# 136 Tien Search Alakazam Latest-Engine Final Active

Date: 2026-07-17 UTC

Local generated package (not committed): `artifacts/submissions/s136-tien-search-alakazam-latest-engine-final-active.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/235084ae725e-a8c9177354b9/main.py), [deck.csv](../agent_zoo/sources/235084ae725e-a8c9177354b9/deck.csv)

Source SHA256: main.py `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`; deck.csv `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54791998`

Validation episode: `86558991`

Public episodes: `86559703`, `86560258`

Public score: 828.7

Status: complete

Source:
- [Search-Augmented Heuristic Agent (Alakazam)](https://www.kaggle.com/code/tientrum/search-augmented-heuristic-agent-alakazam)

Summary:
- Preserved the Search-Augmented Alakazam `main.py` and `deck.csv` bytes from
  experiment 132, which held the strongest mature current-day reading.
- Replaced the earlier runtime files with the complete official July 17 engine
  update that corrected Team Rocket Energy attachment behavior.
- Used the rebuilt package as the final active slot alongside latest-engine
  Stable LLCC.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck return
- Candidate smoke battles completed in 177, 169, and 177 steps
- Archive-root smoke battle completed in 187 steps
- Directed engine regression attached Team Rocket Energy to Team Rocket's
  Tarountula and observed `energyCards=[15]` with energy units `[11, 11]`
- Main SHA-256: `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`
- Deck SHA-256: `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`
- Archive SHA-256: `f66cfe7e6bdf06656b7d61265ff959309d20117a729de2cb6cf3117d651a1c76`

Result:
- Kaggle validation episode `86558991` completed.
- The first two public battles completed normally as wins on turns 11 and 6.
- The public score rose from 651.7 through 713.0 and 823.1 to the current
  828.7.
- The latest-engine rating should not be equated with the mature old-engine
  score. Future engine updates require fresh live evidence; older ratings may
  rank candidates but cannot validate a rebuilt package.
