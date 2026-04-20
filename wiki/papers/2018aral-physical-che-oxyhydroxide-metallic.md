---
id: paper:2018aral-physical-che-oxyhydroxide-metallic
type: paper
title: "Oxyhydroxide of metallic nanowires in a molecular H2O and H2O2 environment and their effects on mechanical properties"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/C8CP02422G"
year: 2018
authors:
  - "Gurcan Aral"
  - "Md Mahbubul Islam"
  - "Yun-Jiang Wang"
  - "Shigenobu Ogata"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "95ddbda87a3e52094e92b1bedd1f666880d37664092ea9784fe80c7e154f49b8"
pdf_path: "papers/Aral_PCCP_FeO_OH_2018.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018aral-physical-che-oxyhydroxide-metallic -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

**ReaxFF reactive MD** is used to simulate **oxidation** of **iron nanowires** in **molecular H₂O** and **H₂O₂**, forming **iron oxide and oxyhydroxide** shells whose **microstructure** depends on the **oxidizing environment**. The work then connects these **oxide shells** to **tensile mechanical response**: pre-oxidation introduces **defect-prone regions** near the **metal–oxide interface**, lowering **yield stress** and **Young’s modulus** compared to cleaner wires, with **H₂O₂** oxidation producing especially **detrimental** mechanical weakening. **Deformation twinning** remains the dominant **plasticity** mechanism, but it **onsets earlier** in oxidized wires. **Adri C. T. van Duin** is a coauthor.

## Methods

- **ReaxFF MD** for **oxidation + tensile loading** protocols described in **PCCP**.
- **Structural analysis** of **oxide phases**, **shell thickness**, and **defect distributions** during deformation.

## Findings

- **H₂O** vs **H₂O₂** leads to **distinct oxide/oxyhydroxide microstructures** on **Fe NWs**, with measurable differences in **mechanical deterioration**.
- **Shell-induced defects** facilitate **plastic onset** at **lower stress/strain**.
- **Twinning** is still the main **plastic carrier**, but **oxidation shifts** when and where twins nucleate.

## Limitations

- **Nanowire diameter**, **strain rate**, and **temperature** in MD influence **quantitative moduli**; compare to experiment where available.
- **ReaxFF Fe/O/H** parameter scope should be verified when extending to **alloys** or **long-time corrosion** kinetics.

## Relevance to group

Demonstrates **group ReaxFF** practice on **reactive metal oxidation** coupled to **nanomechanics**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1039/C8CP02422G` (see `papers/Aral_PCCP_FeO_OH_2018.pdf`).

## Related topics

- [[reaxff-family]]
