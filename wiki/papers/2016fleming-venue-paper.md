---
id: paper:2016fleming-venue-paper
type: paper
title: "New Approach for Investigating Reaction Dynamics and Rates with Ab Initio Calculations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - method:aimd
  - method:enhanced-sampling
  - method:semiempirical-tightbinding
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.5b10667"
year: 2016
authors:
  - "Kelly L. Fleming"
  - "Pratyush Tiwary"
  - "Jim Pfaendtner"
venue: "Journal of Physical Chemistry A"
pdf_sha256: "c874a06e7066debde445c39e1c722a9d62e6b3f7ea224f28af234dcfcee31f42"
pdf_path: "papers/Others/Fleming_Pfaendter_metadynamics_JPCA_2016.pdf"
extraction_quality: "partial"
group_affiliation: false
paper_keywords:
  - keyword:aimd
  - keyword:enhanced-sampling
  - keyword:method-development
  - keyword:parallel-tempering
---
<!-- id:paper:2016fleming-venue-paper -->

## Summary

The authors use **infrequent metadynamics** (an acceleration-factor formulation of biased metadynamics) together with **semiempirical and ab initio molecular dynamics** to estimate reaction rates and Arrhenius-like activation behavior for a **symmetric S_N2** model reaction. The work includes large-scale sampling (reported as **>5000** independent metadynamics runs with the **PM6** Hamiltonian), reweighting of biased free-energy data to recover the reaction potential-energy surface, and a **Car–Parrinello MD + metadynamics** demonstration on the same reaction with only **O(10–20)** rare-event realizations.

The introduction motivates **rare-event** kinetics from biased sampling as a practical route when brute-force **AIMD** cannot reach millisecond-scale barrier crossings, using a textbook **S\(_N2\)** coordinate as a controlled testbed for comparing semiempirical throughput with costly **CPMD** demonstrations.


## Methods

**MD application (enhanced sampling + semiempirical / ab initio MD):** The workflow combines **infrequent metadynamics** (acceleration-factor formulation tied to the instantaneous bias) with large ensembles of biased trajectories for a **gas-phase symmetric S\(_N2\)** benchmark—a **small-molecule cluster** system (implicitly periodic **PBC:** **N/A — gas-phase benchmark**, not a bulk slab). **Semiempirical leg:** **>5000** independent metadynamics runs with **PM6**. **Ab initio leg:** **Car–Parrinello MD** plus metadynamics for the same reaction with only **O(10–20)** rare-event realizations. **Analysis** reweights biased free energies to recover a reaction **PES** and compares **Arrhenius-like** activation behavior to **high-temperature unbiased** kinetics. **Ensemble label (NVT vs NVE) during biased segments:** **N/A — not stated in the partial corpus extract**; see *J. Phys. Chem. A* Methods. **Software package, timestep, thermostat parameters, production segment lengths (ps/ns), barostat, and electric field:** **N/A — not stated in the partial corpus extract**; read **`papers/Others/Fleming_Pfaendter_metadynamics_JPCA_2016.pdf`** and **SI** before reproducing numerically.

**Force-field training:** **N/A — not a ReaxFF or classical FF parameterization study.**

**Static QM / DFT:** **CPMD**-style **ab initio** forces drive the **Car–Parrinello** leg; **functional, basis, and numerical settings** are in **JPCA** (**N/A — not transcribed here**).

**MD setup (gas-phase benchmark):** **S\(_N2\)** **cluster** geometry and any **PBC** choice are defined in *J. Phys. Chem. A*. **Ensemble label for metadynamics segments, barostat/pressure control, and trajectory lengths:** **N/A — not stated on the partial extract used here** (see paper tables).

## Findings

- Infrequent metadynamics can **quantitatively estimate reaction rates** from biased and unbiased simulation setups in the benchmark studied.
- Reweighted metadynamics free energies reproduce a **reaction PES** from which **Arrhenius-like activation energies** can be extracted; results are reported to agree with **unbiased high-temperature** kinetics.
- **Car–Parrinello MD + metadynamics** achieves rare-event sampling for the same reaction with **only about 10–20** calculations of the rare event, supporting feasibility for costly **ab initio** potentials.
- The study highlights **transition-state ensemble** sampling challenges even with enhanced sampling, motivating statistically controlled rate estimates.

## Limitations

- Application focus is a **model gas-phase S_N2** reaction; transfer to condensed-phase or enzyme-scale chemistry requires separate validation.
- **Semiempirical (PM6)** and **DFT-level CPMD** costs and parameter choices (collective variables, bias deposition) strongly affect practical accuracy.

## Relevance to group

Methodological **rare-event kinetics** reference; not ReaxFF-centric but relevant where **AIMD + enhanced sampling** is compared to reactive force-field workflows.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.5b10667](https://doi.org/10.1021/acs.jpca.5b10667) — *J. Phys. Chem. A* **120**, 299–305 (2016).

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Corpus PDF path: `papers/Others/Fleming_Pfaendter_metadynamics_JPCA_2016.pdf`.
