# 166 Tomato Archaludon Engine 1.32.2 Anchor

Date: 2026-07-24 UTC

Local generated package (not committed): `artifacts/submissions/s166-tomato-archaludon-engine-1-32-2-anchor.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/03216723e42e-42165967b565/main.py), [deck.csv](../agent_zoo/sources/03216723e42e-42165967b565/deck.csv)

Source SHA256: main.py `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`; deck.csv `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`

Reproducibility: exact strategy snapshot with Kaggle Environments 1.32.2 runtime binaries

Kaggle submission: `54939046`

Public score: 541.9

Status: complete

Sources:
- [A Sample Archaludon 75% WR vs My 1300 Starmie](https://www.kaggle.com/code/masamikobayashi/a-sample-archaludon-75-wr-vs-my-1300-starmie)
- [Minor Engine update](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/discussion/728587)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Preserved the mature Tomato Archaludon `main.py` and `deck.csv` bytes while
  migrating the four platform binaries to Kaggle Environments 1.32.2.
- Applied the official runtime fix for a delayed-effect crash involving
  Ninetales and Amarys without changing the strategy or deck.
- Kept the competition sample Python API files because the wheel's reduced
  simulation wrapper omits the search declarations used by other strategies.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Three source-root smoke battles completed normally in 123, 106, and 139
  steps with the 1.32.2 runtime
- Three independent extracted-archive smoke battles completed normally in 164,
  119, and 117 steps
- Strategy and deck bytes match the mature Tomato archive exactly
- Main SHA-256: `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`
- Deck SHA-256: `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`
- Windows runtime SHA-256: `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256: `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256: `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256: `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256: `d8a5f24d5dd549eae2e1b518127900b9ce0566d8362eb131ea90156f92d72e4f`

Result:
- Kaggle accepted the package and marked submission `54939046` complete.
- Public evaluation remained at the 600.0 baseline on three early reads,
  moved through 698.6 and 615.8, and later reached 541.9.
- Score checkpoint: `2026-07-24 00:42 UTC`.
