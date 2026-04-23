---
id: paper:2017alhabeb-microsc-micr-atomic-defects
type: paper
title: "Atomic Defects and Edge Structure in Single-layer Ti₃C₂Tₓ MXene"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - task:experiment-integrated
  - method:dft-static
  - scale:atomistic
paper_keywords:
  - keyword:2d-materials
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1017/S1431927617009187"
year: 2017
authors:
  - "Xiahan Sang"
  - "Dundar Yilmaz"
  - "Yu Xie"
  - "Mohamed Alhabeb"
  - "Babak Anasori"
  - "Xufan Li"
  - "Kai Xiao"
  - "Paul R. C. Kent"
  - "Adri van Duin"
  - "Yury Gogotsi"
  - "Raymond R. Unocic"
venue: "Microsc. Microanal. (Proc.)"
pdf_sha256: "58260d1049f24d2529fa914aca59a7615c92b357b3c234878631ec6e336730d3"
pdf_path: "papers/Xiahan_atomic_defects_and_edge_structure_in_singlelayer_ti3c2tx_mxene.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017alhabeb-microsc-micr-atomic-defects -->

Aberration-corrected STEM on single-layer Ti₃C₂Tₓ MXene links HF etching conditions to titanium vacancy populations and heated-edge faceting, with modeling collaborations noted for follow-on DFT and MD.

## Summary

Conference proceedings abstract summarizing **atomic-resolution STEM** of **single-layer Ti₃C₂Tₓ MXene**, revealing **Ti vacancies** and vacancy clusters whose concentration can be tuned via **HF etching** conditions, and **in situ heating** experiments that expose **edge faceting** at elevated temperature. The text notes planned combination with **DFT** and **molecular dynamics** to interpret stability and properties. The imaging campaign targets MXene sheets where point defects and edge reconstructions can dominate electronic transport because the flake thickness approaches the defect spacing.

## Methods

**Experiment-integrated microscopy.** **ADF-STEM** images **single-layer Ti₃C₂Tₓ MXene** on a **Nion UltraSTEM** with a probe aberration corrector, operated at **60 kV** for the defect-imaging campaign described in the proceedings text. **HF** etching concentration is varied to tune **Ti vacancy (V_Ti)** populations, including clusters spanning about **2–17** missing **Ti** columns as illustrated in the figures. **Protochips** in situ heating with **100 kV** STEM imaging at **~500 °C** (after **~20 min** beam/heating conditions described in the proceedings) produces **faceted holes**; facets align with **{100}** planes relative to the crystal schematic.

**Atomistic modeling (not detailed in proceedings excerpt).** The proceedings abstract states that **DFT** and **molecular dynamics** will be combined with the STEM work to discuss **edge stability** and functional consequences, but the **short proceedings PDF** does **not** list **functional/basis/k-mesh**, **supercell sizes**, **timestep**, **ensemble**, **thermostat/barostat**, or **trajectory lengths**. Treat any quantitative modeling protocol as **evidence in the full PDF** or follow-on publications, not this summary alone.

**Static QM / DFT (proceedings-level honesty).** For the **DFT** companion work previewed in the text, the proceedings excerpt does **not** report **dispersion** corrections (**N/A —** not stated), **basis set** / **PAW** details (**N/A —** not stated), **k-point** sampling (**N/A —** not stated), relaxed **reaction pathways** or **transition-state** searches (**N/A —** not stated), or tabulated **energies** / **barriers** (**N/A —** not stated). **Geometry** comparisons for **edges** are referenced qualitatively relative to **STEM** models; take quantitative **DFT** claims from the **full PDF** or linked journal outputs.

## Findings

Imaging resolves **V_Ti** and **multi-vacancy clusters** in **monolayer** flakes (**up to ~17** missing **Ti** columns in the abstract wording). **HF** concentration shifts defect statistics and is tied to **electronic conductivity** control. **Heated** experiments show **faceted pores** whose edges relate to crystallographic schematics in the figures. The abstract frames **point and edge defects** as levers for **catalysis** and **supercapacitance**, pending the **DFT/MD** follow-up described in the proceedings.

## Limitations

Proceedings **short paper**; detailed **DFT/MD** protocols and numerical results may be minimal here—use the **PDF** and any linked **journal** version for full methods and for modeling-backed claims.
- Beam energies differ between the 60 kV imaging called out for defect analysis and the 100 kV heating track noted in the abstract; readers should verify which conditions apply to each figure panel in the full proceedings PDF.

## Relevance to group

**Adri van Duin** coauthorship linking ORNL/Drexel MXene imaging to multiscale modeling.

## Citations and evidence anchors

- DOI: `10.1017/S1431927617009187`.

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

