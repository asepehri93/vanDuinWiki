---
id: paper:2016rahnamoun-venue-study-ice
type: paper
title: "Study of ice cluster impacts on amorphous silica using the ReaxFF reactive force field molecular dynamics simulation method"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - material:silicate-glass
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.4942997"
year: 2016
authors:
  - "A. Rahnamoun"
venue: "J. Appl. Phys."
pdf_sha256: "6d98de3d50f6099e3101f965173da0fc23186c21b93c454939a2cc113f1b7772"
pdf_path: "papers/Rahnamoun_JAP_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016rahnamoun-venue-study-ice -->

!!! note "Authority of statements"

    Prose summarizes the publication identified by `doi`, `title`, and `pdf_path`; confirm numbers in the peer-reviewed PDF.

## Summary

**ReaxFF MD** is used to simulate **high-velocity impacts of ice clusters** onto **amorphous silica** substrates, targeting **mechanochemical damage** and **hydrogen-bond-mediated contact mechanics** relevant to **icy-body impacts**, **cryogenic engineering**, or **tribological** scenarios involving **water ice + silica**. The publication analyzes **energy dissipation**, **substrate disruption**, and **reactive events** enabled by the **reactive force field** that would be invisible to **fixed-bond silica models**.

## Methods

**Reactive MD (ReaxFF).** Collisions between **amorphous** (**150** H\(_2\)O) and **crystalline** (**128** H\(_2\)O) ice clusters and **amorphous silica** substrates are integrated with **ReaxFF** at **1**, **4**, and **7 km s\(^{-1}\)** normal impact speeds (*J. Appl. Phys.* **119**, **095901**). Targets include **fully oxidized** and **suboxide** silica films built by compressing **SiO\(_2\)** and **SiO\(_{1.5}\)** building blocks in **periodic** boxes until **~2600–2610**-atom amorphous slabs form. Prewimpact setup places clusters **~20 Å** from the surface and **NVT**-relaxes the combined system at **150 K** before assigning center-of-mass velocities along the surface normal; the article states **NVT** but does not name a **thermostat** family in the PDF body checked here (**N/A — thermostat model** beyond the **NVT** label). Production impacts use **NVE** microcanonical integration for **30 ps** per collision with a **0.1 fs** timestep (the authors repeat the **7 km s\(^{-1}\)** amorphous-on-suboxide case at **0.05 fs** to verify timestep convergence). Each velocity condition is repeated **three** times for statistics. **N/A — barostat or target hydrostatic pressure** — **NVE** collision segments omit **pressure** control. **N/A — applied electric field; umbrella / metadynamics / replica exchange** — not reported.

**Force-field training.** **N/A —** the article applies ReaxFF rather than publishing a new parametrization.

**Static QM / AIMD.** **N/A —** not the primary technique; the discussion addresses when inferred cluster temperatures might exceed the ground-state chemistry assumed in ReaxFF.
## Findings

**Sticking vs rebound.** At **1 km s\(^{-1}\)**, ice **accumulates** on the surface; at **4** and **7 km s\(^{-1}\)**, some molecules **rebound** from the surface. **Second impacts** on **ice-covered** silica show **velocity-dependent** **mass** gain or loss (including cases where **both** first and second **1 km s\(^{-1}\)** impacts deposit the entire cluster).

**Chemistry.** **Water dissociation** appears **sparsely** at **4** and **7 km s\(^{-1}\)** in the authors’ trajectories.

**Electronic excitation caveat.** Cluster **temperature** diagnostics motivate treating **electronic excitation** as **unlikely** to dominate below **~10 km s\(^{-1}\)** in this classical framework, while **near ~10 km s\(^{-1}\)** the authors report **average** cluster temperatures around **~2000 K** with **occasional** molecular **peaks** **≳ 8000 K**, so **ground-state** ReaxFF chemistry may be **insufficient** at the highest speeds considered—consistent with the paper’s caution about **electron** excitation beyond classical ReaxFF.

**Stopping and morphology.** The authors stress that **stopping force** depends on **speed** and on **cluster shape** (which changes during impact), so **force–velocity** relations are **not** simple scalings.

## Limitations

- **Classical reactive** treatment of **ice** and **proton disorder** omits **full nuclear quantum effects** unless separately augmented.
- **Cluster geometry / crystallinity** strongly affects outcomes.

## Relevance to group

Corpus **ReaxFF application** connecting **water/ice** chemistry with **silica mechanics**, useful alongside **Langmuir tribochemistry** and **geochemical interface** entries.

## Citations and evidence anchors

- Bibliographic metadata in `normalized/papers/2016rahnamoun-venue-study-ice.json` and abstract in `papers/Rahnamoun_JAP_2016.pdf`; **DOI:** `10.1063/1.4942997`.

## Related topics

- [[reaxff-family]]
