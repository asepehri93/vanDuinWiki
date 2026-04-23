---
id: paper:2013bae-j-phys-chem-jp405992m
type: paper
title: "Improved ReaxFF force field parameters for Au–S–C–H systems"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:metallic-systems
  - keyword:lammps
  - keyword:nve-simulation
source_refs: []
doi: "10.1021/jp405992m"
year: 2013
authors:
  - "Bae, Gyun-Tack"
  - "Aikens, Christine M."
venue: "Journal of Physical Chemistry A"
pdf_sha256: "91753abcfbfb55140d28e0e036ab8d0321baec76d9576c5f9a1bfe5193153652"
pdf_path: "papers/ReaxFF_others/Bae_Aikens_AuSCH_JPC_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013bae-j-phys-chem-jp405992m -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

**ReaxFF** **Au–S–C–H** parameters are **reoptimized** from an earlier **Järvi et al.** set (**2011**). **Au–S**, **Au–Au**, and **S–Au–S** **bending** terms are adjusted to improve **bond-bending** **PES** behavior. The updated field reproduces **PBE** **geometries** for **small** **clusters** and **gold–thiolate** **nanoparticles**; **Au₃₈(SCH₃)₂₄** **isomer** **energetics** align with **PBE** **ordering**; **Au₄₀(SCH₃)₂₄** and **SAM**-like models are sampled with the **new** parameters (**abstract** claims). **Thiolated** **Au** **nanoparticles** are ubiquitous in **sensing** and **drug-delivery** models; improving **staple** **motif** **bending** surfaces matters because **Au–S** **coordination** **changes** feed into **facet** **stability** and **ligand** **exchange** pathways.

## Methods


**DFT reference:** **Amsterdam Density Functional (ADF)** with **PBE**, **triple-ζ polarized (TZP)** **basis**, **scalar** **relativistic** **ZORA**, **frozen** **cores** as stated (**Au** core through **4f**, **S** through **2p**, **C** through **1s**). **Cluster** **geometries** and **single-point** **energies** feed the **ReaxFF** **reoptimization** starting from **Järvi et al.** **2011** **Au–S–C–H** parameters.

**ReaxFF / MD:** All **ReaxFF** runs use **LAMMPS**; **NVE** **relaxation** to **0 K** is mentioned with **100 Å** cubic **periodic** **cells** for **Au/S/C/H** **tests** in the **Computational** section excerpt.

**Fitting focus:** Adjust **Au-S**, **Au-Au**, and **S-Au-S** **bending** terms so **staple** **-S-Au-S-** motifs can approach the **near-linear** **PBE** **minimum** (**Figure 1** **PES**). **Parameter** **tables:** **`[[2013aikens-venue-si8]]`** / **`[[2013aikens-venue-si8-2]]`**.

### MD application

**Engine / code:** **LAMMPS** **molecular dynamics** for **ReaxFF** validation (**Computational Details**; extract).

**System & composition:** **100 Å × 100 Å × 100 Å** periodic cells for selected **Au/S/C/H** tests; nanoparticle and **SAM** examples in the article body (**abstract**/**Results**).

**Boundaries / periodicity:** **3D periodic** cubic cells for the cited **MD** relaxation tests.

**Ensemble:** **NVE** relaxation toward **0 K** as stated in the **Computational** section excerpt.

**Timestep:** **N/A —** numerical **Δt (fs)** not recovered from `2013bae-j-phys-chem-jp405992m_p1-2.txt`—see **`pdf_path`**.

**Duration / stages:** **N/A —** total **ps/ns** schedule not in the short extract.

**Thermostat / barostat:** **N/A —** not stated for the **NVE** relaxation description on indexed pages.

**Temperature:** **N/A —** explicit thermostat targets for all **MD** snippets not in the excerpt.

**Pressure:** **N/A —** not stated for these **NVE** cells in the excerpt.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not used.

## Findings

**Outcomes:** **NP-specific ReaxFF** reproduces **PBE** geometries for small **Au–thiolate** clusters and improves **S–Au–S** bending **PES** relative to **Järvi et al. 2011** (abstract). **Au\(_{38}\)(SCH\(_3\))\(_{24}\)** isomer orderings match **PBE**, and larger **Au\(_{40}\)(SCH\(_3\))\(_{24}\)** plus **SAM**-like models are sampled with the updated field (abstract).

**Comparisons:** Benchmarks are primarily **versus PBE** training data; introduction cites **experimental** cluster literature for motivation.

**Sensitivity / levers:** Accuracy hinges on **staple** vs **bridge** motifs and **bending** angles along the **CH\(_3\)–S–Au–S–CH\(_3\)** scan highlighted in **Figure 1**.

**Limitations:** **PBE-centric** training; explicit **solvent**, **electrode potentials**, and **electrochemical** environments are outside the gas-phase/cluster emphasis (see **Limitations** on this page).

**Corpus honesty:** Duplicate wiki slug **`[[2013bae-venue-jp405992m]]`** shares the DOI; confirm **`pdf_sha256`** before merging manifests.

## Limitations

**PBE** **training** scope; **nanoparticle** **isomer** **space** incomplete in any finite study. **Explicit** **solvent**, **electrode** **potentials**, and **image** **charge** effects in **electrochemical** environments are not treated in the **gas-phase**/**periodic** **cluster** setups emphasized in the parameterization paper. **Relativistic** **corrections** beyond the **ZORA** **scheme** employed may matter for **quantitative** **binding** on **very** **small** **Au** **clusters**.

## Relevance to group

**Gold–thiolate** **ReaxFF** line used broadly in **nanoparticle** and **SAM** simulations adjacent to group **metal**/**organic** interfaces.

## Citations and evidence anchors

- DOI **10.1021/jp405992m** — *J. Phys. Chem. A* **117**, 10438–10446 (2013).
- Extract: `normalized/extracts/2013bae-j-phys-chem-jp405992m_p1-2.txt`.

## Related topics

- [[2013bae-venue-jp405992m]]
- [[2013aikens-venue-si8]]
- [[reaxff-family]]

## Reader notes (navigation)

Duplicate **corpus** paths sometimes exist for the same **DOI**; prefer the **`pdf_path`** on this page when resolving **hashes** and **chunks**.
