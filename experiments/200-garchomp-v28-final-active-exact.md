# 200 Garchomp v28 Final Active Exact

Date: 2026-07-31 UTC

Local generated package (not committed):
`artifacts/submissions/s200-garchomp-v28-final-active-exact.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 192, 194, and 197

Kaggle submission: `55124504`

Public score: 684.6

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Garchomp v28 entry-fixed archive as the final active profile
  beside experiment 199 Archaludon.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Selected Garchomp because its conservative repeated-score statistics and
  matchup coverage were stronger than the remaining exact alternatives.

Validation:
- Archive SHA-256 matched experiments 192, 194, and 197 exactly
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- No duplicate members, links, unsafe paths, or nested archive root
- The byte-identical archive retains non-executable AppleDouble and Python
  cache members; the official loader did not select or import them
- The prior 48-game anchor panel completed 32-16 without errors
- The prior 24-game extended panel and 16-game current comparison panel both
  completed without errors
- Garchomp covered Archaludon's Alakazam v23 and replay-trained Grimmsnarl
  weaknesses, while Archaludon covered Garchomp's Crustle risk
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55124504` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline through 521.0
  before recovering to 684.6.
- At the final checkpoint, the four byte-identical official rows read 961.3,
  726.3, 754.0, and 684.6, confirming substantial public-path variance.
- The latest two submissions preserve Archaludon and Garchomp as distinct
  strategy families.
- Score checkpoint: `2026-08-01 05:14 UTC`.
