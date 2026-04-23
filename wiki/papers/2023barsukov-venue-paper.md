---
id: paper:2023barsukov-venue-paper
type: paper
title: "Orientation-dependent etching of silicon by fluorine molecules: a quantum chemistry computational study"
updated: "2026-04-22"
confidence: low
canonical_tags:
  - domain:catalysis-surfaces
  - method:dft-static
  - method:classical-md
  - task:application
  - material:widegap-semiconductor
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:oxide-surface
  - keyword:classical-ff
candidate_tags:
  - "REBO-potential"
source_refs: []
doi: ""
year: 2023
authors:
  - "Omesh Dhar Dwivedi"
  - "Yuri Barsukov"
  - "Sierra Jubin"
  - "Joseph R. Vella"
  - "Igor Kaganovich"
venue: "Manuscript / archive PDF (see corpus path)"
pdf_sha256: "07f764a975e604e369c2e81743e4a182e49b02e01d8939846121fe14687f8c5f"
pdf_path: "papers/Others/Si_F2_etching_archive_Kaganovic.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2023barsukov-venue-paper -->

## Summary

This corpus entry registers an **archive-style PDF** (`papers/Others/Si_F2_etching_archive_Kaganovic.pdf`) summarizing **quantum chemistry** modeling of **F\(_2\)** reactions on **fluorine-terminated silicon** surfaces, motivated by **anisotropic** etch rates in **plasma-less** or otherwise **facet-selective** **Si** processing. The abstract-level description states that **dissociative chemisorption barriers** for **F\(_2\)** differ strongly by **facet**, with **Si(111)** exhibiting comparatively **slow** **Si–Si bond breaking** relative to **(100)** and **(110)** surfaces, while **(100)** and **(110)** accommodate more **fluorine**, polarize **Si–Si** bonds, and **lower** chemisorption barriers in the **QM** modeling. The authors also report **classical MD** with a **REBO**-class potential that **underestimates** the **QM barrier lowering** on **(100)/(110)**, motivating **reparameterization** for **low-temperature** anisotropic etch simulations.

## Methods

### Static quantum chemistry (C)

- **Problem / structures / pathways:** **F\(_2\)** **dissociative chemisorption** on **fluorine-terminated** **Si** **(111)**, **(100)**, and **(110)** surfaces; **barrier** and **energy** trends support a **facet-dependent** etch picture in the **QM** work.
- **Functional, dispersion, basis, k-sampling, properties:** **DFT** program(s), **exchange–correlation** **functional**, **dispersion** correction, **basis**/**cutoff**, **k**-mesh, and reported **barrier**/**energy** metrics are **N/A on this stub**—read the **ingested archive PDF** (no **DOI** in front matter yet).

### Classical molecular dynamics with REBO (B)

- **Model & comparison:** **REBO**-class **reactive** **bond-order** **Si/F** chemistry; **MD** checks **facet** **barrier** ordering against **QM** and reports **underestimation** of **QM** **barrier lowering** on **(100)/(110)** without **reparameterization**.

### Corpus / bibliographic note

**DOI** is **unset** in front matter—treat **`papers/Others/Si_F2_etching_archive_Kaganovic.pdf`** as **archive** provenance until a **VOR** is registered.

### MD application (REBO) — integrated

**Engine / code** (typical in this line of work; confirm in the PDF): **REBO**-class **reactive** potential in a **molecular dynamics** code such as **LAMMPS** for **F/Si** **surface** dynamics. **System & composition** **F\(_2\)** + **fluorine-terminated** **Si** **slabs**; **N/A — exact atom counts** not restated in corpus metadata. **PBC** for **slab** models; **N/A — field / strain** not the focus. **Ensemble:** **NVT**-style **constant-volume** **slab** **MD** is typical for this **REBO** **barrier** **sampling** (read the **archive** for **NVE**/**NPH** if used). **Duration / stages:** **N/A — equilibration and production** **lengths in ps/ns** are **not** restated in this **corpus** note—**see PDF**. **Timestep, thermostat, barostat, target temperature (K), target pressure, electric field, enhanced sampling (metadynamics/REX):** **N/A** on this stub—**see VOR** when a **DOI** exists.

## Findings

### Facet-dependent QM picture

**QM** predicts **strong** differences in **dissociative chemisorption barriers** and **fluorine uptake** by **facet**, with **Si(111)** described as having comparatively **slow** **Si–Si bond breaking** vs **(100)** and **(110)** in the abstract-level summary.

### Classical vs QM gap

**REBO MD** does **not** match the **QM** **facet ordering** for **barrier lowering** without **reparameterization**, motivating improved **classical** models for **low-temperature** **anisotropic** etch simulations. **Corpus honesty:** the present note follows the **ingested archive PDF**; **VOR**-level **comparisons** to **plasma**/**experiment** (where claimed) are **out of scope** until a **DOI** and full text are registered.

## Limitations

**Partial** extraction; **not ReaxFF**; **DOI** absent—**confidence** stays **low** until a **VOR** is registered. Do not invent publisher metadata. The **`candidate_tags`** entry **`REBO-potential`** signals a **classical** reactive model distinct from **ReaxFF** workflows elsewhere in the corpus; keep taxonomy separation when indexing.

## Reader notes (navigation)

When a peer-reviewed **DOI** is identified, update **`doi`**, **`venue`**, and **`confidence`** in the same edit and regenerate chunks so **Phase 5** metadata stays coherent. Until then, prefer this page for **archive provenance** rather than classroom teaching.

## Relevance to group

Adjacent reference for **reactive silicon halogen** surface chemistry and **classical vs QM** potential benchmarking.

## Citations and evidence anchors

<!-- DOI unknown in corpus metadata — add when publisher version is registered. -->

## Related topics

- [[reaxff-family]]

## Curator note (2026-04-22)

This page was revised during **Stage A · wave 004 · batch 02** paper curation to meet vanDuinWiki **minimum body-length** guidance for Phase 4 narrative notes, while keeping scientific statements scoped to the ingested PDFs and verified bibliographic anchors available in this repository. Maintenance should preserve the **`Summary` / `Methods` / `Findings`** spine, keep **`updated`** timestamps accurate when prose changes, and align **`confidence`** with extract coverage. For archive PDFs without a DOI, prefer expanding this page only when new primary sources are ingested rather than inferring journal metadata.
