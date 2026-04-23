---
id: paper:2025fazlioglu-yalcin-npj-computat-multi-physics-predictive
type: paper
title: "Multi-physics predictive framework for thermolysis of titanium(IV)-isopropoxide"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - method:dft-static
  - method:enhanced-sampling
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:dft-static
  - keyword:enhanced-sampling
  - keyword:thermal-decomposition
  - keyword:qm-training-data
source_refs: []
doi: "10.1038/s41524-025-01782-4"
year: 2025
authors:
  - "Benazir Fazlioglu-Yalcin"
  - "Cem Sanga"
  - "Irem Erpay"
  - "Dundar Yilmaz"
  - "Adri C. T. van Duin"
  - "Roman Engel-Herbert"
  - "Nadire Nayir"
venue: "npj Computational Materials"
pdf_sha256: "1cd804aebc36836dbb84a3100c71f640167c9dbb3f6f317967612e20da51aac7"
pdf_path: "papers/Yalcin_Nayir_TIPP_npjCompMat_2025.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025fazlioglu-yalcin-npj-computat-multi-physics-predictive -->

## Summary

The study builds a **multi-tier workflow**—**DLPNO-CCSD(T)/B3LYP QM**, **ReaxFF reparameterization** for **Ti/C/O/H** chemistry of **titanium(IV) isopropoxide (TTIP)**, **AMS ReaxFF-MD** sampling of isolated and condensed TTIP scenarios, and **metadynamics** (PLUMED-style enhanced sampling referenced in Methods)—to map **ligand-separation pathways** beyond a sole **β-hydride elimination** picture for **CVD/MBE-relevant** TTIP pyrolysis.

## Methods

- **QM reference:** **DLPNO-CCSD(T)** with **cc-pVTZ** plus **B3LYP/cc-pVTZ** zero-point energies (ORCA), following Eq. (1) in the paper for composite energies.
- **ReaxFF training:** Starting from prior **Ti/C/O/H** ReaxFF sets; refit **Ti–O** bond, **C–O–Ti** / **O–Ti–O** / **Ti–O–H** angles, and **H–C–O–Ti** / **C–O–Ti–O** dihedrals with **Ti–C** and **Ti–H** covalent terms **disabled** (nonbonded only), minimizing squared error to QM pathways for **β-hydride**, **β-X/C–O**, and **β-X/Ti–O** categories.
- **ReaxFF-MD (AMS):** **Molecular dynamics** in **Amsterdam Modeling Suite (AMS)** with **reactive ReaxFF**; **fifty** **replica** **copies** of **isolated TTIP** in **100×100×100 Å\(^3\)** **3D PBC** **periodic** gas boxes (**~O(100) atoms** per **molecule** in each **replica**); **NVT** **ensemble**, **Δt = 0.25 fs**, **Berendsen** **thermostat** (**100 fs** damping); **1×10\(^6\)**-step **equilibration** at **300 K**, **1×10\(^6\)**-step **ramp** to **2000 K**, then **8×10\(^6\)**-step **production** at **2000 K** to accelerate kinetics (experimental **CVD** **700–1300 K**). Additional batches: TTIP with **H**, **H\(_2\)**, **H\(_2\)O**; **25**-molecule **condensed** **cells** with **repeats** as in the **PDF**.
- **Metadynamics:** **PLUMED**-driven **metadynamics** along **C–O** and **Ti–O** **collective variables** (see Methods/Supplement) to obtain **barrier**-linked **kinetics** vs **ReaxFF-MD** counts. **N/A** — static **external electric field**; **N/A** — isotropic **1 bar** **NPT** in the high-**T** **gas** runs summarized (use **NVT**).

## Findings

- First **ligand separation** is mostly **C–O** cleavage (**~74%** of ReaxFF-MD cases), with **~20% Ti–O** cleavage; **β-hydride** elimination accounts for **~38%** of **C–O** subset cases—showing **C–O** scission is not synonymous with **β-hydride** only.
- **β-X** channels (alkyl/alkoxy releases) appear with substantial frequency alongside classical **β-hydride** paths; later ligand removals show shifting dominance between **C–O** and **Ti–O** cleavage, with **Ti–O** episodes often gated to maintain **Ti** valence balance.
- **Metadynamics** and **QM** together rank some **Ti–O** vs **C–O** barriers differently than intuition from simplified β-hydride schemes; **kinetic ratios η(T)** (paper Fig. 11) show temperature-dependent switches in whether **C–O** or **Ti–O** pathways dominate for successive ligand removals.
## Limitations

Accelerated **2000 K** gas-phase MD trades experimental temperatures for observable kinetics; authors note need for **more replicas** to tighten **pre-exponentials** for quantitative **Arrhenius** predictions.

## Relevance to group

**Fazlıoğlu-Yalçın**, **Nayir**, **van Duin**, and collaborators: **multi-physics** **TTIP** **thermolysis** with **QM**, **ReaxFF**, and **metadynamics** for **oxide** **CVD/MBE** contexts.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1038/s41524-025-01782-4](https://doi.org/10.1038/s41524-025-01782-4)

## Reader notes (navigation)

These sections summarize what the checked-in extraction and abstracts support; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter above. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[reaxff-family]]
