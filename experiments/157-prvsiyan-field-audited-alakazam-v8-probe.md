# 157 Prvsiyan Field-Audited Alakazam V8 Probe

Date: 2026-07-22 UTC

Package: `artifacts/submissions/s157-prvsiyan-field-audited-alakazam-v8-probe.tar.gz`

Kaggle submission: `54891156`

Public score: 725.5

Status: complete

Source:
- [Field-Audited Alakazam V8](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-field-audited-alakazam-v8)

Summary:
- Tested the exact runnable archive published by the current Field-Audited
  Alakazam V8 Code version as a new policy probe.
- Retained the established Alakazam deck while testing a distinct main program
  with no optional search path.
- Preserved every published archive byte so the public result remains tied to
  the source artifact.

Validation:
- Exact-byte copy of the published `submission.tar.gz`
- Clean 12-member archive with `main.py`, `deck.csv`, and the current runtime
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Three isolated archive-root smoke battles completed in 160, 178, and 193 steps
- Two-orientation comparisons split 2-2 against experiment 155 and 2-2 against
  experiment 156 without runtime errors
- The deck excludes the community-reported Ninetales and Amarys crash pair
- Packaged engine binaries match the current competition sample
- Main SHA-256: `ec055c2e77a3865d94ef88f4a4498465130c19ef6f15321edd8a2faf83b28868`
- Deck SHA-256: `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`
- Archive SHA-256: `fec9855958d41b8e1f3f20e28da6cbe874eef75ee507ec66d6f7022526b2e184`

Result:
- Kaggle accepted the package and marked submission `54891156` complete.
- Public evaluation moved from the 600.0 baseline through 494.3, 509.2, and
  607.8 before reaching 725.5 as additional validation battles accumulated.
- Score checkpoint: `2026-07-22 01:53 UTC`.
