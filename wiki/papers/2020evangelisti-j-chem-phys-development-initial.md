---
id: paper:2020evangelisti-j-chem-phys-development-initial
type: paper
title: "Development and initial applications of an e-ReaxFF description of Ag nanoclusters"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - method:ereaxff
  - task:parameterization
  - material:metal-surface
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:charge-equilibration
  - keyword:reactive-md
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1063/5.0018971"
year: 2020
authors:
  - "Benjamin Evangelisti"
  - "Kristen A. Fichthorn"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys."
pdf_sha256: "fe8f3a9f5b971dd5f4a89a1a7138f38dbe4c8c5d44739f9492d98c899d02528c"
pdf_path: "papers/Evangelisti_JCP_Ag_clusters_eReaxFF.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020evangelisti-j-chem-phys-development-initial -->

First **e-ReaxFF** parametrization for **silver** with **explicit classical electrons**, reproducing **2D vs 3D** isomer transitions for **Ag\(_{N\le 20}\)** clusters against **DFT/CCSD(T)** references, with demonstrations on **Ag-halide redox** and **plasmon-like** electron dynamics.

## Summary

Small **Ag clusters** favor **2D** configurations at certain sizes and transition to **3D** with only a few added atoms—a pattern **standard EAM** misses. The authors augment **ReaxFF** with **explicit electrons** (e-ReaxFF) and a **bond-order-dependent dihedral** penalty that disfavors premature 3D branching for small clusters while allowing 3D at larger sizes. After training on **QM energy ordering** and barriers, **NVT MD** in the **standalone ReaxFF code** explores **halide redox** and **electron motion** phenomena not accessible to fixed-charge models.

The work is a methodological bridge between classical metallic potentials and quantum accuracy for sub-nanometer silver, where delocalized electronic effects matter.

## Methods

- **QM references:** **DFT** and **CCSD(T)** data for **Ag\(_N\)** isomers and selected reactions (functionals/basis sets per article).
- **e-ReaxFF form:** Explicit **electron particles** paired with **Ag\(^+\) cores**; **four-body dihedral** term controlling 2D/3D competition; parameters fit to reproduce **2D–3D** transition near **Ag\(_5\)–Ag\(_7\)** sizes as reported.
- **MD (application / validation):** Molecular dynamics in the **standalone** **ReaxFF** **code**; **NVT**; **Nosé–Hoover** **thermostat**; **timestep** **0.250** **fs** to **resolve** **fast** **electron** **motion** (Methods). **System** **size** **(Ag** **cores** **+** **explicit** **electrons**): on the order of **10**–**200** **atoms** in the **cluster** **examples** **(\(N \le 20\)** in the main **training** **corpus,** with **extensions** in the **article**). **Boundaries / PBC:** open-boundary, **isolated** **Ag\(_N\)** **cluster** **supercell** (non-bulk, **PBC: N/A** in the free-cluster sense of the code’s **treatment**). **Duration** **(eq./prod.):** **N/A** to **transcribe** all **ps** **segments** **here;** see **J. Chem. Phys.** **Temperature** **(thermostat** **setpoints**): **300** **K** **(and** **other** **values** in **application** **sections,** per **the** **paper**). **Barostat: N/A**; **hydrostatic** **pressure: N/A**; **external** **electric** **field: N/A**; **umbrella** / **replica** / **metadynamics: N/A**.

Training emphasizes relative isomer energies and barriers because cluster databases are sparse compared to bulk silver benchmarks.

## Findings

- New potential tracks the **2D lowest-energy structures** for small \(N\) and the **onset of 3D** stability by **Ag\(_7\)**, consistent with QM references.
- **EAM** comparisons highlight failures for **planar vs nonplanar** energetics in the sub-20 atom regime where e-ReaxFF agrees more closely with QM ordering.
- Case studies show **e-ReaxFF** capturing **oxidation-state changes** in **silver halide**-like reactions and enabling **plasmon-relevant electron dynamics** in MD (as illustrated in the paper’s application sections).

Demonstrating explicit electron dynamics in MD differentiates this line from prior ReaxFF metals limited to formal oxidation states embedded in bond orders alone.

The J. Chem. Phys. article documents the full training corpus, standalone integrator details, and additional cluster sizes beyond Ag\(_{N\le 20}\) for readers extending the parametrization to surfaces or salts.

Explicit-electron workflows remain more expensive than fixed-charge ReaxFF; scale tests should consult the reported timings in the article.

## Limitations

e-ReaxFF adds cost and parameter complexity; transfer to **bulk Ag** surfaces and alloys requires separate validation.

## Relevance to group

Foundational **van Duin-group** **e-ReaxFF** extension to **metallic silver**, cited as the **first e-ReaxFF metal** parametrization in the article.

## Citations and evidence anchors

- DOI: [10.1063/5.0018971](https://doi.org/10.1063/5.0018971)

## Related topics

- [[reaxff-family]]
