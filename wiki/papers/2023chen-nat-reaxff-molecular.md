---
id: paper:2023chen-nat-reaxff-molecular
type: paper
title: "ReaxFF molecular dynamics simulation and experimental validation about chemical reactions of water and alcohols on SiC surface"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - task:experiment-integrated
  - material:widegap-semiconductor
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:oxide-surface
  - keyword:validation-experiment
source_refs: []
doi: "10.1016/j.ceramint.2023.11.070"
year: 2024
authors:
  - "Haibo Chen"
  - "Jiapeng Chen"
  - "Jiexiong Wu"
  - "Juanfen Shen"
  - "Yunyun Gu"
  - "Tao Sun"
venue: "Ceramics International 50, 4332–4349 (2024)"
pdf_sha256: "a796cd1836444bf547e77ca0bf123e03815227b7b953c008b372d26801b612f2"
pdf_path: "papers/ReaxFF_others/Chen_SiC_water_alcohol_Ceramics_Int_2024.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2023chen-nat-reaxff-molecular -->

## Summary

Chemical–mechanical polishing of silicon carbide involves complex chemo-mechanical interactions between the wide-gap surface and slurry species. This study combines ReaxFF molecular dynamics of water and alcohols at 6H–SiC (001) surfaces with polishing experiments that measure removal rates and surface characterization via atomic force microscopy and XPS. The authors articulate a three-stage oxidation narrative: initial approach and reaction with undercoordinated surface sites, Si–C bond weakening mediated by adsorbed solvent species, and migration of hydrogen and hydroxyl species that promotes Si–O–Si network formation. The simulated relative reactivity of solvents is compared directly to experimental removal-rate ordering.

## Methods

### ReaxFF interface simulations (B)

- **Surface:** **6H–SiC (001)** exposed to **explicit water** or **alcohol** molecules at coverages relevant to **CMP** slurry chemistry.
- **Potential:** **ReaxFF** parametrization for **Si–C–O–H** surface reactions (training/validation context in *Ceramics International* **Methods**).
- **Numerics:** **Cell sizes**, **temperatures**, **durations**, **ensemble**, and **timestep** are listed in the article/SI—**not duplicated** here.

### Experiments (CMP + characterization)

- **CMP:** **Material removal rate** measurements under conditions designed to isolate **chemical** contributions emphasized by simulation.
- **Surface science:** **AFM** (**roughness**/morphology) and **XPS** (**oxidation states**) on polished coupons.

### Multiscale interpretation

Simulations address **near-surface chemistry**; experiments integrate **abrasion**, **fluid transport**, and **particle** effects—matches are therefore **qualitative** along the **reactivity ordering** axis.

### MD application (integrated)

**Engine / code:** **LAMMPS** with **ReaxFF** for **6H–SiC (001)** + **water** or **alcohols**. **System & composition:** **slab** + **molecular** **coverage** in *Ceramics International*; **N/A — atom counts, supercell, fixed layers** on this stub (see paper). **PBC** in **in-plane** directions; bottom **SiC** **layers** may be **fixed** per the article. **Ensemble**, **timestep**, **NVT**/**NPT** stages, **duration**, **thermostat**/**barostat**, **temperature** setpoints (e.g. room-temperature MD), **pressure**, **electrostatics** cutoffs, **QEq** frequency: in **full PDF**; **N/A — exact numbers not duplicated here**. **N/A — macroscopic applied electric field** in the MD (CMP bias is not the atomistic model); **N/A — umbrella/metadynamics/REX.**

## Findings

### Reactivity vs removal-rate ordering

The **relative chemical reactivity** ordering of **water** and several **alcohols** toward **SiC** matches the **experimental removal-rate** ordering under the authors’ test matrix.

### Three-stage oxidation narrative

**Adsorption → Si–C activation → oxide network formation** via **hydroxyl/H migration** provides a mechanistic scaffold for **chemically assisted** removal beyond pure **abrasion**.

### Characterization link

**AFM** and **XPS** connect simulated **trends** to **measurable** **roughness** and **oxidation** shifts, arguing solvent chemistry modulates the **near-surface oxide** rather than only **lubricating** **particle** contact.

### Practical caveat

Full **CMP** prediction still requires **particle** hardness, **pad** mechanics, and **flow**—outside the atomistic solvent–surface model.

## Limitations

Simulations omit full slurry chemistry, particle abrasion, and fluid flow fields present in industrial CMP; ReaxFF remains approximate for wide-gap semiconductor oxidation and radical chemistry at elevated stress.

## Corpus notes

If `normalized/papers/*.json` still lists a 2023 acceptance date while the venue line reads 2024, prefer the bibliographic block in this wiki (peer-reviewed issue pages) when resolving citations for downstream pipelines.

## Relevance to group

Application-oriented **ReaxFF** benchmarking for **SiC** surface chemistry with experimental validation.

## Citations and evidence anchors

- DOI: [10.1016/j.ceramint.2023.11.070](https://doi.org/10.1016/j.ceramint.2023.11.070)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
