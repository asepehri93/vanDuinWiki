---
id: paper:2013yang-chemical-phy-self-weakening-lithiated
type: paper
title: "Self-weakening in lithiated graphene electrodes"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - material:graphene-carbon-nano
  - method:reaxff
  - domain:reactive-md
  - domain:mechanics-tribology
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.cplett.2013.01.048"
year: 2013
authors:
  - "Yang, Hui"
  - "Huang, Xu"
  - "Liang, Wentao"
  - "van Duin, Adri C. T."
  - "Raju, Muralikrishna"
  - "Zhang, Sulin"
venue: "Chemical Physics Letters"
pdf_sha256: "da9fdabd46aa7af125dcb75d8d3ac66f81405f3d61dce4fa8ba086abd4f96985"
pdf_path: "papers/CP_Letter_LiC_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013yang-chemical-phy-self-weakening-lithiated -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **Chemical Physics Letters** article (**Chem. Phys. Lett.** **563**, **58–62**, 2013) studies **mechanochemical coupling** in **lithiated graphene** models relevant to **Li-ion battery anodes**. A **reactive force field (ReaxFF-class)** parametrization is used so that **lithium uptake**, **stress**, and **fracture** can be treated in the same **large-scale MD** framework. The work emphasizes that **Li diffusion** and **mechanical stress** are strongly coupled in these **carbonaceous** systems: **Li** tends to migrate toward **crack tips**, where accumulation can **modulate crack growth and instability**, linking atomistic behavior to electrode **degradation** and **lifetime** questions for **graphene-based** architectures. The local corpus PDF is a **proof/galley** (`CP_Letter_LiC_galley.pdf`); the **version-of-record** text and figures are defined by **DOI `10.1016/j.cplett.2013.01.048`**. The **self-weakening** framing contrasts **purely elastic** estimates of **graphene** **strength** with scenarios where **Li** **ingress** **plasticizes** or **destabilizes** the **carbon** lattice at **defects**.

## Methods

**Corpus honesty (proof PDF).** `papers/CP_Letter_LiC_galley.pdf` on this slug is an **Elsevier author-query / proof** bundle; `normalized/extracts/2013yang-chemical-phy-self-weakening-lithiated_p1-2.txt` contains **highlights** and production boilerplate, not the full **Chem. Phys. Lett.** **Methods** text. For **reproducible** **MD** settings (**engine**, **timestep**, **ensemble**, **thermostat**, **system size**, **loading protocol**), use **`paper:2013yang-chemical-phy-self-weakening-lithiated-2`** (`papers/Yang_Huang_Zhang_Raju_CPLetters_2013.pdf`) or the **DOI** version-of-record.

**1 — MD application (atomistic dynamics).** This **proof** ingest does not reproduce runnable **MD** settings. For orientation only: the **highlights** reference **atomistic** **molecular dynamics**-style modeling where **Li atoms** evolve near **crack** tips in **graphene** electrodes, implying **three-dimensional periodic boundary** treatment in the **VOR** letter (**N/A —** not evidenced on this PDF). **Ensemble / thermostat / timestep / duration / barostat / hydrostatic pressure:** **NVT**/**NVE**/**NPT** labels are **not** recoverable from this **proof** PDF—use **`paper:2013yang-chemical-phy-self-weakening-lithiated-2`** for the **VOR** **Methods** (**NVT** relaxation at **10 K** is documented there, not here). **Temperature:** **N/A —** not stated in the proof highlights excerpt.

**2 — Force-field training.** **N/A —** not recoverable from the **proof** excerpt beyond the highlight line claiming **development** of a reactive model—see the **VOR** PDF on the sibling slug.

**3 — Static QM / DFT-only.** **N/A —** reactive **MD** is implied by the **highlights**, not **DFT** benchmarks, on this ingest path.

## Findings

**Corpus honesty.** Quantitative **fracture metrics**, **Li** configurations, and mechanistic sentences on this page should **not** be sourced from the **proof** extract alone. For the letter’s quantitative **\(\hat{K}_I\)** results and **Li** tip motifs (**X0–X3**), use **`paper:2013yang-chemical-phy-self-weakening-lithiated-2`**.

**Outcomes & mechanisms (highlights only).** The Elsevier **highlights** list claims: a **reactive FF** for **lithiated carbonaceous** materials; **strong coupling** of **Li diffusion** and **stress**; energetically favorable **Li migration toward crack tips**; **tip accumulation** modulating **crack instability**; implications for **graphene-based electrode** lifetime.

**Comparisons / sensitivity / limitations.** **N/A —** not present in the **proof** excerpt beyond slogan-level bullets; read **VOR** article for authored comparisons and caveats.

## Limitations

The local **normalized extract** on file is **proof correspondence plus highlights only**; quantitative values, figures, and full methodological detail should be taken from the **published CPL article** at the DOI above. **Electrolyte** **composition** and **SEI** **formation** are not resolved in the excerpts available in this corpus snapshot.

## Relevance to group

van Duin and Raju coauthorship on Li–graphene mechanical coupling relevant to battery anode modeling.

## Citations and evidence anchors

- Highlights list (extract).
- DOI taken from normalized bibliography venue string `doi:10.1016/j.cplett.2013.01.048` in `normalized/papers/2013yang-chemical-phy-self-weakening-lithiated.json`.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- [[graphene-nanocarbon]]
