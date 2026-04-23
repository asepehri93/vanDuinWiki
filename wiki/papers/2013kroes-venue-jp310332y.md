---
id: paper:2013kroes-venue-jp310332y
type: paper
title: "Atomic oxygen chemisorption on carbon nanotubes revisited with theory and experiment"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:dft-static
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:dft-static
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:neb
  - keyword:validation-experiment
source_refs: []
doi: "10.1021/jp310332y"
year: 2013
authors:
  - "Jaap M. H. Kroes"
  - "Fabio Pietrucci"
  - "Alessandro Curioni"
  - "Rached Jaafar"
  - "Oliver Gröning"
  - "Wanda Andreoni"
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "54b9e7d45d12b9c31f8a4f75a1c68380d0931569be5d3064610441349e5d7a2f"
pdf_path: "papers/ReaxFF_others/Kroes_JPC_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013kroes-venue-jp310332y -->

## Evidence and attribution

!!! note "Evidence"

    Prose below summarizes the **peer-reviewed article** (**DOI `10.1021/jp310332y`**).

## Summary

**DFT (PBE, with additional BLYP/PBE0 comparisons)** studies **low-coverage** **atomic oxygen** chemisorption on **(10,0)** and **(8,4)** **single-walled carbon nanotubes**, addressing **ether vs epoxide** site preferences and **electronic structure** near **STM/STS** probes. **ReaxFF** (C/O reactive FF) is used to compare **classical** predictions of **structure** and **relative stability** against the **DFT** benchmarks for these chemisorption motifs.

## Methods

**DFT** calculations used the **Kohn–Sham** scheme with **PBE** exchange–correlation (with additional **BLYP** and **hybrid PBE0** data reported in places), **norm-conserving pseudopotentials**, and a **plane-wave** cutoff of **100 Ry**, as implemented in **CPMD**. Supercells for **(10,0)** and **(8,4)** **SWNTs** (~**1 nm** diameter) were converged with respect to size (models from **40** to **360** **C** atoms are discussed; much of the analysis uses **360** **C** in a periodic orthorhombic cell with stated lattice parameters in the article).

**ReaxFF** (C/O reactive parameterization cited in the paper) was used in the authors’ **ReaxFF** code for **geometry optimization** of chemisorbed **O** adducts, enabling classical comparison to **DFT** structures and **relative** energetics. **NEB** was used where **barriers** between **ether** and **epoxide**-related configurations were computed.

**STM/STS** measurements on purified **HiPco** **SWNTs** on **Au(111)** at **5 K** used in situ **atomic oxygen** from a **catalytic cracker**; **dI/dV** maps were recorded to probe **gap-state** changes near chemisorption sites.

**1 — MD application (thermally sampled RMD).** Aside from **CPMD**/**DFT** and **NEB** pathway work, the authors’ **ReaxFF** usage summarized above is **geometry optimization** of **O**-chemisorbed adducts, not a reported long **NVT**/**NPT** **production run** with quoted **timestep**/**thermostat** in this wiki’s summary. **N/A** — treat **fs** **timestep**, **ps**/**ns** **duration**, **Berendsen**/**Nosé–Hoover** controls, **barostat**, and **hydrostatic pressure** targets as **not stated** here; read **`papers/ReaxFF_others/Kroes_JPC_2013.pdf`** if production **molecular dynamics** appears beyond the optimization narrative.

## Findings

For an isolated **O** atom on the sidewall, **PBE** finds the **open ether** configuration **more stable** than **closed epoxide** by about **0.4 eV** on **(10,0)**, with **supercell-size** convergence requiring **>200** **C** atoms (smaller cells artificially stabilize **epoxide**-like motifs). **Electronic** differences are strong: **epoxide** introduces characteristic **gap states** detected in **STS**, whereas **ether**-related spectra differ, matching the experimental **dI/dV** trends discussed in the paper.

Prior literature disagreements on **low-coverage** energetics are attributed mainly to **undersized** simulation cells that do not represent **dilute** oxygen on **nanotubes**. **ReaxFF** reproduces **DFT** **structural** trends and **relative** **stability** ordering for these **O** chemisorption motifs in the authors’ tests (with the usual limitations of a classical model for **electronic** spectra).

**Sensitivity / outlook:** **Supercell** size and **functional** choice (**PBE** vs **hybrid**) shift **relative** **stability** of **ether** vs **epoxide** motifs and **gap** features compared to **STS**.

**Corpus honesty:** **`extraction_quality: good`** here refers to metadata alignment; quantitative claims should still be checked against **`pdf_path`** pages and figures.

## Limitations

DFT functional dependence (PBE vs hybrid) affects gaps and relative energies; classical FF cannot fully reproduce quantum electronic spectra.

## Reader notes (navigation)

- [[reaxff-family]]
- [[graphene-nanocarbon]]
