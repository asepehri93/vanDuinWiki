---
id: paper:2022kritikos-combustion-a-reactive-molecular
type: paper
title: "A reactive molecular dynamics study of the effects of an electric field on n-dodecane combustion"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:combustion
  - keyword:reactive-md
  - keyword:charge-equilibration
  - keyword:neb
  - keyword:lammps
source_refs: []
doi: "10.1016/j.combustflame.2022.112238"
year: 2022
authors:
  - "Efstratios Kritikos"
  - "Aditya Lele"
  - "Adri C.T. van Duin"
  - "Andrea Giusti"
venue: "Combust. Flame"
pdf_sha256: "a7358f2aa22da93c28672520c33037a6fc3edebd20c587b95d306862f9955c12"
pdf_path: "papers/Kritikos_Efield_CombFlame_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022kritikos-combustion-a-reactive-molecular -->

## Summary

**ReaxFF** combustion simulations of **n-dodecane** include **external electrostatic fields** using a **local charge-equilibration** treatment that permits **charge transfer** until **orbital overlap** limits and captures **field-induced polarization**. Isolated **n-dodecane** charges under field are first compared to **DFT**. Reactive boxes then scan **temperature** and **density** with varying **E-field** strength. **Arrhenius-like** parameters for selected channels are probed via **NEB** on **minimum-energy paths** and collision-frequency arguments. **Polarization** from close contacts remains **weak** unless **strong** external fields are applied. **Fuel** consumption slows under **strong** fields; **weak** fields show **no clear** monotonic trend. **O₂** consumption can **rise** with strong fields at **high T and ρ**, but **decreases** when **T** and **ρ** drop. **NEB** finds **activation-energy** shifts up to about **2.3 kcal mol⁻¹** for **oxygen-containing** reactions vs. field strength. **Oxygen** chemistry is rate-controlling under field because it couples directly to oxidation and indirectly modulates **fuel pyrolysis**.

## Methods

### A — ReaxFF + electrostatics (field response)

- **Lineage:** **ReaxFF** combustion parameterization with **charge equilibration** extended so external **E-fields** polarize molecules with **overlap-limited** charge transfer (local QEq-style response as described in *Combust. Flame*).

### B — Reactive MD (combustion under field)

- **Engine:** LAMMPS ReaxFF reactive boxes for **n-dodecane** oxidation; scan **temperature** **T**, mass **density** **ρ**, and **electric field** magnitude/orientation per article.
- **Species / kinetics:** Time series for **fuel** and **O\(_2\)** consumption; **Arrhenius**-style interpretation of selected channels.
- **Collision / energy diagnostics:** Kinetic-energy partitioning and **collision frequency** analyses as stated in Methods.

### C — Quantum chemistry

- **DFT** validation of **charges** and **polarization** for **isolated n-dodecane** in an applied field vs ReaxFF.

### D — Nudged elastic band (NEB)

- **NEB** on **minimum-energy paths** for **oxygen-containing** elementary reactions; reported **activation-energy** shifts up to ~**2.3 kcal mol⁻¹** with field strength.

**Reactive MD (combustion box):** **Engine: LAMMPS**; **3D** **PBC** **reacting** **mixtures** of **n-dodecane** and **O₂** (**atom** **counts** and **stoichiometry** in the **PDF**); **NVT** or **NVE** (see **article**) with **Nose–Hoover**-type **thermostat** for **hot** **combustion** **temperatures**; **~0.1–0.25 fs** **timestep** (typical **ReaxFF**; **PDF**); **ps** **production**; **barostat** **N/A** if **fixed** **volume**; **mass** **density** **ρ** **sweeps** and **N/A** for **isotropic** **hydrostatic** **pressure** **as** an **independent** **thermodynamic** **control** in the same sense as **NPT** **(the** **article** **uses** **(T, ρ)** **state** **points**); **externally** **applied** **electrostatic** **field** **E** (strength **sweeps** in *Combust. Flame*); **N/A** **metadynamics**; **NEB** is a **separate** **static** **path** **refinement**, not **on-the-fly** **replica** **exchange**.

## Findings

- Need **strong** fields to materially alter kinetics; otherwise polarization remains minor.
- **n-Dodecane** consumption **decreases** under **strong** fields.
- **O₂** response to field **flips sign** between **high** and **low** **T/ρ** conditions.
- **NEB:** up to **~2.3 kcal mol⁻¹** barrier shifts for **O-bearing** elementary steps.
- **O₂** dynamics gate overall reactivity under **E-field**.
- The authors highlight that **weak** fields leave **polarization** small unless **close contacts** or **high** external **E** are present, so **flame-relevant** field strengths remain a practical limiting case for observable kinetic shifts. **Comparisons / sensitivity: versus** **DFT** for **isolated** **molecule** **charges**; **T** and **ρ** **sweeps** with **E-field**; **NEB** **barrier** **shifts** **(≤~2.3** **kcal/mol**). **Limitations** (turbulent **flames**, **practical** **E**): see **authored** **discussion**. **Corpus / PDF:** use **version-of-record** for **field** **magnitudes** and **reaction** **network** **IDs**.

## Limitations

Field strengths required for strong effects may exceed practical combustion devices; transferability to turbulent flames is not claimed. The **NEB** subset and **Arrhenius** diagnostics emphasize **elementary** channels that may not isolate **coupled** **turbulence–chemistry** interactions present in **engines**; readers should treat **field** effects as **proof-of-principle** for **ReaxFF** **electrostatic** extensions rather than **device**-ready kinetics without further validation. **Species** **budgets** should be read against the **equation-of-state** and **grid** definitions in the **full** **article** when mapping to **reduced** **chemistry** **models**.

## Relevance to group

Demonstrates **ReaxFF + field + QEq**-style electrostatics for **hydrocarbon oxidation** with **van Duin** parametrization lineage.

## Citations and evidence anchors

- DOI: [10.1016/j.combustflame.2022.112238](https://doi.org/10.1016/j.combustflame.2022.112238)

## Related topics

- [[reaxff-family]]
