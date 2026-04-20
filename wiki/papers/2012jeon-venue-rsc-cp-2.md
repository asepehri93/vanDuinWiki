---
id: paper:2012jeon-venue-rsc-cp-2
type: paper
title: "Nanoscale oxidation and complex oxide growth on single crystal iron surfaces and external electric field effects"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:oxides-ceramics, domain:alloys-metallurgy, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1039/c2cp43490c"
year: 2013
authors: ["Jeon, Byoungseon", "Van Overmeere, Quentin", "van Duin, Adri C. T.", "Ramanathan, Shriram"]
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "7ef19c15c7329975b7bc6b70f26bffc88538178d5d05dc084d54350b0ba214d2"
pdf_path: "papers/Jeon_PCCP_Iron_Efield_2013.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2012jeon-venue-rsc-cp-2 -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This PCCP study uses **ReaxFF reactive MD** to investigate **early-stage oxidation** and **nanoscale oxide growth** on **Fe(100), Fe(110), and Fe(111)** across temperature and with an optional **external electric field (~10 MV/cm)**. At **300 K** over **~1 ns**, oxidation kinetics decreases **(110) > (111) > (100)**; higher temperature accelerates oxidation. The mechanism narrative in the excerpt emphasizes early **oxygen interstitial transport** producing **non-stoichiometric wüstite-like** regions, evolving toward more stoichiometric **wüstite/hematite** character as the film thickens, with increasing **cation outward transport**. Post-growth **relaxation** between **600–1500 K** yields **Arrhenius** estimates for **oxygen diffusion activation energies** ~**0.32, 0.26, 0.28 eV** on (100), (110), (111), respectively. The field **accelerates early oxidation** via interstitial oxygen transport but approaches a **self-limiting thickness**; effects on **activation energy** are described as **minimal** while slightly promoting **cation outward migration**.

## Methods

- **ReaxFF** with bond-order-based reactivity and charge equilibration (per article discussion) for **Fe–O** oxidation trajectories; electric field protocol as stated in the paper.

## Findings

- Orientation-dependent oxidation rates and a two-stage kinetic picture (fast initial stage transitioning to slower growth).
- Estimated **O diffusion** barriers in relaxed oxide from high-temperature Arrhenius fits (values quoted above).
- Electric field: helps early oxidation kinetics; limited impact on final oxide thermochemistry in the claims excerpted.


## Limitations

- Classical reactive FF uncertainty for **defect-rich oxides** and long-time **phase evolution**; field representation is model-dependent.

## Relevance to group

Strong example of **ReaxFF for metal oxidation** and **electrochemically biased** oxide growth—useful alongside other Fe/Ni aqueous oxidation entries.

## Citations and evidence anchors

- Abstract and Sec. 1–2 opening: kinetics ordering, mechanism narrative, diffusion activation energies, field effects (Phys. Chem. Chem. Phys., 2013, 15, 1821–1830; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]