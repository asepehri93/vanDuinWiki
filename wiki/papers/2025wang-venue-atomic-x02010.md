---
id: paper:2025wang-venue-atomic-x02010
type: paper
title: "Atomic-Scale Mechanistic Insights into the Ring-Opening Polymerization of Elemental Sulfur (publisher proof PDF)"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - domain:reactive-md
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1002/anie.202511640"
year: 2025
authors:
  - "Mengyi Wang"
  - "Saied Md Pratik"
  - "Nadire Nayir"
  - "Maliheh Shaban Tameh"
  - "Veaceslav Coropceanu"
  - "Jean-Luc Bredas"
  - "Jeffrey Pyun"
  - "Adri C. T. van Duin"
  - "Shamil Saiev"
venue: "Angewandte Chemie International Edition"
pdf_sha256: "d86da515011cfa401af398b9f403a18459c211142823fd45dab535ba5b7d9132"
pdf_path: "papers/Wang_Sulfur_Angewandte_galley_2025.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025wang-venue-atomic-x02010 -->

## Summary

This wiki entry registers a **publisher proof / galley** PDF (`papers/Wang_Sulfur_Angewandte_galley_2025.pdf`) for the same *Angewandte Chemie International Edition* article as **`paper:2025wang-angew-atomic-scale`** (**DOI `10.1002/anie.202511640`**). The science targets **ring-opening polymerization (ROP)** in **molten elemental sulfur** near the **λ-transition**, where viscosity changes sharply and experimental characterization of transient polymeric sulfur species is difficult. The authors introduce a **ReaxFF parameterization specialized for sulfur polymerization**, trained against extensive **quantum mechanical** datasets, and apply it to **large-scale reactive molecular dynamics** with more than **10,000 atoms** to sample melt composition and mechanism at relevant temperatures. The work contrasts simulation outcomes with classical narratives emphasizing **S₈** rings and linear chains, reporting that **very large macrocyclic sulfur rings** can appear at polymerization onset.

## Methods

**1 — MD application (atomistic dynamics).** The reactive model is a **ReaxFF reparameterization** for **elemental sulfur** and its polymerization **chemistry**, with **parameters** fit to **QM** **reference** data spanning bonding environments and **reaction** energetics in the article and **Supporting Information**. **Simulations** use **classical reactive MD** in the **melt** near the **λ**-transition (reported as **~159** **°C**, or approximately **432 K** in the main text for MD targeting of the **λ** transition) with **>10,000** **atom** **composition**; the VOR’s **NVT** **(melt)** **production** plan specifies **thermostat** type (commonly **Berendsen** or **Nose**–**Hoover** in such LAMMPS-class runs) and **K**-resolved **ramps**—**N/A** to quote those **fs** **time** **step**, full **PBC** **slab**/**supercell** description, and **ps/ns** **stages** from this **galley** file alone. **N/A** on this page: full **NPT**/**NVE** **(branch)** **(if** **any**). **N/A** — **NPT** **barostat**/**bar** **(hydrostatic** **(GPa))** not restated here. **N/A** — **static electric field**; **N/A** — no **replica**/**metadynamics**; **N/A** — no **umbrella** sampling in the ROP **production** plan as cited on the canonical page. The **galley** may show **author-query** banners; confirm all numbers in the VOR.

**2 — Force-field training.** **ReaxFF** re-fit for **S** **ROP** with **DFT**/**QM**-based **training** and **parameter optimization**; **structures** and **reaction** targets in the main text and **SI**. **N/A** — this registrant file does not replace the **version-of-record** for **table**-level **QM** settings.

**3 — Static QM only** — **N/A** (supporting **QM** for the **ReaxFF** only).

**4 — Review** — **N/A.**
## Findings

- **Melt** **reaction** pathways, **kinetics**, and **mechanism**-level **composition** are interpreted in **reactive** MD, **compared** to **classical** models that cannot make/break bonds.
- **macrocycle**-rich pictures at ROP **onset** and **sensitivity** to **temperature** (near the **λ** transition) follow the VOR; **N/A** on this page for exact **reaction** **rates**—treat **2025wang-angew-atomic-scale** as the narrative **benchmark**.
- **Corpus honesty:** **galley** layout may differ; **author** may have revised **conclusions**; proof **page** numbers are not canonical.
## Limitations

Galley PDFs can differ in layout, pagination, and figure resolution from the **VOR**; **`pdf_sha256`** differs from the canonical **`papers/Wang_Angewandte_Sulfur_2025.pdf`** path on **`[[2025wang-angew-atomic-scale]]`**.

## Reproducibility notes

Sulfur ROP simulations should record **λ-transition** targeting temperatures, **thermostat** coupling, and whether **long-range** corrections are applied, because molten sulfur’s **ring–polymer** equilibrium is sensitive to both thermodynamics and kinetic accessibility. When comparing to experiment, distinguish **equilibrium** composition metrics from **transient** macrocycle populations sampled in finite MD. If the **galley** and **VOR** disagree on Supporting Information filenames, prefer the journal’s final SI package for **QM training** tables.

## Relevance to group

Duplicate ingest of the Angewandte sulfur ROP manuscript under a galley filename; modeling led by van Duin group collaborators.

## Citations and evidence anchors

- DOI: [10.1002/anie.202511640](https://doi.org/10.1002/anie.202511640)
- Primary curated page: [[2025wang-angew-atomic-scale]]

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- **Canonical article note:** `papers/Wang_Angewandte_Sulfur_2025.pdf` → [[2025wang-angew-atomic-scale]]; this slug tracks `papers/Wang_Sulfur_Angewandte_galley_2025.pdf`.
