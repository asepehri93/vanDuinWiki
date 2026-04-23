---
id: paper:2013verners-venue-paper
type: paper
title: "Molecular dynamics simulation of Al grain mixing in Fe/Ni matrices and its influence on oxidation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
  - scale:atomistic
  - domain:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1063/1.4812387"
year: 2013
authors:
  - "Verners, O."
  - "Shin, Y. K."
  - "van Duin, A. C. T."
venue: "Journal of Applied Physics"
pdf_sha256: "46e38bdbda03b9b89e33ebdbce2f84c83ad8c83c3470b5bd48e85ccd67ee13ab"
pdf_path: "papers/Verners_JAP_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013verners-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Structural **AlₓNiᵧFe₍₁₋ₓ₋ᵧ₎** alloys are candidates for high-temperature energy systems where surfaces oxidize aggressively; understanding how **aluminum-rich grains** mix into **nickel** or **iron** matrices, and how that mixing couples to **oxidation**, motivates the simulations. Using **ReaxFF molecular dynamics**, Verners, Shin, and van Duin follow **aluminum grains** of different sizes embedded in **pure Ni** or **pure Fe** matrices at an approximate **1:3 grain:matrix atom ratio**. The study spans temperatures **above and below** the melting regime of the composite structures, with staged heating and subsequent cooling, and closes with **preliminary slab oxidation** simulations intended to connect grain–matrix mixing state to **oxygen attack** propensity.

## Methods

**1 — MD application (atomistic dynamics).** The abstract embedded in the **AIP author-query / proof** PDF on this slug states **ReaxFF-based molecular dynamics** at **constant pressure**, with temperature **stepwise ramped** from **300–3000 K** for **Al** grains in **pure Ni** or **pure Fe** matrices at an approximate **1:3** grain:matrix **atom** ratio, followed by **cooling** simulations from **3000 K** back to **300 K** (`papers/Verners_JAP_galley.pdf`; extract lines 47–64 in `normalized/extracts/2013verners-venue-paper_p1-2.txt`). **Additional preliminary slab oxidation** with **O\(_2\)** is mentioned qualitatively. **Engine / code, timestep, duration, thermostat types, PBC, and oxidation-slab protocol details:** **N/A —** not recoverable from the **proof** extract (publisher queries dominate early pages). **Barostat / pressure / ensemble:** the proof-page abstract states **constant-pressure** **ReaxFF** **MD** (**NPT**-class pressure coupling as detailed in **`papers/Verners_J_App_Phys_2013.pdf`** on the sibling slug and in the **JAP** **Methods**). **Electric field / enhanced sampling:** **N/A —** not stated in the excerpted abstract block.

**2 — Force-field training.** **N/A —** this is an **application** study using **ReaxFF**, not a parameterization release paper in the excerpted material.

**3 — Static QM / DFT-only.** **N/A —** reactive **MD** drives mixing and preliminary oxidation.

## Findings

**Outcomes & mechanisms.** The proof-page abstract reports **lower chemical strain energy** for **Al** in the **Ni** matrix and **mixing completed at lower temperature** than in the **Fe** matrix, interpreted as **Al–Ni** being energetically more stable than **Al–Fe**, consistent with experiment. **Larger Al grains** favor mixing with **Fe**, while **smaller grains** favor mixing with **Ni**, attributed to **formation-energy** and **bond-distance** differences. **Cooling** simulations find **Fe** alloy solidifies at **lower temperature** than **Ni** alloy for the stated cooling range; both yield **chemically disordered crystalline** products, with **Ni** described as **less ordered** than **Fe**. **Preliminary oxidation:** **unmixed Al** and **unmixed Ni** are the most **O\(_2\)**-active, while **Al/Ni alloy** and **pure Fe** oxidize more slowly in the slab comparison described in the abstract.

**Comparisons.** Explicit **experimental** agreement language appears in the abstract for **Al–Ni** vs **Al–Fe** stability trends.

**Sensitivity & design levers.** **Matrix identity** (**Ni** vs **Fe**), **Al grain size**, and the **300–3000 K** heating / **3000–300 K** cooling schedule are the primary knobs summarized on the proof excerpt.

**Limitations & outlook.** Oxidation simulations are labeled **preliminary** in the abstract; full quantitative kinetics require the **version-of-record** article text.

**Corpus honesty.** This slug tracks a **galley/proof** PDF; use **`paper:2013verners-venue-paper-2`** (`papers/Verners_J_App_Phys_2013.pdf`) for **VOR** figures and complete **Methods** tables.

## Limitations

Galley/proof PDF interleaved with author-query pages; quantitative plots not in p1–2 extract.

## Relevance to group

Structural alloy oxidation linked to energy-system materials modeling with van Duin authorship.

## Citations and evidence anchors

- DOI `http://dx.doi.org/10.1063/1.4812387` embedded in proof text (extract page 1).
- Abstract block lines 37–63 (extract).

## Related topics

- [[reaxff-family]]
