---
id: paper:2018vashisth-polymer-158-effect-chemical
type: paper
title: 'Effect of chemical structure on thermo-mechanical properties of epoxy polymers:
  Comparison of accelerated ReaxFF simulations and experiments'
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:mechanics-tribology
- domain:organics-polymers-pyrolysis
- domain:reaxff-lineage
- material:polymer-organic
- method:reaxff
- task:experiment-integrated
- task:validation
- scale:atomistic
candidate_tags: []
paper_keywords:
- keyword:reaxff-application
- keyword:polymer
- keyword:validation-experiment
source_refs: []
doi: 10.1016/j.polymer.2018.11.005
year: 2018
authors:
- Aniruddh Vashisth
- Chowdhury Ashraf
- Charles E. Bakis
- Adri C. T. van Duin
venue: Polymer
pdf_sha256: 1e523d319a9ee43282c071af159e307f727f4d78bf2f2ade50d74598c7b503be
pdf_path: papers/Vashisth_Polymer_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018vashisth-polymer-158-effect-chemical -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The study applies an **accelerated ReaxFF** workflow—supplying energy comparable to **reaction barriers** so that **slow epoxy crosslinking** events occur on **MD-accessible** timescales—to build **atomistic networks** from **bisphenol-A epoxide** cured with **three classes of amines** (aromatic, cycloaliphatic, aliphatic). **Simulated thermo-mechanical** properties are compared with **experiments**, highlighting how **curing-agent chemistry** shapes **local heterogeneity** (notably for **cyclic** amines) and **strain-rate sensitivity** (stronger for **aliphatic** systems). **Adri C. T. van Duin** is a corresponding author with **Penn State** engineering coauthors. The workflow is explicitly aimed at industrial epoxide–amine networks where cure chemistry controls composite performance. **Thermoset** **design** often trades **Tg**, **toughness**, and **process window**; the paper argues those **macro** knobs have traceable **atomistic** signatures in **crosslink** **density** and **local** **strand** **stiffness**.

## Methods

### Reactive cross-linking and acceleration

**Accelerated ReaxFF** supplies **restraint energy** \(E_\mathrm{rest}\) on selected atom pairs (functional form eq. 2 in the article) so that successful **C–N** epoxy–amine cross-links occur on MD-accessible time scales; restraint parameters (**\(F_1,F_2,R_{12}\)** for **O–C**, **O–H**, **C–N** pairs) and **10 000** steps of **0.25 fs** per acceleration window are given in the **Polymer** Methods. The article states that **ADF** is used together with the **accelerated ReaxFF** cross-linking workflow (see their §2 and Fig. 2). **Stoichiometry** follows commercial cure ratios: **bisA/DETDA** and **bisA/IPDA** at **2:1** epoxide:amine, **bisA/T403** at **3:1**; systems are grown by **doubling** molecule counts as in the authors’ prior protocol. **Polymerization** stages use **accelerated NVT** runs at temperatures tied to the **final cure stage** of each formulation, with **Berendsen** thermostat (**100 fs** damping).

### Annealing, \(T_g\), CTE, and modulus (**LAMMPS**)

After cross-linking, **annealing** ramps **300 K → 600 K** in **100 K** steps with **12.5 ps** **NVT** or **NPT** segments (**0.25 fs** timestep); **Berendsen** thermostat (**100 fs**) and **Berendsen** barostat (**500 fs** damping) are used for the **NPT** portions. **Density vs temperature** for **\(T_g\)** uses **NPT** sweeps (**300 000** steps of **0.25 fs** per **20 °C** interval from **25 °C** to **325 °C**). **CTE** segments repeat **NPT** at **300–330 K** (**300 000** steps, **0.25 fs**). **Tensile tests** use **LAMMPS** `stress/atom` on relaxed networks (**ReaxFF**), with **multiple strain rates** as in the article and **Poisson**-relaxed lateral faces (**ν = 0.5** where cited). All relaxed **epoxy** cells are treated as **bulk** systems with **three-dimensional periodic boundary conditions** in **LAMMPS** (**PBC** on the packed networks).

### Experiments

**Cure schedules**, **MDSC** glass transitions, **density**, and **modulus** follow **Table 1–2** in the paper (mix ratios and temperature windows for **bisA/DETDA**, **bisA/IPDA**, **bisA/T403**).

- **Replica / umbrella / metadynamics:** **N/A — not used** (acceleration is **restraint-based** as above).

- **External electric field:** **N/A — not used**.
## Findings

- **Good correlation** between **simulation** and **experiment** for the **thermo-mechanical** trends compared in the study.
- **Cyclic** curing agents yield **heterogeneous** local structure that **annealing** can partly homogenize; **aliphatic** networks show more **strain-rate** dependence than **aromatic**-cured analogs in the simulations reported, linking cure-agent ring strain to mechanical dispersion.
- The authors relate **modulus** shifts to **free-volume**-like indicators in the **simulated** **cells**, helping interpret why **β**-trends differ across **amine** families.

- **Corpus honesty:** Tabulated moduli, **\(T_g\)**, and **CTE** comparisons are authoritative in **`papers/Vashisth_Polymer_2018.pdf`**; this note is a navigation summary.
## Limitations

- **Accelerated dynamics** changes **pathway competition** relative to **room-temperature** processing; **quantitative** cure kinetics remain **illustrative**.
- **Force-field** scope limits **transfer** to other **epoxide/amine** chemistries without **re-parameterization**.
- Virtual mechanical tests on nanoscale cells omit fiber reinforcement, voids, and interphase regions present in composite coupons, so moduli comparisons should be read as chemistry-controlled trends within the simulated network class rather than drop-in predictions for full laminate stacks.

## Relevance to group

Demonstrates **group ReaxFF** on **thermoset cure** with **side-by-side validation**, relevant to **polymer composites** and **industrial** processing questions.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.polymer.2018.11.005` (`papers/Vashisth_Polymer_2018.pdf`).

## Reader notes (navigation)

- Thermoset cure with **accelerated ReaxFF**; polymer + composite cluster: [[theme-pyrolysis-combustion-organics]] (organics hub).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
