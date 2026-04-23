---
id: paper:2013bae-venue-jp405992m
type: paper
title: "Improved ReaxFF force field parameters for Au–S–C–H systems"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
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
pdf_sha256: "9bcfe15a204633b2c37bf652e6ede227b37a5cc641290490d6c22c41f1079a6b"
pdf_path: "papers/ReaxFF_others/Bae_Aikens_AuSCH_improved_JPCA_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013bae-venue-jp405992m -->

## Summary

The article “Improved ReaxFF Force Field Parameters for Au–S–C–H Systems” (Bae and Aikens, *J. Phys. Chem. A* **2013**, DOI `10.1021/jp405992m`) reparameterizes the Järvi et al. Au–S–C–H ReaxFF description by adjusting Au–S and Au–Au bond parameters together with S–Au–S angle-bending terms to improve bending potential energy surfaces. The abstract states that the revised force field agrees with density functional theory geometries for small gold clusters and gold–thiolate nanoparticles, compares relative energies of Au₃₈(SCH₃)₂₄ isomers in line with PBE calculations, and reports relative energies for Au₄₀(SCH₃)₂₄ nanoparticles and Au-thiolate self-assembled monolayers using the updated parameters, concluding that the new parameters enable studies of larger gold–thiolate nanoparticle geometries and reactivity.

## Methods


Reference quantum data use **ADF** with the **PBE** functional, **TZP** basis, and **ZORA** relativistic treatment as stated in the **Computational Details** section of the extract: single-point energies and optimizations employ PBE; gold uses a frozen core [1s²–4f¹⁴], sulfur [1s²–2p⁶], carbon [1s²] in the basis/core partitioning described in the text layer. ReaxFF optimizations and molecular dynamics tests use **LAMMPS**; the paper notes **NVE-MD** relaxation toward **0 K** in **100 Å × 100 Å × 100 Å** periodic cells for validation cases. The extract presents the ReaxFF energy decomposition (bond, over/undercoordination, valence, torsion, van der Waals, Coulomb) and explains that improving the **S–Au–S** bending PES required parameter changes because the original −S–Au–S− staple motif was not linear/near-linear as in PBE for CH₃–S–Au–S–CH₃ scans from 130° to 220°. Parameters build on the 2011 Järvi training set with targeted refinements. Duplicate wiki coverage also exists under [[2013bae-j-phys-chem-jp405992m]] with author-resolved front matter; scientific content aligns between paths.

### MD application

**Engine / code:** **LAMMPS** **molecular dynamics** for **ReaxFF** validation trajectories (**Computational Details**).

**System & composition:** **100 Å** cubic **periodic** cells for selected **Au/S/C/H** validation runs; larger **Au–thiolate** nanoparticles and **SAM** models in **Results** (**abstract**).

**Ensemble:** **NVE** relaxation toward **0 K** as quoted in the extract.

**Timestep / duration / thermostat / barostat / production temperature:** **N/A —** not recovered from the short extract bundled with this slug—read **`pdf_path`**.

**Pressure:** **N/A —** not stated for these **NVE** validation snippets.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not used.

### Force-field training

**Parent FF / elements:** **ReaxFF Au–S–C–H** built on **Järvi et al. (2011)** with targeted edits to **Au–S**, **Au–Au**, and **S–Au–S** bending terms (abstract).

**QM reference:** **ADF** **PBE** with **TZP** basis and **scalar relativistic ZORA** (frozen cores for **Au**, **S**, **C** as in **Computational Details** on this PDF / sibling **`[[2013bae-j-phys-chem-jp405992m]]`**).

**Training set / optimization:** **DFT** geometries, energies, and **S–Au–S** bending **PES** scans for **thiolate** staples drive the **parameter optimization** / **least-squares** refit described in the article.

**Reference data used:** **PBE** benchmarks for clusters, **Au\(_{38}\)(SCH\(_3\))\(_{24}\)** isomers, **Au\(_{40}\)** motifs, and **SAM**-like assemblies (abstract).

## Findings

**Outcomes:** **Reparameterized Au–S–C–H ReaxFF** improves **S–Au–S** bending **PES** relative to **Järvi et al.**, while matching **PBE** geometries for benchmark clusters and **Au\(_{38}\)(SCH\(_3\))\(_{24}\)** isomer orderings; larger **Au\(_{40}\)** and **SAM** models are explored with the new parameters (**abstract**/**Results**).

**Comparisons:** **Original vs new ReaxFF** vs **PBE** on **CH\(_3\)–S–Au–S–CH\(_3\)** bending coordinates; **experimental** cluster literature cited for context (**Introduction** in extract).

**Sensitivity:** Errors concentrate in **staple bending** degrees of freedom that control **thiolate** binding motifs.

**Limitations:** **PBE** training bias; duplicate **PDF** hashes vs **`[[2013bae-j-phys-chem-jp405992m]]`** should be reconciled before manifest merges.

**Corpus honesty:** Full parameter tables live in **`[[2013aikens-venue-si8]]`** / **`[[2013aikens-venue-si8-2]]`** SI PDFs.

## Limitations

Transferability to very large nanoparticles or unconventional thiolate chemistries still requires case-by-case validation. Duplicate PDF ingests (`2013bae-venue-jp405992m` vs `2013bae-j-phys-chem-jp405992m`) should be consolidated for manifest hygiene when feasible.

Side-by-side comparison of the two wiki slugs should confirm identical `pdf_sha256` values before retiring one path; if hashes differ, investigate whether one PDF is a publisher update or a corrupted copy before merging records.

## Relevance to group

Canonical Au–S ReaxFF reference for thiol-capped gold and interface simulations used across catalysis and nanomaterials notes.

## Reader notes (navigation)

- [[2013bae-j-phys-chem-jp405992m]]
- [[2013aikens-venue-si8-2]]
- [[reaxff-family]]

## Citations and evidence anchors

DOI: [10.1021/jp405992m](https://doi.org/10.1021/jp405992m)
