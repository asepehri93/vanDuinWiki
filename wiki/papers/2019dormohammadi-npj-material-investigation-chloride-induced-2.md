---
id: paper:2019dormohammadi-npj-material-investigation-chloride-induced-2
type: paper
title: "Investigation of chloride-induced depassivation of iron in alkaline media by reactive force field molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:water-silica-geo
  - material:metal-surface
  - material:cement-mineral
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:oxide-surface
  - keyword:reactive-md
source_refs: []
doi: "10.1038/s41529-019-0081-6"
year: 2019
authors:
  - "Hossein DorMohammadi"
  - "Qin Pang"
  - "Pratik Murkute"
  - "Liney Arnadottir"
  - "O. Burkan Isgor"
venue: "npj Materials Degradation 3, 19 (2019)"
pdf_sha256: "0f9b60309902058eae051d3b7939cb17d52e0576588a8d0b8c25433651b42d18"
pdf_path: "papers/ReaxFF_others/DorMohammedi_NatureMatDeg_2019_FeCl.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019dormohammadi-npj-material-investigation-chloride-induced-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    This slug registers a **second corpus path** (`papers/ReaxFF_others/DorMohammedi_NatureMatDeg_2019_FeCl.pdf`) for the same **npj Materials Degradation** article as [[2019dormohammadi-npj-material-investigation-chloride-induced]]. Full protocol locators and evidence anchors follow the canonical page.

## Summary

**Chloride** attack on **passive iron** in **alkaline media** matters for **reinforced concrete** and **corrosion-resistant alloys**, yet atomistic mechanisms must reconcile **thin-film** chemistry with **macroscopic** **polarization** data. **npj Materials Degradation** emphasizes **interface** **science** accessible to **materials** and **civil** **engineers**, so the **simulation** **cells** deliberately **isolate** **Fe** **electrochemistry** from **cement** **pore** **solution** **complexity** while still **capturing** **chloride**-catalyzed **vacancy** **physics** argued to be **transferable** across **substrates**. **DorMohammadi**, **Pang**, **Murkute**, **Arnadottir**, and **Isgor** combine **ReaxFF MD** with **electrochemical** measurements and **XPS** on **Fe** electrodes in **pH ~13.5 NaOH** with **chloride** additions. The **npj Materials Degradation** article argues **chloride** accelerates **iron-vacancy** creation and **migration** within the **oxide**, promoting **local acidification** and **Fe** **dissolution** without requiring classical **film penetration** as the sole mechanism. This wiki slug mirrors **`[[2019dormohammadi-npj-material-investigation-chloride-induced]]`** but records a **second PDF path** under `papers/ReaxFF_others/` with distinct **SHA-256** provenance.

## Methods

This slug is a **duplicate corpus path** for the same **npj Materials Degradation** article as **`[[2019dormohammadi-npj-material-investigation-chloride-induced]]`**.

**Experiments + spectroscopy.** Follow the **canonical** page for **electrochemical** + **XPS** specimen preparation and measurement narratives.

**Reactive MD protocol (same article).** **`[[2019dormohammadi-npj-material-investigation-chloride-induced]]`** summarizes the **LAMMPS**/**ReaxFF** workflow as published: **300 K**, **NVT** with **Nosé–Hoover** **thermostat**, **0.1 fs** **timestep**, **COM** constraint, **Fe/oxide/electrolyte** **supercell** with **3D periodic boundary conditions (PBC)** (see canonical page for **atom** counts and **slab**/**vacuum** dimensions), **energy minimization** plus **equilibration**/**production** stages out to **multi-nanosecond** totals discussed in the **Results** (**PDF**). **Hydrostatic pressure:** **N/A —** **NVT** cell rather than **NPT** servocontrol in the excerpted protocol.

**Electric fields / enhanced sampling.** **N/A —** not summarized as a distinct applied-field MD workflow on this duplicate-ingest note (see canonical page + PDF for any field-coupling approximations discussed by the authors).

## Findings

**Depassivation** follows a **multi-step** sequence: **local pH** drops at **oxide** defects, **Fe** **dissolves**, and **Fe vacancies** accumulate inside the **passive** layer; **chloride** **catalyzes** **vacancy** **nucleation** and **hops** toward the **metal**, amplifying **breakdown** relative to **chloride-free** **alkaline** controls. **XPS** and **polarization** curves support the qualitative **current** and **composition** trends inferred from **MD**. For **figure** numbers and **SI** tables, use the **canonical** page unless this **duplicate** PDF is required for **manifest** auditing. The **npj Materials Degradation** framing ties **atomistic** **vacancy** **physics** to **rebar** **corrosion** contexts where **alkaline** **pore** **solutions** coexist with **chloride** **ingress**, even though the simulations use **model** **Fe** **electrodes** rather than **cement** **paste** **microstructures**.

## Limitations

**Simplified** substrates vs industrial **steels**; **MD** time and length scales; duplicate PDF only changes **provenance**, not scientific limits.

## Relevance to group

**ReaxFF** application to **corrosion** and **passivation** in **alkaline** environments; this file preserves **hash-disambiguated** ingest.

## Citations and evidence anchors

- DOI: [10.1038/s41529-019-0081-6](https://doi.org/10.1038/s41529-019-0081-6) — this artifact: `papers/ReaxFF_others/DorMohammedi_NatureMatDeg_2019_FeCl.pdf`.

## Reader notes (navigation)

- **Canonical article page:** [[2019dormohammadi-npj-material-investigation-chloride-induced]] (`papers/ReaxFF_others/DorMohammadi_npjMatDeg_FeClNa_2019.pdf`).

## Related topics

- [[2019dormohammadi-npj-material-investigation-chloride-induced]]
- [[reaxff-family]]
