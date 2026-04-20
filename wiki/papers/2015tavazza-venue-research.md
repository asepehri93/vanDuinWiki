---
id: paper:2015tavazza-venue-research
type: paper
title: "Molecular dynamics investigation of the effects of tip–substrate interactions during nanoindentation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:reactive-md
  - domain:methods-software
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b01275"
year: 2015
authors:
  - "F. Tavazza"
  - "T. P. Senftle"
  - "C. Zou"
  - "C. A. Becker"
  - "A. C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "516536c5dfd1d863e8a45c341281ccda2a1895fef66f675c22c787a0a8762911"
pdf_path: "papers/Tavazza_JPC_2015_indentor.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015tavazza-venue-research -->

## One-paragraph summary

The paper compares **atomistic nanoindentation** models that differ in how the **indenter interacts** with a **Ni substrate**, moving beyond purely **repulsive spherical indenters** toward **chemically explicit tips** (including **hydrogenated diamond** and **oxidized Ni** scenarios). Reactive and non-reactive treatments are contrasted with **AFM tip-blunting observations** and selected **DFT** references. A central reported trend is **Ni transfer to the tip** under **clean or oxidized** conditions, while **hydrogen termination of the diamond tip** can **suppress or eliminate** transfer—an effect framed as larger than a simple **surface oxide contaminant** story.

## Methods

- **MD nanoindentation** with varying **tip chemistry** (clean, H-terminated, oxide-like).
- Comparisons to **DFT** and **experimental AFM** literature on tip wear and adhesion.

## Findings

- **Material transfer (Ni onto tip)** is pronounced for **clean/oxidized** Ni contacts in the simulations summarized in the abstract.
- **Hydrogen on the diamond tip** strongly mitigates adhesion/transfer relative to the oxide-passivation case in those same comparisons.
- The work argues that **idealized repulsive indenters** can miss **chemomechanical** mechanisms visible in more realistic tip models.

## Limitations

- Scope centers on **model Ni/diamond** interfaces; quantitative transfer rates for other metal/ceramic pairs require separate parameter validation.
- **Finite indentation speeds** and **tip radii** influence outcomes; mapping to AFM time scales is non-trivial.

## Relevance to group

Co-authored **NIST + Penn State** effort connecting **ReaxFF-class reactive modeling** (via van Duin group involvement) to **nanomechanics and tribology** interpretation problems.

## Citations and evidence anchors

- Abstract and Sec. 1 in `papers/Tavazza_JPC_2015_indentor.pdf`; **DOI:** `10.1021/acs.jpcc.5b01275`.

## Related topics

- [[reaxff-family]]
