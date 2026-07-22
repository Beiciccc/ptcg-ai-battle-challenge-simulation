# 150 Tien Search Alakazam Strategy Control

Date: 2026-07-20 UTC

Local generated package (not committed): `artifacts/submissions/s150-tien-search-alakazam-strategy-control.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/235084ae725e-a8c9177354b9/main.py), [deck.csv](../agent_zoo/sources/235084ae725e-a8c9177354b9/deck.csv)

Source SHA256: main.py `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`; deck.csv `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54844108`

Public score: 848.1

Status: complete

Source:
- [Search-Augmented Heuristic Agent (Alakazam)](https://www.kaggle.com/code/tientrum/search-augmented-heuristic-agent-alakazam)

Summary:
- Restored the strategy files used by the prior Search-Augmented Alakazam
  control from the public Code version that matches their recorded hashes.
- Preserved the exact `main.py` and `deck.csv` strategy bytes and paired them
  with the unchanged current competition runtime.
- Rebuilt the tar archive, so this experiment claims strategy-byte continuity
  rather than identity with the earlier archive metadata.

Validation:
- Strategy bytes match experiments 136, 140, 143, and 146
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Three isolated extracted-archive smoke battles completed in 58, 197, and 159
  steps
- Two-orientation comparisons completed without runtime errors: 8-0 against
  experiment 147 and 8-0 against experiment 149, with all games ending in 64
  to 170 steps
- Packaged engine binaries match the current competition sample
- Main SHA-256: `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`
- Deck SHA-256: `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`
- Archive SHA-256: `c651ecce49d10aa1975a359c08c179e10b7ecf1e2cb9703af1067c1b515aa1dd`

Result:
- Kaggle accepted the package and marked submission `54844108` complete.
- Public evaluation moved from the 600.0 baseline through 700.8, 788.9, and
  854.7 before reaching 848.1 as validation battles accumulated.
- Score checkpoint: `2026-07-21 00:55 UTC`.
