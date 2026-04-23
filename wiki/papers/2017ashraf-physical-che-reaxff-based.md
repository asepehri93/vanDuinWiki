---
id: paper:2017ashraf-physical-che-reaxff-based
type: paper
title: "ReaxFF based molecular dynamics simulations of ignition front propagation in hydrocarbon/oxygen mixtures under high temperature and pressure conditions"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1039/C6CP08164A"
year: 2017
authors:
  - "Chowdhury Ashraf"
  - "Abhishek Jain"
  - "Yuan Xuan"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "ebb660a1d4b680881db4c8b834212de3125f9a7724209c0645b1f70e47deac97"
pdf_path: "papers/Ashraf_PCCP_2016_flame_propagation_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017ashraf-physical-che-reaxff-based -->

## Summary

Continuum combustion models rely on empirical correlations for ignition delay, flame speed, and pollutant formation, yet atomistic simulations with explicit bond rearrangements can stress-test those closures when experimental data at extreme pressures are sparse. Ashraf et al. apply ReaxFF molecular dynamics to estimate ignition-front propagation speeds in supercritical hydrocarbon/oxygen mixtures at 55 MPa with an unburned temperature of 1800 K—thermodynamic conditions chosen in the abstract to accelerate oxidative chemistry so that fronts develop within tractable MD windows. Representative alkyne, alkane, and aromatic fuels are compared under matched states, and the extracted MD front speeds are juxtaposed with continuum reactive-flow solutions computed with consistent thermodynamic assumptions.

## Methods

**Reactive MD (LAMMPS, §3.1).** **ReaxFF CHO-2008** (`papers/Ashraf_PCCP_2016_flame_propagation_online.pdf`) drives **ignition-front** studies in a **12 × 12 × 2000 Å** **3D PBC** cell containing **240 n-C₄H₁₀** and **1560 O₂** molecules (**ϕ = 1** baseline) elongated along **z**—order **10⁴ atoms** once hydrogen counts are included. The **unburned** mixture starts at **T_u = 1800 K** and **55 MPa** to accelerate chemistry. Workflows begin with **conjugate-gradient** minimization, **25 ps** of **NVT** equilibration at **1800 K** using **Δt = 0.25 fs** with **C–O/H–O** reactive terms **disabled**, **Berendsen thermostat** (**100 fs** damping), then **NVE** production at **1800 K** with **Δt = 0.1 fs** once reactions activate. **O–O** bonds at the **z** ends are **stretched** to seed **O radicals** while keeping them **≥ 2.5 Å** from neighbors. The quoted protocol is **constant-volume** (**NVT** then **NVE**; **no NPT**); **electric fields** and **replica / enhanced sampling** are **not** used.

**Force-field training:** **N/A — applies CHO-2008** without new fitting in this article.

**Continuum benchmark (§2.2).** **NGA** integrates **Navier–Stokes** plus **species/energy** transport with **CaltechMech** augmented by **JetSurf 2.0** **n-butane** chemistry, invoking an **ideal-gas EOS** after a **compressibility-factor** argument at the stated **reduced** **P, T**.

## Findings

**ReaxFF** trajectories reproduce the qualitative **reactivity ordering** among **alkyne / alkane / aromatic** fuels studied, matching broad **ignition propensity** trends seen **experimentally** in the combustion literature referenced by the authors. **Ignition-front speed** depends strongly on **equivalence ratio**, analogous to **laminar flame speed** sensitivities but evaluated at **55 MPa**/**1800 K**. **Compared** to **Navier–Stokes** solutions with matched **thermochemistry**, the **continuum** solver tracks the **MD** trends and lands near the **tabulated** comparison margins, supporting **ReaxFF** as a **qualitative mechanistic** probe while acknowledging **uncertainty** in **quantitative** rates. **Sensitivity** to **ϕ** mirrors classical flame-speed behavior but at **supercritical** conditions chosen for computational tractability. **Limitations:** the protocol is a **computational convenience**, **not** a direct map to atmospheric flames; **future work** should treat agreement as diagnostic rather than as universal calibration for engineering burners.

## Limitations

The supercritical protocol is a computational convenience and does not map directly to atmospheric flames; extrapolation requires separate validation. ReaxFF omits electronically excited states and non-Born–Oppenheimer channels that may matter for minor species and emissions.

Continuum comparisons inherit uncertainties in transport models and numerical stiffness at 55 MPa that are independent of the force field; readers should treat agreement as diagnostic rather than as a universal flame-speed calibration for engineering burners.

Ignition-front diagnostics in the article tie spatially resolved heat-release or species-gradient measures to an effective front speed; reproduce those definitions carefully and consistently before comparing to external flame-speed databases.

## Relevance to group

Penn State **van Duin**-group **ReaxFF combustion** application paper extending flame/ignition front concepts.

## Citations and evidence anchors

- DOI: `10.1039/C6CP08164A`.

## Related topics

- [[reaxff-family]]
