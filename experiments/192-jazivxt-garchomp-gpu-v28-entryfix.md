# 192 Jazivxt Garchomp GPU v28 Entry Fix

Date: 2026-07-30 UTC

Local generated package (not committed):
`artifacts/submissions/s192-jazivxt-garchomp-gpu-v28-entryfix.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: public Code output plus loader-only final wrapper repair

Kaggle submission: `55097974`

Public score: 961.3

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Tested the public Garchomp v28 strategy on the updated native battle engine.
- Preserved the published policy, 60-card deck, helper files, model weights,
  and runtime.
- Appended a fresh final wrapper name because the original archive's last
  callable did not resolve to its intended v28 entrypoint.

Validation:
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- Root archive with the full current runtime and published helper files
- No duplicate members, links, unsafe paths, or nested archive root
- The archive retains non-executable AppleDouble and Python cache members; the
  official loader did not select or import them
- Forty-eight seat-alternated games completed without errors
- Matchup results: 10-6 against Steel, 10-6 against Alakazam v23, and 12-4
  against replay-trained Grimmsnarl
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Windows runtime SHA-256:
  `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256:
  `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256:
  `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55097974` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline through 755.7,
  871.8, 776.1, and 817.0 before reaching 961.3.
- Score checkpoint: `2026-07-30 03:35 UTC`.
