# Experiment Log

| ID | Date | Package | Public score | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 000 | 2026-06-17 | `baseline.zip` | n/a | prepared | Deterministic starter policy and sample deck; not submitted yet. |
| 001 | 2026-06-17 | `s001-generic-abomasnow.tar.gz` | n/a | error | Generic heuristic with sample deck. Validation episode failed because the loader bound to the last helper function instead of `agent()`. Entrypoint check added. |
| 002 | 2026-06-17 | `s002-generic-abomasnow-entryfix.tar.gz` | 556.4 | complete | Same generic heuristic and sample deck after entrypoint fix. Validated successfully but weak public rating. |
| 003 | 2026-06-17 | `s003-crustle-wall.tar.gz` | 741.4 | complete | Crustle wall deck with generic heuristic plus light healing/tool rules. Best early improvement came from the deck change. |
| 004 | 2026-06-17 | `s004-crustle-specific.tar.gz` | 766.6 | complete | Crustle wall deck with deck-specific sequencing. Best score in this batch at latest refresh. |
| 005 | 2026-06-17 | `s005-lucario-tempo.tar.gz` | 423.4 | complete | Mega Lucario deck with concise tempo policy. Underperformed Crustle. |
| 006 | 2026-06-17 | `s006-lucario-full-policy.tar.gz` | 600.0 | complete | Mega Lucario deck with fuller public-rule policy. Initial validation completed but did not beat Crustle. |
| 007 | 2026-06-18 | `s007-strongstart-lucario.tar.gz` | 600.0 | complete | Strong Start Crustle-aware Lucario policy with original Lucario deck. Initial score pending upward drift check. |
