---
id: paper:2021thierry-tsafack-j-phys-chem-elucidation-molybdenum
type: paper
title: "Elucidation of Molybdenum Trioxide Sulfurization: Mechanistic Insights into Two-Dimensional Molybdenum Disulfide Growth"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - method:reaxff
  - method:dft-static
  - material:tmd
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nose-hoover
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.0c06964"
year: 2021
authors:
  - "Thierry Tsafack"
  - "Stephen F. Bartolucci"
  - "Joshua A. Maurer"
venue: "J. Phys. Chem. A"
pdf_sha256: "10fbcc067036ed16db6888a297554ae00b62219932e0f2a8a56c5534080e37ca"
pdf_path: "papers/ReaxFF_others/Tsafack_MoO3_S2_JPC_A_2021_online.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2021thierry-tsafack-j-phys-chem-elucidation-molybdenum -->

## Summary

Two-dimensional **MoS₂** growth from **MoO₃** and elemental sulfur feeds involves a zoo of **gas-phase sulfur allotropes** (**S₂–S₈**) and condensed **oxysulfide** intermediates whose elementary steps are difficult to isolate experimentally. This **J. Phys. Chem. A** article combines **ReaxFF molecular dynamics in LAMMPS** with **Gaussian** **DFT** (B3PW91 with LanL2MB-style basis handling as stated) to dissect how smaller sulfur units emerge from larger allotropes on **molybdenum oxide** templates and how those units participate in **sulfurization** toward **MoS₂**-like bonding motifs. The MD portion emphasizes **state-to-state connectivity** extracted from reactive trajectories, while DFT supplies **barriers** and **intermediates** for **S₂** and **S₃** channels that anchor the MD interpretation.

## Methods

**1 — MD application (ReaxFF, LAMMPS).** **MoO₃** **slabs** and **S\(_n\)** **allotropes** (and **oxysulfide** rings) are built in **Avogadro**, pre-relaxed with **MMFF94**, then placed in **~10 Å** **PBC** **cubic** **supercells** with explicit **atom** lists. After **conjugate-gradient** **relaxation**, each system receives **2** **ns** of **NVT** **equilibration** with the **temperature** **ramp** in the paper, then **production** **ReaxFF** **molecular dynamics** with **0.25** **fs** **timestep**, **Nosé–Hoover** **thermostat** (25 **fs** damping) on **T** = **500**, **700**, **850**, **1000**, **1150**, **1300** **K**. The **ReaxFF** **force field** follows the **single-layer** **MoS₂** **mechanical** **training** set cited in *J. Phys. Chem. A*. **Barostat** and **N/A** **independent** **isotropic** **pressure** **control** in these **NVT** **cells**; **N/A —** external **electric** **field**; **N/A — umbrella** in the reported **NVT** **ramp**; **N/A** to treat as **metadynamics**. Fragment **connectivity** **graphs** summarize **reaction** **pathways** from the **trajectories**.

**2 — Force-field training. N/A** — the study **uses** a published **ReaxFF** for **Mo–S–O** chemistry; it is not a new **parameter** **fit** report.

**3 — Static QM (DFT).** **Gaussian 09** **DFT** uses **B3PW91** with **LanL2MB**-style **ECP**/**basis** handling for **molybdenum** and light **atoms** (per **Methods**), **k-mesh** / **grid** settings and **tight** **force** **convergence** for **S₂** and **S₃** **reaction** **pathways**; **barriers** and **frequencies** support the **ReaxFF**-based **mechanism** story.
## Findings

Across allotrope starting points, reactive pathways repeatedly factor into **S₂**- and **S₃**-like fragments or their combinations, supporting a reduced reaction basis for complex sulfur vapor chemistry near the oxide surface. **MoO₃** is argued to **catalyze fragmentation** of larger allotropes, effectively funneling sulfur toward sizes that can insert into **Mo–S** networks. DFT barrier analysis for the highlighted channels yields temperature-dependent rates peaking near **1000–1100 K**, overlapping typical **chemical vapor transport** windows used in **MoS₂** growth. Together, the MD connectivity picture and DFT barriers provide a mechanistic narrative linking gas-phase speciation to experimentally accessible temperature ranges. Finite simulation cells and short reactive trajectories may omit long-range sulfur transport or gas-phase three-body chemistry; treat absolute reaction rates as order-of-magnitude guides unless validated against experiment or higher-level theory for the specific allotrope mixture. The article’s connectivity diagrams and temperature sweep should be read as mechanistic scaffolds for experimentalists tuning sulfur partial pressures and oxide pretreatment in MoS₂ growth reactors.

**Comparisons, sensitivity, corpus honesty.** DFT **barrier** **benchmarks** **complement** the **ReaxFF** **connectivity** data; the **1000**–**1100** **K** window is a key **sensitivity** to how **CVT** is tuned. All **kinetics** are **order-of-magnitude** unless the user reconciles to **measured** **S\(_2\)**/**S\(_8\)** **mixtures**.

## Limitations

Finite cells and short-timescale MD may omit long-range transport or reactor-scale effects; DFT level and ReaxFF transferability bound quantitative barrier accuracy.

## Reader notes (navigation)

- [[reaxff-family]]
