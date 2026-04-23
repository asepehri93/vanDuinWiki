---
id: paper:2011huang-venue-paper
type: paper
title: "Chemomechanics control of tearing paths in graphene"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:nose-hoover
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.85.195453"
year: 2012
authors:
  - "Xu Huang"
  - "Hui Yang"
  - "Adri C. T. van Duin"
  - "K. Jimmy Hsia"
  - "Sulin Zhang"
venue: "Physical Review B 85, 195453 (2012)"
pdf_sha256: "f2404a06299ff0444276e91ff6f732d64bd030af25bd04d9259b276ba3a14091"
pdf_path: "papers/Huang_grapene_tear_PhysRevB_2012.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2011huang-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Tearing** is a dominant fracture mode for **monolayer graphene**. This work uses **reactive molecular dynamics** with **ReaxFF** to study how **chemomechanical** conditions steer the **fracture path** when graphene is torn. In **vacuum**, torn **graphene nanoribbon (GNR)** edges tend toward **armchair** character; with **oxygen** (or other) **chemical additives** at fracture surfaces, edges can switch from **armchair** toward **zigzag**. Because graphene has a large **in-plane stretching to out-of-plane bending stiffness ratio**, tearing induces **local bending** at the crack tip, producing **mixed-mode** fracture that also influences path selection. The authors frame the results as guidance for **edge engineering** of GNRs produced by tearing.

## Methods


**Reactive molecular dynamics** uses **ReaxFF** on **monolayer graphene** with either a **finite notch** in a **6 nm × 6 nm** sheet or a **semi-infinite crack** model (Sec. II.A in the article). **Tearing** is imposed by **fixing** atoms along two short edge segments and incrementally separating them in **opposite out-of-plane directions**; after each increment the configuration is **dynamically relaxed** toward a low-energy state. A **Nosé–Hoover** thermostat targets **10 K**, and an **out-of-plane separation rate of 0.0625 Å/ps** is used with the low temperature to mimic **quasi-static** tearing. **Fracture surfaces** are terminated with **hydrogen** or **oxygen** to represent **environmental additives** during crack advance. The discussion connects atomistic outcomes to **continuum fracture mechanics** language (**modes I–III**, **K-dominated** near-tip fields, and **mode mixity**) to interpret how **out-of-plane bending** at the tear front couples to **crystallographic** path selection.

**1 — MD application.** **Engine / code:** **N/A —** MD package name not stated in `normalized/extracts/2011huang-venue-paper_p1-2.txt` (verify `papers/Huang_grapene_tear_PhysRevB_2012.pdf`). **System:** **6 nm × 6 nm** monolayer graphene with a **notch** (finite model) plus the **semi-infinite crack** variant described in the paper. **Boundaries / loading:** **fixed** edge atoms with **out-of-plane separation** driving tear; **PBC** details for the semi-infinite setup are in the PDF beyond the short extract. **Ensemble:** **NVT**-like **thermostatted** relaxation protocol with **Nosé–Hoover** at **10 K** as excerpted. **Timestep:** **N/A —** not stated on the indexed pages. **Duration / stages:** **quasi-static** stepping narrative rather than long **ns** production trajectories in the excerpt. **Barostat:** **N/A —** not used for the described tearing relaxation. **Temperature:** **10 K** as stated. **Pressure:** **N/A —** not a hydrostatic **NPT** study in the excerpt. **Electric field:** **N/A —** not indicated. **Replica / enhanced sampling:** **N/A —** not indicated.

**2 — Force-field training.** **N/A —** applies ReaxFF rather than reparameterizing it here.

**3 — Static QM / DFT.** **N/A —** not the primary engine for the tearing simulations described in the excerpt.

## Findings

In **vacuum** (H-terminated fracture chemistry in the modeling narrative), torn **GNR** edges tend toward **armchair** character, whereas with **oxygen-related** chemistry at fracture surfaces the edge can switch from **armchair** toward **zigzag**, indicating **chemomechanical control** of **edge chirality**.

Because monolayer graphene has a large **in-plane stretching to out-of-plane bending stiffness ratio**, tearing induces **local bending** at the crack tip, producing **mixed-mode** conditions (not pure mode III) that influence **kinking** and **path stability** together with **chemical passivation**.

**Corpus honesty.** The frontmatter `year` (**2012**) matches **Phys. Rev. B** publication metadata (`doi`, `venue`); `extraction_quality` is **partial**—full stress/intensity factor analysis is in **`pdf_path`**.

**Comparisons.** The article contrasts **H vs O** edge termination as a **chemomechanical** switch and ties atomistic tearing to **continuum fracture mechanics** language (**modes I–III**, **K-dominated** fields, **mode mixity**) as printed in the excerpt.

**Sensitivity / levers.** **Temperature** (**10 K**), **separation rate** (**0.0625 Å/ps**), and **passivation chemistry** are explicit knobs in the indexed Methods excerpt.

**Limitations / outlook.** **However**, the study is necessarily a **classical reactive FF** model at **low temperature** and finite model sizes; direct mapping to room-temperature experiments is not claimed on the indexed pages.

## Limitations

- System sizes, rates, and temperature in MD limit direct comparison to room-temperature experiments; edge chemistry is modeled at classical reactive-FF level.
- Normalized metadata lists an incorrect catalog year; the **journal** publication is **2012** (see `doi` and `venue` above).

## Relevance to group

**van Duin-group** coauthored ReaxFF study connecting **reactive mechanics** of graphene to **device-relevant edge structures** for GNRs.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevB.85.195453](https://doi.org/10.1103/PhysRevB.85.195453)
- Text-aligned pointer: `normalized/extracts/2011huang-venue-paper_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
- GNR edge orientation and mechanical processing
