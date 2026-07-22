# 132 Tien Search Alakazam Rebound Probe

Date: 2026-07-17 UTC

Local generated package (not committed): `artifacts/submissions/s132-tien-search-alakazam-rebound-probe.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/235084ae725e-a8c9177354b9/main.py), [deck.csv](../agent_zoo/sources/235084ae725e-a8c9177354b9/deck.csv)

Source SHA256: main.py `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`; deck.csv `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54790755`

Validation episode: `86548262`

Public score: 955.6

Status: complete

Source:
- [Search-Augmented Heuristic Agent (Alakazam)](https://www.kaggle.com/code/tientrum/search-augmented-heuristic-agent-alakazam)

Summary:
- Re-submitted the hardened Search-Augmented Alakazam package as a rebound
  probe after identical archives previously exceeded 900.
- The archive bytes matched experiments 117, 121, 122, 125, and 127 exactly.
- The validation episode completed and the public score moved from an initial
  731.9 reading through 936.7 and 963.0 to the current 955.6 reading.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- Final top-level function: `agent`
- 60-card deck check
- Three seeded smoke battles completed in 158, 166, and 168 steps
- Archive SHA-256: `766fe6a21ee6f73b58f857a8cfefc6b43028b7f157face837c342d5d47a36798`

Result:
- Kaggle validation episode `86548262` completed.
- Current public score is 955.6.
