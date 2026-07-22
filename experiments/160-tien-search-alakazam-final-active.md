# 160 Tien Search Alakazam Final Active

Date: 2026-07-22 UTC

Local generated package (not committed): `artifacts/submissions/s160-tien-search-alakazam-final-active.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/235084ae725e-a8c9177354b9/main.py), [deck.csv](../agent_zoo/sources/235084ae725e-a8c9177354b9/deck.csv)

Source SHA256: main.py `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`; deck.csv `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54891531`

Public score: 640.3

Status: complete

Source:
- [Search-Augmented Heuristic Agent (Alakazam)](https://www.kaggle.com/code/tientrum/search-augmented-heuristic-agent-alakazam)

Summary:
- Re-submitted the exact experiment 155 archive as the first final active
  strategy for the current submission window.
- Retained the mature Alakazam control because one young low-scoring rerun did
  not outweigh its repeated historical observations.
- Reserved the final slot for the currently stronger Tomato Archaludon family.

Validation:
- Archive bytes match experiments 150, 153, 155, and 158 exactly
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- A new-seed archive-root smoke battle completed normally in 178 steps
- Packaged engine binaries match the current competition sample
- Main SHA-256: `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`
- Deck SHA-256: `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`
- Archive SHA-256: `c651ecce49d10aa1975a359c08c179e10b7ecf1e2cb9703af1067c1b515aa1dd`

Result:
- Kaggle accepted the package and marked submission `54891531` complete.
- Public evaluation moved from the 600.0 baseline to 640.3 as additional
  validation battles accumulated.
- Score checkpoint: `2026-07-22 02:08 UTC`.
