---
id: paper:2022nayir-carbon-190-2-atomic-scale-probing
type: paper
title: "Atomic-scale probing of defect-assisted Ga intercalation through graphene using ReaxFF molecular dynamics simulations"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:validation-experiment
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2022.01.005"
year: 2022
authors:
  - "Nadire Nayir"
  - "Mert Y. Sengul"
  - "Anna L. Costine"
  - "Petra Reinke"
  - "Siavash Rajabpour"
  - "Anushka Bansal"
  - "Azimkhan Kozhakhmetov"
  - "Joshua Robinson"
  - "Joan M. Redwing"
  - "Adri van Duin"
venue: "Carbon"
pdf_sha256: "7cd622307ef9d8f18336f061107eeea18267f0b4677cd8ffabfbf141949488f6"
pdf_path: "papers/Nayir_Ga_graphene_Carbon_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2022nayir-carbon-190-2-atomic-scale-probing -->



!!! abstract "Scope"

Joint experiment and ReaxFF MD on Ga and TMGa on graphene with controlled vacancies, linking defect size to intercalation barriers and TMGa-assisted defect healing.

## Summary

Integrating **epitaxial non-layered metals** with **graphene** supports requires controlling **precursor chemistry**, **defect density**, and **intercalation** pathways that couple gas-phase and surface reactions. This **Carbon** article combines **Raman**, **X-ray photoelectron spectroscopy (XPS)**, and **scanning tunneling microscopy / spectroscopy (STM/STS)** on **graphene** with controlled **vacancy** populations alongside **ReaxFF molecular dynamics** for **Ga**, **metallic droplets**, and **trimethylgallium (TMGa)** interacting with **graphene** lattices containing **monovacancies**, **multivacancy** clusters, and **5–8–5** motifs. **Adri van Duin** co-authors the reactive modeling thread, which links **defect topology** to **adsorption strength**, **reaction temperatures**, and **barriers** for **Ga** transport through the sheet.

## Methods

### A — Experiments

- **Raman** (**D:G**), **XPS**, **STM/STS** on **graphene** with tuned **defect** load; track signatures as **Ga** / **TMGa** exposure progresses.

### B — ReaxFF MD

- **Periodic graphene** with **monovacancy** through **multivacancy** motifs (**5–8–5** etc.); **Ga** or **TMGa** impingement; **bond-order** tracking for **adsorption**, **fragmentation**, **intercalation**, **passivation** by **methyl**/hydrocarbon fragments.
- **Temperature** programs and **dosing** windows: *Carbon* **Methods**.

### C — Quantum chemistry

- Not primary; **ReaxFF** supplies pathways and relative barriers subject to QM cross-checks in the paper.

### D — Data fusion

- Compare simulation **pathway** statistics to **Raman** recovery and **STM** contrast trends.

<!-- blueprint-slots:v1 -->

### MD application — blueprint checklist (indexed text)

Use **`N/A`** where this **PDF role** or **short extract** does not restate a quantity; prefer linked **version-of-record** pages for definitive values.

- **Engine / code:** **LAMMPS** is the usual **reactive MD** engine when **ReaxFF** appears in this corpus; **N/A — additional engines** if not stated on this page.
- **System size & composition:** **Atom** counts / **stoichiometry** / **supercell** sizing are **N/A — not stated in the indexed extract** unless quoted above.
- **Boundaries / periodicity:** **Periodic boundary conditions (PBC)** are typical for slab/bulk models; **N/A — frozen layers / walls** if not stated here.
- **Ensemble:** **NVT** is typical for constant-volume production unless **NPT** is explicitly cited elsewhere for this entry.
- **Timestep:** **timestep** on the order of **0.25 fs** is common for **ReaxFF**; **N/A — exact fs** if not stated in the indexed text.
- **Duration / stages:** **Equilibration** and **production** lengths in **ps**/**ns** are **N/A — not stated** on this stub.
- **Thermostat:** **Nose–Hoover** / **Berendsen** / **Langevin** controls are **N/A — damping/time constant not stated** in the indexed pages.
- **Barostat:** **NVT** entries imply **N/A — barostat / hydrostatic pressure control** unless **NPT** is documented on the canonical article page.
- **Temperature:** **Temperature** setpoints (e.g., **300 K**) are **N/A — not restated** when this file is **SI/proof-only**.
- **Pressure:** **N/A — pressure / stress tensor** targets are **not stated** for this PDF role.
- **Electric field:** **N/A — external electric field / bias** not invoked on this page.
- **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not stated for the workflows summarized here.


## Findings

**Defect size** strongly modulates both **Ga** **adsorption** and the **thermal budget** needed for **deposition**: larger openings present more **undercoordinated carbon** that binds **Ga**-bearing species. **Multivacancy** defects **lower kinetic barriers** for **Ga intercalation** relative to pristine graphene, whereas **single vacancies** or **5–8–5** arrangements can remain **kinetically hindered** for through-sheet transport under comparable drives. **TMGa** can **heal** some defects by **passivating dangling bonds** with **carbon- or methyl-derived** fragments, consistent with **Raman** recovery and **STM** contrast changes after processing. Overall, the joint dataset argues that **defect engineering** is a practical knob for **2D metal integration** on **graphene** beyond ideal lattice chemistry alone. ReaxFF cannot capture full organometallic electronic structure; barrier heights and branching between intercalation versus surface growth should be cross-checked against the paper’s convergence tests and any DFT benchmarks they cite.

## Limitations

ReaxFF models approximate electronic structure of graphene defects and organometallic chemistry; quantitative barriers should be read from the paper’s convergence tests.

## Relevance to group

Group-led collaboration on 2DCC graphene processing with ReaxFF interpretation.

## Reader notes (navigation)

- [[reaxff-family]]
- Sibling PDF: [[2022nayir-carbon-190-2-atomic-scale-probing-2]] (Elsevier galley duplicate in corpus). Maintainer catalog (GitHub): [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2022.01.005](https://doi.org/10.1016/j.carbon.2022.01.005)

## Related topics

- [[reaxff-family]]
