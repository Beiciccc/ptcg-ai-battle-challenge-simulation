# 190 Prvsiyan Visible-Grim Belief Alakazam v23 Final Active

Date: 2026-07-28 UTC

Local generated package (not committed):
`artifacts/submissions/s190-prvsiyan-visible-grim-belief-alakazam-v23-final-active.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiment 187

Kaggle submission: `55052245`

Public score: 609.8

Status: complete

Sources:
- [Visible-Grim Belief Alakazam v23](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-visible-grim-belief-alakazam-v23)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact experiment 187 Alakazam v23 archive as the second final
  active strategy.
- Preserved the public strategy, 60-card deck, loader entrypoint, runtime, and
  archive bytes.
- Paired Alakazam v23 with experiment 189 Steel as two distinct strategy
  families.

Validation:
- Archive SHA-256 matched experiment 187 exactly
- Static and dynamic loader checks selected `submission_entrypoint`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Two fresh loader-aware mirror games completed 2-0 without errors
- No invalid actions or timeouts occurred
- All 330 search starts and completions succeeded across 28,038 search steps
- Maximum observed Alakazam decision latency was 0.280 seconds
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
- Kaggle accepted the package as submission `55052245` and marked it complete.
- Public evaluation moved from 600.0 through 496.3 before reaching 609.8.
- Score checkpoint: `2026-07-28 10:28 UTC`.
