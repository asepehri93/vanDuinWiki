---
id: paper:2019zhu-acs-unveiling-carbon
type: paper
title: "Unveiling Carbon Ring Structure Formation Mechanisms in Polyacrylonitrile-Derived Carbon Fibers"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:experiment-integrated
  - scale:multiscale
  - material:polymer-organic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.9b15833"
year: 2019
authors:
  - "Zhu, Jiadeng"
  - "Gao, Zan"
  - "Kowalik, Małgorzata"
  - "Joshi, Kaushik"
  - "Ashraf, Chowdhury M."
  - "Arefev, Mikhail I."
  - "Schwab, Yosyp"
  - "Bumgardner, Clifton"
  - "Brown, Kenneth"
  - "Burden, Diana Elizabeth"
  - "Zhang, Liwen"
  - "Klett, James W."
  - "Zhigilei, Leonid V."
  - "van Duin, Adri C. T."
  - "Li, Xiaodong"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "698399184701995e8f4ebba7c6ff5f6af6d57137655f0c535c7d357fda1a3254"
pdf_path: "papers/Zhu_ACS_AMI_2019_PAN_CarbonFiber.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2019zhu-acs-unveiling-carbon -->

!!! abstract "Scope"

Joint experiments and multiscale modeling (ReaxFF atomistics plus microscale simulation) on polyacrylonitrile-derived carbon fibers, linking carbonization temperature to ring-structure evolution and mechanical trends.

## Summary

Carbon fibers from polyacrylonitrile precursors dominate commercial production; their properties depend sensitively on stabilization and carbonization schedules. The study isolates carbonization temperature while holding other processing variables fixed, combining detailed materials characterization with atomistic ReaxFF modeling and microscale simulation to relate six-membered ring formation and graphitic ordering to strength, ductility, and modulus trends measured experimentally. The **multiscale** framing links **atomistic** ring-condensation statistics to **continuum** mechanical property targets relevant to **aerospace** and **structural** composites supply chains.

## Methods

**Experiments.** Oxidized **PAN** precursor fibers (**ρ** ≈ **1.401 g cm⁻³**, commercial source per article) were **carbonized** at **1800 K**, **2300 K**, or **2800 K** for **30 min** with heating rate **10 K min⁻¹** in flowing **N₂** (**38 scfh** at the facility noted in the paper). Cooled fibers yielded measured densities **1.746**, **1.772**, and **1.858 g cm⁻³** at the three temperatures, respectively.

**Characterization.** **FE-SEM** and **HR-TEM** for morphology; **CHNS/O elemental analysis**; **XRD** (Cu Kα, **2θ** = 10°–80°); **Raman** (**514 nm**); **XPS** (surface chemistry); **gas pycnometry** for density (**ASTM D382**-referenced protocol in the article).

**Atomistic simulation (ReaxFF).** Reactive simulations probe **carbon ring** formation and **graphitic** ordering kinetics as a function of **carbonization temperature**, tied to the experimental temperature ladder.

**Microscale simulation.** Continuum/microstructure-level models (per article) connect evolving **ring** statistics and morphology to **strength**, **ductility**, and **Young’s modulus** trends.

**Integration.** The workflow tests whether **accelerated graphitic nucleation and growth** at higher **T** explains **lower strength/ductility** and **higher modulus** measured on fibers.

**ReaxFF protocol (MD application).** The article reports reactive MD in LAMMPS using a **CHON**-capable ReaxFF description to capture **carbonization**-driven ring formation; **N/A —** full timestep, thermostat, ensemble (NVT vs NPT), and cell boundary conditions for each annealing stage are not copied line-by-line to this page (see *ACS Appl. Mater. Interfaces* text and any SI). **N/A —** barostat for hydrostatic pressure if only NVT stages are used. **N/A —** external electric field. **N/A —** replica exchange, metadynamics, or umbrella sampling for the ReaxFF block.

**Static QM (block 3).** **N/A** — not a DFT-only paper; DFT is not the central method block for the main claims.

**FF training (block 2).** **N/A** — applies an existing ReaxFF parameterization; no new ReaxFF fit is the focus of the reported work.

## Findings

**Experiments vs simulation.** Mechanical testing matches the simulation directionality: **strength** and **ductility** **decrease** while **Young’s modulus** **increases** as **carbonization temperature** rises.

**Mechanism.** Atomistic and microscale results attribute the trade-off to **faster graphitic phase nucleation and growth** at elevated temperature, linking **six-membered ring** development and **ordering** to the measured **stiffening** and **embrittlement** trends.

**Outlook.** The authors frame the coupled **experiment + ReaxFF + microscale** pipeline as a basis for **alternative precursors** and **processing** optimization toward **lower-cost**, high-performance **carbon fibers**. **Six-membered ring** population is emphasized as a **process fingerprint**: higher **T** accelerates **graphitic** ordering, raising **stiffness** at the expense of **ductility** in the combined modeling story.

## Limitations

Fiber experiments integrate many microstructural degrees of freedom; atomistic models idealize chemistry and cannot capture full furnace-scale transport or defect distributions. **Microscale** **fracture** models depend on **morphology** **meshes** derived from **imaging**; misalignment between **2D** **sectioning** statistics and **3D** **void** networks can shift **predicted** **modulus** trends even when **atomistic** chemistry is qualitatively correct. **Raman** **I(D)/I(G)** trends should be interpreted alongside **laser** **spot** **averaging** and **fiber** **texture** as described in the **experimental** **sections**.

## Relevance to group

Flagship collaborative effort between Virginia and Penn State groups using ReaxFF alongside microscale fracture simulations for carbon-fiber process science.

## Citations and evidence anchors

- https://doi.org/10.1021/acsami.9b15833

## Related topics

- [[reaxff-family]]
