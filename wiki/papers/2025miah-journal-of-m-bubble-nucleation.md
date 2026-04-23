---
id: paper:2025miah-journal-of-m-bubble-nucleation
type: paper
title: "Bubble nucleation and Leidenfrost characteristics of nanoscale porous surfaces from molecular dynamics study: Effects of surface morphology and wettability variation"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:methods-software
  - material:metal-surface
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:lammps
  - keyword:classical-ff
candidate_tags: []
source_refs: []
doi: "10.1016/j.molliq.2025.126867"
year: 2025
authors:
  - "Md. Nurannabi Miah"
  - "Al-Kabir Hossain"
  - "Mohammad Nasim Hasan"
venue: "Journal of Molecular Liquids, 421 (2025) 126867"
pdf_sha256: "199f0eb030064a95aaaa39709824709ae32d11f3bbc0462e1bae842f1cc0f713"
pdf_path: "papers/Others/Leidenfrost_JMolLiq_Al-Kabir.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2025miah-journal-of-m-bubble-nucleation -->

!!! abstract

Non-equilibrium molecular dynamics with Lennard-Jones argon–platinum interactions simulates explosive boiling and Leidenfrost film formation on flat and square nano-porous platinum substrates, varying pore width (void fraction) and hydrophilic versus hydrophobic wetting of the base and pore walls; LAMMPS integrates trajectories with a 5 fs timestep after a staged equilibration and heating protocol.

## Summary

The paper studies **nanoscale boiling** of **liquid argon** on **platinum** substrates with **square nanopores**, comparing **flat** surfaces to porous geometries with void fractions **Φ = 17 %, 30 %, and 45 %** (pore widths **2.4, 3.2, and 4.0 nm** at fixed pore height). **Hybrid wettability** cases label hydrophilic (**phi**) and hydrophobic (**pho**) combinations of the flat base (**B**) and structured substrate (**S**): **BϕSϕ**, **BϕSpho**, and **BphoSϕ** (plus flat **Bϕ** / **Bpho** baselines).

## Methods

### System geometry and interactions

- **Simulation cell:** **11.7 nm × 11.7 nm × 100 nm**; **periodic** in **x** and **y**; **z** uses a fixed lower boundary and a **reflecting** top wall; long **z** avoids boundary interference.
- **Fluids and solid:** **Liquid argon** slab **6 nm** thick (**18,522 atoms**), initialized as **FCC** with **5.8 Å** lattice constant (**~1378 kg m⁻³** at **90 K**). **Platinum** **FCC** with **3.92 Å** lattice constant: **eight** base layers, bottom layer **fixed**, **two** thermostat **heating** layers, remaining layers conduct heat into the fluid.
- **Potentials:** **Lennard-Jones (12–6)** for **Ar–Ar**, **Pt–Pt**, and **Ar–Pt**; **σ_Ar–Pt** from **Lorentz–Berthelot** mixing; **ε_Ar–Pt** scaled by **ξ = 0.5 (hydrophobic)** or **ξ = 2.0 (hydrophilic)** relative to **ε_Ar–Ar** as defined in the paper. **Cutoff** ≈ **4 σ_Ar–Ar**.

### Integration, ensembles, and software

- **Equilibration:** **1 ns** **NVE** with **Langevin** thermostat on the **entire** system at **90 K**; **1 ns** with Langevin **removed from liquid argon** only.
- **Heating:** Heating layer temperature ramped **90 K → 230 K** over **0.5 ns** via Langevin to limit thermal shock, then held at **230 K**.
- **Production:** **Time step 5 fs**; **Velocity Verlet**. Simulations run in **LAMMPS**; visualization with **OVITO** (as stated). **N/A** — **NPT** **barostat**; **N/A** — **hydrostatic** **pressure** / **GPa** control (non-**NPT** heating protocol). **N/A** — external **electric** **field**; **N/A** — **replica** **exchange** in the **rare**-**event** **sense** (not used in this LJ model).

## Findings

- **Heat transfer and Leidenfrost:** Compared to flat surfaces, **nano-porous** substrates **improve heat transfer**, **delay Leidenfrost film** formation, and **raise argon temperature at the Leidenfrost point**; **higher void fraction** performs better among the porous designs studied.
- **Wettability ranking:** **BϕSϕ** gives the **best** heat-transfer performance among hybrid layouts; **BϕSpho** is the **least efficient**; **BphoSϕ** is **close to BϕSϕ**. (See *J. Mol. Liq.* **version-of-record** for **experimental** and **grid**-refinement **comparisons**; this page is **LJ**-model-**scoped**.)

## Limitations

Lennard-Jones argon on platinum is a minimalist model: no polar fluids, chemical reactions, or experimental temperature/pressure mapping are included.

## Relevance to group

No Penn State affiliation; included as a **methods / classical MD boiling** reference in the broader corpus.

## Citations and evidence anchors

- DOI: `10.1016/j.molliq.2025.126867` — *Journal of Molecular Liquids*.
