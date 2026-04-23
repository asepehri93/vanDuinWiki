---
id: paper:2013al-venue-reactive-molecular
type: paper
title: "Reactive molecular dynamics simulations of oxygen species in a liquid water layer of interest for plasma medicine"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:water-silica-geo, domain:reactive-md, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1088/0022-3727/47/2/025205"
year: 2014
authors: ["Yusupov, M.", "Neyts, E. C.", "Simon, P.", "Berdiyorov, G.", "Snoeckx, R.", "van Duin, A. C. T.", "Bogaerts, A."]
venue: "Journal of Physics D: Applied Physics"
pdf_sha256: "5bc2241aadaaeee20dd7883c7173dbe0312f11b75a81ee6126a0dc43f21b4729"
pdf_path: "papers/Yusupov_JPhysD_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013al-venue-reactive-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The study uses **ReaxFF reactive MD** (C/H/O/N **glycine/water** parameter set cited as **Rahaman et al.**) to probe **ROS** (**O, OH, HO₂, H₂O₂**) impinging on a **liquid water** film as a surrogate for the aqueous layer around **bacteria** in **cold atmospheric plasma (CAP)** applications. The abstract reports **OH, HO₂, and H₂O₂** can penetrate deeply into the liquid, while **O, OH, and HO₂** undergo **H-abstraction** from water; **H₂O₂** does **not** show H-abstraction in the stated simulations. The motivation is to clarify whether plasma species reach biomolecules directly or react en route through the biofilm water.

## Methods

### Force-field training

**N/A —** the study **employs** an existing **ReaxFF** parameterization for **C/H/O/N** chemistry from **Rahaman et al.** (glycine/water set cited in the article; **`pdf_path`** for full citation).

### MD application (atomistic dynamics)

**Engine / code:** **Reactive molecular dynamics** (**ReaxFF**); **N/A —** integrator package name not recovered from `normalized/extracts/2013al-venue-reactive-molecular_p1-2.txt` (abstract/intro only)—see **`pdf_path`**.

**System & composition:** **Liquid water** layer as a surrogate for the aqueous film around **bacteria**; incident **ROS** species **O**, **OH**, **HO\(_2\)**, **H\(_2\)O\(_2\)** (abstract).

**Boundaries / periodicity:** **N/A —** cell geometry and **PBC** details not on the indexed excerpt pages.

**Ensemble / timestep / duration / thermostat / barostat / explicit temperature setpoints:** **N/A —** not stated in `2013al-venue-reactive-molecular_p1-2.txt`; read **`pdf_path`**. The sibling page **`[[2013al-venue-reactive-molecular-2]]`** records **NVT** water-slab equilibration details for the same DOI when operators need a quick in-wiki pointer.

**Pressure:** **N/A —** not stated in the excerpt.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not stated in the excerpt.

## Findings

**Outcomes:** The abstract reports that **OH**, **HO\(_2\)**, and **H\(_2\)O\(_2\)** can penetrate deeply into the **liquid water** layer and therefore could reach a bio-organism after traversing the film. **O**, **OH**, and **HO\(_2\)** undergo **hydrogen-abstraction** reactions with **water**, whereas **H\(_2\)O\(_2\)** does **not** show **H-abstraction** in their simulations.

**Comparisons:** Framed against the need to understand **plasma–liquid** interactions before species contact cells (**abstract**).

**Sensitivity:** **Species-dependent** reactivity (**abstraction** vs **diffusive penetration**) controls which **ROS** remain aggressive within the film.

**Limitations:** **O\(_3\)** and **RNS** are excluded in-force-field as noted in the article (beyond **ROS** subset studied). **`2013al-venue-reactive-molecular_p1-2.txt`** is **intro-heavy**; quantitative **MD** settings require **`pdf_path`**.

**Corpus honesty:** Prefer **`[[2013al-venue-reactive-molecular-2]]`** when you need the **J. Phys. D** PDF with Methods figures cited in that sibling note.

## Relevance to group

Connects **ReaxFF** to **plasma–liquid–biomolecule** transport chemistry—a distinct application area from solid-state materials, but methodologically aligned.

## Citations and evidence anchors

- Abstract and Secs. 1–2: motivation, species list, force-field citation, simulation rationale (J. Phys. D: Appl. Phys. 47 (2014) 025205; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
