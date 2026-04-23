---
id: paper:2020atmani-energy-fuels-simulating-geological
type: paper
title: "Simulating the Geological Fate of Terrestrial Organic Matter: Lignin vs Cellulose"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:parallel-tempering
  - keyword:lammps
  - keyword:thermal-decomposition
  - keyword:polymer
source_refs: []
doi: "10.1021/acs.energyfuels.9b03681"
year: 2020
authors:
  - "Lea Atmani"
  - "Pierre-Louis Valdenaire"
  - "Roland J.-M. Pellenq"
  - "Christophe Bichara"
  - "Henri Van Damme"
  - "Adri C. T. van Duin"
  - "Franz J. Ulm"
  - "Jean-Marc Leyssale"
venue: "Energy Fuels 34:1537-1547 (2020)"
pdf_sha256: "674ecf2e14ba2eaa0b2fb16b062171ea44fe9b25dac962344857b603b93cf9b2"
pdf_path: "papers/Atmani_Energy_Fuels_2020.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020atmani-energy-fuels-simulating-geological -->

!!! note "Source"

    Prose here summarizes the *Energy Fuels* article at `pdf_path`. For full protocols, parameters, and figures, use the PDF and SI.

## Summary

Shale gas recovery models need nanoscale descriptions of kerogen matrices that adsorb and trap hydrocarbons in tortuous nanopores. Atmani et al. apply replica-exchange molecular dynamics to compare geological maturation of lignin versus cellulose—two abundant terrestrial biopolymers that contribute differently to sedimentary organic matter—into kerogen-like condensed phases plus methane. The abstract reports that lignin yields roughly twice as much kerogen and five times more methane than cellulose under the simulated protocol, consistent with pyrolysis experiments. Even when average composition and bonding statistics appear similar, ex-lignin kerogen is about an order of magnitude more compliant and microporous than ex-cellulose kerogen, implying different effective transport properties in pore-network models of shale where compliance controls fracture response and microporosity controls accessible surface area.

## Methods

**1 — MD application (LAMMPS + ReaxFF + REMD).** Interactions use **ReaxFF** (Reax2013 **C–C** parameters together with **C–O, C–H, O–O, O–H, H–H** sets cited in the paper) in the **large-scale atomic/molecular massively parallel simulator (LAMMPS)** package.

- **System size & composition.** **I-β cellulose** crystal, **~4200 atoms**, **O/C = 0.83**, **H/C = 1.67**. **Lignin** pack: **18 oligomers** from a **softwood lignin** model (Crestini *et al.*, as cited), **O/C = 0.34**, **H/C = 1.11**, in **orthorhombic** cells. Both use **3D periodic boundary conditions**.

- **Boundaries / periodicity.** **3D PBC** throughout.

- **Pre-REMD equilibration.** **NPT** at **423 K** and **25 MPa** until the cell volume converges (about **100 ps** for the disordered lignin case; relaxation details differ slightly by precursor).

- **Ensemble, timestep, integrator.** **NVT** and **NPT** legs as described in *Energy Fuels*: **Nose–Hoover** thermostat; **Nose–Hoover–Andersen** **barostat** for **NPT** legs. **Temperature and pressure** coupling time constants **0.05** and **0.5 ps**, **velocity–Verlet** integration, **0.1 fs** timestep.

- **REMD (enhanced sampling).** **NVT** sampling on an **exponential** temperature ladder from **423 K** to **3500 K** with **96 replicas**; **replica exchange** attempts every **10 fs** with **~20%** acceptance. **NVT** is used for REMD to avoid unphysical first-order transitions at fixed volume; because **volatiles** increase internal stress, the authors **interrupt** runs and **re-equilibrate** the **423 K** replica (and reinitialize all replicas) after **NPT** relaxation at **25 MPa** (e.g. **100 ps**). **Cellulose:** when pressure on the **423 K** replica **exceeds 200 MPa**, a relaxation stage is applied (three such stages in their protocol). **Lignin:** scheduled **NPT** relaxations every **200 ps**. **Cumulative REMD** until a near-equilibrium state at **423 K** takes about **750 ps (cellulose)** and **1300 ps (lignin)** for the *initial* confined-pyrolysis leg; a **second REMD** after **fluid removal** runs **1800 ps** (see paper for the fluid-expulsion protocol).

- **Barostat & pressure.** **NPT** at **25 MPa** during the relaxation/reinitialization windows described above. **N/A** — no external static **electric field** across the cell.

- **Shear, shock, AIMD cutoffs, QEq.** **N/A** — not the focus; standard ReaxFF/QEq usage per the manuscript.

**2 — Force-field training.** **N/A** — the study **applies** published **Reax2013** and related ReaxFF parameter files referenced in the article, rather than reporting a *new* fit in this work.

**3 — Static QM.** **N/A** — reactivity and thermochemistry come from **ReaxFF/REMD**, not a standalone DFT **results** section (QM references in the text support comparisons and field context, not a separate static-QM “application” block for maturation).

**Analysis (brief).** Molecular **clusters** are binned (gas C₀–C₄, light tar, heavy tar, kerogen/char) using bond cutoffs in the **Chemical Analysis** section; kerogen/char structure metrics include **H/C, O/C**, **coordination**, **RDFs**, and **ring** / **pore** descriptors as reported.

## Findings

**Yields (abstract).** **Lignin** produces about **twice** as much **kerogen** and **~5×** more **methane** than **cellulose**, consistent with **pyrolysis** experiments referenced in the paper.

**Structure–property.** Despite **similar** **average** **composition** and **bonding** statistics, **ex-lignin** kerogen is about an **order of magnitude** more **compliant** and **more microporous** than **ex-cellulose** kerogen—**morphology** (pores, compliance) diverges where **chemical** averages do not.

**Modeling use.** The authors position the results as **nanoscale** **building blocks** for **bottom-up** **shale** models that couple **organic** **texture** to **recovery** when combined with **continuum** **fracture**/**flow** solvers.

**Corpus honesty.** Consult `papers/Atmani_Energy_Fuels_2020.pdf` and SI for full **replica** statistics and any **chemical** **kinetic** **checks**; this page stays at abstract-level **yield**/**modulus** claims.

## Limitations

Simplified biopolymer models and idealized thermal histories omit mineral catalysis, confinement pressure, clay surfaces, and basin-specific kerogen variability that alter absolute yields in reservoir rocks.

## Relevance to group

van Duin as co-author on organic matter diagenesis and kerogen properties, relevant to geochemistry and energy applications of MD.

## Citations and evidence anchors

`papers/Atmani_Energy_Fuels_2020.pdf` — abstract (yield ratios, modulus/porosity contrast). https://doi.org/10.1021/acs.energyfuels.9b03681 — full Methods and SI tables should be consulted for replica-exchange parameters and statistical convergence checks.

## Related topics

- [[reaxff-family]]
