---
id: paper:2015shin-venue-research
type: paper
title: "Development of a ReaxFF reactive force field for Fe/Cr/O/S and application to oxidation of butane over a pyrite-covered Cr2O3 catalyst"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - domain:fuel-combustion
  - method:reaxff
  - material:oxide
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acscatal.5b01766"
year: 2015
authors:
  - "Yun Kyung Shin"
  - "Hyunwook Kwak"
  - "Alex V. Vasenkov"
  - "Debasis Sengupta"
  - "Adri C. T. van Duin"
venue: "ACS Catal."
pdf_sha256: "18e2ffbb2b57550408f9326be26c56501d9f1dc14f81ce8fcb6ffd7d8d2df7b2"
pdf_path: "papers/Shin_ACS_Catalysis_2015.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015shin-venue-research -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

A **Fe/Cr/O/S ReaxFF** is parameterized from **QM data** and applied to **high-temperature butane oxidation** on **Cr oxide** surfaces, including scenarios with **iron pyrite (FeS2)** as a **coal-derived impurity**. Reactive trajectories emphasize **surface oxygen species** that drive **dehydrogenation** to radicals and **C–O coupling** pathways, contrasting **partial oxygenates (e.g., CH2O on clean chromia)** with **accelerated deep oxidation to CO/CO2** when pyrite is present. The article also discusses **surface reconstruction / sulfur-containing intermediates (e.g., SOH release)** and **reoxidation** cycles involving water desorption and O2 adsorption at vacancies.

## Methods

- **ReaxFF development** with QM training on **Fe/Cr/O/S** chemistry.
- **Reactive MD** at **1600 K** on model catalyst slabs with and without **FeS2** patches.

The article further notes that the Fe/Cr/O/S ReaxFF parameterization is fit to QM data. Reactive trajectories for butane oxidation on Cr oxide at 1600 K emphasize surface oxygen species in dehydrogenation and C–O coupling; radical intermediates combine with lattice oxygen to form partial oxygenates and light alkenes, with formaldehyde prominent on clean chromia under the quoted conditions.

## Findings

- **Cr-oxide** catalyzes **dehydrogenation** and oxygen insertion, with **CH2O** emphasized as a major product on **clean** surfaces under the simulated conditions reported in the abstract.
- **FeS2** on chromia **accelerates complete oxidation** to **CO2/CO** and is associated with **surface restructuring** and altered **oxygen speciation**.
- **Reoxidation** pathways differ between **clean** and **pyrite-modified** surfaces; **SOH**-related desorption appears on the modified oxide.


From the abstract: dehydrogenation of butane, which is found to be catalyzed by oxygen species on the oxide surface, initiates the reaction and generates butane radicals and surface OH groups. On the other hand, on the modi ﬁed Cr-oxide, it is found that a considerable amount of SOH molecules are released from the surface. The presence of iron pyrite (FeS 2), a common inorganic component in coal-derived fuels and a major slagging component, on Cr-oxide accelerates the complete oxidation of butane forming CO 2 and CO. Surface reconstruction by iron pyrite is probably responsible for the change of the catalytic behavior. Reoxidation of the reduced oxide surface can occur through removal of surface H 2O and adsorption of gaseous molecular oxygen at the vacancy sites on the clean Cr-oxide. These results can provide the detailed mechanisms for the catalytic oxidation of alkane and product distributions in Cr-oxide catalyst and give, for the ﬁrst time, atomistic-scale insight in the complex surface chemistry of these catalysts under realistic operating conditions.

## Limitations

- **Single temperature window** (1600 K in the abstract framing) is far from industrial ODH conditions; extrapolation requires care.
- **ReaxFF** cannot subsume all **electronic redox** subtleties of sulfide–oxide interfaces without extensive validation.

## Relevance to group

Illustrates **multi-element ReaxFF parameterization** for **sulfur-containing fossil-catalyst** chemistries—an important axis of the group’s **reactive catalysis** simulation work with Shin and industrial collaborators.

## Citations and evidence anchors

- Abstract and introduction in `papers/Shin_ACS_Catalysis_2015.pdf`; **DOI:** `10.1021/acscatal.5b01766`.

## Related topics

- [[reaxff-family]]