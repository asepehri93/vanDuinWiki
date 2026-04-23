---
id: paper:20190000-0003-0042-5108-j-phys-chem-multiple-objective
type: paper
title: Multiple Objective NSGA-II-Based Optimization Program and Its Application in
  Reactive Force Field for 2,4,6-Trinitrotoluene Diffusion in the Aqueous Phase
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:reaxff-lineage
- domain:organics-polymers-pyrolysis
- method:reaxff
- task:parameterization
- task:method-development
- scale:atomistic
paper_keywords:
- keyword:reaxff-parameterization
- keyword:energetic-materials
- keyword:water-interfaces
- keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpcc.9b05036
year: 2019
authors:
- Guan Zhang
- Jin Li
- Zongkuan Liu
venue: J. Phys. Chem. C
pdf_sha256: be1baa356850a03a56c5eb2abdcb0e01da8bf6166c302849baca703e1750f66a
pdf_path: papers/ReaxFF_others/Guan_Zhang_JPCC_2019_TNT_Garfield.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:20190000-0003-0042-5108-j-phys-chem-multiple-objective -->

## Summary

**2,4,6-trinitrotoluene (TNT)** environmental chemistry couples **solid-state** packing with **aqueous reaction** pathways that are difficult to probe atomistically without reactive potentials. **Zhang**, **Li**, and **Liu** introduce **MONOP**, a **multi-objective genetic** optimizer patterned on **NSGA-II**, to **retrain** **ReaxFF** parameters for **TNT in liquid water** beginning from the community **CHON-2017_weak** parent set. The objective landscape mixes **crystallographic** observables for **TNT** with **liquid-structure** metrics so the optimizer cannot sacrifice lattice fidelity to fix water alone. A parallel **mean-square displacement (MSD)** analysis compares **TNT** translational diffusion to **hydroxide** mobility to interrogate whether **hydrolysis** is limited by **bulk transport** or **interfacial attack**.

## Methods

**MONOP** evolves populations of **ReaxFF** parameter vectors under **Pareto** selection, updating generations until multi-objective tolerances are met—the abstract cites convergence near **11 generations** for this application. Each candidate undergoes **TNT crystal** simulations to extract **lattice constants (a, b, c)**, **mass density**, and **element–element radial distribution functions**, stacked against the same benchmarks for **CHON-2017_weak** and **ReaxFF-lg** references. **Liquid-phase** cells evaluate **water density** and **transport** statistics. **MSD** curves for **TNT** and **OH⁻** are accumulated from **NVT**-style production segments at states specified in the article, enabling qualitative rate comparisons without invoking full reactive rare-event sampling for every channel.

**Force-field training.** **MONOP** is a multi-objective **NSGA-II**-style **genetic algorithm** optimizer applied to **ReaxFF** parameters for **TNT**/**water**, starting from **CHON-2017_weak** as the parent **parameter set**. **QM**/**DFT** training references and **experiment** targets for **crystal** **lattice** metrics and **liquid water density** are defined in the article and **Supporting Information**; **parameter optimization** balances those objectives on the **Pareto** front rather than a single **least-squares** score.

**MD application (article §2–3).** **Engine / code:** **ReaxFF** **molecular dynamics** driven through **MATLAB**-orchestrated **parallel** **LAMMPS** in the **MONOP** workflow. **Ensemble / stages:** **NVT** and **NPT** **MD** as labeled in the **Methods**; for all **MD** runs, **timestep 0.25 fs**; **Berendsen** **thermostat**; the **Methods** line after the **0.25 fs** **timestep** gives paired **damping** **constants** **500 fs** and **10 fs** for **NVT** vs **NPT** **MD** **segments** (read the **PDF** wording—this summary does not reassign which constant applies to **pressure** vs **temperature**). **RDF** benchmarks: **TNT** **crystal** runs of **~25 ps** **total** time; **RDF** averaged every **50 timesteps** over the **last 20 ps** with **lattice** constants and **density** from that window. **Liquid** **box:** **NPT** **relax** **~25 ps**, then **~75 ps** **production** for **water** **RDF** pairs. **MSD:** after **NPT** **equilibration** of the **aqueous** **cell**, **NVT** **MSD** **analysis** compares **TNT** and **OH⁻** **migration** (see **Results** / **Figure 6**). **System / PBC:** **PBC** **TNT** **crystal** and **TNT**/**water** **liquid** **supercells** with **atom** totals given in the **SI**/**Methods** tables; **~100 K** **crystal** **RDF** **verification** reduces **thermal** **noise**, while **room-temperature** **aqueous** **cells** feed **liquid** metrics and **MSD** analysis. **Electric field / enhanced sampling:** **N/A —** **NSGA-II** is the outer **search**, not **metadynamics**.
## Findings

**MONOP** reaches competitive **Pareto** fronts quickly, indicating that **NSGA-II**-style search pairs well with **ReaxFF**’s moderate-dimensional parameter tweaks when observables are well posed. The optimized **TNT/water** parameterization reproduces **TNT** **crystal** metrics closely while leaving **liquid water density** **modestly high** relative to experiment, a common stress test for **CHON** water subsets. **MSD** analysis reports **TNT** diffusion **orders of magnitude slower** than **OH⁻** transport, supporting a mechanistic picture where **interfacial hydroxide attack** gates **hydrolysis** rather than **bulk TNT** migration. Operators should cross-check **barriers** for specific **reaction channels** with **QM** because genetic fits can overfit tabulated observables. The Xi’an Jiaotong authorship line situates the work as an external consumer of **CHON-2017_weak** parameters; reproducibility requires archiving the exact MONOP parameter files alongside the published force-field tables.

## Limitations

External **Monte Carlo** / **genetic** optimization can overfit **training observables**; validate **reaction pathways** independently with **QM**. **Xi'an Jiaotong** authorship—method is adjacent to, but not authored inside, the Penn State **CHON-2017_weak** line.

## Relevance to group

Demonstrates downstream **reuse of CHON-2017_weak** for **energetic-material aqueous chemistry** and automated **multi-objective ReaxFF** tuning.

## Citations and evidence anchors

<!-- Prefer DOI link when `doi` is present in frontmatter. -->

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
