---
id: paper:2015cherukara-venue-paper
type: paper
title: "Ultra-fast Chemistry Under Non-equilibrium Conditions and the Shock to Deflagration Transition at the Nanoscale"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:shock-compression
  - keyword:energetic-materials
  - keyword:lammps
  - keyword:reaxff-application
  - keyword:reactive-md
source_refs: []
doi: "10.1021/acs.jpcc.5b05362"
year: 2015
authors:
  - "Mathew J. Cherukara"
  - "Mitchell A. Wood"
  - "Edward M. Kober"
  - "Alejandro Strachan"
venue: "J. Phys. Chem. C"
pdf_sha256: "d2b239386b230b7d51850aff9f9ca56c50b726a1533298ceabd99cc926b57a5c"
pdf_path: "papers/ReaxFF_others/Cherukara_Strachan_RDX_JPCC_2015_JustAccepted.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2015cherukara-venue-paper -->

## Summary

**Reactive molecular dynamics** with **ReaxFF** in **LAMMPS** follows **shock-induced collapse** of **cylindrical voids** in **RDX**, focusing on **ultrafast**, **non-equilibrium** chemistry and the emergence of a **deflagration** front from a nanoscale **hot spot**. The study contrasts **dynamically loaded** hot spots with a **static** thermal hot spot of comparable conditions. **Energetic** **material** **safety** models often assume **thermal** **explosion** **kinetics**; this work asks whether **shock** **focusing** at **voids** produces **distinct** **reaction** **pathways** and **front** **structures** not captured by **static** **heating** alone.

## Methods

### MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** with **ReaxFF** for **α-RDX** chemistry; the parameterization **merges** the authors’ **nitramine** training line with the **combustion-branch** ReaxFF data as cited in the manuscript.
- **System construction:** supported **shock** samples are built from a perfect **α-RDX** crystal containing a **single cylindrical void**; pore diameters **10–40 nm** are studied by scaling supercell replications (the **40 nm** case is built from an **8-molecule** unit cell replicated **84×3×204** along **[100]**, **[010]**, **[001]** with the pore centered **60 nm** from the impact face; smaller pores use scaled replications as tabulated in Section 2.1).
- **Pre-shock conditioning:** energy minimization, then **300 K** equilibration: **5 ps** **isobaric-isothermal** followed by **10 ps** **isochoric-isothermal** (as stated in Section 2.1).
- **Electrostatics / ReaxFF charge solve:** self-consistent partial charges are updated **each 0.1 fs** time step using a **conjugate-gradient** solver to a tolerance **1×10⁻⁶** (as stated in Section 2.2).
- **Shock / ensemble for the shock segment:** a **momentum mirror** piston imparts a **particle velocity** of **2 km s⁻¹**, producing ~**11 GPa** shock pressure in the overdriven regime described in the text; the shocked evolution is propagated in **constant-energy MD (NVE)** after piston impact (Section describing shock setup in the PDF).
- **Diagnostics:** spatially resolved **temperature**, **composition**, and **reaction-zone** tracking through void collapse and subsequent chemistry.
- **Barostat during shock:** **N/A —** shock segment is **NVE** piston-driven rather than stochastic NPT.
- **Electric field / replica sampling:** **N/A —** not used.
- **Boundary conditions / thermostat:** samples use **3D periodic boundary conditions (PBC)** for the crystalline **RDX** supercells; the **shocked** segment is **NVE** without an active **Nose–Hoover** or **Berendsen thermostat** during the **momentum-mirror** propagation (thermostating applies only in the pre-shock **300 K** equilibration stages).

### Force-field training

**N/A —** the manuscript **uses** a documented **ReaxFF** merge for RDX rather than introducing a wholly new parameterization workflow here.

### Static QM / DFT

**N/A —** not the primary modality; QM references appear as literature context for chemistry benchmarks.

## Findings

**Shock** focusing at a **nanoscale void** drives **exothermic RDX decomposition** fast enough that the hotspot **does not quench** within the first few **ps** of collapse. The largest pore develops a **thin reaction zone** propagating about **~0.25 km s⁻¹** with sharp **temperature and composition** fronts (abstract-level timescale **~10¹ ps**). A **statically heated** control at comparable thermodynamic conditions **does not** reproduce the same **deflagration-like** phenomenology, so **mechanical loading** and **momentum transport** matter in this model beyond pure heating. The discussion contrasts this pathway with **Tarver**-style kinetics assumptions (**J. Phys. Chem. C**). Outcomes depend on **pore diameter**, **crystal orientation**, and **particle velocity** (Section 2.1). This repo’s **Just Accepted** PDF may differ from the **VOR**; use the on-disk **PDF** for exact tables.

## Limitations

This repository copy is a **Just Accepted** manuscript PDF and may differ from the final **version of record** after production edits. The study isolates a **single cylindrical void** in an otherwise perfect crystal, so **porosity statistics**, **defects**, and **3D microstructure** of real charges are not captured.

## Relevance to group

Landmark **ReaxFF** + **shock** example for **energetic materials**, with explicit **LANL**/**Purdue** lineage tied to **RDX** chemistry and **hot-spot** physics.

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

LANL/**Strachan**-line **energetic** **materials** corpus pairs naturally with **RDX** **detonation** and **hot-spot** **physics** entries elsewhere in the wiki. Prefer the **VOR** PDF for **final** **tables** and **timesteps**.
