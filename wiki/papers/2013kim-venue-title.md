---
id: paper:2013kim-venue-title
type: paper
title: "Molecular dynamics simulations of the interactions between TiO₂ nanoparticles and water with Na⁺ and Cl⁻, methanol, and formic acid using a reactive force field"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:oxides-ceramics, domain:water-silica-geo, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1557/jmr.2012.367"
year: 2013
authors: ["Kim, Sung-Yup", "van Duin, Adri C. T.", "Kubicki, James D."]
venue: "Journal of Materials Research"
pdf_sha256: "716cba7fb22a1e9e5ab76a44ade927da66576717551217132508eaca4a699339"
pdf_path: "papers/Kim_TiO2_clusters_JMR_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013kim-venue-title -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes **J. Mater. Res.** **28**, **513**–… (**DOI** in front matter). Numerical trends (**dissociative adsorption** fractions, **distortion** metrics) must be taken from the **article** tables/figures.

## Summary

The article reports **ReaxFF molecular dynamics** of **~1 nm** **rutile** and **anatase** **TiO₂ nanoparticles** interacting with **water** (with **Na⁺/Cl⁻**), **methanol**, and **formic acid**. The goal is to compare **nanoparticle-scale** **reactivity** and **structural distortion** across **polymorphs** and **adsorbates** at computational scales inaccessible to routine **DFT** trajectories. The introduction surveys extensive prior **DFT** and **experimental** literature on **TiO₂** surfaces and **nanoparticles**, highlighting controversies about **dissociative vs molecular** adsorption for **water** and **organic acids** on **anatase** facets, and motivates **ReaxFF** as a way to treat **larger** **nanoparticle** models with **reactive** **MD**.

The abstract states that the **force field** is **validated** by comparing **water dissociative adsorption percentages** and **Na–O bond lengths** against **DFT** and **experiment**. Reported simulation trends include **higher reactivity for rutile than anatase** for the observables discussed, and **stronger nanoparticle distortion** with **formic acid** than with **water** or **methanol**. **Attached hydroxyl** counts versus time are presented as a **quantitative** probe of **surface** **reaction** progression.

## Methods

**Sources:** **`papers/Kim_TiO2_clusters_JMR_2013.pdf`** and `normalized/extracts/2013kim-venue-title_p1-2.txt` (title page + introduction through motivation).

**1 — MD application.** **Reactive molecular dynamics** uses the **ReaxFF TiO₂/H₂O** parameterization cited in the article. **Engine / code:** **MD** package **N/A** on indexed excerpt pages—confirm (**LAMMPS** is typical for **ReaxFF** in this group’s corpus) in the **PDF** **Methods**. **System size & composition:** **~1 nm** **rutile** and **anatase** **TiO₂ nanoparticles** (hundreds of **atoms** per particle implied by size class) with **water**, **methanol**, **formic acid**, and **Na⁺/Cl⁻** **electrolyte** setups as described in the article. **Boundaries / periodicity:** **N/A** — explicit **PBC** vs cluster treatment not stated on **p1–2** extract. **Ensemble / thermostat / barostat / timestep / duration:** **N/A** for exact **NVT**/**NPT**, **Berendsen**/**Nosé–Hoover** parameters, **fs** **timestep**, and **ps**/**ns** **production** lengths—retrieve from full **Methods** in **`pdf_path`**. **Temperature:** **N/A** on excerpt (likely room **temperature** in main text—verify). **Pressure:** **N/A** on excerpt. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**. **Analysis:** time series of attached **hydroxyl** groups and **nanoparticle** **distortion** metrics versus **adsorbate** choice (**abstract**).

**2 — Force-field training.** **N/A** — applies an existing **TiO₂/H₂O** **ReaxFF** line; fitting details live in the cited parameterization papers.

**3 — Static QM.** **N/A** as primary production method; **DFT**/**experiment** are **validation** references named in the **abstract**.

## Findings

**Outcomes & mechanisms:** **Abstract**-level trends: **rutile** **nanoparticles** appear more **reactive** than **anatase** for the reported metrics; **formic acid** causes stronger **structural** **distortion** than **water** or **methanol**; **hydroxyl** attachment versus time tracks **surface** **reaction** progression.

**Comparisons:** The **force field** is **validated** against **DFT** and **experiment** for **water dissociative adsorption** percentages and **Na–O** bond lengths (**abstract** claims).

**Sensitivity / design levers:** **Polymorph** choice (**rutile** vs **anatase**) and **adsorbate** identity dominate **reactivity**/**distortion** rankings at **~1 nm** scale.

**Limitations & outlook:** **Curvature**/**facet** ensembles on **nanoparticles** differ from single-crystal **DFT** slabs; **ReaxFF** remains empirical—see author caveats in the **PDF**.

**Corpus honesty:** Indexed extract stops early in the introduction; all numerical **MD** settings and statistical uncertainties must be taken from the full **`pdf_path`**, not from this short snippet.

## Limitations

**~1 nm** particles emphasize **curvature** and **undercoordination** effects that may differ from **macroscopic** **single-crystal** experiments. **ReaxFF** remains **empirical**; **quantitative** agreement with **DFT** should be checked for each **new** **coverage** and **electrolyte** composition.

The **rutile vs anatase** comparison in the abstract is a useful **retrieval** hook for **oxide** **polymorph** sensitivity: even at **nanoparticle** sizes, **facet** and **phase** effects can reorder **reactivity** rankings relative to extended-surface literature.

## Relevance to group

Application-focused **oxide nanoparticle–fluid** chemistry using **ReaxFF**, coauthored by **van Duin** and **Kubicki**, connecting **materials** **simulation** to **geochemical** and **interface** science.

## Citations and evidence anchors

- DOI [10.1557/jmr.2012.367](https://doi.org/10.1557/jmr.2012.367); *J. Mater. Res.* **28** (**3**), **513** (2013).
- Excerpt alignment: `normalized/extracts/2013kim-venue-title_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
