"""Catalog ingestion for the openai/math collection."""
from __future__ import annotations
import re
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

SUBJECTS = [
 "Number theory", "Algebraic and complex geometry", "Real and complex analysis",
 "Convex and metric geometry", "Theoretical computer science",
 "Dynamical systems and ergodic theory", "Combinatorics", "Algebra",
 "Probability and statistical mechanics", "Mathematical logic", "Group theory",
 "Mathematical physics", "Operator algebras", "Topology", "Functional analysis",
 "Differential geometry", "Partial differential equations",
]

@dataclass
class Manuscript:
    title: str
    path: str

@dataclass
class Family:
    fam_id: str
    title: str
    description: str = ""
    subject: str = "Unknown"
    manuscripts: list[Manuscript] = field(default_factory=list)
    lean_formalized: bool = False
    lean_sources: list[str] = field(default_factory=list)

def clean_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&emsp;", " ").replace("&nbsp;", " ")
    text = re.sub(r"&[a-zA-Z#0-9]+;", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def parse_contents(path: Path, subjects: dict[str, str] | None = None) -> list[Family]:
    text = path.read_text(encoding="utf-8")
    subjects = subjects or {}
    families: list[Family] = []
    # family blocks start with **NNN. title.**
    pattern = re.compile(r"^\*\*(\d{3})\.\s*(.*?)\*\*(.*?)(?=^\*\*\d{3}\.\s|\Z)", re.M | re.S)
    for m in pattern.finditer(text):
        fam_id = m.group(1)
        title = clean_html(m.group(2)).rstrip(".")
        body = m.group(3)
        ms = [Manuscript(clean_html(a), b) for a, b in re.findall(r"\&emsp;\[([^\]]+)\]\(([^)]+)\)", body)]
        # remove manuscript rows from description
        desc_body = re.sub(r"\&emsp;\[[^\]]+\]\([^)]+\)", " ", body)
        desc = clean_html(desc_body)
        fam = Family(fam_id=fam_id, title=title, description=desc, subject=subjects.get(fam_id, "Unknown"), manuscripts=ms)
        families.append(fam)
    return families

def infer_subjects(math_repo: Path) -> dict[str, str]:
    overview = math_repo / "overview.pdf"
    if not overview.exists():
        return {}
    try:
        from pypdf import PdfReader
    except Exception:
        try:
            from PyPDF2 import PdfReader
        except Exception:
            return {}
    try:
        reader = PdfReader(str(overview))
    except Exception:
        return {}
    lines = []
    for page in reader.pages:
        lines.extend((page.extract_text() or "").splitlines())
    mapping: dict[str, str] = {}
    current: str | None = None
    for line in lines:
        s = line.strip()
        if s in SUBJECTS:
            current = s
            continue
        m = re.match(r"^(\d{3})\.\s", s)
        if m and current:
            mapping[m.group(1)] = current
    return mapping

def parse_formalizations(math_repo: Path) -> dict[str, list[str]]:
    yaml_path = math_repo / "lean" / "formalization.yaml"
    if not yaml_path.exists():
        return {}
    lines = yaml_path.read_text(encoding="utf-8").splitlines()
    # tiny parser: track current title and id
    preprint_to_family: dict[str, str] = {}
    # build from contents later; this only returns title->id
    titles: list[str] = []
    sources: list[tuple[str, str]] = []
    i = 0
    current_title = None
    while i < len(lines):
        line = lines[i]
        m = re.search(r'title:\s*"?(.*?)"?\s*$', line)
        if m:
            current_title = m.group(1)
            i += 1
            continue
        m = re.search(r'^\s*id:\s*(.+?)\s*$', line)
        if m and current_title:
            sources.append((current_title, m.group(1).strip().strip('"')))
            current_title = None
        i += 1
    # map preprint dir to family is done by caller; return title->ids here flattened as title list
    return {"_sources": [f"{t}\t{id}" for t, id in sources]}

def map_preprint_to_family(families: list[Family]) -> dict[str, str]:
    out: dict[str, str] = {}
    for fam in families:
        for ms in fam.manuscripts:
            # preprints/<dir>/file
            parts = ms.path.split("/")
            if len(parts) >= 2 and parts[0] == "preprints":
                out[parts[1]] = fam.fam_id
    return out

def apply_formalizations(families: list[Family], math_repo: Path) -> None:
    parsed = parse_formalizations(math_repo)
    raw_sources = parsed.get("_sources", [])
    p2f = map_preprint_to_family(families)
    by_id = {f.fam_id: f for f in families}
    for entry in raw_sources:
        title, src = entry.split("\t", 1)
        parts = src.split("/")
        preprint_dir = None
        for idx, part in enumerate(parts):
            if part == "preprints" and idx + 1 < len(parts):
                preprint_dir = parts[idx + 1]
                break
        if preprint_dir and preprint_dir in p2f:
            fid = p2f[preprint_dir]
            fam = by_id[fid]
            fam.lean_formalized = True
            if src not in fam.lean_sources:
                fam.lean_sources.append(src)

def make_database(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("""CREATE TABLE IF NOT EXISTS families(
        family_id TEXT PRIMARY KEY, number TEXT NOT NULL, title TEXT NOT NULL,
        description TEXT, subject TEXT, manuscript_count INTEGER, lean_formalized INTEGER,
        lean_sources TEXT)""")
    conn.execute("""CREATE TABLE IF NOT EXISTS manuscripts(
        id INTEGER PRIMARY KEY AUTOINCREMENT, family_id TEXT NOT NULL,
        title TEXT NOT NULL, path TEXT NOT NULL,
        FOREIGN KEY(family_id) REFERENCES families(family_id))""")
    conn.execute("DELETE FROM manuscripts")
    conn.execute("DELETE FROM families")
    return conn

def ingest(math_repo: Path, db_path: Path, search_db: Path | None = None) -> int:
    subjects = infer_subjects(math_repo)
    contents = math_repo / "CONTENTS.md"
    families = parse_contents(contents, subjects)
    apply_formalizations(families, math_repo)

    conn = make_database(db_path)
    for fam in families:
        conn.execute(
            "INSERT INTO families VALUES (?,?,?,?,?,?,?,?)",
            (fam.fam_id, fam.fam_id, fam.title, fam.description, fam.subject,
             len(fam.manuscripts), int(fam.lean_formalized), ";".join(fam.lean_sources)),
        )
        for ms in fam.manuscripts:
            conn.execute("INSERT INTO manuscripts(family_id,title,path) VALUES (?,?,?)",
                         (fam.fam_id, ms.title, ms.path))
    conn.commit()
    conn.close()

    if search_db is not None:
        build_search_index(families, search_db)
    return len(families)

def build_search_index(families: Iterable[Family], db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE VIRTUAL TABLE docs USING fts5(family_id, title, body, tokenize='porter unicode61')")
    for fam in families:
        body = " ".join([fam.description] + [m.title + " " + m.path for m in fam.manuscripts])
        conn.execute("INSERT INTO docs VALUES (?,?,?)", (fam.fam_id, fam.title, body))
    conn.commit()
    conn.close()
