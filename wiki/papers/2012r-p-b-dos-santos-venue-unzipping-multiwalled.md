---
id: paper:2012r-p-b-dos-santos-venue-unzipping-multiwalled
type: paper
title: "On the unzipping of multiwalled carbon nanotubes"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:reactive-md
  - keyword:nve-simulation
source_refs: []
doi: "10.1088/0957-4484/23/46/465702"
year: 2012
authors:
  - "dos Santos, R. P. B."
  - "Perim, E."
  - "Autreto, P. A. S."
  - "Brunetto, Gustavo"
  - "Galvão, D. S."
venue: "Nanotechnology"
pdf_sha256: "171ef081ca5956d81d749c4e533bbf56fac07d0aa6b455c1e6f8fe2c4b37f016"
pdf_path: "papers/ReaxFF_others/dosSantos_CNT_unzipping_Nanotechnology_2012.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2012r-p-b-dos-santos-venue-unzipping-multiwalled -->

## Summary

**Unzipping** **multiwalled carbon nanotubes** into **graphene nanoribbons** is an experimental motif with multiple proposed mechanisms, but **atomic-scale** insight into how **cracks** choose pathways through **nested** walls remains valuable. This **Nanotechnology** article reports fully **atomistic** **ReaxFF** **MD** of **multiwalled CNTs** subjected to **mechanical stretching**, analyzing **chirality-dependent** fracture and **stress** patterns. The abstract introduces **“crests”**—localized, high-curvature, partially unzipped regions nucleated from **defects**—as structural features that can **guide** unzip pathways and help explain why experiments sometimes show a **single dominant cut** despite many potential defect sites. The study is part of the Brazilian **nanocarbon mechanics** line led by **Galvão** and collaborators, adjacent to broader **graphene** and **CNT** reactive mechanics literature. Conceptually, the work links **macroscopic** **unzipping** observations to **defect-mediated** stress concentrations: even when many defects exist, **crests** can channel fracture into **few dominant** pathways, which helps rationalize **anisotropic** cut lines seen in some experiments. The **chirality** dependence further connects to **electronic** and **mechanical** anisotropy intrinsic to **CNTs**, beyond a purely isotropic continuum fracture picture. For retrieval, pair this note with other **nanocarbon mechanics** entries that emphasize **strain-rate** and **defect** sensitivity in **ReaxFF** simulations. Stress and failure timelines should be read from the **Nanotechnology** PDF, not inferred here.

## Methods


Simulations use **ReaxFF** for **carbon** chemistry with **multiwalled** tubes spanning **armchair**, **zigzag**, and **chiral** families (radii and wall counts per **Section 2**). **Mechanical loading** clamps selected **rim** atoms and displaces them along the **tube** axis at **constant speed** (**v = 0.001 Å/fs** in the main tests reported), with **low-temperature** **~300 K** **NVE** runs in regimes that emphasize **stress structure** over thermal noise. Typical fracture runs last **10–20 ps**. **Stress** analysis uses the **von Mises** invariant built from the **deviatoric** stress tensor derived from **atomic forces**. Supplementary media referenced by the journal provide additional trajectories.

### MD application (ReaxFF unzipping)

**Engine / code:** **Fully atomistic molecular dynamics** with **ReaxFF** (`normalized/extracts/2012r-p-b-dos-santos-venue-unzipping-multiwalled_p1-2.txt`); **N/A —** standalone program name not recovered from the indexed excerpt—verify **`pdf_path`**.

**System size & composition:** **Multiwalled** **carbon nanotubes** spanning **armchair**, **zigzag**, and **chiral** families; radii and wall counts per **Section 2** of **`pdf_path`**.

**Boundaries / periodicity:** **N/A —** explicit **PBC** vs free-end treatment not recovered from the indexed excerpt; verify **`pdf_path`**.

**Ensemble:** **NVE** production dynamics after preparation in a **~300 K** regime that emphasizes **stress** structure over thermal noise (per the article’s stated motivation).

**Timestep:** **N/A —** not recovered from the indexed excerpt; verify **`pdf_path`**.

**Duration / stages:** **10–20 ps** fracture runs as summarized on this page; staging/equilibration details in **`pdf_path`**.

**Thermostat:** **N/A —** **NVE** protocol implies no stochastic thermostat; any preparatory thermalization is **N/A —** not excerpted here.

**Barostat / pressure control:** **N/A —** **NPT** barostat not stated for these tensile **NVE** runs.

**Temperature:** **~300 K** nominal conditions for the quoted **NVE** tests.

**Pressure / stress:** **Mechanical stress** from **constant-speed** axial displacement (**\(v = 0.001\) Å/fs** in the main tests summarized on this page) plus **von Mises** diagnostics from **atomic forces** (see article).

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not used.

### Force-field training

**N/A —** applies published **carbon** **ReaxFF** parameters for **mechanical** fracture/unzipping (see references in **`pdf_path`**) rather than reporting a new parametrization in this article.

## Findings

**Outcomes / mechanisms:** **Chirality** controls **crack path** and **von Mises** stress patterns, distinguishing **armchair** versus **zigzag** versus **chiral** responses. **Linear atomic chains** appear frequently during **zigzag**/**chiral** unzip pathways in the simulations described. **Random defect ensembles** develop **high-curvature crests** that **focus** unzip trajectories, offering a mechanistic rationale for **dominant linear** cuts observed experimentally even when many defects could nucleate independent fractures.

**Comparisons:** Simulation morphology is discussed relative to experimental **unzipping** motifs that often show nearly linear cuts despite abundant defects.

**Sensitivity / design levers:** **Chirality**, **defect** density, and **mechanical** loading rate (**Å/fs** scale) steer whether **crests** nucleate and how unzip pathways coalesce.

**Limitations / outlook:** **ReaxFF** carbon chemistry and high **strain-rate** **MD** timescales limit direct experimental mapping; quantitative barriers belong in the **PDF**/SI.

**Corpus / KB honesty:** Grounded in **`pdf_path`** and `normalized/extracts/2012r-p-b-dos-santos-venue-unzipping-multiwalled_p1-2.txt` (mostly abstract/intro pages); later sections and SI hold definitive numerical diagnostics.

## Limitations

**ReaxFF** accuracy for strained **sp\(^2\)** carbon; **strain rates** and **timescales** exceed typical experiment; extract-backed notes may omit later sections.

## Relevance to group

International collaboration line on **nanocarbon mechanochemistry** with **ReaxFF**, comparable audience to other **CNT** reactive mechanics studies.

## Citations and evidence anchors

- DOI [10.1088/0957-4484/23/46/465702](https://doi.org/10.1088/0957-4484/23/46/465702) — *Nanotechnology* **23**, 465702 (2012).
- Extract: `normalized/extracts/2012r-p-b-dos-santos-venue-unzipping-multiwalled_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
