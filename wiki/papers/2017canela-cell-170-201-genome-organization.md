---
id: paper:2017canela-cell-170-201-genome-organization
type: paper
title: "Genome Organization Drives Chromosome Fragility"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - task:experiment-integrated
  - scale:atomistic
  - domain:methods-software
paper_keywords:
  - keyword:validation-experiment
candidate_tags:
  - "genomics-topology-not-md"
source_refs: []
doi: "10.1016/j.cell.2017.06.034"
year: 2017
authors:
  - "Andres Canela"
  - "Yaakov Maman"
  - "Seolkyoung Jung"
  - "Nancy Wong"
  - "Elsa Callen"
  - "Amanda Day"
  - "Kyong-Rim Kieffer-Kwon"
  - "Aleksandra Pekowska"
  - "Hongliang Zhang"
  - "Suhas S. P. Rao"
  - "Su-Chen Huang"
  - "Peter J. McKinnon"
  - "Peter D. Aplan"
  - "Yves Pommier"
  - "Erez Lieberman Aiden"
  - "Rafael Casellas"
  - "André Nussenzweig"
venue: "Cell"
pdf_sha256: "f62686213b9ffc0361699b7c9ecfbd0ba2a672eee1960a27c576424985e49295"
pdf_path: "papers/Others/Cell_from Mahdi_Aug5_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017canela-cell-170-201-genome-organization -->

## Evidence and attribution

!!! note "Corpus context"

    This PDF is **mammalian genomics** (3D genome organization and DNA breaks), **not** a computational chemistry or ReaxFF study. It is retained in the broader corpus as reference material. Summaries follow the **Cell** article identified by **`doi`**.

## Summary

Mammalian genomes fold into loops and topologically associated domains that influence gene regulation and replication timing. This **Cell** paper reports that **CTCF- and cohesin-anchored chromosome loop bases** are **preferred sites** for **DNA double-strand breaks (DSBs)** mediated by **DNA topoisomerase II beta (TOP2B)**. The authors argue these breaks are largely **independent of transcription and replication** as primary explanatory drivers in their framing, correlate with **cohesin** occupancy, and overlap **cancer translocation hotspots**—linking **three-dimensional genome architecture** to **patterns of chromosome fragility**.

The study’s motivation is mechanistic: if **DSBs** concentrate at **architectural** features rather than only at actively transcribed loci, then **loop** wiring becomes a first-class risk factor for **rearrangements** in development and disease. The article therefore combines **high-resolution** break mapping with **3D chromatin** measurements to ask whether **anchor** positions explain **fragility** beyond what **linear** sequence annotations would predict.

## Methods

**Experimental genomics (primary).** **DSB mapping** and **3D chromatin** assays (**Hi-C**-class methods and related protocols in *Cell*) quantify where **TOP2B-mediated breaks** occur relative to **CTCF–cohesin**-anchored **loop bases** and **TAD** structure. **Perturbations** that reduce or relocalize **CTCF/cohesin** are used to test whether **DSB** hotspots **track anchors**. **Comparative genomics:** overlap with catalogs of **recurrent translocations** in selected cancers. **Sequencing depth, cell lines, replicates, peak calling:** follow the primary **Methods**; **N/A — not duplicated at command-line resolution** on this wiki page.

**MD / ReaxFF / DFT —** N/A — not part of this study.

## Findings

Loop anchors bound by **CTCF** and **cohesin** are enriched for **TOP2B-mediated DSBs**, supporting a **mechanistic** link between **3D genome architecture** and **DSB** placement. Cleavage patterns are described as largely **transcription-**, **replication-**, and **cell-type-independent** in the paper’s summary statements. **Polymorphisms** that **rewire** CTCF/cohesin occupancy can **relocate** DSBs to new anchors. Breaks occur throughout **interphase**, are enriched near **topological domain borders**, and overlap **recurrent cancer translocation** breakpoints—supporting the thesis that **genome organization** drives **chromosome fragility**.

**Synthesis.** The authors present **organization** as a **spatial** determinant of where **TOP2B** activity leaves **break** signatures, which in turn intersects **oncogenic** **translocation** breakpoints more often than expected from **random** breakage models—within the evidence limits and statistics described in *Cell*.

**Comparisons:** results are compared against **transcription-first** and **replication-first** alternative explanations using **perturbation** experiments that decouple **CTCF/cohesin** occupancy from some **expression** readouts. **Sensitivity:** **genotype** variants that **rewire** anchors **relocate** **DSB** hotspots, demonstrating **concentration** of damage at **architectural** features. **Limitations / outlook:** statistical power, **cell-type** coverage, and **sequencing** depth govern how broadly the claims generalize—see *Cell* discussion. **Corpus honesty:** this wiki entry is **not** a substitute for the primary **PDF**/**SI** pipelines; it exists because the **PDF** is catalogued beside computational-chemistry sources.

## Limitations

No direct connection to **reactive MD**, **ReaxFF**, or materials simulation without explicit cross-domain bridging; operators should not mix claims with the electrochemistry spine without separate evidence.

## Relevance to group

Peripheral biology reference in the PDF collection; useful only where genomics context is intentionally cross-linked.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1016/j.cell.2017.06.034](https://doi.org/10.1016/j.cell.2017.06.034) (`papers/Others/Cell_from Mahdi_Aug5_2017.pdf`).

## Related topics

- (None required for vanDuinWiki chemistry spine.)
