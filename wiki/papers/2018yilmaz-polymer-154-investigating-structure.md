---
id: paper:2018yilmaz-polymer-154-investigating-structure
type: paper
title: Investigating structure property relations of poly (p-phenylene terephthalamide)
  fibers via reactive molecular dynamics simulations
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:reactive-md
- domain:organics-polymers-pyrolysis
- method:reaxff
- task:application
- material:polymer-organic
- scale:atomistic
paper_keywords:
- keyword:reaxff-application
- keyword:reactive-md
- keyword:polymer
candidate_tags: []
source_refs: []
doi: 10.1016/j.polymer.2018.09.001
year: 2018
authors:
- Dundar E. Yilmaz
venue: Polymer, 154 (2018) 172-181. doi:10.1016/j.polymer.2018.09.001
pdf_sha256: 69009358dabd4c387475227b92da856050e0f3a626f3e5d59f40d2128b6f453c
pdf_path: papers/Yilmaz_Kevlar_Polymer_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018yilmaz-polymer-154-investigating-structure -->

## Summary

Poly(p-phenylene terephthalamide) (PPTA) fibers were built at a realistic scale and subjected to tensile loading using **ReaxFF reactive molecular dynamics**. The study compares **fully crystalline**, **fully disordered**, and **core–shell** (disordered core with crystalline shell) morphologies, introduces **nitrogen vacancies** as defects, and extracts tensile moduli, an empirical modulus relation, and a molecular picture of where chains fail under large strain. The work positions reactive MD as a way to connect **local bond-breaking chemistry** with **macroscopic mechanical** descriptors for aramid fibers when experimental access to atomic failure sites is limited.

## Methods

### Force field and morphologies

**ReaxFF** (parameter lineage discussed in the article) is benchmarked against **DFT** bond/group energetics for **PPTA**-relevant fragments (**Fig. 2**). Fibers are built in three architectures: **fully crystalline**, **fully unordered**, and **core–shell** (disordered core + crystalline shell). **Nitrogen vacancies** up to **5%** probe modulus vs **crystallinity** and **defect** density.

### MD application (**LAMMPS**, **NVT** tensile)

Simulations use **LAMMPS** as the parallel **MD** engine (**256** CPU cores on a **4×4×16** spatial decomposition) with **periodic** boundary conditions along transverse directions and the fiber axis along **z**. **Constant-volume NVT** integration employs a **Nosé–Hoover** thermostat (**25 fs** damping as printed) and a **0.25 fs** timestep for all stages. **Annealing** ramps **300 K → 600 K** over **10 ps**, holds **600 K** for **10 ps**, then cools to **300 K** over **10 ps** to relax artificial construction strain. **Quasi-static** tension increments the **z** strain by **1%** per macro-step; after each increment the authors run **5 ps NVT** to stabilize **pressure/energy**, then **5 ps NVT** to time-average **σ\(_{zz}\)** for the stress–strain point. Each full **1%** strain step spans **10 ps**, corresponding to **2×10¹¹ s⁻¹** engineering strain rate (acknowledged as high vs experiment). Loading continues until **fiber failure**. Representative diameters include **60 Å** (**153** chains) and **180 Å** (**1385** chains) in the crystallinity comparison set (**§3.1**).

- **Barostat / lateral pressure:** **N/A — NVT** at fixed cell volume; lateral **stress** relaxation is handled via the **staged NVT** segments described above rather than **NPT** barostat control.

- **Electric field / replica / metadynamics:** **N/A — not used**.

## Findings

- **Modulus vs order:** Average tensile modulus increases strongly with crystallinity (abstract: **~192 GPa** disordered vs **~289 GPa** crystalline).
- **Defect model:** An **empirical relation** predicts modulus from **crystallinity** and **nitrogen vacancy** density (abstract).
- **Failure mechanism:** Under large tensile load, failure begins with **chain scission at boundaries of crystalline domains** rather than uniformly through the fiber (HIGHLIGHTS/abstract).
- **Domains:** **Crystalline domains** are observed in the crystalline regions during deformation (abstract).
- **Interpretation:** The authors emphasize that **interfacial** weakness between ordered and disordered regions, rather than uniform bulk scission, dominates the simulated failure picture for the morphologies explored.

- **Comparisons / caveats:** Tabulated moduli (**~192 GPa** vs **~289 GPa** for disordered vs crystalline benchmarks in **§3.1**) should be read next to the authors’ discussion of **strain-rate** effects—the quoted **2×10¹¹ s⁻¹** loading is far above **quasi-static** **experiment**, so **versus experiment** claims remain contextual rather than pointwise matches.

- **Corpus honesty:** Numeric moduli and **strain** protocol details are authoritative in **`papers/Yilmaz_Kevlar_Polymer_2018.pdf`**; abstract-only numbers here should be double-checked against the final **Polymer** layout.
## Limitations

Reactive MD is limited by force-field accuracy for conjugated polyamide chemistry and by accessible time scales; quantitative comparison to macroscopic Kevlar fibers requires caution. Minor differences can exist between **proof and version-of-record** PDFs—verify critical numbers in the final journal file if needed.

## Relevance to group

**PPTA (Kevlar-class) reactive MD** with **ReaxFF** from **Yilmaz** and **van Duin**—illustrates **polymer mechanics** and **failure** at scales inaccessible to QM.

## Citations and evidence anchors

- DOI: `10.1016/j.polymer.2018.09.001`

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
