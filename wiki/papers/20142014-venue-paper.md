---
id: paper:20142014-venue-paper
type: paper
title: "Property evolution of Al₂O₃ coated and uncoated Si electrodes: A first principles investigation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - material:li-metal-anode
  - material:oxide
  - method:dft-static
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:dft-static
  - keyword:batteries-interfaces
  - keyword:neb
  - keyword:oxide-surface
source_refs: []
doi: "10.1149/2.0301414jes"
year: 2014
authors:
  - "Sung-Yup Kim"
  - "Yue Qi"
venue: "J. Electrochem. Soc."
pdf_sha256: "3e4e2b1418685aa85612d57041968fdf353183c8a8e8b3e19dc9261ba4b41e17"
pdf_path: "papers/ReaxFF_others/2014_coating_property_Kim_JES.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:20142014-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. This is a **DFT** study of **coatings** on **Si** anodes—not a **ReaxFF** paper.

## Summary

**DFT** compares **ALD Al₂O₃** vs **native SiO₂** on **Si** as **Li-ion battery** anode coatings. Computed properties include **open-circuit voltage** trends vs **Li metal**, **elastic** moduli, and **Li diffusion** barriers in **SiO₂**, **Al₂O₃**, and **lithiated** phases (**Li₄SiO₄**, **LiAlO₂**). The abstract reports **lithiation** at voltages **above** **EC decomposition (~0.8 V)** as a source of **initial irreversible capacity**; **Al₂O₃** **softens** upon lithiation while **SiO₂** **stiffens slightly**; **Li** transport behaviors in **SiO₂** vs **Al₂O₃** **differ** strongly with **lithiation** degree, motivating **coating** design based on **post-lithiation** properties. The study is explicitly a **first-principles materials** comparison of **passivation** chemistries rather than a full **electrode–electrolyte** interface with explicit **liquid** degrees of freedom.

## Methods

### DFT framework (static PBE + PAW)

- **Projector-augmented-wave (PAW)** **PBE-GGA** relaxations of **Li**, **Si**, **Al**, and **oxide / silicate / aluminate** phases; **Table I** lists **cells**, **space groups**, and **k**-meshes (**article**).
- **Dispersion:** **N/A —** the wiki summary does not record a separate **DFT-D**/**vdW** correction layer beyond **PBE-GGA**; confirm whether the **JES** article adds **dispersion** in the **full** **Methods** text.
- **k-point sampling:** **Brillouin-zone** **k-meshes** per phase appear in **Table I** of the **article** (not duplicated numerically here).

### Properties computed from relaxed structures

- **Open-circuit voltage** trends vs **Li metal**, **elastic moduli**, and **Li diffusion** pathways assessed with **NEB**-style barrier searches along representative paths (**article** Methods).

### Material sets compared

- **Native SiO₂** vs **ALD Al₂O₃** coatings on **Si**, including **lithiated** end members such as **Li₄SiO₄** and **LiAlO₂** referenced in the abstract.

### Temperature / dynamics scope

- Results are **0 K static DFT** barriers and thermodynamics—**no** explicit **finite-temperature MD** or **electrolyte** in these calculations (**Limitations**).

**1 — MD application (atomistic dynamics):** **N/A —** not a production **MD** paper.

**2 — Force-field training:** **N/A —** not a force-field parameterization study.

**4 — Reviews / non-simulation:** **N/A —** primary content is **first-principles materials** modeling, not a literature review.

## Findings

- **Lithiation** is predicted **above ~0.8 V vs Li/Li⁺**, comparable to **EC decomposition**, contributing to **initial irreversible capacity** in the authors’ analysis.
- **ALD Al₂O₃ softens** upon lithiation, whereas **native SiO₂ stiffens slightly**, altering how each coating **accommodates Si volume change** in the DFT data presented.
- **Li transport** differs sharply: **SiO₂** shows **fast Li diffusion** early, but **barriers rise with lithiation** until **Li₄SiO₄**-like chemistry **lowers** them again; **Al₂O₃** is **poorly conducting** until **lithiation** drives **LiAlO₂**-like regions with **much lower barriers**, motivating **post-lithiation** coating design.
- Taken together, the DFT trends argue that **coating** performance should be judged after **substantial lithiation**, not only from pristine **oxide** properties.
- **Compared to experiments:** the framing is **first-principles** **trends** vs **EC** stability window and **coating** mechanics narratives in the **battery** literature (**Summary**); treat quantitative **agreement** with any specific **cell** data as **outside** this summary.
- **Sensitivity:** **Li** **diffusion** and **elastic** response change with **lithiation** degree and **oxide** polymorph (**SiO₂** vs **Al₂O₃** branches in **Findings**).
- **Limitations / outlook:** **0 K** static models omit **entropy**, **explicit electrolyte**, and **cycling** microstructure (**## Limitations**).
- **Corpus honesty:** `extraction_quality` is **partial** in front matter—operators should prefer the **PDF** for **Table I** meshes and any **dispersion** footnotes.

## Limitations

- **0 K DFT**; **electrolyte**, **interfaces**, and **cycling** mechanics are **not** fully atomistically resolved.
- **Finite-temperature** **entropic** effects and **explicit** **electrolyte** **decomposition** pathways are outside the static **barrier** picture summarized here.

## Relevance to group

**Interface** **oxide** **physics** adjacent to **ReaxFF** **battery** work; useful **DFT** reference for **ALD** **passivation** on **Si**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1149/2.0301414jes` (`papers/ReaxFF_others/2014_coating_property_Kim_JES.pdf`).

## Related topics

- [[batteries-interfaces-reaxff]]
