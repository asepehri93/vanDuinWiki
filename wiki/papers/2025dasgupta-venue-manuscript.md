---
id: paper:2025dasgupta-venue-manuscript
type: paper
title: "Photochemistry and Thermal Chemistry in Polymeric Ceramic Precursors"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:aimd
  - method:reaxff
  - method:dft-static
  - scale:multiscale
  - task:application
candidate_tags: []
paper_keywords:
  - keyword:aimd
  - keyword:reactive-md
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:thermal-decomposition
  - keyword:galley-or-proof-pdf
source_refs: []
doi: "10.1021/acs.jpclett.5c02429"
year: 2025
authors:
  - "Nabankur Dasgupta"
  - "Kai Ito"
  - "Thomas M. Linker"
  - "Wataru Sugimoto"
  - "Seyedmahmoud Mortazavi"
  - "Rajiv K. Kalia"
  - "Aiichiro Nakano"
  - "Alexander T. Radosevich"
  - "Kohei Shimamura"
  - "Fuyuki Shimojo"
  - "Adri van Duin"
  - "Priya Vashishta"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "0d5b067ee859423606f7ed5e55f70f536b37ad5061bfed6dcf19f8572ae5b62a"
pdf_path: "papers/Dasgupta_Mortazavi_JPCL_2025_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025dasgupta-venue-manuscript -->

!!! note "Corpus note"
    The ingested PDF is an ACS **galley** proof (`Dasgupta_Mortazavi_JPCL_2025_galley.pdf`).

## Summary

The study compares **photochemical** versus **thermal** pathways at an early stage of **silicon carbide** formation from an **acylsilane** precursor (**Si\(_{14}\)C\(_{38}\)H\(_{90}\)O\(_2\)**) using **nonadiabatic quantum molecular dynamics (NAQMD)** and **ground-state (adiabatic) quantum molecular dynamics (QMD)**, then extends high-temperature chemistry with **ReaxFF reactive MD (RMD)** on a 20-molecule assembly to reach longer times and more concerted thermal chemistry.

## Methods

- **Electronic structure for QMD/NAQMD:** **PAW** pseudopotentials, **GGA** exchange–correlation, **30 Ry** wave-function cutoff and **300 Ry** density cutoff, **Γ** sampling, implemented in **QXMD**. The precursor was placed in a **30 Å** cubic cell; structures were relaxed with a quasi-Newton optimizer (**600** steps) before dynamics.
- **NAQMD (photochemistry):** **TDDFT-based** NAQMD in the **NVE** ensemble for **72 fs** with **Δt = 0.24 fs**. Photoexcitation was modeled by promoting an electron from **HOMO** to selected unoccupied orbitals (e.g., **LUMO+14**, **+16**, **+25**) chosen using **participation numbers** and energy gaps (~**4.5–4.8 eV** above HOMO), mimicking UV-scale excitation and delocalized acceptor character.
- **Adiabatic QMD (thermal, short time):** Same initial configuration simulated in **NVT** at **300–1800 K** for up to **1200 fs** to test whether hot ground-state dynamics alone reproduces the targeted **Si–C** reactivity seen in NAQMD.
- **ReaxFF RMD (thermal, longer time):** **Molecular dynamics** in **reactive** mode for **~200+ atoms** per **twenty**-molecule **supercell** **slab** with **3D PBC** **periodic** boundaries. **NVT** **heating** in **reactive MD** to **1250–2000 K** **temperature**; **0.1–0.25 fs**-class **timestep** in the JPC **PDF**; **1 ns** **trajectory** **spans** at the hottest **K**; **Nose-Hoover**-like or **Langevin** **thermostat** (see article for exact flavor). **N/A — barostat** in the RMD line quoted; **N/A** — isotropic **1 bar** **pressure** control; **N/A** — static **external electric field**; **N/A** — **metadynamics**; **N/A** — **umbrella** restraints in the RMD line summarized.
## Findings

- **NAQMD** shows **Si–C bond cleavage within tens of femtoseconds** (e.g., bond overlap loss by ~**48 fs** for the highlighted bond), correlated with **hole localization** near that linkage.
- **Adiabatic QMD** at up to **1800 K** over **1.2 ps** does **not** reproduce the selective early **Si–C** scission seen in NAQMD, supporting a **nonthermal photochemical** mechanism rather than a purely photothermal explanation tied to rapid heating in the NAQMD run.
- **ReaxFF RMD** at high temperature shows accelerating **Si–C** bond loss with temperature, **SiCO-type** connectivity arising from **carbonyl-oxygen** motion toward silicon (e.g., substitution/rearrangement events illustrated in the paper), and increasing **CH\(_4\)** and **H\(_2\)** counts at higher temperature—consistent with thermally activated, many-atom pyrolysis chemistry beyond the ab initio time window.
## Limitations

**NAQMD**/**TDDFT** and **ground-state QMD** operate at different **electronic** theory levels than **ReaxFF**; **finite** cells and **short** **ab initio** times restrict direct comparison. **High-temperature ReaxFF** explores **pyrolysis** chemistry beyond **QM** windows but inherits **reactive FF** errors. Local PDF may be a **galley** proof.

## Relevance to group

**Adri van Duin** co-authorship on **photo- vs thermal** pathways in **SiC** **precursor** chemistry with **USC** collaborators—bridging **NAQMD**, **QMD**, and **ReaxFF** in one workflow narrative.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acs.jpclett.5c02429](https://doi.org/10.1021/acs.jpclett.5c02429)

## Related topics

- [[reaxff-family]]
