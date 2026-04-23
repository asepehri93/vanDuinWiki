---
id: paper:2012yun-kyung-shin-j-phys-chem-development-validation
type: paper
title: "Development and Validation of a ReaxFF Reactive Force Field for Fe/Al/Ni Alloys: Molecular Dynamics Study of Elastic Constants, Diffusion, and Segregation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - material:alloy-bulk
  - method:reaxff
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp308507x"
year: 2012
authors:
  - "Yun Kyung Shin"
  - "Hyunwook Kwak"
  - "Chenyu Zou"
  - "Alex V. Vasenkov"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. A 2012, 116, 12163–12174"
pdf_sha256: "ebcbf5fb6790677f20d471f9fae766ef65284e359d1b18578f1d0310d0cb274a"
pdf_path: "papers/Shin_FeAlNi_JPCA_2012.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2012yun-kyung-shin-j-phys-chem-development-validation -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

A ReaxFF parameterization for **Fe–Al–Ni** alloys is derived from **QM** data on **bulk** phases, **low-index surface energies**, and **adatom binding** motifs needed to capture both **metallic cohesion** and **surface** chemistry within one reactive framework. The article positions the model as a foundation for subsequent **oxidation** and **mechanics** studies where **bond-order**-based descriptions are required. **Validation MD** computes **temperature-dependent elastic constants** for **FeAl**, **FeNi\(_3\)**, and **Ni\(_3\)Al** from **300–1100 K**, reporting **softening** with **temperature** in line with **experimental** trends for these compounds. **Diffusion** simulations in **compositionally graded** **Al/Ni** layers emphasize **composition-dependent** **Al** mobility, with the abstract highlighting strong variation near **1000 K**. **Surface segregation** is examined in **L1\(_2\)**-ordered **finite clusters** at **2500 K**, where **Al** enrichment patterns differ among **Fe\(_3\)Al**, **FeAl**, and **Ni\(_3\)Al**-type surfaces—**Al** is reported to enrich most strongly on **Fe\(_3\)Al** among the cases summarized—qualitatively consistent with older **experimental** segregation literature cited in the paper.

## Methods


- **Fitting:** Assemble **QM-derived** training sets spanning **bulk** equations of state, **surface** energies, and **adatom** binding for **Fe–Al–Ni** interactions, then optimize **ReaxFF** parameters to reproduce those references within the stated fitting workflow.
- **Elastic constants:** **MD** estimates of **elastic moduli** vs **temperature** for **FeAl**, **FeNi\(_3\)**, and **Ni\(_3\)Al** using the fitted potential, compared against **experiment** where available.
- **Diffusion:** **Compositionally graded** **Al/Ni** geometries with **MD** sampling to extract **Al** diffusivity trends around **1000 K** as composition changes.
- **Segregation:** **L1\(_2\)** **nanoparticle**-like clusters simulated at **2500 K** to accelerate **surface** equilibration within accessible **MD** timescales, with **composition profiles** interpreted relative to **bulk** stoichiometries.

### MD application (validation trajectories)

**Engine / code:** **ReaxFF molecular dynamics**; **N/A —** whether **LAMMPS** vs another integrator is used is not recovered from `normalized/extracts/2012yun-kyung-shin-j-phys-chem-development-validation_p1-2.txt`—verify **`pdf_path`**.

**System size & composition:** **Bulk** alloy supercells for **elastic** constants; **compositionally graded** **Al/Ni** multilayers for **diffusion**; **finite** **L1\(_2\)**-ordered **clusters** for **segregation** (sizes and stoichiometries in **`pdf_path`**).

**Boundaries / periodicity:** **Three-dimensional periodic** **bulk** and **slab**/film models as appropriate to each validation task; cluster segregation models use finite nanoparticle-like geometries with surfaces exposed to vacuum (details in **`pdf_path`**).

**Ensemble / thermostat / timestep / duration:** **N/A —** explicit **NVE**/**NVT**/**NPT** labels, **thermostat** couplings, and **Δt** are not recovered from pages **1–2** of the extract; confirm the actual integrator (**NVT** is a common choice for finite-**T** **ReaxFF** property sampling) in **`pdf_path`**. **Equilibration**/**production** schedules for elasticity, diffusion, and segregation are documented there on **ps**–**ns** horizons consistent with the Introduction’s **nanosecond**-scale **ReaxFF** capability statement.

**Barostat / pressure control:** **N/A —** not stated in the indexed excerpt for the **elastic**/**diffusion** tasks.

**Temperature:** **300–1100 K** elastic-constant sweeps; **~1000 K** highlighted for **Al** diffusivity contrasts in graded layers; **2500 K** segregation runs in **L1\(_2\)** clusters (abstract-level summary).

**Pressure / stress:** **Elastic** moduli (**stress**–**strain**-derived) reported vs **temperature**; **N/A —** externally imposed **hydrostatic pressure** protocols are not recovered from the excerpt.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not indicated in the excerpt.

### Force-field training (Fe–Al–Ni ReaxFF)

**Parent FF / elements:** New **ReaxFF** parametrization for **Fe–Al–Ni** binaries.

**QM reference:** **QM** training data spanning **bulk** phases, **(100)/(110)/(111)** **surface energies**, and **adatom** binding motifs (abstract).

**Training set / reference data:** Combined **bulk** + **surface** + **adatom** sets enumerated in **`pdf_path`**.

**Optimization:** **ReaxFF** parameter optimization to the **QM** training data (optimizer and weighting in **`pdf_path`**).

**Reference data used:** **QM** references above; **MD** validation compares to **experiment** for **elastic** trends and cites older **segregation** **experiments** for qualitative agreement.

## Findings

**Outcomes / mechanisms:** A single **ReaxFF** description supports **elastic** moduli vs **temperature**, **Al**/**Ni** **diffusion** trends in **graded** **Al/Ni** layers, and **surface segregation** patterns in **L1\(_2\)**-ordered **clusters**.

**Comparisons:** **Elastic** moduli track **experimental** softening for **FeAl**, **FeNi\(_3\)**, and **Ni\(_3\)Al**; **segregation** results are compared qualitatively to older **experimental** literature cited in the paper.

**Sensitivity / design levers:** **Temperature** (notably **~1000 K** for diffusion contrasts and **2500 K** for accelerated segregation) and **composition** (bulk vs trace **Al**/**Ni** regions) strongly modulate observables.

**Limitations / outlook:** High segregation **temperature** and finite clusters are modeling expedients for accessible **MD** timescales; quantitative transfer to all experimental conditions may require larger cells and longer runs.

**Corpus / KB honesty:** Grounded in **`pdf_path`** and `normalized/extracts/2012yun-kyung-shin-j-phys-chem-development-validation_p1-2.txt` (abstract-heavy); numerical tables live in **J. Phys. Chem. A** **2012**, **116**, **12163–12174**.

## Limitations

- High segregation temperature and simplified geometries are modeling choices to access kinetics within MD timescales; direct quantitative match to all experimental conditions may require larger models and longer runs.

## Relevance to group

Canonical **metallic alloy ReaxFF** development paper used as a foundation for subsequent oxidation and materials mechanics studies.

## Citations and evidence anchors

- DOI: [10.1021/jp308507x](https://doi.org/10.1021/jp308507x)
- Abstract: `normalized/extracts/2012yun-kyung-shin-j-phys-chem-development-validation_p1-2.txt`

## Related topics

- [[reaxff-family]]
- ReaxFF for metals and alloys (Fe–Al–Ni)
- Surface segregation and diffusion in alloys
