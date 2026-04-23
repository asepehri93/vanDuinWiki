---
id: paper:2019kwon-venue-paper
type: paper
title: "Numerical simulations of yield-based sooting tendencies of aromatic fuels using ReaxFF molecular dynamics (uncorrected proof)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2019.116545"
year: 2019
authors:
  - "Hyunguk Kwon"
  - "Sharmin Shabnam"
  - "Adri C. T. van Duin"
  - "Yuan Xuan"
venue: "Fuel (uncorrected proof PDF in corpus)"
pdf_sha256: "b1287861455fc265637f719bb1545bd6eade01ad36580bb6a61a5df345b58acc"
pdf_path: "papers/Kwon_Fuel_2019_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2019kwon-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Corpus note:** this slug registers an **Elsevier uncorrected proof** (`papers/Kwon_Fuel_2019_proof.pdf`). The **same** **Fuel** article is curated on **`[[2019kwon-fuel-correct-numerical-simulations]]`** using the **online** PDF (`papers/Kwon_Fuel_2019_online.pdf`). Maintainer catalog: `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`. **Sooting** **science** readers should remember that **YSI** **metrics** integrate **multiple** **experimental** **protocols**; the **ReaxFF** **workflow** here is **explicitly** **benchmarked** against **toluene** and **phenol** because those **fuels** have **well-tabulated** **YSI** **values** and **recognized** **soot** **pathways**. Scientifically, **Kwon**, **Shabnam**, **van Duin**, and **Xuan** build a **ReaxFF MD** pipeline that maps **gas-phase** **soot-precursor** chemistry to a **Yield Sooting Index (YSI)**-style metric for **aromatic** fuels. **Multi-stage** **post-processing** mirrors **experimental** **YSI** definitions by combining **trajectory**-derived **species** **yields** with **normalization** rules described in **Fuel**. **Toluene** and **phenol** anchor the validation because their **sooting** chemistry is **well mapped** experimentally.

## Methods

This **corpus** **slug** tracks an **uncorrected** **Elsevier** **proof** (`papers/Kwon_Fuel_2019_proof.pdf`); **pagination** and **table** **numbering** may differ from the **VOR**. The **VOR**-aligned **RMD** uses **3D** **PBC** **(cubic** **~38.6** **Å,** **periodic** **x/y/z)**, a **CH₄**/**O₂** **soot**-favorable **pool,** **NVT** **heating** to **3000** **K** **(Berendsen** **thermostat,** **100** **fs** **damping** per *Fuel* **Sec. 2)**, then **NVT** at **2200** **K,** **2400** **K,** **2600** **K** **(five** **replica** **seeds)** on **doped** **pools** **(e.g. ~2308** or **~2224** **atoms,** *Fuel* **Sec. 2**)**. **Time** **histories** **run** **e.g. ~6** **ns** **at** **2200** **K** in the **VOR** **(shorter** **at** **higher** **T,** *Fuel* **Sec. 4.1**)**. **Time** **step (fs):** **N/A** in this **short** **summary**; **VOR** **/SI** **or** **`[[2019kwon-fuel-correct-numerical-simulations]]`**. **Reproducible** **line-by-line** **values:** **`[[2019kwon-fuel-correct-numerical-simulations]]`** and the **DOI** **VOR**. **Barostat** / **NPT** (mean **hydrostatic** stress): **N/A** (constant-**V** **NVT** in the **stated** **framework**). **Electric** **field** / **replica** / **metadynamics:** **N/A**. **FF** **fit** and **Kohn**–**Sham** **DFT:** see **`[[2019kwon-fuel-correct-numerical-simulations]]`** (**N/A** **/** **N/A** in **that** **article**).

## Findings

**ReaxFF** **qualitatively** reproduces **ring-retaining** versus **carbon-loss** **pathways**, including **CO** **evolution** motifs emphasized for **phenol**, and the **derived** **YSI** **numbers** **cluster** near **measurements** for the **benchmark** **set**. The **study** supports **relative** **ranking** of **sooting** **tendency** when **detailed** **kinetic** **models** are **unavailable**, while **absolute** **YSI** **accuracy** should be **quoted** from the **VOR** **page** for **publication** **tables**. **Fuel**-focused readers should note that **YSI** **workflows** depend on **post-processing** **definitions**—always **align** **simulation** **cuts** with the **experimental** **standard** cited in the **Methods** when **comparing** across **labs**. **Aromatic** **fuels** beyond **toluene**/**phenol** will stress **ReaxFF** **aromatic** **bond** **orders** differently, so **extension** **studies** should **revalidate** **YSI** **mappings** on a **fuel-by-fuel** basis.

## Limitations

**Proof** layout and pagination differ from the **version of record**; cite **`[[2019kwon-fuel-correct-numerical-simulations]]`** for stable figure/table references.

## Relevance to group

Duplicate corpus path for **Penn State** / **van Duin** **sooting** workflow traceability.

## Citations and evidence anchors

Prefer **`[[2019kwon-fuel-correct-numerical-simulations]]`**. DOI: https://doi.org/10.1016/j.fuel.2019.116545

## Related topics

- [[2019kwon-fuel-correct-numerical-simulations]]
- [[reaxff-family]]
