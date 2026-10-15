# math-learn

Agentic study system for the `openai/math` manuscript collection.

This repository does **not** duplicate the ~800MB / 133k-file math collection. It points to it (`MATH_REPO`, default `../math`), indexes it locally, and runs a tiered subagent pipeline for faster learning: catalog curation, theorem extraction, critic, Lean verification, tutoring, and spaced-repetition generation.

## Quick start

```bash
cd C:/Workspace/math-learn
python -m pip install -e .
mathlearn ingest --math-repo C:/Workspace/math
mathlearn stats
mathlearn search "quasi Riemann hypothesis"
mathlearn study 003
```

## What you get

- SQLite FTS search over 719 manuscript abstracts.
- Study packs with theorem statements, dependencies, Lean status, and quiz prompts.
- Pluggable vector-search backend (BM25 default; optional sentence-transformers + numpy).
- Subagent contracts and reusable skills under `agents/` and `skills/`.
- Dataset registry and sparse-checkout helpers for the large source repo.

## Safety

All AI-generated summaries are hypotheses until checked against source. The critic and Lean-verification agents must run before a result is marked "understood."
