---
id: paper:2021akbarian-j-chem-phys-atomistic-scale-insight
type: paper
title: "Atomistic-scale insight into the polyethylene electrical breakdown: An eReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - material:polymer-organic
  - method:ereaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/5.0033645"
year: 2021
authors:
  - "Dooman Akbarian"
  - "Karthik Ganeshan"
  - "W. H. Hunter Woodward"
  - "Jonathan Moore"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys. 154:024904 (2021)"
pdf_sha256: "632c88d5b7e60ec90b5cbc17b824924a25b6bcc4b5449a1f783514b3252ae1d2"
pdf_path: "papers/Akbarian_JCP_2020_eReaxFF.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021akbarian-j-chem-phys-atomistic-scale-insight -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

An **eReaxFF** (explicit electron) MD framework, checked against DFT references in the paper, probes time-dependent dielectric breakdown in polyethylene, including effects of density, voids, and XLPE-related by-products such as acetophenone. Higher PE density increases time-to-breakdown in the simulations; adding electron-affine byproducts like acetophenone can shorten TDDB. During breakdown, electron transport localizes through void channels between electrodes; the acetophenone radical anion strongly shifts secondary reaction energetics versus neutral acetophenone.

## Methods

### A — Force-field training / fitting (ReaxFF and related)

- **eReaxFF:** **Molecular dynamics** with an **explicit electron** description within the authors’ **eReaxFF** framework (see the article for the formulation and how it extends **ReaxFF**-style reactive modeling to electronic degrees of freedom).
- **Verification:** The abstract states the framework is **verified against density functional theory data**; full **QM** settings and benchmarks are in the primary paper.

### B — Molecular dynamics, experiments, protocols, and sampling

- **Framework:** **eReaxFF-based MD** used to study **time to dielectric breakdown (TDDB)** in **polyethylene (PE)**, varying **processing** variables called out in the abstract—**density** and **voids**—and **XLPE by-products** such as **acetophenone**.
- **Observables:** **TDDB** trends vs **density** and additives; **electron** migration pathways during **electrical breakdown** (**void**-channel transport from **anode** to **cathode** in the abstract’s summary).
- **MD protocol (full list):** **N/A** in this short note to transcribe every **LAMMPS**-style line; the peer-reviewed file gives **eReaxFF** **MD** with **inter-electrode** **electric** **field** / **bias** protocols for **TDDB**, with **3D** **PBC** **polyethylene** **supercells** (full **atom** **counts** in the **article**), **NVT** or **NVE** segments as reported, **fs**-scale **timestep**, **K**-scale **temperatures**, and **ps**/**ns** trajectory segments (see **pdf_path** for **thermostat**/**barostat**, and **isotropic** **1 bar** **NPT** only if the authors use **pressure** **control**). **Umbrella** / **metadynamics** / **replica** exchange—**N/A** unless the **SI** says otherwise.

### C — Electronic structure / static QM (when reported separately from MD)

- **DFT:** The abstract reports **DFT** data used to **verify** the **eReaxFF** electronic treatment; standalone **QM** benchmarks and convergence settings belong in the primary **J. Chem. Phys.** text and tables.

### D — Review scope, SI/galley notes, and non-primary corpus roles

- **Not applicable:** primary research article.

## Findings

- **Density:** The abstract reports that **increasing PE density increases TDDB** in their simulations.
- **Acetophenone:** Adding a **by-product with positive electron affinity** such as **acetophenone** can **reduce TDDB** relative to the scenarios compared in the abstract.
- **Breakdown path:** During **electrical breakdown**, **electrons** tend to **migrate through voids** when transferring from **anode** to **cathode**.
- **Radical anion chemistry:** Compared with **neutral acetophenone**, the **acetophenone radical anion** can **significantly reduce** the **energy barrier** and **reaction energy** of **secondary chemical reactions** in their analysis. **Comparisons** in the main text are primarily **eReaxFF** vs **DFT** for electronic/reaction data referenced there. **Sensitivity** of **TDDB** to **density**, **void** connectivity, and **additives** is the main axis in the **abstract**-level summary. For **citable** run parameters, use the **version-of-record** **PDF** at `pdf_path`.

## Limitations

System sizes and timescales remain below real cable insulation; eReaxFF approximations apply.

## Relevance to group

Shows group direction on polarizable/explicit-electron extensions of ReaxFF for dielectric polymers—adjacent to high-voltage materials and electronics applications.

## Citations and evidence anchors

`papers/Akbarian_JCP_2020_eReaxFF.pdf` — abstract (TDDB trends, void paths, acetophenone). https://doi.org/10.1063/5.0033645

## Related topics

- [[2021itai-leven-j-chem-theor-recent-advances]]
- [[reaxff-family]]
