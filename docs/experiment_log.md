# Experiment Log

| ID | Date | Package | Public score | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 000 | 2026-06-17 | `baseline.zip` | n/a | prepared | Deterministic starter policy and sample deck; not submitted yet. |
| 001 | 2026-06-17 | `s001-generic-abomasnow.tar.gz` | n/a | error | Generic heuristic with sample deck. Validation episode failed because the loader bound to the last helper function instead of `agent()`. Entrypoint check added. |
| 002 | 2026-06-17 | `s002-generic-abomasnow-entryfix.tar.gz` | 600.0 | complete | Same generic heuristic and sample deck after entrypoint fix. Validated successfully but weak public rating. |
| 003 | 2026-06-17 | `s003-crustle-wall.tar.gz` | 600.0 | complete | Crustle wall deck with generic heuristic plus light healing/tool rules. Score did not improve, suggesting deck-specific sequencing is needed. |
| 004 | 2026-06-17 | `s004-crustle-specific.tar.gz` | 600.0 | complete | Crustle wall deck with deck-specific sequencing. Initial score stayed weak, so next experiment moves to Lucario. |
| 005 | 2026-06-17 | `s005-lucario-tempo.tar.gz` | 600.0 | complete | Mega Lucario deck with concise tempo policy. Initial score stayed weak; final slot will test fuller Lucario logic. |
