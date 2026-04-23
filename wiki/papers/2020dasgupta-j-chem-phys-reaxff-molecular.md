---
id: paper:2020dasgupta-j-chem-phys-reaxff-molecular
type: paper
title: "ReaxFF molecular dynamics simulations of electrolyte–water systems at supercritical temperature"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1063/5.0006676"
year: 2020
authors:
  - "Nabankur Dasgupta"
  - "Yun Kyung Shin"
  - "Mark V. Fedkin"
  - "Adri van Duin"
venue: "J. Chem. Phys."
pdf_sha256: "e464e448c0f0cdc5e44b3eaee1f70e046a66f70af54d0dbfbb82ce7bd5c57578"
pdf_path: "papers/Dasgupta_JCP_2020_supercritical_electrolyte.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020dasgupta-j-chem-phys-reaxff-molecular -->

!!! note "Corpus note"

    A galley/author-proof sibling is [[2020dasgupta-venue-total-number]]; prefer the version-of-record PDF for pagination when both are present. See `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md` for non-primary PDF roles.

**ReaxFF MD** of **alkali chloride** pairs in **water** at **700 K** spans multiple **densities** to map **RDFs/ADFs**, **ion diffusion**, **H-bond residence times**, **Voronoi voids**, and **ion clustering** under supercritical conditions.

## Summary

Supercritical aqueous electrolytes exhibit **void-rich** morphologies and altered **dielectric screening** that change **ion pairing** and **transport**. The paper reports **ReaxFF** trajectories for **LiCl, NaCl, KCl, RbCl, CsCl** in **periodic** cells with **water density** swept from **liquid-like** to **vapor-like** at **700 K**, mapping how **void** topology and **ion** **clustering** **track** **M⁺** **identity** and ρ. **Coordination** **stats**, **angular** **distributions**, **H-bond** **residence** **times**, and **self-diffusion** are reported relative to that grid; consult the **J. Chem. Phys.** **article** and any **SI** for **authoritative** **tables**.

## Methods

- **Engine / integrator:** **ReaxFF** **molecular dynamics** with **velocity Verlet** integration in the **J. Chem. Phys.** implementation (see article for code details).
- **System size & composition:** **Alkali chloride** **+** **water** **periodic** **cells** with **atom** counts and **box** **edge** **lengths** **per** **salt** and **ρ** in **Table I** (each **state** **point** at **700 K**).
- **Potential:** **ReaxFF** parameterization for water and alkali/halide interactions as cited in the article (prior ReaxFF water/electrolyte references).
- **Integrator:** **Velocity Verlet** with **timestep 0.25 fs** (as stated).
- **Thermostat:** **Berendsen** thermostat with **100 fs** temperature damping applied to the **entire system** (per Methods text).
- **State points:** **700 K** with tabulated **simulation box sizes** for each salt at water densities **ρ = 1.00, 0.70, 0.35, and 0.15 g cm\(^{-3}\)** (Table I in the paper).
- **Duration / production: N/A** for a **single** **unified** **ns** line in the **Methods** **abstract** on this page—**equilibration** and **analysis** **windows** are **given** in the **JCP** **text** and should be **read** there.
- **Analysis:** **RDF/ADF**, **mean-square displacement** for diffusion, **residence-time** distributions for water around ions, **Voronoi polyhedra** void analysis, clustering statistics for salt aggregates.
- **PBC** **3D** **periodic** **electrolyte** **boxes** at each **(salt, \(\rho\), 700 K)** state point. **NVT**-style **thermostatting** via **Berendsen** (see above); **N/A** — **barostat** and **NPT** **control** (constant **pressure**) are **not** the focus of the **stated** **sampling**—**isochoric** **ρ** **grids** at fixed **T**. **N/A** — **hydrostatic** **pressure** **servo** in **production** if **density** is **fixed** **per** **Table I**. **Electric field: N/A**; **replica**/**umbrella: N/A**.

## Findings

- **Coordination** of water around cations rises with **ionic radius** along the alkali series at the studied conditions.
- **Self-diffusion** of cations **increases** as **density decreases**, linked to **larger void volumes** in the fluid.
- **Li\(^+\)** shows the **longest water residence** (highest “retaining” tendency) among ions compared in the residence-time analysis.
- At **low density**, **Na\(^+\)** and **K\(^+\)** can form **salt clusters** as dielectric screening weakens; **voids** and **ion nucleation** dramatically alter transport relative to dense liquid-like states.
- **Sensitivity** is primarily to **ρ** and **M\(^+\)** **identity** at fixed **700 K** in the **sweep** described.

## Limitations

700 K and reduced densities accelerate chemistry and vapor-like behavior beyond ambient battery electrolytes; quantitative agreement with experiment requires careful potential validation.

## Relevance to group

**van Duin-group** **ReaxFF** on **supercritical water + electrolytes**, relevant to **hydrothermal** and **extreme-environment** aqueous chemistry.

## Citations and evidence anchors

- DOI: [10.1063/5.0006676](https://doi.org/10.1063/5.0006676)

## Related topics

- [[reaxff-family]]
