---
id: paper:2019akbarian-polymer-183-atomistic-scale-insights
type: paper
title: "Atomistic-scale insights into the crosslinking of polyethylene induced by peroxides"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - material:polymer-organic
  - method:reaxff
  - task:experiment-integrated
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.polymer.2019.121901"
year: 2019
authors:
  - "Dooman Akbarian"
  - "Hossein Hamedi"
  - "Behzad Damirchi"
  - "Dundar E. Yilmaz"
  - "Katheryn Penrod"
  - "W. H. Hunter Woodward"
  - "Jonathan Moore"
  - "Michael T. Lanagan"
  - "Adri C. T. van Duin"
venue: "Polymer"
pdf_sha256: "5a2f6955f45b24df2928c0caded395bf66985f1ea7ab21a5521178610ede86cf"
pdf_path: "papers/Akbarian_Polymer_2019.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2019akbarian-polymer-183-atomistic-scale-insights -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

**ReaxFF molecular dynamics** is combined with **FTIR mapping** and **wide-angle X-ray scattering (WAXS)** to dissect **peroxide-induced crosslinking** of **polyethylene (PE)**—motivated by **dicumyl peroxide (DCP)** chemistry in **high-voltage cable** **XLPE** insulation. The study reports **non-monotonic** behavior of **crosslink extent** with **curing temperature** (moderate heating to **~500 K** helps; **excessive** temperature can hurt), **density** effects, and **peroxide loading** trade-offs between **byproduct** formation and **XLPE** yield. **Electric field** in the **MD** protocol is found to have **little effect** on crosslinking, and an **alternative peroxide** is argued to be **less efficient** than **DCP** under the modeled conditions. **Adri C. T. van Duin** is a corresponding author with **Penn State** and **Dow** collaborators.

## Methods

- **ReaxFF MD** of **PE + peroxide** mixtures under varied **temperature**, **density**, **stoichiometry**, and optional **field** (see **Polymer** for simulation cells).
- **FTIR** and **WAXS** on **cured** samples to **validate** **structural** and **crosslink** trends.

## Findings

- **Atomistic** models reproduce **key experimental** trends for **crosslinking** extent and **byproduct** burden across the **processing** window explored.
- **High DCP:PE** can **increase byproducts** without proportionally increasing **XLPE** quality, informing **formulation** choices.

## Limitations

- **Industrial** **XLPE** recipes include **additives** and **multiphase** morphology not fully captured in **idealized** **MD** cells.
- **ReaxFF** for **hydrocarbon + peroxide** chemistry should be **spot-checked** against **QM** when **new** initiators are studied.

## Relevance to group

**Industry-facing** **ReaxFF** application to **polyolefin crosslinking** with **experimental** validation—parallel to other **group** **polymer** reactive MD papers.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.polymer.2019.121901` (`papers/Akbarian_Polymer_2019.pdf`).

## Related topics

- [[reaxff-family]]
