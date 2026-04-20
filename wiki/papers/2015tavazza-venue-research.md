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



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The paper compares **atomistic nanoindentation** models that differ in how the **indenter interacts** with a **Ni substrate**, moving beyond purely **repulsive spherical indenters** toward **chemically explicit tips** (including **hydrogenated diamond** and **oxidized Ni** scenarios). Reactive and non-reactive treatments are contrasted with **AFM tip-blunting observations** and selected **DFT** references. A central reported trend is **Ni transfer to the tip** under **clean or oxidized** conditions, while **hydrogen termination of the diamond tip** can **suppress or eliminate** transfer—an effect framed as larger than a simple **surface oxide contaminant** story.

## Methods

- **MD nanoindentation** with varying **tip chemistry** (clean, H-terminated, oxide-like).
- Comparisons to **DFT** and **experimental AFM** literature on tip wear and adhesion.

<!-- enrich-from-extract:v2 -->

- In this work we examine the e ﬀects of these assumptions by comparing detailed MD simulations utilizing varying interaction potentials against both experimental atomic force microscopy observations and calculations using density functional theory.
- Speciﬁcally, we examine the e ﬀect of a tip −substrate interaction on the indenter under clean, hydrogenated, and oxidized conditions.
- We ﬁnd that under clean or oxidized conditions (where we include oxygen on the nickel surface to mimic a passivating NiO layer) there is a substantial material transfer from the substrate to the tip.


## Findings

- **Material transfer (Ni onto tip)** is pronounced for **clean/oxidized** Ni contacts in the simulations summarized in the abstract.
- **Hydrogen on the diamond tip** strongly mitigates adhesion/transfer relative to the oxide-passivation case in those same comparisons.
- The work argues that **idealized repulsive indenters** can miss **chemomechanical** mechanisms visible in more realistic tip models.

### Additional results (article abstract)

- This material (Ni atoms) remains adsorbed on the tip upon retraction.
- However, the presence of hydrogen on the diamond tip drastically reduces, or even altogether eliminates, this material transfer, therefore having an e ﬀect much larger than that of a contaminating oxide layer.


## Limitations

- Scope centers on **model Ni/diamond** interfaces; quantitative transfer rates for other metal/ceramic pairs require separate parameter validation.
- **Finite indentation speeds** and **tip radii** influence outcomes; mapping to AFM time scales is non-trivial.

## Relevance to group

Co-authored **NIST + Penn State** effort connecting **ReaxFF-class reactive modeling** (via van Duin group involvement) to **nanomechanics and tribology** interpretation problems.

## Citations and evidence anchors

- Abstract and Sec. 1 in `papers/Tavazza_JPC_2015_indentor.pdf`; **DOI:** `10.1021/acs.jpcc.5b01275`.

## Related topics

- [[reaxff-family]]
