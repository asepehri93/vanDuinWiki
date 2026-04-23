---
id: paper:2019wilkinson-j-phys-chem-topological-control
type: paper
title: "Topological control of water reactivity on glass surfaces: evidence of a chemically stable intermediate phase"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:oxides-ceramics
  - method:reaxff
  - method:classical-md
  - method:dft-static
  - task:application
  - material:silicate-glass
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:oxide-surface
  - keyword:lammps
  - keyword:nvt-simulation
source_refs: []
doi: "10.1021/acs.jpclett.9b01275"
year: 2019
authors:
  - "Collin J. Wilkinson"
  - "Karan Doss"
  - "Seung Ho Hahn"
  - "Nathan Keilbart"
  - "Arron R. Potter"
  - "Nicholas J. Smith"
  - "Ismaila Dabo"
  - "Adri C. T. van Duin"
  - "Seong H. Kim"
  - "John C. Mauro"
venue: "J. Phys. Chem. Lett. (2019), 10, 3955-3960"
pdf_sha256: "5cb59db487fb82fe7de6340e9605eabaa0afe5731801295c9d7cdd314c335818"
pdf_path: "papers/Wilkinson_JPCL_2019_water_reactivity_SiO2.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2019wilkinson-j-phys-chem-topological-control -->

## Summary

This *Journal of Physical Chemistry Letters* article combines three modeling layers to connect **oxide glass network topology** to **aqueous reactivity** at **sodium silicate** surfaces: **classical melt/quench MD** with the **Teter** potential to form bulk glass, **ReaxFF Na/Si/O/H** simulations of **glass–water** contact chemistry, and **density functional theory** benchmarks for **water–surface** binding energetics. The central hypothesis is that **mechanical constraint counting**—a Phillips–Thornton-style **rigidity percolation** viewpoint—can identify **intermediate**, **mechanically isostatic** surface regions that are **comparatively inert** toward **dissolution** relative to under- or over-constrained patches. The work is co-authored by **Adri C. T. van Duin** and targets the long-standing problem that water attacks oxide glasses heterogeneously even when composition is uniform at the macroscopic scale.

## Methods

**1 — Melt–quench classical MD of bulk glass (Teter potential, LAMMPS).** Random placements for nominal **70 SiO₂·30 Na₂O** in a cubic periodic box with edge **\(a = 12.686\) Å** (to match a target mass density) yield **35 Si, 85 O, and 30 Na atoms** (150-atom **stoichiometry** per replicate) after the authors’ equilibration sequence. The protocol in the *JPCL* letter: energy minimization; **NVE** “melt” hold (the letter notes a \~2000–2400 K range over 0.5 ns with a large temperature drift in the microcanonical leg); then **NVT** at 2400 K for 0.5 ns with a **Nosé–Hoover thermostat**; then linear cooling at **0.5 K ps\(^{-1}\)** until **300 K** followed by **1 ns** NVT equilibration (thermostat as in the letter); then **1 ns** at **1 atm** in **NPT** to stabilize density, with **three** independent replicates. **Strain, shock, or applied electric field in this stage:** **N/A**.

**2 — ReaxFF (Na/Si/O/H) and water on cleaved silicate surfaces.** The cleaved glass feeds reactive simulations that map *local* **constraint density** (a Phillips–Thornton–style count on the disordered network) to **water interaction strength**; the main text and SI give cell sizes, water coverages, the ReaxFF time step, and the sampling length. For any detail not recopied here, **N/A** on this wiki line—read the *JPCL* letter and SI. If interfacial segments are NVT, **N/A** for barostat in that leg; the bulk-glass NPT equilibration above already documents pressure-coupled stages where used. **Replica, umbrella, or metadynamics in ReaxFF:** **N/A** in the one-page extract unless the SI adds a separate enhanced-sampling run.

**3 — Static DFT (benchmarks).** Supplemental (or in-text) DFT is used to benchmark selected **water–surface** binding energy trends; **N/A** for a full standalone DFT methods table on this page—use the published functional/basis and k-sampling in the *JPCL* PDF when citing numbers.

**4 — Review / continuum.** **N/A.**

## Findings

The reported trend is that **surface sites** near an **isostatic** window (approximately **three constraints per atom** in their mapping) exhibit **suppressed** water-driven reactivity compared with more under- or over-constrained regions, motivating interpretation as a **chemically stable intermediate surface phase** whose existence is tied to **topology** rather than composition alone. The paper frames this as a bridge between **rigidity theory** and practical **durability** questions for silicate glasses in humid environments.

## Limitations

**Nanoscale** surface slabs and **short** reactive MD windows limit rare-event sampling; transferring structures from **Teter** melts to **ReaxFF** surfaces introduces **hand-off** sensitivity that the article must justify with internal consistency checks.

## Reproducibility notes

Glass preparation requires careful documentation of **melt quench rate**, **density** after **NPT**, and **surface cleavage** plane choices because **constraint counting** maps depend on local network statistics near the interface. For ReaxFF water exposure, record **water loading**, **dissociation** handling (if any), and **timestep**, as silicate surface chemistry can be timestep-sensitive when proton transfer is frequent.

## Relevance to group

**ReaxFF + topological constraint** framing for **glass–water** interfaces (van Duin co-author).

## Citations and evidence anchors

DOI: [10.1021/acs.jpclett.9b01275](https://doi.org/10.1021/acs.jpclett.9b01275)

## Related topics

- [[reaxff-family]]
