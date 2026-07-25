# 171 Maulik Crustle-Aware Lucario V5 Engine 1.32.2

Date: 2026-07-25 UTC

Local generated package (not committed): `artifacts/submissions/s171-maulik-crustle-aware-lucario-v5-engine-1-32-2.tar.gz`

Reproducibility: exact public strategy and deck snapshot with Kaggle Environments 1.32.2 runtime binaries

Kaggle submission: `54970462`

Public score: 605.2

Status: complete

Sources:
- [The Pokemon PTCG AI Battle Agent](https://www.kaggle.com/code/maulikgajera/the-pok-mon-ptcg-ai-battle-agent)
- [Minor Engine update](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/discussion/728587)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Preserved the public V5 strategy and its 60-card Lucario deck while replacing
  the older competition-data binaries with Kaggle Environments 1.32.2.
- Kept the optional search, learned evaluation, and PIMC branches disabled,
  matching the notebook's published selection after its validation runs.
- Evaluated the Crustle-aware policy as a current-code exploratory profile
  before reserving the final two submission positions for stronger controls.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck-return check
- The source notebook reported 30 error-free mirror games, 30 error-free games
  against random play, and a 73-27 Crustle-wall result with its policy enabled
- Six extracted-archive mirror battles completed in 155, 121, 156, 140, 131,
  and 171 steps without errors
- Eight seat-alternated battles against Search-Audited Alakazam V12 completed
  1-7 in 155, 161, 159, 81, 135, 146, 117, and 124 steps without errors
- Eight seat-alternated battles against Archaludon Metal completed 8-0 in 142,
  144, 118, 94, 48, 128, 124, and 143 steps without errors
- Eight seat-alternated battles against the Great Tusk / Crustle V11 control
  completed 8-0 in 104, 36, 30, 78, 67, 45, 88, and 58 steps without errors
- Main SHA-256: `102e2d63ed629538b7f32b45f4e1cd251d078425d491b1f5ffc7e0ca2215d914`
- Deck SHA-256: `b4464eb525a25e6598a972d00efc5e5b5156372e77f51853f4076d8ebb34fd7d`
- Windows runtime SHA-256: `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256: `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256: `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256: `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256: `8b4b478127d2ad769d5781430f5abf7db6a11893df4c3274945275de56bd94f9`

Result:
- Kaggle accepted the package and marked submission `54970462` complete.
- Public evaluation moved from the 600.0 baseline to 605.2.
- Score checkpoint: `2026-07-25 07:59 UTC`.
