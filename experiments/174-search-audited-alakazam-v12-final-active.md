# 174 Search-Audited Alakazam V12 Final Active

Date: 2026-07-25 UTC

Local generated package (not committed): `artifacts/submissions/s174-search-audited-alakazam-v12-final-active.tar.gz`

Reproducibility: exact byte-for-byte rerun of experiment 169

Kaggle submission: `54970978`

Public score: 709.8

Status: complete

Sources:
- [Search-Audited Alakazam V12](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-search-audited-alakazam-v12)
- [Minor Engine update](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/discussion/728587)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Re-submitted the exact experiment 169 archive as an independent observation
  of the search-capable Alakazam strategy on Kaggle Environments 1.32.2.
- Retained the distinct Alakazam strategy family after refreshed public-code
  and discussion scans produced no newer runtime or policy evidence.
- Preserved all strategy, deck, runtime, and archive bytes.

Validation:
- Archive SHA-256 matched experiment 169 exactly
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck-return check
- Three fresh mirror battles completed in 155, 186, and 151 steps
- Eight fresh seat-alternated battles against Mega Lucario Prize-Pressure
  completed 6-2 in 125, 170, 141, 149, 107, 126, 125, and 37 steps
- All 11 battles completed without runtime or agent errors
- The fresh run executed 362 search decisions with zero search failures
- Maximum observed search-decision latency was 0.403 seconds
- Main SHA-256: `e39dbe4241eab3eab866ccf9305488aa59c95f927ea9ae12597f64b5f03fe074`
- Deck SHA-256: `0598646548d081832ec311c15fdc369b32c6f5e63175b0cfd1904d21fd082451`
- Windows runtime SHA-256: `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256: `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256: `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256: `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256: `89d7669bf6c78b466798676468b335a6b6273c45136bd57d5330b7539084b5fb`

Result:
- Kaggle accepted the package and marked submission `54970978` complete.
- Public evaluation moved from the 600.0 baseline to 709.8 as additional
  validation battles accumulated.
- Score checkpoint: `2026-07-25 08:25 UTC`.
