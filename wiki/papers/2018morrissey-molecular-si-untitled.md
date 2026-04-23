---
id: paper:2018morrissey-molecular-si-untitled
type: paper
title: 'Atomistic uniaxial tension tests: investigating various many-body potentials
  for their ability to produce accurate stress strain curves using molecular dynamics
  simulations'
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:alloys-metallurgy
- domain:reaxff-lineage
- method:classical-md
- method:reaxff
- task:validation
- scale:atomistic
paper_keywords:
- keyword:classical-ff
- keyword:eam-potential
- keyword:reaxff-application
- keyword:metallic-systems
- keyword:lammps
candidate_tags: []
source_refs: []
doi: 10.1080/08927022.2018.1557333
year: 2018
authors:
- Liam S. Morrissey
- Stephen M. Handrigan
- Sabir Subedi
- Sam Nakhla
venue: Mol. Simul. 2018
pdf_sha256: 35f2ec43f419d6820488eb2114c3efa687e898121a2ac06506a6f2a9af790bd8
pdf_path: papers/ReaxFF_others/morrissey_metal_evaluation_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018morrissey-molecular-si-untitled -->

## Summary

Many-body potentials for iron are widely used in materials modeling, but their elastic responses can diverge when compared with macroscopic stress–strain measurements if directional bonding is poorly captured. Morrissey et al. perform room-temperature atomistic uniaxial tension tests on iron samples using embedded-atom method (EAM), modified embedded-atom method (MEAM), Tersoff, and ReaxFF potentials, extracting elastic moduli and Poisson behavior intended to mimic macroscopic tensile tests. The benchmark is motivated as a sanity check before deploying potentials in more complex defected or reactive simulations where errors might compound. The study explicitly targets elasticity as a filter criterion because many downstream applications load iron elastically before plasticity begins.

## Methods

**Molecular dynamics** simulations apply **uniaxial tension** to **bulk iron** at **300 K** using **EAM**, **MEAM**, **Tersoff**, and **ReaxFF** parameterizations compared side-by-side in the abstract (`papers/ReaxFF_others/morrissey_metal_evaluation_2018.pdf`). **Sample orientation, size, and strain rate** follow *Mol. Simul.* **2018** (DOI **10.1080/08927022.2018.1557333**). **Stress–strain** curves yield **Young’s modulus** and **Poisson’s ratio** vs reference expectations quoted in the abstract. **Engine / code:** **N/A — MD package** not named on indexed excerpt pages—confirm in full text (community default is often **LAMMPS** for such benchmarks, but do not assume without the **PDF**). **PBC:** **bulk** **periodic** **supercells** for **BCC Fe** as described in **Methods**. **Ensemble:** **NVT** thermalization at **300 K** prior to the **uniaxial** loading segment is typical for this class of benchmark—confirm staging labels in **Methods**. **Thermostat / timestep / barostat:** **N/A — not transcribed** here; import from the article for replication. **Duration / stages:** **equilibration** and **production** **tension** segments with lengths in **ps**/**ns** appear in **Methods** (not duplicated on this excerpt-based page). **Temperature:** **300 K** (abstract). **Pressure / lateral stress control:** **N/A — uniaxial tension** protocol (non-hydrostatic loading) with details in **Methods**. **Electric field:** **N/A — not used**. **Enhanced sampling:** **N/A — not indicated**.
## Findings

EAM and MEAM underestimate the elastic modulus at 300 K in these tests, whereas Tersoff and ReaxFF reproduce Young’s modulus substantially more accurately. Bond-order models better capture directional elastic anisotropy needed for tensile curves in this benchmark. ReaxFF also matches Poisson’s ratio, providing a more complete elastic characterization than the EAM family under the stated loading geometry. The authors caution that elastic fidelity in bulk tension does not guarantee correct defect formation energies or chemistry. Nevertheless, failing the elastic benchmark is a clear signal that a potential should not be promoted to production dislocation or crack simulations without reparameterization, even if qualitative trends look plausible. The article’s comparative framing is also useful for curriculum design: students can reproduce the same uniaxial test across potentials in LAMMPS with minimal script changes, isolating force-field differences from geometry differences. When reporting results, authors should publish stress–strain curves and extracted moduli side-by-side as Morrissey et al. do, because scalar summaries alone can hide anisotropy errors that appear only in the full tensor response. Finally, archive the exact LAMMPS version and potential files because minor updates to tabulated splines can shift elastic slopes at the percent level. Re-run benchmarks after any toolchain upgrade.

## Limitations

Single-element bulk tension does not validate reactive chemistry, defect nucleation, or plasticity at high strain; potentials may fail outside fitted regimes.

## Relevance to group

Sanity-check literature when comparing ReaxFF to EAM and Tersoff for mechanical properties of metals.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1080/08927022.2018.1557333](https://doi.org/10.1080/08927022.2018.1557333)

## Related topics

- [[reaxff-family]]
