---
id: paper:2019sengul-venue-water-x2010
type: paper
title: "Water-mediated surface diffusion mechanism enabling the Cold Sintering Process: a combined computational and experimental study"
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
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:validation-experiment
source_refs: []
doi: "10.1002/anie.201904738"
year: 2019
authors:
  - "Mert Y. Sengul"
  - "Jing Guo"
  - "Clive A. Randall"
  - "Adri C. T. van Duin"
venue: "Angew. Chem. Int. Ed. (Accepted Article PDF)"
pdf_sha256: "dfddab84da8855de5765085662fd811fafb1bc94cce75d65361f3cfd75785c3e"
pdf_path: "papers/SENGUL_et_al-2019-Angewandte_Chemie_International_Edition.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019sengul-venue-water-x2010 -->

## Summary

This slug registers an **Angewandte Chemie** **Accepted Article** PDF (`SENGUL_et_al-2019-Angewandte_Chemie_International_Edition.pdf`) for the same communication as **`[[2019sengul-venue-water-mediated]]`**, **DOI [10.1002/anie.201904738](https://doi.org/10.1002/anie.201904738)**. The work combines **cold sintering process (CSP)** **experiments** on **ZnO** with **ReaxFF molecular dynamics** to explain **fast grain growth** at **low temperature**. The abstract argues that **CSP** densifies ceramics at temperatures far below conventional sintering; for **ZnO**, **grain growth** kinetics show **reduced activation energies**, and the **atomistic** mechanism is investigated with simulations. **Zinc cation** **recrystallization** under **acidic** conditions is examined; **adsorption** of **Zn²⁺** to surfaces can be **rate-limiting**. **Surface hydroxylation** under **CSP** is found **not** to freeze crystallization—instead, hydroxylation forms **surface complexes** that **accelerate surface diffusion** by **orders of magnitude**, speeding **recrystallization**. The **Accepted Article** may differ in layout from the **final Version of Record**; use the **`water-mediated`** sibling when matching pagination to citations. The communication emphasizes **sustainable processing** motivations for **low-temperature** ceramic densification and cites breadth of **CSP** applicability across many **inorganic** systems in the opening paragraphs—those survey claims are part of the published framing and should be read alongside the **ZnO**-specific simulation evidence in the same paper.

## Methods

**Experiments:** **CSP** densification / **grain growth** measurements for **ZnO** under conditions described in the paper and SI.

**ReaxFF MD:** **Molecular** **dynamics** in **LAMMPS** for **ReaxFF** (see the **VOR** on `[[2019sengul-venue-water-mediated]]` for the exact **package** string). **ZnO** **slabs** in **3D** **PBC** with **water** and **acid**-**related** **species**; **NVT** or **NPT** **ensemble**; **Nose**–**Hoover**-class **thermostat**; **timestep** **0.1**–**0.5** **fs**; **equilibration** and **production** **ps**–**ns** in the **SI**; **~10³**-scale **atoms**; **~300** **K** and other **temperatures** in **K** as in the **VOR**. **Hydrostatic** **pressure** with **NPT** **Parrinello**–**Rahman** **barostat** is **N/A** to re-specify on this **duplicate** **PDF**—**use** the **VOR** **/ ** **SI** for **bar** targets. **External** **E**-**field**, **shear**, **umbrella**: **N/A** if **unstated**. **2 — ReaxFF reparameterization: N/A.** This **slug** is a **hash**-**level** **Accepted** **Article** **duplicate** only.

## Findings

**Surface-mediated diffusion** is central to the proposed **CSP** mechanism: **hydroxylation** correlates with large increases in modeled **surface mobility**, consistent with accelerated **grain growth** relative to conventional sintering. **Zn** **surface chemistry** under **acidic** pathways can be **kinetic**ally limiting. Full quantitative barriers and figures should be taken from the **VOR** or the primary wiki page when figures differ between PDFs.

## Limitations

**Accepted Article** text may not match **final** proofreading. Models focus on **ZnO**; other **CSP** chemistries need separate validation. **ReaxFF** surface chemistry is parametrization-dependent; compare **DFT** benchmarks or **experimental** grain-growth exponents when available before exporting **barrier** values into wider **sintering** databases. Keep **SI** **structures** and **simulation** **cells** as the authoritative numerical reference for **MD** reproduction.

## Relevance to group

Core **oxide / sintering** **ReaxFF** contribution with **experimental** validation (**van Duin** co-author).

## Citations and evidence anchors

- DOI: [10.1002/anie.201904738](https://doi.org/10.1002/anie.201904738)

## Reader notes (navigation)

- Primary Accepted Article / VoR path: [[2019sengul-venue-water-mediated]]

## Related topics

- [[2019sengul-venue-water-mediated]]
- [[reaxff-family]]
