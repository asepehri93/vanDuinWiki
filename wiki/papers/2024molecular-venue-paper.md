---
id: paper:2024molecular-venue-paper
type: paper
title: "Molecular modeling of the microstructure evolution during carbon fiber processing"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:carbon-hydrocarbon
  - method:monte-carlo
  - method:classical-md
  - material:graphene-carbon-nano
  - task:application
paper_keywords:
  - keyword:monte-carlo-sampling
  - keyword:thermal-decomposition
  - keyword:graphene-carbon
candidate_tags: []
source_refs: []
doi: "10.1063/1.5000911"
year: 2017
authors:
  - "Desai, S."
  - "Li, C."
  - "Shen, T."
  - "Strachan, A."
venue: "J. Chem. Phys."
pdf_sha256: "c3226bcf659b8a288409b5b4f9f5fc983f71642219558dfe6c3ff57ae0d3d637"
pdf_path: "papers/Others/Molecular modeling of the microstructure evolution during carbon fiber processing.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2024molecular-venue-paper -->

## Summary

Desai and colleagues introduce **MD-CF**, a **coarse-grained simulator** that couples **kinetic Monte Carlo (kMC)** bond-formation steps with **classical molecular dynamics (MD) relaxation** to model **carbonization and graphitization** of **stabilized polyacrylonitrile (PAN)** precursors into **carbon fibers**. Inputs are the **initial ladder-like carbon skeleton** (heteroatom detail averaged out) and **physics-based reaction rates** for \( \mathrm{sp}^2 \) bond formation between neighboring ladders; the workflow targets **cross-sectional microstructure** and **transverse elastic properties**, comparing against **TEM-like morphology** (curved sheets, hairpin motifs), **X-ray diffraction** patterns, and **experimental transverse moduli** (order 1–5 GPa).

## Methods

**Scope (processing stages).** The model focuses on **carbonization** (reported roughly **1300–2000 K**) and **graphitization** (**2700–3000 K** in industrial practice, per the article’s background), after **stabilization** has produced ladder polymers; spinning is not simulated.

**Representation.** Stabilized PAN is represented as **periodic, infinitely long coarse-grained chains** aligned along the fiber \(Z\) axis within a cell with **3D periodic boundaries**. Each ladder has **saturated \(\mathrm{sp}^2\) carbons** and **reactive carbons** intended to form new \(\mathrm{sp}^2\) links between chains.

**kMC + MD cycle.** Graphitization proceeds in **cycles**: propose **new bonds** between eligible nearby reactive pairs subject to **distance and angular alignment criteria** (distance cutoff \(R_0\), improper-angle cutoff \(\theta_0\), stochastic acceptance with probability \(\eta\); Fig. 2 in the paper), then **relax** the network with MD. Misalignment penalties are estimated from strain energy of misoriented ladders to justify suppressing reactions between poorly aligned pairs.

**Rates and temperature.** Bond-formation rates follow an **Arrhenius picture** consistent with **activation barriers** influenced by separation and alignment; the paper discusses relating barrier increases to rate suppression at **carbonization temperatures** (e.g., order-of-magnitude estimates around **2500 K** in the barrier discussion).

**Property evaluation.** The authors compute **XRD**-comparable signals from the evolved microstructures and estimate **transverse moduli**, interpreting low transverse stiffness with **inter-sheet sliding** and **longitudinal texture** in the idealized cell.

**1 — Hybrid kMC + classical MD (not ReaxFF RMD).** **Engine / integrator:** **MD** relaxation (canonical **NVT**/**NVE**-style as defined in the original **MD** substeps) after each **kMC** bond-formation **MC** step (the **MD-CF** scheme in *J. Chem. Phys.* **147**, 224705 (2017)). **PBC** **3D** **supercell** with **ladder** **carbon** **CG** chains; **T** tied to **Arrhenius** **rates** for **sp\(^2\)** bond formation (**~1300–3000 K** regimes in background and **graphitization** discussion). **0 GPa** isotropic **hydrostatic** **NPT** control: **N/A** — the cited protocol focuses on **internal** kinetics, not a GPa-resolved **Parrinello** barostat study in the wiki excerpt. **Timestep**, full **ns**-scale **production** span, and **thermostat** damping: **JCP** *Computational*; this page’s **`extraction_quality` is `partial`**. **2 — ReaxFF / QM training:** **N/A** (the paper explicitly contrasts to **ReaxFF**-based early pyrolysis work as a different modeling line). **3 — DFT** as central method: **N/A**.
## Findings

The MD-CF workflow produces **cross-sectional microstructures** with **curved graphitic sheets** and **hairpin-like** features consistent with microscopy narratives in the paper. **Simulated XRD** agrees well with experiment. **Transverse moduli** fall in the **1–5 GPa** range, matching **high-modulus** fiber experiments better than some **high-strength** fibers (which can be higher). **Higher reaction rates** in the model yield **more porous** microstructures and **lower moduli**, linking **kinetics** to **pore formation** and **stiffness**. **Comparisons** to **TEM**-like morphology, **XRD**, and **GPa**-scale **transverse** moduli are in the main bullets. **Extraction** is only **partial** in frontmatter; confirm details in `papers/.../Molecular modeling of the microstructure...pdf`.
## Limitations

The coarse-grained reaction model **averages** detailed gas elimination and chemistry during carbonization (contrasted with prior **ReaxFF** studies of early pyrolysis steps). Chains are **perfectly aligned** along \(Z\), focusing on **transverse** structure rather than full three-dimensional texture. Absolute kinetics require **approximate** barriers and simplified rate rules.

## Relevance to group

Methodological reference for **hybrid kMC/MD** microstructure evolution of **carbonaceous** materials; distinct from ReaxFF but relevant to **reactive processing** workflows.

## Citations and evidence anchors

- Methods: Sections II–III (J. Chem. Phys. **147**, 224705 (2017)); DOI above.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
