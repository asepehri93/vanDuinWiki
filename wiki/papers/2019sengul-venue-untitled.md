---
id: paper:2019sengul-venue-untitled
type: paper
title: "Water-mediated surface diffusion mechanism enabling the Cold Sintering Process (Angew. Chem. proof)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - task:experiment-integrated
  - material:oxide
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:oxide-surface
source_refs: []
doi: "10.1002/anie.201904738"
year: 2019
authors:
  - "Mert Y. Sengul"
  - "Jing Guo"
  - "Clive A. Randall"
  - "Adri C. T. van Duin"
venue: "Angew. Chem. Int. Ed. (proof PDF, 2019)"
pdf_sha256: "3724d60336e21fabe320850e8be7bc36d28d2e7850272ec3a21a3fd4cc7afdc2"
pdf_path: "papers/Sengul_Angewandte_coldsintering_2019_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019sengul-venue-untitled -->

!!! abstract "Lead"

**Proof / editorial-markup PDF** for the *Angew. Chem. Int. Ed.* communication on **cold sintering** of **ZnO** with **experiments** and **ReaxFF MD** ([DOI 10.1002/anie.201904738](https://doi.org/10.1002/anie.201904738)). Prefer **`[[2019sengul-venue-water-mediated]]`** (or **`[[2019sengul-venue-water-x2010]]`**) for version-of-record curation.

## Summary

Cold sintering processes densify ceramic powders at dramatically lower temperatures than conventional thermal sintering by exploiting transient aqueous films that mediate dissolution–reprecipitation and grain-boundary mobility. This *Angewandte Chemie International Edition* communication (DOI `10.1002/anie.201904738`) combines experiments on zinc oxide with ReaxFF molecular dynamics to argue that reduced activation energies for grain growth under cold sintering arise from acidic, water-mediated surface chemistry rather than from conventional bulk diffusion alone. The mechanistic picture highlights that acidic transients strengthen Zn²⁺ surface adsorption and that hydroxylation can mobilize surface species that accelerate diffusion and recrystallization instead of merely passivating the oxide. Adri C. T. van Duin is a coauthor, linking the work to the group’s reactive modeling of oxide interfaces in electrochemical and processing environments. This wiki slug registers **proof** PDF bytes; narrative alignment and stable pagination should be checked against **`[[2019sengul-venue-water-mediated]]`** or related version-of-record slugs.

## Methods

**Proof** **PDF** **role:** **N/A** to treat this **ingest** as the **sole** **authoritative** **protocol**; **`[[2019sengul-venue-water-mediated]]`** **and** the **VOR** / **SI** have **typeset** **figure**-**to**-**Methods** **mapping**.

**Experiments / MD (summary).** **CSP**-style experiments on **ZnO** and **ReaxFF** **molecular** **dynamics** of hydrated and acidified **ZnO** surfaces rationalize the low **activation** energy for **grain** growth via water-mediated **surface** pathways. **1 — MD:** **3D** **PBC** supercells with **thousands of atoms** (exact **supercell** in *Angew.* **VOR**); **NVT** or **NPT** **ensemble** with **timestep** on the order of **0.1** **fs** and **equilibration**/**production** **ps**–**ns** spans and **Nose**–**Hoover** **thermostat** as in the **VOR**; **LAMMPS** is the typical **engine** for this **ReaxFF** line ( **confirm** in **SI**). **Temperature** **~300** **K** and other **K** targets for **surface** **diffusion** **analysis** are in the **main** **text**. **Hydrostatic** **pressure** in **MD** ( **bar** ) and any **Parrinello**–**Rahman** **barostat** **N/A** to reproduce on this **proof** **slug**—**use** **VOR**. **2 — Force-field training: N/A.** **3 — Electric** **field, umbrella, metadynamics: N/A** unless the **VOR** adds them.

## Findings

**Synthesis (aligned with the communication).** The work posits that **CSP** reduces the **apparent** **activation** **energy** for **grain** **growth** in **ZnO** by **surface**-mediated pathways where **H⁺**-rich, water-containing transients make **Zn²⁺** **adsorption** and **transport** kinetically accessible, relative to **conventional** sintering—**and** that **hydroxylation** is not merely a passivating, lubricant-only effect in the **ReaxFF**-supported **picture**.

**Comparisons / levers** follow **figures** on the **VOR**; **this** **proof** **page** is **not** where **extraction** **should** end for **d** **vs** **T** **kinetics** **or** **prefactors**.

**Limitations (corpus).** **Proof** **duplicates** may have **reordered** **figures**; use **`[[2019sengul-venue-water-mediated]]`**. **Reaxff** **caveats** in the **Limitations** **section** below still apply.

## Limitations

Proof PDFs may retain editorial markup, altered line breaks, and non-final author affiliations; readers preparing citations should download the issue PDF from the publisher. ReaxFF models of acidified oxide interfaces inherit force-field approximations for proton transfer and charged defects that require contextual validation.

## Relevance to group

The publication is a flagship example of ReaxFF applied to oxide processing with experimental co-validation, useful for theme hubs linking ceramics, aqueous interfaces, and reactive force fields.

## Citations and evidence anchors

- DOI: [10.1002/anie.201904738](https://doi.org/10.1002/anie.201904738)

## Reader notes (navigation)

- Version-of-record: [[2019sengul-venue-water-mediated]]  
- [[reaxff-family]], [[theme-oxides-silica-ceramics]]

## Related topics

- [[2019sengul-venue-water-mediated]]
- [[2019sengul-venue-water-x2010]]
- [[reaxff-family]]
