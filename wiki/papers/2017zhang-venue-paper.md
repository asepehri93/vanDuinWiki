---
id: paper:2017zhang-venue-paper
type: paper
title: "Weakening effect of nickel catalyst particles on the mechanical strength of the carbon nanotube/carbon fiber junction"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:application
  - material:graphene-carbon-nano
  - domain:mechanics-tribology
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:metallic-systems
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2017.01.042"
year: 2017
authors:
  - "Chi Zhang"
  - "Adri C. T. van Duin"
  - "Jin Won Seo"
  - "David Seveno"
venue: "Carbon"
pdf_sha256: "297adc848d445a890518cf03907e1554dffff4f858f9fb178a414897b18e428d"
pdf_path: "papers/Zhang_Seveno_Carbon_2017_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2017zhang-venue-paper -->

!!! note "Corpus note"
    Ingested file is an **uncorrected proof**; verify final pagination against the Carbon version of record. Maintainer catalog (GitHub): [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Summary

**Carbon fiber** manufacturers often **graft** **single-wall carbon nanotubes (SWCNTs)** onto **graphitic** **surfaces** to improve **interfacial shear**, yet **residual catalyst nanoparticles** from **CVD** growth can remain at **CNT–substrate** contacts. The **Carbon** study therefore speaks to **quality-control** questions in **CNT** **forests** sold for **composite** **integration**: **catalyst** **removal** or **oxidation** **treatments** may be as important as **grafting** **chemistry** for **junction** **strength**. **Zhang**, **van Duin**, **Seo**, and **Seveno** apply **ReaxFF molecular dynamics** to **tensile** loading of **SWCNT–graphene** junction models with **no particle**, **pure Ni**, **oxidized Ni**, and **unoxidized Ni** **nanoparticles** embedded at the **contact**. The study correlates **peak stress** with **bond-level** **C–O–Ni** chemistry that appears during **deformation**, connecting **catalyst oxidation** state to **mechanical** **weakening** or **preservation** of the **junction**.

## Methods

**Molecular dynamics (reactive).** **ReaxFF molecular dynamics** applies **quasi-static** **tensile strain** to **SWCNT**–**graphene** junction models containing **no Ni**, **metallic Ni**, or **oxidized Ni** nanoparticles, monitoring **C–C**, **C–O**, and **Ni–O** coordination to classify **failure** modes at the **temperature** (**K**) setpoints given in the **Carbon** **Methods** (mirroring **`[[2017zhang-carbon-115-2-weakening-effect]]`**). **Periodic** **supercells**, **atom** counts, **timestep** (fs), **thermostat**/**barostat** settings, **NVT**/**NPT** staging, and **equilibration**/**production** **duration** (ps/ns) match the **Carbon** **version-of-record** summarized on **`[[2017zhang-carbon-115-2-weakening-effect]]`**; confirm any pagination drift using **`papers/Zhang_Seveno_Carbon_2017_proof.pdf`**. **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** highlighted here.

**Force-field fitting.** **N/A —** uses the published **Ni/C/O ReaxFF** line cited in the article for **metal–carbon** **oxidation** states.

**Static QM / DFT.** **N/A —** **MD** drives the mechanical study; **DFT** is not the production engine.

**Review scope.** **N/A —** **uncorrected proof** duplicate; canonical reader entry: **`[[2017zhang-carbon-115-2-weakening-effect]]`**.

## Findings

**Outcomes and mechanisms.** **Nanoparticle-free** junctions retain the **highest peak stress** in the abstract’s set, while **pure Ni** can **weaken** the junction by up to **~50%**; **oxidized Ni** leaves comparatively higher strength because **Ni–O**/**Ni–C** **bond** networks redistribute **stress** instead of localizing it into rapid **C–C** scission channels.

**Comparisons.** **Versus** **metallic** Ni, **oxidized** clusters change **failure** topology through **metal–oxide–carbon** bridges rather than simple **CNT pullout**.

**Sensitivity / design levers.** **Catalyst oxidation** state and **strain** path dominate the **interface** **reaction** sequence during **tension**, echoing **CVD** processing concerns for **CNT-on-fiber** hybrids.

**Limitations / outlook.** **Proof** **PDF** (`extraction_quality: partial`) may omit final copy edits—confirm percentages and supplemental cases against the **issue** **PDF**.

**Corpus honesty.** Use **`[[2017zhang-carbon-115-2-weakening-effect]]`** for stable citations; keep this slug only when the **proof** bytes must be referenced explicitly.
## Limitations

Proof PDF and partial extraction quality: confirm percentages, simulation sizes, and strain rates from the **Carbon** version of record (`papers/Zhang_Seveno_Carbon_2017_proof.pdf` is non-VOR).

## Relevance to group

Adri C. T. van Duin as coauthor; applies ReaxFF to metal–carbon composite interfaces and mechanical failure.

## Citations and evidence anchors

- DOI: `10.1016/j.carbon.2017.01.042`.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
