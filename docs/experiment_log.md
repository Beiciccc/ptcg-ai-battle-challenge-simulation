# Experiment Log

| ID | Date | Package | Public score | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 000 | 2026-06-17 | `baseline.zip` | n/a | prepared | Deterministic starter policy and sample deck; not submitted yet. |
| 001 | 2026-06-17 | `s001-generic-abomasnow.tar.gz` | n/a | error | Generic heuristic with sample deck. Validation episode failed because the loader bound to the last helper function instead of `agent()`. Entrypoint check added. |
| 002 | 2026-06-17 | `s002-generic-abomasnow-entryfix.tar.gz` | 600.0 | complete | Same generic heuristic and sample deck after entrypoint fix. Validated successfully but weak public rating. |
