# 140 Tien Search Alakazam Latest-Engine Final Active

Date: 2026-07-18 UTC

Local generated package (not committed): `artifacts/submissions/s140-tien-search-alakazam-latest-engine-final-active.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/235084ae725e-a8c9177354b9/main.py), [deck.csv](../agent_zoo/sources/235084ae725e-a8c9177354b9/deck.csv)

Source SHA256: main.py `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`; deck.csv `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54798090`

Validation episode: `86616487`

First public episode: `86616643`

Public score: 773.1

Status: complete

Source:
- [Search-Augmented Heuristic Agent (Alakazam)](https://www.kaggle.com/code/tientrum/search-augmented-heuristic-agent-alakazam)

Summary:
- Re-submitted the exact latest-engine archive from experiment 136 as the
  lower member of the final active pair.
- Kept Search-Augmented Alakazam because its prior fixed-engine run had 57
  public battles and the strongest mature result below Lucario.
- Preserved the package bytes so the new observation changes only the active
  submission window.

Validation:
- Exact-byte match with experiment 136
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck return
- Archive-root smoke battles completed in 34, 181, and 172 steps
- Official replay completed in 165 steps with no search crash, runtime error,
  timeout, invalid action, or unexpected stderr output
- Main SHA-256: `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`
- Deck SHA-256: `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`
- Archive SHA-256: `f66cfe7e6bdf06656b7d61265ff959309d20117a729de2cb6cf3117d651a1c76`

Result:
- Kaggle validation episode `86616487` completed normally in 165 steps with
  reward `[-1, 1]` and both players in the DONE state.
- The first public battle completed as a win.
- The score rose from the 600.0 baseline through 712.4 and 799.7, reached
  889.8, and later moved to 773.1 at the final audit checkpoint.
- This active-window observation is paired with Lucario in the final slot.
- Final audit checkpoint: `2026-07-18 03:59 UTC`.
