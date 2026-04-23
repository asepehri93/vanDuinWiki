---
id: paper:2018wang-journal-of-n-new-transferable
type: paper
title: A new transferable interatomic potential for molecular dynamics simulations
  of borosilicate glasses
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:water-silica-geo
- material:silicate-glass
- method:classical-md
- scale:atomistic
- task:validation
paper_keywords:
- keyword:classical-ff
- keyword:lammps
- keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: 10.1016/j.jnoncrysol.2018.04.063
year: 2018
authors:
- Mengyi Wang
- N.M. Anoop Krishnan
- Bu Wang
- Morten M. Smedskjaer
- John C. Mauro
- Mathieu Bauchy
venue: J. Non-Cryst. Solids
pdf_sha256: aed458b2d7bfbcb537b8163e4009e239e30e16dbb1a9949c278a860f14a7d83d
pdf_path: papers/ReaxFF_others/Wang_Mauro_Bauchy_Borosilicate_pairpotential.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018wang-journal-of-n-new-transferable -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the borosilicate potential paper identified by `doi`, `title`, and `pdf_path`.

## Summary

Borosilicate glasses are technologically important for display panels, laboratory glassware, and nuclear waste immobilization, but atomistic modeling requires potentials that remain transferable across boron-rich and silica-rich compositions while reproducing boron coordination (trigonal BO\(_3\) versus tetrahedral BO\(_4\)), mass density, medium-range order, and transport-related properties such as shear viscosity. This article introduces a fixed-parameter empirical interatomic potential intended to span silicate-to-borate chemistries without composition-dependent refitting of energy parameters. The authors validate the model using LAMMPS molecular dynamics across a series of glass compositions, comparing simulated structural and mechanical properties to experimental trends and to the needs of industrial and nuclear-glass design workflows.

Prior **classical** potentials for **borosilicates** often struggled because **boron** speciation is **composition-** and **thermal-history** dependent: **network modifiers** can convert **BO\(_3\)** to **BO\(_4\)** or create **non-bridging oxygens** on **silicon**, shifting **ring** statistics and **viscosity** in ways that are difficult to capture with **composition-specific** refits. The authors position their model as a **single** global parameter set that still tracks these **crossovers** across a broad **composition** grid.

## Methods

### Empirical potential (non-reactive classical MD)

The authors introduce a **two-body Buckingham + fixed partial charge** form with a **single global parameter set** spanning **borosilicate** compositions from **borate-rich** to **silicate-rich** end members (pair parameters tabulated in the article; **Buckingham catastrophe** safeguards discussed where needed). This is a **fixed-bond-topology** classical model (not **ReaxFF**): it targets **composition transferability** without composition-dependent charge refits of the kind criticized for earlier borosilicate potentials.

### MD application (**LAMMPS**, melt–quench)

Simulations use **LAMMPS** with **11 Å** cutoffs for both **short-range** and **Coulomb** interactions and **PPPM** electrostatics (**accuracy ~10⁻⁵** as stated). The integration timestep is **1.0 fs**. **~3000** atoms are placed randomly in a **cubic** cell without overlaps, **melted** at **3000 K** for **10 ps** in **NVT** followed by **100 ps** at **zero pressure** in **NPT**, then **linearly cooled** to **300 K** at **1 K/ps** under **NPT**. Each glass is **relaxed** at **300 K**, **zero pressure**, for **100 ps**, followed by **100 ps NVT** production from which **100** snapshots spaced **1 ps** apart are averaged. **Exploding** high-temperature **NPT** trials trigger an alternate path: **100 ps NVT** melt at **3000 K**, **NVT** cool to **300 K**, then restart the standard melt–quench. **Glassy-state** **RDFs**, **coordination**, **density**, and **Green–Kubo** **viscosity** use those trajectories. **Boundaries / periodicity:** all melt–quench and production segments use **three-dimensional periodic boundary conditions** (**PBC**) on the **cubic** simulation cell, as standard for bulk glass **MD** in **LAMMPS**.

- **Thermostat / barostat brands:** **N/A — not extracted** into plain text by the **pypdf** pass used for curation; the **J. Non-Cryst. Solids** **PDF** (`papers/ReaxFF_others/Wang_Mauro_Bauchy_Borosilicate_pairpotential.pdf`) should be consulted for any explicit integrator or **thermostat** names beyond the **NVT**/**NPT** staging above.

- **Electric field / metadynamics:** **N/A — not used** (bulk melt–quench **MD** only).

### Observables

**BO\(_3\)/BO\(_4\)** fractions, **mass density**, **pair** and **ring** statistics, and **shear viscosity** from **equilibrium** **MD** (**stress autocorrelation** / **Green–Kubo** protocol per the article) are compared to **experimental** benchmarks from **Smedskjaer & Mauro** datasets and related literature compositions (**Table 1** naming such as **75B … 0B** in the **PDF**).
## Findings

Across the benchmarked borosilicate set, the potential reproduces compositional trends in boron speciation, density, short- and medium-range structure, and viscosity in line with the experimental and simulation targets discussed in the paper. The work supports using a single transferable parameterization for structure–property exploration in complex borosilicate formulations, subject to the usual caveats of classical fixed-bond-order models.

**Practical takeaway.** For **nuclear waste** **glass** design workflows, having **viscosity** and **speciation** trends tracked together across **modifier** content is often more useful than reproducing a single **end-member** silicate perfectly; the paper’s validation emphasizes **composition** sweeps rather than a single benchmark composition.

## Limitations

The potential does not describe bond-making and bond-breaking chemistry; extrapolation outside the fitted composition grid or to extreme thermal histories should be checked case by case. Oxide and alkali diffusion in highly modified glasses may need additional validation.

## Related topics

- [[theme-oxides-silica-ceramics]]
