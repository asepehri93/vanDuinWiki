---
id: paper:2014golkaram-venue-jp-2014-07915j
type: paper
title: "Reactive molecular dynamics study of the pH-dependent dynamic structure of α-helix"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:reaxff-parameterization
  - keyword:nvt-simulation
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/jp507915j"
year: 2014
authors:
  - "Golkaram, M."
  - "Shin, Y. K."
  - "van Duin, A. C. T."
venue: "Journal of Physical Chemistry B"
pdf_sha256: "091c599284c6f30cfd71e0e562b168b6980da33d7f443a873883159a29d713ce"
pdf_path: "papers/Golkaram_JPCB_Helix_2014_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014golkaram-venue-jp-2014-07915j -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. For definitive numerical values, use the **JPCB** article (prefer the **version-of-record** PDF over this **proof** ingest when available).

## Summary

Peptide **secondary structure** is often simulated with **nonreactive** force fields that freeze **protonation states** or treat **pH** only implicitly, missing **acid–base** events that can reshape **hydrogen-bond networks** during **unfolding**. This **J. Phys. Chem. B** article uses **ReaxFF reactive MD** to follow an **α-helix → coil** transition as a function of **pH** for a peptide model, emphasizing **proton transfer** between **solvent** and **backbone** groups that break patterns nonreactive models cannot capture. At **extreme pH**, the simulations show substantial **unraveling** driven by **solution–peptide proton transfer**, and the authors compare **temperature** effects on the mechanism. The abstract claims **significantly better agreement with ab initio references** than prior **nonreactive MD** for the chemistry examined. The corpus PDF is a **proof**; minor layout differences from the final issue are possible.

## Methods

### Force field (biomolecular ReaxFF)

- Simulations use the authors’ **published ReaxFF biomolecular parameterization** for **C/H/O/N** chemistry in peptides and water (article introduction/Methods).

### Peptide and solvent setup

- **Ala\(_{13}\)** is built in a **zwitterionic** (charged termini) form deemed stable near **neutral pH**, placed in a **30 Å** cubic cell solvated to **~1 g cm\(^{-3}\)** liquid-like density (Methods opening on this page).

### pH mapping in reactive MD

- **Acidic/basic** conditions are explored by adding **excess H\(^+\)** and **OH\(^-\)** to the simulation cell rather than a full **constant-pH** Monte Carlo scheme—an approximate **pH** proxy consistent with the article’s framing (see **Limitations**).

### Sampling and observables

- Trajectories monitor **α-helix** content (or equivalent secondary-structure metrics defined in the paper) as functions of **pH** and **temperature**; **integration timestep, thermostat, and total runtime** are specified in **JPCB** Methods/SI rather than this proof-oriented wiki summary.

### 1 — MD application (ReaxFF biomolecular RMD)

- **Engine / code:** **LAMMPS** **molecular dynamics** with **ReaxFF** is the typical integration path for this group’s biomolecular **RMD** workflows—confirm the explicit engine statement in **`pdf_path`** / SI.
- **System size & composition:** **Ala₁₃** **zwitterion** in a **~30 Å** cubic cell solvated to **~1 g cm⁻³** (Methods summary on this page).
- **Boundaries / periodicity:** **3D PBC** cubic cell (implicit in the **30 Å** protocol description).
- **Ensemble:** **NVT** **molecular dynamics** at **300 K** production segments as reported in **JPCB** Methods—**N/A in this wiki summary** to quote alternative ensembles without reopening the PDF.
- **Timestep / thermostat / barostat / duration:** **N/A in this wiki summary**—see **JPCB** Methods/SI (`pdf_path`) for **Δt**, thermostat, **ps**/**ns** lengths, and any **NPT** segments if present.
- **Temperature:** multiple **temperature** conditions are compared in the article alongside **pH** proxies (abstract).
- **Pressure / stress control:** **N/A — hydrostatic pressure** is **not** part of the summarized **NVT**-style **helix** protocol here; confirm if any **NPT** equilibration appears in SI.
- **Electric field / metadynamics:** **N/A —** not part of the summarized protocol.

### 2 — Force-field training (this publication)

**N/A —** uses a **published biomolecular ReaxFF** parameterization (cited in the article) rather than reporting a new fit in the abstract framing summarized here.

### 3 — Static QM

**N/A —** **ab initio** references enter as **benchmarks** for selected chemistry, not as the primary **MD** engine (abstract).

## Findings

### 1 — Outcomes and mechanisms

Reactive MD identifies **new proton-transfer mechanisms** during denaturation that **nonreactive** force fields cannot represent, including **solution–backbone** transfers that disrupt **α-helical** hydrogen-bonding patterns. At **extreme pH**, the peptide undergoes substantial **unraveling**, and **temperature** modulates the mechanistic details in the comparisons reported. The authors argue reactive sampling aligns more closely with **ab initio** references than their **nonreactive** MD baselines for this chemistry, supporting ReaxFF as a tool for **pH-coupled** peptide dynamics—within the limitations of empirical protonation models.

### 2 — Comparisons

- **ReaxFF** trajectories vs **nonreactive MD** baselines and **ab initio** references for selected motifs (abstract).

### 3 — Sensitivity

- **pH** (via excess **H⁺**/**OH⁻**) and **temperature** modulate **helix** stability and **proton-transfer** pathways (abstract).

### 4 — Limitations / outlook

- Approximate **pH** mapping; see **## Limitations**.

### 5 — Corpus / KB honesty

- **`papers/Golkaram_JPCB_Helix_2014_proof.pdf`** may differ slightly from the final **JPCB** layout; quantitative metrics must be taken from the **version-of-record** PDF when available.

## Limitations

Proof PDF; **pH** in classical reactive MD is an approximate mapping to **excess** ions and **reactive** water chemistry, not a full **constant-pH** formalism.

## Citations and evidence anchors

- DOI [10.1021/jp507915j](https://doi.org/10.1021/jp507915j) (article footer in extract).

## Related topics

- [[reaxff-family]]
