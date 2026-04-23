---
id: paper:2024yalcin-venue-manuscript
type: paper
title: "Atomic level insight into the nucleation of SnSe thin films using a graphene mask in molecular beam epitaxy: ReaxFF molecular dynamics simulations"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:2d-layered
  - method:reaxff
  - task:parameterization
  - task:application
  - material:tmd
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:2d-materials
  - keyword:oxide-surface
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.4c03096"
year: 2024
authors:
  - "Benazir Fazlioglu-Yalcin"
  - "Mengyi Wang"
  - "Nadire Nayir"
  - "Stephanie Law"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "1adcef0a521295dd56cb118a3b622ab3db4e30b3e63f1bb574bd8e1a8505ea76"
pdf_path: "papers/Yalcin_Wang_Nayir_Law_SnSe_MgO_JPC_C_2024_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024yalcin-venue-manuscript -->

ReaxFF reactive MD is used to study selective-area nucleation of SnSe on MgO(001) with graphene masks, mimicking aspects of molecular beam epitaxy (MBE). An Sn/Se/Mg/O/C parameterization is trained against DFT (VASP, PBE, 500 eV cutoff, PAW, Γ-centered k-grids, DFT-D3, 20 Å vacuum) and prior ReaxFF data for Sn–Se phases and Sn/Se adsorption on MgO. The corpus PDF is a publisher galley; when a version-of-record PDF is available locally, prefer it for pagination and figures.

## Summary

The work reports atomistic ReaxFF MD of SnSe nucleation on MgO(001) with perforated graphene masks, motivated by selective-area thin-film growth. The authors extend a Sn/Se/Mg/O/C ReaxFF (building on prior Sn/Se condensed-phase and cluster training), fit Sn–O, Se–O, Sn–Mg, and Se–Mg interactions to DFT adsorption data on MgO, and keep Mg/O from a Na/Ca/Mg/C/O/H parameterization; graphene edge atoms interact only through nonbonded terms with Sn, Se, and Mg. MD uses the AMS platform, orthorhombic cells (about 21 × 63 × 90 Å and 21 × 63 × 120 Å), periodic boundaries, 1–4-layer graphene masks with a central hole (~3.2 Å mask–substrate gap), Sn:Se 1:4 precursor supply, energy minimization, heating to 500 K in NVT, velocity Verlet integration with time steps of 0.25 fs or smaller, total run lengths of 50–1000 ps, and Berendsen thermostats. Two thermostat schemes are compared: a single strict thermostat (100 fs damping) versus a “mixed” scheme (100 fs on the bottom 12 MgO layers, 107 fs on precursors, mask, and the top four substrate layers) to approximate MBE heating from the substrate back side.

## Methods

- **Reactive force field:** ReaxFF bond-order formulation; training extends Chin et al. Sn/Se/Mg/O/C data (heats of formation, equations of state for α-Sn, Pnma SnSe, cubic SnSe, trigonal P3̅m1 SnSe₂, Sn\(_x\)Se\(_y\) clusters) with added VASP-PBE DFT binding energies for Sn and Se on three MgO adsorption sites; optimization of Sn–O, Se–O, Sn–Mg, Se–Mg bonds, off-diagonals, angles, and torsions. Mg/O from Dasgupta et al.; C–C/C–O covalent terms from literature; C–Se, C–Sn, C–Mg treated as nonbonded only so mask edges do not form covalent bonds to Sn, Se, or Mg.
- **DFT reference (training):** VASP, PAW PBE, 500 eV cutoff, 0.1 meV electronic convergence, 0.01 eV/Å force threshold, dipole correction normal to the surface, Gaussian smearing 0.02 eV, DFT-D3, Γ-centered k-mesh equivalent to 4×4×1 for a 1×1 MgO c(0001) cell, 20 Å vacuum.
- **MD protocol:** AMS; cells ~21 × 63 × 90 Å and 21 × 63 × 120 Å; periodic boundaries; graphene masks 1–4 layers with a central hole (24 C atoms removed); Sn:Se 1:4; minimization then NVT at 500 K; velocity Verlet; Δt ≤ 0.25 fs; Berendsen thermostat(s) as above; run lengths 50, 125, 250, and 1000 ps depending on the case.

**1 — MD application (ReaxFF, MBE-mimic).** The authors use the **AMS** **platform** to run **molecular dynamics** (MD) with **ReaxFF**; details match the **MD** bullet list below. **NVT** at **500 K**, **Berendsen** thermostat (**~100** vs **~107 fs** damping in the **split**-substrate case), **velocity** **Verlet**, **Δt** ≤ **0.25 fs**, **PBC** **~21×63×90/120** **Å** cells, **1–4**-layer **graphene** **mask** with a **~3.2** **Å** gap to **MgO**, **Sn:Se 1:4** supply, **heating** to **500 K**, **50–1000 ps** case-dependent runs. **N/A** — no **NPT**/**barostat** or **external** **E-field** in the summarized protocol. **N/A** — no **metadynamics** or **replica** methods in the summary here.

**2 — Force-field training** — the three bullet lists in **Methods** (ReaxFF construction + VASP **PBE+DFT-D3** training data). **3 — Static QM** — VASP **PBE** **reaction/adsorption** data for the fit; not a DFT-only application paper.
## Findings

1. A single-layer graphene mask promotes formation of the crystalline P3̅m1 SnSe₂ phase during nucleation relative to scenarios explored in the study.
2. Using multiple thermostats (hot substrate bulk, weak coupling to gas and mask) reduces spurious gas-phase Sn\(_x\)Se\(_y\) clustering and is presented as better mimicking MBE-like conditions than a single thermostat for the same system size and duration.
3. **Mask** thickness (1–4 **graphene** layers) and **precursor** **loading** modulate **SnSe** morphology (see article **figures** / **SI**).

**Comparisons, limitations, and outlook.** The **ReaxFF** **trends** are **intended** as **relative** **kinetic** readouts of **nucleation** **morphology** under **thermostat** **schemes** that **mimic** **MBE**-like **heating**; they **do** **not** replace **continuum** **reactor** **CFD** or **long**-**time** **coarsening** **experiments** without **further** **calibration** (see **`## Limitations`**).
## Limitations

Finite system sizes and short nanosecond-scale trajectories limit direct comparison to experimental coarsening timescales; galley PDF pagination may differ from the journal version.

## Relevance to group

Develops and applies group ReaxFF methodology to 2D materials nucleation on oxide substrates with explicit processing-inspired thermostat design.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.4c03096](https://doi.org/10.1021/acs.jpcc.4c03096)

## Reader notes (navigation)

- Local PDF is a **galley** (`pdf_path` above); prefer VOR PDF for citation-ready pagination when available.
- Related: [[reaxff-family]], [[theme-oxides-silica-ceramics]], [[graphene-nanocarbon]].

## Related topics

- [[reaxff-family]]
