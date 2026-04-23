---
id: paper:2018schuyler-b-nicholson-the-journal-effects-temperature
type: paper
title: Effects of temperature and mass conservation on the typical chemical sequences
  of hydrogen oxidation
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:fuel-combustion
- domain:methods-software
- domain:reactive-md
- method:reaxff
- task:method-development
- scale:atomistic
paper_keywords:
- keyword:combustion
- keyword:puremd
- keyword:reaxff-application
- keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: 10.1063/1.5012760
year: 2018
authors:
- Schuyler B. Nicholson
- Mohammad Alaghemandi
- Jason R. Green
venue: J. Chem. Phys.
pdf_sha256: 0e91df89b62e5cb42ea8c68a7693c7602fe96db4a9fadc2b5f2d87770dcfb910
pdf_path: papers/ReaxFF_others/Alaghemandi_JCP_H2_O2_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018schuyler-b-nicholson-the-journal-effects-temperature -->

## Summary

**PuReMD-GPU** integrates gas-phase **H\(_2\)/O\(_2\)** chemistry with Chenoweth–van Duin / Agrawalla-type **ReaxFF** parameters, generating stochastic species trajectories in a **20 × 20 × 20 Å** periodic cell (**66 H\(_2\)**, **33 O\(_2\)**, **OH** seed). **NVT** trajectories (**Nosé–Hoover**, **1 ps** coupling, **0.1 fs** timestep) at **20** temperatures from **2400 K** to **6800 K** (**50** runs per **T**) feed marginal species statistics; time series are windowed around **water** formation crossovers for variational **typical-set** and **mass-conserving typical-set** analyses of reaction sequences.

Elementary reaction sequences in combustion underpin ignition and extinction reduced models; typical sets summarize dominant pathways without enumerating every trajectory, and the mass-conserving extension probes how forbidden transitions distort joint probabilities when mapping **ReaxFF** **MD** to symbolic kinetics. Full trajectory lengths in **ps**/**ns** and tables are in the *J. Chem. Phys.* **Methods** / **SI** on `pdf_path`.
## Methods

**Reactive MD engine and force field.** **PuReMD-GPU** integrates gas-phase **H\(_2\)/O\(_2\)** chemistry with **ReaxFF** parametrizations for hydrocarbon/hydrogen combustion (Chenoweth *et al.* 2008; Agrawalla & van Duin 2011; Cheng *et al.* adaptive variants cited in the article).

**System, boundaries, and protocol.** Simulations use a **cubic** periodic cell (**20 Å** per side) containing **66 H\(_2\)**, **33 O\(_2\)**, and an **OH** radical seed (**composition** as reported), with **three-dimensional periodic boundary conditions (PBC)**. **Ensemble:** **NVT** with a **Nosé–Hoover thermostat** (**1 ps** coupling time) and a **0.1 fs** **timestep**. **Temperature** is scanned across **20** set points from **2400 K** to **6800 K** (**thermal** grid as reported). **Barostat / hydrostatic pressure:** **N/A — constant-volume NVT** gas-phase box without **NPT** stress control in the protocol summarized here. **Electric field:** **N/A — not used**. **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not used; statistics come from brute-force **reactive MD** trajectories analyzed by information-theoretic sequence constructions.

**Sampling plan and analysis window.** The study runs **50** independent **trajectories** at each **temperature**; **N/A — full production segment length in ps/ns** should be taken from the *J. Chem. Phys.* **Methods** (not restated in the p1–2 extract used for this page). **Species** time series are windowed around **water** formation crossovers to build joint probabilities for **variational typical sets**, including a **mass-conserving** variant compared against **atom-tracked** sequences from **MD**.
## Findings

Mass-conserving typical sets capture a larger fraction of probability in the restricted sequences and overlap atom-tracked mechanistic sequences with >90% probability at intermediate sequence lengths. Topological and joint entropy rates extracted from typical-set sizes and probabilities scale approximately linearly with temperature, suggesting extrapolation of sequence statistics across temperatures without exhaustive new simulations (within the paper’s tested H2/O2 model).

**Comparisons, sensitivity, and limitations.** The **mass-conserving** construction is compared directly to **atom-tracked** **reaction** sequences from **MD**, while the **temperature** dependence of **entropy rates** supports **extrapolation** claims across the scanned **thermal** window. **Limitations** of the symbolic representation—including combinatorial cost for larger mechanisms and the approximate nature of **ReaxFF** **kinetics**—are discussed in the article and mirrored under **## Limitations** below. **Corpus honesty:** numerical details beyond the abstract + p1–2 extract should be verified in `pdf_path`.
## Limitations

Information-theoretic construction enumerates sequences combinatorially—expensive for larger mechanisms; reactive FF kinetics are approximate.

## Relevance to group

Directly cites ReaxFF combustion parametrizations associated with van Duin-group development and applies PuReMD-GPU trajectories as data for symbolic sequence statistics.

## Citations and evidence anchors

- DOI: [10.1063/1.5012760](https://doi.org/10.1063/1.5012760)

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
