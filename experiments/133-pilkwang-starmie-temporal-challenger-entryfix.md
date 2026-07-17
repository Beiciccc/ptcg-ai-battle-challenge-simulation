# 133 Pilkwang Starmie Temporal Challenger Entryfix

Date: 2026-07-17 UTC

Package: `artifacts/submissions/s133-pilkwang-starmie-temporal-challenger-entryfix.tar.gz`

Kaggle submission: `54791084`

Validation episode: `86551085`

First public episode: `86551796`

Second public episode: `86552357`

Public score: 500.8

Status: complete

Source:
- [Pokemon TCG AI Battle Meta Snapshot 18 July](https://www.kaggle.com/code/pilkwang/pok-mon-tcg-ai-battle-meta-snapshot-18-july)

Summary:
- Tested the snapshot's Starmie Temporal Challenger as an independent profile
  from the current Alakazam, Stable LLCC, and Archaludon guards.
- Preserved the published policy and dependency files while replacing the
  object-only entrypoint with a minimal callable function required by the
  competition loader.
- Rebuilt the archive with the official July 17 engine update that corrected
  Team Rocket Energy attachment behavior.

Validation:
- Clean 20-file archive with `main.py`, `deck.csv`, nine runtime files, the
  published model, and its eight-module Python package
- No links or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Candidate smoke battles completed in 52, 125, and 129 steps
- Archive-root smoke battle completed in 110 steps
- Entrypoint SHA-256: `a55b71536ed64adff81d05b0ffc49f222b635db68969b7ba3271cbcceaf77d89`
- Archive SHA-256: `1b75907aa9e2055bf15604d1b619951b908d9002a92816ac881ed10099721711`

Result:
- Kaggle validation episode `86551085` completed.
- Both observed public battles completed normally. The Starmie side lost on
  turn six to Mega Abomasnow ex and again after a 26-turn battle, confirming
  gameplay losses rather than a packaging or runtime failure.
- Six public episodes have now completed. Later matchmaker updates recovered
  the public score from 349.7 to the current 500.8, still below the guards.
- The profile is excluded from the final active pair unless later live evidence
  exceeds 800; the remaining final slots retain the stronger mature guards.
