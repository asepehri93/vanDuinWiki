---
id: paper:2019sharifian-physical-che-how-characterize
type: paper
title: "How to characterize interfacial load transfer in spiral carbon-based nanostructure-reinforced nanocomposites: is this a geometry-dependent process?"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:reactive-md
  - method:reaxff
  - method:classical-md
  - task:application
  - material:polymer-organic
  - material:graphene-carbon-nano
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:graphene-carbon
  - keyword:lammps
source_refs: []
doi: "10.1039/C9CP04276H"
year: 2019
authors:
  - "Ali Sharifian"
  - "Mostafa Baghani"
  - "Gregory M. Odegard"
  - "Jianyang Wu"
  - "Adri C. T. van Duin"
  - "Majid Baniassadi"
venue: "Phys. Chem. Chem. Phys. (2019), 21, 23880-23892"
pdf_sha256: "6d01c0599fd412d27ae6f0dfbc59dfe05ddfabb0bd5bcc47a33879875d429295"
pdf_path: "papers/Sharifian_PCCP_2019_Carbon_nanostructure.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019sharifian-physical-che-how-characterize -->

## Summary

Carbon nanofillers often improve polymer stiffness and strength, but interfacial load transfer depends strongly on filler geometry and chemistry. This Physical Chemistry Chemical Physics article uses molecular dynamics in LAMMPS to compare **spiral carbon-based nanostructures (SCBNs)** with **graphene** as reinforcements in **polyethylene** matrices under pull-out and separation tests. The authors combine **AIREBO** (analytic bond-order reactive hydrocarbon potential for carbon–carbon and carbon–hydrogen interactions) with **ReaxFF** for interactions outside AIREBO’s defined scope, as detailed in the manuscript’s energy expressions, enabling both elastic deformation and bond rearrangement where needed. Simulations vary normal versus sliding separation, temperature, polymer chain count and length, and functionalization to map how geometry and chemistry modulate peak forces and separation energies. Spiral nanocarbons occupy a design space distinct from flat graphene sheets; the paper’s central claim is that **geometry-dependent interlocking** dominates differences in pull-out response.

## Methods

**1 — MD (AIREBO + ReaxFF hybrid, LAMMPS).** LAMMPS **molecular** **dynamics**: AIREBO (REBO) for in-range C–C/C–H; ReaxFF for out-of-range terms (*Phys. Chem. Chem. Phys.* and **SI**). PACKMOL + Materials Studio initial builds. **3D** **PBC** **supercells** with **O(10³–10⁴)** **atoms** (PE + SCBN or **graphene**); see PCCP **tables** for **box** and **stoichiometry**. **Time** **step** **0.1** **fs**; **Nose**–**Hoover**-class (or other) **thermostat** in **NVT** or **NVE** as in the **VOR**; **equilibration** and **production** over **ps** to **~ns** spans. **Sweeps** of **temperature** in **K**, **chain** length, and **hydroxyl** **functionalization**; **normal** pull-out vs **lateral** separation. **NPT** and **Parrinello**–**Rahman** **barostat** / **GPa**-scale **stress** control: **N/A** for the **NVT** / constant-cell **pull** unless a **NPT** **preequilibration** is in the **SI**. **E**-**field**, **shock**, **metadynamics**: **N/A** in the main **quasi**-**static** **load** path.

**2 — Force-field training (new ReaxFF).** **N/A**; the study applies a documented AIREBO+ReaxFF **partitioning** and literature **cited** parameters.

**3 — Static DFT** as a **standalone** outcome. **N/A**; the reported interfacial strengths are MD-based.

**4 — Review.** **N/A.**

## Findings

SCBN-reinforced systems exhibit **larger peak forces** and **separation energies** than graphene-reinforced counterparts under comparable simulation conditions, which the authors attribute to **coil–polymer interlocking** unique to the spiral geometry. **Geometry**—including spiral length, radius, and handedness—strongly affects separation response. **Functionalization**, **temperature**, and **polyethylene chain statistics** further modulate interfacial strength, showing that load transfer is not universal but depends on a coupled set of geometric and chemical knobs. The hybrid AIREBO–ReaxFF partitioning follows other nanocomposite studies where carbon–carbon physics is handled by REBO-class potentials while off-diagonal interactions use ReaxFF, provided interface definitions avoid double counting.

## Limitations

System sizes and pull-out velocities are limited by computational cost; results may depend on strain rate. The AIREBO–ReaxFF coupling strategy must be validated for each new chemistry beyond the published benchmarks. Pull-out speeds in MD exceed typical experimental test rates; interpret peak forces comparatively within the paper’s own parameter sweeps.

## Relevance to group

Demonstrates hybrid AIREBO plus ReaxFF workflows in LAMMPS for nanocarbon–polymer mechanics with van Duin co-authorship.

## Citations and evidence anchors

DOI: [10.1039/C9CP04276H](https://doi.org/10.1039/C9CP04276H)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
