---
id: paper:2016hong-venue-research
type: paper
title: "Atomistic-scale analysis of carbon coating and its effect on the oxidation of aluminum nanoparticles by ReaxFF molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b00786"
year: 2016
authors:
  - "Sungwook Hong"
  - "Adri C. T. van Duin"
venue: "Journal of Physical Chemistry C"
pdf_sha256: "abc115674b2b3d76434bd4137d45da194ca9a541a11e5e66b6f9f6aa425d0539"
pdf_path: "papers/Hong_AlCOx_JPCC_2016_proof.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:combustion
  - keyword:reactive-md
  - keyword:galley-or-proof-pdf
  - keyword:neb
---
<!-- id:paper:2016hong-venue-research -->

## Summary

A **ReaxFF** parametrization for **Al/C/H/O** is developed using **VASP DFT** and **Jaguar QM** training sets, then applied in **ReaxFF molecular dynamics** (implemented in **ADF**) to model **hydrocarbon-derived carbon coating** on **aluminum nanoparticles (ANPs)** and subsequent **O₂ oxidation**, comparing to **prior experiments** on laser/plasma carbon coating.

## Methods

- **QM training (periodic):** **VASP** **GGA-PBE** with **PAW** potentials, **400 eV** cutoff; **Al(111)** slabs (**6 layers**, bottom layers fixed) for **hydrocarbon adsorption/decomposition**; **k-meshes** include **8×8×8** (bulk **Al₄C₃**) and **5×5×1** (slab adsorbates); **NEB** (**L-BFGS**, **3 images**) for barriers.
- **QM clusters:** **Jaguar** **B3LYP/6-311G** for **nonperiodic Al/C/H/O** geometries; **bond/angle scans** for **Al–C** dissociation and distortion energies.
- **ReaxFF optimization:** Sequential refinement of **Al–C**, **Al/H**, and angle/off-diagonal terms to match QM targets; **ReaxFF-NEB** cross-checks vs **DFT-NEB** for selected pathways (e.g., **C–C** cleavage unfavorability on **Al(111)**).
- **MD protocol (coatings / oxidation):** **NVT** with **Berendsen thermostat** (**100 fs** damping); **time step 0.1 fs** (motivated by high **T** up to **~3000 K**); executed with **ADF** **ReaxFF molecular dynamics** (**4–8** processors stated). **Hydrostatic pressure** / **NPT** segments: **N/A — not used** in the summarized coating/oxidation stages (constant-volume **NVT**).
- **Coating cycles:** **864 Al** ANP in **45×45×45 Å³** box with **350** gas molecules per cycle; **ANPs at 300 K**, **hydrocarbon gas at 2500 K for 15 ps**, cool to **300 K in 8.5 ps**; repeat cycles; precursors **ethylene**, **ethane**, **acetylene** compared.
- **Oxidation:** Carbon-coated ANP + **600 O₂** in **60×60×60 Å³**; **300 K vs 3000 K** snapshots to **150 ps**; elevated **O₂ density ~0.15 g/cm³** to accelerate kinetics within short MD windows.

## Findings

- ReaxFF reproduces key **QM interaction energies/barriers** and shows **hydrocarbon deposition** proceeds primarily by **H transfer to Al sites** with **no C–C bond breaking** in the ethylene coating runs (up to **six cycles**).
- **Carbon coverage** and **C/Al ratio** trends vs precursor follow **binding strength** ordering (**acetylene > ethylene > ethane**), modulating **coating thickness**.
- **Oxidation MD:** At **300 K**, oxidation products remain limited; at **3000 K**, **gas-phase H₂O, H₂, CO, CO₂** form as the **carbonaceous layer is stripped**, increasing exposed **Al** and **O₂** uptake—consistent with **temperature-dependent** protection described experimentally.

## Limitations

- Corpus PDF is an **ACS author proof** (`Hong_AlCOx_JPCC_2016_proof.pdf`); cite the **journal version-of-record** for pagination and final copy edits.
- **Short oxidative timescales** require **accelerated O₂ density**; reported oxidation kinetics are **qualitative** indicators within the MD window.

## Relevance to group

**van Duin** group **ReaxFF parametrization + application** on **Al combustion** nanoparticles with explicit **coating chemistry**.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.6b00786](https://doi.org/10.1021/acs.jpcc.6b00786) — *J. Phys. Chem. C* **120**, 9466–9480 (2016).

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Alternate PDF bytes: [[2016hong-venue-research-2]] (`Hong_AlCOx_JPCC_2016_reduced.pdf`).
