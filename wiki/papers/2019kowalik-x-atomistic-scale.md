---
id: paper:2019kowalik-x-atomistic-scale
type: paper
title: "Atomistic Scale Analysis of the Carbonization Process for C/H/O/N-Based Polymers with the ReaxFF Reactive Force Field"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:application
  - material:polymer-organic
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:reactive-md
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcb.9b04298"
year: 2019
authors:
  - "Malgorzata Kowalik"
  - "Chowdhury Ashraf"
  - "Behzad Damirchi"
  - "Dooman Akbarian"
  - "Siavash Rajabpour"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. B"
pdf_sha256: "beada20388c9385eca5c309728e4fc941db32055fb11cd3690fe537eebac48a9"
pdf_path: "papers/Kowalik_JPCB_2019_CHON_polymer_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019kowalik-x-atomistic-scale -->

## Summary

**Carbonization** converts **polymer** precursors into **carbon fibers**; **graphitic** domains that emerge during heating strongly influence **mechanical properties**. The **J. Phys. Chem. B** article reports an improved **ReaxFF** parameterization for **C/H/O/N** chemistry trained against **density functional theory** data, with particular focus on **N\(_2\)** formation **kinetics** and interactions of **N\(_2\)** with **polymer-associated radicals** formed during carbonization—extending prior **C/H/N**-only **ladder PAN** models that could not treat **oxygen**-containing precursors. **Reactive molecular dynamics** then probes **initial-stage** carbonization for three precursors: **idealized ladder polyacrylonitrile (PAN)**, a **modeled oxidized PAN**, and **poly(\(p\)-phenylene-2,6-benzobisoxazole) (PBO)**. The abstract emphasizes resolving **molecular pathways** for **low-molecular-weight** **gas** species and **all-carbon** six-membered **ring** formation, plus **alignment** tendencies of **ring clusters** as prerequisites for further **graphitic** evolution. The corpus PDF filename indicates a **proof**; verify **pagination** against the **version of record** at the DOI. Maintainer catalog: `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`.

## Methods

### ReaxFF training (A)

**CHON-2019** improves **C/H/O/N** **ReaxFF** using **DFT** training data, emphasizing **N\(_2\)** formation **kinetics** and **N\(_2\)** interactions with **polymer-associated radicals**—extending **C/H/N**-only **ladder PAN** models that cannot treat **oxygenated** precursors. Full training reaction lists and optimization workflow: **JPCB** article + **Supporting Information**.

### Reactive MD protocols (B)

**RMD (B):** **Initial-stage carbonization** of **ladder PAN**, **oxidized PAN**, and **PBO**; **PBC**; **Berendsen thermostat**; **0.25 fs** timestep; **10 K/ps** ramp to **2800 K**; **900 ps** **NVT**; **bond-order cutoff 0.3** (authoritative **tables** on **[[2019kowalik-j-phys-chem-atomistic-scale]]** and **JPCB** **VOR**). **System size (atoms)**: see **SI**/**PDF**. **Barostat:** **N/A** — **NVT** after heat-up. **Pressure / stress / hydrostatic** **GPa** targets: **N/A** — not used (**constant**-**volume** **NVT**). **Electric field / umbrella / metadynamics / replica exchange:** **N/A** — not used.

### Note on this corpus PDF (D)

**Proof** in corpus; use **[[2019kowalik-j-phys-chem-atomistic-scale]]** for **pagination**-stable locators.
## Findings

### Mechanisms

The refined field enables **oxidized PAN** within the same **C/H/O/N** framework as **ladder PAN**. Trajectories resolve **low-molecular-weight gas** pathways (including **N\(_2\)** channels) and **six-membered** **carbon** ring formation with **cluster alignment** trends tied to early **graphitic** ordering. **Precursor-dependent** differences among **PAN** variants and **PBO** are explicit in the **ring**/**gas** statistics.

### Limitations

**Proof** PDF; verify **VOR** for final figure numbering. **Shock** temperatures exceed typical **furnace** ramps—mechanistic insight, not direct **process** **kinetics** mapping.

## Limitations

**Proof-stage** PDF in corpus; verify final **pagination** and any **editorial** changes against the **version-of-record** DOI. **High-temperature** **MD** provides **mechanistic** insight but does not replace **continuum** **furnace** models for **industrial** **carbonization** schedules.

## Relevance to group

Develops group ReaxFF capability for realistic C/H/O/N polymer carbonization beyond C/H/N-only ladder PAN models and connects to carbon-fiber precursor chemistry.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcb.9b04298](https://doi.org/10.1021/acs.jpcb.9b04298)

## Related topics

- [[reaxff-family]]
