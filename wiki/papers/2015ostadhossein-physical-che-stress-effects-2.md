---
id: paper:2015ostadhossein-physical-che-stress-effects-2
type: paper
title: "Stress effects on the initial lithiation of crystalline silicon nanowires: reactive molecular dynamics simulations using ReaxFF (reduced PDF duplicate)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - material:widegap-semiconductor
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1039/C4CP05198J"
year: 2015
authors:
  - "Alireza Ostadhossein"
  - "Ekin D. Cubuk"
  - "Georgios A. Tritsaris"
  - "Efthimios Kaxiras"
  - "Sulin Zhang"
  - "Adri C. T. van Duin"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "aec5ff1bab44122d9df6fb275cc1d164d0686bddc4b3d71137c73422fe78d38f"
pdf_path: "papers/Ostadhossein_PCCP_LiSi_2014_reduced.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015ostadhossein-physical-che-stress-effects-2 -->

??? info "PDF variant"
    **Reduced** PDF duplicate. Full figures and pagination: [[2015ostadhossein-physical-che-stress-effects]] (`papers/Ostadhossein_PCCP_LiSi_2014.pdf`). See also NON_PRIMARY list: proof sibling `2014ostadhossein-venue-rsc-cp`.

## Summary

This slug registers a **reduced-page** PDF copy `papers/Ostadhossein_PCCP_LiSi_2014_reduced.pdf` of the PCCP article DOI `10.1039/C4CP05198J`, “Stress effects on the initial lithiation of crystalline silicon nanowires: reactive molecular dynamics simulations using ReaxFF.” The extract (`normalized/extracts/2015ostadhossein-physical-che-stress-effects-2_p1-2.txt`) reproduces the **abstract** and opening **Introduction**: silicon anodes promise high capacity; in situ TEM shows lithiation of crystalline Si nanowires proceeds via migration of the interface between lithiated shell and pristine core with **solid-state amorphization**; and the paper uses **ReaxFF MD** to characterize mechanisms. The abstract states ReaxFF reproduces **Li migration barriers** from **DFT** in both crystalline and amorphous Si; that Li insertion between adjacent **{111}** planes leads to **peeling-off** of {111} facets and amorphization consistent with experiment; that breaking Si–Si bonds between {111} bilayers requires high local Li concentration, explaining a sharp **ACI**; that stress analysis shows **compressive stress** at the ACI layer retarding the front, matching TEM; and that high-temperature lithiation (example **1200 K**) can produce an **amorphous-to-crystalline** transformation near **Li:Si ≈ 4.2:1**. Full figures and any SI pages may be absent compared with [[2015ostadhossein-physical-che-stress-effects]].

## Methods

This slug registers only a **reduced-page** PDF duplicate of DOI `10.1039/C4CP05198J`; the **simulation protocol is identical** to **[[2015ostadhossein-physical-che-stress-effects]]** (same **PCCP** article). **Reactive MD** uses **LAMMPS** with **ReaxFF** (**Fan** **Si–Li** parameters) on an **h112** **crystalline Si nanowire** of **~5976 Si atoms** in a **~8.43×9.22 nm²** cross-section with **periodic boundary conditions (PBC)** in-plane, a **Li reservoir**, a **reflective** top boundary, and a fixed **bottom** layer. **Timestep:** **0.25 fs** (**velocity Verlet**). **Thermostat:** **Nosé–Hoover** **NVT** during thermalization (**~10 ps** from **~1 K**, ramp to **600 K** at **0.048 K/fs**, then hold **~2.2 ns** in the equilibration segment described in the paper) with additional **NVE** segments where the article reports **virial stress** at the **amorphous–crystalline interface**. **Production** lithiation uses the **NVE**/**NVT** staging described on **[[2015ostadhossein-physical-che-stress-effects]]** (full segment lengths, **stress** panels, and any **SI** pages live on the canonical **PCCP** PDF, not necessarily in this reduced export). **Temperature (K):** protocols span **cryogenic initialization (~1 K)**, a ramp toward **600 K** during thermalization, **~300 K** lithiation–**stress** analyses at the reaction front, and **~1200 K** high-**temperature** **Li–Si** examples in the abstract. **Barostat / hydrostatic pressure:** **N/A —** constant-volume **nanowire** workflow. **Electric field / metadynamics:** **N/A**.

## Findings

**Mechanisms / outcomes:** the **abstract** on the reduced PDF matches the canonical article: **ReaxFF** reproduces **DFT** **Li** migration barriers in **c-Si** and **a-Si**; **{111}**-channel **Li** insertion drives **peeling**, **amorphization**, and a **sharp amorphous–crystalline interface**; **compressive stress** at that interface can **retard** the reaction **kinetics** of the lithiation front.

**Comparisons:** trends are discussed relative to **in situ TEM** observations of **Si** nanowire lithiation and relative to **DFT** barrier benchmarks in the **PCCP** article.

**Sensitivity:** behavior depends strongly on **temperature** (room-temperature **stress**-limited fronts versus **~1200 K** pathways) and on **Li:Si** loading (example **amorphous→crystalline** **Li–Si** transition near **Li:Si ≈ 4.2:1** at high **temperature** in the abstract).

**Limitations / outlook:** this slug’s **duplicate PDF** may omit figures or **SI** pages; quantitative **stress** fields and barrier tables should be read from the **version-of-record** file on **[[2015ostadhossein-physical-che-stress-effects]]**, not from cropped **proof**/**reduced** exports.

## Limitations

Reduced PDFs may omit pages present in the primary file; always prefer `papers/Ostadhossein_PCCP_LiSi_2014.pdf` for complete content.

## Relevance to group

Duplicate **PDF** registration for the same **PCCP** article; use **[[2015ostadhossein-physical-che-stress-effects]]** for figures, **SI**, and pagination when citing quantitative **stress** or **ACI** data.

## Reader notes (navigation)

- [[2015ostadhossein-physical-che-stress-effects]]
- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]

## Citations and evidence anchors

DOI: [10.1039/C4CP05198J](https://doi.org/10.1039/C4CP05198J)
