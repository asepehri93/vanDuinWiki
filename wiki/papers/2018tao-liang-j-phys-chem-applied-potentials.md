---
id: paper:2018tao-liang-j-phys-chem-applied-potentials
type: paper
title: Applied Potentials in Variable-Charge Reactive Force Fields for Electrochemical
  Systems
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:batteries-electrochemistry
- domain:catalysis-surfaces
- domain:methods-software
- method:reactive-md-generic
- task:method-development
- scale:atomistic
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpca.7b06064
year: 2018
authors:
- Tao Liang
- Andrew C. Antony
- Sneha A. Akhade
- Michael J. Janik
- Susan B. Sinnott
venue: J. Phys. Chem. A
pdf_sha256: 569e2b7af7a89199373ea7a177827802b6180d0013ee77060800d1a692dcdbec
pdf_path: papers/Others/2018_Liang_JPCA.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018tao-liang-j-phys-chem-applied-potentials -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **J. Phys. Chem. A** article uses **molecular dynamics** with the **third-generation charge-optimized many-body (COMB3)** potential—a **variable-charge**, **reactive** framework distinct from **ReaxFF**—to treat **Cu electrode / aqueous electrolyte** cells with tunable **OH⁻** and **H⁺** concentrations. **Applied electrochemical bias** is represented by an **electronegativity offset** on **metal** atoms, embedded in COMB3’s **charge equilibration** scheme; the study compare this **offset** approach with **QEq-style** equilibration and propose a **charge-neutral electrolyte** protocol suited to **electrochemical** boundary conditions. The paper is **Penn State**–authored (**Liang**, **Sinnott**, **Janik**, **Akhade**, **Antony**) and is a **methods** reference for **biased metal–water interfaces** adjacent to **ReaxFF / eReaxFF** electrochemistry workflows.

## Methods

### Potential model

**COMB3** (third-generation **charge-optimized many-body** potential) supplies reactive bond-order physics with **variable** atomic charges via **charge equilibration** (distinct from **ReaxFF** but aimed at the same class of multicomponent electrochemical interfaces). **Coulomb** interactions use COMB3’s built-in treatment (the article cites a **11 Å** cutoff for Wolf summation in the COMB3 electrochemical setup). **Externally applied voltages** enter as **electronegativity offsets** on electrode atoms inside the variable-charge loop; the manuscript also analyzes how that recipe interacts with **dynamic QEq**-style equilibration and proposes a **charge-neutral electrolyte** variant for biased cells.

### MD application (COMB3 / LAMMPS, two Cu(111) electrodes in water)

- **Engine / code:** **LAMMPS** with **COMB3** forces (as stated in the article’s simulation section).
- **System size & composition:** Two parallel **six-layer Cu(111)** slabs (**1008** Cu atoms per electrode; **168** atoms per layer) bound **2240** water molecules as electrolyte; cell about **90.1 × 31.0 × 30.7 Å** with **~20 Å** vacuum along the surface normal; liquid density set to **1.0 g cm⁻³** (COMB3 bulk-water value per the paper).
- **Boundaries / periodicity:** **Three-dimensional periodic** supercell; **outermost Cu layers** on each electrode (**Cs** and **As** in the paper’s Figure 1 notation) are **fixed**; mobile electrolyte and interior metal atoms evolve in **NVT**.
- **Ensemble:** **NVT** for reported production trajectories.
- **Timestep:** **0.25 fs** integration of Newton’s equations.
- **Duration / stages:** **2000 ps** trajectories for the electrochemical cases summarized in the Results section; properties are **time-averaged over the last 20 ps** (as stated for water dynamics diagnostics).
- **Thermostat:** **Nosé–Hoover** on **Cu** atoms and **Langevin** on **water**, both with **1 ps** damping, holding **300 K** unless otherwise noted for parameter scans.
- **Barostat / pressure:** **N/A — constant-volume NVT**; no **NPT** barostat in the production protocol described for these cells.
- **Temperature:** **300 K** baseline thermostat set point; additional scans with applied potentials use the same thermal control unless the article specifies otherwise for a given figure.
- **Pressure:** **N/A — not pressure-controlled** in the quoted **NVT** production runs.
- **Electric field:** **N/A — no homogeneous external E-field**; instead, **finite inter-electrode voltages** (**0.625, 1.25, 2.5 V** in the cases quoted in the simulation paragraph) are imposed via the **electronegativity-offset** scheme together with COMB3 charge dynamics.
- **Replica / enhanced sampling:** **N/A — not used** (standard time-stepped **MD**).
## Findings

- **Outcomes / mechanisms:** With **standard dynamic QEq** on the full Cu/water cell, COMB3 can accumulate **unphysical net charge** on the electrolyte (the paper reports **~−0.039 e per water** for the zero-bias configuration in Figure 1). The **electronegativity-offset** treatment on electrodes reduces that pathology while still capturing **interfacial charge separation**, **water density profiles**, **dipole response**, and **local electrostatic potential** trends across the gap.
- **Comparisons:** The authors contrast **constant-electrode-charge** literature models with their **variable-charge** implementation and benchmark how well **precalibrated offsets** reproduce target **voltages** for the discrete applied-bias cases they report.
- **Sensitivity / design levers:** **OH⁻ / H⁺** loading in the electrolyte modulates **water dynamics** and **electrochemical** fingerprints in the COMB3 cells; **applied bias** shifts interfacial **charging** and **solvent layering** in the ways summarized in their Results figures.
- **Limitations / outlook (as authored):** The study emphasizes **qualitative** electrochemical fidelity and **voltage precalibration** rather than a full **constant-potential** metal model of the Siepmann–Sprik type; transfer to other **metals**, **electrolytes**, or **potentials** requires revalidation of COMB3 parameters.
- **Corpus honesty:** Numerical diagnostics beyond the simulation paragraph (extended bias sweeps, SI calibration tables) should be checked in **`papers/Others/2018_Liang_JPCA.pdf`**; this page mirrors the **Methods** numbers printed in the **version-of-record** PDF.

## Limitations

- Results are tied to the **COMB3** parameterization and **Cu/water** chemistry; **transfer** to other **metals**, **electrolytes**, or **ReaxFF** implementations is **not automatic**.
- **Classical** treatment of **electrochemical** interfaces omits **explicit electron transfer** chemistry at full **ab initio** fidelity.

## Relevance to group

**Conceptual overlap** with how **variable-charge reactive** models implement **electrode bias**—useful when comparing **COMB3** and **ReaxFF / eReaxFF** routes for **electrified interfaces**. Keep software package versions in mind when reproducing quoted **voltage** calibration behavior.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpca.7b06064` (`papers/Others/2018_Liang_JPCA.pdf`).

## Related topics

- [[reaxff-family]]
