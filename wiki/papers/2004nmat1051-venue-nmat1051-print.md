---
id: paper:2004nmat1051-venue-nmat1051-print
type: paper
title: "Large electric-field-induced strain in ferroelectric crystals by point-defect-mediated reversible domain switching"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - method:classical-md
  - task:application
candidate_tags: []
source_refs: []
doi: "10.1038/nmat1051"
year: 2004
authors:
  - "Xiaobing Ren"
venue: "Nat. Mater."
pdf_sha256: "6b7a902e96317be94b78e83ec53f6dc48e62027b7f6bba06dc57e59c5e095ec1"
pdf_path: "papers/Others/nmat1051_ferroelectric_electric_field.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2004nmat1051-venue-nmat1051-print -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Ferroelectric crystals develop **electric-field-induced strain** when ions displace under **polarization**; conventional **piezoelectric** responses are **small**, limiting actuators. The **letter** reports that **aged BaTiO\(_3\)** **single crystals** can generate a **large, recoverable nonlinear strain ~0.75%** at only **200 V mm\(^{-1}\)**. At the same field, the author states this strain is **~40×** larger than typical **PZT ceramics** and **>10×** larger than high-strain **PZN–PT** single crystals cited for comparison. The mechanism is **reversible non-180° domain switching** where **point defects** exhibit **symmetry-conforming** behavior that provides a **restoring force**, enabling **repeatable** macroscopic strain—contrasting with usual **non-180°** switching between **degenerate** domain states that is **one-time** because no thermodynamic drive restores the initial texture.

## Methods


**Experimental materials / protocol (checklist D)**—no atomistic simulation.

- **Material / state:** **BaTiO\(_3\)** **single crystals** subjected to **aging** treatments that enable the reported **reversible** **non-180°** switching phenomenology (details of **aging** time/temperature and **electrode** configuration are in the **letter** + any **methods** supplements; **not fully reproduced** in the short corpus extract).
- **Drive / measurement:** **electric-field**-induced **strain** and **domain** behavior under **cycling**; the **letter** highlights a **large recoverable strain ~0.75%** at **200 V mm\(^{-1}\)** and compares against **PZT** **ceramic** and **PZN–PT** **single-crystal** benchmarks quoted therein (*Nat. Mater.* **3**, **91** (2004); **DOI** **10.1038/nmat1051**).
- **Operators:** verify **figure** numbering, **SI** pointers, and **pagination** against the **Nature Materials** PDF—`extraction_quality` metadata is **good** but **full** procedural parameters should be taken from the **primary PDF**.

### MD application (not reported)

This **Nature Materials** letter is an **experimental** **single-crystal** **electromechanics** study, not an atomistic **molecular dynamics** paper. **N/A — MD engine**; **N/A — atom counts** (no atomistic supercell reported here); **N/A — PBC**; **N/A — NVE/NVT/NPT** MD; **N/A — timestep**; **N/A — trajectory length** (no **ps**/**ns** MD); **N/A — equilibration** MD stages; **N/A — thermostat**; **N/A — barostat**; **N/A — MD temperature control**; **N/A — MD pressure control**; **N/A — replica exchange / umbrella sampling** in MD. **Electric field:** macroscopic **bias** is central to the experiment (**~0.75%** recoverable strain at **200 V mm\(^{-1}\)** as stated in the letter), not a simulated **E-field** in an MD sense. Grounding: `papers/Others/nmat1051_ferroelectric_electric_field.pdf`, `normalized/extracts/2004nmat1051-venue-nmat1051-print_p1-2.txt`.

## Findings

- **Electromechanical response:** reports **very large** **recoverable** **nonlinear strain** (**~0.75%**) at **200 V mm\(^{-1}\)**, claimed **~×40** vs a cited **PZT** **ceramic** and **>×10** vs a cited high-strain **PZN–PT** **single crystal** at comparable field (*Nat. Mater.* **3**, **91**).
- **Mechanism (as argued in the letter):** **reversible** **non-180°** **domain switching** assisted by **point defects** in a **symmetry-conforming** regime—yielding a **restoring** tendency absent in **degenerate** **non-180°** states that would otherwise be **one-time** switching.
- **Broader claim:** **defect–domain engineering** may unlock **large electrostrain** together with **cyclability**, distinct from optimizing linear **piezoelectric** coefficients alone.
- **Comparisons:** strain and field responses are **compared** to cited **PZT** **ceramic** and **PZN–PT** **single-crystal** benchmarks in the letter.
- **Sensitivity / design levers:** the highlighted effect depends on **field** amplitude (**200 V mm\(^{-1}\)** in the abstract/letter) and the **aged** **BaTiO\(_3\)** preparation pathway.
- **Limitations / outlook (authors vs scope):** the **letter** emphasizes a **mechanism** narrative over exhaustive microstructural statistics; **thin films** and other chemistries may differ (**Limitations** section below).
- **Corpus honesty:** this wiki page is grounded in **`pdf_path`** and the short extract; **figure**-level timing should be taken from the **PDF**, not inferred here.

## Limitations

Demonstrated on **BaTiO\(_3\)** with a specific **aging** history; **thin films**, **different dopants**, and **other ferroelectrics** may not replicate the effect without targeted **defect engineering**. This corpus entry is **not** a **ReaxFF** paper—use it as **ferroelectric mechanics** context adjacent to **perovskite** simulation pages. The **letter** format emphasizes **mechanism** over **exhaustive** **microstructural** statistics; consult the **full PDF** for any **supplementary** **characterization** referenced in the journal version.

## Relevance to group

**Ferroelectric** **mechanics** context largely outside **reactive MD**, but relevant when comparing **multiphysics** **actuation** literature with **materials modeling** portfolios. The **defect-mediated reversible switching** narrative complements **perovskite** **ReaxFF** pages that focus on **polarization** and **surfaces** rather than **macroscopic actuator** strain metrics.

## Citations and evidence anchors

- **DOI:** https://doi.org/10.1038/nmat1051 — *Nat. Mater.* **3**, 91 (2004); `papers/Others/nmat1051_ferroelectric_electric_field.pdf`; extract `normalized/extracts/2004nmat1051-venue-nmat1051-print_p1-2.txt` (letter text).

## Related topics

- [[reaxff-family]]
