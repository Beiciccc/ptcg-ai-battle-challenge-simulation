from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tarfile
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from build_agent_zoo_release import DEFAULT_NAME, build_release
from materialize_agents import load_manifest, materialize, select_experiments


MANIFEST = ROOT / "agent_zoo" / "manifest.json"
FORBIDDEN_SUFFIXES = {".dll", ".dylib", ".onnx", ".pt", ".pth", ".so"}


def _git_show(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def test_manifest_covers_v1_experiments_and_verifies_source() -> None:
    manifest = load_manifest(MANIFEST)
    entries = manifest["experiments"]
    assert [entry["experiment"] for entry in entries] == [f"{index:03d}" for index in range(162)]
    assert len({entry["source_id"] for entry in entries}) == 38
    by_id = {entry["experiment"]: entry for entry in entries}
    assert by_id["084"]["required_unpublished_dependencies"] == []
    assert by_id["133"]["required_unpublished_dependencies"] == ["pilot_factory_model.json"]
    assert by_id["147"]["required_unpublished_dependencies"] == ["model.pt"]

    documents = {path.as_posix() for path in ROOT.glob("experiments/*.md")}
    assert {str(ROOT / entry["experiment_doc"]) for entry in entries} <= documents

    cache: dict[tuple[str, str], bytes] = {}
    for entry in entries:
        assert entry["source_commit"] == manifest["source_commit"]
        assert len(entry["source_commit"]) == 40
        assert entry["package_downloadable"] is False
        assert entry["kaggle_ref"] == entry["kaggle_submission"]
        assert len(entry["archive_sha256"]) == 64
        assert {item["name"] for item in entry["source_files"]} >= {"main.py", "deck.csv"}

        document = (ROOT / entry["experiment_doc"]).read_text(encoding="utf-8")
        assert "Local generated package (not committed):" in document
        assert f"Source commit: [{entry['source_commit'][:7]}]" in document
        assert "Reproducibility:" in document
        assert entry["main_sha256"] in document
        assert entry["deck_sha256"] in document

        for item in entry["source_files"]:
            key = (entry["source_commit"], item["git_path"])
            if key not in cache:
                cache[key] = _git_show(*key)
            data = cache[key]
            assert len(data) == item["bytes"]
            assert sha256(data).hexdigest() == item["sha256"]


def test_materialize_all_has_only_source_allowlist(tmp_path: Path) -> None:
    manifest = load_manifest(MANIFEST)
    entries = select_experiments(manifest, None)
    output = materialize(manifest, entries, tmp_path / "zoo")

    agents = sorted((output / "agents").iterdir())
    assert len(agents) == 162
    for agent in agents:
        assert (agent / "main.py").is_file()
        assert (agent / "deck.csv").is_file()
        assert (agent / "metadata.json").is_file()

    for path in output.rglob("*"):
        assert not path.is_symlink()
        if not path.is_file():
            continue
        relative = PurePosixPath(path.relative_to(output).as_posix())
        assert "cg" not in relative.parts
        assert path.suffix.lower() not in FORBIDDEN_SUFFIXES
        assert not path.name.startswith(("._", ".__"))

    sums = (output / "SHA256SUMS").read_text(encoding="utf-8").splitlines()
    assert sums
    for line in sums:
        digest, relative = line.split("  ", 1)
        assert sha256((output / relative).read_bytes()).hexdigest() == digest


def test_release_archives_are_deterministic_and_source_only(tmp_path: Path) -> None:
    first = build_release(MANIFEST, tmp_path / "first", DEFAULT_NAME)
    second = build_release(MANIFEST, tmp_path / "second", DEFAULT_NAME)
    assert [sha256(path.read_bytes()).hexdigest() for path in first] == [
        sha256(path.read_bytes()).hexdigest() for path in second
    ]

    tar_path = next(path for path in first if path.name.endswith(".tar.gz"))
    with tarfile.open(tar_path, "r:gz") as archive:
        members = archive.getmembers()
        assert members
        assert all(member.isfile() and not member.issym() and not member.islnk() for member in members)
        names = [PurePosixPath(member.name) for member in members]
        assert any(path.name == "main.py" for path in names)
        assert any(path.name == "deck.csv" for path in names)
        assert all("cg" not in path.parts for path in names)
        assert all(path.suffix.lower() not in FORBIDDEN_SUFFIXES for path in names)

    zip_path = next(path for path in first if path.suffix == ".zip")
    with ZipFile(zip_path) as archive:
        names = [PurePosixPath(name) for name in archive.namelist()]
        assert all(".." not in path.parts and not path.is_absolute() for path in names)
        assert all("cg" not in path.parts for path in names)
        assert all(path.suffix.lower() not in FORBIDDEN_SUFFIXES for path in names)


def test_readme_states_archive_boundary() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    normalized = " ".join(readme.split())
    assert "not currently downloadable" in readme
    assert "python tools/materialize_agents.py --all" in readme
    assert "Full submission archives will only be published" in normalized
