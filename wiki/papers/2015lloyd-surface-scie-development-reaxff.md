---
id: paper:2015lloyd-surface-scie-development-reaxff
type: paper
title: "Development of a ReaxFF potential for Ag/Zn/O and application to Ag deposition on ZnO"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - method:reaxff
  - task:parameterization
  - task:application
  - material:metal-surface
  - material:oxide
  - scale:atomistic
source_refs: []
doi: "10.1016/j.susc.2015.11.009"
year: 2015
authors:
  - "A. Lloyd"
  - "D. Cornil"
  - "A.C.T. van Duin"
  - "D. van Duin"
  - "R. Smith"
  - "S. D. Kenny"
  - "J. Cornil"
  - "D. Beljonne"
venue: "Surface Science 645 (2016) 67–73"
pdf_sha256: "abdd27650d9ba7f3773556390efc78066c5a7656376ecbbe0a54613d65fcb8dc"
pdf_path: "papers/Lloyd_AgZnO_SurfSci2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015lloyd-surface-scie-development-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Lloyd *et al.* derive **Ag–Zn–O** interactions for **ReaxFF** by extending an established **ZnO** parameter set, fitting new terms to **density functional theory (DFT)** data from **SIESTA** for **bulk** references (elemental **silver**, **Ag–Zn** alloy, **silver oxides**) and for **Ag on ZnO** **surface** configurations, including **equations of state**, **binding energies**, and **works of separation**. The reported fits reproduce the DFT bulk benchmarks and track **Ag–ZnO** surface energetics with useful accuracy for the training scope. The work is motivated by **low-emissivity (Low-E)** glazing, where **Ag** films are sputtered onto **ZnO seed layers** but the **Ag/ZnO** junction is mechanically weak (**large lattice mismatch**, order **10%**). The parametrized field is exercised in **reactive MD** using **single-atom Ag deposition** onto **wurtzite ZnO**, comparing **O-terminated polar (0001)** and **nonpolar (1010)** orientations for impact energies from **0.1 eV to 30 eV**, bracketing **magnetron sputtering**-like conditions. Over that campaign, **adsorption is strongest when deposition energies stay at or below ~10 eV**, whereas higher energies favor reflection or subsurface behavior (per the article’s summarized trajectories).

## Methods

### Force-field training

**Parent field / elements:** Starting from the established **ZnO** ReaxFF set, new terms describe **Ag–Zn–O** interactions while retaining the reduced energy expression used for ZnO (bond, van der Waals, shielded Coulomb with **EEM** charges, valence, lone-pair, over/undercoordination terms as in the article’s Eq. (4) narrative). **QM reference:** **SIESTA DFT** on **bulk** crystals (Ag, Ag–Zn alloy, silver oxides) and **Ag-on-ZnO** surface configurations—**equations of state**, **binding energies**, and **works of separation** among the targets described in the abstract and Sec. 2. **Training set:** expanded and distorted lattice configurations plus surface binding motifs referenced to supplementary material in the paper. **Optimization:** ReaxFF parameters adjusted to reproduce those DFT benchmarks (see article and SI for weights/objectives).

### MD application (atomistic dynamics)

**Reactive MD** with the fitted **ReaxFF** field uses the **velocity Verlet** integrator with **Δt = 1 fs** on **wurtzite ZnO** slabs, comparing **O-terminated polar (0001)** and **nonpolar (1010)** surfaces for **single-atom Ag deposition** at **0.1–30 eV** incident energy (motivated by **magnetron sputtering** in the introduction). **Boundaries / cells:** **periodic** replication in **x** and **y** with a **fixed bottom ZnO layer**; supercells are about **22.80 × 26.33 × 30 Å** (**512 atoms**) for **(0001)** and **26.51 × 26.33 × 30 Å** (**640 atoms**) for **(1010)** (*Surface Science* Sec. 2.4). A **Berendsen** thermostat acts on the **second and third double ZnO layers** beneath the impact region. **Barostat / NPT:** **N/A —** constant-volume slab impacts. **Electric field / enhanced sampling:** **N/A**. The article’s deposition subsection does **not** name a specific MD **package**; coupling to standard **ReaxFF** workflows is implicit. **Thermal conditions:** the **Berendsen** coupling is applied to specified **ZnO** layers, but a single numeric **target temperature (K)** for the thermostated region is **not stated** in the Sec. **2.4** excerpt checked here (**N/A** beyond “temperature control” wording in *Surface Science*). **Equilibration / production durations (ps–ns):** **N/A** in that same excerpt beyond the **1 fs** timestep—the paper moves immediately to **Results** without quoting total trajectory lengths in the subsection summarized.

## Findings

The fitted **ReaxFF** reproduces **DFT equations of state** for **Ag**, **Ag–Zn**, and **silver oxide** training crystals and tracks **Ag–ZnO** **binding** and **work of separation** trends versus **DFT** in the authors’ tables. **Deposition MD** indicates that **maximum Ag adsorption** occurs for deposition energies **at or below about 10 eV**, whereas higher energies favor **reflection** or **subsurface** behavior—consistent with the **sputtering**-relevant energy window emphasized in the abstract. **Sensitivity:** outcomes depend on **facet** (**polar (0001)** vs **nonpolar (1010)**) and on incident energy along the **0.1–30 eV** grid. **Comparisons:** the introduction connects the interface science problem to **Low-E** glazing, where **Ag** on **ZnO** seed layers suffers weak adhesion and roughly **11% lattice mismatch** relative to experiment-oriented motivation. **Limitations:** high-energy impacts access **non-equilibrium** chemistry; translating trajectories to industrial **sputtering** requires validation against **experiment** for real terminations, **defects**, and plasma composition.

## Limitations

High-energy impacts access **non-equilibrium** chemistry; validate **sputtering**-like outcomes against **experiment** for each **facet** termination and defect population.

## Relevance to group

**A.C.T. van Duin** and **RxFF Consulting** contributors appear on the author list, reflecting **industry-facing** **ReaxFF** parameterization for **oxide/metal** interfaces.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1016/j.susc.2015.11.009](https://doi.org/10.1016/j.susc.2015.11.009)

## Related topics

- [[reaxff-family]]
