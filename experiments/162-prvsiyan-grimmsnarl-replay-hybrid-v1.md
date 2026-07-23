# 162 Prvsiyan Grimmsnarl Replay Hybrid V1

Date: 2026-07-23 UTC

Local generated package (not committed): `artifacts/submissions/s162-prvsiyan-grimmsnarl-replay-hybrid-v1.tar.gz`

Reproducibility: exact public Code output; public model checkpoint and Kaggle runtime required

Kaggle submission: `54919201`

Public score: 507.4

Status: complete

Source:
- [Rmy Grimmsnarl Replay Hybrid](https://www.kaggle.com/code/prvsiyan/ptcg-rmy-grimmsnarl-replay-hybrid-v1)

Summary:
- Tested the exact public Code output for a replay-cloned Marnie's Grimmsnarl
  and Froslass strategy with two visible-board corrections.
- Selected the candidate after the 2026-07-22 aggregate meta snapshot placed
  Marnie Grimmsnarl first in the 1100+ score band.
- Preserved the published archive bytes, including its public model
  checkpoint, so the result remains tied to the reproducible upstream output.

Validation:
- Exact-byte copy of the published `submission.tar.gz`
- Clean 13-file archive root with `main.py`, `bc_agent.py`, `deck.csv`,
  `model.pt`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Three new-seed archive-root smoke battles completed normally in 202, 187,
  and 207 steps
- Packaged engine binaries match the current competition sample
- Main SHA-256: `f2e2c18d50570b15ab4380ec540c128afff45d84f989b4bdd8ea4ff1a901d398`
- Policy SHA-256: `9d58027de1edaae597920b82631f4abca51b8462fb755ecbffb741ac3a8dc754`
- Deck SHA-256: `92b92bac9f9163ecff933b3dc39294d2cc154c8684f3c8497877661419ebc59d`
- Model SHA-256: `2e5733afb26bef0842005dddd6ea142179b04f10c113786539b9e8f2fba145f1`
- Archive SHA-256: `6f17ba014f026c83625c3e959857539443f67e7427b2483103c8407f4fde71d7`

Result:
- Kaggle accepted the package and marked submission `54919201` complete.
- Public evaluation moved from the 600.0 baseline to 507.4 as additional
  validation battles accumulated.
- Score checkpoint: `2026-07-23 04:43 UTC`.
