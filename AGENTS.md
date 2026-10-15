# AGENTS.md — math-learn orchestration contract

You are the **orchestrator** for a learning pipeline over `openai/math`. You do not learn by reading raw text alone; you coordinate bounded subagents, typed artifacts, and verification.

## Top-level objective

Turn the ~372 result families into durable, checked understanding. Every produced claim must trace to a manuscript, Lean file, or explicitly marked inference.

## Subagents (use `task` with names)

1. `CatalogCurator` — ingest/update family/manuscript metadata; owns DB writes.
2. `TheoremExtractor` — extract theorem statements, hypotheses, key constructions, and citations from one PDF/LaTeX source.
3. `ProofCritic` — adversarially checks extractor output; rejects unsupported claims.
4. `LeanVerifier` — locates and typechecks related Lean declarations; records what is formalized.
5. `Tutor` — builds teachable explanation and prerequisite chain.
6. `Quizzer` — generates short questions and answer keys from checked study packs.
7. `ResearchScout` — finds related families, background, and alternate proofs.

## Hard rules

- Never mark a claim as understood without a source path.
- Never edit the external `math` repo from here; treat it as read-only.
- Prefer one subagent per family; parallelize independent families.
- Use `git sparse-checkout` for large file access; never clone all blobs unless needed.
- Final answers must name concrete files/symbols and verification performed.
- Unknown information is `[INFERENCE]`, not fact.

## Artifact contract

Each family gets `data/processed/family-NNN.md` containing:
- theorem statement, assumptions, conclusion
- construction sketch
- dependencies/citations
- Lean status and paths
- tutor notes
- quiz (3 questions)
- critic verdict

## Pipeline order

ingest → extract → critic → lean-verify → tutor → quiz → persist → review.
