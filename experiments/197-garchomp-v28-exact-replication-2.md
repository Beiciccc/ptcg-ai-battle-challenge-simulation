# 197 Garchomp v28 Exact Replication 2

Date: 2026-07-31 UTC

Local generated package (not committed):
`artifacts/submissions/s197-garchomp-v28-exact-replication-2.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 192 and 194

Kaggle submission: `55123892`

Public score: 660.0

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Garchomp v28 entry-fixed archive for a third independent
  public-score observation.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Added a fresh targeted comparison against the two most recent exact public
  archives before submission.

Validation:
- Archive SHA-256 matched experiments 192 and 194 exactly
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- No duplicate members, links, unsafe paths, or nested archive root
- The byte-identical archive retains non-executable AppleDouble and Python
  cache members; the official loader did not select or import them
- Sixteen fresh seat-alternated games completed without errors
- Fresh results: 6-2 against experiment 196 Archaludon and 4-4 against
  experiment 195 Crustle
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55123892` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline to 660.0.
- The three byte-identical observations reached 961.3, 674.6, and 660.0 at
  their recorded checkpoints, confirming substantial public-path variance.
- Score checkpoint: `2026-07-31 01:45 UTC`.
