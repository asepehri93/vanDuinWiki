---
id: paper:2018dengpan-dong-in-this-stud-multiscale-modeling
type: paper
title: "Multiscale Modeling of Structure, Transport and Reactivity in Alkaline Fuel Cell Membranes: Combined Coarse-Grained, Atomistic and Reactive Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - material:polymer-organic
  - method:classical-md
  - method:hybrid-qmmm
  - method:reaxff
  - task:application
  - scale:multiscale
candidate_tags: []
source_refs: []
doi: "10.3390/polym10111289"
year: 2018
authors:
  - "Dengpan Dong"
  - "Weiwei Zhang"
  - "Adam Barnett"
  - "Jibao Lu"
  - "Adri C. T. van Duin"
  - "Valeria Molinero"
  - "Dmitry Bedrov"
venue: "Polymers"
pdf_sha256: "41070f46fe1677dbba14643c0055c2bdd320d8ec57a47b833c89712b43f2f74e"
pdf_path: "papers/Dong_Polymers_2018.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018dengpan-dong-in-this-stud-multiscale-modeling -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **open-access Polymers** article develops a **three-tier modeling chain** for **hydrated anion-exchange membranes (AEMs)** based on **functionalized poly(phenylene oxide)**: a **high-resolution coarse-grained** model for **morphology**, an **atomistic polarizable (APPLE&P)** model for **local hydration**, **ion–water structure**, and **vehicular transport**, and **ReaxFF** for **reactive** questions such as **hydroxide transport mechanisms** (including **Grotthuss-like** behavior as framed in the paper) and **chemical degradation** pathways. The authors argue that **no single model** can span this whole property space, but **sequential mapping** between resolutions enables **practical materials-by-design** guidance for **AEM** chemistry.

## Methods

- **CG equilibration** of **hydrated AEM** morphology, then **backmapping** to **APPLE&P** atomistic configurations.
- **Non-reactive atomistic MD** for **structure/transport** observables, then mapping to **ReaxFF** for **reaction** and **stability** analyses.

## Findings

- **Multiscale coupling** is presented as necessary to capture **morphology**, **ion correlations**, and **bond-breaking chemistry** in the same **material class**.
- **ReaxFF** is used where **proton/hydroxide** events and **decomposition** require **explicit reactivity**.


## Limitations

- **Mapping fidelity** between CG, polarizable atomistic, and ReaxFF representations introduces **uncertainty**; sensitive observables need **cross-checks**.
- **Parameter sets** and **water models** strongly affect **ionic conductivity** and **mechanistic attribution**.

## Relevance to group

**Adri C. T. van Duin** coauthorship anchors the **ReaxFF** segment of a **large collaborative** membrane modeling effort.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.3390/polym10111289` (`papers/Dong_Polymers_2018.pdf`).

## Related topics

- [[reaxff-family]]
