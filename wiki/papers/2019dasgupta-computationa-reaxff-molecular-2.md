---
id: paper:2019dasgupta-computationa-reaxff-molecular-2
type: paper
title: "ReaxFF molecular dynamics simulations on the structure and dynamics of electrolyte water systems at ambient temperature"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:nvt-simulation
  - keyword:galley-or-proof-pdf
  - keyword:lammps
source_refs: []
doi: "10.1016/j.commatsci.2019.109349"
year: 2019
authors:
  - "Nabankur Dasgupta"
  - "Yun Kyung Shin"
  - "Mark V. Fedkin"
  - "Adri C. T. van Duin"
venue: "Computational Materials Science (corrected proof, 2019)"
pdf_sha256: "0f952c099905e6a745210bde716fbfa51392e405dd72f046af2519154c106364"
pdf_path: "papers/Nabankur_2019_CompMatSci_electrolyte_in_press.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019dasgupta-computationa-reaxff-molecular-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    This ingest is an **Elsevier corrected proof** (`papers/Nabankur_2019_CompMatSci_electrolyte_in_press.pdf`) for the same article as [[2019dasgupta-computationa-reaxff-molecular]]. **Table** and **figure** numbering follow the **published** volume.

## Summary

**ReaxFF** molecular dynamics studies **aqueous LiCl**, **NaCl**, and **KCl** at **1–5 M** (plus **pure water**) at **300 K** using the **Fedkin** et al. **electrolyte–water** parameterization, reporting **RDFs**, **angular** distributions in the first **hydration shell**, **H-bond** and **reorientational** dynamics, **residence times**, and **diffusion coefficients**. This slug is an **in-press / proof** PDF variant; science matches [[2019dasgupta-computationa-reaxff-molecular]]. **Ambient** **electrolyte** structure benchmarks are useful for **battery** **electrolyte** **screening** and for validating **force-field** **ion–water** couplings before **interfacial** **runs** add **electrode** chemistry.

## Methods

**Molecular dynamics (MD) systems (same article as VOR).** **1000** water molecules (**pure water**) or **700** water molecules plus stoichiometric salt for **1–5 M** **LiCl**, **NaCl**, and **KCl**; **atom counts** follow from those water counts plus the ions tabulated on **`[[2019dasgupta-computationa-reaxff-molecular]]`** (**Table 1**). **Box volumes** use **ion van der Waals radii** and target **concentration** as in the published **Computational details**.

**Protocol.** **Minimization**, **compression**, heating to **300 K**, **100 ps** equilibration, **0.5 ns** production, **0.25 fs** timestep, **PBC**, and **Berendsen** thermostat (**100 fs** damping) as summarized on the **canonical** page.

**Ion concentration series.** The authors keep **box construction** and **neutralization** conventions consistent across concentrations so **RDF** comparisons are meaningful.

**Engine / code.** **LAMMPS** with **ReaxFF** (same article as **`[[2019dasgupta-computationa-reaxff-molecular]]`**; this duplicate-ingest note does not add a separate engine declaration beyond that canonical record).

**Barostat / pressure.** **N/A —** **fixed-volume** (**NVT**-like) workflow without **NPT** **hydrostatic pressure** servocontrol (see canonical page).
## Findings

- **ReaxFF** reproduces **solvation-shell** structure and **angular** behavior in line with cited **DFT**/literature references; **salt** concentration **reduces** **water** **self-diffusivity** in the regimes reported, with mechanistic discussion of **transient** **ionic** species on [[2019dasgupta-computationa-reaxff-molecular]].
- **Cation**-specific ordering trends (**Li** vs **Na** vs **K**) are interpreted through **hydration** **strength** and **pair** **correlation** shifts summarized on the **canonical** page.

## Limitations

**Proof** layout may differ cosmetically from the **paginated** **Comput. Mater. Sci.** article; **sub-ns** segments and **finite-size** effects apply as on the canonical page.

**Curation note:** this duplicate exists because the corpus retained both **in-press** and **final** PDF filenames; **DOI** `10.1016/j.commatsci.2019.109349` is **single**—keep **one** **canonical** narrative on [[2019dasgupta-computationa-reaxff-molecular]] and use this page for **provenance** of the **alternate** bytes. **Chunk** builders should hash the **canonical** page’s sections when generating **Phase 5** IDs for this topic. **Ambient** **300 K** **production** length **0.5 ns** matches the canonical **Comput. Mater. Sci.** protocol table.

## Relevance to group

**van Duin** co-authorship on **ambient** **electrolyte–water** **ReaxFF** built on the **Fedkin** line; this entry tracks **alternate** PDF bytes only.

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2019.109349](https://doi.org/10.1016/j.commatsci.2019.109349) — proof: `papers/Nabankur_2019_CompMatSci_electrolyte_in_press.pdf`; VOR: [[2019dasgupta-computationa-reaxff-molecular]].

## Reader notes (navigation)

- **Corpus catalog (corrected-proof duplicate):** [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (entry **2019dasgupta-computationa-reaxff-molecular-2**)
- **Published article page:** [[2019dasgupta-computationa-reaxff-molecular]] (`papers/Nabankur_2019_CompMatSci_electrolyte.pdf`)

## Related topics

- [[2019dasgupta-computationa-reaxff-molecular]]
- [[reaxff-family]]
