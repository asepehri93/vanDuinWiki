---
id: paper:2014casillas-venue-jp5093459
type: paper
title: "Elasticity of MoS₂ sheets by mechanical deformation observed by in situ electron microscopy"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - material:tmd
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:validation-experiment
  - keyword:2d-materials
source_refs: []
doi: "10.1021/jp5093459"
year: 2014
authors:
  - "Gilberto Casillas"
  - "Ulises Santiago"
  - "Héctor Barrón"
  - "Diego Alducin"
  - "Arturo Ponce"
  - "Miguel José-Yacamán"
venue: "J. Phys. Chem. C"
pdf_sha256: "c2a1ad9304d956075e41f63cd858cdab57d0b469b1a9de4028cdeff240f6e479"
pdf_path: "papers/ReaxFF_others/Casillas_MoS2_JPCC_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014casillas-venue-jp5093459 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. This is an **in situ TEM** **mechanics** paper—not a **ReaxFF** study. The PDF filename references **2015**; metadata **year** follows the article publication context encoded in the corpus slug (**2014**).

## Summary

**In situ TEM** with an **STM tip** bends **few-layer MoS₂** sheets. The abstract reports **extreme bending** (**~180°**) with **elastic recovery** upon tip retraction, **bond reconstruction** during bending, and **flexibility** of **trilayer** comparable to **monolayer** while the **bending modulus** rises by **~three orders of magnitude** vs **monolayer** in their interpretation. Results are stated to align with **theoretical** work on **MoS₂** **mechanics**. The experiment targets **mechanics** of **2D** **TMDs** under **large** **curvature**—relevant to **flexible** **electronics** and **strain engineering** where **failure** modes may differ from bulk **ceramics** because **vdW** **sliding** and **out-of-plane** **buckling** can accommodate **deformation**.

## Methods

### In situ mechanical loading (TEM + STM tip)

- **Few-layer MoS₂** specimens are **bent** and **released** using an **STM tip** integrated with a **TEM** stage so that **large-curvature** deformation and **elastic recovery** are observed **in real time** (abstract; experimental mechanics—**not** a force-field simulation).

### Structural characterization

- **Selected-area electron diffraction (SAED)** and **high-resolution TEM (HRTEM)** identify **layer count** and lattice continuity before/after bending (abstract-level workflow).

### Deformation metrics discussed in the abstract

- The authors report **extreme bending (~180°)** with **elastic recovery** on unloading and discuss **bond reconstruction** under bending while preserving recoverability (abstract).

### Protocol details not in the short extract

- **Electron dose**, **strain rate**, and **tip–sample** contact mechanics are **not** recoverable from the checked-in **`_p1–2` extract**—use the **J. Phys. Chem. C** article at `pdf_path` for quantitative **loading** conditions.

### Atomistic simulation (this publication)

- **MD application:** **N/A —** this work reports **in situ TEM** mechanics of **MoS₂**, not production **MD**, **AIMD**, or **ReaxFF** trajectories (`papers/ReaxFF_others/Casillas_MoS2_JPCC_2015.pdf`).
- **Force-field training:** **N/A —** not applicable.
- **Static QM / DFT:** **N/A —** not the primary methodology described in the abstract-level material indexed here.

## Findings

- Sheets sustain **bending approaching ~180°** yet **elastically recover** their **initial morphology** when the tip retracts, indicating **reversible** large-strain deformation.
- **In situ** evidence points to **bond reconstruction** during bending while retaining **recoverability** of the **prismatic** lattice upon unloading.
- **Trilayer** sheets remain **similarly flexible** to **monolayer** in this setup, but the **bending modulus** inferred in the authors’ analysis rises by **~three orders of magnitude** with thickness, consistent with **literature** **elastic** models cited in the paper.
- **Implication:** **apparent** **softness** under **bending** can coexist with **large** **modulus** values extracted from **different** **deformation** metrics—motivating careful definition of **strain** and **layer** **sliding** when comparing to **simulation**.

## Limitations

- **Electron beam** effects and **small** **sample** statistics; **theory** comparisons rely on **external** **calculations**.
- **In situ** **loading** may differ from **macroscopic** **nanoindentation** **strain rates**; **layer** **count** assignments from **TEM** carry **uncertainty** when **contrast** is **low**.
- **Residual** **stress** from **sample** **preparation** can bias **measured** **elastic** **response** compared to **free-standing** **mechanics** tests.

## Relevance to group

**2D sulfide** **mechanics** context for **TMD** **simulation** papers; **no** **van Duin** authorship—present as **corpus** **experimental** reference.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/jp5093459` (`papers/ReaxFF_others/Casillas_MoS2_JPCC_2015.pdf`).

## Related topics

- [[graphene-nanocarbon]]
