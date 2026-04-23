---
id: paper:2017yeon-venue-am6b14159
type: paper
title: "Mechanochemistry at Solid Surfaces: Polymerization of Adsorbed Molecules by Mechanical Shear at Tribological Interfaces"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:polymer
  - keyword:validation-experiment
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.6b14159"
year: 2017
authors:
  - "Jejoon Yeon"
  - "Xin He"
  - "Ashlie Martini"
  - "Seong H. Kim"
venue: "ACS Applied Materials & Interfaces (2017)"
pdf_sha256: "5c1b30edfc9b91c44646a3a368a03a1ab62c4a9e275ad732878fff9d9f83c395"
pdf_path: "papers/ReaxFF_others/Yeon_Mechanochem_ACSAMI_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017yeon-venue-am6b14159 -->

## Summary

Tribochemical reactions can produce polymeric films at sliding interfaces from small molecules that would not polymerize rapidly under thermal activation alone. This ACS Applied Materials & Interfaces article couples vapor-phase lubrication experiments on allyl alcohol with ReaxFF molecular dynamics in which adsorbates are sheared against a hydroxylated silica surface under tunable normal load. The experimental side measures product formation as a function of mechanical load in a tribometer configuration; the simulation side resolves bond formation events, including carbon–carbon coupling consistent with polymerization, under shear. The authors interpret agreement between load-dependent product trends in experiment and simulation as evidence that the modeled atomistic pathways lie in the same mechanochemical regime as the laboratory setup, and they contrast shear-driven polymerization with purely thermal or photochemical polymerization scenarios. Silicon oxide is a common tribopair material in microelectromechanical systems; the study’s focus on alcohol chemistry at oxide surfaces connects to lubrication challenges beyond academic model contacts.

## Methods

**Experiments (tribology).** **Vapor-phase lubrication** tribometer tests shear **allyl alcohol** films on **hydroxylated silicon oxide** under controlled **normal load** with negligible frictional heating and wear (per the article’s Supporting Information discussion excerpted in the introduction), so **thermal**, plasma, and electrochemical pathways are argued to be minor compared with **mechanochemical** shear.

**Molecular dynamics (reactive).** **Computational molecular dynamics** simulations use **ReaxFF** so large **oxide**/organic **slabs** containing many **atoms** and explicit **molecules** can evolve bonds under **dynamic** shear. The authors compare the slope of **ln(reaction yield)** **versus** **contact pressure** between **experiment** and simulation to argue the atomistic trajectories occupy the same **mechanically assisted thermal reaction** regime discussed analytically in the paper. **Periodic** supercell conventions, **timestep** (fs), **NVT**/**NPT** choices, **thermostat**/**barostat** parameters, **equilibration**/**production** **duration** (ps/ns), and **sliding velocity** magnitudes are specified in **ACS Appl. Mater. Interfaces** **2017**, **9**, **3142–3148** and should be read from **`papers/ReaxFF_others/Yeon_Mechanochem_ACSAMI_2017.pdf`** rather than this summary. **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** highlighted in the indexed excerpt.

**Force-field fitting.** **N/A —** the manuscript cites established **ReaxFF** parameterizations for **Si/O/C/H** tribochemistry; no new **training** loop is summarized on the excerpted pages.

**Static QM / DFT.** **N/A —** production interface modeling is **ReaxFF MD**, not on-the-fly **DFT**.

**Review scope.** **N/A —** integrated **experiment** + simulation research article.

## Findings

**Outcomes and mechanisms.** **Shear** at the **hydroxylated silica** interface promotes **C–C coupling** among **allyl alcohol** moieties consistent with **polymerization**, with atomistic pathways described as distinct from conventional radical **polymerization** because **mechanical distortion** of **anchored** **reactants** enables association under mild **thermal** conditions.

**Comparisons.** **Experimental** product trends **versus** **normal load** align with **simulated** **pressure** dependence of reaction yields, supporting the relevance of the modeled **interface** chemistry to **vapor-phase lubrication** tribometry.

**Sensitivity / design levers.** **Contact pressure** (or **stress**) emerges as the shared control knob linking **experiment** and **simulation**; the Arrhenius-style mechanochemical discussion emphasizes how mechanical terms enter alongside **temperature** in effective barrier-crossing pictures.

**Limitations / outlook.** Industrial lubricants include additives and roughness beyond the idealized **oxide**/monomer models; **ReaxFF** organic barriers remain approximate.

**Corpus honesty.** Detailed protocol numerics and figure-level yields are in the **PDF** at `pdf_path`; the local extract covers motivation plus the **MD**/**experiment** validation logic through the early methods narrative.
## Limitations

Industrial vapor-phase lubricant formulations include additives and roughness not modeled atomistically. ReaxFF barrier heights for organic coupling are approximate; long-chain desorption and wear particle formation require larger or multiscale models.

## Relevance to group

Template for combining ReaxFF with experimental tribology to validate interface chemistry models under load.

## Citations and evidence anchors

- DOI: [10.1021/acsami.6b14159](https://doi.org/10.1021/acsami.6b14159)

## Related topics

- [[reaxff-family]]
- [[2017wen-computationa-atomistic-mechanisms]]
