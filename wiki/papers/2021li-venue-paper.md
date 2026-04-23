---
id: paper:2021li-venue-paper
type: paper
title: "Supporting information: Revealing the chemical reaction properties of SiHCl3 pyrolysis by ReaxFF molecular dynamics (related article, ACS Omega)"
updated: "2026-04-20"
confidence: low
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-parameterization
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: ""
year: 2022
authors:
  - "Yanping Li"
  - "Dazhou Yan"
  - "Tao Yang"
  - "Guosheng Wen"
  - "Xin Yao"
venue: "ACS Omega (main article); this PDF is Supporting Information"
pdf_sha256: "fb323439ec76ee4fc257cb2ad0b903b035a936935a7e09db021e587af176598c"
pdf_path: "papers/ReaxFF_others/Li_SiClH_ACS_Omega_2022_SI.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2021li-venue-paper -->

## Summary

This wiki slug registers **Supporting Information** (`papers/ReaxFF_others/Li_SiClH_ACS_Omega_2022_SI.pdf`) for an **ACS Omega** study of **trichlorosilane (SiHCl₃)** **pyrolysis** using **ReaxFF molecular dynamics**, authored by **Yanping Li** *et al.* The SI’s primary scientific payload is **reproducibility**: it publishes the **full `ffield.reax` table** for the **Si–Cl–H–C** parameterization used in production runs, with parameters sourced from the **multi-objective ReaxFF optimization framework** of **Jaramillo-Botero**, **Naserifar**, and **Goddard** (*J. Chem. Theory Comput.* **2014**, **10**, **1426–1439**) as stated in the SI header. The **main article** (not ingested as this file) carries the **narrative** **Summary**, **simulation** **protocols**, **validation** against reference data, and **pyrolysis** **mechanism** discussion; this page should not be read as a standalone scientific result.

## Methods

### 1 — MD application (atomistic dynamics)

The ingested `pdf_path` is **Supporting Information**; **molecular dynamics** in the *ACS Omega* **main** article (not in this file) is ReaxFF-based, typically **LAMMPS** in this literature line—confirm the VOR. **N/A in this PDF** for supercell composition / atom count, 3D PBC details, NVT or NPT choice, **timestep (fs)**, equilibration **duration** or **ns**-scale production, **thermostat** (Berendsen / Nosé–Hoover / Langevin), isotropic NPT **barostat**, target **temperature** in **K**, or bulk **pressure** in **bar** or **GPa**—all belong to the main article, not the SI. **N/A** for static or oscillating **electric field** and **N/A** for **umbrella** or **metadynamics**; **N/A** for a separable “Methods” run table in the SI, which is parameter-only. This slug exists so operators can find `ffield.reax` bytes, not a simulation protocol.

### 2 — Force-field training (ReaxFF and related)

The SI publishes the full **`ffield.reax`** for the **Si–Cl–H–C** set used in the work. The header cites the **multi-objective ReaxFF** optimization framework of Jaramillo-Botero, Naserifar, and Goddard (*J. Chem. Theory Comput.* **2014**, 10, 1426–1439) as the **lineage** for how parameters were obtained; **parent** / **element** **blocks** are the tables in the SI. **Training / QM** details: follow that **JCTC** 2014 reference and any **reoptimization** / **editing** **notes** in the **main** *Omega* paper—**N/A** to re-derive from the SI file alone. **External validation** of the fit against experiment or DFT: **N/A** on this page—stated in the main article if present in the ingested **corpus** copy.

### 3 — Static QM

**N/A** in the SI for standalone **DFT** **methods**; QM enters **ReaxFF** **training** **citations** in the main text.

## Findings

**N/A** for a standalone **kinetic** **/ mechanistic** **conclusion** **(SI-only):** the SI’s **payload** is the **ReaxFF** **parameter** **file**; **reaction** **outcomes** and **validation** are on the **main** **article** (not this PDF). **Corpus / KB honesty:** treat `pdf_path` as provenance for the `ffield.reax` table; reaction outcomes and kinetics are in the main *Omega* article, not in this SI PDF. **Comparisons / limitations:** N/A to summarize without the VOR main article in the working tree.

## Limitations

The repository currently tracks **SI** **only** (`doi` empty in frontmatter); **full** **methods** and **results** require the **main** **ACS Omega** PDF. **`extraction_quality: partial`** reflects **PDF** state and **manifest** completeness, not a judgment on the underlying research.

## Relevance to group

Illustrates corpus practice: SI PDFs register parameters and provenance for ReaxFF applications in chlorosilane pyrolysis.

## Citations and evidence anchors

- `ffield.reax` listing: Supporting Information of the ACS Omega article cited in the main publication.

## Related topics

- [[reaxff-family]]
