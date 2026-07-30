# 191 Jazivxt A Better Hand Alakazam Rising Tide v21 Exact

Date: 2026-07-30 UTC

Local generated package (not committed):
`artifacts/submissions/s191-jazivxt-a-better-hand-alakazam-rising-tide-v21-exact.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: exact public Code output

Kaggle submission: `55097827`

Public score: 568.8

Status: complete

Sources:
- [A Better Hand Alakazam Rising Tide v21](https://www.kaggle.com/code/jazivxt/a-better-hand-alakazam-rising-tide-v21)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Tested the exact public Alakazam Rising Tide v21 output after the native
  battle-engine update.
- Preserved the published strategy, 60-card deck, loader entrypoint, current
  runtime, and archive bytes.
- The source-linked public result and local comparison panel did not transfer
  to this independent official evaluation.

Validation:
- Static and dynamic loader checks selected `competition_entrypoint`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Forty-eight seat-alternated games completed without errors
- Matchup results: 15-1 against Steel, 8-8 against Alakazam v23, and 9-7
  against replay-trained Grimmsnarl
- Maximum observed decision latency was 0.410 seconds
- Main SHA-256:
  `da8702c0f9b12836ec4c90c0a0203890fdaf058341c4145ffe5d1969db4d66dd`
- Deck SHA-256:
  `8eccc69c3bf7d499f38c6116c33c5fac837050bf0ec71a5a1883f0f20f41ddbc`
- Windows runtime SHA-256:
  `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256:
  `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256:
  `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256:
  `9aed12f6ae5eac45498d8c2a2b9554c3330e91b6853ed73eb47e4421783376f1`

Result:
- Kaggle accepted the package as submission `55097827` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline through 515.9,
  593.6, 476.6, and 580.1 before reaching 568.8.
- Score checkpoint: `2026-07-30 03:24 UTC`.
