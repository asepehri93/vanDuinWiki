---
id: paper:2018selcuk-nat-structural-evolution
type: paper
title: Structural evolution of titanium dioxide during reduction in high-pressure
  hydrogen
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:oxides-ceramics
- domain:reactive-md
- material:oxide
- method:reaxff
- method:dft-static
- task:application
- scale:atomistic
paper_keywords:
- keyword:reaxff-application
- keyword:lammps
- keyword:oxide-surface
- keyword:npt-simulation
- keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: 10.1038/s41563-018-0135-0
year: 2018
authors:
- Sencer Selcuk
- Xunhua Zhao
- Annabella Selloni
venue: Nature Materials
pdf_sha256: bde882511727947fc4eff4154c3240c14756e8052ef9d68a0cee86d10322d79e
pdf_path: papers/ReaxFF_others/Selcuk_Selloni_NatureMaterials_2018_TiO2_H2.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018selcuk-nat-structural-evolution -->

## Summary

Hydrogen treatment can convert wide-gap anatase **TiO\(_2\)** into reduced, **Ti\(^{3+}\)**-bearing, **oxygen-vacancy**-rich forms associated with “black **TiO\(_2\)”** motifs used to extend visible-light response. Selcuk, Zhao, and Selloni combine **ab initio thermodynamics** (DFT-level free-energy surfaces in **H\(_2\)/H\(_2\)O** environments) with **ReaxFF reactive molecular dynamics** in **LAMMPS** to follow **high-temperature**, **high-pressure H\(_2\)** attack on **anatase** surfaces and nanoparticle models. The study emphasizes **H\(_2\)O** formation, **oxygen-vacancy** production and **migration**, **surface disordering**, and the emergence of a **disordered shell** around a more **crystalline core**, connecting atomistic pathways to experimental pictures of hydrogenated nanoparticles.

## Methods

**Static QM / DFT + ab initio thermodynamics.** **DFT** total energies feed **ab initio thermodynamics** surfaces for **anatase** in **H\(_2\)/H\(_2\)O** environments (Fig. 1 in the article), contrasting **dissociative H\(_2\)** adsorption vs **H\(_2\) + O\(_\mathrm{s}\) \(\rightarrow\) H\(_2\)O + V\(_\mathrm{O}\)**-type channels versus **temperature** and **water chemical potential**. **Functional / dispersion / basis / k-mesh** details should be taken from the *Nature Materials* **Methods** rather than duplicated here.

**Force-field training / validation against QM.** **ReaxFF** parameters for **Ti–O–H** chemistry are **benchmarked** against **DFT** (and **DFT+U** where cited) for **H** diffusion and **oxygen-vacancy** **migration** (Supplementary Fig. 1 referenced in the main text). The article explicitly notes a large **DFT** vs **ReaxFF** mismatch for **H\(_2\)** **dissociative adsorption** thermochemistry while reporting much closer agreement for **H** **diffusion** pathways used in long **MD**.

**MD application (ReaxFF in LAMMPS).** Production trajectories use **LAMMPS** with **ReaxFF** on **anatase** **slab** and **nanoparticle** models exposed to **high-pressure H\(_2\)**. Representative extended-surface runs reported in the main text include **\(T = 800\) K** and **\(p = 200\) bar** for the principal low-index surfaces, with **NPT** (**Nosé–Hoover** **thermostat** and **barostat**) control, **0.1 fs** **timestep**, and **nanosecond-scale** segments (e.g. **~1 ns** reductions quoted for comparable **slab** shapes in the indexed extract). **PBC:** **three-dimensional periodic** supercells for **slab** and particle models as standard for these simulations. **System sizes** (**atom** counts/thicknesses) and any **fixed** **layers** should be copied from the article/SI tables. **Electric field:** **N/A — not used** in the classical **MD** Hamiltonian described here. **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not indicated for the production **ReaxFF** protocol in the indexed excerpt.
## Findings

Reactive trajectories show **water** formation and **oxygen-vacancy** creation at **anatase** surfaces under the modeled **H\(_2\)** environments, followed by **vacancy** redistribution that can **disorder** outer layers while leaving a more **crystalline** interior—consistent with **core–shell** interpretations of hydrogenated **TiO\(_2\)** nanoparticles discussed relative to **experiment**. Facet-dependent **kinetics** appear in the indexed text (e.g. different **V\(_\mathrm{O}\)** accumulation rates on **(101)**, **(001)**, and **(100)** surfaces under the same nominal **temperature**/**pressure**), and the authors relate **H\(_\mathrm{ads}\)** inventories to prior surface **reactivity** rankings while cautioning that **ReaxFF** **overbinds** **H\(_2\)** **dissociation** relative to **DFT** (large energy mismatch quoted in the article). **Limitations / outlook:** the manuscript frames this mismatch as a deliberate **acceleration** tradeoff (analogous to elevated **temperature**) to observe **rare** **reduction** events, and points readers to **DFT**/**AIMD** segments in **Supplementary** material when quantitative **oxygen** fluxes are required. **Corpus honesty:** numerical values and additional **nanoparticle** protocols should be verified against `pdf_path` and **SI** beyond the indexed extract snippets used for this page.

## Limitations

ReaxFF accuracy remains below AIMD; phase diagrams depend on pressure/temperature sampling.

## Relevance to group

Demonstrates ReaxFF + DFT validation for oxide reduction under H2 relevant to catalysis and energy materials.

## Citations and evidence anchors

- DOI: [10.1038/s41563-018-0135-0](https://doi.org/10.1038/s41563-018-0135-0)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
