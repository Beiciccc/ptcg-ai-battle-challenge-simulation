# 163 Prvsiyan Search-Audited Alakazam V12

Date: 2026-07-23 UTC

Local generated package (not committed): `artifacts/submissions/s163-prvsiyan-search-audited-alakazam-v12.tar.gz`

Reproducibility: exact public Code output; Kaggle runtime required

Kaggle submission: `54919342`

Public score: 727.0

Status: complete

Source:
- [Search-Audited Alakazam V12](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-search-audited-alakazam-v12)

Summary:
- Tested the exact public Code output for a current-field Alakazam deck with
  deterministic option scoring and bounded forward search.
- Selected the candidate after the 2026-07-22 aggregate meta snapshot placed
  Alakazam first in both the 900-999 and 1000-1099 score bands.
- Preserved the published archive bytes so the public result remains tied to
  the reproducible upstream output.

Validation:
- Exact-byte copy of the published `submission.tar.gz`
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Three new-seed archive-root smoke battles completed normally in 186, 148,
  and 176 steps
- Packaged engine binaries match the current competition sample
- Main SHA-256: `e39dbe4241eab3eab866ccf9305488aa59c95f927ea9ae12597f64b5f03fe074`
- Deck SHA-256: `0598646548d081832ec311c15fdc369b32c6f5e63175b0cfd1904d21fd082451`
- Archive SHA-256: `24b451b81b48f7fb95a4f5c81856e01cfadf9a1279461b2dde569c4f3cb626ea`

Result:
- Kaggle accepted the package and marked submission `54919342` complete.
- Public evaluation moved from the 600.0 baseline through 689.8 and 760.4
  before later movement reached 727.0.
- Score checkpoint: `2026-07-23 05:07 UTC`.
