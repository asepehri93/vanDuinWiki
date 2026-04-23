---
id: paper:2021gao-computationa-molecular-dynamics
type: paper
title: "Molecular dynamics study of melting, diffusion, and sintering of cementite chromia core-shell particles"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:oxides-ceramics
  - method:reaxff
  - material:alloy-bulk
  - material:oxide
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:oxide-surface
  - keyword:lammps
source_refs: []
doi: "10.1016/j.commatsci.2021.110721"
year: 2021
authors:
  - "Yawei Gao, Ana Paula Clares Pastrana, Guha Manogharan, Adri C.T. van Duin"
venue: "Comput. Mater. Sci. 199 (2021) 110721"
pdf_sha256: "d11facbf0b62ee2e88ad0ae813b87f1d477ad07e89062020819cbfc23af88351"
pdf_path: "papers/Gao_CompSciMat_2021_Cementite_Chromia.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021gao-computationa-molecular-dynamics -->

## Summary

ReaxFF molecular dynamics in LAMMPS models hydrated Fe\(_3\)C nanoparticles with a Cr\(_2\)O\(_3\) passivation shell versus bare Fe\(_3\)C, as a minimal atomistic picture of cementite in chromium-oxide-coated stainless steel powder during thermal processing. The authors probe melting with a Lindemann index across 1000–2600 K, mean-squared displacements and composition/RDF changes for diffusion at 900 K and 2000 K, and pairwise sintering in 200 Å cubic cells at 900 K (solid) and 2000 K (liquid) over 0.5 ns, including cohesive-energy estimates with a restraint potential to separate the particles. They report that the Cr\(_2\)O\(_3\) shell does not shift the inferred melting point relative to pure Fe\(_3\)C at the same particle size, but shell oxygen diffuses into the core and that melting initiates in the core for core–shell particles versus the surface for bare cementite; liquid-phase sintering progresses through four contact-to-fusion stages, while 900 K runs only reach the first three within the simulated time.

## Methods

### 1 — MD application (atomistic dynamics)

- **Engine / code:** LAMMPS with the ReaxFF implementation; charges updated every MD step.
- **System size & composition:** Spherical Fe\(_3\)C core (cementite crystal) radius 12 Å with Cr\(_2\)O\(_3\) shell inner/outer radii 13 and 15 Å, plus hydration (e.g. 240 H\(_2\)O in the large-cell workflow described in the article); a pure Fe\(_3\)C particle of 30 Å diameter; melting/diffusion cells 200 × 200 × 200 Å\(^3\); sintering uses two hydrated core–shell particles in the same 200 Å box. Atom types C, H, O, Fe, Cr.
- **Boundaries / periodicity:** Cubic cells with “sufficiently large” isolation of particles; open boundaries N/A (3D PBC in standard supercell setup for isolated nanoparticles in a box as stated).
- **Ensemble:** NVT throughout the MD stages described.
- **Timestep:** 0.25 fs (melting, diffusion, sintering segments as quoted).
- **Duration / stages:** Melting: temperature stepped 1000–2600 K in 200 K steps; 200 ps at each T after continuation from the prior T, trajectories saved every 1 ps. Diffusion: MD-NVT at 900 K and 2000 K. Sintering: 0.5 ns NVT (after initial non-contact configuration); sintering analysis at 900 K and 2000 K; an additional 1 ns NVT after 500 ps initial segment for a separation-energy workflow where described in the article. Cohesive energy: external restraint on selected atom pairs to separate the two particles.
- **Thermostat:** Berendsen with 100 fs temperature damping constant in the quoted segments.
- **Barostat / pressure:** N/A — NVT; no constant-pressure control.
- **Temperature:** 900 K and 2000 K for diffusion and sintering comparisons; 1000–2600 K heating protocol for melting; 300 K not used in these production cases (stated heating starts from 1000 K chain per Section 2.3.1 in the VOR text).
- **Pressure:** N/A in the sense of controlled hydrostatic stress — contact pressure in sintering is not a barostatted bulk pressure; the authors add a directional restraint for cohesive-energy pulls rather than a bulk barostat.
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A.
- **Electrostatics / ReaxFF QEq:** Charges are updated every integration step in the quoted diffusion and sintering segments.

### 2 — Force-field training

The work does not present a new global ReaxFF fit. The authors use a published C/H/O/Fe/Cr ReaxFF parametrization from Shin *et al.* (as referenced in the article). **Parent FF / elements:** that multi-element set with bond-order and polarizable (QEq-style) charges. **QM reference / training set for this paper:** N/A for new fitting — the manuscript instead **validates** Fe\(_3\)C and related properties before production MD. **Reference data and validation (Section 2.1):** a 3×3×3 Fe\(_3\)C supercell; comparisons of lattice constants, equation of state vs DFT literature, (100)/(010)/(001) surface formation energies vs DFT, and elastic moduli vs experiment; auxiliary BAND DFT (GGA-PBE, TZP) on Cr(CH\(_3\)\)\(_3\) to argue Cr–C bonds are weak relative to C–O chemistry so Cr/C bond terms are omitted in the FF. This is validation of an existing parameterization, not reoptimization.

### 3 — Static QM / DFT (validation only, not a standalone DFT study)

- **Functional / data used for comparison:** DFT from the literature for Fe\(_3\)C EOS and surfaces; BAND PBE/TZP for a molecular Cr–C strength estimate, as in Section 2.1. **N/A** as a primary DFT production campaign — the paper’s new simulations are ReaxFF MD; DFT entries support force-field **sanity checks**.

### 4 — Reviews, perspectives, or non-simulation studies

N/A — primary ReaxFF MD research article.

## Findings

**Melting and Lindemann index:** The Cr\(_2\)O\(_3\) shell does not change the apparent melting point vs pure Fe\(_3\)C of the same size; oxygen from the shell diffuses into Fe\(_3\)C and elevates “impurity”/oxygen content, destabilizing the core. Melting **starts in the core** for core–shell particles and **at the surface** for bare Fe\(_3\)C, as argued from Lindemann and structural analysis in the paper.

**Diffusion (MSD, RDF, composition):** At 2000 K (liquid) vs 900 K (solid), H and O are more mobile in MSD ordering than Fe, Cr, and C. Heating from 900 K to 2000 K redistributes O and C between shell and core in the direction summarized in the abstract; RDFs for C–Fe, O–Fe, O–Cr, and O–C track compositional change.

**Sintering:** Liquid (2000 K) sintering shows four stages: approach/contact, shell intermingling, core fusion. Solid 900 K runs reach only the first three within the 0.5 ns protocol; Stage 4 is not achieved at 900 K in the simulated time. Cohesive energy between particles is accessed via a restraint force to separate the pair.

**Comparisons:** Direct comparison of core–shell vs pure cementite under identical heating and box protocols; DFT/ experiment used only for pre-MD validation, not for one-to-one AM powder experiments (authors note micron-scale real powders vs nanometer model particles).

**Limitations (as implied in the text):** Nanometer particles and short times cannot map quantitatively onto 10–100 μm AM powders; ReaxFF errors on Fe\(_3\)C expansion in EOS validation are noted. No external field or plume chemistry is included.

**Corpus / KB honesty:** Prose is grounded in `pdf_path`; for figure-level numbers, use the same Comput. Mater. Sci. PDF. Slug `2021gao-venue-paper` is a proof duplicate; `2021gao-computationa-molecular-dynamics-2` is a reduced-size PDF of the same article.

## Limitations

Model particles are nanoscale and simulation times for sintering are finite; ReaxFF has documented discrepancies for some Fe\(_3\)C bulk expansion energies relative to DFT. Absolute alignment with industry powder sizes and atmospheres is not claimed.

## Relevance to group

Adri C. T. van Duin is senior author; application of ReaxFF to AM-relevant stainless steel powder chemistry.

## Citations and evidence anchors

Sections 2.1–2.4 and Figs. 1–2 *et seq.*, *Comput. Mater. Sci.* **199** (2021) 110721.

## Related topics

- [[reaxff-family]]
- [[2021gao-computationa-molecular-dynamics-2]]
