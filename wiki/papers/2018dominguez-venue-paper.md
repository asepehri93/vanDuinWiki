---
id: paper:2018dominguez-venue-paper
type: paper
title: "Deuterium uptake and sputtering of simultaneous lithiated, boronized, and oxidized carbon surfaces irradiated by low-energy deuterium (publisher proof)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:graphene-carbon-nano
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1063/1.5026415"
year: 2018
authors:
  - "F. J. Domínguez-Gutiérrez"
  - "P. S. Krstić"
  - "J. P. Allain"
  - "F. Bedoya"
  - "M. M. Islam"
  - "R. Lotfi"
  - "A. C. T. van Duin"
venue: "J. Appl. Phys. (proof PDF; see sibling for VOR-style ingest)"
pdf_sha256: "0666227cb071913845c95c3cccdead745be6a73714d4bf718434d4a1100b9d1f"
pdf_path: "papers/Dominguez_Gutierrez_JAP_2018_deuterium_update_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2018dominguez-venue-paper -->

**Publisher proof PDF** (layout/author-query banner) for the **J. Appl. Phys.** study of **low-energy D** bombardment of **Li–B–C–O** amorphous carbon surfaces with **ReaxFF** extended for **B** and **Li**. Scientific content matches [[2018f-j-dom-nguez-guti-r-journal-of-a-deuterium-uptake]]; prefer that page for **pagination** and **figure** citation.

## Summary

**Reactive MD** with **ReaxFF** (EEM charges, **LAMMPS**) quantifies **D retention** and **sputtering** for plasma-facing **carbon** conditioned with **Li**, **B**, and **O**, comparing to **new experiments** on **B–C–O–D** systems. The work interprets how **oxygen** and **mixed conditioning** tune **erosion** vs **retention** of **D** at fusion-relevant **low impact energies**. **Tokamak** and **stellarator** first walls see **low-Z** **carbon** tiles and **mixed-material** coatings where **lithium** injectors, **boronization**, and **oxygen** recycling all change **near-surface** stoichiometry; matching **simulation** to **beam** or **plasma** exposure data therefore requires **chemically specific** **ReaxFF** extensions for **Li–B–C–O–D** rather than pure **hydrocarbon** carbon models.

## Methods

Same protocol as [[2018f-j-dom-nguez-guti-r-journal-of-a-deuterium-uptake]] (**Sec. II** in the VOR PDF): **ReaxFF** **Li–B–C–O–D** trained vs **NWChem** **PBE0/6-31G*** benchmarks; **~400-atom** surface cells (**~1.8 nm** lateral, **~2.0 nm** depth); melt/quench + **300 K** **Langevin** preparation; **D** impacts at **5 eV** (retention) and **5 eV** / **30 eV** (sputtering) with **50 ps** spacing, **20 ps** cascade + **20 ps** rethermalization + **10 ps** relax; **N = 15000** impacts for production statistics. This slug’s PDF is the **proof** variant—typography may differ from the **version of record**.

**MD packaging:** Simulations are run in **LAMMPS** with **ReaxFF** on **~400-atom** **slab** supercells under **3D PBC**. Each impact cycle uses **~20 ps** **NVE**-like cascade evolution, **~20 ps** rethermalization toward **300 K** with **canonical** sampling as in Sec. II, then **~10 ps** relaxation—**durations** on the **picosecond** scale between impacts. The **timestep** is specified in Sec. II of the **version-of-record** **PDF** on [[2018f-j-dom-nguez-guti-r-journal-of-a-deuterium-uptake]]. **N/A — NPT barostat** and **N/A — fixed hydrostatic pressure** targets for the documented bombardment recipe (constant-volume **slab** protocol).

## Findings

- **Oxygen** participates in **D** bonding pathways across compositions; combined **experiment + simulation** highlight retention mechanisms in **B–Li–C–O** mixtures.
- **Boron** can **reduce carbon erosion** vs reference surfaces; **lithium** modulates **oxygen** surface content under **D** bombardment in the regimes discussed.
- **Mixed Li + B + O** conditioning acts as a knob for **erosion/retention** trade-offs relevant to **fusion PFC** materials. The companion **version-of-record** page (**[[2018f-j-dom-nguez-guti-r-journal-of-a-deuterium-uptake]]**) should be cited for **final** **figure** labels and **pagination** when preparing **benchmark** questions; this **proof** slug exists mainly for **manifest** provenance.

## Limitations

Proof PDF may lack final pagination; **classical reactive** models omit explicit **electronic** sputtering. Full methodological tables: [[2018f-j-dom-nguez-guti-r-journal-of-a-deuterium-uptake]].

**Magnetic** **field** effects, **impurity** **atoms** beyond **Li–B–C–O–D**, and **long-time** **diffusive** **mixing** in **tokamak** **tiles** are outside the **single-impact** **statistics** emphasized in the **Sec. II** protocol; upscaling to **reactor** **wall** **lifetimes** requires **multiscale** **models** layered on top of these **ReaxFF** **cross sections**.

## Relevance to group

**van Duin** coauthorship on **ReaxFF** for **fusion** boundary plasmas; this file records **proof-stage** corpus provenance.

## Reader notes (navigation)

- Version-of-record wiki: [[2018f-j-dom-nguez-guti-r-journal-of-a-deuterium-uptake]].

## Related topics

- [[2018f-j-dom-nguez-guti-r-journal-of-a-deuterium-uptake]]
- [[reaxff-family]]
