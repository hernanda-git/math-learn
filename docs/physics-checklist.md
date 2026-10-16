# Physics checklist — master list

One itemized checklist of everything mapped to the interest profile: laws & formulas, landmark papers, `openai/math` families, verified declassified/FOIA/official documents, and legend resolutions. Details, links and archive IDs: `physics-inventory.md`. Family descriptions: `family-list.md`. Coverage tracker: `user-interests.md`. Status as of 2026-10-16 — `[x]` = resolved/covered, `[ ]` = open.

## A. Laws & formulas

### Energy
- [ ] Conservation of energy (`dE/dt = 0`; Noether: time-translation symmetry)
- [ ] Work–energy theorem (`W = ΔKE`)
- [ ] Mass–energy equivalence (`E = mc²`)
- [ ] Planck–Einstein relation (`E = hν`)
- [ ] Schrödinger equation (`iℏ ∂ψ/∂t = Ĥψ`)
- [ ] Zero-point of a mode (`E₀ = ½ℏω`)

### Fusion
- [ ] Coulomb barrier (`V = q₁q₂/4πε₀r`)
- [ ] Gamow tunneling factor (rate `⟨σv⟩`, Gamow window)
- [ ] Mass defect / Q-value (D + T → ⁴He + n = 17.6 MeV)
- [ ] Lawson criterion (`nTτ_E ≳ 3×10²¹ keV·s/m³`)
- [ ] Debye screening (`λ_D = √(ε₀k_BT/ne²)`)

### Gravity
- [ ] Newton's law (`F = Gm₁m₂/r²`)
- [ ] Einstein field equations (`G_μν + Λg_μν = (8πG/c⁴)T_μν`)
- [ ] Geodesic equation
- [ ] Schwarzschild radius + Kerr frame dragging
- [ ] Hawking temperature & Bekenstein–Hawking entropy
- [ ] Penrose inequality (`M ≥ √(A/16π)`)
- [ ] Gravitational-wave strain (quadrupole; LIGO `~10⁻²¹`)

### Electromagnetism / Coulomb
- [ ] Coulomb's law
- [ ] Maxwell's equations (Gauss, `∇·B = 0`, Faraday, Ampère–Maxwell)
- [ ] Lorentz force (`F = q(E + v×B)`)
- [ ] Poynting flux + field energy density
- [ ] Larmor radiation formula
- [ ] Fine-structure constant (`α ≈ 1/137.036`)

### Thermodynamics
- [ ] Zeroth law
- [ ] First law (`ΔU = Q − W`)
- [ ] Second law (`ΔS ≥ 0`)
- [ ] Third law (`S → 0` as `T → 0`)
- [ ] Boltzmann entropy (`S = k_B lnΩ`)
- [ ] Free energies (`F = U − TS`, `G = H − TS`) + Maxwell relations
- [ ] Carnot efficiency (`η = 1 − T_c/T_h`)
- [ ] Jarzynski equality (`⟨e^{−βW}⟩ = e^{−βΔF}`)
- [ ] Landauer bound (`k_BT ln2` per erased bit)

### Negative energy & backreaction
- [ ] Classical energy conditions
- [ ] Ford–Roman quantum inequalities
- [ ] Hawking negative-energy flux
- [ ] Alcubierre warp requirement + Pfenning–Ford no-go

### Zero-point energy & vacuum
- [ ] Harmonic zero-point (`E_n = (n+½)ℏω`)
- [ ] Casimir force (`F/A = π²ℏc/240d⁴`)
- [ ] Lamb shift (`≈1057.8 MHz`)
- [ ] Schwinger limit (`1.32×10¹⁸ V/m`)
- [ ] `ρ_Λ ≈ 6×10⁻¹⁰ J/m³` vs ~10¹²⁰ QFT gap
- [ ] Jaffe caveat (Casimir ≠ extractable vacuum energy)

### Space and time
- [ ] Minkowski interval + Lorentz factor
- [ ] Time dilation / length contraction / Doppler
- [ ] Equivalence principle + gravitational redshift
- [ ] GPS net correction (`+38 μs/day`)
- [ ] Friedmann equations
- [ ] Penrose singularity theorem / cosmic censorship

### Quantum matter
- [ ] Uncertainty principle (`ΔxΔp ≥ ℏ/2`)
- [ ] Pauli exclusion + Fermi/Bose statistics + BEC `T_c`
- [ ] Heisenberg model + Bloch `T^{3/2}` law
- [ ] Haldane gap (`Δ ≈ 0.41J` for S=1)
- [ ] Quantum Hall (`σ_xy = νe²/h`) + Laughlin ν=1/3
- [ ] Kohn–Sham DFT equations
- [ ] Lieb–Thirring inequalities

### Quantum computation
- [ ] Qubit + gate unitaries + no-cloning
- [ ] CHSH (`|S| ≤ 2` classical vs `2√2` quantum)
- [ ] Shor & Grover algorithms
- [ ] BQP / QMA complexity
- [ ] Channel capacity + quantum error correction

## B. Landmark papers

- [ ] Maxwell, *A Dynamical Theory of the Electromagnetic Field* (1865)
- [ ] Hertz, electric-wave experiments (1887)
- [ ] Lorentz, electron theory (1895 → 1904)
- [ ] Planck, quantum hypothesis (1900)
- [ ] Einstein, special relativity (1905)
- [ ] Einstein, photoelectric effect (1905)
- [ ] Bohr, atomic model (1913)
- [ ] Einstein, general relativity field equations (1915)
- [ ] Schwarzschild solution (1916)
- [ ] Heisenberg, matrix mechanics (1925)
- [ ] Schrödinger, wave equation (1926)
- [ ] Dirac, relativistic electron (1928)
- [ ] Carnot (1824) · Clausius (1850/65) · Boltzmann (1877) · Gibbs (1902)
- [ ] Onsager reciprocity (1931)
- [ ] Bloch, ferromagnetism theory (1930)
- [ ] Lamb–Retherford, 2S–2P shift (1947)
- [ ] Casimir, plates attraction (1948)
- [ ] Feynman / Schwinger / Tomonaga, QED (1948)
- [ ] BCS theory (1957)
- [ ] Anderson, absence of diffusion (1958)
- [ ] Sparnaay, first Casimir attempt (1958)
- [ ] Landauer, erasure cost (1961)
- [ ] Bell inequality (1964)
- [ ] Penrose, singularity theorem (1965)
- [ ] Hawking, black-hole radiation (1974/75)
- [ ] von Klitzing, quantum Hall (1980)
- [ ] Aspect et al., Bell test (1982)
- [ ] Feynman, simulating physics with computers (1982)
- [ ] Haldane, large-spin chains (1983)
- [ ] Laughlin, fractional QH wavefunction (1983)
- [ ] BB84 quantum key distribution (1984)
- [ ] Shor, factoring algorithm (1994)
- [ ] Alcubierre, warp drive metric (1994)
- [ ] Ford–Roman quantum inequalities (1995)
- [ ] Grover, search algorithm (1996)
- [ ] Lamoreaux, Casimir measurement (1997)
- [ ] Jarzynski equality (1997)
- [ ] Pfenning–Ford, warp-drive no-go (1997)
- [ ] Mohideen–Roy, precision Casimir (1998)
- [ ] Jaffe, Casimir ≠ vacuum energy (2005)
- [ ] Gravity Probe B final results (2011)
- [ ] Hensen et al., loophole-free Bell (2015)
- [ ] LIGO, GW150914 (2016)
- [ ] Google Sycamore supremacy (2019, contested)
- [ ] IBM quantum utility (2023, contested)
- [ ] NIF ignition (2024 — target gain ≈1.5, not net plant)

## C. Collection families (`openai/math`)

Mathematical-physics slice:
- [ ] 260 Spacetime Penrose inequalities (gravity)
- [ ] 261 Anderson localization
- [ ] 262 Lieb–Thirring inequalities
- [ ] 263 Ionization & generalized ionization conjectures (Coulomb/energy)
- [ ] 264 Strong cosmic censorship near Kerr (gravity)
- [ ] 265 Area laws & tensor networks
- [ ] 266 Three MUBs in dimension six
- [ ] 267 Positive-temperature BEC & quantum depletion
- [ ] 268 Spin-one Haldane gap
- [ ] 269 Uniform Laughlin gap
- [x] 270 BFSS threshold + SU(2) positive spectrum — pack `study-packs/family-270.md`
- [ ] 271 Bloch law / magnetization laws
- [ ] 272 Entanglement without distillable secret key
- [ ] 273 Entropy photon-number inequality (vacuum/photon)
- [ ] 274 Parity not in QAC⁰
- [ ] 275 QMA-hardness of continuum Coulomb energy
- [ ] 276 Amplitude-damping channel capacity
- [ ] 277 Threshold repetition for entangled games
- [ ] 278 Kohn–Sham ensemble failure
- [ ] 279 Exact quantum factoring (fixed gate set)
- [ ] 280 Unitary vertex operator algebras & conformal nets
- [ ] 281 QAOA attains the SK optimum
- [ ] 282 Scale → conformal symmetry in 4D QFT
- [ ] 283 Unitary synthesis from a Boolean oracle
- [ ] 284 Randomized-vs-quantum query separation

Adjacent:
- [ ] 090 Riesz/Coulomb energies, triangular-lattice optimality
- [ ] 218 Ising conformal universality
- [ ] 221 Mézard–Paris formula (diluted spin glasses)
- [ ] 234 All-temperature pressure of Ising spin glasses
- [ ] 236 Free Ising spins on trees
- [ ] 373 Coulomb Monge problem

Outside the buckets (done as starter): `[x] 001 Milne's rationality conjecture — study-packs/family-001.md`

## D. Declassified / FOIA / official documents (verified)

Fusion & nuclear energy
- [ ] Project Sherwood (US AEC fusion program; declassified 1958; Bishop monograph 1960)
- [ ] ZETA, Harwell (Nature 181, 217, 1958 — claimed then refuted)
- [ ] Rover / NERVA nuclear thermal rockets (NTRS 20140008771, 19920001873)
- [ ] Project Orion (GA-5009, NTRS 20000096503; Dyson, Science 1965)
- [ ] Plowshare / GNOME / Sedan (LLNL page; DOE fact sheet)
- [ ] Gasbuggy (OSTI 7132471) & Rulison (OSTI 441657) gas-stimulation shots
- [ ] LLNL nuclear test-film declassification, 2017 (~750 films; LLNL-TR-727297)
- [ ] DOE/ERAB cold-fusion review, 1989 (DOE/S-0073; files.ncas.org/erab)
- [ ] NIF ignition, Dec 2022 (PRL 132, 065102/065103)
- [ ] SNAP-10A / SNAP-8 (NTRS 20210025352)

Gravity, spacetime & propulsion
- [ ] Project 1794 (NARA ARC ID 6920770 + 6981836)
- [ ] Electrogravitics reports 1956 (Aviation Studies Intl. — provenance unverified)
- [ ] T. T. Brown / ONR File 24-185 (Cady 1952 evaluation)
- [ ] NASA Breakthrough Propulsion Physics 1996–2002 (NTRS 20060000022; AIAA vol. 227)
- [ ] Eagleworks EMDrive (AIAA 2014-4029; JPP 2017) + refutations (CEAS 2021)
- [ ] Podkletnov claim (Physica C 1992) + NASA MSFC evals + Hathaway 2003 null
- [ ] DIA DIRDs AAWSAP/AATIP (FOIA 2019; warp-drive/dark-energy DIRD 2010)
- [ ] NIAC gravitational-wave detection studies (2012–13)
- [ ] Alcubierre 1994 (CQG 11, L73) + White 2011 (NTRS 20110015936)
- [ ] Gravity Probe B (PRL 106, 221101) & LIGO GW150914 (PRL 116, 061102)
- [ ] Woodward Mach-effect NIAC Phase II (2018–20; contested)

Vacuum, zero-point & negative energy
- [ ] Casimir 1948 / Sparnaay 1958 / Lamoreaux 1997 / Mohideen–Roy 1998
- [ ] Lamb–Retherford 1947 + Welton 1948
- [ ] Hawking 1974/75; Ford–Roman 1995/97; Pfenning–Ford 1997; Jaffe 2005
- [ ] DIA-08-1004-007, "Concepts for Extracting Energy From the Quantum Vacuum" (2010) — itself rejects net extraction
- [ ] AAWSAP DIRDs 18/19/29/36 (negative energy, antigravity, negative mass)
- [ ] CIA "Zero-point energy" Intellipedia note (FOIA Case 78752A)
- [ ] NASA/CR-2004-213311 vacuum-energy study + BPP TMs + Forward's Casimir battery (NTRS 19990023210)
- [ ] Cosmological-constant reviews (Weinberg 1989; Martin 2012)

EM archives, quantum matter & computing
- [ ] HAARP (AFRL/ONR; EIS AFD-111103-026; DTIC ADA355641, ADA426081)
- [ ] Project Sanguine → SEAFARER → ELF (MTU MS-037; DTIC ADA306957; OSTI 5844304)
- [ ] CIA CREST: Soviet Directed Energy Weapons (1985), Soviet Battlefield Lasers, Soviet Atomic Energy Program, Soviet Space Nuclear Power, Tesla Industrial Enterprise
- [ ] NARA Project Blue Book (+ NARA MJ-12 examination, negative)
- [ ] Bell 1964 · Aspect 1982 · Hensen 2015 · von Klitzing 1980 (Nobel 1985)
- [ ] DARPA QuIST (2001) + IARPA QCS (BAA-10-02, ~2010)
- [ ] NIST PQC standards (FIPS 203/204/205, Aug 2024)
- [ ] NSA PQC guidance (public); "Penetrating Hard Targets" (press-reported leak, not declassified)
- [ ] Sycamore 2019 (contested: Kalai et al.) · IBM utility 2023 (contested: Begušić–Chan)

## E. Legend resolutions (checked — no supporting documents found)

- [x] Cold fusion / ZPE engines validated — DOE/ERAB 1989 + DIA-08-1004-007 reject
- [x] ZETA proved fusion — refuted by Harwell's own correction
- [x] Orion flew / Plowshare profitable — no nuclear-pulse flight; gas unusable, program ended
- [x] Philadelphia Experiment — ONR fact sheet: untrue
- [x] Die Glocke / Nazi anti-gravity — no archival basis
- [x] MJ-12 / Roswell ET craft — NARA/GAO negative
- [x] Project 1794 = anti-gravity craft — files describe conventional VTOL
- [x] Biefeld–Brown = anti-gravity — ion wind (ONR 1952 skeptical)
- [x] HAARP weather/mind control — FAQ refutes; no such program docs
- [x] Tesla death ray — CREST shows a radio enterprise only
- [x] Podkletnov shielding — no replication; null tests
- [x] EMDrive thrust — null after controls (2018–21)
- [x] NIAC-funded Casimir extraction — no such award; real work = NASA/CR-2004-213311
- [x] Casimir = padlock on free energy — force real, extraction not (Jaffe 2005)

Footer: details and links per item in `physics-inventory.md`; archive evidence in `data/processed/work/research/archives-*.md`; tick items here as they become checked study packs.
