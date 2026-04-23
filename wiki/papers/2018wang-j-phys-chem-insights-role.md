---
id: paper:2018wang-j-phys-chem-insights-role
type: paper
title: Insights into the Role of H2O in the Carbonation of CaO Nanoparticle with CO2
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:oxides-ceramics
- domain:reactive-md
- material:oxide
- method:reaxff
- scale:atomistic
- task:experiment-integrated
paper_keywords:
- keyword:oxide-surface
- keyword:reaxff-application
- keyword:validation-experiment
- keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpcc.8b05517
year: 2018
authors:
- Nana Wang
- Yuchuan Feng
- Xin Guo
- Adri C. T. van Duin
venue: J. Phys. Chem. C
pdf_sha256: c965ae78996532f7560f71f6e2dd6ba5f744f85fe48af92e064de5d87ccd4289
pdf_path: papers/Wang_CO2_H2O_CaO_NP_JPCC_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018wang-j-phys-chem-insights-role -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the JPCC article identified by `doi`, `title`, and `pdf_path`.

## Summary

**C/H/O/Ca** (and **Al** where applicable) **ReaxFF** **RxMD** simulates **CO\(_2\)** and **H\(_2\)O** co-adsorption and reaction on **nanoparticulate CaO**, distinguishing a **fast surface/kinetic** carbonation stage from a **slow diffusion-limited** stage in **calcium looping**. Results are cross-checked with **TGA** on **sol–gel** CaO (**~31 nm** crystallite size, **~11.85 m\(^2\)/g** surface area). **Steam** is found to **strongly enhance** the **diffusion-controlled** stage with **little** change to the initial kinetic stage, traced to faster **ion/gas transport**, thicker **carbonate** product layers, and **proton/OH**-mediated disruption of the CaO interior. The motivation connects to **CO\(_2\)** capture cycles where **carbonate** product layers can choke **gas** access: if **steam** reshapes **transport** without accelerating the **initial** surface reaction, **operating** strategies can target **humidity** to extend **utilization** of **CaO** **sorbent** particles.

## Methods

### Reactive MD (**ReaxFF** in **LAMMPS**)

**Six-processor** parallel jobs use the **ReaxFF** implementation in **LAMMPS** to follow **CO\(_2\)/H\(_2\)O** adsorption and reaction on **spherical CaO** nanoparticles (**~1.8 nm** radius) centered in an **88 × 88 × 88 Å** box with **Packmol**-generated gas placement. A representative setup contains **3591–2691** atoms (as printed in the article) with **300 CO\(_2\)** molecules and **H\(_2\)O:CO\(_2\) = 1:1**; **in-plane PBC** apply to the full supercell. Simulations use the **canonical (NVT)** ensemble with a **Berendsen** thermostat (**100 fs** coupling), **0.25 fs** timestep, **4 ns** total trajectory length, and output every **1000** steps; additional runs scan **400–1000 K** to probe temperature effects on carbonation.

### Analysis and experiment

Reactive **C/H/O/Ca/Al** **ReaxFF** (parameterization cited in the article) drives **Ca–O–C** chemistry; **carbonation degree** vs radius, **pair correlations**, and **diffusive flux** diagnostics follow §3 of the **JPCC** paper. **TGA** uses **~5 mg** **sol–gel** CaO after **calcination** (**900 °C**, **N\(_2\)**, **10 min**) and **650 °C** carbonation with **15 vol% CO\(_2\)** (**60 min**), with **steam** levels per **Table 1** to separate **kinetic** vs **diffusion-limited** stages.

- **Barostat / pressure control during adsorption MD:** **N/A — NVT** runs (no **NPT** barostat in the quoted gas-on-nanoparticle protocol).
- **Replica / metadynamics:** **N/A — not used**.
- **External homogeneous electric field:** **N/A — not used** (electrochemical driving forces enter through chemistry and composition, not an applied **E-field** term in the excerpted protocol).
## Findings

- **Stage-specific steam effect:** MD + TGA consistently show **H\(_2\)O** accelerates **late-stage** (diffusion-limited) carbonation while leaving the **early kinetic** stage largely unchanged.
- **Microscopic mechanism:** **OH** from water dissociation promotes **CO\(_3^{2-}\)** formation and **CaCO\(_3\)** layer growth; **protons** migrate inward, hydroxylate the oxide, and **open** diffusion pathways—together improving **CO\(_2\)** penetration and **conversion** relative to dry conditions.
- **Practical reading:** because **steam** mainly speeds the **slow** regime, **process** designers may see the largest **gains** when **particles** are already **partially** carbonated and **diffusion** limits uptake—matching the **calcium-looping** context emphasized in the introduction.

- **Corpus honesty:** Quantitative **TGA** time constants and **MD** radial profiles should be taken from **`papers/Wang_CO2_H2O_CaO_NP_JPCC_2018.pdf`** (and **SI** references therein), not inferred from this summary alone.
## Limitations

Nanoparticle models may omit full reactor-scale transport; ReaxFF uncertainty on multicomponent oxide carbonation kinetics remains. **Sintering**, **particle** **packing**, and **interparticle** **diffusion** in **fixed** **beds** are not captured in single-particle MD, so **pilot** **reactor** data remain necessary when scaling **TGA**-informed **kinetics** to **process** **models**. **Particle** **polydispersity** and **intrapore** **diffusion** in **CaO** **pellets** add further **scale-up** **uncertainty**.

## Related topics

- [[reaxff-family]]
