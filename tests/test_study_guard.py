from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from mathlearn.cli import main

REPO_ROOT = Path(__file__).resolve().parents[1]
FAMILIES_DB = REPO_ROOT / "data" / "processed" / "families.sqlite"


def _write_config(tmp_path: Path) -> Path:
    cfg = {
        "math_repo": "../math",
        "indexes": {
            "families": str(FAMILIES_DB),
            "fts": str(REPO_ROOT / "data" / "processed" / "search.sqlite"),
        },
        "study_output_dir": str(tmp_path / "packs"),
    }
    p = tmp_path / "config.json"
    p.write_text(json.dumps(cfg), encoding="utf-8")
    return p


def test_study_refuses_to_overwrite_checked_pack(tmp_path):
    if not FAMILIES_DB.exists():
        return
    cfg = _write_config(tmp_path)
    out = tmp_path / "packs" / "family-003.md"
    out.parent.mkdir(parents=True)
    checked = "# Family 003: checked pack\n\n## Theorem statement\n\ntruth.\n"
    out.write_text(checked, encoding="utf-8")

    rc = main(["--config", str(cfg), "study", "003"])

    assert rc == 1
    assert out.read_text(encoding="utf-8") == checked


def test_study_writes_stub_and_force_overwrites_checked_pack(tmp_path):
    if not FAMILIES_DB.exists():
        return
    cfg = _write_config(tmp_path)
    out = tmp_path / "packs" / "family-003.md"

    # No file yet: stub is written.
    assert main(["--config", str(cfg), "study", "003"]) == 0
    assert "## To learn (agent pipeline)" in out.read_text(encoding="utf-8")

    # Checked pack present: --force regenerates the stub.
    out.write_text("# checked\n", encoding="utf-8")
    assert main(["--config", str(cfg), "study", "003", "--force"]) == 0
    assert "## To learn (agent pipeline)" in out.read_text(encoding="utf-8")
