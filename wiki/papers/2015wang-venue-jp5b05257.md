---
id: paper:2015wang-venue-jp5b05257
type: paper
title: "Hydration Mechanism of Reactive and Passive Dicalcium Silicate Polymorphs from Molecular Simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - material:cement-mineral
  - method:dft-static
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:classical-md
  - keyword:oxide-surface
  - keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b05257"
year: 2015
authors:
  - "Qianqian Wang"
  - "Hegoi Manzano"
  - "Yanhua Guo"
  - "Iñigo Lopez-Arbeloa"
  - "Xiaodong Shen"
venue: "J. Phys. Chem. C"
pdf_sha256: "46c6e1b02c387a2e412fa55d4be11ddd2a26d168468d053b937c3a703e16c1b6"
pdf_path: "papers/ReaxFF_others/Wang_Manzano_JPCC_2015_CaSiO2.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2015wang-venue-jp5b05257 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **J. Phys. Chem. C** article identified by `doi` and `pdf_path`. It is not new primary claims by this wiki.

## Summary

**Dicalcium silicate (C\(_2\)S)** exists as multiple **polymorphs** with markedly different **hydraulic** reactivity in cement clinker, yet the atomistic origins of “**reactive**” versus “**passive**” behavior remain debated. This **Journal of Physical Chemistry C** article combines **DFT** and **classical molecular dynamics** to compare **hydration** of **β-C\(_2\)S** and **γ-C\(_2\)S**. The study computes **cleavage energies** for **low-index** surfaces, constructs **Wulff equilibrium morphologies**, maps **adsorption energy surfaces** for water, locates **transition-state** structures for **chemisorption** pathways, and runs **~2 ns** **room-temperature MD** to observe **spontaneous** surface reactions. The overarching thesis is that **reactive site density**—not only intrinsic **per-site** reactivity—controls net **hydration** kinetics for the polymorphs compared.

## Methods

**MD (ReaxFF):** **LAMMPS Reax/c** (build **1 Feb 2014**, Computational Details in `papers/ReaxFF_others/Wang_Manzano_JPCC_2015_CaSiO2.pdf`) simulates **β-** and **γ-C₂S** slabs with explicit **water** in **3D PBC** supercells; the article uses **external potential / dipole correction** language for charged slabs. Production segments are **NVT** at **300 K**, **0.2 fs** velocity-Verlet, **Nosé–Hoover** thermostat (**20 fs** damping), **~2 ns** trajectories on selected surfaces to capture **spontaneous** surface chemistry. No barostat, controlled pressure, electric field, or enhanced sampling is used for those **NVT** runs.

**Force-field training:** **N/A —** published **ReaxFF** parametrizations for **C–S–H / silicate** chemistry are cited and applied.

**Static QM / DFT:** **DMol³ GGA-PBE**, **DNP** basis, **5.5 Å** orbital cutoff; **Monkhorst–Pack** **1×2×1** (**β** slab) and **1×1×1** (**γ** slab); **external potential** in the vacuum region when needed to suppress spurious slab dipoles. **Dispersion:** **N/A —** the Computational Details block quoted in `papers/ReaxFF_others/Wang_Manzano_JPCC_2015_CaSiO2.pdf` does not specify an empirical dispersion add-on for **DMol³** (the article later contrasts accuracy with **plane-wave** literature that included **dispersive** corrections). Computed quantities include relaxed **β/γ** bulk (Table 1), **surface energies**, **Wulff** morphologies, **water adsorption** maps, and **NEB**-style pathways for water activation.

## Findings

**Water dissociation** proceeds via multi-step sequences (**rotation → dissociation → diffusion**) with **different barriers** on **β-** vs **γ-C₂S** facets. **γ-C₂S** can be locally more favorable for some elementary steps than **β-C₂S**, but **γ** exposes **far fewer reactive sites** on its **Wulff** shape, limiting **net hydration** and reconciling slower macroscopic kinetics with locally attractive chemistry (abstract and discussion). **Table 1** and related figures compare bulk and surface metrics to **experiment** and prior work. **Polymorph**, **facet**, and **reactive-site density** are the main explanatory knobs. Ideal **single-crystal** surfaces omit paste **pore fluid**, **alkali**, and **grain-boundary** effects in real cements. External **JPCC** reference—not a van Duin parametrization paper.

## Limitations

**Ideal surfaces** omit **grain boundaries**, **impurities**, and **alkali** chemistry present in real **cement** pastes.

## Reader notes (MAS / retrieval)

Use this page when the question mentions **β–γ belite differences**, **Wulff morphology**, or **water dissociation sequences** on **C\(_2\)S** surfaces; pair with cement microstructure pages for paste-scale context.

The **~2 ns** classical MD complements static barriers in the article.

## Relevance to group

**Cementitious silicate** simulation adjacent to group expertise in **oxide–water** interfaces and reactive modeling culture.

## Citations and evidence anchors

- **DOI:** `10.1021/acs.jpcc.5b05257` — `papers/ReaxFF_others/Wang_Manzano_JPCC_2015_CaSiO2.pdf`.

## Related topics

- [[reaxff-family]]
