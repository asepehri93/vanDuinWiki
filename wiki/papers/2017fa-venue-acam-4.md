---
id: paper:2017fa-venue-acam-4
type: paper
title: "Pyrolysis stage evolutions and reaction mechanisms of coal and lignin revealed by ReaxFF MD"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:gpu-md
candidate_tags: []
source_refs: []
doi: ""
year: 2017
authors:
  - "Xiaoxia Li"
  - "Mo Zheng"
  - "Tingting Zhang"
  - "Fengguang Nie"
  - "Xiaofang Tao"
  - "Zhaojie Xia"
  - "Li Guo"
venue: "2017 International Conference on Coal Science & Technology / 2017 Australia-China Symposium on Energy (Beijing)"
pdf_sha256: "ce832386fb963bfd8e3931e380c40e3dc0c327b33f0d60d86c8a953870e442b1"
pdf_path: "papers/ReaxFF_others/Chinese_Coal_Abstracts/Pyrolysis stage evolutions and reaction mechanisms of coal and lignin revealed by ReaxFF MD.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017fa-venue-acam-4 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the conference materials** identified by `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

## Summary

This conference abstract from the 2017 International Conference on Coal Science & Technology and the 2017 Australia–China Symposium on Energy presents GPU-accelerated ReaxFF molecular dynamics of large molecular models for lignin and Liulin coal pyrolysis, analyzed with automated reaction mining. The authors argue that coal and lignin share structural analogies—cross-linked aromatic units with diverse linkages and substituents—so lignin offers a more tractable surrogate for probing atomistic mechanisms that are difficult to isolate in complex coal. Simulations employ the GMD-Reax code for GPU-enabled ReaxFF dynamics and the VARxMD toolkit to classify bond-breaking and forming events as temperature and time evolve. The van Duin and Goddard ReaxFF lineage is cited explicitly as the underlying reactive model.

## Methods

**A — Force-field training / fitting:** The abstract cites the **van Duin and Goddard ReaxFF** lineage for **coal/lignin** reactive chemistry; it does **not** describe new bond-order or parameter optimization in this conference contribution—treat parameters as the **published** reactive model used in **GMD-Reax**.

**B — Molecular dynamics / reactive sampling:** **GPU-accelerated ReaxFF MD** in **GMD-Reax** on large molecular models (**lignin** ~15,920 atoms; **Liulin coal** ~28,351 atoms) with slow **heat-up** rates stated as **0.4 K/ps** (lignin) and **1 K/ps** or **2 K/ps** (coal). **VARxMD** classifies **bond-breaking and forming** events versus **temperature** and **time**. The indexed conference PDF states **slow heat-up ReaxFF MD** with **NVT** used in related **isothermal** comparisons for Liulin coal (**Figure 1** caption region in the extract) but does **not** spell out **timestep**, **thermostat damping**, or **cutoff** parameters on the pages indexed here—**confirm in the full PDF** at `pdf_path`. **Boundaries / periodicity:** **N/A —** explicit **PBC** wording for these **heat-up** cells is **not** on the indexed pages (likely **3D PBC** for bulk models; verify in-source).

**C — DFT / static QM:** **Not reported** in the abstract-level material used here.

**D — Review / non-simulation framing:** **Conference abstract** (coal science & energy symposium); **not** a methods review—scope is **application** of GPU ReaxFF + automated reaction mining to **pyrolysis staging**.

**Barostat / pressure / electric / enhanced sampling:** **N/A —** **heat-up / NVT** reactive MD framing without **NPT**, **fields**, or **metadynamics**-class sampling described in the indexed excerpt.

## Findings

For lignin, the authors partition initial pyrolysis into three stages. Stage I corresponds to extensive depolymerization dominated by cleavage of α-O-4 and β-O-4 ether linkages. Stage II involves broader linkage cracking together with conversion of propyl chains and methoxy substituents. Stage III is dominated by recombination reactions that produce heavier pyrolyzates containing five-, six-, or seven-membered aliphatic rings. For Liulin coal, they propose an analogous three-stage picture: Stage I as structural activation, Stage IIA and IIB as primary and secondary pyrolysis regimes, and Stage III as recombination-dominated chemistry. They further claim that mesoscale structural evolution can be described in terms of units, linkages, and substituents in the molecular models. These conclusions are presented as conference-level summaries; quantitative barriers and exhaustive species validation are not established from the abstract text alone.

The introduction text reproduced in the conference extract further motivates GPU acceleration and automated reaction analysis by noting that coal pyrolysis involves radical-driven chemistry within exceptionally complex macromolecular architectures, making manual reaction enumeration impractical at the scales targeted by large reactive molecular models. The abstract also frames stage identification through joint analysis of pyrolyzate evolution and the underlying chemistry of linkages, aromatic rings, and substituents as temperature rises.

## Limitations

**Conference abstract**; **quantitative barriers** and **full validation** not established from the extract.

## Relevance to group

References **van Duin / Goddard ReaxFF** in the context of **GPU** **coal/lignin** simulation—useful for **software + application** cross-links.

## Citations and evidence anchors

- No DOI; cite **PDF** path in front matter.

## Reader notes (navigation)

- Conference abstract—confirm details from PDF; GPU coal/lignin: [[theme-pyrolysis-combustion-organics]], [[reaxff-family]].

## Related topics

- [[reaxff-family]]
