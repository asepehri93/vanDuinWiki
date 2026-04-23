---
id: paper:2002stoliarov-venue-pii-s0032-3861
type: paper
title: "A reactive molecular dynamics model of thermal decomposition in polymers: I. Poly(methyl methacrylate)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reactive-md-generic
  - task:method-development
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/S0032-3861(02)00761-9"
year: 2003
authors:
  - "Stanislav I. Stoliarov"
  - "Phillip R. Westmoreland"
  - "Marc R. Nyden"
  - "Glenn P. Forney"
venue: "Polymer"
pdf_sha256: "a21c85e8ddaf1acc04f64142fe02ce41d555bbe2a35be80c90f2325ce5ce045b"
pdf_path: "papers/Others/Stoliarov_Westmoreland_RMD_PMMA_Polymer_2003.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2002stoliarov-venue-pii-s0032-3861 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Thermal decomposition** of **polymethyl methacrylate (PMMA)** is often summarized as **depolymerization** to **methyl methacrylate**, but **initiation** steps and the relative fate of **primary versus tertiary** radicals in the **condensed phase** remain debated when only **TGA** or **TGA/MS** data are available. Stoliarov, Westmoreland, Nyden, and Forney present **reactive molecular dynamics (RMD)**: classical **MD** in which **covalent bonds** may **break and form** according to a **reactive** modification of a **valence force field**, implemented in their **MD_REACT** program. They apply the method to **bulk PMMA** heating so chemistry evolves **in situ** in the **dense polymer**, avoiding gas-phase-only mechanistic assumptions.

## Methods

### Reactive force-field training / QM reference (checklist A)

- **Lineage:** **Reactive molecular dynamics (RMD)** implemented in **MD_REACT**; **valence** energy follows a **CVFF**-type decomposition (bonds, angles, torsions, nonbonded pairs) with **bond stretching** replaced by **Morse** functions so bonds can **dissociate** (Sec. 2, *Polymer* **44**, 883–894).
- **QM training data:** **CBS-QB3** **reaction enthalpies** \(\Delta H_0\) for a **Table 1** set of **model reactions** representing **PMMA** decomposition; **D** parameters taken from dissociation reactions (with **zero-point** corrections as stated), **\(\pi\)**-bond energetics from **\(\beta\)-scission** reactions; **\(r_e\)** from **B3LYP/CBSB7** optimized geometries (Appendix A lists **Morse** parameters and provenance).

### Molecular dynamics protocol (checklist B)

- **Engine:** **MD_REACT**; **Hamilton’s equations** integrated with **Verlet velocity** integrator (Sec. 3.1).
- **System:** **Bulk** **PMMA** models—primarily **one** **15-unit** chain (**~230 atoms**); **four-chain** bundles (**15** units each, **~920 atoms**) for **inter-chain** chemistry; **periodic boundary conditions**; **nonbonded** interactions via **atom-based** summation with **16.5 Å cutoff** (Sec. 3.1).
- **Equilibration:** **simulated annealing** from **600 K**, **NPT** at **101 kPa**, then energy minimization steps; **Morse** bonds temporarily replaced by **harmonics** to avoid premature **scission**; equilibration **0.5–15 ps**; reported **mass density** **~1.02–1.04 g cm\(^{-3}\)** (weak **T** dependence) (Sec. 3.1).
- **Production RMD:** **NVT** after equilibration; **timestep** **0.2–1 fs** (smaller at higher **T** to avoid divergence); total **RMD** time **2–100 ps** per run; target **temperatures** **1000**, **1200**, **1500 K** (lowest **1000 K** chosen for observable chemistry in feasible time); **10** single-chain and **3** four-chain runs per **T** (Sec. 3.1–3.2).
- **Thermostat:** **direct velocity scaling** preferred over **Nosé–Hoover** at these conditions because **Nosé–Hoover** gave large fluctuations/divergence; **velocity scaling** kept instantaneous **T** within **±10 K** when used (Sec. 3.1).

### DFT / static QM in support of the FF

- **CBS-QB3** thermochemistry for the **Table 1** training reactions (as above).

## Findings

- **Volatile speciation:** **methyl methacrylate** dominates volatile products (**~80–90%** mass fraction of volatiles from **1000–1500 K** in simulations), with trace **H\(_2\)**, **CO**, **CO\(_2\)**, light **hydrocarbons**, and **methyl formate**—qualitatively consistent with compiled **experimental** product analyses cited in the paper (Sec. 3.2).
- **Effective rate of monomer production:** Arrhenius fit to simulation-derived **\(k\)** (Eq. (9)) gives **\(A \approx (1.9\text{–}2.9)\times 10^{12}\ \mathrm{s}^{-1}\)** and **\(E \approx 53 \pm 14\ \mathrm{kJ\,mol^{-1}}\)** (2\(\sigma\)); authors compare to **experimental** **mass-loss** **\(E_a\)** ranges **60–270 kJ mol\(^{-1}\)** and discuss **underestimation** of overall **mass-loss** activation energy, noting **experiments** near **500–700 K** vs simulations **1000–1500 K** (Sec. 3.2, Fig. 3).
- **Initiation mechanism:** **backbone** and **side-group** scissions each **<~20%** of initiation events; a **two-step** **C–C** channel (their **Reactions (11)–(13)**) accounts for **~50–60%** (plus **~20–25%** for related channels)—contrasting with textbook **random-scission** or **Manring** side-group dominance hypotheses (Sec. 3.2).
- **Radical fate / “unzipping”:** **tertiary** radicals mainly **\(\beta\)-scission** to monomer; **primary** radicals compete with **termination** channels **(16)–(17)**—at **1500 K**, **<0.5** monomer on average from the **primary** site before termination vs **2–3** at **1000 K** (Sec. 3.2).
- **Authors’ limitations / future work:** **FF** is a **first-order** approximation to **PES**; **quantum** effects and longer **time/length** scales not captured; **concluding remarks** call out **condensed-phase** initiation dynamics differing from **gas-phase** bond dissociation (Sec. 4). The article appears in *Polymer* **44**, **883–894** (2003).

## Limitations

- Model chemistry and **FF** errors still bound mechanistic conclusions; extrapolation to **additives**, **flame** conditions, or other **polymers** requires separate validation.

## Relevance to group

**Reactive MD** lineages connect conceptually to **ReaxFF** applications in **polymers** and **combustion**; **Westmoreland** ties to **Penn State**-adjacent reaction-engineering networks.

## Citations and evidence anchors

- **DOI:** https://doi.org/10.1016/S0032-3861(02)00761-9

## Related topics

- [[reaxff-family]]
