# 173 Plamen06 Steel Search-Disabled Engine 1.32.2

Date: 2026-07-25 UTC

Local generated package (not committed): `artifacts/submissions/s173-plamen06-steel-search-disabled-engine-1-32-2.tar.gz`

Reproducibility: public strategy snapshot with one documented compatibility flag change and Kaggle Environments 1.32.2 runtime binaries

Kaggle submission: `54970766`

Public score: 600.0

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Public 46 + Sample 4 Roster Update](https://www.kaggle.com/code/makimakiai/ptcg-public-28-plus-sample-4-roster-update)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Selected the public Steel strategy after the latest 50-agent matrix reported
  385 wins and 105 losses, the highest aggregate result in 12,250 games.
- Preserved the published strategy and deck except for setting its optional
  search flag to false after a current-SDK compatibility audit.
- Replaced the older competition-data binaries with Kaggle Environments 1.32.2.

Compatibility finding:
- The published search branch calls `search_begin` with one serialized input,
  while the mounted public Python API requires seven positional arguments.
- An instrumented game observed 57 eligible search decisions and 57 caught
  `TypeError` results before the strategy fell back to its heuristic.
- Disabling the branch removed those exceptions and matched the published
  fallback action on 199 consecutive decisions across three battles.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck-return check
- Six extracted-archive mirror battles completed in 104, 152, 55, 126, 73,
  and 165 steps without errors
- Eight seat-alternated battles against Search-Audited Alakazam V12 split 4-4
  in 62, 140, 136, 136, 136, 148, 101, and 144 steps without errors
- Eight seat-alternated battles against Mega Lucario Prize-Pressure completed
  7-1 in 106, 123, 136, 132, 130, 146, 148, and 147 steps without errors
- Eight seat-alternated battles against Maulik V5 Lucario completed 5-3 in 167,
  129, 124, 122, 156, 162, 154, and 82 steps without errors
- Published main SHA-256: `4b3946f9a1078a5afad36fe584ce9474a5d5b495516ebd755553afd9b38f9bbf`
- Submitted main SHA-256: `4cc4c469d1c5caced0439cb2db32ad4827a87f7dcc698419bef6c07fc64aedcb`
- Deck SHA-256: `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Windows runtime SHA-256: `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256: `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256: `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256: `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256: `b5c7601e843a9f7269513a1ba9489cc1354a8dbff52e0ddd74f93fa8ff165bf2`

Result:
- Kaggle accepted the package and marked submission `54970766` complete.
- The first completed public-score checkpoint was the 600.0 baseline.
- Score checkpoint: `2026-07-25 08:08 UTC`.
