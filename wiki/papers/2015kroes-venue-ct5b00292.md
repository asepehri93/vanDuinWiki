---
id: paper:2015kroes-venue-ct5b00292
type: paper
title: "Atom vacancies on a carbon nanotube: to what extent can we simulate their effects?"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - method:dft-static
  - method:reaxff
  - material:graphene-carbon-nano
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:reaxff-application
  - keyword:classical-ff
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.5b00292"
year: 2015
authors:
  - "Jaap M. H. Kroes"
  - "Fabio Pietrucci"
  - "Adri C. T. van Duin"
  - "Wanda Andreoni"
venue: "Journal of Chemical Theory and Computation"
pdf_sha256: "24b07ed2ef97f5ddd1a8f01c450c672fd681b6ec7c32c55aee1892e60f987059"
pdf_path: "papers/Kroes_CNT_vacancy_JCTC_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015kroes-venue-ct5b00292 -->

??? info "Curators"
    Body text summarizes the **JCTC** article identified in YAML; numeric barriers and structures should be checked against the publisher PDF.

## Summary

This Journal of Chemical Theory and Computation article benchmarks classical interatomic models against spin-polarized density functional theory for intrinsic vacancies in a (10,0) zigzag single-wall carbon nanotube. The study focuses on single and double vacancies and reports relaxed structures, vacancy formation energies, and energy barriers for elementary processes such as reconstruction, migration, and coalescence. On the DFT side, calculations use CPMD with PBE and BLYP exchange–correlation functionals and include selected hybrid PBE0 repeats; on the classical side, the authors compare widely used carbon potentials including AIREBO, LCBOP (LCBOPI as primary, LCBOPII partly in Supporting Information), ReaxFF15, REBO (more fully in Supporting Information), and a Tersoff parameterization oriented toward amorphous carbon. Adri C. T. van Duin is a co-author, placing ReaxFF15 explicitly in a comparative validation setting rather than as a standalone claim of accuracy.

## Methods

**Reference system.** **(10,0)** zigzag **single-wall** carbon nanotube models with **single** and **double** vacancies; quantities reported include **relaxed structures**, **vacancy formation energies**, and **barriers** for **reconstruction**, **migration**, and **vacancy coalescence**.

**Static QM (DFT).** **Spin-polarized** **plane-wave DFT** in **CPMD** with **PBE** and **BLYP** functionals, **Γ-only** sampling, and selected **PBE0** repeats as described; **lowest spin multiplicity** (singlets) is enforced in the benchmark set noted in the article.

**Classical potentials (energy landscapes).** The same defect motifs are evaluated with **AIREBO**, **LCBOPI** (**LCBOP** family; **LCBOPII** partly in **SI**), **ReaxFF15**, **REBO** (**SI**), and **Tersoff** (discussed largely in **SI**) using the same **tetragonal** supercells (**~359–360** atoms for most cases, **598** atoms for the slowly converging **5r8r5r-Z** double vacancy). **Formation energies** use the **carbon chemical potential** definition printed in the article.

**Auxiliary classical MD (motif sampling).** The authors additionally report **high-temperature AIREBO molecular dynamics** on a **large** **~100,000-atom**, **~1 µm** tube model followed by **simulated annealing** to propose **vacancy** geometries that are subsequently **relaxed** in **DFT**; this exploratory MD is **not** the same object as the **small-cell** barrier tables.

**Production reactive MD (ReaxFF).** **N/A —** **ReaxFF15** enters as **static** energies and **barriers** on the **(10,0)** benchmark cells, not as long **finite-temperature ReaxFF MD** production trajectories. The separate **high-temperature AIREBO MD** on a **large** tube followed by **annealing** is exploratory geometry sampling later **relaxed** in **DFT**; it is **not** the quantitative **ReaxFF15** benchmark path. **Timestep, thermostat law, NPT barostat, replica exchange, and electric fields:** **N/A —** not applicable to the **small-cell** minimization/barrier workflows (and not separately tabulated for the scouting **MD** in the sections indexed for this note). **PBC:** **3D periodic** **tetragonal** supercells for the **DFT** / classical **small-cell** work as stated in the article.

## Findings

The central empirical result is lack of uniform agreement: vacancy-related structures, formation energies, and barriers differ markedly among DFT choices and among classical potentials, and no single classical model matches PBE benchmarks across all processes examined. ReaxFF15, AIREBO, LCBOP, Tersoff, and related schemes each show distinct strengths and failures depending on the vacancy process, underscoring that reactive and bond-order potentials require careful, property-specific validation for defective nanotubes. The authors frame the compilation as guidance for constructing or refining DFT-informed classical schemes for carbon nanostructures rather than as endorsement of a single potential for all vacancy dynamics.

The introduction additionally notes that vacancies can influence binding of adsorbates, oxidation, and coalescence phenomena in nanotubes, and that growth or fracture simulations that move atoms between gas-like and condensed environments especially depend on reliable classical energetics for defect rearrangements, motivating systematic benchmarking against spin-polarized DFT rather than isolated literature values. The authors also highlight exchange-correlation sensitivity within DFT itself by comparing gradient-corrected functionals with partial exact-exchange hybrid checks for selected quantities.

## Limitations

**Γ-point** supercells and specific vacancy topologies; classical models inherit known transferability limits for **charged/spin** states and long-range relaxation.

## Relevance to group

**Adri C. T. van Duin** co-authorship; directly contextualizes **ReaxFF** against **DFT** for **defective CNT** energetics.

## Citations and evidence anchors

DOI `10.1021/acs.jctc.5b00292`.

## Reader notes (navigation)

- CNT defect benchmark vs [[2016tomas-carbon-109-2-graphitization-amorphous]] (carbon FF survey); [[reaxff-family]].

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
