# Experiment Log

| ID | Date | Package | Public score | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 000 | 2026-06-17 | `baseline.zip` | n/a | prepared | Deterministic starter policy and sample deck; not submitted yet. |
| 001 | 2026-06-17 | `s001-generic-abomasnow.tar.gz` | n/a | error | Generic heuristic with sample deck. Validation episode failed because the loader bound to the last helper function instead of `agent()`. Entrypoint check added. |
| 002 | 2026-06-17 | `s002-generic-abomasnow-entryfix.tar.gz` | 556.4 | complete | Same generic heuristic and sample deck after entrypoint fix. Validated successfully but weak public rating. |
| 003 | 2026-06-17 | `s003-crustle-wall.tar.gz` | 741.4 | complete | Crustle wall deck with generic heuristic plus light healing/tool rules. Best early improvement came from the deck change. |
| 004 | 2026-06-17 | `s004-crustle-specific.tar.gz` | 766.6 | complete | Crustle wall deck with deck-specific sequencing. Best score in this batch at latest refresh. |
| 005 | 2026-06-17 | `s005-lucario-tempo.tar.gz` | 423.4 | complete | Mega Lucario deck with concise tempo policy. Underperformed Crustle. |
| 006 | 2026-06-17 | `s006-lucario-full-policy.tar.gz` | 870.3 | complete | Mega Lucario deck with fuller public-rule policy. Highest refreshed score from the first batch. |
| 007 | 2026-06-18 | `s007-strongstart-lucario.tar.gz` | 757.1 | complete | Strong Start Crustle-aware Lucario policy with original Lucario deck. Improved after additional public games. |
| 008 | 2026-06-18 | `s008-strongstart-retuned.tar.gz` | 799.5 | complete | Strong Start policy with retuned anti-Crustle deck. Best refreshed score from the second-day batch so far. |
| 009 | 2026-06-18 | `s009-resubmit-lucario-full.tar.gz` | 893.0 | complete | Resubmitted the previous high-scoring full Lucario policy. Latest refreshed score became the best observed result so far. |
| 010 | 2026-06-18 | `s010-resubmit-crustle-specific.tar.gz` | 761.4 | complete | Resubmitted the Crustle-specific policy as a wall candidate. Refreshed score nearly matched the original Crustle-specific run. |
| 011 | 2026-06-18 | `s011-final-strongstart-retuned.tar.gz` | 885.8 | complete | Re-submitted the retuned Strong Start list after it became the best refreshed second-day result. Latest refreshed score became a strong guard result. |
| 012 | 2026-06-19 | `s012-roman-v7-guarded.tar.gz` | 748.4 | complete | Updated the retuned Strong Start policy with low-deck and extra selection guards from the public V7 notebook. Refreshed score stayed below prior guards. |
| 013 | 2026-06-19 | `s013-lucario-search-915.tar.gz` | 858.4 | complete | Tested the public 915+ Lucario search baseline with bounded forward search enabled. Best result from the 2026-06-19 exploratory set. |
| 014 | 2026-06-19 | `s014-yaroslav-lucario-v2.tar.gz` | 681.2 | complete | Tested the public Lucario V2 crustle-aware policy. Refreshed score stayed below prior guards. |
| 015 | 2026-06-19 | `s015-latest-two-guard-strongstart.tar.gz` | 694.3 | complete | Restored the retuned Strong Start guard as the first latest-two repair slot. Refreshed score underperformed the original run. |
| 016 | 2026-06-19 | `s016-latest-two-guard-lucario-full.tar.gz` | 746.6 | complete | Restored the full Lucario policy as the final latest-two repair slot. Refreshed score stayed below the original run. |
| 017 | 2026-06-20 | `s017-maktha-1084-baseline.tar.gz` | 600.0 | complete | Tested the public 1084.5 baseline candidate. Initial public score was 600.0. |
