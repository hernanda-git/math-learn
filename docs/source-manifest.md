# Source corpus — index

Physics learning corpus gathered 2026-10-16. Local root: `C:/Workspace/math-learn/data/sources/` (gitignored — the files stay local; this index is committed so the corpus is reproducible).

**Contents:** 105 PDFs + 23 HTML pages, ≈670 MB, across 6 slices. ~87% of named targets acquired; every miss is recorded as a `link-only` row with reason + alternate. Every PDF passed a `%PDF` magic-byte check; volume scans were additionally page-verified (mislabelled aggregator copies were caught and replaced — see Corrections).

**Policy:** only arXiv, publisher open-access, NASA NTRS, DOE/OSTI, agency FOIA reading rooms, NARA, NIST, archive.org and openly posted author/university copies. **No sci-hub/libgen/paywall-bypass anywhere.** `mirror` = official host blocked at retrieval time (403/JS wall); mirrors are the Black Vault (FOIA archive), archive.org/Wayback copies of official URLs, or author pages. US-Government works are public domain; pre-1930 scans are public domain; a few in-copyright items sit as flagged `mirror` copies for personal study (canonical paywalled DOI recorded in the row).

## Slices

| dir | contents | targets | size |
|---|---|---|---|
| `papers-foundations/` | 23 PDFs — EM/relativity/quantum/stat-mech classics (Maxwell 1865, Hertz 1887, Planck 1900+1901, Einstein 1905 SR + photoelectric + 1915 GR + 1916 review, Bohr 1913 I–III, Heisenberg 1925, Schrödinger 1926, Dirac 1928, Carnot 1824, Clausius 1865, Gibbs 1902, Onsager 1931, Landauer 1961, Bell 1964, Aspect 1982, Feynman 1982) | 18/20 | 267.5 MB |
| `papers-vacuum/` | 14 PDFs — Casimir 1948, Lamb–Retherford 1947, Lamoreaux 1997, Mohideen–Roy 1998, Jaffe 2005, Ford–Roman 1995 + 1997, Ford–Pfenning–Roman 1998, Pfenning–Ford 1997, Hawking 1975, Cole–Puthoff 1993, Moddel–Dmitriyeva 2019, Jarzynski 1997, Martin 2012 | 13/17 | 9.3 MB |
| `papers-gravity-matter-qi/` | 17 PDFs — Penrose 1965, Gravity Probe B final, GW150914 (PRL + DCC companion), Alcubierre 1994, White 2011, BCS 1957, von Klitzing 1980, Haldane 1983, BB84, Shor, Grover, Hensen 2015, Sycamore (suppl.), IBM utility (Nature OA), Begušić–Chan rebuttal, NIF ignition PRL | 16/19 | 35.2 MB |
| `gov-fusion-energy/` | 16 PDFs + 20 HTML — NERVA/NTX history, Rover/NERVA workshop, Orion, SNAP overview (DTIC), Plowshare fact sheet + LLNL look-back, Gasbuggy + Rulison booklets, ERAB 1989 cold-fusion report (full PDF + HTML edition), NIF companions (PRL 129, PRE 106, Nature 601), LLNL test-film reanalysis, CIA CREST Soviet atomic energy + space nuclear power | 13/16 | 34.4 MB |
| `gov-gravity-vacuum/` | 22 PDFs — NARA Project 1794 (both reports), ONR 24-185 transcript, NASA BPP set (TM-107381, TM-97-206241, TM-2005-213998, TM-2004-213082, CP-1999-208694 proceedings, CR-2004-213311, Forward Casimir battery), Eagleworks full paper, Tajmar refutation (OA), Podkletnov evaluations ×2, DIA DIRDs 18/19/24/29/36, NSA Intellipedia ZPE, Woodward NIAC Phase II | 22/22 | 282.7 MB |
| `gov-em-quantum/` | 13 PDFs + 3 HTML — HAARP (fact sheet, 1993 EIS vol 1 + part 2, EMI study, ADA355641, ADA426081), CIA CREST (Soviet DEW 1985, battlefield lasers, Tesla enterprise), NIST FIPS 203/204/205, DARPA QuIST pages + PDF, IARPA QCS page | 16/19 | 57.3 MB |

Per-item detail (exact URL, status, size, license note) lives in each slice's `MANIFEST.md`.

## Collection (`openai/math`) — already local, not duplicated

All 59 physics manuscripts (25 Mathematical-physics families) are on disk in the read-only collection clone: `C:/Workspace/math/preprints/<preprint-dir>/paper.pdf`. Machine-readable list: `data/sources/collection-physics-raw.txt`. Study packs for the covered families: `../study-packs/family-270.md`, `family-001.md`.

## Corrections found while acquiring

- **Ford & Roman 1997** is *PRD* **55, 2082** (not 2080 — that DOI does not exist); gr-qc/9607003.
- **gr-qc/9711030** is Ford–Pfenning–Roman, *PRD* 57, 4839 (1998) — not Pfenning–Ford; the actual **Pfenning–Ford 1997** is gr-qc/9702026, *CQG* 14, 1743.
- **Bruhn 2006**: *Phys. Scr.* 74, **535–536** (no article at p. 561).
- **Gravity Probe B final** is arXiv:**1105.3456** (1104.2714 is a double-beta-decay review).
- **IBM quantum utility** has no matching arXiv id; Nature OA version used instead.
- Mislabelled aggregator copies rejected and replaced: Zenodo "Zur Elektrodynamik" = Max Abraham 1909; Zenodo "Elementary Principles" = Bryan's review; IA Feynman item = student seminar notes; Planck 1900 volume OCR-checked before keeping.

## Known link-only items (retry candidates)

Sparnaay 1958 (Elsevier), Hawking 1974 *Nature*, Weinberg 1989 (OA exists at UT Austin + OSTI — hosts unreachable from this network), Bloch 1930 (Springer), Boltzmann 1877 (no open scan; archive.org volume lacks the text), Anderson 1958 + Laughlin 1983 (APS paywall; Laughlin Nobel lecture is the open alternate), Feynman 1982 canonical (mirror copy stored), Bishop *Project Sherwood* (archive.org borrow-only), OSTI purls 7132471/441657/4476722/1959535 (osti.gov unreachable; alternates stored), Project Sanguine/ELF set (skipped; DTIC/OSTI links recorded), OSTI 5844304. DTIC and cia.gov bot-block this network — a normal browser session can fetch the official copies of the mirrored rows.
