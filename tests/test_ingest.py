from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from mathlearn.catalog import parse_contents, infer_subjects

def test_parse_contents():
    repo = Path("C:/Workspace/math")
    if not (repo / "CONTENTS.md").exists():
        return
    subs = infer_subjects(repo)
    fams = parse_contents(repo / "CONTENTS.md", subs)
    assert len(fams) == 372
    assert sum(len(f.manuscripts) for f in fams) == 719
