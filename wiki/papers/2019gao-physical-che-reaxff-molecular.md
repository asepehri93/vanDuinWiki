---
id: paper:2019gao-physical-che-reaxff-molecular
type: paper
title: "A ReaxFF molecular dynamics study of molecular-level interactions during binder jetting 3D-printing"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:mechanics-tribology
  - method:reaxff
  - task:application
  - material:oxide
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:nvt-simulation
  - keyword:oxide-surface
  - keyword:validation-experiment
source_refs: []
doi: "10.1039/c9cp03585k"
year: 2019
authors:
  - "Yawei Gao"
  - "Yun Kyung Shin"
  - "Daniel Martinez"
  - "Guha Manogharan"
  - "Adri C. T. van Duin"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "7ac67901a4d416a1e46b6b2575cacbc0a28f7e5f09be986d9f64a71d888611ea"
pdf_path: "papers/Gao_PCCP_binder_jetting_3D_printing.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019gao-physical-che-reaxff-molecular -->

## Summary

**Binder jetting 3D printing (BJP)** of **AISI 316L stainless steel** is modeled with **ReaxFF MD** using **Cr-oxide nanoparticles** and aqueous **diethylene glycol (DEG)** binder, following a **print → cure → burn-out → sinter** thermal sequence. Simulations relate **hydrogen-bond networks**, **DEG oxidation**, and **Cr–O bond formation** to a computed **breaking strength** proxy (restraint potential separating two nanoparticles). Varying **water/DEG** composition and comparing **2-ethoxyethanol**, **DEG**, and **1-(2,2,2-trihydroxyethoxy)ethane-2,2,2-triol** probes the role of **hydroxyl** content during early stages.

## Methods

### Force-field lineage (A)

**Cr/C/H/O ReaxFF** from **Shin et al.** for **Cr₂O₃**-rich passivated nanoparticle surfaces.

### Molecular dynamics: system, stages, and mechanical probe (B)

**Particles:** **Cr-oxide** spheres ~**22 Å** diameter (~**500** atoms) after **annealing** in **H₂O + O₂** at **1273 K**. **Print** reference: **two** particles, **160 H₂O**, **60 DEG**, **80 Å** periodic cube, **300 K**, **NVT**, **Berendsen** thermostat (**100 fs** damping).

**Binder-jetting sequence:** **print** **300 K** → **cure** **393 K** in **200 Å** cell (per article/ESI) with **dissociated water** removed → **burn-out** **900 K** (volatiles stripped) → **sintering** **1900 K**; **direct** heating between stages.

**Stage** **goals** mirror **BJP** **practice**: **print/cure** **preserve** **H-bonded** **green** **strength**, **burn-out** **removes** **organics** that would **outgas** in **furnace** **sintering**, and **1900 K** **sintering** **welds** **particles** through **oxide** **bridges** rather than **metallic** **necking** in this **ReaxFF** **model**.

**Mechanical proxy:** **bell-shaped restraint** separating **50** atom pairs (**25** per particle); **strain rate** via **R₁₂** updates (**Eq. 3**). **Sets A/B** vary **water/DEG** (**Table 1**). **ESI** figures **S1–S3** for geometries.

### Static QM (C)

Not a standalone **DFT** study—**ReaxFF** application to **BJP**.

**Constant-volume stages.** All BJP staging trajectories summarized above remain **NVT** without **NPT** **barostat** or target **GPa** **pressure**—**N/A** for hydrostatic **pressure** control beyond the **stress** implied by the restraint probe.

## Findings

### Mechanisms

**H-bond** networks from **DEG** + **water** link particles in **print/cure**, raising **restraint** strength when both polar components are balanced. **Burn-out** consumes **DEG** and disrupts **H-bonds**; **sintering** forms **Cr–O** bridges. **Water** contributes little to late-stage strength; an **optimal binder content** emerges for **post-sinter** cohesion. **Hydroxyl count** (**2-ethoxyethanol < DEG < triol**) tracks **early** strength in this workflow.

**Sets A/B** in **Table 1** vary **water/DEG** ratios at fixed **particle** count to show **non-monotonic** **cohesion**: too much **water** dilutes **DEG** **H-bond** donors, while **DEG-rich** mixes retain **organic** **linkers** through **cure** but still **pyrolyze** during **burn-out**, so **post-sinter** **Cr–O** **bridges** dominate **ultimate** **strength** in the model.

## Limitations

Nanoparticle size and **nanosecond** MD windows do not map **one-to-one** to industrial **BJP** time/length scales; the study aims at **mechanistic** trends rather than quantitative part-scale prediction.

## Relevance to group

Penn State **mechanical engineering** / **van Duin**-group **ReaxFF** application to **additive manufacturing** binders and **oxide** powder beds.

## Citations and evidence anchors

- `papers/Gao_PCCP_binder_jetting_3D_printing.pdf` (PCCP article PDF).

## Related topics

- [[reaxff-family]]
