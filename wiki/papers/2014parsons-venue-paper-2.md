---
id: paper:2014parsons-venue-paper-2
type: paper
title: "Modeling of molecular nitrogen collisions and dissociation processes for direct simulation Monte Carlo"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:methods-software
  - method:reaxff
  - task:method-development
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:method-development
  - keyword:validation-experiment
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1063/1.4903782"
year: 2014
authors:
  - "Neal Parsons"
  - "Deborah A. Levin"
  - "Adri C. T. van Duin"
  - "Tong Zhu"
venue: "J. Chem. Phys. 141, 234307 (2014)"
pdf_sha256: "5f1aa8bac026da5b6095980b1b2d5e0dd2891401a957f08a093da4523fc601ab"
pdf_path: "papers/Parsons_N2_N2_JCP_2014_proof.PDF"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2014parsons-venue-paper-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow the **JCP** article (`doi`). The corpus PDF is an **AIP proof**; verify pagination in the **published** issue.

## Summary

Computes **N₂–N₂** **collision** and **reaction** cross sections for **hypersonic** **nonequilibrium** flows using **MD/Quasi-Classical Trajectories** on a **global PES** fit with **ReaxFF** to advanced **ab initio** data. **DSMC** models built from these cross sections predict **less dissociation** than a baseline **total collision energy** model under strong **nonequilibrium**, while **equilibrium rates** agree with reference data; **1D shock** tests show modest changes in **dissociation** and **shock thickness** vs baseline chemistry. The abstract reproduced in the proof extract explains that **DSMC** for **Earth re-entry** needs reliable **collision** cross sections and **reaction probabilities**, yet **viscosity-based** extrapolations may fail at **shock temperatures**, and **equilibrium** **rate laws** may misrepresent **strong thermal nonequilibrium**—motivating **MD/QCT** on a **ReaxFF-fitted** **N₂–N₂** surface for the dominant **air** diatom.

## Methods

Grounding: **`papers/Parsons_N2_N2_JCP_2014_proof.PDF`** (AIP **proof**; same work as **`[[2014parsons-venue-paper]]`**) and `normalized/extracts/2014parsons-venue-paper-2_p1-2.txt`.

**Molecular dynamics / quasi-classical trajectories (MD/QCT)** on a **global N₂–N₂ potential energy surface** fit with **ReaxFF** to **advanced ab initio** data, targeting **N₂(¹Σ⁺_g)–N₂(¹Σ⁺_g)** collisions relevant to **hypersonic** **nonequilibrium** air (**J. Chem. Phys.** **141**, 234307). The manuscript compares **MD/QCT** **reaction probabilities** to a **total collision energy (TCE)** baseline, validates **equilibrium reaction rates** against reference data, and checks **total collision cross sections** against **variable hard sphere (VHS)** totals, then couples the chemistry model to **DSMC** with a **1D shock** example.

### 1 — MD application (trajectory sampling)

- **Engine / code:** **MD/QCT** workflows driven by the fitted **PES** (**Summary**); **N/A — integrator and software** not copied here.
- **System size & composition:** Binary **N₂–N₂** collision partners per trajectory.
- **Boundaries / periodicity:** **N/A — gas-phase** collision setup (see **JCP**).
- **Ensemble:** **N/A — not stated** on this stub (not bulk **NVT**/**NPT** MD).
- **Duration / stages:** **MD/QCT** sampling spans **ps**/**ns**-scale trajectory batches as reported in **JCP** **141**, **234307**—see article tables.
- **Timestep:** **N/A — integration timestep** not copied into this wiki stub (see **JCP** **141**, **234307**).
- **Thermostat:** **N/A — not applicable** to the quasi-classical collision workflow in the same sense as bulk **MD** thermostats—confirm treatment in **JCP** **Methods**.
- **Temperature / pressure:** **Nonequilibrium** energy distributions for **shock**-like conditions (**abstract**); **N/A — detailed tables** not duplicated here.
- **Electric field:** **N/A — not stated.**
- **Replica / enhanced sampling:** **N/A — not stated.**

### 2 — Force-field training

- **Parent FF / elements:** **ReaxFF** fit to **ab initio** references to build the **global N₂–N₂ PES** (**Summary**).
- **QM reference / training set / optimization / external reference data:** documented in **JCP** **141**, **234307**—**N/A — not duplicated** on this proof-ingest page.

## Findings

### Outcomes and mechanisms

**MD/QCT** **reaction probabilities** show **better physical behavior** and predict **less dissociation** than the baseline **TCE** model under strong **nonequilibrium** **shock**-like conditions (abstract). **Dissociation** chemistry is therefore tied to an **ab initio**-anchored **PES** rather than purely phenomenological models.

### Comparisons

**Equilibrium rates** agree computed references and **shock-tube** data; **total cross sections** agree **VHS** where compared (abstract).

### Sensitivity and scope

**N₂** dominates **air** chemistry in **hypersonic** shocks in the authors’ framing, motivating a dedicated **N₂–N₂** dataset before extending to full **air** chemistry.

### Limitations and corpus honesty

**Proof PDF** with embedded editorial queries in `normalized/extracts/2014parsons-venue-paper-2_p1-2.txt`; cite the **published** **JCP** issue for **pagination** and final numbers. Prefer **`[[2014parsons-venue-paper]]`** when using the non-proof PDF path in this corpus.

## Limitations

Proof PDF; **air chemistry** is broader than **N₂–N₂** alone; PES accuracy limits extrapolation to very high energies.

## Relevance to group

**van Duin** coauthored **ReaxFF**-based **aerospace** chemistry **cross sections**—distinct from electrochemistry but part of the **reactive FF** portfolio.

## Citations and evidence anchors

- https://doi.org/10.1063/1.4903782 — J. Chem. Phys. **141**, 234307 (2014).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
