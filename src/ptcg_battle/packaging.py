from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import tarfile
from zipfile import ZIP_DEFLATED, ZipFile


@dataclass(frozen=True)
class SubmissionPackage:
    path: Path
    file_count: int
    has_support_files: bool


EXCLUDED_DIRS = {"__pycache__", ".pytest_cache"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def validate_submission_dir(source_dir: str | Path, require_support_files: bool = True) -> list[str]:
    source = Path(source_dir)
    problems: list[str] = []
    for filename in ("main.py", "deck.csv"):
        if not (source / filename).exists():
            problems.append(f"Missing required submission file: {filename}")

    support_file = source / "cg" / "api.py"
    if require_support_files and not support_file.exists():
        problems.append("Missing support files under submission/cg/. Run tools/download_assets.py --light.")
    return problems


def build_submission_zip(
    source_dir: str | Path,
    output_zip: str | Path,
    require_support_files: bool = True,
) -> SubmissionPackage:
    source = Path(source_dir)
    output = Path(output_zip)

    problems = validate_submission_dir(source, require_support_files=require_support_files)
    if problems:
        raise ValueError("\n".join(problems))

    output.parent.mkdir(parents=True, exist_ok=True)
    files = list(_iter_submission_files(source))
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for file_path in files:
            archive.write(file_path, file_path.relative_to(source).as_posix())

    return SubmissionPackage(
        path=output,
        file_count=len(files),
        has_support_files=(source / "cg" / "api.py").exists(),
    )


def build_submission_tar_gz(
    source_dir: str | Path,
    output_tar_gz: str | Path,
    require_support_files: bool = True,
) -> SubmissionPackage:
    source = Path(source_dir)
    output = Path(output_tar_gz)

    problems = validate_submission_dir(source, require_support_files=require_support_files)
    if problems:
        raise ValueError("\n".join(problems))

    output.parent.mkdir(parents=True, exist_ok=True)
    files = list(_iter_submission_files(source))
    with tarfile.open(output, "w:gz") as archive:
        for file_path in files:
            archive.add(file_path, file_path.relative_to(source).as_posix())

    return SubmissionPackage(
        path=output,
        file_count=len(files),
        has_support_files=(source / "cg" / "api.py").exists(),
    )


def _iter_submission_files(source: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(source.rglob("*")):
        if path.is_dir():
            continue
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        if path.suffix in EXCLUDED_SUFFIXES:
            continue
        if path.name == ".DS_Store":
            continue
        if path.name.startswith("._") or path.name.startswith(".__"):
            continue
        files.append(path)
    return files
