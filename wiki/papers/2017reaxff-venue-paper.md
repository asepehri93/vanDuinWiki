---
id: paper:2017reaxff-venue-paper
type: paper
title: "Development of a Transferable Reactive Force Field of P/H Systems: Application to the Chemical and Mechanical Properties of Phosphorene (workflow PDF)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:2d-layered
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.7b05257"
year: 2017
authors:
  - "Hang Xiao"
  - "Xiaoyang Shi"
  - "Feng Hao"
  - "Xiangbiao Liao"
  - "Yayun Zhang"
  - "Xi Chen"
venue: "The Journal of Physical Chemistry A (manuscript export; see sibling for VOR PDF)"
pdf_sha256: "4a7a8e36514e87c30f2566f557fe6bee8d229a8aceac5daedd08c0da85412079"
pdf_path: "papers/ReaxFF_others/ReaxFF_Phosphorus.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2017reaxff-venue-paper -->

This corpus PDF is an **ACS Paragon Plus / manuscript-style** export for the *J. Phys. Chem. A* article on **ReaxFF parametrization for phosphorus and hydrogen** and applications to **phosphorene**. The curated bibliography and cleaner figures live with **`[[2017xiao-venue-research]]`** (`papers/ReaxFF_others/Xiao_ReaxFF_Phosphor_2017.pdf`). The summary below duplicates that article-level account so this slug remains scientifically self-contained.

## Summary

The peer-reviewed work develops ReaxFF parameters for P/H systems to describe black phosphorene and related phosphorus hydrides and clusters, using global optimization against ab initio reference data. A \(60^\circ\) correction term improves energetics for phosphorus clusters relative to baseline bond-order expressions. Mechanical benchmarks compare ReaxFF to a Stillinger–Weber nonreactive model for defective phosphorene, and the authors explore thermal stability motifs including nanotubes. A preliminary P/H/O/C extension is introduced toward oxidized phosphorene and van der Waals heterostructures. ReaxFF substantially improves elastic and failure behavior versus the SW baseline for pristine and defective sheets, including counterintuitive sensitivity of failure to single versus double vacancies and orientation-dependent defect sensitivity.

## Methods

This slug is a **manuscript / Paragon-style export** (`papers/ReaxFF_others/ReaxFF_Phosphorus.pdf`) for the same peer-reviewed article curated as **[[2017xiao-venue-research]]** (*J. Phys. Chem. A*, DOI `10.1021/acs.jpca.7b05257`). Methods below mirror that **canonical** page; **`extraction_quality: partial`** here reflects workflow cover pages rather than missing science.

### 1 — MD application (atomistic dynamics)

**Reactive MD** exercises the fitted **P/H** (**and preliminary P/H/O/C**) **ReaxFF** on **phosphorene sheets**, **defective** supercells, **nanotubes**, and **mechanical** test geometries described in **[[2017xiao-venue-research]]** (uniaxial loading, thermal ramps, etc.).

- **Engine / code:** **ReaxFF MD** as implemented in the **J. Phys. Chem. A** article (engine name on canonical PDF).
- **System size & composition:** **Phosphorus** nanostructures ranging from **clusters** to **extended sheets** and **tubes**—exact **atom counts** per figure are on **[[2017xiao-venue-research]]**.
- **Boundaries / periodicity:** **3D periodic** supercells for extended **phosphorene** models unless a finite cluster study is noted in the article.
- **Ensemble / thermostat / barostat:** **N/A on this stub** — use the **canonical** wiki + PDF for **NVT/NPT** choices, **thermostat** labels, and any **stress-control** barostat used in mechanical tests.
- **Timestep / duration:** **N/A on this stub** — confirm **Δt** and trajectory lengths on **[[2017xiao-venue-research]]**.
- **Temperature / pressure:** **Hot** segments appear for **thermal stability** and **mechanical** failure tests; numeric **T**/**P** schedules are tabulated in the article, not duplicated here.
- **Electric field:** **N/A** — not a field-study paper.
- **Replica / enhanced sampling:** **N/A** — brute-force **ReaxFF MD** within the reported windows.

### 2 — Force-field training

**Global optimization** of **ReaxFF** parameters for **P/H** (extension toward **P/H/O/C**) against **QM** training sets covering **bulk P**, **blue phosphorene**, **edges**, **hydrides**, and **clusters**, including a **60°** correction term for **P-cluster** energetics as described in **[[2017xiao-venue-research]]**; **QM program / functional / basis** choices are listed there.

### 3 — Static QM / DFT-only

**DFT** (and related **QM**) data supply **training energies/forces**; **DFT MD** is **not** the production dynamics engine.

## Findings

### Outcomes and mechanisms

The refit **ReaxFF** improves agreement with **QM** benchmarks for **P/H** chemistries highlighted in the article and yields **mechanical** responses for **defective phosphorene** that outperform a **Stillinger–Weber** baseline in the authors’ tests, including **counterintuitive** sensitivity of **failure** to **single vs double vacancies** tied to **local failure modes** rather than defect formation energy alone.

### Comparisons

**ReaxFF vs Stillinger–Weber** comparisons on **elastic** and **failure** observables, plus **QM** training residuals, anchor the claimed accuracy gains.

### Sensitivity / design levers

**Defect type**, **crystallographic orientation**, and **temperature** modulate **reactivity** and **mechanical** failure sequences; the **P/H/O/C** extension is presented as a **first step** toward **oxidized** phosphorene and **vdW heterostructure** simulations.

### Limitations and corpus honesty

Prefer **[[2017xiao-venue-research]]** for **citation-ready** figures and **hashes**; this export may carry **banner**/**typesetting** artifacts. **Transferability** outside the **training manifold** (liquids, electrolytes, heavy oxidation) still requires explicit validation as the authors note.

## Limitations

Confidentiality banner text may appear in this export; prefer the sibling PDF for citation-ready figures. Transferability to liquid-electrolyte or heavily oxidized environments needs explicit testing.

## Relevance to group

Duplicate ingest of the **phosphorene ReaxFF** line; **`[[2017xiao-venue-research]]`** remains the preferred navigation target for operators seeking a single canonical file hash.

## Citations and evidence anchors

- Peer-reviewed article: [[2017xiao-venue-research]] — DOI [10.1021/acs.jpca.7b05257](https://doi.org/10.1021/acs.jpca.7b05257).

## Reader notes (navigation)

- **Canonical article page:** [[2017xiao-venue-research]].

## Related topics

- [[reaxff-family]]
- [[2017xiao-venue-research]]
