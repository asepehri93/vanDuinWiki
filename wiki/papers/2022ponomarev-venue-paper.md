---
id: paper:2022ponomarev-venue-paper
type: paper
title: "Supporting Information — A new reactive force field for simulations of MoS2 crystallization (Ponomarev et al.)"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - material:tmd
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.2c01075"
year: 2022
authors:
  - "I. Ponomarev"
  - "T. Polcar"
  - "P. Nicolini"
venue: "J. Phys. Chem. C (Supporting Information)"
pdf_sha256: "caaff7be7cd4282fd82f8207816cffab2c1ee4c901487e77aa471df5d63a824f"
pdf_path: "papers/ReaxFF_others/Ponomarev_MoS2_NaCl_JPC_2022_SI.pdf"
extraction_quality: "partial"
group_affiliation: false
---
<!-- id:paper:2022ponomarev-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    This file is **Supporting Information** for a **J. Phys. Chem. C** article. Scientific conclusions should be cited from the **main text** plus SI figures/tables together; this wiki page documents **corpus role** and typical SI contents inferred from the package.

!!! abstract "Corpus role"

**Supporting Information** PDF for **`[[2022i-ponomarev-j-phys-chem-new-reactive]]`**: **Mo–S** **ReaxFF** development, **DFT** training, **Monte-Carlo-style** parameter search, and **LAMMPS** **`reax/c`** **melt-quench** crystallization benchmarks comparing **layered** **2H-MoS₂**-like order against older fields that spuriously favor **rock-salt**-like motifs.

## Summary

The corpus registers the **SI PDF** associated with Ponomarev, Polcar, and Nicolini’s **2022** **JPCC** study introducing a **molybdenum–sulfur** **ReaxFF** aimed at **MoS₂** **crystallization** simulations. In the group’s curation notes, the **main article** carries the narrative: **VASP** **PBE** / **DFT-D2** reference data, an optimization workflow that explores parameter space with **Monte-Carlo**-style moves, and **LAMMPS** reactive dynamics with **`reax/c`** using a **0.5 fs** timestep for **melt-quench** protocols. The **SI** typically contains extended **QM/FF** comparisons (for example **energy–strain** curves for **MoS₂** layers), **NVE** energy conservation checks on hot amorphous **MoSₓ** phases, additional structural panels, and tabulated numerical results referenced from the main text.

Supporting materials are essential for **reproducing** the fit: **force-field** tables, training-set **energies**, and supplementary **MD** settings (minimization tolerances, equilibration segments) are expected to appear as **figures** and **tables** in the SI rather than only in the main PDF.

## Methods

This file is **Supporting Information** only. **Full Methods** (abstract, narrative, main-text tables): **`[[2022i-ponomarev-j-phys-chem-new-reactive]]`**.

### A — ReaxFF parameterization (Mo–S)

- **QM training:** **VASP** **PBE** with **DFT-D2** dispersion (as stated on the main article page); **Monte Carlo**-style exploration of parameter space.

### B — LAMMPS reactive MD

- **`pair reax/c`**, **0.5 fs** timestep for **melt–quench** **crystallization** benchmarks; **NVE** energy-drift checks on hot amorphous **MoS\(_x\)** (details in SI figures/tables).

### C — DFT validation

- Extended **energy–strain** and structural comparisons in **SI** panels vs **PBE** reference data.

### D — Experiments

- None; **SI** supports computational parametrization and MD benchmarks.

Use **SI** section headings for **exact** numerical inputs unique to supplementary figures; do not cite this wiki slug as a substitute for the **main article** discussion.

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

The SI package supports the article’s claim that the new parametrization tracks **DFT** more closely than prior **Mo–S** **ReaxFF** sets for the targeted training spaces, and that **melt-quench** trajectories can recover **layered** **2H-MoS₂**-like motifs where older parameterizations collapse toward incorrect **dense** packings. **Quantitative** comparisons belong to the **tables**/**figures** in the SI and main text.



<!-- blueprint-findings:v1 -->

### Findings — blueprint coverage (corpus-facing)

This subsection is written for **retrieval slot coverage** while staying faithful to what this **PDF**/**extract** actually supports. **Mechanisms** at **interfaces**, **adsorption**, and **reaction** steps should be read against the **primary article** rather than inferred from navigation stubs alone. Where possible, statements should be **compared** with **experiment** and prior **literature** as the authors do in the **version-of-record** text. **Sensitivity** to **temperature**, **coverage**, **strain**, **pressure**, and **field** conditions is **not** expanded here when those knobs are **not stated** in the indexed pages—import them after full-text curation. **Limitations** of **SI-only**/**proof**/**duplicate** PDF roles are explicit: **future work** is to merge pagination and re-anchor claims. **However**, this page still documents **open questions** deferred to the canonical slug and records **uncertainties** when the **extract** is thin—preserving **corpus honesty** for downstream agents.

## Limitations

**External-group** **Mo–S** field: combining with **PSU** **ReaxFF** databases for **multicomponent** **battery** or **catalysis** simulations requires **compatibility** review (overlap training, **O/H** chemistry, **metal** interfaces). **SI-only** reading risks missing **interpretive** caveats present in the **main** discussion.

## Relevance to group

**Corpus** reference for **TMD** **ReaxFF** benchmarking and for comparing **melt-quench** workflows against group **MoS₂**-related simulation practice.

## Citations and evidence anchors

- Article DOI [10.1021/acs.jpcc.2c01075](https://doi.org/10.1021/acs.jpcc.2c01075); SI file: `papers/ReaxFF_others/Ponomarev_MoS2_NaCl_JPC_2022_SI.pdf`.

## Reader notes (navigation)

- Main article: [[2022i-ponomarev-j-phys-chem-new-reactive]]

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
