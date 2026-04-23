---
id: paper:2025wang-venue-manuscript
type: paper
title: "New ReaxFF Reactive Force Field Optimized for Vibrational and Thermal Properties of Molybdenum Disulfide"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:2d-layered
  - domain:reactive-md
  - material:tmd
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:lammps
  - keyword:2d-materials
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.5c00464"
year: 2025
authors:
  - "Tao Wang"
  - "Juan M. Marmolejo-Tejada"
  - "Martín A. Mosquera"
  - "Vincent H. Crespi"
  - "Adri C. T. van Duin"
venue: "The Journal of Physical Chemistry Letters"
pdf_sha256: "9db3e0fcee4f42cc3bd88eb1283bad3a3ecc22c1f87d9800a8744612b2ce90e7"
pdf_path: "papers/Wang_JPC_letters_2025_MoS2_phonons_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025wang-venue-manuscript -->

## Summary

Phonon dispersions and lattice thermal conductivity of two-dimensional transition metal dichalcogenides are expensive at full first-principles fidelity in large, defective cells. This letter introduces **ReaxFF₂₀₂₄** for monolayer **MoS₂**, fit using a comparatively **small DFT training set**, with the explicit goal of reproducing **harmonic and anharmonic lattice dynamics** while retaining ReaxFF’s ability to model **bond rearrangements**. Relative to the earlier **ReaxFF₂₀₁₇** MoS₂ parameterization, the new force field shifts zone-center optical phonon frequencies much closer to DFT references and predicts an **in-plane thermal conductivity κ∞ ≈ 73 W K⁻¹ m⁻¹**, described as falling within the spread of experimental measurements quoted in the paper.

## Methods

- **Baseline and target:** Prior **ReaxFF₂₀₁₇** for 2D MoS₂ (Ostadhossein et al.) reproduces vacancy energetics but overestimates optical phonon frequencies; **ReaxFF₂₀₂₄** is reoptimized with emphasis on **small-displacement dynamics** near equilibrium as well as reactive degrees of freedom.
- **Training data:** Density functional theory calculations—described as a modest number of DFT evaluations compared with typical machine-learning potential datasets—used to fit bond-order and related ReaxFF terms for Mo–S interactions relevant to phonons and thermal transport.
- **Validation:** Comparison of Γ-point and dispersion-related phonon features to DFT (e.g., A₂″, E′ modes cited in the abstract); thermal conductivity from equilibrium MD using **Green–Kubo** heat-flux autocorrelation (as standard for κ in the letter’s framing).
- **Context:** Discussion contrasts against ML potentials (SNAP, GAP, MTP) and nonreactive fits (e.g., Stillinger–Weber) that target phonons but omit reactivity.

**1 — MD application (atomistic dynamics).** LAMMPS **molecular dynamics** with the letter’s ReaxFF on **monolayer MoS₂** **(PBC 3D supercell; see VOR for atom count)**. **NPT** equilibration: **Berendsen** **thermostat** (damping **100** **fs**) and **Berendsen** **barostat** (damping **5000** **fs**), **0.25** **fs** time step, **25** **ps** duration, target near **300** **K** as in the main text. **Melt**/**anneal** stages in the **SI** use **0.5** **fs** in places. **κ** from **NVT** **equilibrium** **Green–Kubo** with isothermal **temperature** sets per the letter (e.g. **~300** **K** and higher for thermal transport). **N/A** — no static **electric** **field** in these MD sets; **N/A** — no **replica** or **metadynamics**; **NPT** **barostat** only on the equilibration leg; **κ** production is **NVT** as stated.

**2 — Force-field training.** **Parent:** **ReaxFF** **ReaxFF₂₀₂₄** for **2D** **MoS₂** built from **ReaxFF₂₀₁₇**-class **parameters**; **DFT** **reference** for **formation** **energies**, **harmonic**/**anharmonic** **phonon** targets, and small-displacement **dynamics**; **QM** **training** set described as small versus MLIP corpora. **Optimization** and **parameter** table in the letter and **SI**; **validation** against **DFT** **phonon** **frequencies** and **experiment**-anchored **κ** quotes.

**3 — Static QM / DFT-only** — **N/A** (DFT is **reference** for **ReaxFF** training, not a separate **DFT** “application” block for this page).

**4 — Review** — **N/A.**
## Findings

- **Optical modes at Γ:** ReaxFF₂₀₂₄ moves the zone-center A₂″ and E′ frequencies from **1438 cm⁻¹ and 822 cm⁻¹** (ReaxFF₂₀₁₇) to **456 cm⁻¹ and 358 cm⁻¹**, near DFT values **461 cm⁻¹ and 367 cm⁻¹** quoted in the abstract.
- **Thermal conductivity:** κ∞ **≈ 73 W K⁻¹ m⁻¹** for the monolayer model studied, consistent with the experimental range cited by the authors.
- **Positioning:** The authors highlight **ReaxFF** as simultaneously trainable for **near-equilibrium** **phonon** **dynamics** and **reactive** **chemistry**, enabling **defect** and **heat** **transport** studies in **TMDs** in one **classical** stack; **outlook** in the letter points to **future** **transfer** **tests** (see `## Limitations`).

- **Corpus honesty:** This note tracks a **galley** `pdf_path`; any **erratum**-level **number** change belongs to the VOR.

## Limitations

Galley PDF in corpus; check the final journal pages for any numerical updates. Classical MD thermal conductivity depends on simulation size, thermostat, and duration; the letter should be consulted for convergence tests. Transferability to other chalcogenides is suggested but requires separate validation.

## Relevance to group

Core van Duin-group ReaxFF development for 2D MoS₂ with Vincent H. Crespi and colleagues; supports large-scale reactive + thermal transport modeling.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpclett.5c00464](https://doi.org/10.1021/acs.jpclett.5c00464)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]

## Reader notes (navigation)

- Corpus filename includes **galley**; when a clean JPCL version-of-record PDF is ingested, update `pdf_path` / `pdf_sha256` via manifest sync scripts.
