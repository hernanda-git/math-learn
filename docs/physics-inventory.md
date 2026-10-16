# Physics inventory — interests → laws, papers, families, archives

Master inventory for the interest profile in `user-interests.md`: energy, fusion, gravity, electromagnetism/Coulomb, thermodynamics, negative energy & backreaction, zero-point energy & vacuum, space & time, quantum matter, quantum computation.

**Layers:** (1) laws & formulas — standard textbook physics, orientation layer; (2) landmark published papers; (3) the `openai/math` physics slice with coverage status; (4) verified declassified / FOIA / official program documents; (5) legends with no documentary support; (6) archive search pointers.

**Scope honesty:** layer 3 is the complete physics slice of the collection; layer 4 is the verified archive inventory (checked 2026-10-16, raw evidence in `data/processed/work/research/`); layers 1–2 are a curated orientation set, not literally all of physics. Legendary claims are listed **with what documents actually show**, not as endorsements.

---

## 1. Laws & formulas (orientation layer)

### Energy
- Conservation of energy — `dE/dt = 0` for closed systems; Noether: energy = conserved charge of time-translation symmetry.
- Work–energy theorem — `W = ΔKE`.
- Mass–energy — `E = mc²`.
- Planck–Einstein — `E = hν`.
- Schrödinger (time-dependent) — `iℏ ∂ψ/∂t = Ĥψ`, with `Ĥ = T̂ + V̂`.
- Harmonic ground state — `E₀ = ½ℏω` (the zero-point term).

### Fusion
- Coulomb barrier — `V(r) = q₁q₂/(4πε₀r)`.
- Gamow tunneling — `P ∝ exp(−2πZ₁Z₂α c/v)`; reaction rate `⟨σv⟩` peaks at the Gamow window.
- Mass defect / Q-value — `Q = (Σm_reactants − Σm_products)c²`; D + T → ⁴He + n releases **17.6 MeV**.
- Lawson criterion — `n T τ_E ≳ 3×10²¹ keV·s/m³` for D–T.
- Debye screening — `λ_D = √(ε₀k_BT/(ne²))`.

### Gravity
- Newton — `F = Gm₁m₂/r²`.
- Einstein field equations — `G_μν + Λg_μν = (8πG/c⁴)T_μν`.
- Geodesic equation — freely falling motion extremizes proper time.
- Schwarzschild — `r_s = 2GM/c²`; metric `ds² = −(1−r_s/r)c²dt² + …`; Kerr for rotation (frame dragging).
- Hawking temperature/entropy — `T_H = ℏc³/(8πGMk_B)`, `S = k_B A/(4ℓ_P²)`; Bekenstein–Hawking.
- Penrose inequality — `M_ADM ≥ √(A/16π)` (collapse cannot hide more mass than the horizon area allows).
- Gravitational waves — quadrupole radiation; LIGO strain `h ~ 10⁻²¹`.

### Electromagnetism / Coulomb
- Coulomb — `F = (1/4πε₀) q₁q₂/r²`.
- Maxwell's equations — Gauss, no monopoles, Faraday, Ampère–Maxwell; light speed `c = 1/√(μ₀ε₀)`.
- Lorentz force — `F = q(E + v×B)`.
- Energy transport — Poynting `S = E×H`; density `u = ½(ε₀E² + B²/μ₀)`.
- Radiation — Larmor power `P = q²a²/(6πε₀c³)`.
- Fine-structure constant — `α = e²/(4πε₀ℏc) ≈ 1/137.036`.

### Thermodynamics
- Laws — 0th: thermal equilibrium transitive; 1st: `ΔU = Q − W`; 2nd: `ΔS_total ≥ 0`; 3rd: `S → 0` as `T → 0`.
- Entropy — Boltzmann `S = k_B ln Ω`; Clausius `dS = δQ_rev/T`.
- Potentials — `F = U − TS`, `G = H − TS`; Maxwell relations.
- Carnot bound — `η = 1 − T_c/T_h`.
- Fluctuation theorems — Jarzynski `⟨e^{−βW}⟩ = e^{−βΔF}`.
- Information — Landauer: `k_BT ln2` erased per bit.

### Negative energy & backreaction
- Energy conditions — weak/null/dominant/averaged (`T_μν k^μ k^ν ≥ 0` and relatives); classical GR assumes them.
- Quantum inequalities (Ford–Roman) — negative energy density is allowed in QFT but bounded in magnitude × duration (first derived 1994/95).
- Hawking pair picture — negative-energy flux into the horizon funds the outgoing radiation; backreaction shrinks `M`.
- Warp metrics — Alcubierre 1994 requires negative energy density; Pfenning–Ford 1997 showed the quantum inequalities make it unphysical for known physics.

### Zero-point energy & vacuum
- Oscillator zero-point — `E_n = (n+½)ℏω`; each mode keeps `½ℏω` at T = 0.
- Casimir — `F/A = π²ℏc/(240 d⁴)` (attractive; negative pressure `P = −π²ℏc/(240 d⁴)`).
- Lamb shift — 2S₁/₂–2P₁/₂ splitting ≈ **1057.8 MHz** (vacuum-fluctuation evidence).
- Schwinger pair production — critical field `E_c = m_e²c³/(eℏ) ≈ 1.32×10¹⁸ V/m`.
- Cosmological constant — observed dark-energy density `ρ_Λ ≈ 6×10⁻¹⁰ J/m³`; QFT vacuum estimates exceed it by ~10¹²⁰ (the cosmological-constant problem).
- Interpretation caveat — Jaffe (2005): the Casimir force follows from standard QED (Lifshitz/van der Waals) without requiring "extractable" vacuum energy.

### Space and time
- Minkowski interval — `ds² = −c²dt² + dx²`; Lorentz factor `γ = 1/√(1−v²/c²)`.
- Time dilation / length contraction / relativistic Doppler; twin effect.
- Equivalence principle; gravitational redshift `Δν/ν = ΔΦ/c²`; GPS net correction ≈ **+38 μs/day**.
- Friedmann equations — `(ȧ/a)² = 8πGρ/3 − kc²/a² + Λc²/3`.
- Singularity/censorship — Penrose 1965 trapped-surface theorem; cosmic censorship (family 264 works near two-ended Kerr).

### Quantum matter
- Schrödinger equation; uncertainty `ΔxΔp ≥ ℏ/2`.
- Pauli exclusion; Fermi–Dirac vs Bose–Einstein statistics; BEC below `T_c`.
- Heisenberg model — `Ĥ = −J Σ⟨ij⟩ S_i·S_j`; ferromagnet Bloch law `M ∝ M₀(1 − cT^{3/2})`; Haldane gap for integer-spin chains (`Δ ≈ 0.41J` for S=1).
- Quantum Hall — `σ_xy = νe²/h` (integer plateaus to 10⁻⁷); Laughlin fractional states (ν = 1/3 wavefunction — family 269).
- Density-functional theory — Kohn–Sham equations `(−ℏ²/2m ∇² + v_eff)φ_i = ε_iφ_i`; ensemble-representation failure studied in family 278.
- Lieb–Thirring — kinetic-energy bounds by density moments (family 262 gives sharp finite-matrix constants).

### Quantum computation
- Qubit — `|ψ⟩ = α|0⟩ + β|1⟩`, unitaries as gates; no-cloning.
- Bell/CHSH — classical `|S| ≤ 2`, quantum `2√2`; loophole-free tests 2015.
- Algorithms — Shor (factoring, quantum polynomial), Grover (`√N` search); families 279 (exact factoring over fixed gate sets), 283 (unitary synthesis), 284 (query-complexity separation).
- Complexity — BQP / QMA; family 275 is QMA-hardness of continuum Coulomb energy.
- Channels — capacity of amplitude-damping channels (family 276); entanglement vs secret-key distillation (family 272).

---

## 2. Landmark published papers (by field)

| Field | Paper |
|---|---|
| EM | Maxwell, *A Dynamical Theory of the Electromagnetic Field*, Phil. Trans. R. Soc. 155 (1865); Hertz wave experiments (1887); Lorentz electron theory (1895→1904) |
| Relativity/gravity | Einstein, SR (Ann. Phys. 17, 1905) and GR field equations (1915); Schwarzschild (1916); Penrose, PRL 14, 57 (1965); Hawking, Nature 248, 30 (1974) + CMP 43, 199 (1975); Gravity Probe B final, PRL 106, 221101 (2011); GW150914, PRL 116, 061102 (2016) |
| Quantum foundations | Planck (1900); Einstein photoelectric (1905); Bohr (1913); Heisenberg (1925); Schrödinger (1926); Dirac (1928); Bell, Physics 1, 195 (1964); Aspect et al., PRL 49, 1804 (1982); Hensen et al., Nature 526, 682 (2015) |
| QFT / vacuum | Dirac radiation theory (1927); Lamb–Retherford, PR 72, 241 (1947); Feynman/Schwinger (1948); Casimir, Proc. KNAW 51, 793 (1948); Sparnaay, Physica 24, 751 (1958); Lamoreaux, PRL 78, 5 (1997); Mohideen–Roy, PRL 81, 4549 (1998); Jaffe, PRD 72, 021301 (2005) |
| Negative energy | Ford–Roman, PRD 51, 4277 (1995); Pfenning–Ford, CQG 14, 1743 (1997); Alcubierre, CQG 11, L73 (1994) |
| Thermo / stat. mech. | Carnot (1824); Clausius (1850/65); Boltzmann (1877); Gibbs (1902); Onsager (1931); Landauer (1961); Jarzynski, PRL 78, 2690 (1997) |
| Quantum matter | Bloch (1930); BCS (1957); Anderson (1958); von Klitzing et al., PRL 45, 494 (1980); Haldane, PRL 50, 1153 (1983); Laughlin, PRL 50, 1395 (1983) |
| Quantum info | Feynman, *Simulating physics with computers* (1982); BB84 (1984); Shor (1994/97); Grover (1996); Nielsen–Chuang (2000); Arute et al., Nature 574, 505 (2019); Kim et al., Nature 618, 500 (2023, contested — Begušić–Chan arXiv:2306.16372) |
| Fusion | Fleischmann–Pons (1989, refuted by DOE/ERAB 1989); NIF ignition, PRL 132, 065102 (2024) — target gain ≈ 1.5, not net plant gain |

---

## 3. The collection: `openai/math` physics slice

All 25 Mathematical-physics families (59 manuscripts), with Lean catalog flag and coverage. Full 372-family list: `family-list.md`.

| # | Family | Lean | m# | Coverage |
|---|---|---|---|---|
| 260 | Spacetime Penrose inequalities (area/charge/rotation/AdS) | – | 13 | queued |
| 261 | Anderson localization / delocalization | – | 2 | queued |
| 262 | Sharp finite-matrix Lieb–Thirring inequalities | Y | 3 | queued |
| 263 | Ionization and generalized ionization conjectures | Y | 3 | queued |
| 264 | Strong cosmic censorship near two-ended Kerr data | – | 3 | queued |
| 265 | Area laws and tensor networks for 2D gapped systems | – | 2 | queued |
| 266 | Exactly three MUBs in dimension six | – | 2 | queued |
| 267 | Positive-temperature BEC and exact quantum depletion | – | 5 | queued |
| 268 | The spin-one Haldane gap | – | 2 | queued |
| 269 | Uniform Laughlin gap under disorder | Y | 2 | queued |
| 270 | BFSS threshold and positive-energy bound states | Y* | 2 | **covered** (`study-packs/family-270.md`) |
| 271 | Bloch's law, lattice correction, spherical magnetization law | – | 4 | queued |
| 272 | Entanglement without distillable secret key | – | 1 | queued |
| 273 | Entropy photon-number inequality | – | 1 | queued |
| 274 | Parity ∉ QAC⁰ | Y | 2 | queued |
| 275 | QMA-hardness of continuum Coulomb energy | – | 2 | queued |
| 276 | Classical capacity of generalized amplitude damping | Y | 1 | queued |
| 277 | Threshold repetition for entangled games | Y | 1 | queued |
| 278 | Failure of Kohn–Sham ensemble representation | – | 1 | queued |
| 279 | Exact quantum factoring over a fixed finite gate set | – | 1 | queued |
| 280 | Unitary vertex operator algebras and conformal nets | – | 1 | queued |
| 281 | QAOA attains the SK optimum | – | 2 | queued |
| 282 | Scale → local conformal symmetry in 4D QFT | – | 1 | queued |
| 283 | Polynomial-time unitary synthesis from a Boolean oracle | – | 1 | queued |
| 284 | Optimal quartic randomized-vs-quantum query separation | – | 1 | queued |

`*` 270: catalog says `–`; an uncatalogued `sorry`-free 74-file Lean development exists in-tree (`lean/OAI/MathematicalPhysics/BFSS/`), audited 2026-10-16 and recorded in `families.sqlite`.

Physics-adjacent families outside the Mathematical-physics subject: `090` (Riesz/Coulomb energies, triangular-lattice optimality), `218` (Ising conformal universality), `221`/`234`/`236` (spin glasses, Ising on trees), `373` (Coulomb Monge problem). Also `001` (starter family, number theory) already has a pack.

---

## 4. Declassified / FOIA / official program documents (verified)

Status labels: `declassified`, `FOIA-released`, `official/public`, `published`. Raw evidence (links opened and checked 2026-10-16): `data/processed/work/research/archives-*.md`.

### Fusion & nuclear energy
- **Project Sherwood** — the classified US fusion program (Princeton Matterhorn stellarator, LANL Perhapsatron, LLNL mirrors); declassified along with the 1958 Atoms-for-Peace push. AEC monograph: Bishop, *Project Sherwood* (1960; archive.org `projectsherwoodu0000bish`). `official/public`.
- **ZETA (Harwell, 1958)** — Nature 181, 217; claimed fusion neutrons, refuted by Harwell's own correction within ~4 months (plasma instabilities, not D–D fusion). `published` + refuted.
- **Rover / NERVA** — nuclear thermal rockets, Nevada tests 1959–1973 (NRX-A3 to 1122 MW/13 min; Phoebus 2A ~4100 MW/12 min). NASA NTRS 20140008771, 19920001873. `official/public, declassified historical reports`.
- **Project Orion** — nuclear-pulse design studies (GA-5009 1964); only non-nuclear sub-scale tests flown. NASA NTRS 20000096503; Dyson, *Death of a Project*, Science 149 (1965). `official/public`.
- **Plowshare / GNOME / Sedan / Gasbuggy / Rulison** — peaceful nuclear explosions for excavation and gas stimulation; stimulated but radioactive gas → failure; ended 1977. DOE LM site pages, OSTI 7132471/441657, LLNL Plowshare page. `official/public`.
- **LLNL 2017 atmospheric test-film declassification** — ~750 films re-scanned; revealed 1950–60s yield measurements were off 20–30%. LLNL-TR-727297 + press 43191/43956. `declassified`.
- **1989 DOE/ERAB cold fusion review (DOE/S-0073)** — "no convincing evidence" of useful energy or a nuclear origin; recommended against dedicated funding. files.ncas.org/erab. `official/public`.
- **NIF ignition (5 Dec 2022)** — 2.05 MJ laser → 3.1 MJ fusion (target gain ≈1.5); first G>1; not net plant energy (PRL 132, 065102/065103). `published`.
- **SNAP-10A** — first (and only US) fission reactor in orbit, launched 3 Apr 1965; SNAP-8 ground-tested only. NASA NTRS 20210025352. `official/public`.

### Gravity, spacetime & propulsion
- **Project 1794** (USAF/Avro saucer, 1956) — declassified by NARA 2012: NARA NDC blog; RG 342, **ARC ID 6920770** (report) + 6981836 (1957 extension). Conventional VTOL study, **not** anti-gravity. `declassified (NARA)`.
- **"Electrogravitics Systems" / "The Gravitics Situation"** (Aviation Studies Intl., 1956) — British industry studies circulating as scans; **not** found as a US declassification → status unverified. `uncertain provenance`.
- **T. T. Brown / ONR File 24-185** (W. M. Cady, 15 Sep 1952) — a skeptical Navy evaluation of the Biefeld–Brown anti-gravity proposal; effect explained as ion wind. `official/public`.
- **NASA Breakthrough Propulsion Physics** (1996–2002) — assessed space drives / warp / wormholes; no breakthrough; closed out. NTRS 20060000022, 19970009634; book *Frontiers of Propulsion Science* (AIAA vol. 227, 2009). `official/public`.
- **NASA Eagleworks EMDrive tests** — AIAA 2014-4029; JPP 2017 (10.2514/1.B36120); claimed ~1.2 mN/kW. Refuted 2018–2021: Tajmar et al., CEAS Space J. (10.1007/s12567-021-00385-1) — no thrust after controls. `official/public` + refuted.
- **Podkletnov gravity-shielding** — Physica C 203, 441 (1992); no replication; NASA MSFC evaluations NTRS 19990046249 / 19990023209; null test: Hathaway et al., Physica C 385, 488 (2003). `published`, refuted.
- **DIA DIRDs (AAWSAP/AATIP, FOIA 2019)** — e.g. "Warp Drive, Dark Energy, and the Manipulation of Extra Dimensions" (2010); literature surveys, not test programs. `FOIA-released`.
- **NASA NIAC gravitational-wave studies** — atom-interferometry GW detection concepts (2012–13). **No** NIAC HFGW-*generator* study exists. `official/public`.
- **Alcubierre 1994** (CQG 11, L73); **White, "Warp Field Mechanics 101"** (NASA JSC-CN-24651/NTRS 20110015936, 2011) — theory/analysis only, "no Chicago Pile moment". `published` / `official/public`.
- **Gravity Probe B** (PRL 106, 221101) and **LIGO GW150914** (PRL 116, 061102) — real tests/measurements of relativistic gravity. `published`.
- **Woodward Mach-effect, NIAC Phase II (2018–20)** — small thrust claims contested/unreplicated. `official/public` + contested.

### Vacuum, zero-point & negative energy
- **Casimir 1948** (Proc. KNAW 51, 793); **Sparnaay 1958** (first attempt, ~no confirmation); **Lamoreaux PRL 78, 5 (1997)** (~5% agreement); **Mohideen–Roy PRL 81, 4549 (1998)**. `published`.
- **Lamb–Retherford 1947** + Welton 1948; **Hawking 1974/75** (negative-energy flux interpretation); **Ford–Roman PRD 51, 4277 (1995)** + PRD 55, 2080 (1997); **Pfenning–Ford CQG 14, 1743 (1997)**; **Jaffe PRD 72, 021301 (2005)**. `published`.
- **DIA-08-1004-007, "Concepts for Extracting Energy From the Quantum Vacuum" (2010)** — FOIA-released DIRD; reviews Casimir/ZPF extraction proposals and its own text states none has been demonstrated and that Forward's cycle loses energy (thermodynamic failure). DIA FOIA FileId/170031; mirrored in the Black Vault DIRD set. `FOIA-released`.
- **AAWSAP DIRD series (38 docs, 2009–11)** — incl. DIRD_18 (wormholes/negative energy), DIRD_19 (antigravity survey), DIRD_29 (negative mass propulsion), DIRD_36 (negative-energy tomography). Speculative literature surveys. `FOIA-released`.
- **CIA release: "Zero-point energy" (Intellipedia), FOIA Case 78752A (2014)** — encyclopedic note, no research findings. `FOIA-released`.
- **NASA/CR-2004-213311**, "Study of Vacuum Energy Physics for Breakthrough Propulsion" (NTRS 20040171927) + BPP/TM reports (TM—2004-213082, TM—2005-213998) + workshop proceedings incl. Forward's Casimir "battery" paper (NTRS 19990023210) and Puthoff's vacuum-engineering talk. `official/public`; Forward's cycle contradicted in the DIA review.
- **Cosmological constant problem** — Weinberg, RMP 61, 1 (1989); Martin, C. R. Physique 13, 566 (2012). `published`.

### Electromagnetism archives, quantum matter, quantum computing
- **HAARP** — official HF ionospheric heater (3.6 MW, 180 antennas, 2.7–10 MHz); AFRL + ONR; transferred to U. Alaska Fairbanks 2015; FAQ states not classified. EIS: Kirtland AFB AFD-111103-026; DTIC ADA355641, ADA426081. `official/public`.
- **Project Sanguine → SEAFARER → ELF** — Navy ELF submarine comms; declassified EIS/hearing records at MTU Archives MS-037; DTIC ADA306957; OSTI 5844304; NRC 1997 evaluation; ended 2004. `declassified`.
- **CIA CREST** — ~13M pages, online since 17 Jan 2017; physics-relevant examples: *Soviet Directed Energy Weapons* (CREST 19850305), *Soviet Battlefield Lasers* (DOC_0000500257), *Soviet Atomic Energy Program* (CIA-RDP79R01012A022200020001-4), *Soviet Space Nuclear Power* (SW91-10074X), *Nikola Tesla Industrial Enterprise* (CIA-RDP82-00457R009200160001-6 — radio apparatus, no death ray). `declassified`.
- **NARA Project Blue Book** — 12,618 sightings, 701 unexplained; USAF found no evidence of beyond-known science; NARA's MJ-12 examination negative. `declassified`.
- **Bell 1964; Aspect 1982; Hensen 2015; von Klitzing 1980 (+ Nobel 1985)** — quantum matter foundations. `published`.
- **DARPA QuIST (2001–)** — first DARPA QIS program; DARPA + IARPA quantum program families (CSQ, LogiQ, MQCO, QEO); IARPA QCS (BAA-10-02, ~2010). `official/public`.
- **NIST PQC standardization** — FIPS 203/204/205 (ML-KEM, ML-DSA, SLH-DSA) published 13 Aug 2024. `official/public`.
- **NSA quantum-cryptanalysis interest** — public PQC migration guidance (`official`); "Penetrating Hard Targets" ($79.7M) is `reported via press (leaked, not declassified)` — Washington Post, 2 Jan 2014.
- **Google Sycamore supremacy (Nature 574, 505, 2019)** — contested (Kalai et al., arXiv:2210.12753); **IBM quantum utility (Nature 618, 500, 2023)** — contested (Begušić–Chan arXiv:2306.16372). `published`, contested.

---

## 5. Legends — what documents actually show

Consolidated; each was searched, not assumed.

- **"Cold fusion / zero-point engines validated in government archives"** — no document found. The DOE/ERAB 1989 review rejected cold fusion; DIA-08-1004-007 itself states no continuous vacuum-energy extraction is demonstrated and that cyclic Casimir schemes fail thermodynamics. A "DOE 2006 zero-point review" could not be sourced → unsubstantiated.
- **"ZETA proved fusion (1958)"** — refuted by the UK's own correction; plasma instability artifact.
- **"Orion flew / Plowshare was profitable"** — no nuclear-pulse flight exists; Plowshare produced radioactive, unusable gas and was terminated.
- **"Philadelphia Experiment"** — ONR fact sheet: untrue; no logs/orders/records support it.
- **"Die Glocke / Nazi anti-gravity"** — no archival basis (Witkowski claim; no engineering record).
- **"MJ-12", "Roswell ET craft"** — NARA searches negative; USAF/GAO reports consistent with balloon projects.
- **"Avrocar / Project 1794 = anti-gravity craft"** — the declassified files describe conventional VTOL thrust.
- **"Biefeld–Brown = anti-gravity"** — mainstream explanation: ion wind; ONR 1952 evaluation skeptical.
- **"HAARP = weather/mind control"** — HAARP FAQ refutes; HF waves don't couple to tropospheric weather; no program documents support it.
- **"Tesla death ray"** — CREST's Tesla documents concern a Yugoslav radio enterprise.
- **"Podkletnov gravity shielding"** — no replication; NASA/Hathaway null results.
- **"EMDrive = propellantless thrust"** — 2018–2021 controlled tests found no thrust after thermal/EM artifacts removed.
- **"NIAC funded Casimir/vacuum-energy extraction"** — no such NIAC award in NASA's funded-studies list (the real work was the 2004 BPP contractor study).
- **"Casimir force proves vacuum is a power source"** — force is real and measured; Jaffe 2005 shows it follows from ordinary QED without extractable vacuum energy.

---

## 6. Archive search pointers

- **CIA CREST** — `cia.gov/readingroom` (advanced search or `document-type/crest`); confirm `CIA-RDP…` numbers.
- **NARA** — `catalog.archives.gov` (e.g. ARC 6920770) + `archives.gov/research/military/air-force/ufos`; NDC blog for declassification stories.
- **NASA NTRS** — `ntrs.nasa.gov` (BPP: 20060000022, 19970009634; warp: 20110015936; NERVA: 20140008771).
- **DOE OSTI / OpenNet** — `osti.gov`, `osti.gov/opennet` (Plowshare, SNAP, ELF monitoring).
- **DTIC** — `discover.dtic.mil` (ADA accessions; was under maintenance during checks).
- **DIA FOIA reading room / Black Vault DIRD sets** — `dia.mil` FOIA (HTTP 403 to bots; mirrors at the Black Vault).
- **Affiliated raw evidence for this doc** — `data/processed/work/research/archives-{fusion-energy,gravity-propulsion,vacuum-zeropoint,em-quantum}.md`.

Footer: compiled 2026-10-16 from the verified research artifacts above + standard textbook physics (layers 1–2). Anything not backed by a checked source is out of scope by construction; corrections go through the same critic-verify loop as the study packs.
