---
id: paper:2014yusupov-venue-inactivation-endotoxic
type: paper
title: "Inactivation of the Endotoxic Biomolecule Lipid A by Oxygen Plasma Species: A Reactive Molecular Dynamics Study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:polymer
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1002/ppap.201400064"
year: 2014
authors:
  - "Maksudbek Yusupov"
  - "Erik C. Neyts"
  - "Christof C. Verlackt"
  - "Umedjon Khalilov"
  - "Adri C. T. van Duin"
  - "Annemie Bogaerts"
venue: "Plasma Process. Polym."
pdf_sha256: "d5f956a3a268a505f4f94cc1c132840a53b2a18c1efe278a790ae2f029921051"
pdf_path: "papers/Yusupov_PlasmaProcPoly_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014yusupov-venue-inactivation-endotoxic -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below (**Summary**, **Methods**, **Findings**) summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. It is not new primary science from this wiki.

    For bond-level mechanisms, SI parameter discussion, and full protocol tables, use the peer-reviewed PDF—not this page alone.

## Summary

Cold atmospheric-pressure plasmas can generate reactive oxygen species (ROS) that deactivate biomolecules on medical-device surfaces, but atomistic mechanisms—especially for endotoxic **lipid A**, the toxic moiety of lipopolysaccharide from Gram-negative bacteria—are difficult to isolate experimentally. This **Plasma Processes and Polymers** article uses **ReaxFF reactive molecular dynamics** to simulate collisions of **OH**, **HO\(_2\)**, and **H\(_2\)O\(_2\)** with an **E. coli lipid A** model, tracking bond cleavage, functional-group evolution, and inferred loss of endotoxic activity as structural degradation proceeds. The work positions simulations alongside plasma biochemistry literature that shows ROS can modify or etch lipid films, aiming to differentiate **radical-specific** fragmentation channels. **Adri C. T. van Duin** is a coauthor, linking the study to the Penn State reactive MD tradition.

## Methods

**Force-field training.** Simulations use **ReaxFF** with a **C/H/O/N/P** parameterization assembled as described in the article; alternative parameter choices are discussed in **Supporting Information** (**N/A** for full QM training tables on this page).

**MD application (ROS projectiles + lipid A).** **Reactive MD** studies collisions of **OH**, **HO\(_2\)**, and **H\(_2\)O\(_2\)** with an **E. coli lipid A** model (**NVT** at **300 K**, **Bussi** thermostat; **0.25 fs** timestep; **500 ps** equilibration of the initial **lipid A** configuration before production impacts, as stated in the computational setup). **Engine** name/version, supercell size, **PBC** details, full production segment lengths, and any **NPT** segments are **N/A** beyond what is quoted here—see **`papers/Yusupov_PlasmaProcPoly_2014.pdf`**/**SI**. **Electric-field** driving and **enhanced sampling** are **N/A** in this summarized impact framing.

**Static QM.** **N/A** as headline method: reported chemistry is **ReaxFF MD**; **QM** may appear as references or SI benchmarks per the article.

## Findings

The abstract reports that modeled plasma species can **destroy lipid A**, reducing modeled **toxic activity** relative to intact lipid A. **HO\(_2\)** and **H\(_2\)O\(_2\)** impacts follow **different bond-breaking mechanisms** than **OH**-driven chemistry in the sampled trajectories, consistent with a mechanistic distinction between hydrogen-peroxide-class pathways and hydroxyl-radical pathways. The authors summarize agreement between simulation trends and **experimental observations** from plasma biochemistry studies cited in the introduction and discussion. Quantitative comparison to any specific plasma reactor should account for photon fluxes, electric fields, and secondary chemistry not explicitly included in the gas-phase ROS impact model.

## Limitations

The biomolecular model is necessarily simplified relative to full LPS assemblies and membranes; ReaxFF accuracy for phosphate and acyl-chain chemistry should be checked against QM benchmarks for the bonds most critical to the claimed degradation channels.

## Relevance to group

Applies **ReaxFF** to **plasma–biomolecule** interactions with **van Duin** coauthorship, connecting reactive MD to biomedical plasma processing literature.

## Citations and evidence anchors

- DOI: [10.1002/ppap.201400064](https://doi.org/10.1002/ppap.201400064)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
