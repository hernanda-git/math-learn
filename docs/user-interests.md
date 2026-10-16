# User interest profile

This repository is being used as a learning system for the `openai/math` collection.

Companion documents: `physics-inventory.md` (laws & formulas, landmark papers, the full physics family slice, verified declassified/official archives, and legends-vs-documents) and `family-list.md` (all 372 families).

## Primary interests

The user wants to deep dive and eventually solve problems across:

- energy
- fusion
- gravity
- electromagnetism and Coulomb physics
- thermodynamics
- negative energy and backreaction
- zero-point energy and vacuum effects
- space and time / spacetime
- quantum matter and quantum computation

## What "deep dive" means here

For each selected family, the goal is:

1. extract the exact theorem statement and assumptions;
2. identify the main construction or proof idea;
3. separate verified claims from inference;
4. record Lean/formalization status;
5. produce a study pack, quiz, and critic verdict;
6. only mark understanding after source-level and, when possible, Lean verification.

## Suggested starting buckets
### Negative energy, zero-point energy, and vacuum effects

No family is literally about negative-energy engines or zero-point energy devices. The nearest mathematical entries are quantum field, Coulomb, matrix-model, and conformal-net results:

- `263` Ionization and generalized ionization conjectures
- `267` Positive-temperature Bose–Einstein condensation
- `270` BFSS threshold and positive-energy bound states
- `273` Entropy photon-number inequality
- `275` QMA-hardness of continuum Coulomb energy
- `278` Failure of Kohn–Sham ensemble representation
- `280` Unitary vertex operator algebras and conformal nets
- `282` From scale symmetry to local conformal symmetry in four-dimensional QFT

These are mathematical building blocks, not device-physics proofs.


### Gravity and space-time

- `260` Spacetime Penrose inequalities
- `264` Strong cosmic censorship near two-ended Kerr data
- `280` Unitary vertex operator algebras and conformal nets
- `282` From scale symmetry to local conformal symmetry in four-dimensional QFT
- `284` Optimal quartic separation between randomized and quantum queries

### Energy, thermodynamics, and quantum matter

- `263` Ionization and generalized ionization conjectures
- `267` Positive-temperature Bose–Einstein condensation
- `268` Spin-one Haldane gap
- `269` Uniform Laughlin gap
- `270` BFSS threshold and positive-energy bound states
- `271` Bloch magnetization law
- `273` Entropy photon-number inequality
- `275` QMA-hardness of continuum Coulomb energy
- `278` Failure of Kohn–Sham ensemble representation
- `281` QAOA and the SK optimum

### Electromagnetism / Coulomb-related mathematics

- `263` Ionization thresholds
- `275` Coulomb energy complexity
- `278` Kohn–Sham density representation
- `276` Generalized amplitude-damping capacity (quantum noise/energy exchange, not classical EM)

### Fusion

No family is literally about fusion reactor physics. The nearest mathematical physics entries are quantum many-body, Coulomb, matrix-model, and condensed-matter results. Treat fusion as a user research target to map onto those families, not as an existing paper category in this catalog.

## Coverage tracker

Updated 2026-10-16. A family is **covered** when a critic-verified study pack exists at `data/processed/study-packs/family-NNN.md` (pipeline: extract → critic → lean-verify → tutor → quiz).

| Field | Nearest families | Covered | Queued |
|---|---|---|---|
| Negative energy / zero-point / vacuum effects | 263, 267, 270, 273, 275, 278, 280, 282 | **270** | 263, 267, 273, 275, 278, 280, 282 |
| Gravity and space-time | 260, 264, 280, 282, 284 | — | 260, 264, 280, 282, 284 |
| Energy, thermodynamics, and quantum matter | 263, 267, 268, 269, 270, 271, 273, 275, 278, 281 | **270** | 263, 267, 268, 269, 271, 273, 275, 278, 281 |
| Electromagnetism / Coulomb-related mathematics | 263, 275, 278, 276 | — | 263, 275, 278, 276 |
| Fusion | no literal family; maps onto the Coulomb / many-body entries above | — | research target |

Produced outside the interest buckets: `001` Milne's rationality conjecture (starter family) — pack at `data/processed/study-packs/family-001.md`.

Notes on 270 (the first covered family):

- Pack covers: undeformed relative SU(N) BFSS has exactly one normalizable zero-energy state for every finite $N \ge 2$ (Witten's threshold-bound-state conjecture), and the relative SU(2) Hamiltonian has infinitely many positive eigenvalues $E_j \to \infty$.
- Lean audit: an uncatalogued, `sorry`-free 74-file development exists at `lean/OAI/MathematicalPhysics/BFSS/` (imported at `OAI.lean:702`); not typechecked (no toolchain installed). The audited flag was written to `data/processed/families.sqlite` (`lean_formalized = 1` for 270).
- `docs/family-list.md` stays the raw catalog export — it lists 270 as `Lean = -`, which reflects `formalization.yaml`, not the in-tree development.

## Agent guidance

When selecting families automatically, prefer unresolved (`Lean = -`) families from the buckets above unless the user explicitly prioritizes formalized material; skip families already marked covered in the Coverage tracker. Pair extraction with critic and Lean-verifier before marking understanding.
