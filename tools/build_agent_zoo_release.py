#!/usr/bin/env python
from __future__ import annotations

import argparse
from gzip import GzipFile
from hashlib import sha256
from io import BytesIO
from pathlib import Path
import re
import shutil
import tarfile
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from materialize_agents import DEFAULT_MANIFEST, ROOT, load_manifest, materialize, select_experiments


DEFAULT_NAME = "ptcg-agent-zoo-source-only-v1.0.0"
DEFAULT_OUTPUT = ROOT / "artifacts" / "releases"


def _files(root: Path) -> list[Path]:
    files = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"release boundary rejects links: {path}")
        if path.is_file():
            files.append(path)
    return files


def build_tar_gz(source: Path, output: Path, archive_root: str) -> None:
    with output.open("wb") as raw:
        with GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode="w", format=tarfile.PAX_FORMAT) as archive:
                for path in _files(source):
                    data = path.read_bytes()
                    relative = path.relative_to(source).as_posix()
                    info = tarfile.TarInfo(f"{archive_root}/{relative}")
                    info.size = len(data)
                    info.mode = 0o644
                    info.mtime = 0
                    info.uid = 0
                    info.gid = 0
                    info.uname = ""
                    info.gname = ""
                    archive.addfile(info, BytesIO(data))


def build_zip(source: Path, output: Path, archive_root: str) -> None:
    with ZipFile(output, "w") as archive:
        for path in _files(source):
            relative = path.relative_to(source).as_posix()
            info = ZipInfo(f"{archive_root}/{relative}", date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())


def build_release(manifest_path: Path, output: Path, name: str) -> list[Path]:
    if not re.fullmatch(r"[A-Za-z0-9._-]+", name):
        raise ValueError(f"unsafe release name: {name!r}")
    output.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(manifest_path)
    entries = select_experiments(manifest, None)

    with tempfile.TemporaryDirectory(prefix="ptcg-agent-zoo-") as temp_dir:
        source = Path(temp_dir) / name
        materialize(manifest, entries, source)
        tar_path = output / f"{name}.tar.gz"
        zip_path = output / f"{name}.zip"
        build_tar_gz(source, tar_path, name)
        build_zip(source, zip_path, name)
        manifest_json = output / f"{name}.manifest.json"
        manifest_csv = output / f"{name}.manifest.csv"
        shutil.copyfile(source / "manifest.json", manifest_json)
        shutil.copyfile(source / "manifest.csv", manifest_csv)

    assets = [tar_path, zip_path, manifest_json, manifest_csv]
    sums = output / "SHA256SUMS"
    sums.write_text(
        "".join(f"{sha256(path.read_bytes()).hexdigest()}  {path.name}\n" for path in assets),
        encoding="utf-8",
    )
    return [*assets, sums]


def main() -> int:
    parser = argparse.ArgumentParser(description="Build deterministic source-only Agent Zoo assets.")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--name", default=DEFAULT_NAME)
    args = parser.parse_args()

    assets = build_release(args.manifest, args.output, args.name)
    for path in assets:
        print(f"{sha256(path.read_bytes()).hexdigest()}  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
