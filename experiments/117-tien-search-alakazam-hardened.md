# 117 Tien Search Alakazam Hardened

Date: 2026-07-14 UTC

Local generated package (not committed): `artifacts/submissions/s117-tien-search-alakazam-hardened.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/235084ae725e-a8c9177354b9/main.py), [deck.csv](../agent_zoo/sources/235084ae725e-a8c9177354b9/deck.csv)

Source SHA256: main.py `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`; deck.csv `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54676655`

Validation episode: `85886634`

Public score: 860.3

Status: complete

Source:
- [Search-Augmented Heuristic Agent (Alakazam)](https://www.kaggle.com/code/tientrum/search-augmented-heuristic-agent-alakazam)
- The published checkpoint reports a 1034.6 ladder result from 2026-07-05 and
  identifies itself as an older, superseded checkpoint.

Summary:
- Rebuilt the published 60-card Alakazam checkpoint with the standard
  cross-platform competition runtime.
- Added the missing `sys` import used by search fallback diagnostics. No
  strategy weights, search parameters, or deck entries changed.
- Later score refreshes recovered above 850 and moved the checkpoint back into
  provisional final-active contention.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- Final top-level function: `agent`
- 60-card deck check
- Missing-template and missing-search-input fallback checks
- Three seeded archive-root smoke battles completed in 168, 181, and 159 steps
- Maximum observed main-decision wall time: 0.808 seconds
- Archive SHA-256: `766fe6a21ee6f73b58f857a8cfefc6b43028b7f157face837c342d5d47a36798`

Result:
- Kaggle validation episode `85886634` completed.
- Latest refreshed public score was 860.3.
