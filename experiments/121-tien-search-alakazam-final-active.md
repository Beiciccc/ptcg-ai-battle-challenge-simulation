# 121 Tien Search Alakazam Final Active

Date: 2026-07-14 UTC

Local generated package (not committed): `artifacts/submissions/s121-tien-search-alakazam-final-active.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/235084ae725e-a8c9177354b9/main.py), [deck.csv](../agent_zoo/sources/235084ae725e-a8c9177354b9/deck.csv)

Source SHA256: main.py `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`; deck.csv `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54677479`

Validation episode: `85890112`

Public score: 928.2

Status: complete

Source:
- [Search-Augmented Heuristic Agent (Alakazam)](https://www.kaggle.com/code/tientrum/search-augmented-heuristic-agent-alakazam)

Summary:
- Re-submitted the hardened Search-Augmented Alakazam package as the second
  final active profile after experiment 117 matured above 900.
- The archive bytes matched the successful experiment 117 package.
- Mature score refreshes rose above 925 and made this the strongest final
  active profile.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- Final top-level function: `agent`
- 60-card deck check
- Three seeded search battles completed in 180, 165, and 135 steps
- Maximum observed main-decision wall time: 0.223 seconds
- Archive SHA-256: `766fe6a21ee6f73b58f857a8cfefc6b43028b7f157face837c342d5d47a36798`

Result:
- Kaggle validation episode `85890112` completed.
- Mature public score was 928.2.
