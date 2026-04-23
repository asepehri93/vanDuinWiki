---
id: paper:2016rajesh-kumar-j-phys-chem-jp6b05812
type: paper
title: "Effects of different hydrogenation regimes on mechanical properties of h-BN: A reactive force field study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - material:hexagonal-boron-nitride
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:lammps
  - keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b05812"
year: 2016
authors:
  - "Rajesh Kumar"
  - "Pierre Mertiny"
  - "Avinash Parashar"
venue: "J. Phys. Chem. C 2016, 120, 21932-21938"
pdf_sha256: "ec9dcba04a0841dc08a27edcefc011090c2aa4215cfbf87334a702e93e39465c"
pdf_path: "papers/Others/Kumar_hBN_JPC_C_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016rajesh-kumar-j-phys-chem-jp6b05812 -->

## Summary

Hexagonal boron nitride shares a graphene-like lattice but with ionic character between boron and nitrogen, so fixed-charge classical potentials can miss charge redistribution when edges or surfaces are hydrogenated. Molecular dynamics with ReaxFF (the Han *et al.* parametrization for B/N/H referenced in the article) compares mechanical behavior of pristine, semihydrogenated (hydrogen on boron only or nitrogen only), and fully hydrogenated h-BN nanosheets in armchair and zigzag-oriented model cells on the order of a few nanometers per side. Radial distribution functions track how local bonding environments evolve under chemical decoration, while displacement-controlled uniaxial tension extracts elastic stiffness, strength, and failure pathways. The authors highlight strain-driven switching of hydrogen between donor and acceptor-like roles in hydrogen-bonding interactions, which can increase toughness for particular semihydrogenated motifs relative to the pristine sheet, with quantitative trends presented as stress–strain curves in the primary publication.

## Methods

**1 — MD application (reactive classical MD).** Simulations use **LAMMPS** with **ReaxFF** using the **B/N/H** parameterization of **Han *et al.*** cited in the article. The authors prefer **ReaxFF** over **Tersoff**-type **BN** models because **charge redistribution** and **bond-order evolution** matter for **hydrogenated** h-BN under **mechanical strain**. **Nanosheet** supercells are about **5.0 nm × 5.2 nm** along **armchair** and **zigzag** in-plane directions for **pristine** h-BN, **semihydrogenated** cases (**H on B only** vs **H on N only**), and **fully hydrogenated** h-BN. **Radial distribution functions** characterize local bonding; **uniaxial tension** after relaxation yields **stress–strain** curves to failure. **Timestep**, **ensemble** choices during relaxation versus loading, **thermostat** and **barostat** settings, target **temperature**, **strain rate**, **equilibration/production** durations, **electrostatic** cutoffs, and **QEq** update frequency are **N/A —** not stated on the short extract used for this pass; take numerical protocol values from **`pdf_path`**. **Shear or shock loading**, **applied electric fields**, and **enhanced sampling** (umbrella, metadynamics, replica exchange) are **N/A —** not described as part of this study in the indexed front matter of the article used here.

**2 — Force-field training.** **N/A —** the paper **applies** a published **B/N/H ReaxFF**; it does not report a new parameterization.

**3 — Static QM / DFT.** **N/A —** central results are **classical reactive MD**, not DFT production trajectories.

In-plane **periodic boundary conditions** apply to the nanosheet models. Unless the full text is quoted elsewhere on this page: **NVT**/**NPT** staging, **timestep** (fs), **equilibration** and **production run** lengths (ps or ns), **thermostat** and **barostat**/**pressure** control, target **temperature** (K), and **strain rate** are **N/A —** not transcribed from the indexed excerpt; confirm in **`pdf_path`**. **Molecular dynamics** is implemented in **LAMMPS** as stated above. **Electric field** driving and **umbrella**/**metadynamics**/**replica-exchange** sampling are **N/A —** not reported for this study.

## Findings

**Outcomes and mechanisms.** Relative to **pristine** h-BN, hydrogenation changes **structural stability** in the authors' comparison: **semihydrogenation with H bound only to N** is the **least stable** configuration considered, while **full hydrogenation** is the **most stable**. Under **applied tensile strain**, **hydrogen** can alternate between **hydrogen-bond acceptor and donor** roles, which the authors associate with **higher toughness** for certain **semihydrogenated** nanosheets.

**Comparisons and sensitivity.** **RDF** and **stress–strain** trends are given in **J. Phys. Chem. C** figures and tables; elastic moduli, strengths, and failure strains should be read from that source. Trends **versus** hydrogenation motif and **strain** follow the article’s curves rather than this summary.

**Limitations and outlook.** The authors’ discussion of model scope (nanosheet size, edge chemistry, loading path) should be read in the **PDF**; any claim not visible in the indexed excerpt is **N/A —** here.

## Limitations

Finite-size nanosheets and one loading orientation set limit direct comparison to bulk h-BN experimental values without extrapolation.

## Relevance to group

Shows ReaxFF-based mechanical testing protocols for hydrogenated BN nanosheets in the LAMMPS ecosystem.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.6b05812](https://doi.org/10.1021/acs.jpcc.6b05812)

## Reader notes (navigation)

- 2D mechanics: [[graphene-nanocarbon]]; ReaxFF applications: [[reaxff-family]].

## Related topics

- [[reaxff-family]]
