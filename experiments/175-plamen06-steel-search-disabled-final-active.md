# 175 Plamen06 Steel Search-Disabled Final Active

Date: 2026-07-25 UTC

Local generated package (not committed): `artifacts/submissions/s175-plamen06-steel-search-disabled-final-active.tar.gz`

Reproducibility: exact byte-for-byte rerun of experiment 173

Kaggle submission: `54971134`

Public score: 600.0

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Public 46 + Sample 4 Roster Update](https://www.kaggle.com/code/makimakiai/ptcg-public-28-plus-sample-4-roster-update)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Re-submitted the exact experiment 173 archive after its independent public
  observation reached 966.4 and the latest 50-agent matrix had ranked the
  underlying Steel strategy first with a 385-105 aggregate record.
- Retained the documented search compatibility flag and all strategy, deck,
  runtime, and archive bytes from experiment 173.
- Paired Steel with the distinct Search-Audited Alakazam V12 strategy family.

Validation:
- Archive SHA-256 matched experiment 173 exactly
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck-return check
- Three fresh mirror battles completed in 164, 119, and 147 steps
- Eight fresh seat-alternated battles against Search-Audited Alakazam V12
  completed 3-5 in 131, 170, 39, 146, 170, 163, 136, and 129 steps
- All 11 battles completed without runtime or agent errors
- The disabled search branch was called zero times
- Maximum observed Steel decision latency was 0.074 seconds
- Submitted main SHA-256: `4cc4c469d1c5caced0439cb2db32ad4827a87f7dcc698419bef6c07fc64aedcb`
- Deck SHA-256: `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Windows runtime SHA-256: `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256: `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256: `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256: `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256: `b5c7601e843a9f7269513a1ba9489cc1354a8dbff52e0ddd74f93fa8ff165bf2`

Result:
- Kaggle accepted the package and marked submission `54971134` complete.
- The first completed public-score checkpoint was the 600.0 baseline.
- Score checkpoint: `2026-07-25 08:25 UTC`.
