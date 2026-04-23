---
id: paper:2018kapil-computer-phy-i-pi-universal
type: paper
title: "i-PI 2.0: A universal force engine for advanced molecular simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - method:enhanced-sampling
  - method:pimd
  - task:software
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.cpc.2018.09.020"
year: 2019
authors:
  - "Venkat Kapil"
  - "Mariana Rossi"
  - "Ondrej Marsalek"
  - "Riccardo Petraglia"
  - "Yair Litman"
  - "Thomas Spura"
  - "Bingqing Cheng"
  - "Alice Cuzzocrea"
  - "Robert H. Meißner"
  - "David M. Wilkins"
  - "Benjamin A. Helfrecht"
  - "Przemysław Juda"
  - "Sébastien P. Bienvenue"
  - "Wei Fang"
  - "Jan Kessler"
  - "Igor Poltavsky"
  - "Steven Vandenbrande"
  - "Jelle Wieme"
  - "Clemence Corminboeuf"
  - "Thomas D. Kühne"
  - "David E. Manolopoulos"
  - "Thomas E. Markland"
  - "Jeremy O. Richardson"
  - "Alexandre Tkatchenko"
  - "Gareth A. Tribello"
  - "Veronique Van Speybroeck"
  - "Michele Ceriotti"
venue: "Comput. Phys. Commun."
pdf_sha256: "413940892ee3e27869b7546f945d41ed61c160bf0321e0a0c3aa93eb441e8d2b"
pdf_path: "papers/Others/Kapil_PIMD_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018kapil-computer-phy-i-pi-universal -->

## Summary

**i-PI 2.0** is presented as a **modular, Python-driven client** that drives **ab initio** and **empirical** “**forces engines**” (external codes such as **DFT packages** or **MD engines**) to implement **path-integral MD**, **advanced thermostats**, **ring-polymer contraction schemes**, and other **enhanced sampling / nuclear quantum** workflows. The article is a **methods/software** contribution to the **molecular simulation ecosystem**, not a **ReaxFF parameterization** paper; it is included in the corpus as a **general tooling** reference. **Note:** the repository `paper_id` slug uses **2018** while the **journal volume (236, 2019)** reflects **publication timing**—frontmatter **`year`** follows the **bibliographic** year in the normalized record’s venue string. The abstract states the goal is to lower the **implementation barrier** for **state-of-the-art sampling** and **geometry optimization** across many **electronic-structure** and **empirical-potential** programs (abstract).

## Methods

- **Architecture:** **Python** package with **socket** communication to **external drivers** that return **forces** and **energy**; **NumPy** dependency noted in the **program summary** (abstract block).
- **Problem/solution framing:** positions **force evaluation** as the usual **bottleneck**, motivating a **refactored core** suited to **multiple replicas** and **advanced sampling** beyond the original **PIMD**-centric scope (introduction §1–2).
- **Licensing:** **GPLv3** and **MIT** noted for the **distribution**; **sample drivers** included for testing with **simple model** potentials (program summary).

**How i-PI drives MD (conceptual protocol).** **Engine / client:** **i-PI** is a **Python** **molecular dynamics** client that issues **coordinate** updates and receives **forces** from external **drivers** (**LAMMPS**, **CP2K**, **Quantum ESPRESSO**, etc.) over **sockets**, enabling **path-integral MD** (**PIMD**), **ring-polymer contraction**, **generalized Langevin** **thermostats**, **pressure** / **stress** control integrators, and **replica exchange** workflows described in *Comput. Phys. Commun.* **N/A — single-system production benchmark** — the article is a **software** paper, not one fixed **NVE**/**NVT** **nanosecond** trajectory with tabulated **timestep**/**duration** for a specific material. **PBC:** inherited from each **driver** supercell. **Pressure / stress control:** **N/A — target hydrostatic pressure (bar/GPa)** is not a built-in quantity of the **i-PI** client—**stress**/**pressure** coupling is delegated to driver-side integrators documented in the **CPC** article. **Electric field:** **N/A — bias** not part of the core **i-PI** feature summary here.

## Findings

**Outcomes.** **i-PI 2.0** extends **PIMD** and related **nuclear quantum** estimators while keeping **driver** coupling central, so **sampling** **algorithms** can be prototyped once and attached to many **QM**/**MM** backends.

**Comparisons.** The manuscript contrasts the refactored release with **i-PI (2014)** and positions it relative to other **community** **MD** frameworks in the **literature**.

**Sensitivity / limitations.** Practical throughput depends on **driver** **latency**, **parallelization**, and **network** settings—**deployment-specific**, as noted in **Limitations**.

**Corpus honesty.** Feature lists and licensing statements follow the **CPC** **PDF** (`pdf_path`); this page is **not** a substitute for the upstream **documentation** repository.
## Limitations

- Practical performance depends on **engine latency**, **parallelization**, and **network** coupling choices; these are **deployment-specific**.

## Relevance to group

Useful **infrastructure** adjacent to **LAMMPS/ReaxFF** workflows when **nuclear quantum effects** or **advanced sampling** is required; **not** a **van Duin group** authorship paper.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.cpc.2018.09.020` (`papers/Others/Kapil_PIMD_2019.pdf`).

## Related topics

- [[reaxff-family]]
