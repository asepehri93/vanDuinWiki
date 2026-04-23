---
id: paper:2013somers-catalysis-to-temperature-influence-2
type: paper
title: "Temperature influence on the reactivity of plasma species on a nickel catalyst surface: An atomic scale study"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:metallic-systems
  - keyword:reactive-md
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reactive-md
  - material:metal-surface
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.cattod.2013.02.010"
year: 2013
authors:
  - "W. Somers"
  - "A. Bogaerts"
  - "A. C. T. van Duin"
  - "S. Huygh"
  - "K. M. Bal"
  - "E. C. Neyts"
venue: "Catalysis Today"
pdf_sha256: "a42c9002f93df7aa1f781cadb9911383652f627c78dbeb0978e08070f07425d0"
pdf_path: "papers/Somers_CatalysisToday_2013_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013somers-catalysis-to-temperature-influence-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

The **abstract** motivates **H\(_2\)** from **Ni-catalyzed methane reforming** and argues that **atomic-scale** insight is needed to interpret **surface** reactions. Reactive MD with **ReaxFF** follows **H\(_2\)** formation after **CH\(_x\)** fragments impact a **Ni(111)** surface from **400–1600 K**. **Some** H\(_2\) forms at **lower** temperatures, but **substantial** H\(_2\) production appears only at **≥ ~1400 K**; at **1600 K**, H\(_2\) is the **most frequently formed** species. In parallel, **surface-to-subsurface carbon diffusivity** rises with temperature alongside **dehydrogenation**, tying **plasma-surface** reactivity to **thermal** activation in a reforming-relevant **Ni/C/H** setting.

## Methods

**1 — MD application (atomistic dynamics).** Same study as [[2013somers-catalysis-to-temperature-influence]] (DOI **10.1016/j.cattod.2013.02.010**); this corpus row points at the **“article in press”** PDF (`pdf_path`). **Reactive MD** with **ReaxFF** follows **H\(_2\)** evolution after **CH\(_x\)** impacts on **Ni(111)** from **400–1600 K** per the abstract (`normalized/extracts/2013somers-catalysis-to-temperature-influence-2_p1-2.txt`). The **Ni(111)** **slab** models use **three-dimensional periodic boundary conditions** (**3D PBC**) as standard for surface **MD** in this article family (**Computational details** in **`pdf_path`**). **Thermostat / ensemble:** **Bussi** vs **Berendsen** comparison at **400 K** establishes equivalence; thermostatted segments are **NVT**/**canonical** as labeled in the full text. The introduction motivates **steam methane reforming**, **plasma–catalyst** synergies, and **CNT** growth precursors, then states that **consecutive CH\(_x\)** impacts at **400 K** are repeated with **Bussi** vs **Berendsen** thermostats to verify equivalence, before extending impacts from **800–1600 K** focused on **H\(_2\)**. **Engine / code, system size, boundaries, timestep, duration, barostat, pressure coupling:** **N/A —** not recoverable from the **p1–2** extract (it truncates at the start of **Section 2.1**); use the full PDF for **Computational details**. **Thermostat:** **Bussi** and **Berendsen** compared at **400 K** as above. **Temperature:** **400 K** cross-check; **800–1600 K** production window in the introduction’s plan; abstract summarizes **400–1600 K**. **Electric field / enhanced sampling:** **N/A —** not in the indexed excerpt.

**2 — Force-field training.** **N/A —** application of an existing **ReaxFF** parametrization (literature-cited in the article), not a new training paper.

**3 — Static QM / DFT-only.** **N/A —** **DFT** is cited comparatively in the introduction for **Ni** facet and **CH\(_4\)** chemistry at smaller scale.

## Findings

**Outcomes & mechanisms.** The abstract reports **some H\(_2\)** at lower **\(T\)**, **substantial H\(_2\)** only from **≥1400 K**, and **H\(_2\)** as the **most frequent** product species at **1600 K**, with **elevated dehydrogenation** and **higher surface-to-subsurface C diffusivity** at higher temperature.

**Comparisons.** The introduction connects to prior **DFT** and **MD** work on **Ni** facets and **CH\(_4\)** / **CH\(_x\)** reactivity; quantitative agreement statements live in the **Results**/**Discussion** of the PDF.

**Sensitivity & design levers.** **Temperature** is the main scanned variable in the abstract; **thermostat** family is checked at **400 K** for methodological consistency.

**Limitations & outlook.** Warm-plasma (**~1000–2000 K**) motivation is stated in the introduction; author-stated caveats beyond that require the full text.

**Corpus honesty.** This slug tracks an alternate **Catalysis Today** PDF hash; for **VOR** layout in another filename, see sibling **`paper:2013somers-catalysis-to-temperature-influence`**. Detailed MD settings are **PDF-grounded**, not extract-complete, for both slugs.

## Limitations

Single-crystal **Ni(111)** models omit **steps**, **alloys**, and **oxide** **overlayers** present on **supported** catalysts; **impact** simulations emphasize **short** **collision** sequences rather than **steady** **reforming** **conversion** at fixed **gas** **composition**. **ReaxFF** **Ni/C/H** chemistry carries **parameterization** uncertainty for **subsurface** **carbon** **solubility** and **diffusivity**, so **quantitative** **diffusion** **coefficients** should be cross-checked against the article’s discussion and any **SI** benchmarks.

## Relevance to group

This **Catalysis Today** study exemplifies **plasma–catalyst** **Ni/C/H** chemistry with **van Duin** **ReaxFF** involvement in an **Antwerp–PSU** collaboration.

## Citations and evidence anchors

- DOI: [10.1016/j.cattod.2013.02.010](https://doi.org/10.1016/j.cattod.2013.02.010)
- Extract: `normalized/extracts/2013somers-catalysis-to-temperature-influence-2_p1-2.txt`

## Related topics

- [[reaxff-family]]
- Nickel-catalyzed reforming and plasma–surface modeling
