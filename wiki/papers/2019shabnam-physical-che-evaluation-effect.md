---
id: paper:2019shabnam-physical-che-evaluation-effect
type: paper
title: "Evaluation of the effect of nickel clusters on the formation of incipient soot particles from polycyclic aromatic hydrocarbons via ReaxFF molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:catalysis-surfaces
  - domain:reactive-md
  - method:reaxff
  - material:metal-surface
  - task:application
candidate_tags: []
source_refs: []
doi: "10.1039/C9CP00354A"
year: 2019
authors:
  - "Sharmin Shabnam"
  - "Qian Mao"
  - "Adri C. T. van Duin"
  - "K. H. Luo"
venue: "Phys. Chem. Chem. Phys. 21:9865-9875 (2019)"
pdf_sha256: "7329f8a1300deec0579b23731e09b8e154eb42f162a25d3d1dbf5dd3587c7b78"
pdf_path: "papers/Shabnam_PCCP_Ni_soot_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019shabnam-physical-che-evaluation-effect -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Soot formation in engines involves **polycyclic aromatic hydrocarbons (PAHs)** as gas-phase precursors, but **trace metals**—from fuels, lubricants, or wear—can perturb **nucleation** and **growth** in ways that are difficult to isolate experimentally. Shabnam, Mao, van Duin, and Luo apply **ReaxFF reactive molecular dynamics** in the **NVT** ensemble to compare **homogeneous** PAH assembly with **Ni₁₃-catalyzed** assembly for a ladder of **PAH monomers** (**naphthalene** through **circumcoronene**) from **400 K to 2500 K**. The central question is how a small **nickel cluster** changes **incipient soot** morphology and chemistry relative to metal-free trajectories at the same temperatures.

## Methods

Each simulated system contains **one Ni₁₃ cluster** and **one PAH species** per study (monomer identity and temperature are scanned across the abstract’s matrix). **ReaxFF** supplies bond-order-dependent reactivity for **C/H** chemistry and **Ni–C** interactions consistent with the parameterization cited in *Phys. Chem. Chem. Phys.* Simulations are analyzed for **clustering timescales**, **chemisorption** signatures on Ni, **dehydrogenation** extent, and **carbonization** toward **fullerene-like** soot motifs. The paper contrasts trajectories **with** versus **without** Ni at matched temperatures to attribute differences to the metal rather than to stochastic gas-phase alone.

**1 — MD (ReaxFF, NVT).** **Molecular** **dynamics** in the **NVT** **ensemble** ( **abstract** ) for **incipient** **soot** from **naphthalene** through **circumcoronene** at **400**–**2500** **K**; **3D** **PBC** **typical** of **gas**-**phase**-**like** **cells** with **Ni₁₃** **+** **PAH** ( **atom** **counts** and **box** in **PCCP**). **Engine** ( **LAMMPS** for **ReaxFF** in **group**-**style** work): **N/A** on this page if the **local** **extract** omits the **string** “**LAMMPS**”—**confirm** in **full** **PDF**; **reactive** **MD** is **explicit** in the **title** / **abstract**. **Timestep**, **thermostat** **damping** or **Nose**-**Hoover** **τ**, and **run** **lengths** in **ps** / **ns** are in **PCCP** **Methods**; **N/A** to **reproduce** all **here**. **Barostat, pressure**-**control** in **NVT** **soot** **burner**-**like** **cells** **N/A** for the **NVT** **stated** in the **abstract** ( **constant** **volume** **gas**-**cell** **soot** **model**). **Shear, external** **E**-**field, shock, umbrella, metadynamics: N/A** unless the **main** **text** **says** so.

**2 — Force-field training.** **N/A** as a **new** **ReaxFF** **fit** ( **uses** **cited** **Reaxff** for **C/H** and **Ni**-**containing** **soot** **chemistry** per **PCCP** ).

**3 — Static DFT** as **sole** **outcome** **N/A.**
## Findings

At **low temperature**, PAHs aggregate by **stacking and binding** around the **nickel** cluster, producing **larger nascent particles earlier** than in homogeneous systems—nickel acts as a **structural template** that accelerates **physical clustering**. Between **1200 K and 1600 K**, the authors report **chemisorption** of PAHs onto Ni surfaces, producing **incipient soot** morphologies distinct from purely van der Waals stacks. Near **2000 K**, they identify **chemical nucleation**: **nickel-assisted dehydrogenation** and **chemisorption** yield **stable soot growth** that does not occur in Ni-free runs at the same conditions. At **2500 K**, Ni **accelerates ring opening** and **graphitization** toward **fullerene-type** soot and increases particle size relative to homogeneous trajectories. Across the ladder, the cluster shifts the balance between **physical stacking** and **metal-catalyzed covalent growth**, motivating caution when extrapolating gas-phase soot models to metal-rich flame zones.

## Limitations

Cluster size and metal identity are fixed; gas-phase equivalence to flame chemistry is approximate. ReaxFF uncertainty for organometallic Ni–C edge cases should be kept in mind.

## Relevance to group

Penn State–led study coupling catalytic metals to PAH/soot chemistry using ReaxFF, aligned with fuels and emissions research threads.

## Citations and evidence anchors

`papers/Shabnam_PCCP_Ni_soot_2019.pdf` — abstract (temperature stages, Ni13, PAH list). https://doi.org/10.1039/C9CP00354A

## Related topics

- [[reaxff-family]]
