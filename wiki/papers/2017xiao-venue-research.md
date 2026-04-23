---
id: paper:2017xiao-venue-research
type: paper
title: "Development of a Transferable Reactive Force Field of P/H Systems: Application to the Chemical and Mechanical Properties of Phosphorene"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:2d-layered
  - method:reaxff
  - material:widegap-semiconductor
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:2d-materials
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.7b05257"
year: 2017
authors:
  - "Hang Xiao"
  - "Xiaoyang Shi"
  - "Feng Hao"
  - "Xiangbiao Liao"
  - "Yayun Zhang"
  - "Xi Chen"
venue: "The Journal of Physical Chemistry A (2017)"
pdf_sha256: "1aea8b3e2f1bfafea4566bcba65517b69798b17ce2632b12e361192fd551356d"
pdf_path: "papers/ReaxFF_others/Xiao_ReaxFF_Phosphor_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017xiao-venue-research -->

## Summary

Two-dimensional phosphorus allotropes and hydrogenated derivatives combine strong in-plane anisotropy with chemical sensitivity to ambient oxidation, motivating reactive models that can simultaneously describe covalent chemistry and mechanical response. This *Journal of Physical Chemistry A* article presents a ReaxFF parametrization for phosphorus and hydrogen trained by global optimization against quantum-mechanical reference data spanning bulk black phosphorus, blue phosphorene motifs, edge-hydrogenated ribbons, phosphorus clusters, and small phosphorus hydrides. The authors introduce a sixty-degree correction term to improve energetics for certain phosphorus cluster configurations that are challenging for a naive bond-order fit. Beyond the baseline P/H description, the manuscript sketches extensions toward P/H/O/C parameter subsets aimed at oxidized phosphorene and van der Waals heterostructure scenarios where oxygen insertion and mixed-element interfaces matter for stability.

## Methods

**Force-field training (ReaxFF + QM).** **P/H ReaxFF** parameters are generated via **global optimization** against **DFT** reference data computed in **CASTEP** using the **PBE** functional with **Grimme D2 dispersion**, **ultrasoft pseudopotentials**, a **520 eV** plane-wave cutoff, **Monkhorst–Pack** **k-point** spacing (~0.02 Å⁻¹) for periodic **slabs**, and **Γ** sampling for **20 Å** cubic **supercells** housing **phosphorus clusters**/**hydrides**. **Spin polarization** enters cluster/molecule evaluations. A **60° correction term** improves **phosphorus cluster** energetics that are otherwise too stiff in a naive bond-order expansion. A preliminary **P/H/O/C** extension is sketched for **oxidized phosphorene** but is not claimed as fully converged.

**Molecular dynamics (reactive + classical benchmarks).** **Reactive MD** and follow-on **mechanical** tests (uniaxial **strain** to **failure**, **phosphorene nanotube** **thermal** stability) compare **ReaxFF** to the **Stillinger–Weber** baseline for **pristine**, **single-vacancy**, and **double-vacancy** sheets, highlighting **armchair** versus **zigzag** **anisotropy**. The indexed excerpt does not spell out every **NVT**/**NPT** flag, **timestep** (fs), **thermostat**/**barostat**, or **equilibration**/**production** **duration** (ps/ns); copy those from **`papers/ReaxFF_others/Xiao_ReaxFF_Phosphor_2017.pdf`**. **Periodic boundary conditions** apply to monolayers separated by **15 Å** vacuum in the **DFT** training setups. **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** described in the excerpted methodology pages.

**Static QM / DFT.** **DFT** provides **training** **energies**, **forces**, and **relaxed geometries** for **clusters**, **ribbons**, and **defective** **slabs**; it is distinct from production large-scale **MD**.

**Review scope.** **N/A —** primary **JPCA** research article (workflow duplicate note: **`[[2017reaxff-venue-paper]]`**).

## Findings

**Outcomes and mechanisms.** **ReaxFF** reproduces **elastic** and **failure** behavior for **pristine** and **defective** **phosphorene** far better than the nonreactive **Stillinger–Weber** potential, showing that **bond-breaking** freedom matters even for ostensibly mechanical observables when **vacancies** participate. A **counterintuitive** trend appears: **single vacancies** can weaken sheets more than **double vacancies** under selected loads despite higher **double-vacancy formation energies**, because **stress concentrations** and local **failure** pathways are not monotonic in defect count.

**Comparisons.** **Versus** the literature **SW** potential cited in the abstract, **ReaxFF** improves **Young’s modulus** trends (notably along **zigzag**) and captures **defect** mechanics absent from fixed-bond models.

**Sensitivity / design levers.** **Defect** density/orientation and loading direction (**armchair** vs **zigzag**) control strength and **thermal** stability of **nanotubes** in the validation narrative.

**Limitations / outlook.** Preliminary **P/H/O/C** parameters are demonstration-only; aggressive **aqueous oxidation** or organophosphorus chemistry needs broader **training** data.

**Corpus honesty.** Detailed **MD** staging beyond the **DFT** subsection is not in the short extract—confirm timings and thermostats from the **PDF** at `pdf_path`.

## Limitations

Transferability to aggressive aqueous electrolytes, long-time oxidation, or organophosphorus chemistries requires expanded training sets and independent validation against experiment and higher-level electronic structure where available.

## Relevance to group

The work extends the ReaxFF ecosystem into two-dimensional phosphorus with explicit mechanical benchmarks, complementing the group’s broader reactive studies on carbon, oxides, and hybrid interfaces.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.7b05257](https://doi.org/10.1021/acs.jpca.7b05257)

## Reader notes (navigation)

- Workflow duplicate PDF: [[2017reaxff-venue-paper]].

## Related topics

- [[reaxff-family]]
- Phosphorene and 2D semiconductors
