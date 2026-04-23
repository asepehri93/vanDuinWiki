---
id: paper:2016islam-venue-research-3
type: paper
title: "Reductive decomposition reactions of ethylene carbonate by explicit electron transfer from lithium: an eReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:ereaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b08688"
year: 2016
authors:
  - "Md Mahbubul Islam"
  - "Adri C. T. van Duin"
venue: "Journal of Physical Chemistry C"
pdf_sha256: "25e01170f6b2e7be043e7ce6ac94b80c0efc33d0392cbec762278bd9bb5cca0d"
pdf_path: "papers/Islam_eReaxFF_LiEC_JPC_2016_proof.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:batteries-interfaces
  - keyword:reactive-md
  - keyword:nvt-simulation
---
<!-- id:paper:2016islam-venue-research-3 -->

## Summary

Solid-electrolyte interphase formation in lithium-ion batteries involves reduction of carbonate solvents at metal anodes, a process dominated by electron transfer, ring opening, and radical chemistry that is expensive to sample with ab initio molecular dynamics at electrode scales. This *Journal of Physical Chemistry C* article applies eReaxFF—an extension of ReaxFF that augments bond-order reactive dynamics with explicit pseudoclassical electron degrees of freedom—to ethylene carbonate reduction initiated by electron transfer from lithium metal. The model aims to capture SEI-relevant elementary events such as ring opening toward radical intermediates and subsequent termination reactions without prescribing a fixed reaction network beforehand. The authors argue that eReaxFF improves energetics for key reduction steps relative to standard ReaxFF and tracks literature quantum-chemistry trends for selected pathways. This wiki slug points at an ACS author-proof PDF; **`[[2016islam-venue-jp6b08688]]`** should be preferred for stable pagination and figure numbering when both files exist in the corpus.

## Methods

Duplicate **ACS author proof** PDF for the same article as [[2016islam-venue-jp6b08688]] (DOI `10.1021/acs.jpcc.6b08688`). Protocol matches that page: **eReaxFF** **molecular dynamics** in the **NVT** ensemble on **60 EC** and **40 Li** atoms (composition stated in the article) with three-dimensional **periodic** **boundary** conditions, **1 K** relaxation, **300 K** and **600 K** production (gradual heating toward **600 K**), **Berendsen** thermostat (**100 fs** damping), **velocity Verlet** at **0.10 fs**, **1 amu** fictitious mass per explicit electron carrier (Section 3.2), and multi‑ps segments discussed in Section 3 and figure captions. **NPT** barostats, **N/A — applied electric field:** not used in the primary workflow, and umbrella or replica metadynamics are likewise omitted. The paper applies published **eReaxFF** parameters and compares to literature quantum chemistry rather than reporting a new parametrization or standalone DFT campaign.

## Findings

Same SEI-oriented picture as [[2016islam-venue-jp6b08688]]: **reduction** and **decomposition** pathways begin with lithium-to-EC electron transfer, **ring opening** toward EC⁻/Li⁺-type radicals, and termination chemistry sampled without a fixed reaction network. **eReaxFF** tracks **literature** quantum-chemistry trends better than prior ReaxFF on EC electron affinity and dissociation kinetics—a direct **versus**-ReaxFF **benchmark** highlighted in the abstract. **Temperature** (**300 K** versus **600 K**) changes which termination channels appear within the reported time windows, a key sensitivity lever for kinetics on multi‑ps trajectories. **Limitations:** the introduction stresses that salts, cosolvents, and additives at realistic interfaces remain beyond the EC + Li emphasis, an **open** modeling direction. **Corpus honesty:** this proof **PDF** defers figure and page locators to [[2016islam-venue-jp6b08688]] as the **canonical** slug for the same DOI.

## Limitations

Proof PDFs can differ in line breaks and figure placement from the version of record; cite **`[[2016islam-venue-jp6b08688]]`** for authoritative locators. eReaxFF remains an approximate treatment of electronic structure; quantitative overpotentials and product distributions should be cross-checked against experiment and higher-level theory where decisions depend on fine energetics.

## Relevance to group

The entry preserves manifest provenance for duplicate PDFs while routing readers to the canonical slug for DOI `10.1021/acs.jpcc.6b08688`, a van Duin-coauthored eReaxFF battery-interface benchmark in the corpus.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.6b08688](https://doi.org/10.1021/acs.jpcc.6b08688) — *J. Phys. Chem. C* **120**, 27128–27134 (2016).

## Reader notes (navigation)

- [[2016islam-venue-jp6b08688]]

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
