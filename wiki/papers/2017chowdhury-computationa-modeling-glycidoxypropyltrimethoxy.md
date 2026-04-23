---
id: paper:2017chowdhury-computationa-modeling-glycidoxypropyltrimethoxy
type: paper
title: "Modeling of glycidoxypropyltrimethoxy silane compositions using molecular dynamics simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - method:classical-md
  - material:silicate-glass
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:polymer
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2017.08.033"
year: 2017
authors:
  - "Sanjib C. Chowdhury"
  - "Robert M. Elder"
  - "Timothy W. Sirk"
  - "Adri C. T. van Duin"
  - "John W. Gillespie Jr."
venue: "Comput. Mater. Sci."
pdf_sha256: "12eec05fa248593d37574a4f62bf48395450d92be80d9b5054e7bc59851b4bf3"
pdf_path: "papers/Chowdhury_Sanjib_gdpt_silane_CompMatSci_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017chowdhury-computationa-modeling-glycidoxypropyltrimethoxy -->

## Summary

Reactive and non-reactive atomistic models are used to relate the fraction of silane condensation species (T0–T3) in a glycidoxypropyltrimethoxy silane (GPS) sizing network to density, structure, and mechanical response under deformation. The motivation is **composite** manufacturing: **sizing** layers on **glass fibers** influence **matrix** adhesion and **damage** tolerance before a full **epoxy** interphase is formed.

**Reactive all-atom MD** probes **GPS-based glass-fiber sizing** networks in which **Si–O–Si** linkages create **T0–T3** silicon sites. Six **T0:T1:T2:T3** compositions are built; **GAFF** cross-links the network, then **ReaxFF** captures **bond breaking** during mechanical tests. **LAMMPS** is the engine. Structure (density, RDF, void space) and mechanics (modulus, strength, strain, energy absorption, failure modes) are reported as functions of species composition.

## Methods

**MD application.** **LAMMPS** drives **all-atom MD** in two stages. **Stage 1 (network build, non-reactive):** **GAFF** interactions support a **single-step cross-linking** algorithm (cited to prior publications) that condenses **glycidoxypropyltrimethoxy silane (GPS)** into **Si–O–Si**-linked films. **Six** **T0:T1:T2:T3** compositions are built—**100% T3**, **100% T2**, **50:50 T2:T3**, **75:25 T2:T3**, **10:10:40:40**, and **25:25:25:25**—each with **three independent replicas** to average conformational variability. **Stage 2 (mechanical test, reactive):** **ReaxFF** replaces **GAFF** during **deformation** so **Si–O** **bond scission** and **damage** nucleation are permitted; the manuscript contrasts **GAFF** vs **ReaxFF** functional form (continuous bond order, polarizable **geometry-dependent** charges).

**Supercells** are **PBC** **GPS** films with **atom counts** and **cell vectors** tabulated in *Comput. Mater. Sci.* **§2**. **Reported observables** include **mass density**, **radial distribution functions**, **interstitial/void** measures, **stress–strain** curves, **elastic modulus**, **strength**, **failure strain**, **energy absorption**, and **failure morphology** classifications.

**Force-field training** is **N/A** (**GAFF** + literature **ReaxFF**). **Static QM**, **electric fields**, and **enhanced sampling** are **N/A** for the main workflow.

**Thermodynamic ensemble, timestep, thermostat/barostat, temperature, strain rate, and run lengths** for cross-linking equilibration and **ReaxFF** mechanical loading appear in *Comput. Mater. Sci.* **§2** and are **not transcribed** from the short indexed extract used here.

**MD blueprint honesty.** **LAMMPS** is named in the article for **molecular dynamics** on **PBC** **GPS** films. **NVT**/**NPT**/**NVE** choices, **timestep**, **thermostat**, **barostat**/**pressure** control during network curing vs **ReaxFF** deformation, and **equilibration**/**production** durations (**ps**/**ns**) are **N/A** on this page—retrieve from *Comput. Mater. Sci.* **§2**.

## Findings

**Outcomes:** **Mechanical response** of the **GPS sizing layer** depends systematically on **T-species composition**; **structure** (**density**, **RDF**, **void space**) and **mechanics** (**modulus**, **strength**, **strain**, **energy absorption**) co-vary across the six models. **Damage:** **ReaxFF** deformation captures **bond-breaking** pathways and **failure modes** not accessible under **GAFF** alone. **Statistics:** **three independent networks** per composition are used to average variability. **Comparisons / limitations:** the paper discusses **GAFF→ReaxFF handoff** stresses and the omission of **film former**, **epoxy**, and full **fiber/matrix interphase** chemistry—see **## Limitations** below and the manuscript discussion. ## Limitations

**GAFF-to-ReaxFF handoff** can introduce **internal stress**; the paper discusses equilibration implications. **Film former, epoxy, and full interphase chemistry** are not simulated here—focus is **pre-interphase GPS network**. Future work would need to embed these **sizing** networks adjacent to **polymer** matrices to capture **interphase** formation explicitly.

## Relevance to group

Direct **ReaxFF application** from **van Duin (RxFF Consulting)** on **composite interphase-relevant** organosilicon chemistry, with explicit **LAMMPS + ReaxFF** workflow. The paper is a practical reference for how **condensation** speciation maps to **measurable** **mechanical** metrics in **sizing** layers.

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2017.08.033](https://doi.org/10.1016/j.commatsci.2017.08.033)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
