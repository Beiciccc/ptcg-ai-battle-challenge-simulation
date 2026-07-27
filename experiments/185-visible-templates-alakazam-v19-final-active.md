# 185 Visible Templates Alakazam v19 Final Active

Date: 2026-07-27 UTC

Local generated package (not committed):
`artifacts/submissions/s185-visible-templates-alakazam-v19-final-active.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: experiment 183 strategy with one additional loader entrypoint

Kaggle submission: `55024981`

Public score: 712.6

Status: complete

Sources:
- [Visible Templates Alakazam v19](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-visible-templates-alakazam-v19)
- [Tracking 3,057 teams through six weeks of meta](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/discussion/729926)

Summary:
- Preserved experiment 183's public strategy, deck, current runtime, and
  decision behavior.
- Appended `final_submission_entrypoint`, which delegates directly to the
  previously validated loader wrapper.
- Paired Alakazam with experiment 184 Garchomp to cover the current
  Grimmsnarl-heavy field and a possible Garchomp counter-rotation.

Validation:
- Static entrypoint check selected the unique final
  `final_submission_entrypoint`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Four fresh loader-aware mirror games completed without errors
- Twelve fresh games against experiment 184 Garchomp completed 7-5
- All 400 observed search calls completed without failures
- Maximum observed Alakazam decision latency was 0.249 seconds
- Main SHA-256:
  `e1ecbf36ccf06883b8692afc93769f6711722a3090a4bd7e94b8eb8bfd195ade`
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
  `be610489884b7996afb9a7540ebd66a47cb2eddabca98295a767a4ce4d39fb36`

Result:
- Initial direct creation attempts returned `Invalid token` and did not add an
  official submission row.
- The identical archive bytes were accepted after normalizing only the upload
  filename to `submission.tar.gz`.
- Kaggle marked submission `55024981` complete.
- Public evaluation moved from 600.0 to 712.6 as additional validation battles
  accumulated.
- Score checkpoint: `2026-07-27 09:48 UTC`.
