---
id: paper:2021verma-venue-paper
type: paper
title: "ReaxFF reactive molecular dynamics simulations to study the interfacial dynamics between defective h-BN nanosheets and water nanodroplets"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - material:hexagonal-boron-nitride
  - domain:water-silica-geo
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:water-interfaces
  - keyword:reactive-md
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1039/d1cp00546d"
year: 2021
authors:
  - "Akarsh Verma"
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "85a5c9c3c762831bee2118b159943757682228ee17de483422da1f519b70564a"
pdf_path: "papers/Verma_PCCP_BN_water_2021_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2021verma-venue-paper -->

## Summary

Hexagonal boron nitride (**h-BN**) nanosheets in realistic devices often contain **vacancy defects** that alter wetting, friction with water, and mechanical failure. The *Phys. Chem. Chem. Phys.* work introduces **ReaxFF** parameters for **B/N/O/H** chemistry so that **bond-order** dynamics can follow **water–defect** interactions beyond fixed-charge models. The graphical abstract in the publisher proof stresses investigation of **vacancy-bearing** **h-BN** exposed to water, including how **interfacial** interactions differ from pristine sheets. Simulated scenarios include **water dissociation** near undercoordinated sites, **nanoconfined** water between stacked sheets, and **nanodroplet** contact behavior versus **pore size** and **temperature**, motivated by membrane and **desalination** contexts where **defect** populations are not negligible.

## Methods

**Corpus PDF.** The checked-in file is a **RSC** **proof/galley**; see **`[[2021verma-physical-che-reaxff-reactive]]`** (typeset **PCCP** PDF) for final **table** and **typography** **numbers**.

**1 — MD application (LAMMPS, ReaxFF).** As on the VOR: **B/N/O/H** **ReaxFF** **molecular dynamics** in **NVT** in **3D** **PBC** **h-BN**+**H₂O** **slabs** with **vacancy** and **pore** models; **timestep** (**fs**), **ps**–**ns** **runs**, **thermostat**, and **temperature** set-points in **K** as in **PCCP** **Methods**. **Barostat** and **N/A** **independent** **isotropic** **pressure** in these droplet/confined **cells**; **N/A** **external** **electric** **field**; **N/A — umbrella** in the highlighted **protocols**.

**2 — Force-field training.** **ReaxFF** **parrex**-like **fit** to **DFT** **reaction** **energies** and **geometries** for **defective** **h-BN**+**water**; **parent** **parameter** set extends prior **B/N** chemistry; **validation** on **pristine** **h-BN** **mechanics**/**wetting**; full **reference** list on **`[[2021verma-physical-che-reaxff-reactive]]`**.

**3 — Experiments. N/A.**
## Findings

Water dissociates near vacancy defects with distinct bonding at undercoordinated **N** versus **B** sites. Under confinement, water organizes into **layers**; fracture under load can **nucleate from vacancy defects**. Upon cooling from high temperature, **intermolecular hydrogen bonding** promotes **water agglomeration** near functionalized pores. **Contact angles** decrease with **increasing temperature** and **larger pore sizes** in the nanodroplet studies reported. The authors relate these observations to possible **desalination** and **underwater** device contexts where stable, adsorption-tunable h-BN membranes are of interest. Taken together, the simulations emphasize that **defect chemistry**—not only **pristine** **hydrophobicity**—sets **interfacial** **speciation** and **mechanical** **failure** precursors when water is present.

**Corpus / comparisons.** Match **any** **quantitative** **claim** to the **VOR** on **`[[2021verma-physical-che-reaxff-reactive]]`**, not this **galley** alone.

## Limitations

The registered PDF is a **publisher proof/galley**; layout and some metadata in the mechanical extract reflect proofing boilerplate. Prefer the **published PCCP** PDF for figure numbering and final wording when available. **RSC** proof extracts in this repository may include **typesetting** **queries** and **graphical** **abstract** **placeholders** that are **not** part of the **final** **article** **body**—operators should **curate** **quantitative** **claims** from the **VOR** **PDF** when accessible.

## Relevance to group

**Adri C. T. van Duin** coauthors; the **B/N/O/H** **ReaxFF** line supports broader **2D** **nitride** and **water-interface** entries in this knowledge base alongside [[reaxff-family]].

## Reader notes (navigation)

- **Corpus catalog (non-primary PDF):** [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) · [local](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (entry **2021verma-venue-paper**)
- [[reaxff-family]]
