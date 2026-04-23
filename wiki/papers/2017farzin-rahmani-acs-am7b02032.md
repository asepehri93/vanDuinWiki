---
id: paper:2017farzin-rahmani-acs-am7b02032
type: paper
title: "Reactive molecular simulation of the damage mitigation efficacy of POSS-, graphene-, and carbon nanotube-loaded polyimide coatings exposed to atomic oxygen bombardment"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - material:polymer-organic
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:graphene-carbon
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.7b02032"
year: 2017
authors:
  - "Farzin Rahmani"
  - "Sasan Nouranian"
  - "Xiaobing Li"
  - "Ahmed Al-Ostaz"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "c4339f77aff73e8b563f502f7c1d3f87b439747fcb00bd93e07c9d27afdb578b"
pdf_path: "papers/ReaxFF_others/Rahmani_ACS_AMI_POSS_O_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017farzin-rahmani-acs-am7b02032 -->


**Reactive MD** compares **atomic oxygen** bombardment of **polyimide** nanocomposites loaded with **pristine vs PI-grafted POSS**, **graphene**, and **CNTs**, emphasizing **nanoparticle orientation** and **exposed PI** at the **surface**.

## Summary

**Reactive molecular dynamics** (methodology adapted from **Rahnamoun & van Duin**) models **hyperthermal AO** impacts on **PI** with **POSS**, **graphene**, or **CNT** fillers at controlled **wt %** and **alignment**. Observables include **mass loss**, **erosion yield**, **surface damage**, **AO penetration depth**, and **temperature rise**. **Random** **Gr/CNT** and **grafted POSS** generally outperform **pristine POSS** and **aligned** **Gr/CNT** at equal loading. **Exposed PI** (highest intrinsic **erosion yield**) dominates **composite erosion** when nanoparticles remain undamaged.

## Methods

**A — Force-field training / fitting:** **Reactive MD** follows methodology adapted from **Rahnamoun & van Duin**—**C/H/O/N** **ReaxFF** chemistry for **polyimide** and **nanofillers** without new **GA**/**QM training** details on this page (see **Computational details** in the article).

**B — Molecular dynamics / reactive sampling:** **Hyperthermal atomic oxygen** **bombardment** of **neat PI** and composites: **pristine vs PI-grafted POSS** (**15%**, **30%**), **random vs aligned** **graphene** and **CNT** (**15%**); simulation cells **~43–46 Å** (**Table 1**). Tracks **mass loss**, **erosion yield**, **damage**, **AO penetration**, **temperature rise**; **RDF** compares **POSS dispersion**.

**C — DFT / static QM:** **Not stated** as the primary layer in the summarized protocol—**ReaxFF** drives **reactive** **impact** simulations.

**D — Review / non-simulation framing:** **Application** study for **space-environment** **polyimide** **erosion**; **not** a review.

**Engine:** **LAMMPS** **ReaxFF** **reactive MD** for **hyperthermal atomic oxygen** impacts (per **Computational details** in **ACS Appl. Mater. Interfaces**). **System:** **neat polyimide** and **nanocomposite** **slabs** / **supercells** with **POSS** (**15%**, **30%**), **graphene**, and **CNT** (**15%**); lateral box sizes about **43–46 Å** (**Table 1**); **atom** totals and **stoichiometry** are tabulated in the **PDF**. **Ensemble:** **NVT** is the usual **impact** setup in this literature line; confirm the authors’ declared **ensemble** in **Computational details**. **Timestep / thermostat / duration / PBC / barostat:** **N/A —** not transcribed on this wiki page—copy from **`pdf_path`**. **Temperature:** **hot** **AO** beam conditions and **thermostat** settings are defined in the article’s **impact protocol**. **Pressure / gas:** **AO** **flux** and **beam energy** are specified in-source (not duplicated here). **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

## Findings

- **Random Gr/CNT** and **PI-g-POSS** show **lower** **mass loss**, **erosion**, **damage**, **penetration**, and **heating** than **pristine POSS** or **aligned** **Gr/CNT** at the **same** **nanoparticle** **concentration**.
- **Exposed PI area** on the **surface** is the **dominant** lever for **erosion yield** while nanoparticles remain **intact**—consistent with **early-stage** **experimental** degradation data cited in the paper.
- **PI-grafted POSS** achieves **much lower erosion** than **aligned** **Gr/CNT** systems because **less PI** is **exposed**; **grafting** vs **pristine POSS** lowers erosion by **~4×** (low conc.) and increasing **POSS** loading helps (**~1.5×**) via **better dispersion** (**RDF** evidence).
- **Aligned** **nanoparticles** leave **more PI** **uncovered**, raising **erosion** vs **random** **orientation**.

## Limitations

**Idealized PI monomer** representation and **specific AO** **flux/energy** window; extrapolation to **space mission** **environments** needs **experimental** **validation** beyond cited **early** data. The study’s conclusions are inherently **morphology- and orientation-dependent** (random vs aligned fillers), so quantitative **erosion yield** comparisons require care when translating to different **nanocomposite** processing histories.

## Relevance to group

**LEO AO + polyimide + ReaxFF** damage study—close to **prior van Duin-group** **AO/polymer** reactive MD cited in the introduction. Use this page when benchmarking **nanocomposite** erosion against **neat polymer** baselines under **hyperthermal oxygen** conditions relevant to **low Earth orbit** exposure models.

## Citations and evidence anchors

- DOI: [10.1021/acsami.7b02032](https://doi.org/10.1021/acsami.7b02032)
- Full article tables list **cell sizes** and **nanoparticle** loadings referenced in the Methods summary above.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
