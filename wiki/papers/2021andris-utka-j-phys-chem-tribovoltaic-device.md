---
id: paper:2021andris-utka-j-phys-chem-tribovoltaic-device
type: paper
title: "Tribovoltaic Device Based on the W/WO3 Schottky Junction Operating through Hot Carrier Extraction"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - material:oxide
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:tribology
  - keyword:oxide-surface
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.1c04312"
year: 2021
authors:
  - "Andris Šutka"
  - "Martins Zubkins"
  - "Artis Linarts"
  - "Linards Lapčinskis"
  - "Kaspars Mālnieks"
  - "Osvalds Verners"
  - "Anatolijs Sarakovskis"
  - "Raitis Grzibovskis"
  - "Jevgenijs Gabrusenoks"
  - "Edvards Strods"
  - "Krisjanis Smits"
  - "Viktors Vibornijs"
  - "Liga Bikse"
  - "Juris Purans"
venue: "J. Phys. Chem. C"
pdf_sha256: "0bbba628700dcf0663ca56dd8a3866d89f750d02e97c981e0f315d6e87733491"
pdf_path: "papers/Others/Verners_et_al_2021_acs.jpcc.1c04312.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021andris-utka-j-phys-chem-tribovoltaic-device -->

## Summary

Šutka *et al.* report a **tribovoltaic** device in which a **tungsten** needle slides on **magnetron-sputtered amorphous tungsten trioxide**, forming a **dynamic metal/oxide Schottky** junction where **friction**-driven electronic excitations inject **hot carriers** across the interface, producing **unbiased** **electric current** (*J. Phys. Chem. C*, DOI `10.1021/acs.jpcc.1c04312`). The framing parallels **hot-carrier photovoltaics**, but replaces photon absorption with **mechanical** energy input at the sliding contact. The authors position **tribovoltaics** as a route to **high current densities** from **mechanical** motion compared with many **piezoelectric**/**triboelectric** harvesters that deliver lower **current** at comparable **sliding** conditions, while emphasizing **oxide** durability because **repeated** **wear** can destroy **junction** quality in practical devices. The **materials** stack is intentionally **minimal**—**needle-on-disk** geometry with **sputtered** **oxide**—to separate **Schottky** **rectification** physics from **polymer** **electret** or **humidity-dominated** charging pathways that often complicate **classical** **triboelectric** **nanogenerator** interpretations.

## Methods

### A — Force-field training / fitting (ReaxFF and related)

- **N/A** — the publication is an **experimental** **tribovoltaic** / **tribology** + **mesoscale** electronics study, not a **ReaxFF** (or other FF) refit; there is no atomistic **parameterization** thread to report on this page.

### B — Experiments, protocols, and device measurements (primary)

**Fabrication** centers on **WO₃** prepared by **magnetron sputtering** onto a substrate stack described in the article, paired with a **W** **needle** counter-body chosen to realize a well-defined **Schottky** contact against the **wide-gap** **oxide**. **Electrical** measurements record **unbiased** **current density** during **controlled sliding** with specified **normal load**, **speed**, and **contact** geometry (exact ranges and instrumentation appear in **JPCC**). **Materials characterization** focuses on whether the **amorphous** **WO₃** film survives **cycling** without **catastrophic** **spallation** or **conductive** **shorting**, since **tribovoltaic** operation depends on maintaining a **rectifying** interface rather than a purely **ohmic** **wear** scar. Any **reported** **atmosphere** (**humidity**, **oxygen**) should be read carefully because **oxide** **surface** **hydroxyl** coverage and **adsorbate** films can shift **contact** **electrification** and **oxide** **defect** populations—quantities that atomistic models must set explicitly when attempting mechanistic comparisons.

### C — Static QM / electronic-structure modeling (if any)

- **N/A in this note** — if the *J. Phys. Chem. C* article or **SI** references **DFT** or other **QM** for the **W/WO₃** **interface** or **defects**, use `pdf_path`; this wiki page does not transcribe those details.

### D — Review scope, SI/galley notes, and non-primary corpus roles

- **Not applicable** — this is a primary **experimental** article, not a proof-only ingest route.

**Atomistic MD (LAMMPS, AIMD, etc.):** **N/A** — no production **MD** trajectory study is the focus; cross-link to reactive **MD** / **ReaxFF** **tribochemistry** pages only for conceptual comparison.

## Findings

The **W/WO₃** couple yields **tribovoltaic** currents with **peak** **unbiased** **current densities** up to **~1270 A m⁻²** as stated in the abstract, alongside reports of **durable** **amorphous** **WO₃** under the tested **sliding** protocol. The paper’s value for this knowledge base is primarily as **experimental** **tribology/oxide electronics** context: it is **not** a **ReaxFF** or **atomistic** simulation study, so mechanistic claims remain at **device** and **mesoscale** interpretation unless paired with separate modeling literature. For readers navigating **oxide** **interfaces** in the wiki, the article is nonetheless useful as a **benchmark** for **orders-of-magnitude** **current** **density** achievable from **sliding** **Schottky**-like contacts, which helps contextualize **interface** **charging** and **electron** **injection** discussions adjacent to **ReaxFF** **tribochemistry** entries that focus on **hydrocarbon** **films** rather than **metal**/**oxide** **diodes**.

## Relevance to group

Included as **corpus** **tribology/oxide electronics** context; **van Duin** is **not** among the authors—use for **interface** science cross-links sparingly.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.1c04312](https://doi.org/10.1021/acs.jpcc.1c04312)

## Related topics

- [[theme-oxides-silica-ceramics]]
