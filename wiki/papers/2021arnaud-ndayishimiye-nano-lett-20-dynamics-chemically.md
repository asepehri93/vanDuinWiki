---
id: paper:2021arnaud-ndayishimiye-nano-lett-20-dynamics-chemically
type: paper
title: "Dynamics of the Chemically Driven Densification of Barium Titanate Using Molten Hydroxides"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - material:perovskite-oxide
  - method:reaxff
  - task:application
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:validation-experiment
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1021/acs.nanolett.1c00069"
year: 2021
authors:
  - "Arnaud Ndayishimiye"
  - "Mert Y. Sengul"
  - "Dooman Akbarian"
  - "Zhongming Fan"
  - "Kosuke Tsuji"
  - "Sun Hwi Bang"
  - "Adri C. T. van Duin"
  - "Clive A. Randall"
venue: "Nano Lett."
pdf_sha256: "cabe176723dae945cb3b70d32cde281f96995630e02d9aab085cf053863ad158"
pdf_path: "papers/Ndayishimiye_NanoLetters_2021_sintering.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021arnaud-ndayishimiye-nano-lett-20-dynamics-chemically -->

## Summary

Ndayishimiye *et al.* combine **molten hydroxide cold sintering**, detailed **microscopy**, and **ReaxFF molecular dynamics** to explain how **barium titanate** can densify near **300 °C** under **~350 MPa** using a **NaOH–KOH** eutectic—far below conventional **ceramic** **sintering** temperatures (*Nano Lett.*, DOI `10.1021/acs.nanolett.1c00069`). **Adri C. T. van Duin** co-authorship anchors the simulation component to the group’s **reactive** **oxide**/**molten salt** practice. Experimentally, the authors track **densification kinetics** and show **potassium** accumulating at **triple junctions** in **TEM/EDS**, implicating **chemically** **heterogeneous** pathways beyond simple **particle** **rearrangement**. Atomistically, **ReaxFF** is used to propose **interfacial complexes** and **dissolution–reprecipitation** motifs consistent with **pressure-solution** creep pictures from the geoscience and ceramics literature, translated here into a **ferroelectric** **perovskite** processing context.

## Methods

### Experiments (molten-hydroxide cold sintering and microscopy)

**BaTiO₃** (BTO) is densified using a **NaOH–KOH eutectic (51/49 mol %)** at **300 °C** under **~350 MPa** uniaxial pressure in the cold sintering process (CSP) configuration described in *Nano Lett.* Time-dependent **relative density** (semilog) and **strain** (log–log) are reported for the densification window; **XRD**, **optical** appearance, and **HR-SEM** illustrate the resulting ceramic. **TEM/STEM-EDS** shows **K** accumulated at **triple junctions** against a background of **Na**-rich melt elsewhere, supporting chemically heterogeneous transport during CSP.

### MD application (ReaxFF)

**ReaxFF molecular dynamics (MD)** (ref. 41 in the article) is used to model **BaTiO₃** interfaces in contact with **NaOH** and **KOH** melt chemistry. The **ReaxFF description** in this work **combines** two prior parameterizations—one for **BTO** and one for the **KOH–NaOH** system (see *Nano Lett.* text and refs. 44+). The simulations target **interfacial speciation**, **ionic complex** scenarios, and **surface population** trends compared to the molten flux; **Supporting Information** methods document additional setup and analyses (e.g. population analysis cited with **Figure 3**). For mechanical checklist items not spelled out on the main-text pages, treat as **N/A—confirm SI:** **periodic (PBC)** in-plane **slab/supercell** details for the interface cells, **NVT**/**NPT** **ensemble** and **thermostat** (Berendsen/Langevin/etc.), **timestep** in **fs**, and **equilibration** then **production** spans in **ps**/**ns**; **N/A—barostat** as hydrostatic **NPT** for the full melt **unless** the SI lists bulk **NPT** segments (interface studies often use fixed-cell or hybrid control). **Electric field (MD):** **N/A**—not used. **Enhanced sampling:** **N/A**—no umbrella or metadynamics in the main workflow. **N/A**—direct mapping of the laboratory **350 MPa** uniaxial **pressure** to in-cell **stress** control unless the SI defines it.

### Force-field training in this work

**N/A —** the paper **applies** a **merged** BTO + molten-hydroxide ReaxFF line from prior work; it is not a *de novo* open-parameter training paper. Full training provenance for the parent BTO and hydroxide fields remains in the cited ReaxFF references and companion CSP studies (see *Nano Lett.* references list).

### Static QM (standalone)

**N/A —** the study’s primary atomistic layer is **ReaxFF MD** with experiment; any isolated DFT in supporting literature is not the Methods centerpiece here.

## Findings

**Densification kinetics and strain:** The reported **(semi)log** density and **log–log** strain curves are interpreted in terms of **pressure-solution**/**dissolution–precipitation** creep under **~300 °C** and **~350 MPa**, consistent with a chemically enabled transport picture rather than conventional high-**T** solid-state sintering alone. **K** enrichment at **triple junctions** in **TEM/STEM-EDS** ties macroscopic mass transport to localized chemistry that motivates interfacial ionic partitioning in atomistic terms.

**Atomistic support:** ReaxFF **molecular dynamics** is used to propose **interfacial** complexes and reaction scenarios at **BaTiO₃**/**molten hydroxide** contacts (e.g. hydroxide participation and ion rearrangements) that are compatible with a dissolution–reprecipitation view of how mass can be shuttled at temperatures far below the usual **BaTiO₃** furnace sintering window. **Comparisons** in the full article also situate the mechanism relative to the broader **cold sintering** and **pressure-solution** literature (see *Nano Lett.* text and figures). **PDF/SI** should be used for any quantitative comparison of **simulation** time scales to **in situ** kinetics: nanosecond **MD** is illustrative for pathways, not a direct calibrator of macroscopic sintering rates. Version-of-record protocol numbers for the ReaxFF runs are in `pdf_path` and SI rather than in this short summary.

## Relevance to group

Couples **ReaxFF** to **cold sintering** of a **canonical ferroelectric ceramic** with **Nano Letters**-level **experimental** validation.

## Citations and evidence anchors

- DOI: [10.1021/acs.nanolett.1c00069](https://doi.org/10.1021/acs.nanolett.1c00069)

## Related topics

- [[reaxff-family]]
