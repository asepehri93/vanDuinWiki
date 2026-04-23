---
id: paper:2018kyoungmin-min-acs-characterization-mechanical
type: paper
title: "Characterization of mechanical degradation in perfluoropolyether film for its application to anti-fingerprint coatings"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:organics-polymers-pyrolysis
  - domain:oxides-ceramics
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:oxide-surface
  - keyword:tribology
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.8b13159"
year: 2018
authors:
  - "Kyoungmin Min"
  - "Jungim Han"
  - "Byungha Park"
  - "Eunseog Cho"
venue: "ACS Appl. Mater. Interfaces (Just Accepted manuscript; web 9 Oct 2018)"
pdf_sha256: "027166f709181f5f34e12010a7744b66390084c4cc940152eae6fe416ec32cb1"
pdf_path: "papers/ReaxFF_others/eunseog_durability of PFPE.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018kyoungmin-min-acs-characterization-mechanical -->

## Summary

Min *et al.* apply **reactive molecular dynamics** to **perfluoropolyether (PFPE)** films intended as **anti-fingerprint** coatings on **glass**/**silica** substrates, a consumer-electronics context where **durability** under **mechanical** wiping and **thermal** cycling must coexist with **low surface energy** (*ACS Appl. Mater. Interfaces*, DOI `10.1021/acsami.8b13159`; the ingested PDF is an ACS **“Just Accepted”** web release, so **pagination** may differ slightly from the **issue** PDF). The study decomposes failure into **intrachain** versus **interchain** contributions: **Si–C** linkages emerge as a particularly **vulnerable** **intrachain** motif, with **scission** and subsequent **C–O** chemistry proposed as a **degradation** channel, while **longer** **PFPE** chains improve **interchain** **load transfer** in the simulated films. The authors further explore a **deposition-ordering** idea—placing **shorter** chains adjacent to **silica** and **longer** chains outward—to maximize **interchain** **cohesion** in a **layer-by-layer** **deposition** test described in the article.

## Methods

The simulation campaign implements multiple **mechanical** interrogations consistent with keywords in the manuscript (**PFPE–silane** chemistry, **pulling**/**adhesion** tests): **reactive MD** allows **bond breaking** so that **Si–C** and **C–O** responses are not artificially frozen as they would be in many **non-reactive** organic force fields. The article defines **crosslinking** conditions, **strain** protocols, and **film** construction steps used to compare **stacking** sequences; this wiki entry does not duplicate every numerical **pulling rate** or **temperature** but directs readers to the **Just Accepted**/**VOR** PDF for exact parameters. Because the corpus file is a **pre-issue** **PDF**, citations requiring **volume/page** should be verified against the **final** **bibliographic** record.

**MD application (ReaxFF on PFPE–silica).** **Engine:** **LAMMPS**-style **reactive MD** with the **ReaxFF** parameterization cited in *ACS Appl. Mater. Interfaces* for **C/F/O/Si/H** chemistry in **PFPE** films on **glass**/**silica**. **System:** **atom** counts, **film** thicknesses, and **oxide** **slab** dimensions are given in **Methods**/**figures**. **PBC:** **three-dimensional PBC** for in-plane **film** models unless stated otherwise. **Ensemble / thermostat / timestep / duration:** follow the **Just Accepted** manuscript—**N/A — full numerical tables not transcribed** on this page; confirm final values in the **VOR** **PDF**. **Barostat:** **N/A — NPT** not emphasized for the summarized **mechanical** tests if cells are **NVT**/**strain** controlled. **Pressure:** **N/A — bulk GPa hydrostatic targets** not the focus beyond **tensile**/**shear** **loading** protocols. **Electric field:** **N/A — bias** not applied. **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not reported.

## Findings

**Outcomes.** **Si–C** linkages are the weakest **intrachain** motifs, promoting **scission** and **oxygen**-involving **degradation** channels in **reactive** trajectories. **Longer** **PFPE** chains improve **interchain** load sharing and **toughness** metrics in the modeled films.

**Comparisons.** **Deposition** **ordering** (**short** chains at the **oxide**, **long** chains outward) improves **interchain** cohesion versus alternate **stacking** sequences in the same **benchmark**.

**Sensitivity.** **Crosslinking** density and **strain** rate alter when **failure** localizes at the **interface** versus within the **fluorocarbon** film.

**Limitations and PDF grounding.** **Just Accepted** `pdf_path` may differ from the **issue** PDF; **fingerprint** oils are absent from the **pure** **PFPE**/**silica** **simulation** cells, so **field** **durability** remains an **experimental** question. Detailed **MD** numbers: **`pdf_path`**.
## Limitations

- **Industrial** films include **processing** variability beyond the **idealized** **MD** setups; quantitative transfer requires **experimental** benchmarking on target **formulations**.

## Relevance to group

Shows **ReaxFF-class** **reactive MD** applied to **fluoropolymer** **durability** on **oxide** supports.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acsami.8b13159](https://doi.org/10.1021/acsami.8b13159)

## Related topics

- [[reaxff-family]]
