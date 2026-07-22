#!/usr/bin/env python
from __future__ import annotations

import argparse
import csv
from hashlib import sha256
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import tempfile
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "agent_zoo" / "manifest.json"
DEFAULT_OUTPUT = ROOT / "artifacts" / "agent_zoo"
SOURCE_PREFIX = PurePosixPath("agent_zoo/sources")
ALLOWED_SOURCE_SUFFIXES = {".py", ".csv"}

CSV_FIELDS = (
    "experiment",
    "slug",
    "title",
    "source_id",
    "source_commit",
    "experiment_commit",
    "kaggle_submission",
    "public_score",
    "status",
    "reproducibility",
    "main_sha256",
    "deck_sha256",
    "archive_sha256",
    "local_generated_package",
    "upstream_notebook_urls",
    "upstream_version_pinned",
)

BUNDLE_README = """# PTCG Source-only Agent Zoo

This package contains one source directory per recorded experiment. Repeated
experiments may intentionally contain identical source bytes.

Each agent directory includes `main.py`, `deck.csv`, any allowlisted Python
helper source, and `metadata.json`. File hashes and provenance are recorded in
the top-level manifests and `SHA256SUMS`.

This is not a collection of runnable Kaggle submission archives. The package
does not contain the competition runtime (`cg/`), engine binaries, model data,
or replay data. Obtain the public runtime from Kaggle after accepting the
competition rules. Experiments whose metadata names an excluded model remain
non-runnable until that dependency is supplied separately under its own terms.
"""


def load_manifest(path: Path = DEFAULT_MANIFEST) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError(f"unsupported manifest schema: {data.get('schema_version')!r}")
    experiments = data.get("experiments")
    if not isinstance(experiments, list) or not experiments:
        raise ValueError("manifest has no experiments")
    return data


def select_experiments(
    manifest: dict[str, Any],
    requested: Iterable[str] | None,
) -> list[dict[str, Any]]:
    entries = manifest["experiments"]
    if requested is None:
        return list(entries)

    wanted = {str(item).removeprefix("s").zfill(3) for item in requested}
    selected = [entry for entry in entries if entry["experiment"] in wanted]
    found = {entry["experiment"] for entry in selected}
    missing = sorted(wanted - found)
    if missing:
        raise ValueError(f"unknown experiment(s): {', '.join(missing)}")
    return selected


def _safe_source_file(entry: dict[str, Any], item: dict[str, Any]) -> tuple[PurePosixPath, PurePosixPath]:
    git_path = PurePosixPath(item["git_path"])
    output_name = PurePosixPath(item["name"])
    expected_parent = SOURCE_PREFIX / entry["source_id"]

    if git_path.is_absolute() or ".." in git_path.parts or git_path.parent != expected_parent / output_name.parent:
        raise ValueError(f"unsafe source path: {git_path}")
    if output_name.is_absolute() or ".." in output_name.parts:
        raise ValueError(f"unsafe output path: {output_name}")
    if output_name.suffix not in ALLOWED_SOURCE_SUFFIXES:
        raise ValueError(f"source allowlist rejected: {output_name}")
    if output_name.suffix == ".csv" and output_name.name != "deck.csv":
        raise ValueError(f"only deck.csv is allowed: {output_name}")
    return git_path, output_name


def _git_show(commit: str, path: PurePosixPath) -> bytes:
    if len(commit) != 40 or any(char not in "0123456789abcdef" for char in commit):
        raise ValueError(f"invalid source commit: {commit!r}")
    result = subprocess.run(
        ["git", "show", f"{commit}:{path.as_posix()}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"cannot read {path} at {commit}: {detail}")
    return result.stdout


def _write_csv(path: Path, entries: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        for entry in entries:
            row = {field: entry.get(field) for field in CSV_FIELDS}
            row["upstream_notebook_urls"] = " ".join(entry["upstream_notebook_urls"])
            pinned = row["upstream_version_pinned"]
            row["upstream_version_pinned"] = "" if pinned is None else str(pinned).lower()
            writer.writerow({key: "" if value is None else value for key, value in row.items()})


def _write_checksums(root: Path) -> None:
    lines = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        if path.name == "SHA256SUMS":
            continue
        digest = sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {path.relative_to(root).as_posix()}")
    (root / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _replace_existing_output(output: Path) -> None:
    manifest_path = output / "manifest.json"
    if not manifest_path.is_file():
        raise ValueError(f"refusing to replace unrecognized directory: {output}")
    existing = json.loads(manifest_path.read_text(encoding="utf-8"))
    if existing.get("bundle_type") != "ptcg_source_only_agent_zoo":
        raise ValueError(f"refusing to replace unrecognized directory: {output}")
    shutil.rmtree(output)


def materialize(
    manifest: dict[str, Any],
    entries: list[dict[str, Any]],
    output: Path,
    *,
    force: bool = False,
) -> Path:
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        if not force:
            raise FileExistsError(f"output exists; pass --force to replace it: {output}")
        _replace_existing_output(output)

    staging = Path(tempfile.mkdtemp(prefix=f".{output.name}-", dir=output.parent))
    source_cache: dict[tuple[str, str], bytes] = {}
    try:
        agents_root = staging / "agents"
        agents_root.mkdir()
        for entry in entries:
            agent_root = agents_root / f"s{entry['experiment']}-{entry['slug']}"
            agent_root.mkdir()
            for item in entry["source_files"]:
                git_path, output_name = _safe_source_file(entry, item)
                cache_key = (entry["source_commit"], git_path.as_posix())
                data = source_cache.get(cache_key)
                if data is None:
                    data = _git_show(entry["source_commit"], git_path)
                    source_cache[cache_key] = data
                digest = sha256(data).hexdigest()
                if digest != item["sha256"] or len(data) != item["bytes"]:
                    raise ValueError(f"source verification failed: {git_path}")
                destination = agent_root / Path(output_name.as_posix())
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(data)

            metadata = dict(entry)
            metadata["materialized_from_git"] = True
            (agent_root / "metadata.json").write_text(
                json.dumps(metadata, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )

        bundle = {key: value for key, value in manifest.items() if key != "experiments"}
        bundle["bundle_type"] = "ptcg_source_only_agent_zoo"
        bundle["experiments"] = entries
        (staging / "manifest.json").write_text(
            json.dumps(bundle, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        _write_csv(staging / "manifest.csv", entries)
        (staging / "README.md").write_text(BUNDLE_README, encoding="utf-8")
        shutil.copyfile(ROOT / "agent_zoo" / "THIRD_PARTY_NOTICES.md", staging / "THIRD_PARTY_NOTICES.md")
        licenses = staging / "LICENSES"
        licenses.mkdir()
        shutil.copyfile(
            ROOT / "agent_zoo" / "LICENSES" / "Apache-2.0.txt",
            licenses / "Apache-2.0.txt",
        )
        _write_checksums(staging)
        os.replace(staging, output)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize source-only agents from Git history.")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--all", action="store_true", help="Materialize every recorded experiment.")
    selection.add_argument(
        "--experiment",
        action="append",
        metavar="ID",
        help="Materialize one experiment; repeat for multiple IDs.",
    )
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--force", action="store_true", help="Replace a prior materialized Agent Zoo.")
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    entries = select_experiments(manifest, None if args.all else args.experiment)
    output = materialize(manifest, entries, args.output, force=args.force)
    print(f"materialized {len(entries)} experiment(s) at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
