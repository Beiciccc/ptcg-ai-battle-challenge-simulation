# 196 Jazivxt Archaludon Metal v28 Exact Public Archive

Date: 2026-07-31 UTC

Local generated package (not committed):
`artifacts/submissions/s196-jazivxt-archaludon-metal-v28-exact-public-archive.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: exact public Code output

Kaggle submission: `55123678`

Public score: 726.6

Status: complete

Sources:
- [Archaludon Metal GPU v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Tested the exact public Archaludon Metal v28 archive against the current
  runtime and an expanded six-strategy comparison panel.
- Preserved the published policy, 60-card deck, selector data, helper files,
  current runtime, and archive bytes.
- The official loader selects the earlier base function named `agent` because
  the later v28 wrapper reuses existing global names. Validation and submission
  therefore used the exact loader-selected behavior.

Validation:
- Kaggle's `get_last_callable` selected the base function named `agent`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean root archive with the full current runtime and published helper files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Ninety-six seat-alternated games completed 54-42 without errors
- Matchup results: 9-7 against Garchomp v28, 10-6 against Crustle v29,
  16-0 against Spidops / Tarountula, 7-9 against an Alakazam rule skeleton,
  9-7 against Steel, and 3-13 against Alakazam v23
- Main SHA-256:
  `085f399dadf5e15d0e89c13ad4288e22a727514a5b95f538877eb804f970962e`
- Deck SHA-256:
  `bb3d2c7167975be58701bb5b74b88d83c8eb6510b829b7a73219cafa14ad1ed7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`

Result:
- Kaggle accepted the package as submission `55123678` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline through 483.8
  before recovering to 726.6.
- The wide movement reinforces the need to treat early public readings as
  time-specific observations.
- Score checkpoint: `2026-07-31 02:21 UTC`.
