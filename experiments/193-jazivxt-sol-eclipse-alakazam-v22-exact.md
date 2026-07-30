# 193 Jazivxt Sol Eclipse Alakazam v22 Exact

Date: 2026-07-30 UTC

Local generated package (not committed):
`artifacts/submissions/s193-jazivxt-sol-eclipse-alakazam-v22-exact.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: exact public Code output

Kaggle submission: `55098217`

Public score: 647.9

Status: complete

Sources:
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Tested the exact public Sol Eclipse Alakazam v22 archive on the updated
  native battle engine.
- Preserved the published policy, 60-card deck, loader entrypoint, current
  runtime, and archive bytes.
- The candidate adds a narrow late-game guard for Abra's Teleportation while
  retaining the Rising Tide strategy family.

Validation:
- Static and dynamic loader checks selected
  `codex_sol_eclipse_alakazam_v22`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean root archive with `main.py`, `deck.csv`, published metadata, and the
  full current runtime
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Forty-eight seat-alternated anchor games completed without errors
- Matchup results: 12-4 against Steel, 10-6 against Alakazam v23, and 7-9
  against replay-trained Grimmsnarl
- Twenty-four direct games against experiment 192 Garchomp split 12-12
- All observed search calls completed without failures
- Maximum observed decision latency was 0.384 seconds
- Main SHA-256:
  `f31eba2e819ee2b3d46765b4195ea7dab8f32d0b5d09cafd39b3823661f6b5aa`
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
  `78dde4d68910a7c841a4c989a7e39fe8ae4ec15b0ba278f28b7ba43cdec5476b`

Result:
- Kaggle accepted the package as submission `55098217` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline to 647.9.
- Score checkpoint: `2026-07-30 03:24 UTC`.
