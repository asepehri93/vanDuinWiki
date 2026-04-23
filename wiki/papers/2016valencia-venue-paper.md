---
id: paper:2016valencia-venue-paper
type: paper
title: "Hydrogen Storage in Palladium Hollow Nanoparticles"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - material:metal-surface
  - method:classical-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b07895"
year: 2016
authors:
  - "Felipe J. Valencia"
  - "Rafael I. Gonzalez"
  - "Diego Tramontina"
  - "Jose Rogan"
  - "Juan Alejandro Valdivia"
  - "Miguel Kiwi"
  - "Eduardo M. Bringa"
venue: "J. Phys. Chem. C (2016); corpus PDF is ACS Just Accepted imprint"
pdf_sha256: "f8fbdbff995509daf34b7e39523f42c03fc232b5408a13db8344069cfddb5699"
pdf_path: "papers/ReaxFF_others/Valencia_JPhysChemC_2016_PdH.pdf"
extraction_quality: "good"
group_affiliation: false
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:metallic-systems
---
<!-- id:paper:2016valencia-venue-paper -->

!!! note "Just Accepted PDF"

    The checked-in file is an ACS **Just Accepted** manuscript (web **26 Sep 2016**). ACS boilerplate warns that **copy-editing, formatting, and figure resolution** may still change before the **version of record**.

## Summary

Classical **molecular dynamics** in **LAMMPS** explores **hydrogen uptake** in **palladium hollow nanoparticles (hNPs)** built as **fcc Pd ⟨100⟩** shells with spherical voids. **EAM (Zhou parametrization)** treats **Pd–Pd** mechanics and initial **H loading**, while **gas-phase H\(_2\)** chemistry uses **ReaxFF** (**Senftle** parametrization) because **EAM** alone allows unphysical **H clustering**. **Atomic H** is inserted into the cavity **every 100 fs** to mimic rapid charging. Simulations report **hydride** formation on the **inner wall**, subsequent **H\(_2\)** generation inside the void, rising **intracavity pressure** (up to **~7 GPa** before mechanical failure in the narrative of the abstract), and maximum **H/Pd** ratios of **~1.21** (cavity-only loading) versus **~1.70** when **H** is also supplied to the **outer** surface—about **25% larger** than earlier reports cited in the abstract—followed by **particle rupture** and **H\(_2\) ejection** when loaded beyond those regimes.

## Methods

**1 — MD application (classical + reactive segments).** **Engine:** **LAMMPS**. **Boundary conditions:** **three-dimensional periodic boundaries** on the simulation boxes described in **Methods** (bulk-like embedding of each **hNP**). **Pd skeleton:** **EAM** potential with **Zhou** parameters; hNPs are carved from bulk **fcc Pd ⟨100⟩** with external radii **\(6a_0 \le R_\mathrm{ext} \le 60a_0\)** (**\(a_0 = 3.89\) Å**) and shell thicknesses **\(a_0 \le w \le 6a_0\)** as stated in **Methods**. **Initial relaxation:** alternation of **FIRE** and **conjugate-gradient** minimization. **Thermal ramp:** **0 → 300 K** in steps of **20 K** every **0.2 ns** with a **Nosé–Hoover** thermostat and **1 fs** timestep for the stability survey. **Hydrogen charging:** single **H** atoms added to the cavity **every 100 fs** (kinetic protocol motivated in the article). **H\(_2\) gas treatment:** **ReaxFF** (**Senftle** parameters) replaces **EAM** for **H–H** interactions when **molecular hydrogen** forms, as **EAM** is noted to cluster **H** unphysically in the gas phase. **Ensemble labels for all production segments:** follow the manuscript’s staged protocols (**NVT**-like thermal control is explicit for the **300 K** ramp; subsequent uptake stages are described sequentially in **Methods**—read the **PDF** for any additional ensemble switches not summarized here). **Barostat for charging runs:** **N/A —** not emphasized in the excerpted protocol text reviewed for this page. **Pressure control:** **N/A —** no external **hydrostatic barostat**; **intracavity H\(_2\) pressures** reported in **Results** emerge from inserted **H** loading. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** the study **uses** published **EAM** and **ReaxFF** parameterizations.

**3 — Static QM.** **N/A —** not a DFT paper.

**4 — Experimental comparison.** Stability diagrams are compared against cited **TEM**/**synthesis** literature for **hNP** dimensions (discussed around **Fig. 1**).

## Findings

**Outcomes.** **MD** predicts **three stability classes** for hollow geometries (**stable**, **half-stable**, **collapsed**) versus **\(R_\mathrm{ext}\)** and **\(w\)** when ramped to **300 K**, bracketed against experimental size/thickness claims in the article’s **stability diagram**. **H insertion** first builds a **Pd hydride** layer on the **inner** surface, lowers the uptake rate, and eventually yields **H\(_2\)** gas inside the cavity with **pressures** peaking near **7 GPa** prior to mechanical breakdown (abstract narrative). **Maximum H/Pd** reaches **~1.21** for **inner-only** loading and **~1.70** when **both surfaces** are charged (**25%** higher than prior computational reports quoted in the abstract), beyond which the **hNP** fractures and **ejects** gas.

**Comparisons.** Simulation **stability regions** are mapped against multiple experimental datasets referenced in the **Results** discussion (e.g., **7 nm** and **40 nm** examples).

**Sensitivity / levers.** Response depends strongly on **wall thickness**, **outer radius**, and whether **H** accesses **one or both** surfaces.

**Limitations (authored).** Inner-only insertion is a **computational expedient** versus experimental **external** charging; **classical** models omit **quantum** **H** effects and **electronic** stopping relevant to some beam experiments (**N/A** for this article’s focus).

**Corpus honesty.** This page was drafted from the **Just Accepted** **PDF** at `pdf_path`; prefer the **typeset VOR** for pagination and final figure labels when available.

## Limitations

- **Just Accepted** text may differ slightly from the **issue** PDF.
- **Charging protocol** is idealized (**discrete H insertions**); map numerical **pressure**/**H/Pd** peaks to **figures** in the article before reuse in benchmarks.

## Relevance to group

Adjacent corpus material for **Pd–H** **nanostructures** and **mechanical failure** under **hydride** formation—useful when contrasting **EAM** **metal** models with **ReaxFF** **covalent** gas chemistry in multiphysics workflows.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.6b07895](https://doi.org/10.1021/acs.jpcc.6b07895)
- Primary PDF: `papers/ReaxFF_others/Valencia_JPhysChemC_2016_PdH.pdf`

## Related topics

- [[reaxff-family]]
- Palladium hydrides and hydrogen storage (see primary PDF for quantitative tables)
