---
id: paper:2015lin-nat-atomistic-understandings
type: paper
title: "Atomistic understandings of reduced graphene oxide as an ultrathin-film nanoporous membrane for separations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:reactive-md
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:water-interfaces
  - keyword:lammps
  - keyword:berendsen-thermostat
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1038/ncomms9335"
year: 2015
authors:
  - "Li-Chiang Lin"
  - "Jeffrey C. Grossman"
venue: "Nature Communications"
pdf_sha256: "109fe6abffb8112f1b1a06f6b4ef006d9bafc069816717be48cc71f5b0f34f17"
pdf_path: "papers/ReaxFF_others/Lin_Grossman_Graphene_separation_Nature_Comm_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015lin-nat-atomistic-understandings -->

## Summary

**Reduced graphene oxide (rGO)** is often discussed as an **ultrathin nanoporous membrane**, but pore creation is tied to how **oxygen** leaves the **graphene oxide (GO)** lattice during **thermal reduction**. Lin and Grossman combine **ReaxFF** simulations in **LAMMPS** to model **GO→rGO** chemistry with explicit **epoxy** and **hydroxyl** functionality, then use **classical** (non-reactive) permeation MD—**DREIDING** with **SPC/E** water and **TIP3P**-style ions—to evaluate **water desalination** and **CO₂/CH₄** separation through representative **rGO** pores. The two-stage workflow links **atomic-scale defect chemistry** to **continuum-like** transport metrics.

## Methods

**MD application — GO→rGO formation (ReaxFF in LAMMPS).** **GO** sheets ~**3.4 nm × 3.2 nm** in-plane with **random epoxy/hydroxyl** decoration are placed in **~15 nm**-tall **3D periodic** cells so **CO\(_2\)** and **H\(_2\)O** desorbates can accumulate along **±z** during reduction. **ReaxFF** structural optimization precedes **thermal reduction**: the cell is **ramped from 10 K** to the target **reduction temperature** at **~6 K/fs**, then **annealed ~400 ps** with a **Berendsen** thermostat (**damping = 100 MD steps**) and temperature-dependent timesteps (**0.1 / 0.08 / 0.05 / 0.05 fs** for **1500 / 2000 / 2500 / 3000 K**, respectively, as listed in *Nature Communications* **Methods**). **By-products** more than **5 nm** away from the sheet along **z** are removed every **200 fs** to mimic vacuum; a **0.175 nm** bond cutoff culls leftover small molecules after reduction.

**Parameter / morphology survey.** **Ten** randomized **GO** samples per **oxygen concentration** (**17 / 25 / 33%**) × **epoxy:hydroxyl ratio** (**2:1, 1:1, 1:2**) combination are reduced at **1500–3000 K**, yielding **360** **rGO** realizations for pore-statistics analysis as stated in the article.

**Permeation MD (downstream classical FF).** **Desalination** and **CO\(_2\)/CH\(_4\)** permeation use **hybrid setups** described in **Methods**: the **rGO** membrane is still treated with **ReaxFF**, while **water** uses **SPC/E**, **ions** use **Joung–Cheatham**-family parameters, and **nonbonded rGO–water** interactions use **Lennard-Jones + Coulomb** with **DREIDING** LJ parameters for **C/O/H** and **Lorentz–Berthelot** mixing—see the membrane/piston box description in the paper for geometry and driving-force details. **Replica exchange / applied electric-field MD:** **N/A —** not reported for these permeation workflows.

**Ensembles and pressure.** **GO→rGO reduction:** **constant-volume** cells with **Berendsen** thermostat (**damping = 100 MD steps**) during heating/annealing; **NPT** barostat is **not** reported for this stage. **Permeation:** a **piston**-style **membrane** cell with **pressure** control is described in *Nature Communications* **Methods**—read the article for **GPa**-level targets and box geometry rather than transcribing numbers from this note alone.

## Findings

**Pore dimensions** correlate with **total oxygen**, the **epoxy/hydroxyl** balance, and the **reduction temperature**: higher **oxygen** load and **epoxy-rich** starting points tend to enable more **carbon removal** and **larger pores** under the simulated annealing windows. For transport, certain **rGO** realizations exhibit **high permeance** with **selectivity** favorable for **desalination** or **gas separation** in the classical MD tests; absolute numbers inherit **force-field** and **pore statistics** uncertainty, which the authors acknowledge when contrasting qualitative trends versus quantitative engineering predictions. The two-stage workflow—**ReaxFF** for **pore genesis**, **classical** **FF** for **permeation**—mirrors how **membrane** design often separates **chemical** defect formation from **hydraulic** performance estimation.

## Limitations

Authors note **qualitative** structural predictions owing to **ReaxFF** accuracy and **timescale** limits; separation numbers depend on **classical** water/ion models. **Membrane** engineers should treat permeation metrics as **illustrative** unless validated against **experimental** **pore** distributions for specific **rGO** processing routes.

## Relevance to group

Demonstrates **ReaxFF**-based **GO→rGO** modeling coupled to downstream **membrane** performance estimates.

## Citations and evidence anchors

DOI `10.1038/ncomms9335`.

## Related topics

- [[reaxff-family]]
- [[theme-water-silica-geo]]
