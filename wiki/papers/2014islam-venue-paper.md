---
id: paper:2014islam-venue-paper
type: paper
title: "ReaxFF reactive force field simulations on the influence of Teflon on electrolyte decomposition during Li/SWCNT anode discharge in lithium-sulfur batteries"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
  - domain:reactive-md
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:reactive-md
source_refs: []
doi: "10.1149/2.005408jes"
year: 2014
authors:
  - "Islam, Md Mahbubul"
  - "Bryantsev, Vyacheslav S."
  - "van Duin, Adri C. T."
venue: "Journal of The Electrochemical Society"
pdf_sha256: "272018bcc02e1f65043e09313fc8a0ed0a50e4259c3d7708e547ecdbe0ec34d1"
pdf_path: "papers/Islam_JES_2014.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2014islam-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **JES** article identified by `doi`, `title`, and `pdf_path`. The corpus PDF is the **electrochemical society** layout for this focus issue paper (not a separate proof sibling listed in `NON_PRIMARY_ARTICLE_PAPER_SLUGS.md` for a different slug).

## Summary

Lithium–sulfur batteries offer high theoretical capacity but face polysulfide shuttle, lithium dendrites, and aggressive electrolyte reduction at the negative electrode. Replacing bare lithium metal with a **Li/single-wall carbon nanotube (SWCNT) composite anode** and using **TEGDME** (tetra(ethylene glycol) dimethyl ether) as a model ether electrolyte, this study applies **ReaxFF reactive molecular dynamics** to compare **bare** versus **ex situ Teflon-coated** anode surfaces during discharge. In lithium-rich interfacial regions, the simulations show **TEGDME dissociation** with **ethylene** as a major gaseous product. **Discharge** at the anode is **exothermic**, producing **local hot spots** that accelerate electrolyte attack. A **Teflon** surface layer is found to **damp initial heat flow** and **suppress lithium-driven electrolyte decomposition** relative to the uncoated interface in the modeled scenarios.

The **composite** architecture matters because **SWCNTs** provide **conductive** **scaffolding** and **interfacial** area where **lithium** **deposition** and **solvent** contact can be spatially heterogeneous; the paper uses that geometry to interrogate how a **fluoropolymer** **skin** changes **heat** and **reaction** pathways at the **earliest** stages of **reduction**.

## Methods

**Force field.** ReaxFF parametrization for Li, carbon nanotube chemistry, ether solvents, and fluoropolymer interactions as described in the article and Supporting Information references.

**Systems.** Composite anode models with explicit TEGDME; variants include **bare** SWCNT-supported lithium versus **Teflon-treated** surface preparation mimicking ex situ coating.

**Protocol.** Reactive MD trajectories sample interfacial regions during processes analogous to discharge (lithium redistribution and reactivity toward solvent); analysis tracks bond-breaking channels, gas evolution, and temperature localization.

### 1 — MD application (Li/SWCNT + TEGDME)

- **Engine / code / PBC / timestep / thermostat / barostat / duration / temperature schedules:** **N/A — not stated on `normalized/extracts/2014islam-venue-paper_p1-2.txt` and not duplicated reliably here**; read **`papers/Islam_JES_2014.pdf`** *J. Electrochem. Soc.* **161** (8) **E3009–E3014** Computational section (and SI if referenced).
- **System size & composition:** **Li/SWCNT** composite anode regions with explicit **TEGDME**-family solvent chemistry as described in the **JES** article (**Summary**); **atom counts** are **N/A — not on the indexed extract** (Computational section).
- **Ensemble:** **N/A — NVT/NPT choice not stated on the indexed extract** (Computational section).
- **Hydrostatic pressure / barostat:** **N/A — pressure control not stated on the indexed extract** (confirm whether strictly constant-volume interfacial sampling).
- **Electric field:** **N/A — not indicated** in the abstract-level corpus summary used for this page.
- **Replica / enhanced sampling:** **N/A — not indicated** in the abstract-level summary used here.

## Findings

**Ethylene** emerges as a prominent decomposition product when the electrolyte interacts with lithium-rich zones at the anode interface. **Thermal localization** from exothermic discharge steps couples positively with **decomposition kinetics**. **Teflon** mitigates early **heat transfer** into the electrolyte and reduces **lithium reactivity** toward solvent in the simulations, consistent with the abstract’s protective framing.

**Mechanistic reading.** The protective effect is framed partly as **thermal management** at the **interface**: slowing **localized** **heating** reduces the **rate** of **solvent** **cleavage** even when **thermochemistry** remains favorable at equilibrium.

**Electrolyte scope.** **TEGDME** is a **model** **ether** electrolyte for **Li–S** research; translating conclusions to **carbonate** or **fluorinated** **electrolytes** requires different **ReaxFF** **parameter** **domains** and was not attempted in this **JES** study.

## Limitations

`extraction_quality` is marked **partial** in corpus profiling—confirm numerical rates and full reaction lists on the PDF. Long-timescale **SEI** evolution and cell-level transport are not captured in nanosecond-class trajectories.

## Relevance to group

van Duin-group contribution to **Li–S** interfacial chemistry and **protective coatings** on nanostructured anodes.

## Citations and evidence anchors

- *J. Electrochem. Soc.* **161** (8) E3009–E3014 (2014); **DOI** [10.1149/2.005408jes](https://doi.org/10.1149/2.005408jes) (`papers/Islam_JES_2014.pdf`).
- Extract pointer: `normalized/extracts/2014islam-venue-paper_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- [[graphene-nanocarbon]]
