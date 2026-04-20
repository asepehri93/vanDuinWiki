---
id: paper:2016mortazavi-physical-che-mechanical-response
type: paper
title: "Mechanical response of all-MoS2 single-layer heterostructures: a ReaxFF investigation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:reaxff
  - material:tmd
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/c6cp03612k"
year: 2016
authors:
  - "Bohayra Mortazavi"
  - "Alireza Ostadhossein"
  - "Timon Rabczuk"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "caed4a000ddfea887de9455f7b3955885b5eb37abd6210f76e93a87088a14d66"
pdf_path: "papers/Mortazavi_MoS2_PCCP_2016.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2016mortazavi-physical-che-mechanical-response -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF molecular dynamics** is applied to **all-MoS2 single-layer heterostructures** to probe **mechanical response** and **failure mechanisms** under the loading protocols described in the article. The work connects **structural motifs** accessible in **2D hetero-stacking** to **stress–strain behavior**, **fracture**, and **energy dissipation** channels that differ from **homogeneous MoS2** sheets. **PCCP** framing places the study in the **atomistic materials mechanics** literature for **transition metal dichalcogenides**.

## Methods

- **ReaxFF MD** with deformation modes and strain rates specified in the publication (uniaxial / biaxial variants per article sections).
- Structural analysis of **bond rupture** and **defect nucleation** during loading.

## Findings

- The paper reports **heterostructure-dependent** elastic and failure characteristics tied to **interlayer registry** and **local bonding** (see figures for quantitative moduli and critical strains).
- **ReaxFF** enables **bond-breaking** during failure, beyond harmonic **Tersoff-like** descriptions sometimes used for TMDs.

## Limitations

- **ReaxFF MoS2** parameterizations must be checked against **DFT/experiment** for each **new stacking** or **phase** explored.
- **Strain-rate** and **system-size** effects influence **brittle vs ductile** interpretations in MD.

## Relevance to group

Adds a **TMD mechanics** reference using **ReaxFF**, adjacent to the group’s broader **2D materials + reactive simulation** coverage.

## Citations and evidence anchors

- Title/DOI block in `papers/Mortazavi_MoS2_PCCP_2016.pdf`; **DOI:** `10.1039/c6cp03612k`.

## Related topics

- [[reaxff-family]]
