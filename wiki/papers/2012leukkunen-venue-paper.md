---
id: paper:2012leukkunen-venue-paper
type: paper
title: "A multiscale code for flexible hybrid simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - domain:reaxff-lineage
  - method:reaxff
  - task:software
  - scale:atomistic
paper_keywords:
  - keyword:method-development
  - keyword:lammps
  - keyword:aimd
  - keyword:reaxff-application
  - keyword:charge-equilibration
candidate_tags: []
source_refs: []
doi: "10.48550/arXiv.1211.2075"
year: 2012
authors:
  - "L. Leukkunen"
  - "T. Verho"
  - "O. Lopez-Acevedo"
venue: "arXiv:1211.2075 [physics.comp-ph] (12 Nov 2012)"
pdf_sha256: "0baddec0be0c13079c6b1548563816ba4e05cf92d4ab1e2b83f3a3af08969f56"
pdf_path: "papers/ReaxFF_others/Leukkunen -ASE ReaxFF LAMMPS 2012 copy.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2012leukkunen-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **arXiv** manuscript describes **multi-scale** workflows in the **Atomistic Simulation Environment (ASE)** that combine **classical MD in LAMMPS** (including **ReaxFF**) with **DFT** via **GPAW**, and introduces a **force/energy Mixer** that combines multiple calculators in an **ONIOM-like** weighted scheme. A redesigned **ASE/LAMMPS** interface represents each **LAMMPS force field** as its own **ASE calculator** class (subclassing **`LAMMPSBase`**), with **FFData** parsing, **atom typing**, and optional **partial charges**; **LAMMPS-specific dynamics** classes run long segments inside LAMMPS to avoid per-timestep Python overhead.

## Methods


**ASE calculators:** each **LAMMPS** functional form is wrapped as a separate calculator; shared **`LAMMPSBase`** handles communication, **bond/angle/dihedral/improper** detection, and **LAMMPS input** generation from **FFData** and typing rules (template syntax for chemical environments and precedence). **LAMMPS dynamics** classes mirror standard ASE dynamics API but batch **many timesteps** in **LAMMPS** while still supporting **observers** and **trajectory** slices.

**Demonstration MD:** a **phenol-dimer** example from the **s22** dataset runs **10 ps** with **ReaxFF** (`ffield.reax`) then **10 ps** with **CHARMM CGenFF** (`par_all36_cgenff.prm`) using **`LAMMPS_NVT`** at **300 K** and **1 fs** steps; **ReaxFF**'s **built-in charge equilibration** supplies charges for the subsequent **CHARMM** stage where the interface does not implement its own **QEq**.

**Mixer:** combines **full-system classical** energy/forces with a **QM** correction on an inner region using per-atom **weights**; energy uses an **ONIOM-style** \(H = H_{3C} + \{H_{2Q} - H_{2C}\}\) split (notation as in the paper), while forces use **\(F_i = F_{i,3C} + w_i(F_{i,2Q} - F_{i,2C})\)** to mix **quantum** and **classical** sub-calculators.

**ReaxFF context:** text notes **ReaxFF** as a **reactive** bridge between **ab initio** and **empirical FF** methods, with large speed gain vs **GPAW** in mixed setups (e.g., **5000-atom** systems where **10 atoms** on **GPAW** dominate runtime).

<!-- blueprint-slot-coverage:auto -->
### MD application (blueprint slots)

**Engine / code:** **LAMMPS** for **molecular dynamics** when MD is discussed (indexed text).
**System size & composition:** Atom counts / stoichiometry appear in indexed text (see excerpt for numbers).
**Boundaries / periodicity:** **Non-periodic** / **cluster** / **surface** language appears in indexed text (no bulk **PBC** claim here).
**Ensemble:** **NVT** (indexed text).
**Timestep:** 1 fs (matched in indexed text)
**Duration / stages:** **ps**/**ns** scale timing or **equilibration**/**production** language appears in indexed text—see PDF for full schedule.
**N/A — thermostat** type/damping not recovered from indexed excerpt; verify PDF.
**Barostat:** **N/A — NVT** protocol without **hydrostatic pressure** control in indexed summary (no **NPT** stated).
**Temperature:** 300 K (matched in indexed text)
**Pressure / stress:** **Pressure**/**stress** language appears in indexed text—see PDF for control mode.
**Electric field:** **N/A — external electric field** bias not indicated in indexed excerpt for MD (if any field appears, it belongs to static QM/experiment sections).
**Replica / enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not indicated in indexed excerpt.

<!-- /blueprint-slot-coverage:auto -->

## Findings

**Outcomes / mechanisms:** The **ASE/LAMMPS** redesign enables **plug-in mixing** of **LAMMPS** (including **ReaxFF**) with **GPAW** or other calculators with **minimal extra coding**, and documents **performance-oriented** patterns for **production** classical or **hybrid** runs. The **phenol-dimer** walkthrough shows **back-to-back** **ReaxFF** and **CHARMM** dynamics on the same structure. The **Mixer** adds **flexible weighting** between **QM** and **classical** regions using an **ONIOM-style** energy split and per-atom force weighting, as defined in the article.

**Comparisons:** The authors contrast **ReaxFF** throughput with **GPAW** costs in representative **hybrid** sizing arguments (see **`pdf_path`**).

**Sensitivity / design levers:** **Calculator choice**, **LAMMPS** batching vs per-step **Python**, and **Mixer** weights are the main implementation levers discussed.

**Limitations / outlook:** **Hybrid QM/MM** boundaries and **weight** choices carry accuracy trade-offs; **ReaxFF** and **CHARMM** remain **training-set-limited** outside their intended chemistry.

**Corpus / KB honesty:** No `normalized/extracts/2012leukkunen-venue-paper_p1-2.txt` is present in this checkout; summaries follow **`pdf_path`** and the curated arXiv record `normalized/papers/2012leukkunen-venue-paper.json` (`extraction_quality: partial`).

## Limitations

Hybrid **QM/MM** boundaries and **weight** choices affect accuracy; **ReaxFF** and **CHARMM** remain **parameterization-limited** outside their training sets.

## Relevance to group

**Operator reference** for **ASE + LAMMPS + ReaxFF** integration adjacent to **PuReMD/LAMMPS** reactive workflows in the corpus.

## Citations and evidence anchors

- DOI: [10.48550/arXiv.1211.2075](https://doi.org/10.48550/arXiv.1211.2075)
- Primary source: `papers/ReaxFF_others/Leukkunen -ASE ReaxFF LAMMPS 2012 copy.pdf` (see `pdf_sha256` in front matter)
- Normalized stub: `normalized/papers/2012leukkunen-venue-paper.json`

## Related topics

- [[reaxff-family]]
- [[2012aktulga-parallel-com-parallel-reactive]]
- LAMMPS reactive workflows
