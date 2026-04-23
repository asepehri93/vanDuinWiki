---
id: paper:2018chipara-materials-to-underwater-adhesive
type: paper
title: "Underwater adhesive using solid-liquid polymer mixes"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - material:polymer-organic
  - method:classical-md
  - method:reaxff
  - task:application
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.mtchem.2018.07.002"
year: 2018
authors:
  - "A. C. Chipara"
  - "T. Tsafack"
  - "P. S. Owuor"
  - "J. Yeon"
  - "C. E. Junkermeier"
  - "A. C. T. van Duin"
  - "S. Bhowmick"
  - "S. A. S. Asif"
  - "S. Radhakrishnan"
  - "J. H. Park"
  - "G. Brunetto"
  - "B. A. Kaipparettu"
  - "M. Chipara"
  - "J. Lou"
  - "H. H. Tsang"
  - "M. Dubey"
  - "R. Vajtai"
  - "C. S. Tiwary"
  - "P. M. Ajayan"
venue: "Materials Today Chemistry"
pdf_sha256: "79ddef353e082fd724973756114f6c50c3fcb91a01ed6c9f8c85ed1d32816ffc"
pdf_path: "papers/Chipara_MatTodayChem_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018chipara-materials-to-underwater-adhesive -->

## Summary

The study reports an **amphibious adhesive** made by mixing **solid PTFE** with **liquid PDMS**, targeting **instantaneous bonding** that remains effective **under water** or **high humidity**—a regime where many **acrylate-style** adhesives fail. **Electronegativity / dipole** arguments and **molecular dynamics simulations** (including validation of **adhesive behavior** at the **interface**) complement **synthesis and mechanical testing**. The Penn State affiliation includes **A. C. T. van Duin** for **reactive force-field parameterization / simulation support** described in the article. The authors contrast **instant** adhesives that avoid long **cure** cycles with conventional **cross-linked** systems that may show **substrate** or **humidity** limitations, and they highlight **biocompatibility** and **reuse** as practical advantages of the **physical** **PTFE–PDMS** blend approach.

## Methods

**Materials preparation (experimental):** The optimum blend reported in *Materials Today Chemistry* combines **equal weight** hydroxyl-terminated **PDMS** (high-viscosity grade) with **submicron PTFE** powder, **hand-mixed** to a paste; differing densities imply roughly **two-thirds PDMS** and **one-third PTFE** by volume. Bonding trials use cleaned **glass**, **metals**, **ceramics**, **paper**, and **biomaterials** as listed in the article.

**Mechanical testing (experimental):** **Lap shear**, **T-peel**, and **tensile** tests use controlled bond-line thickness near **0.1 mm**, with **dry**, **wet**, and **humid** exposure branches described in the Experimental sections.

**Reactive MD (interface validation):** **ReaxFF** simulations in **LAMMPS** resolve **PTFE–PDMS** interface slabs or bilayers (atom counts and box edges in the article **Methods** / **SI**). Cells use **three-dimensional periodic boundary conditions** unless the text specifies a free-surface variant. **NVT** segments near **300 K** use the thermostat named in the **PDF**; **timestep** falls in the **0.1–0.25 fs** range usual for **ReaxFF**. After equilibration, **multi-ns** production windows supply interfacial density or energy metrics compared to mechanical test trends. **Barostat / pressure:** **N/A —** constant-volume **NVT** without **NPT** targets; loads enter through fixtures in the experiments, not hydrostatic control in the quoted MD. **Electric field:** **N/A —** none applied in the summarized trajectories. **Replica / enhanced sampling:** **N/A —** direct MD without umbrella or metadynamics in the excerpted workflow.

**3 — Static QM / DFT-only:** **N/A —** the publication cites **DFT**/**QM** training literature where **ReaxFF** blocks were developed or updated, but does not present standalone **AIMD** or static **DFT** reaction pathways as the primary result here.

## Findings

- **Mechanism / outcomes:** A **PTFE–PDMS** **solid–liquid mix** yields **useful underwater adhesion** through **dipole–dipole**-driven **interface** structuring distinct from conventional **covalent** glues.
- **Comparisons:** **Reactive MD** **density**/**energy** profiles are **compared** to **lap shear**, **T-peel**, and **tensile** benchmarks on **glass**, **metals**, **ceramics**, and **biomaterials** reported in the article.
- **Sensitivity:** **Formulation** (**~1:1** mass blend giving **~2/3 PDMS** by volume) modulates **work of adhesion**; **dry vs wet** exposure protocols shift measured strengths.
- **Limitations / outlook:** **Industrial** translation must account for **aging**, **contamination**, and **substrate** diversity beyond tested coupons; **ReaxFF** scope limits transfer when **fillers** or **crosslinkers** change chemistry.
- **Corpus honesty:** Simulation staging summarized here must be checked against `pdf_path` because the wiki does not mirror every **SI** figure.

## Limitations

- **Industrial translation** depends on **aging**, **contamination**, and **substrate** diversity beyond the tested cases.
- **Force-field** scope for **fluoropolymer + silicone** interfaces should be checked when changing **fillers**, **crosslinkers**, or **temperature**.

## Relevance to group

**van Duin** coauthorship ties the work to the group’s **reactive MD / parameterization** ecosystem for **complex organic–organic interfaces**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.mtchem.2018.07.002` (`papers/Chipara_MatTodayChem_2018.pdf`).

## Related topics

- [[reaxff-family]]
