---
id: paper:2020izadi-j-chem-phys-reactive-molecular
type: paper
title: "Reactive molecular dynamics simulation for isotope-exchange reactions in H/D systems: ReaxFFHD development"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:lammps
source_refs: []
doi: "10.1063/5.0008386"
year: 2020
authors:
  - "Mohammad Ebrahim Izadi"
  - "Ali Maghari"
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys. 152, 224111 (2020)"
pdf_sha256: "d4aa72f16f0c435e5ee2b9bec7181b2f94ef562a99dd2affd06797b1818c60ba"
pdf_path: "papers/Izadi_JCP_2020_H_D_exchange.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020izadi-j-chem-phys-reactive-molecular -->

## Summary

The authors develop **ReaxFF_HD**, a **ReaxFF** parameterization aimed at **H/D isotope-exchange** chemistry in **hydrogen plasma** environments. The force field is trained against **QM** data for **bond dissociation**, **angle distortions**, and **exchange reactions** among **triatomic hydrogenic ions** (H₃⁺, D₃⁺, H₂D⁺, D₂H⁺). **Reactive MD** trajectories up to **~1 ns** explore product formation pathways and **isotope partitioning** in mixed **H/D** plasmas. The scientific motivation ties **isotope exchange** in **edge**/**divertor** plasmas to **fuel recycling**, **particle balance**, and **spectroscopic** signatures—where **classical** reactive models must still capture **mass-dependent** rearrangements among light ions (introduction themes; abstract).

## Methods

**2 — Force-field training (ReaxFF\(_\mathrm{HD}\)).** A **ReaxFF** description (**ReaxFF\(_\mathrm{HD}\)**) is **parameterized** against a **QM training set** covering **bond dissociation**, **angle distortion**, and **an exchange reaction** for the **triatomic ions** H\(_3^+\), D\(_3^+\), H\(_2\)D\(^+\), and D\(_2\)H\(^+\) relevant to **H/D** **plasma** media (per abstract; full fit scope and any **reoptimization** **software** in the **J. Chem. Phys.** / **SI**). **QM** serves as the **reference** for **energies** and **structures** in that training. **Reference data for validation:** the article compares the fitted **ReaxFF\(_\mathrm{HD}\)** to the same class of **QM** data for the triatomic reaction network.

**1 — MD application (production RMD).** **Reactive MD** (ReaxFF\(_\mathrm{HD}\)) is run on **various** **H/D** **mixtures**; the abstract reports **analysis of reactions** over **~1 ns** trajectories. **N/A —** **code** (typically **LAMMPS**-class in this line of work), **PBC** setup, **ensemble** (NVT vs NVE), **timestep**, **thermostat**, and **box** **composition/number of particles** are **not** in the p1–2 **extract** here—confirm in the full **PDF** and **SI**. **Target temperature (K):** use the value(s) in the **J. Chem. Phys.** **article** and **SI**; not copied from the short **extract** to this page. **Barostat / NPT / pressure:** **N/A** if simulations are constant-volume **plasma** boxes as typically used—verify in the article. **External electric field:** **N/A —** not the focus in the extract. **Enhanced sampling:** **N/A —** not mentioned in the abstract; standard **BOMD**-style RMD is implied for the **1 ns** **window**.

**3 — Static QM / DFT-only (as a standalone report).** **N/A** as the *published* result **thread**; **DFT**/**QM** data enter as **training** and **validation** for **ReaxFF**, not as the production dynamics method.

## Findings

**Outcomes and mechanisms.** The fitted **ReaxFF\(_\mathrm{HD}\)** is reported to model **isotope exchange** of the **triatomic** ions and to show **good transferability** to related reactions in the same **H/D** systems. Over **~1 ns** RMD, **H\(_2\)**, **D\(_2\)**, and **HD** appear as **intermediates** that **undergo further reactions** so that **triatomic ions** are among the most **favorable** **products** in the simulated **hydrogen** **plasma** conditions (abstract). **Deuterium** is **enriched** in some products, tied to **lower** **zero-point** energy of **D**-rich species—i.e. **isotope** **effects** carried in the **fitted** **surface** (not new quantum dynamics beyond ReaxFF).

**Comparisons and sensitivity.** The work positions **H\(_3^+\)-family** **chemistry** as central in **weakly ionized** **H** plasmas where these ions are **abundant** and mediate **fast** **H/D** **scrambling**; quantitative **kinetic** and **branching** numbers should be taken from **article** **figures**/**tables** rather than this note.

**Limitations / outlook.** **Nonadiabatic** **plasma** **physics** and full **kinetics** of the discharge are **outside** a classical **ReaxFF** RMD model; the **validity** **region** is bounded by the **training** **chemistry** (stated in the **Discussion**).

## Limitations

Plasma chemistry is vast; the model’s domain of validity is bounded by the **training set** composition and **nonadiabatic** phenomena omitted from classical ReaxFF dynamics.

## Relevance to group

A clear **ReaxFF parameterization** paper from the **van Duin** line for **isotopic** reactive environments—useful for benchmarking **light-element** reactive training practices.

## Citations and evidence anchors

- DOI: [10.1063/5.0008386](https://doi.org/10.1063/5.0008386)

## Related topics

- [[reaxff-family]]
- [[reaxff-parameterization-workflow]]
