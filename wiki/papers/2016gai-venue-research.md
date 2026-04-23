---
id: paper:2016gai-venue-research
type: paper
title: "Atomistic adsorption of oxygen and hydrogen on platinum catalysts by hybrid grand canonical Monte Carlo/reactive molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - method:reaxff
  - method:monte-carlo
  - material:metal-surface
  - task:validation
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b01064"
year: 2016
authors:
  - "Lili Gai"
  - "Yun Kyung Shin"
  - "Muralikrishna Raju"
  - "Adri C. T. van Duin"
  - "Sumathy Raman"
venue: "J. Phys. Chem. C"
pdf_sha256: "9c51c72f55e9e6045c41d4461e819f9a8615a5e21cd1ec876ac962f1bcd3ed26"
pdf_path: "papers/Gai_PtHO_JPC_2016_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2016gai-venue-research -->

## Summary

The study combines **hybrid grand canonical Monte Carlo with reactive MD (GCMC/RMD)** and a **Pt/O/H ReaxFF** to predict **coverage-dependent adsorption** of **oxygen and hydrogen** on **Pt facets**, **reconstructed Pt(110)**, and **Pt nanoparticles** across **pressure–temperature** conditions relevant to **operando catalysis**. The study reports **isotherm-style** behavior, **subsurface/bulk penetration** at aggressive chemical potentials, and **spot validation** of **O binding on Pt(321)** outside the primary training set. Industrial coauthorship (**ExxonMobil**) signals application targeting **reactor-relevant adsorbate structure preparation** for follow-on reaction MD.

## Methods

**MD application (hybrid GCMC/RMD + ReaxFF):** **Grand canonical Monte Carlo** moves insert or delete **O** and **H** under imposed **gas-phase chemical potentials** while **ReaxFF** forces relax **Pt(111)**, **unreconstructed and reconstructed Pt(110)**, and several **Pt nanoparticle** morphologies. **Pressure–composition** style sweeps span roughly **\(10^{-20}\)**–**\(10\)** atm in the abstract’s statement. A **Pt(321)** spot test probes **O** binding on a **kinked** facet **outside** the primary training set. **Boundaries / PBC:** **3D periodic supercells** for extended **Pt** facets and nanoparticle models as in standard **LAMMPS**-style setups (*JPCC* computational section—**N/A — cell vectors not on the short extract**). **Temperature setpoints for GCMC/RMD segments:** **N/A — not on the short corpus extract**; the abstract emphasizes **gas-phase potential** sweeps rather than tabulating **K**-resolved schedules here. **Total trajectory time per chemical-potential point / production-run duration (ps or ns):** **N/A — not on the short corpus extract**; use **`papers/Gai_PtHO_JPC_2016_proof.pdf`** and **SI** for equilibration vs production staging. **Engine, timestep, thermostat/barostat:** **N/A — not on the short corpus extract**; use **`papers/Gai_PtHO_JPC_2016_proof.pdf`** and **SI**.

**Force-field training:** The article reports a **Pt/O/H ReaxFF** and ties **GCMC/RMD** behavior to **training-set** coverage (**QM program, functional/basis, weighting, and optimizer details** are in the **JPCC** computational section—**N/A — not transcribed on this page**).

**Static QM / DFT:** **Validation** against **DFT** and literature **experiment** as cited in the paper; **functional/basis/k-mesh:** **N/A — see article** rather than this summary.

## Findings

- **Adsorption isotherms** map how **O and H** populate **surface, subsurface, and bulk** regions as a function of imposed **gas-phase potential**.
- **Pt(321)** tests indicate **transferable** qualitative performance for **step/kink** sites not explicitly in the training data (as claimed in the abstract narrative).
- Results are cross-compared to **DFT and experiment** where available in the article body.
- The **abstract-level** message is that **hybrid** **GCMC/RMD** can prepare **realistic** **adsorbate** **ensembles** on **complex** **Pt** **morphologies** before **follow-on** **reaction** **MD** that would be too costly if starting from **bare** surfaces.

**O** and **H** fill **surface**, then **subsurface**, then **bulk**-like regions as the imposed potential becomes more oxidizing, so uptake competes with **subsurface** transport. Where **DFT** and **experiment** are cited, the authors argue the **Pt/O/H** parametrization is **adequate** for these coverage models. **Sensitivity** to the **10⁻²⁰–10 atm** pressure window (abstract) moves the dominant **adsorption** branch. **Gas-phase** grand-potential control is **not** a full **electrochemical double layer**; **quantitative isotherms** and final pagination belong in the **journal PDF**, not this note.

## Limitations

- **GCMC/RMD** still inherits **ReaxFF uncertainties** for **oxidized, hydroxylated, and reconstructed** Pt under electrochemical potentials not identical to the gas-phase grand potential used here.
- **Proof PDF** path may differ cosmetically from the final issue layout.
- **Electrochemical** **interfaces** with **explicit** **solvent** and **applied bias** may require **extensions** beyond the **gas-phase** **grand-potential** **protocol** emphasized in the abstract-level summary.
- **Coverage** **isotherms** should be read with the **same** **pressure** **scales** and **reference** **states** used in the **article** to avoid **misinterpreting** **chemical** **potential** **units**.

## Relevance to group

Showcases **time-accelerated sampling + ReaxFF** for **Pt catalysis**, a recurring theme in collaborations between **Penn State** and **industry partners**.

## Citations and evidence anchors

- Abstract and metadata in `papers/Gai_PtHO_JPC_2016_proof.pdf`; **DOI:** `10.1021/acs.jpcc.6b01064`.

## Related topics

- [[reaxff-family]]
