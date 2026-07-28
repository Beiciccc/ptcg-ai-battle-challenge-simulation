# 187 Prvsiyan Visible-Grim Belief Alakazam v23 Entry Fix

Date: 2026-07-28 UTC

Local generated package (not committed):
`artifacts/submissions/s187-prvsiyan-visible-grim-belief-alakazam-v23-entryfix.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: public v23 output with one loader-safe entrypoint

Kaggle submission: `55051109`

Public score: 793.9

Status: complete

Sources:
- [Visible-Grim Belief Alakazam v23](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-visible-grim-belief-alakazam-v23)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Preserved the public v23 Alakazam strategy, deck, runtime, and decision
  behavior.
- Appended only a fresh `submission_entrypoint` wrapper so Kaggle's loader
  selects the intended agent.
- Tested the new public policy as an independent response to Steel, Garchomp,
  and the replay-trained Grimmsnarl profile.

Validation:
- Static and dynamic loader checks selected `submission_entrypoint`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Four loader-aware mirror games completed 2-2 without errors
- Twenty-four games against Cynthia Garchomp completed 16-8
- Twenty-four games against Visible Templates Alakazam v19 completed 12-12
- Twenty-four games against current-runtime Steel completed 19-5
- Twenty-four games against replay-trained Grimmsnarl completed 7-17
- All observed search calls completed without failures
- Maximum observed Alakazam decision latency was 0.659 seconds
- Main SHA-256:
  `b44c68f9d25bda71b2c00dc5300f4548089a49765a364d5d978bd541079d54c7`
- Deck SHA-256:
  `0598646548d081832ec311c15fdc369b32c6f5e63175b0cfd1904d21fd082451`
- Windows runtime SHA-256:
  `a3a401d0f5ccc3474b9c8a7a2431920c4b728d28105a510aa6927ad6283e5cf7`
- Linux runtime SHA-256:
  `feafd4046b2f688bdb33a4972c139b78e13e243ab5707ece52c43cf39a34b887`
- Linux ARM64 runtime SHA-256:
  `116750365a1043f0d95e200bb283c042753cdbd44c7d16331827ad0a44df0553`
- macOS runtime SHA-256:
  `00154aee7d3071451096c929c52da9f9af360a2821e686671097f5011e5a5d95`
- Archive SHA-256:
  `81d8a7e00f8955d2be66b58ae03e382a86be90d9f841d4ad2505a0d1445fa38b`

Result:
- Kaggle accepted the package as submission `55051109` and marked it complete.
- Public evaluation moved from 600.0 through 706.8 before reaching 793.9.
- Score checkpoint: `2026-07-28 09:37 UTC`.
