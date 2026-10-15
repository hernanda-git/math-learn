"""Generate a study pack for one or more families."""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from mathlearn.cli import main
if __name__ == "__main__":
    fams = sys.argv[1:] or ["003"]
    for f in fams:
        main(["study", f])
