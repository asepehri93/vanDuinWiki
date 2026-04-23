---
id: paper:2013somers-catalysis-to-temperature-influence
type: paper
title: "Temperature influence on the reactivity of plasma species on a nickel catalyst surface: An atomic scale study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
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
  - "K. M. Bala"
  - "E. C. Neyts"
venue: "Catalysis Today 211 (2013) 131–136"
pdf_sha256: "a90d719d4b7bf345ad05c532837a39b58929cb45e24d671d9fff7dbc7b5299c5"
pdf_path: "papers/Somers_CatalysisToday_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013somers-catalysis-to-temperature-influence -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Plasma–catalyst** systems aim to combine **non-equilibrium** gas activation with **metal** selectivity, but elementary steps at the **Ni** surface depend strongly on **temperature** when **CHx** radicals impact the catalyst after **plasma** activation. Somers *et al.* simulate **consecutive CHx impacts** on **Ni(111)** from **400 K to 1600 K** using **ReaxFF MD**, focusing on **H₂** formation efficiency as **temperature** rises—motivated by **warm-plasma** regimes where **gas heating** may synergize with **surface** reactivity. The work connects to **steam methane reforming** and **plasma-assisted** **CNT** growth literatures where **CHx** and **H₂** are co-present.

## Methods

**1 — MD application (atomistic dynamics).** The publication reports **reactive molecular dynamics** using the **ReaxFF** reactive force field for **H\(_2\)** formation after **CH\(_x\)** species impact a **Ni(111)** surface, motivated by **plasma–catalyst** and **CH\(_x\)** / **H\(_2\)**-relevant contexts discussed in the introduction (*Catalysis Today* **211**, 131–136; `pdf_path`). **Engine / code:** **N/A —** the indexed extract (`normalized/extracts/2013somers-catalysis-to-temperature-influence_p1-2.txt`) begins **Section 2** but truncates before naming an MD package; confirm in the full PDF. **System size & composition, boundaries, timestep, duration, ensemble (beyond thermostat tests), barostat, pressure control:** **N/A —** same truncation; the article’s **Computational details** section in the PDF should be used for supercell geometry, periodicity, integration settings, and run lengths. **Thermostat / ensemble:** the authors explicitly compare **Bussi** and **Berendsen** thermostats for **consecutive CH\(_x\)** impacts at **400 K** on **Ni(111)** to demonstrate equivalence for this system before comparing to their prior **400 K** work; thermostatted segments follow **NVT**-style **canonical** thermal control as described in *Catalysis Today* **211** (full labeling in **`pdf_path`**). **Temperature:** **400 K** (thermostat cross-check), then **800–1600 K** for consecutive impacts focused on **H\(_2\)** formation; the abstract summarizes **400–1600 K** overall. **Electric field:** **N/A —** not stated in the indexed extract. **Replica / enhanced sampling:** **N/A —** not stated in the indexed extract.

**2 — Force-field training.** **N/A —** this work applies an existing **ReaxFF** formulation (cited in the article) rather than reporting a new parameterization fit in *Catalysis Today* **211**.

**3 — Static QM / DFT-only.** **N/A —** central results are **ReaxFF MD**; **DFT** appears in the introduction as context for smaller-system studies of **CH\(_4\)** on **Ni** facets.

## Findings

**Outcomes & mechanisms.** The abstract states that **some H\(_2\)** already forms at **lower** temperatures, while **substantial H\(_2\)** formation appears only at **elevated** temperatures of **1400 K** and above; at **1600 K**, **H\(_2\)** is even the **most frequently formed** species. **Dehydrogenation** strengthens with temperature, and **surface-to-subsurface C diffusivity** increases in parallel—linking **H\(_2\)** yields to **thermal** activation after **CH\(_x\)** impacts in this model.

**Comparisons.** The introduction situates **Ni(111)** reactivity relative to **DFT** and prior **MD** literature on **Ni(100)**, **steps**, and **CH\(_4\)** dehydrogenation sequences; definitive numerical comparisons beyond the abstract require the **Results** section in the PDF.

**Sensitivity & design levers.** **Temperature** is the primary lever explored across **400–1600 K** in the abstract framing; **thermostat** choice at **400 K** is explicitly checked for robustness.

**Limitations & outlook (as authored).** The introduction frames **warm-plasma** (**~1000–2000 K**) gas heating as motivation for extending temperature beyond prior **400 K** **CH\(_x\)** impact work; detailed author limitations appear in the full article.

**Corpus honesty.** The local **`normalized/extracts/`** snippet ends at the opening of **Section 2.1**; integration-level protocol numbers (timestep, cell size, impact rate) are **not** recoverable from that excerpt alone—use **`pdf_path`** for authoritative **Methods** tables.

## Limitations

The model uses an **idealized Ni(111)** template and **beam-like** **CHx** delivery rather than a full **reactor** mixture with **coverage**, **steps**, and **oxide** phases; **long-time** **coking** chemistry is outside the simulated window.

## Relevance to group

Illustrates **ReaxFF + catalysis** collaborations (Antwerp PLASMANT + van Duin) for nickel surfaces and high-T hydrocarbon chemistry.

## Citations and evidence anchors

- DOI: [10.1016/j.cattod.2013.02.010](https://doi.org/10.1016/j.cattod.2013.02.010)
- Abstract: `normalized/extracts/2013somers-catalysis-to-temperature-influence_p1-2.txt`

## Related topics

- [[reaxff-family]]
- Nickel surface chemistry and methane-derived CHx fragments
- High-temperature reactive MD for catalysis
