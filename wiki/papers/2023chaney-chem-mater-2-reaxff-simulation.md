---
id: paper:2023chaney-chem-mater-2-reaxff-simulation
type: paper
title: "ReaxFF Simulation of Pyrolysis Behaviors of Polysiloxane Precursors with Different Carbon Content"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:lammps
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.chemmater.3c00010"
year: 2023
authors:
  - "Harrison Chaney"
  - "Kathy Lu"
venue: "Chemistry of Materials 35, 3902–3910 (2023)"
pdf_sha256: "443bb28ad004299714bcc1d1924579ebb700c3e4ef7273a9e4bf602687d12bb9"
pdf_path: "papers/ReaxFF_others/chaney-lu-2023-reaxff-simulation-of-pyrolysis-behaviors-of-polysiloxane-precursors-with-different-carbon-content.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2023chaney-chem-mater-2-reaxff-simulation -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

## Summary

This Chemistry of Materials article uses LAMMPS molecular dynamics with a ReaxFF reactive potential to simulate pyrolysis of polysiloxane precursors with different carbon content, aiming to quantify atomistic routes from polymer to silicon oxycarbide ceramic products. The authors motivate the study by noting that polymer-derived ceramics are technologically attractive but that experiments often cannot fully resolve atomic-scale bond rearrangements, cluster formation, and domain sizes during conversion. The manuscript states that it is among the first efforts to quantify the atomic evolution of polymer-to-ceramic conversion for the chosen precursors, with emphasis on ceramic composition, yield, bond populations, radial distribution functions, and the sizes of silicon–oxygen-rich versus carbon-rich regions in the final models.

## Methods

### Reactive force field and software (A/B)

- **Potential:** **ReaxFF** for **Si–O–C–H** chemistry in **LAMMPS**.
- **Precursors:** **PDMS**, **PDES**, and **SPR-684 PSO**—spanning different **carbon content** and **side-group** architecture on a **siloxane** backbone.

### Pyrolysis MD protocol (B)

- **System size:** ~**10⁵ atoms** (order-of-magnitude statement in the article), larger than many prior **ReaxFF pyrolysis** benchmarks cited by the authors.
- **Temperature window:** **1500–2100 K** (intended as more **realistic** than some ultra-high-T prior studies).
- **Gas handling:** Periodic removal of small **volatile** molecules using **molecular-weight** / **deletion** rules described in **Methods** (affects final **stoichiometry** if mishandled).

### Analysis

**Ceramic yield**, **elemental composition**, **bond-type** populations, **RDFs**, **cluster** sizes for **Si–O-rich** vs **C-rich** domains, and residual **H** content.

### MD application (integrated)

**Engine / code:** **LAMMPS** with **ReaxFF** for **Si–O–C–H** **pyrolysis**. **System & composition:** order **~10⁵ atoms** and **PDMS** / **PDES** / **SPR-684 PSO** **precursor** **stoichiometry** in *Chemistry of Materials* **Methods**. **PBC** for **3D** **bulk** pyrolysis cells. **Temperature** program: **1500–2100 K** **heating** window (as reported). **Ensemble, timestep, thermostating, total burn-off duration, volatile deletion cadence, barostat, pressure, field, enhanced sampling (metadynamics/REX/umbrella):** **N/A in this short summary**—read the **peer-reviewed** article for the **NVT**/**NVE**-style **stages** and **timestep**/**duration** in **ps/ns**; **N/A — static electric field**; **N/A — enhanced sampling** in the main protocol.

## Findings

### Composition–structure mapping

**Final ceramic** **composition** tracks **initial polymer** **composition**, linking **side-group** chemistry to **carbon retention** and **networking**.

### Carbon networking vs scission

**Carbon-rich** precursors build **C–C** connectivity via loss of **Si–O**, **Si–C**, and **C–H**; **less carbon-rich** precursors may lose **C–H** with limited **C–C** formation in the highlighted stages.

### Domains and RDFs

**Si–O-rich** vs **C-rich** **domains** differ in **size** and connectivity at the **atomic** scale; **RDFs** show more **C–C** bonding at higher **T**, while **C–H** can persist even at **2100 K** and **long-range crystallinity** does not emerge in their models.

### Experimental context (intro)

The article cites **experimental silicon oxycarbide** literature on **Si–C scission** thresholds and **phase separation** at high temperature to motivate **temperature** choices and **RDF** interpretation.

## Limitations

**ReaxFF** accuracy for **siloxane→ceramic** chemistry should be checked against **QM/experiment** where available.

## Relevance to group

**Polymer-derived ceramic** pyrolysis mapped with **ReaxFF** in the **organosilicon** lineage.

## Citations and evidence anchors

- DOI: [10.1021/acs.chemmater.3c00010](https://doi.org/10.1021/acs.chemmater.3c00010)

## Reader notes (navigation)

- Polymer-derived ceramics: [[theme-pyrolysis-combustion-organics]], [[reaxff-family]].

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
