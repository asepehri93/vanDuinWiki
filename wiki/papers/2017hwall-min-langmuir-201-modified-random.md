---
id: paper:2017hwall-min-langmuir-201-modified-random
type: paper
title: "Modified Random Sequential Adsorption Model for Understanding Kinetics of Proteins Adsorption at a Liquid–Solid Interface"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:metallic-systems
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
  - keyword:validation-experiment
  - keyword:polymer
candidate_tags: []
source_refs: []
doi: "10.1021/acs.langmuir.7b00523"
year: 2017
authors:
  - "Hwall Min"
  - "Eugene Freeman"
  - "Weiwei Zhang"
  - "Chowdhury Ashraf"
  - "David Allara"
  - "Adri C. T. van Duin"
  - "Srinivas Tadigadapa"
venue: "Langmuir (2017), 33, 7215–7224"
pdf_sha256: "e0163c72641eb835ce606d989e80bb2f2e9205cc44d7494465b97a3052926fdf"
pdf_path: "papers/Min_Protein_Gold_Langmuir_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017hwall-min-langmuir-201-modified-random -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below (**Summary**, **Methods**, **Findings**) summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For fitted kinetic parameters, RSA derivations, and MD setup details, rely on the peer-reviewed article.

## Summary

Human serum albumin (HSA) adsorption on a **hydrophobic hexadecanethiolated gold** surface is measured in real time with **83 MHz micromachined quartz crystal resonators**, comparing single-injection and multi-injection protocols at the **same final bulk concentration**. The measured kinetics show **RSA-like jamming** at long times together with a slowdown that standard random sequential adsorption (RSA) transport models do not fully capture. The authors introduce an **interface-depletion modified RSA** picture with an exponentially depleting interfacial supply. Complementary **ReaxFF molecular dynamics** of a thiolated gold surface with explicit water supports **preferred interfacial orientation** of adsorbed protein segments and a **strongly reduced lateral diffusion coefficient** in the interfacial layer; coupling faster surface attachment to slower interfacial diffusion rationalizes the **depleted interfacial concentration** and the observed **slowdown** relative to bulk-limited uptake.

## Methods

**A — Force-field training / fitting:** **ReaxFF** for **Au–S–C–H–O** **thiolated gold** / **aqueous** interfaces as used in the article (**no** new parameter fit summarized on this page).

**B — Molecular dynamics / sampling:** **ReaxFF MD** (**LAMMPS**) of **hexadecanethiol**-covered **Au** with **explicit water** and **reduced HSA** representation; staged **equilibration** then **400 ps** production (**analysis** **last 200 ps**). **NVT**, **298.15 K**, **0.25 fs**, **Berendsen** thermostat (**100 fs** damping).

**C — DFT / static QM:** **Not** the primary layer for adsorption trajectories summarized here.

**D — Review / non-simulation framing:** **Experiment:** **83 MHz** **QCM** **real-time** **HSA** adsorption on **hydrophobic** **thiol/Au**; **single- vs multi-injection** at matched **final** **concentration**; **RSA**/**jamming**-limit coverage.

**Engine:** **LAMMPS** **ReaxFF** as above. **System:** **hexadecanethiol**-covered **Au** with **explicit water** and a **reduced HSA** representation; **atom counts** are given in the **Langmuir** article. **Boundaries / periodicity:** **3D PBC** is the default for this class of **thiol/Au** **aqueous** **slab** models; confirm **frozen** vs mobile **Au** layers in **`pdf_path`**. **Ensemble / thermostat / timestep / duration:** **NVT**, **298.15 K**, **0.25 fs**, **Berendsen** thermostat (**100 fs** damping), **400 ps** production (**analysis** on **last 200 ps**) after staged **equilibration** as in **Methods**. **Barostat / pressure:** **N/A —** **NVT** **constant-volume** interfacial cell; no **NPT** segment reported for the production **MD**. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

## Findings

Experimental transients are described with the proposed **interface-depletion RSA** framework (exponential depletion of the interfacial layer). ReaxFF trajectories indicate **specific adsorption orientation** at the thiolated interface and **markedly reduced** in-layer **diffusion** versus bulk-like behavior, supporting the idea that **reduced interfacial diffusivity** and **adsorption rate** together produce **interfacial depletion** and the **slowed** HSA uptake observed on the hydrophobic surface.

## Limitations

- Atomistic modeling uses a **reduced representation** of HSA (segments / simplified geometry as in the paper), not full all-atom protein at experimental size; quantitative diffusion coefficients are **model-dependent**.
- Classical reactive MD cannot capture all **conformational** and **electrostatic** details of soft biological adsorption without experimental or higher-level benchmarks.

## Relevance to group

Includes **Adri C. T. van Duin** as co-author; demonstrates **ReaxFF** at **biomolecule–metal–aqueous** interfaces paired with **microgravimetric** kinetics.

## Citations and evidence anchors

- DOI: [10.1021/acs.langmuir.7b00523](https://doi.org/10.1021/acs.langmuir.7b00523)

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Protein / interface and biosensor-adjacent work: cross-link from [[paper-index-by-domain]] or theme hubs as the corpus grows.
