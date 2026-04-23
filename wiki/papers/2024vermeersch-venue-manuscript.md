---
id: paper:2024vermeersch-venue-manuscript
type: paper
title: "Computational Insights into Tunable Reversible Network Materials: Accelerated ReaxFF Kinetics of Furan–Maleimide Diels–Alder Reactions for Self-Healing and Recyclability"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:validation
  - material:polymer-organic
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reactive-md
  - keyword:polymer
  - keyword:dft-static
  - keyword:enhanced-sampling
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.4c05470"
year: 2024
authors:
  - "L. Vermeersch"
  - "T. Wang"
  - "N. Van den Brande"
  - "F. De Vleeschouwer"
  - "A. C. T. van Duin"
venue: "J. Phys. Chem. A"
pdf_sha256: "85215bee6dcc91c51f5c848d1c0a36b50b3888b14d3e56cb4a01b9c5e61b33ee"
pdf_path: "papers/Vermeersch_JPCA_DielsAlder_2024_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024vermeersch-venue-manuscript -->

!!! abstract "Scope"
    **ReaxFF MD** with the **bond boost** acceleration targets **retro Diels–Alder** kinetics of **furan + N-methylmaleimide** (endo/exo) as a model for **reversible covalent adaptable networks** (self-healing / recyclable polymer networks).

## Summary

**Covalent adaptable networks (CANs)** use **reversible bonds**—here the **furan–maleimide Diels–Alder (DA)** motif—to enable **self-healing** and **recyclability**. Prior work mapped **thermodynamics and kinetics** with **DFT** on small models, but **network environment** (chains, packing, stereochemistry) alters **endo vs. exo** pathways. This paper presents **ReaxFF molecular dynamics** accelerated by the **bond boost** method to study the **retro-DA** reaction for **furan** and **N-methylmaleimide**, benchmarking **endo/exo product ratios** against **DFT** and **experiment** while varying **bond-boost parameters**, and extending to **polymer-backbone** models and **temperature** with a **newly reparametrized** ReaxFF description.

## Methods

From the extract: **ReaxFF reactive MD** is used because **bond formation and cleavage** are central. **Bond boost** (Miron–Fichtorn-type; as applied in related epoxy–amine work) adds **targeted energy** along reaction coordinates to access **nanosecond** windows for chemistry that would otherwise require far longer real time. Simulations focus on **retro-DA** of **endo** and **exo** adducts, with **bond breaking tracked in ensembles of product molecules** (the abstract cites **40** product molecules). The **endo/exo ratio** from boosted trajectories is **compared to DFT** and **experiment** across **bond-boost parameter sets**; additional runs probe **polymer backbone** inclusion and **temperature**. **Full timestep, thermostat, and boost parameter tables** are in the article and **Supporting Information** (not fully contained in the p1–2 extract).

**1 — MD application (ReaxFF + bond boost).** **Engine:** **ReaxFF** **molecular** **dynamics** with **Miron–Fichtorn**-style **bond** **boost** to reach **reactive** **events** on **ns** **scales** (cited in relation to **epoxy–amine** precedent). **System:** **furan** / **N**-**methylmaleimide** **adducts**; **~40** **molecules** in the **stated** **gas**-phase **batch** and **O(10²–10³) atoms**-scale **supercell**-style **runs** in the **SI** (**N/A** for the exact **atom** **count** on *this* **note**). **NVT**-class **sampling** with **PBC**; **N/A** on this page for every **thermostat** **constant** and **.fs** **timestep** (see **VOR**/**SI**). **Barostat / NPT, external E-field, umbrella/metadynamics, replica exchange:** **N/A** in the high-level **abstract** summary. **Accelerated** **dynamics** — **bond** **boost** (not **hyperdynamics**/PRD unless stated in **PDF**—confirm there).

**2 — Force-field training** — **reparametrized** **ReaxFF** for the **Diels–Alder** / **furan**/**maleimide** **chemistry**; **DFT** and **experiment** **barriers** and **stereoisomer** **ratios** **enter** the **fit** and **validation** (abstract; **SI** for **loss** and **data**). **3 — Static QM** — **DFT** **retro** **barriers** (~**3 kcal/mol** **endo**/**exo** **gap** in the **introduction** narrative) used as **benchmarks**; full **level-of-theory** lines on **p1–2** are **incomplete**—**use** **`pdf_path`**.
## Findings

**Kinetics, stereochemistry, and CAN relevance.** The **abstract** states **ReaxFF**+**bond** **boost** matches **relative** **retro-DA** **kinetics** for **furan** / **N-methylmaleimide** and **endo**/**exo** **partitioning** **vs** **DFT** and **experiment** across **boost** **settings**; the **reparametrized** **FF** also tracks **polymer** **backbone** and **temperature** **effects** in **network**-like **setups** (as claimed). A **~3** **kcal**/**mol** **stereochemical** **split** in **retrod** **barriers** (introduction) **motivates** **rare**-**event** **sampling** of the **back** **reaction** for **reversible** **covalent** **adaptable** **networks** **(CANs)**.
## Limitations

Bond boost is an **acceleration approximation**; parameters must be **validated** for each reaction class. The local PDF is a **galley**; cite the **version-of-record** for pagination. CAN kinetics in real materials spans **longer times** than accessible **unboosted** ReaxFF trajectories.

## Relevance to group

**Adri C. T. van Duin** is corresponding author; the study extends **ReaxFF** into **reversible polymer networks** and **accelerated reactive MD** workflows.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.4c05470](https://doi.org/10.1021/acs.jpca.4c05470)

## Related topics

- [[reaxff-family]]
