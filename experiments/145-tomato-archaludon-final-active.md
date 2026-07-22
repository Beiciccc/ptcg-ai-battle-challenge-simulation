# 145 Tomato Archaludon Final Active

Date: 2026-07-19 UTC

Local generated package (not committed): `artifacts/submissions/s145-tomato-archaludon-final-active.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/03216723e42e-42165967b565/main.py), [deck.csv](../agent_zoo/sources/03216723e42e-42165967b565/deck.csv)

Source SHA256: main.py `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`; deck.csv `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54819765`

Validation episode: `86797471`

Public score: 828.7

Status: complete

Summary:
- Re-submitted the exact latest-engine Tomato Archaludon archive as the first
  member of the final active pair.
- Retained Tomato because its current-day probe led the three-profile
  comparison before the final slots and its local matchups split 3-3 with both
  Alakazam and the improved Lucario heuristic.
- Preserved every archive byte so the new observation changes only the active
  public evaluation window.

Validation:
- Exact-byte match with experiments 139 and 144
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck return
- Archive-root smoke battles completed in 130, 33, and 110 steps
- Main SHA-256: `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`
- Deck SHA-256: `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`
- Archive SHA-256: `97de047d4f4cad11ac77378b1cbc52da3d11b0989f032be02ed3dce7eb8ff0f0`

Result:
- Kaggle accepted the package and marked submission `54819765` complete.
- Validation episode `86797471` reached the completed terminal state with
  reward `[-1, 1]`.
- Public evaluation later recovered from 599.1 to 828.7.
- Score checkpoint: `2026-07-20 03:04 UTC`.
