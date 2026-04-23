---
id: paper:2024shen-construction-unveiling-intricacies
type: paper
title: "Unveiling the intricacies of steel corrosion induced by chloride: Insights from reactive molecular dynamics simulation"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:alloys-metallurgy
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reactive-md
  - keyword:water-interfaces
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:dft-static
  - keyword:qm-training-data
candidate_tags: []
source_refs: []
doi: "10.1016/j.conbuildmat.2024.137839"
year: 2024
authors:
  - "Shen, F."
  - "Li, M."
  - "Liu, G."
  - "van Duin, A. C. T."
  - "Zhang, Y."
venue: "Constr. Build. Mater."
pdf_sha256: "216492efa9e897200f298b35b5dedbdf4fae6d6fda4927ed7f5f27aa65a5b38f"
pdf_path: "papers/Shen_Construction_Building_Mat_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024shen-construction-unveiling-intricacies -->

## Summary

Shen and colleagues develop **Fe/Cl** extensions for **ReaxFF** to study **chloride-assisted corrosion** of an **Fe(100)** surface in **alkaline aqueous electrolyte** using **LAMMPS**. **Cluster DFT** (**B3LYP-D3(BJ)**, **6-311++G(2df,2p)**) and **periodic CASTEP (GGA-PW91)** data train and validate **bond dissociation**, **angle distortion**, **adsorption energies** (top/bridge/hollow **Cl** on Fe(100)), and **Mulliken charges**. The **NVT** trajectory (**300 K**, **Δt = 0.1 fs**, **500 ps total**) for a **~34.4 × 34.4 × 66.3 Å\(^3\)** cell with **3168 Fe** atoms and explicit **water/Na\(^+\)/Cl\(^-\)/OH\(^-\)** at **pH 13.5** and **1 mol/L Cl\(^-** captures **oxide growth**, **Fe dissolution**, **chloride catalysis**, and **competitive OH\(^-\)** vs **Cl\(^-** adsorption.

## Methods

**1 — MD application (ReaxFF, §2.3).** **Engine / code:** **LAMMPS** with **ReaxFF** **molecular** **dynamics**. **System:** **Fe(100)** **slab** in **~34.4 × 34.4 × 66.3 Å\(^3\)** cell, **3168** **Fe** atoms, **1160** **H\(_2\)O**, **27** **Na\(^+\)**, **20** **Cl\(^-\)**, **7** **OH\(^-\)** (**pH 13.5**, **1 mol/L** **Cl\(^-\)**). **Boundaries:** **PBC** in **x,y**; **fixed** **z** with **reflective** upper **wall**. **Ensemble / T:** **NVT** at **300 K** with **NVT** **thermostat** settings as in §2.3 (damping/algorithm in **VOR** **PDF** if not repeated here). **Timestep / duration:** **Δt = 0.1 fs**; **500 ps** **total** **trajectory**; **snapshots** every **1000** **steps**; **OVITO** for film analysis. **Barostat / pressure control:** **N/A** for this **NVT** **slab** setup. **Electric field / external bias:** **N/A**. **Replica / metadynamics / umbrella:** **N/A** in the reported protocol.

**2 — Force-field training.** **Parent / scope:** **Fe/Cl** **extensions** to **ReaxFF** for **aqueous** **Fe** **corrosion** chemistry. **QM reference:** **B3LYP-D3(BJ)/6-311++G(2df,2p)** **cluster** data; **CASTEP** **GGA-PW91** **periodic** **(2×2)** **Fe(100)+Cl** **slab** (**4** **layers**, **15 Å** **vacuum**, **spin-polarized**, **340 eV** cutoff, **4×4×1** **k** mesh) for **E\_ads** **Cl** (top/bridge/hollow) and **Mulliken** data. **Training set / optimization:** **Fe–Cl** **bond** **curves**, **angle** **distortions**, **adsorption** **energies**; **weighted** **ReaxFF** **error** **functional** (§3.1); **Tables 2–4** for **parameters**. **Reference data:** **QM** **primary**; **RDF** **peaks** compared to **published** **Fe–Cl** **lengths** in **Findings**.

**3 — Static QM** — used for **parameterization** and **spot** **validation**; not a separate **static-only** **DFT** **application** **paper** beyond the training set.
## Findings

**Corrosion sequence.** Early dynamics show **oxide initiation** from **OH/O** interaction, then **Cl\(^-\)** accumulation that **weakens Fe–Fe** bonding and promotes **Fe dissolution** and **vacancy** formation, consistent with **catalytic** chloride roles emphasized in the discussion. **Charge analysis** tracks **Fe oxidation**, **O reduction**, and **Cl\(^-\)**-mediated **electron transfer** patterns over **5–500 ps**.

**Mechanistic detail (§3.2.2).** The paper traces **short-lived intermediates** (e.g., **Fe(OH)\(^+\)** formation and **Cl substitution** steps) culminating in **Fe(OH)\(_2\)**-like products, with **Cl\(^-\)** argued to remain **surface-catalytic** rather than bulk-intercalated—supporting a **catalytic** picture over direct **bulk chlorination**.

**RDF and morphology.** **Fe–O** and **Fe–Cl** **RDFs** align with **Fe–Cl** **~2.35 Å** vs a **~2.32 Å** **experimental** mean cited in the text. **Surface roughening** and **pitting** progress through **nucleation–growth–stabilization** by **500 ps**.

**Authored model limits** — **short** **ns**-scale **sampling** and **simplified** **electrolyte** (see **`## Limitations`**).
## Limitations

**Short nanosecond-scale** trajectories and **finite** electrolyte model **do not** capture **long-time** **passivation** or **macroscopic transport** in **cement pores**; **ReaxFF** accuracy is **lower** far from equilibrium bond lengths (noted in validation).

## Relevance to group

**Adri C. T. van Duin** co-authors **Fe/Cl ReaxFF** development applied to **infrastructure corrosion** chemistry—useful reference for **aqueous Fe oxidation** parameterization.

## Citations and evidence anchors

- Simulation parameters: **§2.3**; validation: **§3.1**; kinetics/mechanism: **§3.2–3.2.4** (*Constr. Build. Mater.* **443**, 137839 (2024)).

## Related topics

- [[reaxff-family]]
