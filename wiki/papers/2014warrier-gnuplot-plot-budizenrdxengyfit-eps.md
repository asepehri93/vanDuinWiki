---
id: paper:2014warrier-gnuplot-plot-budizenrdxengyfit-eps
type: paper
title: "Interatomic potential parameters for molecular dynamics simulations of RDX using a reactive force field: A validation study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - domain:organics-polymers-pyrolysis
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:energetic-materials
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1088/1742-6596/377/1/012100"
year: 2014
authors:
  - "Manoj Warrier"
venue: "J. Phys.: Conf. Ser. 377 012100 (2012)"
pdf_sha256: "b12b8d138adc8f61e736d8dd2a606ca588781faacd243233e77593d9e2ba095d"
pdf_path: "papers/ReaxFF_others/Interatomic potentials for MD J phys conf proc 377(2012)01200.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014warrier-gnuplot-plot-budizenrdxengyfit-eps -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below (**Summary**, **Methods**, **Findings**) summarizes the conference article identified by `doi`, `title`, and `pdf_path` in the front matter. It is not new primary science from this wiki.

    For definitive numerical values and tables, use the peer-reviewed PDF (and any SI), not this page alone.

## Summary

Warrier reports a **conference proceedings** validation study (*J. Phys.: Conf. Ser.* **377** **012100**, DOI `10.1088/1742-6596/377/1/012100`) that asks a narrow but important engineering question: can the **ReaxFF** parameter sets **bundled** with the **LAMMPS** distribution (April 2011 release) reproduce basic **solid-state** properties of **crystal RDX**—a nitramine **energetic** material—when used with the authors’ **MD** protocols? Rather than proposing new parameters, the paper **benchmarks** **three** packaged sets referenced as **general-purpose hydrocarbon (GPHP)**, **reactive nitramine (RFFN)**, and **PETN-focused (RFFPETN)** parameterizations, comparing predicted **unit-cell dimensions** and **bulk modulus** at **300 K** against **experiment** and prior **ReaxFF** literature values. The overarching motivation is **defense/industrial** safety and performance modeling: **RDX** chemistry is expensive at **DFT** cost, so practitioners often reach for **ReaxFF**, but only if the **parameterization** and **code path** are trustworthy for the **crystal** phase of interest.

## Methods

**MD application (crystal RDX benchmarks).** **LAMMPS** (open source) drives **ReaxFF MD** on **crystal RDX** supercells to extract **unit-cell** dimensions and **bulk modulus** for each tested parameter file; the abstract reports **20** **NVT** trajectories at **300 K** per parameter set plus **NPT** simulations to examine **lattice relaxation** relative to **NVT** and **experiment**. The authors note prior **Cu** validation of their **MD** workflow. **Periodic** (**PBC**) construction, timestep, **equilibration**/**production** **durations** (**ps**/**ns**), and thermostat/**barostat**/**pressure** damping are **N/A** on the indexed **IOPscience** front matter in `normalized/extracts/2014warrier-gnuplot-plot-budizenrdxengyfit-eps_p1-2.txt` and appear in the full conference PDF.

**Force-field training.** **N/A**: the work **benchmarks** three **ReaxFF** parameter sets bundled with **LAMMPS** (**5 April 2011** release)—**GPHP**, **RFFN**, and **RFFPETN** as named in the abstract—rather than fitting new parameters.

**Static QM.** **N/A** as headline method: comparisons are to **experiment** and literature **ReaxFF** applications cited in the paper.

## Findings

Under the stated validation, **none** of the three **bundled** **ReaxFF** sets simultaneously reproduce **experimental** **unit-cell** size **and** **bulk modulus** for **crystal RDX**, despite literature **ReaxFF** studies reporting better agreement under other parameterizations/implementations. With **LAMMPS** previously validated for **Cu**, the authors argue the failure is unlikely to be a generic integrator defect and more plausibly reflects **unsuitability** of the **2011**-bundled **parameters** or **implementation** path for **crystal RDX** in their tests. The paper therefore reads as a **historical cautionary benchmark** about **default** parameter **provenance** for **nitramine** crystals; newer releases and retrained fields may behave differently—consult the PDF tables for the exact numerical deviations.

## Limitations

The study is tied to a **2011** **LAMMPS** **distribution** and **specific** **parameter** file versions; newer **ReaxFF** **releases** and **bugfix** histories may change conclusions. The paper does **not** provide a **new** **fitted** **RDX** field—readers seeking predictive **crystal** properties should follow subsequent **parameterization** work and validate against **independent** **QM** benchmarks.

## Relevance to group

Useful **validation** folklore adjacent to **van Duin**-lineage **ReaxFF** practice: it reinforces that **default** **distributed** parameters are not automatically **transferable** to **crystal** **energetics** benchmarks without **explicit** checks.

## Citations and evidence anchors

- DOI: [10.1088/1742-6596/377/1/012100](https://doi.org/10.1088/1742-6596/377/1/012100)

## Related topics

- [[reaxff-family]]
