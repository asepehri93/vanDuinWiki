---
id: paper:2017ming-chen-acs-ordered-atomically
type: paper
title: "Ordered and Atomically Perfect Fragmentation of Layered Transition Metal Dichalcogenides via Mechanical Instabilities"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - task:application
paper_keywords:
  - keyword:2d-materials
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.7b04158"
year: 2017
authors:
  - "Ming Chen"
  - "Juan Xia"
  - "Jiadong Zhou"
  - "Qingsheng Zeng"
  - "Kaiwei Li"
  - "Kazunori Fujisawa"
  - "Wei Fu"
  - "Ting Zhang"
  - "Jing Zhang"
  - "Zhe Wang"
  - "Zhixun Wang"
  - "Xiaoting Jia"
  - "Mauricio Terrones"
  - "Ze Xiang Shen"
  - "Zheng Liu"
  - "Lei Wei"
venue: "ACS Nano"
pdf_sha256: "b40e8733c71b0481ae7f3c0878edf15f3dfbe1bba1c1b2a055371aabc0b35e3f"
pdf_path: "papers/Others/Ordered and Atomically Perfect Fragmentation of Layered Transition Metal Dichalcogenides via Mechanical Instabilities.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017ming-chen-acs-ordered-atomically -->

!!! abstract
Polymer necking localizes strain to fragment sandwiched TMD monolayers into ordered nanoribbons across materials and sizes; electrical and HER demonstrations use MoS₂ nanoribbon arrays.

## Summary

The paper reports a **polymer necking** method: atomically thin **transition metal dichalcogenides (TMDs)** on a **theroplastic polycarbonate** substrate are fragmented into **ordered nanoribbons** when a tensile neck propagates through the polymer, localizing strain at the neck front. **WS₂** monolayers transferred via PMMA are used for many optics/Raman/PL demonstrations; the approach is stated to generalize across semiconducting TMDs from monolayer to bulk thickness. **Field-effect transistors** from monolayer **MoS₂** nanoribbon arrays show on/off ratios ~**10⁶**. **Hydrogen evolution** activity improves on monolayer MoS₂ nanoribbons, attributed to increased edge sites from physical fragmentation. The authors contrast **uncontrolled** cracking from random defects with **neck-guided** fragmentation that aligns ribbons along the **strain direction** while producing **compressive wrinkles** from **transverse PC shrinkage** after the neck passes.

## Methods

**Force-field training / fitting.** **N/A —** no **atomistic force-field** development or **ReaxFF**/**classical** refit is reported.

**MD application (atomistic dynamics).** **N/A —** **atomistic molecular dynamics** is **not** a primary methodology in this **experimental**/**device** study.

**Static QM / DFT.** **N/A —** **DFT** or other **static QM** workflows are **not** central to the reported **polymer necking** fabrication route.

**Review / non-simulation / experiment.** **Polymer necking** processes **TMD** flakes **sandwiched** in **thermoplastic polycarbonate (PC)** stacks: **WS₂** (and other **TMDs**) are transferred to **PC** via **PMMA**-mediated transfer, consolidated, clamped on a **linear travel stage** with **load-cell** **stress–strain** acquisition, and stretched until **neck** initiation and **propagation** at approximately **constant neck speed** along the film (**Fig. 1**). **Optical / Raman / PL** characterize **ribbon** morphology; **FET** arrays (**MoS₂**) and **HER** measurements (**MoS₂** edges) follow **device**/**electrochemistry** protocols in **Methods**/**SI** (see article for **electrolyte**, **bias**, and **rate** details).

## Findings

**Outcomes and mechanisms.** **Polymer necking** localizes **strain** at the propagating neck and fragments **sandwiched TMD** monolayers into **parallel, ordered nanoribbons** over a wide range of initial flake sizes (micron–**100 µm** scale) with **limited sensitivity** to pre-existing **defect** content in the experiments reported. The authors distinguish this **neck-front** mechanism from **shear-lag** cracking: **transverse shrinkage** of the **polycarbonate** after the neck passes produces **compressive wrinkles** alongside **ribbon** alignment along the **tensile** direction.

**Comparisons.** **Field-effect transistors** built from **monolayer MoS₂** **nanoribbon arrays** show **on/off ratios** of order **10⁶** (as reported). **Hydrogen evolution** measurements on **monolayer MoS₂** **nanoribbons** show **improved** activity versus **unfragmented** material, attributed to **increased edge** area from **physical** fragmentation. **WS₂** **optical/Raman/PL** data illustrate **ribbon morphology**; additional **TMD** chemistries (**MoS₂**, **MoSe₂**, **WSe₂**) demonstrate **breadth** of the necking approach.

**Sensitivity and design levers.** **Neck propagation speed**, **pre-stretch**, and **stack** details (see **Methods/SI**) influence **ribbon width** and **spacing** distributions.

**Limitations and outlook (as authored).** **Device** metrics and **HER** conditions follow **ACS Nano** **Methods/SI**; this wiki does not substitute for those **electrolyte**/**bias** tables.

**Corpus honesty.** Summaries follow the **indexed PDF** at `pdf_path`; confirm any **figure** numerics on the **DOI-linked** article before downstream reuse.

## Limitations

Mechanical protocol is materials-specific to the polymer/TMD stack; electronic performance may trade off with grain-structure changes not modeled atomistically here. Neck **propagation speed** and **polymer** **viscoelastic** details can couple to **ribbon** **width** distributions in ways not exhaustively parameterized across every **TMD** chemistry in the study.

## Relevance to group

Experimental 2D materials processing adjacent to computational work on TMDs in the broader corpus.

## Citations and evidence anchors

- DOI: `10.1021/acsnano.7b04158`

## Related topics

- [[graphene-nanocarbon]]
