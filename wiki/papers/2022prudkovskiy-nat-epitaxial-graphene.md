---
id: paper:2022prudkovskiy-nat-epitaxial-graphene
type: paper
title: "An epitaxial graphene platform for zero-energy edge state nanoelectronics"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:graphene-carbon
  - keyword:2d-materials
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/s41467-022-34369-4"
year: 2022
authors:
  - "Vladimir S. Prudkovskiy"
  - "Yiran Hu"
  - "Kaimin Zhang"
  - "Yue Hu"
  - "Peixuan Ji"
  - "Grant Nunn"
  - "Jian Zhao"
  - "Chenqian Shi"
  - "Antonio Tejeda"
  - "David Wander"
  - "Alessandro De Cecco"
  - "Clemens B. Winkelmann"
  - "Yuxuan Jiang"
  - "Tianhao Zhao"
  - "Katsunori Wakabayashi"
  - "Zhigang Jiang"
  - "Lei Ma"
  - "Claire Berger"
  - "Walt A. de Heer"
venue: "Nature Communications"
pdf_sha256: "45632a4317f5931a15feff65d28711860907028b8e93d17ec2598e6902361d71"
pdf_path: "papers/Others/Graphene_ribbons_conductivity.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2022prudkovskiy-nat-epitaxial-graphene -->

!!! abstract "Scope"

Transport on epitaxial graphene on SiC shows long mean free path edge states distinct from bulk carriers, enabling quasi-ballistic edge networks in patterned ribbons.

## Summary

Lithographically patterned graphene often suffers from edge disorder that obscures graphene’s intrinsic electronic promise. Prudkovskiy et al. report low-temperature electronic transport in epitaxial graphene on silicon carbide (epigraphene) where annealed edges remain stabilized by the substrate. They demonstrate a protected edge state with mean free path greater than 50 micrometers, about five thousand times longer than bulk channels in their comparison, associated with a zero-energy non-degenerate quasiparticle feature discussed in the abstract. Seamless ribbon networks exhibit low-dissipation nodes at junctions, motivating edge-state-based device concepts distinct from bulk graphene transistors. The introduction contrasts epigraphene with chemically exfoliated nanoribbon networks that require metal interconnects and suffer from edge roughness. The abstract further argues that epigraphene matches industrial substrate constraints while offering a distinct electronics paradigm compared with conventional CMOS scaling.

## Methods

### A — Force fields / reactive MD

- **None.** This is an **experimental** **transport** paper on **epitaxial graphene/SiC**—no **ReaxFF** or classical **MD** protocol.

### B — Device fabrication

- **Epitaxial graphene** on **SiC**; **lithographic** patterning into **ribbons** / networks; **edge** **anneal** recipes in *Nat. Commun.* **Methods**.

### C — Electronic characterization

- **Low-temperature** **transport**; **scanning gate microscopy**; **magnetotransport**; supporting **structural** probes as listed in the article.

### D — Literature / theory context

- Interpretation references **ballistic** **edge** states vs **bulk** channels; **reproduce** **cryogenic** **bias** and **gate** layouts from the **peer-reviewed** **PDF**.

For citation hygiene, pair this transport study with **2D materials** synthesis pages in the corpus when users ask about **edge chemistry** versus **edge electronics**—the present article addresses the latter.

## Findings

Annealed edges of patterned epigraphene support edge-localized conduction with mean free path exceeding 50 μm and vastly longer than bulk mean free paths in the same structures according to the authors’ comparison. Integrated seamless ribbons form quasi-ballistic networks with low-loss junctions. The work positions epigraphene as a candidate platform for edge-centric nanoelectronics when paired with industrial SiC substrates. The authors argue this combination satisfies industrial fabrication constraints while introducing a new electronic degree of freedom tied to edge topology. For the van Duin knowledge base, the article is primarily a transport physics reference rather than a reactive MD template, but it anchors realistic edge quality metrics when discussing graphene device literature alongside reactive simulations of carbon oxides elsewhere in the corpus. The reported mean free path exceeding tens of micrometers provides orders-of-magnitude context when judging whether classical transport models or ballistic edge models dominate in patterned devices. Readers should pair this citation with fabrication details in Methods when comparing epigraphene to CVD graphene, because edge chemistry differs drastically across growth routes. Quantum transport refinements beyond the experimental analysis here are outside scope for this wiki page.

## Limitations

Results are specific to high-quality epigraphene; exfoliated or chemically derived graphene may not reproduce edge-state behavior without similar substrate stabilization.

## Relevance to group

Peripheral to the ReaxFF corpus—retained for graphene nanoelectronics context and citation linking.

## Reader notes (navigation)

- Not a [[reaxff-family]] methods paper.

## Citations and evidence anchors

- DOI: [10.1038/s41467-022-34369-4](https://doi.org/10.1038/s41467-022-34369-4)

## Related topics

- [[graphene-nanocarbon]]
