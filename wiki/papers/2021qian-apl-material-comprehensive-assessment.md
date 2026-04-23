---
id: paper:2021qian-apl-material-comprehensive-assessment
type: paper
title: "A comprehensive assessment of empirical potentials for carbon materials"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:ml-atomistic
  - method:ml-potential
  - method:dft-static
  - task:application
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:dft-static
  - keyword:graphene-carbon
candidate_tags: []
source_refs: []
doi: "10.1063/5.0052870"
year: 2021
authors:
  - "Cheng Qian"
  - "Ben McLean"
  - "Daniel Hedman"
  - "Feng Ding"
venue: "APL Mater. 9, 061102 (2021)"
pdf_sha256: "c8f9e43b7cfdccc0b514a7bf8f2758027aacafdb82f1636e4f4183d90552990d"
pdf_path: "papers/ReaxFF_others/APL_Materials_Carbon_materials_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021qian-apl-material-comprehensive-assessment -->

!!! abstract "Scope"
    Benchmarks **carbon bond-order potentials (CBOPs)** and the **GAP-20** machine-learning potential against **DFT** across lattice data, cohesion, defects, vdW interactions, thermal stability, and mechanical response for several carbon allotropes.

## Summary

The article systematically compares widely used empirical carbon bond-order potentials and the Gaussian approximation potential GAP-20 (machine-learned on carbon) to density functional theory references. Properties examined include lattice constants, cohesive energies, defect formation energies, van der Waals interactions, thermal stability, and mechanical behavior across different carbon phases. The authors highlight that potential choice strongly affects predicted allotrope behavior, with GAP-20 generally tracking DFT more closely than the assessed CBOPs for structure, defects, and several thermal/mechanical tests, while still sharing CBOP-like limitations on van der Waals treatment.

The benchmark is motivated by widespread use of **CBOPs** in carbon materials modeling where transferability across **sp**, **sp²**, and **sp³** bonding environments is not guaranteed, and by interest in whether **ML** potentials can reduce systematic errors without hand-tuned bond-order forms.


## Methods

**MD application (classical CBOPs and GAP-20).** The study runs **large-scale** **molecular** **dynamics** with several **carbon** **bond-order** **potentials** (**CBOPs**: Tersoff/REBO/**AIREBO** family members and related forms as listed in the paper) and with the **machine-learned** **GAP-20** **potential** on the **same** **benchmark** **geometries** to compare **thermal** **stability** (e.g. **C\(_{60}\)** **heating** **tests**) and **mechanical** **response** (e.g. **nanotube** **fracture**, **graphene** **elastic** **tests** in the **figures**). **Ensemble** uses **NVT**/**NPT** as **stated** for each **thermo**/**stress** **case**; **timestep** **(fs)**, **K**-ramped **T**, **ps**–**ns** **trajectory** **lengths**, and **P** **(bar)** **in** **NPT** **segments** are **documented** in the **computational** **section** of *APL Mater.* **9**, **061102**—**N/A** to **transcribe** here. **LAMMPS**-style **inputs** are **typical** for the **field**; **N/A** **if** the **article** **names** a **different** **engine**—**verify** `pdf_path`. **Electric** **field** / **rare-event** **enhanced** **sampling: N/A** in the **abstract**-level **summary**.

**Static QM / DFT (reference data).** **DFT** supplies **lattice** **parameters**, **cohesive** **energies**, **defect** **formation** **energies**, and **other** **static** **properties** used as **the** **reference** for **comparing** **CBOPs** and **GAP-20**, including **assessment** of **interlayer** **van** **der** **Waals**-sensitive **quantities** (see **abstract**). **Functional**, **dispersion** **correction** **choice**, **basis**/**PAW**/**plane-wave** **settings**, and **k-point** **meshes** are **in** the **main** **text**—**N/A** in this **wiki** **note** (open **`pdf_path`** **Section** **2**). **Geometry** **relaxations** and, where used, **reaction**-**path** or **barrier** **protocols** are **spelled** **out** **there**; **N/A** to **re-list** every **NEB** **image** **count** **here**.

**ReaxFF**/**FF** **training. N/A** — **benchmark** **only**.

## Findings

**Comparisons to DFT.** **GAP-20** **more** **closely** **matches** the **DFT** **reference** for **structural** **and** **defect** **energetics** **across** the **crystalline** **allotropes** **and** **cases** **tabulated** than the **CBOPs** **surveyed** in the **work**. For **finite**-**T** **and** **mechanical** **tests** highlighted in the **abstract**, **GAP-20** **reproduces** **C\(_{60}\)** **thermal** **stability** and **nanotube**/**graphene** **fracture** **or** **elastic** **trends** **where** **CBOPs** **are** **reported** to **struggle**. **N/A** — the **article** is **not** a **kinetics** **database** for **reactive** **combustion** **chemistry**; **scope** is **all**-**carbon** **benchmarks** **in** the **manuscript**.

**Limitations (authored).** **Like** **CBOPs**, **GAP-20** **does** **not** **fully** **capture** **van** **der** **Waals** **interactions** in the **authors**’ **assessment**; **see** the **PDF** for **where** that **matters** **(layered** **stacking,** **fullerene** **crystals,** **etc.)**.

**Sensitivity.** **Property**-by-**property** **trends** **differ** **across** **allotropes**; **potential** **choice** is **a** **strong** **lever** **(pressure** in **NPT** **stretches**, **T** in **NVT** **heating** **protocols**).

## Limitations

Benchmark scope is defined by the potentials and carbon systems explicitly included; reactive chemistry and hetero-elements are not the focus.

## Relevance to group

External benchmark paper in corpus context: situates classical and ML carbon potentials relative to DFT for method selection in carbon MD.

## Citations and evidence anchors

- DOI: [10.1063/5.0052870](https://doi.org/10.1063/5.0052870)

## Related topics

- [[reaxff-family]] (context only—ReaxFF is not the subject of this benchmark)
