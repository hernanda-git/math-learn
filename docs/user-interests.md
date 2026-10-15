# User interest profile

This repository is being used as a learning system for the `openai/math` collection.

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

## Agent guidance

When selecting families automatically, prefer unresolved (`Lean = -`) families from the buckets above unless the user explicitly prioritizes formalized material. Pair extraction with critic and Lean-verifier before marking understanding.
