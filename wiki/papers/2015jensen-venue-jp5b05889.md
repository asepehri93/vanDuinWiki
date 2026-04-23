---
id: paper:2015jensen-venue-jp5b05889
type: paper
title: "Simulation of the elastic and ultimate tensile properties of diamond, graphene, carbon nanotubes, and amorphous carbon using a revised ReaxFF parametrization"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - material:graphene-carbon-nano
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:lammps
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.5b05889"
year: 2015
authors:
  - "Benjamin D. Jensen"
  - "Kristopher E. Wise"
  - "Gregory M. Odegard"
venue: "Journal of Physical Chemistry A"
pdf_sha256: "ebf8b492695195ddf64b397fb2be169d300ca2fd1d381a3c179bd3ca1c7a1318"
pdf_path: "papers/ReaxFF_others/Jensen_graphene_JPCA_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015jensen-venue-jp5b05889 -->

!!! abstract "Scope"
Large-strain reactive MD benchmarks of **ReaxFFC‑2013** (carbon parametrization including DFT mechanical training data) against DFT and experiment for diamond, graphene, amorphous carbon, and nanotubes, using **VASP** reference calculations and **LAMMPS** simulations.

## Summary

The study evaluates the **ReaxFFC‑2013** reactive force field for elastic response and fracture of several carbon allotropes. DFT reference data use **VASP** with **PAW–PBE** and **Grimme DFT-D2** (PBE-D2) van der Waals corrections. Reactive MD uses **ReaxFF in LAMMPS**, comparing **ReaxFFC‑2013** to the older **ReaxFF CHO** parametrization for diamond and graphene, then testing transferability to amorphous carbon and carbon nanotubes.

## Methods

**Static QM (DFT reference).** Reference stresses and energies use **VASP** with **PAW–PBE** and **Grimme DFT-D2** (**PBE-D2**), **virial stresses** at deformed geometries, and **k**-meshes **15×15** (**800 eV** cutoff) for **graphene** and **16×16×16** (**700 eV** cutoff) for **diamond** primitive cells (convergence-checked as reported).

**Reactive MD (LAMMPS + ReaxFF).** Large-strain tests use **LAMMPS** **ReaxFF** with **ReaxFFC‑2013** everywhere; **ReaxFF CHO** appears only for the **diamond**/**graphene** comparison against the older parametrization. **Systems** include periodic **diamond** supercells (**~8000** atoms, **⟨100⟩** and **⟨112⟩** orientations), **single-layer graphene** (**~6696** atoms, **3D PBC** with vacuum normal to the sheet, **0.34 nm** effective thickness for stress), plus **amorphous carbon** and **CNT** arrays detailed in the article and **SI** (structures visualized with **Ovito**).

**Equilibration before loading (diamond/graphene).** Each allotrope model is heated **0 → 300 K** over **5 ps** (**Langevin**), held at **300 K** and **~0 pressure** for **16 ps** (**Berendsen** thermostat **+ barostat**), then **2 ps** at **300 K** after removing the barostat. **Tensile** production segments use **Δt = 0.2 fs** as stated.

**CNT and amorphous carbon paths.** **CNT arrays** are heated **0 → 300 K** over **100 ps** (**Langevin** + **Berendsen barostat**), then run **50 ps** with **Berendsen** thermostat only; array **mass densities** are tabulated in the paper. **Amorphous carbon** cells are built by heating disordered configurations to **3000 K** under **NVT** and quenching—densities and cycle counts are in **Computational Details**.

## Findings

For **diamond** and **graphene**—allotropes represented in the **ReaxFFC‑2013** training set—simulated **elastic** and **large-strain** responses track **DFT (PBE-D2)** and available **experiment** more closely than the older **ReaxFF CHO** parametrization in the article’s comparisons. **Amorphous carbon** and **CNT** arrays, which were **not** in the mechanical fitting set, still show largely consistent trends with experiment for single- and multi-walled tubes and for amorphous carbon across densities, with specific deviations the authors flag for future parametrization. The discussion stresses **GGA+D2** limitations, **k**-mesh and **cutoff** choices, and **strain-rate** / **model-size** effects common to large-deformation MD. **Numerical moduli, strengths, and residuals** are **figure/table-specific**; cite the **JPCA** PDF for any number used downstream.

## Limitations

DFT uses a specific **GGA+D2** setup; mechanical observables are sensitive to k-sampling, strain rate, and model size. Transferability targets (amorphous carbon, CNTs) lie outside the original mechanical training data for the parametrization.

## Relevance to group

Benchmarks **ReaxFF** carbon parametrizations for large-deformation carbon mechanics—adjacent to reactive **carbon/hydrocarbon** simulation practice in the broader ReaxFF literature.

## Citations and evidence anchors

Prefer the publisher version via DOI `10.1021/acs.jpca.5b05889` (see `pdf_path` for the local PDF used here).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
