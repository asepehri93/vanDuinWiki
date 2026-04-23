---
id: paper:2015liu-venue-jp5b08026
type: paper
title: "Tunable mechanical and thermal properties of one-dimensional carbyne chain: phase transition and microscopic dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:reaxff
  - method:classical-md
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b08026"
year: 2015
authors:
  - "Xiangjun Liu"
  - "Gang Zhang"
  - "Yong-Wei Zhang"
venue: "Journal of Physical Chemistry C"
pdf_sha256: "e3bf1abd590fe81343ba2a42ef01bc5a91d356caa8dc8ea0419dc419bd97ed2d"
pdf_path: "papers/ReaxFF_others/Liu_carbyne_JPCC_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015liu-venue-jp5b08026 -->

## Summary

One-dimensional sp-hybridized carbon chains—α-polyyne (alternating single/triple bonds) and β-cumulene (repeating double bonds)—are studied with reactive MD using **LAMMPS** and the literature **ReaxFF CHO** parameter set (*J. Phys. Chem. C*). The paper stresses mechanical contrast (bending stiffness, Young’s modulus, tensile response), a thermally driven cumulene→polyyne transition with a critical temperature near **499 K** and ultrafast bond rearrangement (**~145 fs** for the **50-atom** chain in the authors’ Fig. 2 trajectory), and thermal transport from **Green–Kubo equilibrium MD** (cumulene **κ** reported around **83 W/(m·K)** at **480 K** in their calculation, roughly **twice** the polyyne value there, with defective polyyne dropping to about **13%** of pristine polyyne **κ**).

## Methods

**MD application.** Simulations use **LAMMPS** with **ReaxFF** for carbon/hydrogen chemistry: bond orders (σ, π, π–π contributions) are updated **every MD step**, and charges follow ReaxFF’s **geometry-dependent** scheme (*J. Phys. Chem. C*, Computational Methods). Integration is **velocity Verlet** with **Δt = 0.1 fs**. A repeated protocol equilibrates at target **T** with **100 ps NVT** (Nosé–Hoover thermostat) followed by **100 ps NVE** to check energy conservation before longer segments. **Carbyne** models are **50 carbon atoms** per chain with **periodic boundary conditions along the chain axis** and **free** boundaries transverse to the axis in the thermal-conductivity setup; heat-flux data are accumulated **each timestep for 10 ns** for **Green–Kubo** analysis (the article notes PBC along the chain omits explicit length/edge effects in **κ**). **Mechanical loading** applies **uniaxial strain** by end displacements at **2.5×10⁻⁵ Å/fs** (strain-rate independence reported between **2.5×10⁻⁶** and **2.5×10⁻⁴ Å/fs**); **virial stress** is reported using a **3.35 Å** effective chain diameter (plus **1D force** metrics to reduce cross-section ambiguity). **Bending** analyses give fitted **D ≈ 8.5 eV·Å** (cumulene) vs **6.7 eV·Å** (polyyne) in the small-curvature regime discussed in the text. **Phase-transition** studies compare slow heating (**~0.04 K/fs**, near-pristine polyyne) with **2.5 K/fs** heating that leaves **defective** bond populations. **Barostat / NPT**, **applied electric fields**, and **umbrella or metadynamics** are **not used** in these chain protocols.

**Force-field training.** **N/A —** the article **applies** an existing **ReaxFF** parametrization (QM-fitted in prior work cited there); it does not document a new optimization campaign.

**Static QM / DFT production.** **N/A —** reported observables are from **ReaxFF MD**; **DFT** enters only as **published** benchmarks when the authors compare transition temperatures and bending stiffness to prior first-principles studies.

## Findings

**Outcomes and mechanisms.** Near **499 K**, cumulene converts to polyyne on a **sub-200 fs** timescale for the **50-atom** model; slow heating from **5 K** yields alternating single/triple bonding, whereas **2.5 K/fs** ramps (or initializing hot cumulene) introduce **nonideal** bond-length peaks (**~1.45 Å**) tied to **defective** polyyne. **Cumulene** is **stiffer** in bending (**D** about **27%** larger than polyyne in the quoted linear **E_b** vs **ρ²** regime) and shows **~2×** higher **thermal conductivity** than polyyne in the authors’ **Green–Kubo** results, with **defective** bonding collapsing polyyne **κ** to about **13%** of the pristine value. **Tensile** data for polyyne at **500 K** give failure near **~8% strain** with ultimate stress **~67 GPa** (or **~7.5 nN** 1D force) and a **Young’s modulus ~1345 GPa** from a linear fit to **~2% strain**—numbers the authors compare to diamond, graphene, and nanotube benchmarks in the same section.

**Comparisons.** The article contrasts its **499 K** transition temperature with a higher **DFT-based** literature estimate and lists **classical vs quantum statistics**, **PBC choices**, **ReaxFF** accuracy, and **DFT band-gap** issues as contributing factors—not as new experiments.

**Sensitivity.** **Thermal conductivity** and **persistence length** depend on temperature (e.g., **L_p ~ 33 nm** at **300 K** in their polymer-physics estimate); **mechanical** response is insensitive to the tested strain-rate window but **strongly** sensitive to **defect** content after fast heating.

**Authored limitations / outlook.** They flag **ReaxFF** mismatch to first-principles forces where **Peierls** distortion is delicate, finite-size/PBC effects in **1D** transport, and the need for careful **temperature ramps** to avoid **defective** polyyne when targeting ideal alternating bonds.

## Limitations

**ReaxFF** accuracy for sp-rich carbon, **classical** phonon statistics vs **quantum** modes, **PBC** choices along the **1D** chain, and **Green–Kubo** finite sampling all affect phase stability and reported **κ**; the authors explicitly compare their **499 K** transition temperature to higher **DFT** literature values and list multiple methodological reasons (*J. Phys. Chem. C* discussion section).

## Citations and evidence anchors

DOI `10.1021/acs.jpcc.5b08026`; PDF `papers/ReaxFF_others/Liu_carbyne_JPCC_2015.pdf`.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
