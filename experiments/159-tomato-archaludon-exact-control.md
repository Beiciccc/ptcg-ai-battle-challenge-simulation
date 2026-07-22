# 159 Tomato Archaludon Exact Control

Date: 2026-07-22 UTC

Local generated package (not committed): `artifacts/submissions/s159-tomato-archaludon-exact-control.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/03216723e42e-42165967b565/main.py), [deck.csv](../agent_zoo/sources/03216723e42e-42165967b565/deck.csv)

Source SHA256: main.py `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`; deck.csv `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54891424`

Public score: 642.8

Status: complete

Source:
- [A Sample Archaludon 75% WR vs My 1300 Starmie](https://www.kaggle.com/code/masamikobayashi/a-sample-archaludon-75-wr-vs-my-1300-starmie)

Summary:
- Re-submitted the exact experiment 156 archive as a distinct strategy-family
  control beside the two current Alakazam observations.
- Preserved every archive byte so the new observation changes only the public
  evaluation window.

Validation:
- Archive bytes match experiments 151, 154, and 156 exactly
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- A new-seed archive-root smoke battle completed normally in 72 steps
- Packaged engine binaries match the current competition sample
- Main SHA-256: `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`
- Deck SHA-256: `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`
- Archive SHA-256: `7024a524fc5fcbc150e30861e2f07dcec4575b6723416ed5d7d926fbaba18d4f`

Result:
- Kaggle accepted the package and marked submission `54891424` complete.
- Public evaluation rose from the 600.0 baseline through 712.7 and 832.7
  before later movement reached 642.8.
- Score checkpoint: `2026-07-22 02:08 UTC`.
