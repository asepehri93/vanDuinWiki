---
id: paper:2013huang-venue-paper-3
type: paper
title: "Controllable atomistic graphene oxide model and its application in hydrogen sulfide removal"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:reactive-md
  - keyword:water-interfaces
  - keyword:lammps
source_refs: []
doi: "10.1063/1.4832039"
year: 2013
authors:
  - "Huang, Liangliang"
  - "Seredych, Mykola"
  - "Bandosz, Teresa J."
  - "van Duin, Adri C. T."
  - "Lu, Xiaohua"
  - "Gubbins, Keith E."
venue: "The Journal of Chemical Physics"
pdf_sha256: "b9bf26f0d052578e5c0c2921f3ba5372dafa969f02723d322883b188f26e24df"
pdf_path: "papers/Huang_GrapOxide_H2S_JCP2013.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013huang-venue-paper-3 -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter. The corpus PDF includes **AIP boilerplate** pages; `extraction_quality` remains **partial** until a clean extract is regenerated.

## Summary

Uses **temperature-programmed MD** with **ReaxFF** to generate **atomistic graphene oxide (GO)** models by grafting **epoxy** and **hydroxyl** groups with tunable concentrations, aiming to match **experimental** structural fingerprints and selected **QM** benchmarks. The constructed models are then used for **reactive adsorption** simulations of **H₂S**, including **H₂O/H₂S** mixtures, interpreting **dissociation** at **carbonyl**-class sites and release of **H₂O**, **CO₂**, and **CO** as chemistry progresses. **Water** is found to **compete** for carbonyl sites, suppressing **H₂S** reactivity in mixtures—consistent with the authors’ experimental comparison.

## Methods

**1 — MD application** (`papers/Huang_GrapOxide_H2S_JCP2013.pdf`; abstract + intro in `normalized/extracts/2013huang-venue-paper-3_p1-2.txt`). **Engine / code:** **Reactive molecular dynamics** with **ReaxFF** in **LAMMPS** as stated in the article body summarized on this page. **System size & composition:** **Graphene** sheets are **oxidized** by grafting **epoxy** and **hydroxyl** groups with tunable **composition** to build **GO supercells** containing many **carbon atoms** plus oxygen/hydrogen; exact counts per realization are in the **PDF** Methods (not on the short extract). **H₂S** and **H₂O/H₂S** runs use the generated **GO** slabs with adsorbates as specified there. **Boundaries / periodicity:** **three-dimensional periodic boundary conditions** (**PBC**) / in-plane **periodicity** as standard for the **LAMMPS** cells described in the article (confirm non-periodic variants, if any, in **PDF**). **Ensemble:** **NVT** for both the **temperature-programmed** construction stage (**300–2300 K** ramp at **0.005 K/iteration**) and the **300 K** **H₂S** production segments. **Timestep:** **0.25 fs** (**velocity Verlet**) for the **200 ps** **H₂S** window quoted in prior curation (verify in **PDF**). **Duration / stages:** **temperature-programmed** anneal for **GO** build; **200 ps** reactive sampling for **H₂S**/**mixture** cases (plus any **equilibration** legs tabulated in **Methods**). **Thermostat:** **Berendsen** with **τ = 100 fs** for the **300 K** **H₂S** protocol as stated in the article. **Barostat:** **N/A** — **constant-volume** **NVT** legs summarized here. **Pressure:** **N/A** — no **NPT** hydrostatic **pressure** target stated for these cells on the indexed excerpt. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**. **Connectivity tracking:** bond-order criterion at **20%** of equilibrium bond length (article **Methods**).

**2 — Force-field training.** **N/A** as a standalone new fit: the work **applies** published **ReaxFF** chemistry while **benchmarking** motifs with **DFT** where the article specifies.

**3 — Static QM.** **DFT** checks on selected **GO** motifs as cited against **QM** references in the article (**functional**/**basis** details in **PDF**).

## Findings

**Outcomes & mechanisms:** **H₂S** **dissociates** at **carbonyl**-class oxygen sites on the modeled **GO**, releasing **H₂O**, **CO₂**, and **CO** as **reaction** products in the **ReaxFF** trajectories summarized by the authors. In **H₂O/H₂S** **mixtures**, **H₂O** **preferentially adsorbs** to **carbonyl** sites and **blocks** **H₂S** access to those **reactive** sites.

**Comparisons:** Abstract states agreement between calculation and **experiment** for mixture **trends** on **GO** materials studied.

**Sensitivity / design levers:** **Temperature-programmed** construction tunes epoxy/hydroxyl **concentrations** and defect content; **H₂O**/**H₂S** **concentration** controls competitive **adsorption** at **carbonyl** sites.

**Limitations & outlook:** **Amorphous** **GO** realizations are non-unique; longer **production** runs and broader **composition** sweeps may be needed for quantitative sorption isotherms—see authored caveats in the **PDF**.

**Corpus honesty:** **`extraction_quality: partial`** for this slug; this page is grounded in **`pdf_path`**, the **DOI** abstract/intro extract, and the Methods bullets already published in the wiki—confirm every numerical protocol line against **`papers/Huang_GrapOxide_H2S_JCP2013.pdf`**.

## Limitations

GO structural disorder is vast; any single atomistic realization is illustrative. Quantitative sorption isotherms require longer sampling and broader composition sweeps. Where `extraction_quality` is partial, the tracked **PDF** and **DOI** remain the quantitative authority over short local extracts.

## Relevance to group

**van Duin** co-authorship on **ReaxFF** for **functionalized graphene** in environmental **sulfide** chemistry.

## Citations and evidence anchors

- Abstract and Sec. 1: GO model + H₂S chemistry claims (J. Chem. Phys. **139**, 194707 (2013); DOI above).

## Related topics

- [[graphene-nanocarbon]]
- [[reaxff-family]]
