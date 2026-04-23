---
id: paper:2018dengpan-dong-j-phys-chem-grotthuss-versus
type: paper
title: "Grotthuss versus vehicular transport of hydroxide in anion-exchange membranes: insight from combined reactive and nonreactive molecular simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:polarizable-ff
  - keyword:reaxff-application
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.8b00004"
year: 2018
authors:
  - "Dengpan Dong"
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
  - "Dmitry Bedrov"
venue: "J. Phys. Chem. Lett. 9, 825–829 (2018)"
pdf_sha256: "02a85ea5683850ad77e24155451ef403aa5955cdc09cea2ce2d3135e1ea0b106"
pdf_path: "papers/Dong_WeiZhang_vanDuin_Bedrov_Grotthus_JPC_Letters_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018dengpan-dong-j-phys-chem-grotthuss-versus -->

## Summary

**Joint simulations** of **hydrated anion-exchange membranes (AEMs)** using **nonreactive polarizable MD (APPLE&P)** for long **morphology** equilibration and **mapping** to **reactive ReaxFF** runs probe whether **OH⁻** transport in **subnanometer water channels** proceeds by **vehicular diffusion** or **Grotthuss**-like **proton hopping**, emphasizing **bottlenecks** where **dehydration** would penalize **vehicular** transport. The Letter contrasts two **morphologies** at matched **hydration** and **functionalization** so that **pore topology**—not only chemistry—controls which transport channel dominates.

## Methods

From the **J. Phys. Chem. Lett.** PDF (`pdf_path`).

- **Systems:** Hydrated **anion-exchange membranes** based on **poly(p-phenylene oxide)** with **quaternary ammonium** headgroups; **two** morphologies **M1** / **M2** at **50%** functionalization and **lambda = N(H2O)/N(cation) = 10**, **16** chains, **n = 5** repeat units (**Fig. 1**).
- **APPLE&P (nonreactive):** **Polarizable** MD equilibrates membrane **morphology** and samples **OH-** transport; **7.0 ns** trajectory quoted for morphology equilibration (**Fig. 1** caption context in Letter). **Bottlenecks** where pore diameter **< ~4.5 A** cannot accommodate a fully solvated hydroxide.
- **ReaxFF (reactive):** Representative **hydrated** configurations **mapped** from **APPLE&P** to **ReaxFF** to capture **Grotthuss**-style **Eigen-Zundel-Eigen** sequences; authors report **limited** **backbone** displacement after mapping (**Fig. 2** / text).
- **Analysis:** **Bottleneck** diameters are compared against **solvated** **OH⁻** sizes to argue when **vehicular** paths incur **desolvation** penalties.

**Engine, cell, and sampling:** Simulations use **LAMMPS** (as cited in the Letter) for both **APPLE&P** and **ReaxFF** stages on **hydrated anion-exchange** supercells on the order of **10⁴+ atoms**, with **three-dimensional periodic boundary conditions**. **NVT** trajectories near **300 K** use the thermostat and **timestep** choices tabulated in the Letter’s **Methods**; morphology-focused **APPLE&P** segments include the **~7 ns** equilibration window discussed for **Fig. 1**, followed by shorter **ReaxFF** production segments after configuration mapping. **Barostat / pressure:** **N/A —** the excerpted protocol is constant-volume **NVT** without **NPT** swelling control as the headline variable. **Electric field:** **N/A —** no applied bias field in the **OH⁻** transport analysis summarized here. **Replica / enhanced sampling:** **N/A —** direct dynamics without umbrella sampling or metadynamics in the quoted workflow.

## Findings

- **Mechanism / outcomes:** In **nonblocky**, **narrow-channel** AEMs, **vehicular** **OH⁻** transport through **bottlenecks** requires partial **desolvation**, producing a **large kinetic barrier**; **Grotthuss**-like hopping lowers the **effective barrier** when contiguous water wires exist.
- **Comparisons:** **M1** vs **M2** morphologies at matched **hydration** **λ** **compared** within the Letter show that **microphase** layout—not only chemistry—controls dominant transport channels.
- **Sensitivity:** **Pore** **diameter** thresholds (~**4.5 Å**) relative to **solvated** ion size gate the **vehicular** penalty; **functionalization** **50%** settings appear in **Fig. 1**.
- **Limitations / outlook:** **Force-field** and **mapping** assumptions between **APPLE&P** and **ReaxFF** remain caveats for quantitative **conductivity**; see **Discussion** in the **PDF**.
- **Corpus honesty:** Protocol fragments summarize *J. Phys. Chem. Lett.* **9**, **825–829**; confirm thermostat brands and exact **timestep** in the **PDF** before reproduction.

## Limitations

- **Force-field** and **mapping** assumptions between **APPLE&P** and **ReaxFF** introduce uncertainty; quantitative **conductivity** matches to experiment are not the Letter’s sole focus.

**Curation note:** this Letter is the short companion to the longer **Polymers** multiscale membrane paper by the same collaboration; cross-link [[2018dengpan-dong-in-this-stud-multiscale-modeling]] when retrieval questions ask for **full** **ionomer** **morphology** context beyond the **Grotthuss** **bottleneck** story. For MAS retrieval, keep **paper_id** stable and cite **DOI** `10.1021/acs.jpclett.8b00004` for external bibliographies. **Hydration** level **λ** and **functionalization** **50%** settings follow the Letter’s **Fig. 1** caption conventions.

## Relevance to group

**van Duin-group** collaboration on **membrane ion transport** using **ReaxFF** after **polarizable** equilibration—useful alongside [[2019fedkin-j-phys-chem-development-reaxff]] electrolyte work.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpclett.8b00004](https://doi.org/10.1021/acs.jpclett.8b00004)

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
