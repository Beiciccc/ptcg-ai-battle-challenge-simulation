# 165 Prvsiyan Great Tusk Crustle Control V11

Date: 2026-07-23 UTC

Local generated package (not committed): `artifacts/submissions/s165-prvsiyan-great-tusk-crustle-control-v11.tar.gz`

Reproducibility: exact public Code output; Kaggle runtime required

Kaggle submission: `54919632`

Public score: 710.7

Status: complete

Source:
- [Control V11 Meta Portfolio](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-control-v11-meta-portfolio)

Summary:
- Tested the exact public Code output for a Great Tusk / Crustle control
  strategy after its published comparison panel reported 29-11 against the
  mature Search-Augmented Alakazam package and 24-16 against Tomato
  Archaludon.
- Limited the candidate to one public probe because the published matchup
  table also reported a 5-27 result against the classic Crustle profile.
- Preserved the published archive bytes so the result remains tied to the
  reproducible upstream output.

Validation:
- Exact-byte copy of the published `submission.tar.gz`
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Three new-seed archive-root smoke battles completed normally in 122, 114,
  and 78 steps
- Packaged engine binaries match the current competition sample
- Main SHA-256: `f3caef5a8ef0b1e7d4d019009248223cbc9ce46b4f414eece9207b9a18700082`
- Deck SHA-256: `6415396d35c0f4b3d69ee6c231337968cc9f2d5d0767de801346d6f412c18e62`
- Archive SHA-256: `5d7699b8b33d420688a293e04405626c73b4e6d9c06954da592644ca1be3b87f`

Result:
- Kaggle accepted the package and marked submission `54919632` complete.
- Public evaluation moved from the 600.0 baseline to 710.7 as additional
  validation battles accumulated.
- Score checkpoint: `2026-07-23 05:07 UTC`.
