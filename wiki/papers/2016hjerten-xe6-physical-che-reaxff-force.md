---
id: paper:2016hjerten-xe6-physical-che-reaxff-force
type: paper
title: "A ReaxFF force field for sodium intrusion in graphitic cathodes"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/c6cp06774c"
year: 2016
authors:
  - "Eirik Hjertenæs"
  - "Anh Quynh Nguyen"
  - "Henrik Koch"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "1d2ac2027652c6f34110300d187b2659257e733ba224b001262983652b57d160"
pdf_path: "papers/ReaxFF_others/Hjertenaes_PCCP_2016_Na_graphite.pdf"
extraction_quality: "good"
group_affiliation: false
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:charge-equilibration
  - keyword:monte-carlo-sampling
  - keyword:dft-static
---
<!-- id:paper:2016hjerten-xe6-physical-che-reaxff-force -->

## Summary

A **Na–C (graphitic) ReaxFF** parameter set is **trained** against **DFT/PBE** data on **potential energy surfaces**, **geometries**, and **charge-related observables**, then applied to **hybrid grand-canonical Monte Carlo / molecular dynamics (GC-MC/MD)** simulations of **sodium intrusion** in simplified **graphitic cathode** models motivated by **aluminum electrolysis** wear and **sodium-ion battery** adjacency. The **PCCP** article frames **Na** **chemical potential** control as essential for modeling **intercalation** versus **pore** **filling** in **disordered** **carbon** **microstructures**.

## Methods

**Force-field training (Na–C ReaxFF):** **QM reference** uses **DFT/PBE** data for **Na adsorption and intercalation** on **PAH** models (**circumcoronene**, stacked **coronene** pairs, etc.), including **gradient-rich PES** regions weighted heavily in the error function. **Optimization** uses **Metropolis Monte Carlo** moves on ReaxFF parameters with **simulated annealing** cycles minimizing a weighted **least-squares** mismatch to QM targets (**Table 1** in *PCCP*). **EEM** bond-order/charge parameters are trained against **MDC-q** reference charges on selected **Na/PAH** configurations.

**MD application (GC-MC/MD + ReaxFF):** After fitting, **hybrid grand-canonical Monte Carlo / MD** imposes **Na chemical potential** on **graphitic cathode** **granule** models with distinct **ordered** vs **pore-like inter-domain** carbon (**PCCP** §4 and figures). **Timestep, thermostat/barostat, move acceptance rules, and trajectory lengths:** **N/A — not transcribed numerically here**; see **article/SI**.

**Static QM / DFT:** Training **DFT/PBE** settings (**dispersion**, **basis**, **k-point** conventions) are in the **PCCP** computational section (**N/A — not copied into this summary**).

**GC-MC/MD supercells:** **Na** insertion cells use **3D PBC** **LAMMPS**-style **granule** models whose **composition** sets porosity. **Imposed bulk hydrostatic pressure during uptake:** **N/A — chemical potential** is the primary control in the summarized protocol.

## Findings

- The fitted force field **reproduces training PES features** with **reasonable accuracy** while acknowledging **EEM limitations** for steep **charge vs separation** trends.
- **GC-MC/MD** applications illustrate **Na uptake** behavior in **graphitic** model systems consistent with the article’s **qualitative** transport picture (see figures for density profiles and insertion statistics).
- Discussion ties **intercalation vs pore diffusion** mechanisms to **domain type** within the cathode microstructure model.

## Limitations

- **EEM** charges are **approximate**; authors caution on **long-range charge transfer** artifacts (mitigated somewhat for **alkali + PAH** cases).
- Structural disorder of real **industrial cathodes** is only **coarsely** represented.

For **density profiles**, **insertion statistics**, and **move probabilities** in **GC-MC/MD**, use **`papers/ReaxFF_others/Hjertenaes_PCCP_2016_Na_graphite.pdf`** / **SI** rather than this summary alone.

## Relevance to group

**ReaxFF parameterization** for **Na + graphitic carbon** overlaps thematically with **battery interface** and **carbon wear** interests; complements **Li-focused** ReaxFF lines elsewhere in the corpus.

## Citations and evidence anchors

- DOI: [10.1039/c6cp06774c](https://doi.org/10.1039/c6cp06774c) — *Phys. Chem. Chem. Phys.* **18**, 31431–31440 (2016).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
