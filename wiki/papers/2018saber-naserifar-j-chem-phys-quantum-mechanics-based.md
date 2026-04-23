---
id: paper:2018saber-naserifar-j-chem-phys-quantum-mechanics-based
type: paper
title: The quantum mechanics-based polarizable force field for water simulations
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:water-silica-geo
- domain:classical-ff-specialized
- method:classical-md
- task:parameterization
- task:validation
- scale:atomistic
paper_keywords:
- keyword:polarizable-ff
- keyword:charge-equilibration
- keyword:water-interfaces
- keyword:dft-static
candidate_tags: []
source_refs: []
doi: 10.1063/1.5042658
year: 2018
authors:
- Saber Naserifar
- William A. Goddard III
venue: J. Chem. Phys.
pdf_sha256: 0adf94309484002002aeab5cc9f3541ef6c96f1c38316d8e3ad359a3b1e3a2ae
pdf_path: papers/Others/JCP-RexPoN_forcefield.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018saber-naserifar-j-chem-phys-quantum-mechanics-based -->

## Summary

**RexPoN** is a polarizable molecular-mechanics water potential whose parameters are fit entirely to quantum data rather than empirical liquid properties. **Naserifar** and **Goddard III** assemble **coupled-cluster CCSD(T)** energies for the **water dimer** across **distances** and **orientations**, **X3LYP** energies for **19** larger **clusters** capturing **many-body** polarization, **fluctuating charges** via a **polarizable charge-equilibration** formalism, and **DFT-D3** **dispersion** references anchored to **H\(_2\)** and **O\(_2\)** **crystals**. The **JCP** article situates **RexPoN** within **Goddard**-school **FF** development where **QM** **training** **data** are **preferred** over **empirical** **liquid** **fits**, trading **lower** **computational** **cost** than **explicit** **QM** **solvent** for **higher** **fidelity** than **fixed-charge** **water** models in **hybrid** **pipelines**. The resulting field reproduces **melting point**, **298 K** **density**, **heat of vaporization**, **entropy**, **dielectric constant**, and **self-diffusivity** near **experiment** without **post hoc** scaling to **experimental** **densities**.

## Methods
**1 — MD application (RexPoN validation).** After integrating **RexPoN** into **LAMMPS**, the authors run **liquid water** benchmarks (e.g., **216** molecules/cell at **298 K**) and **ice melting** studies. Protocol excerpts in *J. Chem. Phys.* include **NPT** equilibration segments (**~1 ns**), **NVT** segments (**150 ps** blocks), and **NPT** relaxations (**120 ps**) feeding two-phase thermodynamics analysis, followed by additional **NVT** cycles for analysis windows (**100 ps** total split into **5 × 20 ps** in the excerpt). **Thermostat:** **Nosé–Hoover** with **100 fs** damping (rigid water unless noted otherwise in their rigid-molecule discussion). **Barostat:** **relaxation time ~1 ps** for **pressure** control in **NPT** melting studies. **Timestep:** **1.0 fs** for the reported RexPoN **LAMMPS** validation and melting workflows (the article notes **2.0 fs** would likely be acceptable but was not used for the quoted benchmarks). **PBC:** **three-dimensional PBC** for bulk water cells. **Electric fields / enhanced sampling:** **N/A —** not used in the benchmark suite summarized here.

**2 — Force-field training (RexPoN).** **Parent / functional form:** new **RexPoN** polarizable water model (not **ReaxFF**). **QM reference:** **CCSD(T)** dimer surfaces across orientations/distances; **X3LYP DFT** on **19** larger clusters; **DFT-D3** dispersion coefficients anchored to **H₂** and **O₂** molecular crystals. **Training set:** dimer + cluster **binding**/**polarization** manifolds described in **Section II**. **Optimization:** parameters determined to reproduce **QM** many-body energies while retaining efficient **MD** (see energy decomposition and **PQEq** coupling in the article). **Reference data:** compared against **experimental** melting (**273.15 K** target), **298 K** **density**, **ΔH_vap**, **entropy**, **dielectric constant**, and **ln D_s** tabulated in the abstract.

**3 — Reactive ReaxFF MD.** **N/A —** this paper is **not** a **ReaxFF** reactive study.

## Findings
**Outcomes / mechanisms:** **RexPoN** reproduces **ice melting** near **273.3 K** (cf. **273.15 K** experiment) and **298 K liquid** benchmarks (**density**, **ΔH_vap**, **entropy**, **dielectric constant**, **ln D_s**) close to experiment **without** empirical liquid refitting.

**Comparisons:** metrics are compared explicitly to **experimental** values listed in the abstract.

**Sensitivity / outlook:** accuracy comes at higher cost than **TIP3P**-class models; **electrolyte** and **reactive interface** extensions are flagged as needing future validation.

**Limitations:** rigid-water approximations in parts of the workflow and **2PT**-based analysis windows depend on the detailed **Methods** sections.

**Corpus honesty:** benchmark numbers are taken from the **JCP** abstract on `papers/Others/JCP-RexPoN_forcefield.pdf`; this page is **not ReaxFF** despite the wiki’s optional **Related topics** link.

## Limitations

Not a ReaxFF model; transferability to electrolyte or reactive interfaces requires separate validation. Computational cost exceeds fixed-charge water models.

## Relevance to group

Complementary polarizable water FF literature adjacent to ReaxFF/eReaxFF aqueous workflows.

## Citations and evidence anchors

- DOI: [10.1063/1.5042658](https://doi.org/10.1063/1.5042658)

## Related topics

- [[reaxff-family]]
