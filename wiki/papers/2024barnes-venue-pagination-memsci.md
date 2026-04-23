---
id: paper:2024barnes-venue-pagination-memsci
type: paper
title: "Mapping TpPa-1 covalent organic framework (COF) molecular interactions in mixed solvents via atomistic modeling and experimental study"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:classical-ff-specialized
  - method:classical-md
  - material:polymer-organic
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:polymer
  - keyword:validation-experiment
  - keyword:galley-or-proof-pdf
candidate_tags:
  - "organic-solvent-nanofiltration"
  - "COF-TpPa-1"
source_refs: []
doi: ""
year: 2024
authors:
  - "Anastasia M. Barnes"
  - "Mohammad M. Afroze"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
  - "Katie D. Li-Oakey"
venue: "J. Membr. Sci. (corrected proof in corpus; assign DOI from VOR)"
pdf_sha256: "914a5b6281437a8b08374bcc3d0426e79826d2b9106a213ba8abb7d768fdb927"
pdf_path: "papers/Barnes_Shin_COF_JMemSci_2024_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024barnes-venue-pagination-memsci -->

!!! note "Corpus note"
    The PDF is a **corrected proof**; pagination in the header is a placeholder. Record the **final DOI** from the **version of record** when available.

## Summary

Organic solvent nanofiltration separates complex chemical streams using membranes whose performance depends on nanoscale pore topology, framework flexibility, and nonideal sorption in mixed solvents—effects that are difficult to infer from macroscopic permeance alone. This *Journal of Membrane Science* contribution models the TpPa-1 covalent organic framework in contact with multicomponent organic solvents and compares atomistic predictions of solvent permeance and solute rejection to laboratory OSN measurements. Yun Kyung Shin and Adri C. T. van Duin are coauthors, signaling force-field work consistent with the group’s classical and reactive parameterization practices, though readers must open the Computational Methods section to confirm whether fixed-bond or reactive potentials dominate for this chemistry. The ingested corpus file is a corrected proof; assign the final Digital Object Identifier from the version of record when it appears in publisher metadata.

## Methods

### Membrane experiments (OSN)

**Polycrystalline** **TpPa-1** films; **permeance** + **solute rejection** in **mixed organic solvents** (**pharma**/fine-chemical-relevant conditions).

### Atomistic transport models (classical MD)

**Solvent–COF** interactions; **permeance** normalized to **water** to bridge **continuum** tests and **periodic** cells; **software**, **ensemble**, **duration**, **FF** (**fixed-bond** vs **reactive**) in **`papers/Barnes_Shin_COF_JMemSci_2024_galley.pdf`**—**not** restated here.

**MD application (classical, COF, mixed solvents).** The **Journal of Membrane Science** work uses an **MD** **package** (e.g. **GROMACS** or **LAMMPS** as named in the article) for **molecular dynamics** of **TpPa-1** **framework**+**solvent** cells; **N/A** for exact **atom** counts, **3D** **PBC** and **fixed** **framework** **protocols**, **NVT**/**NPT** choice, **0.25**–**1** **fs** **time step** ranges, and **Nosé–Hoover** **thermostat**+**NPT** **Parrinello**/**Berendsen** **barostat** for **chemical potential**-matched **permeation** if used—**Methods** in the **galley**/**VOR**. **Temperature**s match **OSN** conditions. **N/A**—**external electric field**; **N/A**—**metadynamics**; **Hydrostatic** **pressure** per **NPT** when the protocol applies (**N/A** in **NVT**-only segments).

## Findings

The authors report good agreement between modeled organic-solvent permeance/rejection trends and measured OSN data under explicit modeling assumptions. Where mismatch persists, they attribute discrepancies to realistic film microstructure effects such as linear polymer defects, grain boundaries, and interstitial percolation that bypass nominal pore channels—phenomena that a perfectly crystalline through-pore model would omit.

**Comparisons and limitations as authored.** The **permeance** and **solute** **rejection** story is explicitly **compared** to **experiment**; **sensitivity** to **film** **defects** explains residual gaps. The **DOI** will appear with the final **JMS** issue; see **## Limitations** for **proof** caveats.

## Limitations

Proof-stage PDFs can differ in pagination and editorial metadata from the final issue; operators should reconcile DOI, volume, and page numbers before citing locators. Force-field choices for COF–solvent systems should be verified in the Methods section because abstract-level summaries may not state whether bonds are fixed or reactive.

## Relevance to group

The paper illustrates atomistic digital-twin style workflows for advanced membranes with van Duin-group participation, connecting polymer/COF materials keywords to solvation and transport validation.

## MAS / retrieval notes

Agents should flag `candidate_tags` such as COF TpPa-1 and organic-solvent nanofiltration when building facet filters; until the final DOI is registered in frontmatter, retrieval answers should cite the corrected-proof caveat and avoid inventing pagination. Link to [[reaxff-family]] only after Methods confirm whether reactive or fixed-bond force fields dominate.

## Citations and evidence anchors

<!-- Add DOI when the issue/volume is finalized in `normalized/papers`. -->

## Related topics

- [[reaxff-family]]
