---
id: paper:2022schulze-venue-paper
type: paper
title: "JOM author proof — PVA hydrogels with LiCl vs KCl (ReaxFF MD)"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1007/s11837-022-05482-y"
year: 2022
authors:
  - "Jessica A. Schulze"
  - "Malgorzata Kowalik"
  - "Adri C. T. van Duin"
venue: "JOM (proof PDF)"
pdf_sha256: "563100c88b74857a01ffb578208989013e115d7e6348c21e0164772500123170"
pdf_path: "papers/Schulze_JOM_polymer_cation_2022_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2022schulze-venue-paper -->

## Evidence and attribution

!!! note "Proof duplicate"

    **`[[2022schulze-jom-https-do-investigation-mechanical]]`** is the **version-of-record** PDF path for **DOI** `10.1007/s11837-022-05482-y`. This slug tracks the separate **publisher proof** bytes (`papers/Schulze_JOM_polymer_cation_2022_galley.pdf`).

## Summary

This page tracks a **JOM publisher proof** PDF (`papers/Schulze_JOM_polymer_cation_2022_galley.pdf`) for the article with DOI `10.1007/s11837-022-05482-y` on **ReaxFF molecular dynamics** of **poly(vinyl alcohol) (PVA) hydrogels** in **LiCl** versus **KCl** **electrolytes**, with **Adri C. T. van Duin** as a senior collaborator. The scientific story—developed fully on [[2022schulze-jom-https-do-investigation-mechanical]]—connects **ion-specific** **interfacial** chemistry to **macroscopic** **mechanical** trends measured experimentally: **Li⁺** environments are associated with pathways that **deprotonate** **hydroxyls** and disrupt **intra-/interchain** **hydrogen bonding**, while **K⁺** conditions better preserve **H-bond** **percolation** and **stiffer** **network** responses in the comparisons highlighted. This **slug** exists because the manifest retains **proof** bytes separately from the **final** **layout** PDF for provenance and hash alignment. For **MAS** retrieval, treat this note as a **duplicate-ingest** pointer: the **scientific** **claims** should be indexed from the **VOR** page unless an operator explicitly needs to cite the **proof** file’s **hash** or **publisher** state.

## Methods

### Corpus role (publisher proof duplicate)

Tracks **`papers/Schulze_JOM_polymer_cation_2022_galley.pdf`** separately from the **VOR** for **hash** provenance—**not** the canonical **Methods** locator.

### Protocol pointer (mirrors VOR)

Same **ReaxFF/LAMMPS** **PVA** + **LiCl/KCl** **electrolyte** story as **`[[2022schulze-jom-https-do-investigation-mechanical]]`**; take **ion** concentrations, **box**, **equilibration**, **deformation**, and **`ffield`** inputs from the **published** article/SI (**proof** may break equations across lines).

For reader-facing detail, **`[[2022schulze-jom-https-do-investigation-mechanical]]`**: **ReaxFF** in **LAMMPS**, **explicit water** with **Li⁺/K⁺/Cl⁻**; analysis includes **proton transfer** and **H-bond** / **ion coordination** contrasting **LiCl** vs **KCl**. This **proof** file does not replace the *JOM* **Methods** for **supercell** size, **timestep (fs)**, **ensemble** (**NVT**/**NPT**), **thermostat** parameters, or **trajectory** **length**; take those from the **VOR** and **SI**.

### MD application (readout; proof duplicate)

**Engine / code, system (including **supercell** **atom** count and **stoichiometry**), PBC, ensemble, timestep, **equilibration** and **production** **duration (ps/ns)**, **thermostat** coupling, **QEq/cutoffs,** and **room-temperature** or other **K**-scale **setpoints**:** as on the VOR. **N/A** — this duplicate page does not restate numerical values. **N/A** — no **static electric field** in the ReaxFF setup summarized. **N/A** — no **barostat** for constant-volume ReaxFF unless the VOR uses **NPT**; **N/A** — no **umbrella** or **replica** **sampling** beyond **MD** in the work summarized.

## Findings

### Scientific substance (duplicate of VOR)

**Li⁺** conditions favor **deprotonation** and **H-bond** loss (**softer** networks); **K⁺** tends to preserve denser **H-bond** networks (**stiffer** response)—the **mechanism** the authors connect to **ion-specific** **Hofmeister**-style behavior versus **K⁺**-penetration pictures. **Compared** to **experimental** **salt-soak** **PVA** (freeze–thaw) **toughness** and **modulus** ranges, **sensitivity** to **salt** identity and **ion** **concentration** is a central axis; see **VOR** **Results** and **SI** (not the **proof** **PDF** alone). **Open question:** which **kinetic** steps limit **gelling** in **lithium** systems beyond the atomistic H-bond statistics sampled—an **outlook** left to follow-on work in the field. This **proof**-ingest page defers to the **VOR** for all **version-of-record** **pagination**; **uncertainty** from **layout** on **this** file should be resolved against the final **issue** **PDF** when available.

## Limitations

Proof PDFs may differ in **layout**, **line breaks**, or **figure resolution** from the **final** issue. Prefer the **VOR** `pdf_path` on [[2022schulze-jom-https-do-investigation-mechanical]] for citation-ready reading.

## Relevance to group

**Workflow duplicate** for a **group-authored** **JOM** **ReaxFF** biomaterials paper.

## Reader notes (navigation)

- VOR article: [[2022schulze-jom-https-do-investigation-mechanical]]

## Citations and evidence anchors

- DOI: [10.1007/s11837-022-05482-y](https://doi.org/10.1007/s11837-022-05482-y)

## Related topics

- [[reaxff-family]]
