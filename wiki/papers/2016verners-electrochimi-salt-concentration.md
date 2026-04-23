---
id: paper:2016verners-electrochimi-salt-concentration
type: paper
title: "Salt concentration effects on mechanical properties of LiPF6/poly(propylene glycol) diacrylate solid electrolyte: Insights from reactive molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - material:polymer-organic
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.electacta.2016.10.035"
year: 2016
authors:
  - "Osvalds Verners"
  - "Barend J. Thijsse"
  - "Adri C. T. van Duin"
  - "Angelo Simone"
venue: "Electrochimica Acta (2016) 221, 115–123"
pdf_sha256: "7f1380cd0d42545eaacac4b7e57e0bbb07660b5ff32660ee7ef88785a20a3d17"
pdf_path: "papers/Verners_Electrochimica_Acta_2016.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:polymer
  - keyword:lammps
  - keyword:npt-simulation
---
<!-- id:paper:2016verners-electrochimi-salt-concentration -->

## Summary

**Reactive MD (ReaxFF)** study of **mechanical properties** of **LiPF\(_6\)**-doped **poly(propylene glycol) diacrylate (PPGDA)** solid polymer electrolyte motifs aimed at **structural battery** coatings. The work targets how **salt concentration** shifts **stiffness**, **failure** under **multiaxial** loading scenarios, and contrasts **isotropic compression vs expansion** and **shear** responses, including **hydrostatic** failure behavior.

The introduction positions **PPGDA** as a room-temperature-processable coating whose conductivity near **10\(^{-6}\)** S/cm motivates ultrathin conformal layers in structural-battery architectures, and frames reactive MD as a way to probe how **LiPF\(_6\)** loading couples to load-bearing capacity under hydrostatic, expansion, shear, and compression modes.

## Methods

**1 — MD application (ReaxFF in LAMMPS).** **Engine:** **LAMMPS** with **ReaxFF** plus **QEq** charge equilibration in **USER-REAXC**, using the **C/H/P/F/O/S/Li** parameter set previously applied to **battery-related** systems (§2.2). **Boundary conditions:** **three-dimensional periodic** **PPGDA** supercells as built in §2.1. **Structures:** **crosslinked** and **non-crosslinked** **PPGDA** cells built with **Molden** then assembled in **LAMMPS** (§2.1); orthogonal **~520-atom** cells (**~17 Å × ~18 Å** in-plane averages at **300 K**, **1 atm**) doped with **LiPF\(_6\)** at **Li:EO = 1:16** and **1:32** (**EO** = ethylene-oxide atoms in the repeat), with **2×2×2** supercells for finite-size checks (§2.1). **Minimization:** **conjugate-gradient** to **\(10^{-6}\) kcal/mol/Å** max force with quadratic line search (**\(10^{-2}\) Å** max displacement). **Integration:** **Verlet** with **0.25 fs** timestep. **Equilibration:** **NPT** at **300 K**, **1 atm** using **Nosé–Hoover** chains (**five** thermostats) with **100 fs** temperature damping and **250 fs** pressure damping (**anisotropic** stress control as stated). **Follow-on segments:** **NVT** **Nosé–Hoover** equilibration until mean potential-energy drift is **\(\mathcal{O}(1)\) kcal/mol/ns** (§2.2 narrative). **Mechanical tests:** **dynamic tensile stiffness** scans along backbone-orthogonal directions under **NPT** with alternative damping tuples (**100/250**, **25/25**, **25/250 fs**); **strain rates** in **[0.08, 8] ns\(^{-1}\)** for stiffness; **simple shear** failure at **12.5 ns\(^{-1}\)**; **Müller–Plathe** setup for **non-equilibrium shear viscosity** (§2.2). **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** the study **employs** a published **ReaxFF** database; **§3.1** compares selected **bond-dissociation** and **charge** metrics against **DFT** rather than refitting here.

**3 — Static QM (validation DFT).** **VASP** **PAW** **GGA-PBE** with **DFT-D3(BJ)** dispersion for condensed motifs; **electronic** convergence and **ionic** relaxation criteria, **k**-point (**Monkhorst–Pack**) settings, and **400/520 eV** cutoffs for fixed/variable cell tasks as listed in §2.2. **Atomic charges:** **DDEC** post-processing for comparison to **ReaxFF/QEq** charges.

**4 — Continuum or mesoscale.** **N/A —** atomistic **RMD** focus.

## Findings

**Mechanical trends (abstract + §3).** **Stiffness** can **increase beyond a threshold** **LiPF\(_6\)** concentration, while **failure** behavior depends on **loading path**. **Isotropic expansion** and **shear** show **modest decreases** in **failure strength** and **failure strain** as **salt** loading rises. **Isotropic hydrostatic compression** produces **no bond-dissociation failure up to 10 GPa** in the reported simulations, contrasting with expansion/shear channels.

**Validation / transferability.** **§3.1** documents **ReaxFF** vs **DFT** gaps for **ether dissociation**, **LiPF\(_6\)** dissociation energies, and **PPGDA** **crosslink / monomer** energetics (**Table 1**), plus **PEO** **melting point**, **density**, **viscosity**, and **LiPF\(_6\)/PEO** transport benchmarks (**Tables 2–3**).

**Sensitivity / levers.** **Salt stoichiometry**, **crosslink density**, and **multiaxial** loading direction change which **C–O** **acrylate** bonds break first, linking **microscopic** bond statistics to **macroscopic** **stiffness** and **failure** trends discussed in **§3.4**.

**Limitations (authored).** **Abstract** positions **~10\(^{-6}\) S/cm** room-temperature conductivity as an acceptable trade-off for **ultrathin** **structural-battery** coatings; **ReaxFF** barriers may **underestimate** absolute **failure** stresses relative to **DFT** (**§3.1** discussion).

## Limitations

- **ReaxFF** accuracy for **salt-polymer** chemistries should be checked case-by-case; **§3.1** flags systematic gaps vs **DFT** for some **dissociation** pathways.
- Room-temperature **conductivity** (~10\(^{-6}\) S/cm class in Introduction) is **low**; structural-battery use cases assume architectures tolerating that scale (as discussed in the paper).

## Relevance to group

**van Duin-group** coauthored **ReaxFF** investigation of **polymer electrolyte mechanics**—pairs naturally with other **battery interface** reactive MD notes in the wiki.

## Citations and evidence anchors

- DOI: [10.1016/j.electacta.2016.10.035](https://doi.org/10.1016/j.electacta.2016.10.035)
- Text-aligned pointers: `normalized/extracts/2016verners-electrochimi-salt-concentration_p1-2.txt` (truncated; use PDF for full Methods)

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
