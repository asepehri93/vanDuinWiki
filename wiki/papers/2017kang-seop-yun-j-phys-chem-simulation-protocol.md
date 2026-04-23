---
id: paper:2017kang-seop-yun-j-phys-chem-simulation-protocol
type: paper
title: "Simulation Protocol for Prediction of a Solid-Electrolyte Interphase on the Silicon-based Anodes of a Lithium-Ion Battery: ReaxFF Reactive Force Field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:qm-training-data
  - keyword:batteries-interfaces
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.7b00898"
year: 2017
authors:
  - "Kang-Seop Yun"
  - "Sung Jin Pai"
  - "Byung Chul Yeo"
  - "Kwang-Ryeol Lee"
  - "Sun-Jae Kim"
  - "Sang Soo Han"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "8466ca605c26b3c8ae45a7fa82e8c38bc0cabc903f9396127b26601ade4d35a8"
pdf_path: "papers/ReaxFF_others/Kang_Seop_Yun_SiC_EC_JPC_Lett_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017kang-seop-yun-j-phys-chem-simulation-protocol -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** reaction pathways, stoichiometries, and numerical values, use the **peer-reviewed Letter** (and Supporting Information where cited)—not this page alone.

## Summary

This Letter develops a ReaxFF reactive model aimed at SEI-relevant chemistry for **liquid carbonate electrolytes in contact with Si-based anodes** (pristine Si and SiO\(_x\)), including **multi-solvent mixtures and VC/FEC additives**, trained from ab initio reference data. Large-scale reactive molecular dynamics then samples electrolyte decomposition and interfacial reactions so that gas-phase species (for example C\(_2\)H\(_4\), CO, CO\(_2\), CH\(_4\), C\(_2\)H\(_6\)), inorganic fragments (Li\(_2\)CO\(_3\), Li\(_2\)O, LiF), and organic motifs (ROLi and ROCO\(_2\)Li with R = methyl or ethyl) can be discussed in the same framework as experimentally relevant liquid formulations—at computational cost tractable for multicomponent cells.

## Methods

**A — Force-field training / fitting:** **ReaxFF** adjusted to **DFT** targets for **carbonate** **reduction**, **ring-opening**, **EC** **one-electron** routes (**SI** expands tables); **Li**-containing **electrolyte** chemistry for **Si**/**SiO\(_x\)** interfaces.

**B — Molecular dynamics / sampling:** **LAMMPS** via **iBat** battery workflow; **velocity Verlet**, **0.5 fs**, **NVT** **800 K**, **thermostat** **Nose–Hoover** (**0.01 fs⁻¹** damping per manuscript; the **Letter** prints **Nosé–Hoover**). **Cells:** **pristine Si** vs **SiO\(_x\)**, **mixed carbonates**, **VC**/**FEC** **additives**. **Barostat / pressure:** **N/A —** the summarized **production** trajectories are **NVT** **liquid**/**interface** cells at **800 K** without **NPT** hydrostatic **pressure** control; confirm any **NPT** or **stress**-controlled segments in **SI** if present.

**C — DFT / static QM:** **DFT** reference data for **parameter** **fitting** and **spot checks** (**SI**).

**D — Review / non-simulation framing:** **Primary** **JPCL** **Letter**—**not** a review.

**System / boundaries:** Electrolyte–electrode supercell compositions, **3D PBC** choices, and fixed vs mobile **Si** layers are tabulated in the **Letter**/**SI** rather than duplicated here. **Duration / staging:** The **Letter** reports **multi-ns** cumulative **NVT** reactive sampling at **800 K** to accumulate SEI-relevant decomposition chemistry; exact per-segment **ps**/**ns** splits and any **equilibration** windows should be read from **`pdf_path`**/**SI** (indexed **abstract** alone is insufficient for full protocol tables).

## Findings

On **Si(100)** with **dangling Si sites**, EC can undergo ring-opening chemistry even **without Li** in the shown interfacial setup, evolving **C\(_2\)H\(_4\)** and **CO** among other products, whereas on a **hydrogen-terminated** Si surface **no EC dissociation** is observed in the paired comparison—consistent with the experimental trend cited. Across anode chemistries, electrolyte **composition** (including mixtures) and **additives** shift relative product distributions, supporting the authors’ argument that a **mixture-capable reactive protocol** is needed for SEI modeling beyond single-solvent, fixed-composition cells.

**Comparisons / limitations.** The Letter explicitly contrasts **dangling** vs **H-terminated** **Si** reactivity and ties **additive** / **solvent** **composition** trends to **experimental** SEI-relevant observations; **800 K** **acceleration** is a documented **limitation** relative to **room-temperature** **battery** operation.

**Corpus / PDF honesty.** Use **`pdf_path`** and **SI** for **stoichiometric** product tables beyond this summary.

## Limitations

- Elevated **800 K** MD is used to accelerate reactions; it is **not** a direct room-temperature operating snapshot, and barrier crossing statistics may differ from lower-temperature electrochemical conditions.
- **ReaxFF** remains an approximate reactive model; quantitative agreement with DFT or experiment should be checked case by case, especially for subtle additive effects and long-time SEI maturation.
- **Electrochemical reduction** in the full sense (potentials, explicit electron transfer at controlled bias) is not reproduced atomistically in the Letter’s MD framing; the work focuses on **chemical reactivity** pathways in condensed-phase setups aligned with prior reduction-focused literature.

## Relevance to group

Independent **Korea Institute of Science and Technology / Sejong University** work on **ReaxFF + LIB SEI chemistry** on Si anodes; useful cross-reference for **reactive electrolyte–electrode interface** modeling alongside group battery and ReaxFF lineage pages.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpclett.7b00898](https://doi.org/10.1021/acs.jpclett.7b00898)
- Text pointers: `normalized/extracts/2017kang-seop-yun-j-phys-chem-simulation-protocol_p1-2.txt`; Supporting Information for extended DFT and parameterization tables as referenced in the Letter.

## Reader notes (navigation)

- **Theme hub:** [[batteries-interfaces-reaxff]]
- **Force-field overview:** [[reaxff-family]]

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
