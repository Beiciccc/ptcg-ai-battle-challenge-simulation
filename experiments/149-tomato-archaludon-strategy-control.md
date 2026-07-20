# 149 Tomato Archaludon Strategy Control

Date: 2026-07-20 UTC

Package: `artifacts/submissions/s149-tomato-archaludon-strategy-control.tar.gz`

Kaggle submission: `54843996`

Public score: 453.0

Status: complete

Source:
- [A Sample Archaludon 75% WR vs My 1300 Starmie](https://www.kaggle.com/code/masamikobayashi/a-sample-archaludon-75-wr-vs-my-1300-starmie)

Summary:
- Restored the strategy files used by the prior Tomato Archaludon control from
  the public Code version that matches their recorded hashes.
- Preserved the exact `main.py` and `deck.csv` strategy bytes and paired them
  with the unchanged current competition runtime.
- Rebuilt the tar archive, so this experiment claims strategy-byte continuity
  rather than identity with the earlier archive metadata.

Validation:
- Strategy bytes match experiments 139, 144, and 145
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Three isolated extracted-archive smoke battles completed in 156, 142, and 91
  steps
- Two-orientation comparisons completed without runtime errors: 7-1 against
  experiment 147 and 4-4 against experiment 148
- Packaged engine binaries match the current competition sample
- Main SHA-256: `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`
- Deck SHA-256: `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`
- Archive SHA-256: `7024a524fc5fcbc150e30861e2f07dcec4575b6723416ed5d7d926fbaba18d4f`

Result:
- Kaggle accepted the package and marked submission `54843996` complete.
- Public evaluation moved through 600.0, 606.0, and 529.7 before reaching
  453.0 as validation battles accumulated.
- Score checkpoint: `2026-07-20 03:41 UTC`.
