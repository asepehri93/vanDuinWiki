---
id: paper:2020sim-venue-paper
type: paper
title: "Functionalized graphene sheet as a dispersible fuel additive for catalytic decomposition of methylcyclohexane (proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:berendsen-thermostat
  - keyword:combustion
  - keyword:galley-or-proof-pdf
  - keyword:nvt-simulation
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1016/j.combustflame.2020.04.002"
year: 2020
authors:
  - "Hyung Sub Sim"
  - "Richard A. Yetter"
  - "Sungwook Hong"
  - "Adri C. T. van Duin"
  - "Daniel M. Dabbs"
  - "Ilhan A. Aksay"
venue: "Combustion and Flame (Elsevier Article in Press proof)"
pdf_sha256: "355740ae86c747ff5645f33fa5741ccfcb2ae5a9ccbc7b3b8977231c6f31f494"
pdf_path: "papers/Sim_CombFlame_2020_graphene_catalysis_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2020sim-venue-paper -->

## Summary

This slug points to an **Elsevier “Article in Press” proof** PDF for the same **Combustion and Flame** study as **`[[2020sim-combustion-a-functionalized-graphene]]`** (**DOI [10.1016/j.combustflame.2020.04.002](https://doi.org/10.1016/j.combustflame.2020.04.002)**). The work couples a **high-pressure flow reactor** investigation of **methylcyclohexane (MCH)** decomposition under **supercritical** conditions with **ReaxFF reactive MD** in **AMS/ADF**. Experiments span **780–825 K** at **4.72 MPa** with **50 ppmw FGS**; the abstract reports increased **fuel conversion** and **C₁–C₂** product yields (about **+43.3%** and **+62.1%** respectively at **820 K** with **50 ppmw FGS**). MD is run at **1700, 1800, and 1900 K** with **Berendsen** thermostat, **NVT** ensemble, **0.25 fs** timestep, and density **~0.31 g/cm³**, matching the primary page’s description of FGS **oxygen** groups, **C₇H₁₃** formation, and early **H** / **CH₃** / **C₂H₅** chemistry. This page keeps the **proof** artifact for manifest provenance; use **`[[2020sim-combustion-a-functionalized-graphene]]`** for the non-proof PDF when citing pagination and the issue-of-record.

## Methods

**1 — MD application.** Same protocol summary as the VOR page: **reactive molecular dynamics** with **ReaxFF** **C/H/O** in **AMS/ADF** (engine as published); **MCH** fuel molecules interacting with **FGS** in a **periodic** simulation cell (**PBC**), full **atom** counts in **Section 3** of the VOR PDF. **NVT**; **Berendsen** **thermostat**; **0.25 fs** time step; **1700, 1800, 1900 K**; **~0.31 g cm⁻³**; **multi-ns** segments. **N/A** — NPT; **N/A** — electric field; **N/A** — enhanced sampling beyond the authors’ standard MD. Full staging is in the VOR **Section 3** and on **`[[2020sim-combustion-a-functionalized-graphene]]`**.

**2 — High-pressure flow reactor (experiment).** **Supercritical** MCH, **4.72 MPa**, **780–825 K**, **50 ppmw** FGC as in the article abstract; **GC/MS** in the full text. **N/A** — in situ diagnostics beyond the article text for this proof slug (partial extract).

**3 — Force-field training.** **N/A** — same published **ReaxFF** as the study; not refit in the manuscript.

**4 — Static QM.** **N/A** for a standalone in-paper DFT block.

**5 — Review / non-simulation.** **N/A.**

## Findings

**Outcomes.** The proof abstract is consistent with the curated VOR page: FGS increases **MCH** conversion and **C₁–C₂** yields; MD highlights **oxygen** on FGS in MCH **decomposition** and **C₇H₁₃** / early-radical chemistry. **N/A** — new results beyond the primary article; **provenance** of this file is the only distinction.

**Comparisons and sensitivity.** Same qualitative points as the VOR page: large **T** gap between **MD** and **reactor** (qualitative use).

**Authored limitations.** **Proof** PDFs may have layout and line-number artifacts relative to the final **issue of record**; use **`[[2020sim-combustion-a-functionalized-graphene]]`** for canonical pagination when possible.

**Corpus honesty.** Protocol minutiae are tracked on the VOR `pdf_path`; this proof is **partial** extract quality for automated pipelines.

## Limitations

Proof PDFs may show **layout** differences, **line numbers**, and headers absent from the **final** issue. Large **T** gaps between **MD** and experiment limit quantitative rate mapping.

## Relevance to group

**van Duin** co-authorship; **combustion** / **endothermic fuel** chemistry with **ReaxFF** and **experimental** validation.

## Citations and evidence anchors

- DOI: [10.1016/j.combustflame.2020.04.002](https://doi.org/10.1016/j.combustflame.2020.04.002)

## Reader notes (navigation)

- Version-of-record PDF: [[2020sim-combustion-a-functionalized-graphene]]

## Related topics

- [[2020sim-combustion-a-functionalized-graphene]]
- [[reaxff-family]]
