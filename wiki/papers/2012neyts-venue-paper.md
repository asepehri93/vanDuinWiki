---
id: paper:2012neyts-venue-paper
type: paper
title: "Combining molecular dynamics with Monte Carlo simulations: implementations and applications"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - method:classical-md
  - method:monte-carlo
  - task:review
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:review-or-perspective
  - keyword:monte-carlo-sampling
  - keyword:method-development
  - keyword:enhanced-sampling
source_refs: []
doi: "10.1007/s00214-012-1320-x"
year: 2012
authors:
  - "Neyts, Erik C."
  - "Bogaerts, Annemie"
venue: "Theoretical Chemistry Accounts"
pdf_sha256: "685a89d2944d954360800afe53c2d7661991feb871e1958020580da5c60a1b90"
pdf_path: "papers/ReaxFF_others/Neyts_MC_ReaxFF_TCA_2013.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2012neyts-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the review identified by `doi` and `pdf_path`. The ingest filename contains “ReaxFF” but the article text is a **methods** survey (**MD**/**MC** coupling), not a ReaxFF parametrization paper.

## Summary

Overview of **atomistic** **molecular dynamics** combined with **Monte Carlo** techniques for **condensed matter**, with a section on **accelerated dynamics**, emphasis on **force-bias Monte Carlo** and recent developments, and **example** applications where **combined MD/MC** improves efficiency versus **pure MD** or **pure MC**. The abstract positions the work as a **survey** of implementations and **use cases**. For **reactive** workflows common in **ReaxFF** studies, the review’s taxonomy matters because **bond** **forming/breaking** events can be **rare** on **ps/ns** **MD** windows; **hybrid** **sampling** is presented as one way to reach **long-time** kinetics without abandoning **atomistic** detail.

## Methods


This is a **methods** **review**, not a **ReaxFF** **parameterization** study. It surveys how **atomistic** **molecular dynamics** can be **combined** with **Monte Carlo** (**Metropolis MC**, **kinetic** / **dynamic** **Monte Carlo**, catalogs of **rates**, etc.), summarizes **accelerated** **molecular dynamics** techniques as a parallel strategy for long timescales, and gives **special** attention to **force-bias Monte Carlo** and its **coupling** to **MD**, including recent claims of a **definable timescale** in that family.

The article also catalogs practical **implementation** choices—how **Monte Carlo** **moves** interleave with **MD** **propagation**, how **rates** enter **kinetic** **Monte Carlo**, and where **parallel** **replica** **accelerated** **MD** competes with **MC**-based **resampling**. The survey spans **Metropolis MC**, **kinetic / dynamic MC**, and catalogs of **rates** used in multiscale kinetics, alongside **accelerated molecular dynamics** variants discussed as an alternative route when **rare events** limit plain **MD**.

## Findings

The review positions **hybrid MD/MC** and **accelerated MD** as routes to **rare events** and **long-time** behavior when **plain MD** is too short, and it highlights **force-bias Monte Carlo** as one **coupled** strategy; **concrete** **benchmark** **systems** and **timings** are in the **full text** (`pdf_path`).

**Practical guidance:** readers comparing **methods** should check whether a **hybrid** scheme preserves **detailed balance** (or a controlled approximation), what **order** of **magnitude** **speedup** is demonstrated for specific **barriers**, and whether **reactive** **potentials** were used in the cited **applications** or only **nonreactive** **bonded** models.

**Corpus / KB honesty:** This page summarizes the review using **`pdf_path`** and `normalized/extracts/2012neyts-venue-paper_p1-2.txt` when present; the ingest filename suggests **2013** print metadata—confirm **volume/issue** against the publisher record for citations.

## Limitations

**Partial** extract in corpus; **PDF** year in filename (**2013**) vs bibliographic **2012** receipt—verify **volume/issue** against publisher. **Reactive** **ReaxFF** applications appear only indirectly through citations in the broader literature—this review should not be mistaken for a **parameterization** or **validation** study of **combustion** **ReaxFF**.

## Relevance to group

General **simulation methodology** context for workflows that may later couple to **ReaxFF** or other **reactive** engines; **not** a **van Duin** group paper.

## Citations and evidence anchors

- DOI **10.1007/s00214-012-1320-x** — *Theor. Chem. Acc.* **132**, 1320 (2013).
- Extract: `normalized/extracts/2012neyts-venue-paper_p1-2.txt`.

## Related topics

- [[reaxff-family]]
