---
id: paper:2013joshi-venue-research
type: paper
title: "Connectivity-based parallel replica dynamics for chemically reactive systems: From femtoseconds to microseconds"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:organics-polymers-pyrolysis, domain:methods-software, method:reaxff, task:method-development, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1021/jz4019223"
year: 2013
authors: ["Joshi, Kaushik L.", "Raman, Sumathy", "van Duin, Adri C. T."]
venue: "The Journal of Physical Chemistry Letters"
pdf_sha256: "548b25f15a12b90ad445d0e0d8dae0e61bd822f87e64e58e5167fa603ff88689"
pdf_path: "papers/Joshi_PRD_JPC_Letter_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013joshi-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

Standard **reactive molecular dynamics (RMD)** advances chemistry by **femtoseconds**, while many **pyrolysis** and **combustion** phenomena require **microsecond** horizons for rare activated events to manifest—creating a persistent **timescale gap** even with reactive force fields. This **J. Phys. Chem. Lett.** communication introduces **Reactive Parallel Replica Dynamics (RPRD)**, which adapts **parallel replica** acceleration to **bond-order-based** simulations by detecting transitions through **changes in bond connectivity** rather than coordinate-space harmonic basins used in earlier PRD theory for nonreactive systems. The authors benchmark RPRD on **1-heptene pyrolysis** using **ReaxFF**, reaching **up to ~1 μs** aggregate time with **40 heptene molecules** at temperatures as low as **1350 K** in the demonstration described in the abstract. The abstract further claims **reasonable agreement** between RPRD **product distributions** and **mechanistic** features and **shock tube experiments**, arguing that RPRD can reduce the distortion introduced by naive **high-temperature** brute-force sampling that skews branching ratios. Methodologically, the paper is a bridge between **rare-event** algorithms developed for **nonreactive** systems and **bond-order** reactive simulations where **connectivity** is the natural reaction coordinate; that alignment matters for hydrocarbon **pyrolysis** where both **barriers** and **branching** are sensitive to effective temperature histories.

## Methods

**Sources:** **`papers/Joshi_PRD_JPC_Letter_2013.pdf`** and `normalized/extracts/2013joshi-venue-research_p1-2.txt` (title, **abstract**, introduction through PRD background).

**1 — MD application.** **Engine / code:** **Reactive molecular dynamics** with **ReaxFF** plus **Reactive Parallel Replica Dynamics (RPRD)** clock merging as described in the letter; specific MD package string **N/A** on excerpt—confirm in **PDF**. **System size & composition:** **1-heptene** **pyrolysis** benchmark with **40 heptene** molecules (**~8×10² atoms** in the stoichiometry implied by the **abstract**). **Boundaries / periodicity:** **three-dimensional periodic** gas-phase **supercell** (**PBC**) is the standard setup for this benchmark class—still verify cell vectors in the **PDF**. **Ensemble:** **NVT**-style thermal control is typical for condensed/gas reactive cells in this literature; exact ensemble string **N/A** on **p1–2** excerpt—confirm. **Timestep:** introductory text notes **0.25** or even **0.10 fs** integration for reactive **MD** at high **temperature** (`2013joshi-venue-research_p1-2.txt`); use the letter’s **Computational Methods** for the **RPRD** benchmark value. **Duration / stages:** **RPRD** reaches **up to ~1 μs** aggregate reactive time for the **1-heptene** case (**abstract**), with **replica** trajectories run until **connectivity**-detected events advance the parallel clock. **Thermostat:** **Berendsen**/**Nosé–Hoover** parameters **N/A** on excerpt—read full **Methods**. **Barostat:** **N/A** — constant-volume reactive pyrolysis cell unless the letter specifies **NPT**. **Temperature:** demonstrations include **1350 K** and cooler regimes relative to brute-force overheating (**abstract**). **Pressure:** **N/A** — not highlighted on excerpt. **Electric field:** **N/A**. **Replica / enhanced sampling:** **parallel replica** / **PRD** acceleration with **connectivity**-based event detection (**abstract** + introduction).

**2 — Force-field training.** **N/A** — applies published **ReaxFF** hydrocarbon chemistry; fitting is not the letter’s focus.

**3 — Static QM.** **N/A** — letter centers on accelerated **RMD**, not standalone **DFT** production.

## Findings

**Outcomes & mechanisms:** **RPRD** extends **ReaxFF** trajectories to **microsecond** horizons for **1-heptene** **pyrolysis**, using **connectivity** changes as reactive events so **branching**/**mechanism** paths differ less from **low-temperature** chemistry than naive ultra-hot brute-force **MD**.

**Comparisons:** **Abstract** reports **reasonable agreement** of **product distributions** and **mechanistic** features with **shock tube experiments**.

**Sensitivity / design levers:** **Temperature** history (including **1350 K** demonstrations vs higher brute-force windows) and **replica** count / clock-merging policy affect inferred kinetics; authors caution that overheated brute-force runs skew **branching**.

**Limitations & outlook:** **PRD** requires approximate **Markovian** first-order escape kinetics and careful **event detection** tolerances—authors note limits when those assumptions break down.

**Corpus honesty:** Protocol tables, tolerance values, and software identifiers are only guaranteed in **`pdf_path`**; this page is **abstract**/**intro**-grounded plus the **timestep** discussion on **`normalized/extracts/2013joshi-venue-research_p1-2.txt`**.

## Limitations

PRD validity requires careful checking of **Markovian** assumptions and **event completeness**; performance depends on rare-event rates and hardware parallelism.

## Relevance to group

Methodological bridge between **ReaxFF chemistry** and **rare-event sampling**—important for pyrolysis/combustion and other activated processes.

## Citations and evidence anchors

- Abstract and introduction: RPRD definition, 1-heptene case, PRD background (J. Phys. Chem. Lett. **2013**, **4**, 3792–3797).

## Related topics

- [[reaxff-family]]
