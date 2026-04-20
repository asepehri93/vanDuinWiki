---
id: paper:2014sen-nat-oxidation-assisted-ductility
type: paper
title: "Oxidation-assisted ductility of aluminium nanowires"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
  - scale:atomistic
source_refs: []
doi: "10.1038/ncomms4959"
year: 2014
authors:
  - "Fatih G. Sen"
  - "Ahmet T. Alpas"
  - "Adri C.T. van Duin"
  - "Yue Qi"
venue: "Nature Communications 5, 3959 (2014)"
pdf_sha256: "c7b5990da8e42e29f42ca4cb75fcf5ab8313e3bd581718a541b08bd06afdc19b"
pdf_path: "papers/Sen_Nature_Comm_2014.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2014sen-nat-oxidation-assisted-ductility -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

Oxidation changes the mechanics of high surface-to-volume aluminium nanowires (NWs). Using **ReaxFF** reactive molecular dynamics, Sen *et al.* argue that an amorphous oxide shell can **increase** apparent ductility of the metallic core: the shell lowers the stress needed to nucleate dislocations in aluminium by increasing activation volume and the number of nucleation sites, while the shell itself can show **superplastic**-like flow when oxygen diffusion heals broken Al–O bonds below a critical strain rate. They connect simulations to experimental hints from hot forming (oxide-rich NW debris with core–shell structure) and emphasize the coupled roles of **oxidation rate** and **mechanical strain rate** for nanoscale devices and larger-scale deformation at interfaces.

## Methods

- **Reactive MD (ReaxFF)** with charge transfer between aluminium and oxygen, applied to oxidized single-crystal Al NW models formed in high-pressure O\(_2\) at scaled room temperature, followed by tensile deformation at multiple strain rates in vacuum versus oxygen.
- Experimental motivation from **TEM** of debris from hot stamping of AA5083 on steel, used to motivate core–shell NW morphology as a simulation starting point.

## Findings

- Oxidation is predicted to **enhance** Al NW ductility relative to the vacuum-deformed case described in the introduction framing.
- The **oxide shell** is associated with lower dislocation nucleation stress in the core via larger activation volume and more nucleation sites.
- **Superplastic-like** response of the amorphous oxide is attributed to viscous flow enabled by **oxygen diffusion** repairing Al–O bond scission when the strain rate stays below a critical value relative to oxidation.
- The manuscript develops a picture where **MD strain rates** and **simulated oxidation rates** are scaled to preserve ratios relevant to experiment despite orders-of-magnitude acceleration inherent to atomistic oxidation MD.

## Limitations

- Atomistic strain rates and oxygen uptake rates remain far above laboratory values; the study relies on **scaling arguments** to relate simulated oxidation/strain-rate ratios to experiment.
- Extract on disk covers early pages only; quantitative stress–strain tables, extended sensitivity analysis, and full methods detail require the **full PDF**.

## Relevance to group

Adri C. T. van Duin is a co-author; the work showcases **ReaxFF** for environmentally coupled **metal/oxide** mechanics at the nanoscale, aligned with reactive MD parameterization and application threads in the group’s broader portfolio.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1038/ncomms4959](https://doi.org/10.1038/ncomms4959)

## Related topics

- [[reaxff-family]]
