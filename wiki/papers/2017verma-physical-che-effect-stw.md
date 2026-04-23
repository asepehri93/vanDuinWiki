---
id: paper:2017verma-physical-che-effect-stw
type: paper
title: "The effect of STW defects on the mechanical properties and fracture toughness of pristine and hydrogenated graphene"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - method:classical-md
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:graphene-carbon
  - keyword:classical-ff
candidate_tags: []
source_refs: []
doi: "10.1039/c7cp02366a"
year: 2017
authors:
  - "Akarsh Verma"
  - "Avinash Parashar"
venue: "Physical Chemistry Chemical Physics 19, 16023–16037 (2017)"
pdf_sha256: "53a1ff37972a58836f393a68d73227b88b3f2d267698cf2dfb1cc3a1c6f40517"
pdf_path: "papers/Others/Verma_STW_defects_AIREBO.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017verma-physical-che-effect-stw -->

## Summary

This Physical Chemistry Chemical Physics article uses **classical molecular dynamics** with the **AIREBO** potential to probe how **Stone–Thrower–Wales (STW)** topological defects—local rearrangements of the hexagonal network that do not remove atoms—change **fracture toughness** and crack-tip mechanics in **graphene**. The motivation is that graphene is often treated as extraordinarily strong yet brittle in tension, while real sheets contain a zoo of **defects** that can either weaken or, unexpectedly, **toughen** the material by enabling additional deformation modes. The authors compare **pristine** graphene against systems where STW defects are placed in the neighborhood of cracks, and they also examine **hydrogen-passivated crack edges** to separate **pure topology** effects from **edge chemistry** effects on failure.

## Methods

**Molecular dynamics (classical).** All atomistic runs use **LAMMPS** with the **AIREBO** potential for graphene and hydrogen-passivated (graphane) crack edges; a **1.92 Å** bond-order cutoff is applied uniformly to avoid spurious C–C failure modes. The graphene sheet is about **270 Å** on a side (**~27 468 atoms**), with lateral dimensions chosen so the crack length remains roughly one tenth of the sheet width to mitigate finite-size artifacts. **Periodic boundary conditions** are imposed along the in-plane directions so free-edge artifacts are suppressed while out-of-plane rippling remains allowed. The protocol quoted in the indexed article text relaxes structures in the **isothermal–isobaric (NPT) ensemble** using **Nosé–Hoover** thermostat and barostat coupling, holding the **temperature** of the box at **1.0 K** (to damp thermal fluctuations during quasi-static loading studies) with an integration **timestep of 0.5 fs** and **50 ps** of relaxation before the fracture workflow continues in the full **PDF**. **Electric field** coupling and **umbrella / metadynamics**-style **enhanced sampling** are **not** used.

**Force-field fitting.** **N/A —** AIREBO is used as a **published, fixed parameter set**; this PCCP study does not reoptimize bond-order parameters.

**Static QM / DFT.** **N/A —** the reported fracture and STW mechanics come from classical MD only.

**Review / non-simulation scope.** **N/A —** primary research article, not a literature review.

## Findings

**Outcomes and mechanisms.** Stone–Thrower–Wales (5–7–7–5) defects are created by rotating a C–C bond without removing atoms; the authors argue these defects promote **out-of-plane displacement** and **stress redistribution** near crack tips, which can **raise fracture toughness** relative to selected pristine cases under the same modeled crack placement. **Hydrogen passivation** of crack edges changes how load is shed between in-plane scission and stabilizing interactions, shifting toughness relative to both pristine and bare-edge configurations in the same framework.

**Comparisons.** The narrative contrasts STW-assisted toughening with brittle, strictly planar cleavage pictures and cites broader literature on defect engineering; head-to-head **versus** experimental fracture curves is not the focus of the excerpted introduction—use the **PDF** for any quantitative comparison tables.

**Sensitivity and design levers.** Reported response depends on **defect placement** relative to the crack and on **edge chemistry** (hydrogenated versus unpassivated), so toughness changes are **geometry- and loading-protocol-dependent** rather than universal scalars.

**Limitations (authored / model).** AIREBO captures covalent carbon mechanics but not full **oxidative** or organofunctional edge chemistry; extrapolation to ambient oxidation or ReaxFF-class bond rearrangements requires different models.

**Corpus honesty.** Modeling details through relaxation staging are confirmed from `normalized/extracts/2017verma-physical-che-effect-stw_p1-2.txt` and the article **PDF** at `pdf_path`; confirm any additional loading substeps from the full PCCP text if your workflow needs complete stress–strain tables.


## Limitations

AIREBO captures **bond order** and **carbon chemistry** in a classical sense but does not reach **ReaxFF**-level explicit reactivity for oxygenated or highly functionalized edges; oxidation-driven failure is outside scope. Results are **geometry- and loading-protocol-dependent**, as in most atomistic fracture studies.

Readers comparing this study to **ReaxFF** graphene irradiation or oxidation work should treat the potentials as answering different questions: AIREBO emphasizes **mechanical** response and **topological** defect mechanics under assumed bonding descriptions, whereas reactive simulations become necessary when **bond-breaking chemistry** and **environmental** species participate directly in failure.

## Citations and evidence anchors

- DOI: [10.1039/c7cp02366a](https://doi.org/10.1039/c7cp02366a)

## Relevance to group

Shows **non-ReaxFF** reactive/classical carbon potentials applied to **defect engineering** in nanocarbon—useful contrast next to **ReaxFF** studies where bond chemistry is central.

## Related topics

- [[graphene-nanocarbon]]
- [[reaxff-family]]

