---
id: paper:2013ding-venue-jp311498u
type: paper
title: "A reactive molecular dynamics study of n-heptane pyrolysis at high temperature"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:thermal-decomposition
  - keyword:nvt-simulation
  - keyword:reactive-md
  - keyword:berendsen-thermostat
source_refs: []
doi: "10.1021/jp311498u"
year: 2013
authors:
  - "Ding, Junxia"
  - "Zhang, Liang"
  - "Zhang, Yan"
  - "Han, Ke-Li"
venue: "The Journal of Physical Chemistry A"
pdf_sha256: "baa0fd95e8f4e32f341b3933da7cb3a5cc23aa3dce816174ef6a23e4f6245778"
pdf_path: "papers/ReaxFF_others/Ding_JPC_2013_heptane_ReaxFF.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013ding-venue-jp311498u -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

**ReaxFF-based reactive MD** is used to study **gas-phase pyrolysis** of **n-heptane** at very **high temperatures** (multi-thousand Kelvin regime in the reported simulations). The work emphasizes a **radical-dominated** mechanism with **unimolecular C–C fission** as the principal initiation channel, nonuniform scission propensity along the carbon chain (**central C–C bonds** preferentially), and qualitative support for **Rice–Kossiakoff**-type decomposition organization at the atomistic level. Apparent **activation energies** extracted from simulation kinetics fall in the **~43–54 kcal/mol** range for the sampled temperature window, described as broadly consistent with experimental high-temperature pyrolysis literature.

## Methods

**1 — MD application (atomistic dynamics).** **Engine / code:** **Reactive molecular dynamics (RMD)** with **ReaxFF** as described in **Computational Details** (explicit package name—e.g., **LAMMPS**—should be confirmed in **`pdf_path`**; the indexed excerpt emphasizes **ReaxFF** **RMD**). **System size & composition:** **unimolecular** cells contain **one** **n-heptane** molecule in a **20 Å × 20 Å × 20 Å** periodic cube (**~10¹–10² atoms** class); **multimolecular** cells contain **16** **n-heptane** molecules per periodic box (**~10³ atoms** class), with trajectory-count convergence tests reported in the article (**>~140** trajectories for unimolecular statistics; **≥9–12** trajectories for multimolecular observables depending on the quantity). **Boundaries / periodicity:** **three-dimensional periodic** cubic cells (**PBC**). **Ensemble:** **NVT** **MD**. **Timestep:** **0.1 fs**. **Duration / stages:** multiple independent trajectories and staged **annealing**/**heating** workflows are described in **`pdf_path`** (full schedule not reproduced in `normalized/extracts/2013ding-venue-jp311498u_p1-2.txt`). **Thermostat:** **Berendsen**-style coupling with **0.05 ps** temperature damping constant as stated in **Computational Details**. **Barostat:** **N/A —** **gas-phase** **NVT** protocol without **Parrinello–Rahman** pressure control. **Temperature:** **2400–3000 K** window emphasized for multimolecular kinetics analysis in the wiki summary; additional temperatures may appear in the full **Methods**. **Pressure:** **N/A —** not used as an explicit **MD** control variable in the summarized **NVT** gas-phase setup. **Electric field:** **N/A —** not reported. **Replica / enhanced sampling:** **N/A —** not reported. **Electrostatics / cutoffs:** **N/A —** not recovered from the indexed excerpt (confirm in **`pdf_path`** if relevant). **Species detection:** **bond-order cutoff 0.3**.

**2 — Force-field training.** **N/A —** uses published **C/H/O** **ReaxFF** parameters from **van Duin** / **Chenoweth** “**without modification**” (article wording in the extract).

**3 — Static QM / DFT.** **N/A —** **QM** is referenced only as historical context for **ReaxFF** parameter origins in the extract; this is not a **DFT**-application study.

## Findings

**1 — Outcomes & mechanisms.** **Pyrolysis** is **radical-dominated**; **unimolecular** decomposition proceeds primarily via **C–C bond fission**, with **central C–C bonds** breaking preferentially over **terminal** bonds in the sampled statistics (abstract/extract).

**2 — Comparisons.** **Multimolecular** product and intermediate distributions are compared qualitatively to several **experimental** **n-heptane** **pyrolysis** studies cited in the article (see **`pdf_path`** for species lists).

**3 — Sensitivity & design levers.** **Temperature** (**2400–3000 K** for the quoted **Ea** window), **unimolecular vs multimolecular** setup, and **trajectory** ensemble sizes are the main **levers** discussed for converged statistics.

**4 — Limitations & outlook.** The **Discussion** notes that additional **intermolecular** channels would be needed for richer **dense-phase** modeling beyond the gas-phase **supercells** emphasized here (article framing).

**5 — Corpus honesty.** Parallel corpus registration may exist as **`[[2013heptane-venue-jp311498u]]`**; numerical values should be verified against **`pdf_path`** for the paginated **J. Phys. Chem. A** article (**DOI** in front matter).

## Limitations

- Extremely high simulated temperatures and short timescales constrain direct comparison to engine-relevant lower-temperature chemistry; force-field fidelity for radical-rich networks is scenario-dependent.

## Relevance to group

Corpus **fuel pyrolysis** reference using the widely circulated **hydrocarbon ReaxFF** parameter lineage associated with the group’s foundational papers.

## Citations and evidence anchors

- Abstract and methods: force-field citation, temperature ranges, Ea extraction (J. Phys. Chem. A; DOI above).

## Reader notes (navigation)

- Parallel corpus PDF for the same article: [[2013heptane-venue-jp311498u]].

## Related topics

- [[theme-pyrolysis-combustion-organics]]
- [[reaxff-family]]
