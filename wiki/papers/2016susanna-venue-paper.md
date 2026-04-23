---
id: paper:2016susanna-venue-paper
type: paper
title: "Supporting Information: Quantum Mechanics Calculations for Parametrizing PNA–Gold (related JCTC work)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - method:hybrid-qmmm
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2016
authors:
  - "Xin Li"
  - "Vincenzo Carravetta"
  - "Cui Li"
  - "Susanna Monti"
  - "Zilvinas Rinkevicius"
  - "Hans Ågren"
venue: "Supporting Information (ACS JCTC companion)"
pdf_sha256: "f62f97b7a105f5f1e97e6754d1784853a11d82bf19678a0101d57e727aa9b910"
pdf_path: "papers/ReaxFF_others/Li_Monti_Au_peptide_acs.jctc.2016_SI.pdf"
extraction_quality: "partial"
group_affiliation: false
paper_keywords:
  - keyword:supporting-information
  - keyword:qm-training-data
  - keyword:dft-static
---
<!-- id:paper:2016susanna-venue-paper -->

## Summary

**PNA–metal** interfaces matter for **biosensing** and **nanoparticle** functionalization because **charge transfer** and **geometry** jointly set **optical** response; **QM** benchmarks are typically required before **classical** models can be trusted across **adsorption** motifs. **`papers/ReaxFF_others/Li_Monti_Au_peptide_acs.jctc.2016_SI.pdf`** is **Supporting Information** for a *J. Chem. Theory Comput.* article on **optical properties** of **gold nanoclusters** functionalized with an **organic conjugate** (see **`[[2016xin-li-j-chem-theor-ct6b00283]]`**). The SI opens with **“Quantum Mechanics Calculations Used to Parametrize the Interaction of PNA with the Gold Atoms of the Surface,”** signaling that its core content is **QM reference data**—**energies**, **geometries**, and **spectroscopy-related** quantities—used to build or validate **hybrid quantum–classical** models for **peptide nucleic acid (PNA)** on **Au** surfaces.

## Methods

**1 — MD application.** **N/A —** this PDF is **Supporting Information** for **QM calculations** feeding a **hybrid quantum–classical** model in **`[[2016xin-li-j-chem-theor-ct6b00283]]`**; it does not define a standalone **production MD** protocol on this page.

**2 — Force-field / hybrid parametrization (SI role).** The SI opens with **“Quantum Mechanics Calculations Used to Parametrize the Interaction of PNA with the Gold Atoms of the Surface,”** documenting **DFT** (or related **QC**) **levels of theory**, **basis sets**, and numerical settings used to build **training** points for **PNA–Au** interactions. Expect **total-energy** scans along **adsorption** coordinates, **Au** **cluster**/**facet** models with **PNA** fragments, and **optical**-related **QM** settings where applicable—full tables are only in **`pdf_path`** (`extraction_quality: partial`).

**3 — Static QM / DFT.** The SI **is** primarily **QM** input documentation for the parent **JCTC** workflow described in **`[[2016xin-li-j-chem-theor-ct6b00283]]`**.

## Findings

**Role of the SI.** The file makes **QM convergence** and **benchmark** numbers **inspectable** for readers auditing how **PNA–Au** interactions are encoded before use in the **hybrid** model of **`[[2016xin-li-j-chem-theor-ct6b00283]]`**. The parent article optimizes classical **metal–PNA** parameters against this **DFT** training set and validates the model against **QM** benchmarks (and experiment-oriented checks where reported). It is **not** a standalone **results** article: **figures and tables** support parent claims about **parametrization** quality and **optical** assignments.

Cite the **version-of-record** parent work (**`[[2016xin-li-j-chem-theor-ct6b00283]]`**) for scientific conclusions; use **`pdf_path`** for complete **QM** tables (`extraction_quality: partial`). The SI is a **QM** training appendix; limitations include **cluster** models of **Au** and truncated **PNA** fragments.

## Limitations

**`doi`** is absent here because the SI is not separately DOI’d; cite the **parent article**. **`extraction_quality: partial`** in the manifest—use the **PDF** as authority. Treat as **non-primary** SI per `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`.

**Confidence rationale:** `med`—SI pointer; detailed QM claims require parent PDF.

## Reader notes (navigation)

**Hybrid** **QM/MM** workflows for **metal–organic** interfaces share **training-data** practices with **ReaxFF** development even when the **classical** region is not **ReaxFF**; compare SI **tables** with **`[[taxonomy/paper_keywords.yml]]`** **keywords** when tagging. **Primary article:** [[2016xin-li-j-chem-theor-ct6b00283]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

If **ACS** updates **SI** **hosting** URLs, update **`pdf_path`** only through a **controlled** corpus migration while preserving **`pdf_sha256`** provenance rows in **`raw/MANIFEST.jsonl`**. [[2016xin-li-j-chem-theor-ct6b00283]]
