# Submission Notes

Submission packages are built from `submission/`:

```bash
python tools/download_assets.py --light
python tools/check_deck.py submission/deck.csv
python tools/check_submission_entrypoint.py
python tools/package_submission.py --name baseline
```

The package tarball is written to `artifacts/submissions/`. Before uploading,
check that the archive contains `main.py`, `deck.csv`, and the `cg/` support
files.

Submit a package with:

```bash
python tools/submit_package.py artifacts/submissions/baseline.tar.gz --message "baseline"
```

Use `tools/list_recent_submissions.py` to review recent Kaggle submission rows.

For this simulation format, keep the required submission entrypoint as the last
top-level binding in `submission/main.py`, and give it a fresh global name that
has not been bound earlier in the file. Kaggle selects the last callable in the
executed module's global insertion order. Redefining an earlier function name
does not move that key to the end and can bind the loader to a helper instead.

Run `tools/check_submission_entrypoint.py` on the exact packaged `main.py`
before submission.
