# 167 Tien Search Alakazam Engine 1.32.2 Anchor

Date: 2026-07-24 UTC

Local generated package (not committed): `artifacts/submissions/s167-tien-search-alakazam-engine-1-32-2-anchor.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/235084ae725e-a8c9177354b9/main.py), [deck.csv](../agent_zoo/sources/235084ae725e-a8c9177354b9/deck.csv)

Source SHA256: main.py `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`; deck.csv `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`

Reproducibility: exact strategy snapshot with Kaggle Environments 1.32.2 runtime binaries

Kaggle submission: `54939180`

Public score: 600.0

Status: complete

Sources:
- [Search-Augmented Heuristic Agent (Alakazam)](https://www.kaggle.com/code/tientrum/search-augmented-heuristic-agent-alakazam)
- [Minor Engine update](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/discussion/728587)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Preserved the mature Search-Augmented Alakazam strategy and deck bytes while
  migrating the four platform binaries to Kaggle Environments 1.32.2.
- Retained the competition sample Python API files because the strategy
  requires search functions omitted by the wheel's reduced simulation wrapper.
- Verified the search ABI dynamically rather than treating exported symbols or
  normal game completion as sufficient compatibility evidence.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- New binaries export `SearchBegin`, `SearchStep`, `SearchEnd`,
  `SearchRelease`, `AgentStart`, `AllCard`, and `AllAttack`
- Three isolated extracted-archive battles completed normally in 166, 186,
  and 188 steps
- Those battles executed 663 successful search starts, 72,921 search steps,
  and 663 search completions with zero search failures
- Four seat-alternated battles against the 1.32.2 Tomato package completed
  2-2 in 25, 174, 163, and 140 steps with zero errors
- Strategy and deck bytes match the mature Tien archive exactly
- Main SHA-256: `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`
- Deck SHA-256: `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`
- Windows runtime SHA-256: `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256: `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256: `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256: `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256: `2838fc5380f23506485e9732a2870f68138fac9430d4f86c7ac701982a86e665`

Result:
- Kaggle accepted the package and marked submission `54939180` complete.
- Two spaced official reads remained at the 600.0 baseline; later score
  movement may occur as additional validation battles accumulate.
- Score checkpoint: `2026-07-24 00:36 UTC`.
