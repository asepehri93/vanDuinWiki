---
id: paper:2018zhang-fuel-234-201-investigation-ethanol
type: paper
title: Investigation of ethanol oxidation over aluminum nanoparticle using ReaxFF
  molecular dynamics simulation
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:fuel-combustion
- domain:reactive-md
- method:reaxff
- task:application
- material:metal-surface
- scale:atomistic
paper_keywords:
- keyword:combustion
- keyword:reaxff-application
- keyword:reactive-md
- keyword:metallic-systems
- keyword:dft-static
candidate_tags: []
source_refs: []
doi: 10.1016/j.fuel.2018.06.119
year: 2018
authors:
- Yi Ran Zhang
venue: Fuel, 234 (2018) 94-100. doi:10.1016/j.fuel.2018.06.119
pdf_sha256: 500f1d3bafaa67a89c43fbcbdc85f01ccca8282f97279e9b625da0e328d8ad8b
pdf_path: papers/YiranZhang_Fuel_Al_ethanol_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018zhang-fuel-234-201-investigation-ethanol -->


## Summary

**ReaxFF molecular dynamics** is used to follow **ethanol oxidation** in contact with **aluminum nanoparticles** prepared with **different oxidation states** (bare metal versus **thin** or **thick oxide** shells prepared by controlled **O₂** exposure in **NVT** **LAMMPS** runs). The abstract reports that nanoparticles can lower the **initial** ethanol reaction **temperature** to **324 K** on **pure Al**, contrasts **OH-abstraction** vs **H-abstraction** pathways by oxide coverage, and quotes **Eₐ ≈ 4.58 kcal/mol** for **adsorptive dissociation** on the **thin-oxide** particle, benchmarked against **DFT**.

## Methods

**1 — MD application (ReaxFF, *Fuel* 234 (2018) 94–100, §2–3).** Simulations use **ReaxFF** reactive **molecular dynamics** implemented through the **REAXC** package in **LAMMPS**. **System size & composition:** an **Al** nanoparticle **~2.8 nm** in diameter (**856 atoms**) is prepared first, then placed in a cubic cell **50 × 50 × 50 Å** with **PBC** in all directions. **Oxide variants:** **300** or **600 O₂** molecules are distributed around the nanoparticle for **NVT** oxidation at **298 K** (velocity **Verlet**, **timestep 0.2 fs**, **2 × 10⁶** steps, **0.4 ns** total) until oxygen uptake and potential energy plateau; resulting oxide shells are **~0.76 nm** (**APO300**) and **~1.03 nm** (**APO600**) thick, with **pure Al** denoted **AP**. **Ethanol oxidation cells:** **20 ethanol** and **60 oxygen** molecules (**stoichiometric** **C₂H₅OH/O₂** mixture) surround each nanoparticle; initial velocities are **Maxwell–Boltzmann** at **298 K**. **Ensemble:** **NVT** is used for the ethanol–oxygen runs described in §3. **Temperature program:** systems are heated from **298 K** toward reaction temperatures (the **C₂H₅OH/O₂** gas mixture without nanoparticles is ramped to **3000 K** at **2 K/ps** in §3.1; nanoparticle-bearing systems use **298 → 500 K** at the same **2 K/ps** rate before higher-**T** stages in §3.2). **Thermostat / barostat / pressure:** **NVT** runs are **constant-volume** thermal sampling; **N/A — hydrostatic pressure** is not an independent control variable in those **NVT** **segments** (no **NPT** **barostat** in the **ethanol**–**O₂** **production** protocol described in §3). **Duration:** oxidation prep **~0.3 ns** to equilibrate oxygen uptake; ethanol–surface studies extend to **2000 K** in the narrative examples in §3.2. **Electric field:** **N/A —** not applied. **Enhanced sampling:** **N/A —** no **umbrella**, **metadynamics**, or **replica exchange**; the authors additionally report selected **NVE** microcanonical checks for nanoparticle systems starting at **298 K** (§3.3). **Electrostatics / QEq:** handled within the standard **ReaxFF** formulation in §2.

**2 — Force-field training.** **N/A —** application paper using the **Al/C/H/O** **ReaxFF** of **Hong** *et al.* as cited in §2 (not a new parameterization).

**3 — Static QM / DFT-only.** **DFT** references are used for **barrier** comparisons (e.g., **O–H** / **Cα–O** cleavages on **Al(111)** and **Al₂O₃(0001)** surfaces) alongside **bond-restraint** **ReaxFF** barrier extraction in §3.2.

**Analysis.** Track adsorption vs dissociation, temperature-dependent rates, and gas-phase fragments; **activation energy** for **adsorptive dissociation** on **APO300** is reported as **4.58 kcal/mol**, compared with **DFT** in the abstract.
## Findings

- **O₂ vs ethanol adsorption:** **Oxygen** adsorbs more readily than **ethanol** on the Al-based surfaces under the simulated conditions (abstract).
- **Oxidation state steers chemistry:** **OH-abstraction** dominates on **pure Al**, whereas **H-abstraction** is more prevalent on **oxidized** particles (abstract).
- **Oxides block dissociation:** A surrounding **oxide layer hinders adsorptive dissociation** of ethanol relative to bare pathways; **H** from hydroxyl couples to **Al** vs **O** depending on oxide thickness (abstract).
- **Products vs uptake:** With a **thick oxide**, volatile products such as **H₂O** and **CO** appear, whereas for **thin or no oxide**, much of the **C/H/O** from ethanol **diffuses into the nanoparticle** rather than desorbing as CO/H₂O (abstract).
- **Kinetics:** Dissociation rates increase with temperature; reported **Eₐ ≈ 4.58 kcal/mol** for the thin-oxide **adsorptive dissociation** channel matches **DFT** within the authors’ comparison (abstract).

## Limitations

**ReaxFF** remains empirical; barriers and product channels should be spot-checked with **QM** when extrapolating outside the trained **Al/C/H/O** chemistry window. **Industrial** ignition involves **ms**–**s** timescales and **continuum** transport not captured in these **nanosecond** cells. **Coauthorship note:** **Adri C. T. van Duin** is a coauthor on the *Fuel* article; treat quantitative reuse like any external **ReaxFF** application and cite the **version-of-record** **PDF** for any reproduction work.

## Relevance to group

**Combustion/nanofuel** atomistic study in the corpus; useful for linking **Al nanoparticle oxidation state** to **ethanol** decomposition channels, separate from the Penn State **ReaxFF parameterization** lineage unless a coauthorship update is recorded in the version-of-record PDF.

## Citations and evidence anchors

- DOI: `10.1016/j.fuel.2018.06.119`
- Full **Methods** in the article lists integrator settings, temperatures, and nanoparticle construction beyond the abstract-level kinetics quoted on this page.

## Related topics

- [[reaxff-family]]
