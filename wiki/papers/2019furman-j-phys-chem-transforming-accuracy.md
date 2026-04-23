---
id: paper:2019furman-j-phys-chem-transforming-accuracy
type: paper
title: "Transforming the Accuracy and Numerical Stability of ReaxFF Reactive Force Fields"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:methods-software
  - method:reaxff
  - task:method-development
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:method-development
  - keyword:reactive-md
  - keyword:lammps
source_refs: []
doi: "10.1021/acs.jpclett.9b02810"
year: 2019
authors:
  - "David Furman"
  - "David J. Wales"
venue: "J. Phys. Chem. Lett. 2019, 10, 7215-7223"
pdf_sha256: "de0399ceba82ec2f288f473dd4d0eeac51f10cfe7f22a592e23fbb16646e04a0"
pdf_path: "papers/ReaxFF_others/Furman_JPC_letters_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019furman-j-phys-chem-transforming-accuracy -->

## Summary

Furman and Wales publish a methods-focused *Journal of Physical Chemistry Letters* article (DOI `10.1021/acs.jpclett.9b02810`) arguing that some widely observed **ReaxFF** pathologies—**poor microcanonical energy conservation** during **MD** and **stalling** or **noisy** **geometry optimization**—are not merely “**force-field accuracy**” issues but can arise from **inconsistencies** between **analytic** energy **derivatives** and **numerical** **finite-difference** references for particular **ReaxFF** **term** implementations. Their diagnosis matters for the **reactive MD** community because practitioners often attribute bad **NVE** drift to **time integration** settings or **ReaxFF** parameters when part of the signal can be **implementation** error in **forces**. The Letter’s punchline is practical: **correcting** derivative definitions can yield **orders-of-magnitude** improvements in **energy drift** and **optimization** convergence on representative **benchmarks** spanning **liquid water**, **molecular crystals**, and **peptides**, without increasing the **asymptotic** **per-step** cost of the force evaluation.

## Methods

### Force-field fitting vs implementation (A)

This Letter does **not** introduce a new **ReaxFF parameterization**; it diagnoses **inconsistencies** between **analytic** energy **derivatives** and **numerical finite-difference** forces for certain **term implementations** in **reference ReaxFF** code paths (analysis anchored to **van Duin**-style reference implementations cited in the paper).

### Software verification, optimization, and microcanonical MD (B)

**Gradient auditing:** **Systematic** comparison of **analytic ReaxFF gradients** to **finite-difference** references, decomposing errors across **bond-order-dependent valence** terms, **van der Waals**, and **Coulomb** pieces to locate defective contributions.

**Geometry optimization benchmarks:** **L-BFGS** **stress tests** on **small organics**, **benzene** and **TNT** **single crystals** (stated supercell dimensions in the Letter), **bulk liquid water**, and **peptide** models (**alanine dipeptide**, **trpzip2**), requiring convergence to tight **residual force** norms; **legacy** vs **corrected** derivative formulations are compared.

**NVE molecular dynamics:** Short **microcanonical** segments assess **energy conservation** (**drift**) as an end-to-end check that **forces** match the **energy** model—complementary to pointwise finite-difference tests.

### Static QM (C)

**Not applicable**—the work is **force-field implementation** analysis on **ReaxFF** PESs.

### Energy-landscape framing (D)

The text ties **gradient noise** and **optimization failure** to **computational potential energy landscape** concepts (**stationary points**, **Hessian index**, **conditioning**) as **sensitive** probes that **standard MD** may mask.

**Benchmark MD and optimization cells.** **Geometry optimization** and short **microcanonical NVE molecular dynamics** use **periodic** **supercells** for **bulk liquid water**, **molecular crystals** (e.g., **benzene**, **TNT**), and **peptide** models with **atom** counts and **unit-cell** dimensions stated in the Letter (`pdf_path`). **Integration timestep** in **fs** and **NVE** segment lengths in **ps** appear in the **Methods** for the drift tests. **Thermostat:** **N/A** for the quoted **NVE** energy-conservation checks; **NVT**/**thermal** protocols are **N/A** for those specific microcanonical segments. **Ensemble:** **NVE** for drift diagnostics; optimization uses energy minimization without **NPT** **barostat** servocontrol—**N/A** for **hydrostatic pressure** targets. **Temperature:** minimized structures correspond to **300 K**-class benchmarks where the Letter specifies **thermal** preparation. **External electric field:** **N/A**. **Enhanced sampling:** **N/A** — direct **MD** and **L-BFGS** optimization only.

## Findings

### Mechanisms (root cause)

Across **benchmark** systems, **legacy** derivative implementations can fail tight **L-BFGS** tolerances even when structures look chemically plausible; **corrected** gradients converge to **much lower residual forces** and cut **NVE energy drift** by **orders of magnitude** at **no extra asymptotic cost** per force evaluation. The core issue is framed as **implementation inconsistency**, not **parameter inaccuracy**.

### Limitations

Benefits are **engine-dependent**: users must run a build that includes the **corrected** **gradient** definitions analyzed in the Letter. The benchmarks are **representative** organic/inorganic/peptide/water cells—not exhaustive coverage of every **ReaxFF** term in every **fork**.

### Future work and practice (implied)

**Regression tests** combining **finite-difference force checks** and **short NVE** segments on the **published benchmark cells** are the practical takeaway when **patching** **ReaxFF** paths in **LAMMPS** / **PuReMD** / related codes; **loose** optimization tolerances in production can **hide** residual derivative bugs.

## Relevance to group

Foundational ReaxFF integrator/gradient correctness referenced across the reactive MD community; relevant to any long-time ReaxFF production runs.

## Citations and evidence anchors

https://doi.org/10.1021/acs.jpclett.9b02810

## Related topics

- [[reaxff-family]]
