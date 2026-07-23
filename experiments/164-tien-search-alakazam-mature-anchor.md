# 164 Tien Search Alakazam Mature Anchor

Date: 2026-07-23 UTC

Local generated package (not committed): `artifacts/submissions/s164-tien-search-alakazam-mature-anchor.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/235084ae725e-a8c9177354b9/main.py), [deck.csv](../agent_zoo/sources/235084ae725e-a8c9177354b9/deck.csv)

Source SHA256: main.py `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`; deck.csv `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54919474`

Public score: 600.0

Status: complete

Source:
- [Search-Augmented Heuristic Agent (Alakazam)](https://www.kaggle.com/code/tientrum/search-augmented-heuristic-agent-alakazam)

Summary:
- Re-submitted the exact mature Search-Augmented Alakazam archive after two
  new public candidates opened below the established control distribution.
- Used the exact-byte archive with 15 prior official observations rather than
  rebuilding or retuning the strategy.

Validation:
- Archive bytes match experiments 150, 153, 155, 158, and 160 exactly
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Three new-seed archive-root smoke battles completed normally in 187, 174,
  and 175 steps
- Packaged engine binaries match the current competition sample
- Main SHA-256: `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`
- Deck SHA-256: `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`
- Archive SHA-256: `c651ecce49d10aa1975a359c08c179e10b7ecf1e2cb9703af1067c1b515aa1dd`

Result:
- Kaggle accepted the package and marked submission `54919474` complete.
- Two official reads remained at the 600.0 baseline; later score movement may
  occur as additional validation battles accumulate.
- Score checkpoint: `2026-07-23 04:57 UTC`.
