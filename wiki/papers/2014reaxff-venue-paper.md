---
id: paper:2014reaxff-venue-paper
type: paper
title: "Buckybomb: reactive molecular dynamics simulation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:energetic-materials
  - keyword:graphene-carbon
  - keyword:thermal-decomposition
  - keyword:combustion
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.5b00120"
year: 2015
authors:
  - "Vitaly V. Chaban"
  - "Eudes Eterno Fileti"
  - "Oleg V. Prezhdo"
venue: "The Journal of Physical Chemistry Letters"
pdf_sha256: "818e6716f15feaa2be458e347da6382b28ea7697978da8953485be6e44139eeb"
pdf_path: "papers/ReaxFF_others/ReaxFF_nanobomb.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2014reaxff-venue-paper -->

!!! abstract "ReaxFF MD of heated nitrofullerene C60(NO2)12 shows an ultrafast ‘nano-explosion’: NO2 rearrangement, NO release, surface CO/CO2 chemistry, and eventual C2 at extreme temperature; initiation temperature and energy release depend on composition and density."

## Summary

This work uses **ReaxFF reactive molecular dynamics** to study **decomposition of a nitrofullerene**, **C60(NO2)12**, as a model **nanoscale energetic** system. Upon rapid heating, the simulations show a violent **energy release** on **picosecond** timescales with large rises in **temperature and pressure**. The authors describe a stepwise **chemical mechanism** starting from **NO2** isomerization, **NO** emission, **CO** formation on the cage, oxidation chemistry involving **NO2**, **CO2** liberation as the cage fragments, and at the highest temperatures **diatomic carbon** from **CO2**-derived chemistry (as summarized in the abstract).

The study argues that **initiation temperature** and **released energy** depend on **composition and packing density**, offering a qualitative picture of how **nanoscale energetic materials** might behave differently from bulk explosives.

## Methods

### Source files / DOI alignment

- Local PDF: `papers/ReaxFF_others/ReaxFF_nanobomb.pdf`; extract: `normalized/extracts/2014reaxff-venue-paper_p1-2.txt`.
- Authoritative bibliographic record: **DOI** **10.1021/acs.jpclett.5b00120** (*J. Phys. Chem. Lett.*, **2015**), which may differ from the **filename** year in the slug.

### Reactive MD system

- **ReaxFF reactive MD** of **nitrofullerene** **C\(_{60}\)(NO\(_2\))\(_{12}\)** as a **model nanoscale energetic** (**Summary**).

### Thermal initiation protocol (qualitative)

- Simulations apply **rapid heating** to trigger an ultrafast **energy-release** sequence; **cell**, **thermostat**, **timestep**, and **heating rate** are specified in the **JPCL** article beyond the one-page extract.

### Observables

Trajectories resolve **species evolution**, **temperature**, and **pressure** rises associated with the **decomposition** cascade described in the abstract (**Findings**).

### 1 — MD application (ReaxFF reactive MD)

The preprint-style PDF (`papers/ReaxFF_others/ReaxFF_nanobomb.pdf`) and one-page extract `normalized/extracts/2014reaxff-venue-paper_p1-2.txt` document **reactive molecular dynamics** of **C\(_{60}\)(NO\(_2\))\(_{12}\)** under **rapid heating** leading to an ultrafast energy release. **Engine (LAMMPS/VASP/etc.), system size in atoms, PBC, timestep in fs, thermostat, barostat, staged equilibration vs heating ramps, and total trajectory length:** **N/A —** not contained in the checked-in extract; the **authoritative protocol** is in the **J. Phys. Chem. Lett.** article (**DOI** `10.1021/acs.jpclett.5b00120`, **2015**). **Ensemble:** **NVT** vs **NVE** vs **NPT** labeling is **N/A —** not printed on the one-page extract—confirm in the journal **PDF**. **Electric field / enhanced sampling:** **N/A —** not indicated on the extract for this heating-driven **decomposition** study.

### 2 — Force-field training

**N/A —** the indexed excerpt is an **application** note for **ReaxFF** on a **nitrofullerene**; it does not summarize a new parameter fit on that page.

## Findings

Upon heating, **C\(_{60}\)(NO\(_2\))\(_{12}\)** undergoes a violent **decomposition** that drives **large increases in temperature and pressure** on **tens-of-picosecond** timescales. The authors describe a **stepwise chemical mechanism** beginning with **NO\(_2\)** group **isomerization** into **C–O–N–O**, followed by **NO** release and **CO** formation on the **fullerene** surface, further **oxidation** involving **NO\(_2\)**, **CO\(_2\)** liberation as the cage fragments, and at the **highest temperatures** **diatomic carbon** formation from **CO\(_2\)**-related chemistry (**abstract**, extract).

**Sensitivity.** The **abstract** states **initiation temperature** and **released energy** depend strongly on **chemical composition** and **material density**—a lever relevant to **nanoscale** energetic packing.

**Comparisons / limitations (corpus).** The local filename/slug predates the **JPCL** bibliographic record; quantitative benchmarks versus **experiment** are **N/A —** not present on the one-page extract—use the **version-of-record** **PDF** for any validation discussion.

## Limitations

- The registered PDF may correspond to a **preprint-era** document name (`ReaxFF_nanobomb.pdf`); cite the **journal article** via DOI for authoritative metadata.
- Quantitative predictions are **classical reactive FF**-level and should be validated for any quantitative safety or performance use.

## Relevance to group

Illustrates **ReaxFF** applied to **energetic nanocarbon** chemistry and **extreme transient heating** scenarios.

## Reader notes (navigation)

- Published JPCL record: DOI below (2015). An **arXiv preprint** also exists for earlier dissemination.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpclett.5b00120](https://doi.org/10.1021/acs.jpclett.5b00120)
