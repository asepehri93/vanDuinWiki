---
id: paper:2016senftle-venue-cs6b02447
type: paper
title: "Methane Activation at the Pd/CeO2 Interface"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:oxides-ceramics
  - material:metal-surface
  - method:reaxff
  - method:dft-static
  - method:monte-carlo
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acscatal.6b02447"
year: 2016
authors:
  - "Thomas P. Senftle"
  - "Adri C. T. van Duin"
  - "Michael J. Janik"
venue: "ACS Catalysis (see PDF; manuscript id cs6b02447 family)"
pdf_sha256: "585dfc9ab3a0bbcb9394f04ae0d28019dee94f91ff2dddd0bae75bf454604b23"
pdf_path: "papers/Senftle_ACS_Catalysis_2017.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:catalysis-surface
  - keyword:qm-training-data
---
<!-- id:paper:2016senftle-venue-cs6b02447 -->

## Summary

The paper develops a **combined DFT + ReaxFF** workflow for **Pd/CeO\(_2\)** interfaces relevant to **methane activation**. **Grand Canonical Monte Carlo (GC-MC)** with ReaxFF explores oxide/metal interface morphologies; **reactive MD (RMD)** probes **methane light-off** trends when **Pd mixes into the CeO\(_2\)** lattice; **DFT** then targets **Pd\(^{4+}\)**-like stabilization in **PdO\(_x\)** clusters partially embedded in ceria and **barriers** for methane activation on those motifs.

Methane partial oxidation and reforming on ceria-supported Pd are technologically important but structurally heterogeneous; the manuscript uses classical sampling to propose realistic interface motifs before committing to expensive cluster models for barrier calculations.

## Methods

**1 — MD application (ReaxFF GC-MC and RMD).** **Grand Canonical Monte Carlo (GC-MC)** with **ReaxFF** explores **oxygen** insertion, deletion, and translation on **Pd** clusters on **CeO\(_2\)(111)** and in **partially embedded** interface geometries motivated by **HRTEM**-inspired cluster models (see article for cell dimensions and **T = 500 K**, **P\(_{\mathrm{O}_2}\)** ranges such as **10\(^{-20}\)**–**1 atm** in the excerpted letter). **Geometry optimization** at **MC** steps relaxes supported versus embedded morphologies; embedded clusters show **Pd mixing** into **defective ceria** regions not seen on pristine supported clusters. **Reactive molecular dynamics (RMD)** of **methane** activation then uses **equilibrated GC-MC** structures as **surface models**. **Timestep**, full **thermostat/barostat** choices, **electrostatic** details, and **production** lengths for all **RMD** segments are **N/A —** not duplicated on this wiki page; read **`pdf_path`**. **Shear**, **tribological** loading, **electric fields**, and **umbrella/metadynamics** are **N/A —** not part of the summarized workflow unless introduced explicitly in the full text.

**2 — Force-field training.** **N/A —** the letter **applies** assembled **Pd/O**, **Pd/C/H**, and **Ce/O** parameter sets and **Pd/Ce/O** cross terms documented in **Supporting Information**; this page does not reproduce the fit protocol.

**3 — Static QM / DFT.** **DFT** on **cluster/surface** models inspired by **GC-MC/RMD** explores **Pd\(^{4+}\)**-like stabilization in **PdO\(_x\)** partially embedded in **CeO\(_2\)** and reports **methane activation barriers** on those motifs. **Functional**, **basis**, and **k**-mesh details are **N/A —** not tabulated here—see the article/SI.

**RMD** staging after **GC-MC** (timestep, thermostat, production length for methane activation) is **N/A —** not duplicated on this page; see **`pdf_path`**. **GC-MC**/**RMD** cells use **PBC**; the supported slab **supercell** is **39.8 × 33.9 × 75.0 Å** in the letter excerpt, with **Pd**/**Ce**/**O** **atoms** arranged as published. Unless quoted above, **NVT**/**NPT** staging for **RMD**, **timestep** (fs), **equilibration**/**production run** lengths (ps/ns), **thermostat** and **barostat**/**pressure** beyond the **GC-MC** **oxygen pressure** range (**10\(^{-20}\)**–**1 atm** at **500 K**), and **temperature** ramps for **RMD** are **N/A —** on this page. Shear, **electric field** driving, and **umbrella**/**metadynamics**/**replica-exchange** workflows are **N/A —** unless the full text adds them.

## Findings

**Outcomes.** **GC-MC** shows higher **O:Pd** ratios for **embedded** versus **supported** clusters across the **oxygen pressures** surveyed, consistent with **Pd** migrating toward **oxide** coordination at **defect** sites. **RMD** indicates **rapid methane light-off** when **Pd** **mixes** into the **ceria** lattice in the scenarios highlighted in the abstract.

**DFT refinement.** **DFT** on models informed by **GC-MC/RMD** reports **Pd\(^{4+}\)**-like states stabilized in **PdO\(_x\)** **partially embedded** in **CeO\(_2\)**, with **low barriers** for **methane activation** on those motifs as stated in the letter.

**Interpretation.** The authors frame a **combined ReaxFF + DFT** workflow for **emergent** **Pd/CeO\(_2\)** interface morphology and **electronic-structure**-sensitive **activation** chemistry.

## Limitations

Multistep workflows can be **sensitive to classical interface sampling**; quantitative **barriers** and **electronic** assignments should be traced to **DFT** sections and tables in **`pdf_path`**. Corpus **`year`** may differ from the **ACS Catal.** volume year on the PDF—use publisher metadata when citing pagination.

## Relevance to group

Direct **van Duin-group** ReaxFF + **catalysis** interface study connecting **oxide-supported Pd** with **methane chemistry**.

## Citations and evidence anchors

- DOI: [10.1021/acscatal.6b02447](https://doi.org/10.1021/acscatal.6b02447)
- Primary PDF: `papers/Senftle_ACS_Catalysis_2017.pdf`
- Text-aligned pointers: `normalized/extracts/2016senftle-venue-cs6b02447_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[theme-catalysis-surfaces]]
