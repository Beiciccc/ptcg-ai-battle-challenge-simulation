# 169 Prvsiyan Search-Audited Alakazam V12 Engine 1.32.2

Date: 2026-07-24 UTC

Local generated package (not committed): `artifacts/submissions/s169-prvsiyan-search-audited-alakazam-v12-engine-1-32-2.tar.gz`

Reproducibility: exact public strategy snapshot with Kaggle Environments 1.32.2 runtime binaries

Kaggle submission: `54939406`

Public score: 804.2

Status: complete

Sources:
- [Search-Audited Alakazam V12](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-search-audited-alakazam-v12)
- [Minor Engine update](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/discussion/728587)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Preserved the public Search-Audited Alakazam V12 strategy and deck bytes
  while migrating the four platform binaries to Kaggle Environments 1.32.2.
- Used the candidate to distinguish a Tien-specific low reading from a broader
  current-runtime Alakazam-family shift.
- Verified the full search path and decision latency before submission.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Three isolated extracted-archive battles completed normally in 144, 182,
  and 165 steps
- Those battles executed 471 successful search starts, 34,052 search steps,
  and 471 search completions with zero search failures
- Maximum observed search-decision latency was 0.193 seconds
- Four seat-alternated battles against the 1.32.2 LLCC package completed 4-0
  in 92, 158, 123, and 97 steps with zero errors
- Four seat-alternated battles against the 1.32.2 Tien package completed 3-1
  in 171, 32, 177, and 50 steps with zero errors
- Main SHA-256: `e39dbe4241eab3eab866ccf9305488aa59c95f927ea9ae12597f64b5f03fe074`
- Deck SHA-256: `0598646548d081832ec311c15fdc369b32c6f5e63175b0cfd1904d21fd082451`
- Windows runtime SHA-256: `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256: `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256: `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256: `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256: `89d7669bf6c78b466798676468b335a6b6273c45136bd57d5330b7539084b5fb`

Result:
- Kaggle accepted the package and marked submission `54939406` complete.
- Public evaluation moved from the 600.0 baseline through 715.2 to 804.2 as
  additional validation battles accumulated.
- Score checkpoint: `2026-07-24 01:02 UTC`.
