---
id: paper:2019amar-m-kamat-nat-bioinspired-cilia
type: paper
title: Bioinspired Cilia Sensors with Graphene Sensing Elements Fabricated Using 3D
  Printing and Casting
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:carbon-hydrocarbon
- material:graphene-carbon-nano
- task:application
- task:experiment-integrated
paper_keywords:
- keyword:graphene-carbon
- keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: 10.3390/nano9070954
year: 2019
authors:
- Amar M. Kamat
- Yutao Pei
- Ajay G. P. Kottapalli
venue: Nanomaterials 2019, 9(7), 954 (MDPI)
pdf_sha256: 37653b290a0305647fe24913078a728eb1b5b0e765c89e3b27c3e55de6c3c408
pdf_path: papers/Others/Kamat-graphene-flow-sensor-2019.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2019amar-m-kamat-nat-bioinspired-cilia -->

## Summary

**Bioinspired** **cilia** sensors mimic **biological** **flow** **haircells** by transducing **fluid** **shear** and **contact** into **electrical** signals using **soft** elastomer bodies and **conductive** nanofillers. Kamat, Pei, and Kottapalli report **flexible, bioinspired flow and tactile sensors** built by **3D printing** metallic **molds**, **casting** **PDMS** structures, and embedding **graphene nanoplatelet** **piezoresistive** films inside **microchannels**. A **cilia-inspired** pillar–cantilever geometry transduces **mechanical** stimuli into **resistance** changes. The **abstract** reports a **gauge factor ~37** under **cyclic tension–compression** and **detection thresholds** down to **~12 µm displacement** and **~58 mm s⁻¹ flow speed** for the demonstrated **water-flow** tests. The study is **experimental MEMS** work, not an atomistic simulation paper.

## Methods

**PDMS** **Young’s modulus**, **channel** aspect ratios, and **graphene** **percolation** within the composite set **sensitivity** limits for **gauge factor** and **noise**; the article’s **Methods** should be consulted for **dimensions** and **electrical** **measurement** circuits. The abstract describes the workflow as three-dimensional printing of a metallic mold with micropillar and microchannel features, casting polydimethylsiloxane into that mold, then drop-casting graphene nanoplatelets into the predesigned microchannel to realize the piezoresistive strain gauge before electrical testing. **Fabrication** uses **3D-printed** metal templates defining **micropillar** and **microchannel** features. **PDMS** **replica molding** forms the **soft** structural body. **Graphene nanoplatelets** are **drop-cast** into channels to create a **strain-sensitive** conductive network. **Electrical** characterization applies **cyclic** mechanical loading to extract **gauge factor**; **flow** and **tactile** tests calibrate **sensitivity** thresholds reported in the abstract.

## Findings

**Outcomes and mechanism.** The **cilia** pillar geometry concentrates **fluid shear** and **contact** into **strain** on the embedded **graphene nanoplatelet** network, producing **piezoresistive** **resistance** changes; the **abstract** reports a **gauge factor ~37** under **cyclic tension–compression**, consistent with a **percolating** conductive path modulated by **mechanical** deformation of the **PDMS** body rather than atomistic **reaction** or **diffusion** chemistry.

**Comparisons.** The article positions performance against generic **soft** **strain-gauge** expectations (high **gauge factor**, **low** **detection thresholds**); this wiki does not restate **literature** tables from the **PDF**—use the **Results** section for any head-to-head device **benchmarks**.

**Sensitivity and levers.** Reported **sensitivity** depends on **cyclic** loading conditions, **channel** and **pillar** dimensions from fabrication, and **graphene** loading in the composite; **flow** tests quote thresholds near **~12 µm** displacement and **~58 mm s⁻¹** **water** **flow** speed in the **abstract**, illustrating how **geometry** and **composite** microstructure set the **response** curve.

**Limitations and outlook.** **Graphene** here means **nanoplatelet** films, not **monolayer** graphene; **electrical noise**, **hysteresis**, and long-term **PDMS** aging are **not** fully characterized in this short wiki summary—see the paper for authored **limitations** and **future work**.

**Corpus honesty.** This page follows the **MDPI** **PDF**/`pdf_path` **abstract** and **Methods**-level description only; channel dimensions, bias circuits, and full **experimental** statistics beyond the **abstract** must be read from the **version-of-record** **PDF** (and **SI** if any).

## Limitations

For **corpus** readers searching **graphene** **ReaxFF** work, note this reference is **device fabrication**; link out to **materials** pages only for **supply-chain** or **sensor** context, not **atomistic** parameterization. **Graphene** here refers to **macroscopic nanoplatelet** films, not **monolayer** graphene; **electrical** and **noise** properties differ from **single-layer** devices. **No ReaxFF** or **DFT** appears in this work—corpus value is **adjacent** **application** context for **nanocarbon** integration.

**Confidence rationale:** `high`—claims limited to abstract-level reported metrics.

## Citations and evidence anchors

Open-access **MDPI** articles provide **HTML** and **PDF** variants with identical **DOI** metadata; prefer **DOI-based** citations for **pagination** independence. DOI: [10.3390/nano9070954](https://doi.org/10.3390/nano9070954).

## Reader notes (navigation)

**Experimental** **strain-gauge** characterization on **soft** substrates differs from **nanoscale** **AFM** **pull-off** tests; interpret **threshold** metrics as **device-level** **figures of merit**, not **single-bond** properties.

- [[graphene-nanocarbon]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[graphene-nanocarbon]]
