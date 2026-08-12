# 195 Jazivxt Crustle v29 Exact Public Archive

Date: 2026-07-30 UTC

Local generated package (not committed):
`artifacts/submissions/s195-jazivxt-crustle-v29-exact-public-archive.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: exact public Code output

Kaggle submission: `55098511`

Public score: 705.4

Status: complete

Sources:
- [Crustle Counter v29](https://www.kaggle.com/code/jazivxt/crustle-counter-al220-v29-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Tested the exact public Crustle v29 archive as the complementary final
  strategy beside experiment 194 Garchomp.
- Preserved the published policy, 60-card deck, helper files, selector data,
  current runtime, and archive bytes.
- The official loader selects the earlier base function named `agent` because
  the later v29 wrapper reuses existing global names. This exact selected
  behavior, rather than an entry-fixed variant, was validated and submitted.

Validation:
- Kaggle's `get_last_callable` selected the base function named `agent`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean root archive with the full current runtime and published helper files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Fifty-six seat-alternated games completed 28-28 without errors
- Matchup results: 5-11 against Steel, 11-5 against Alakazam v23, 5-11
  against replay-trained Grimmsnarl, and 7-1 against Garchomp v28
- The Garchomp counter result supplied the complementary evidence for the
  final active pair
- Main SHA-256:
  `5efff0b1c51d86adff8d9c134fdf45cb05c3cc0d5b344510b7e35f42ce1db70b`
- Deck SHA-256:
  `e3b7429fa5b1858ad995577ba0fce953c5d92027bed9ed94a1d4cbec64ce3151`
- Windows runtime SHA-256:
  `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256:
  `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256:
  `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256:
  `c342491c38afe44941efb366dbb212825381f3de64b286170029f7db1e795a16`

Result:
- Kaggle accepted the package as submission `55098511` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline to 705.4.
- The latest two submissions retain Garchomp and Crustle as distinct strategy
  families.
- Score checkpoint: `2026-07-30 03:38 UTC`.
