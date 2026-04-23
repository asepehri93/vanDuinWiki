---
id: paper:2020momeni-npj-computat-multiscale-computational-2
type: paper
title: "Multiscale computational understanding and growth of 2D materials: a review"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - task:review
  - scale:multiscale
paper_keywords:
  - keyword:review-or-perspective
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1038/s41524-020-0280-2"
year: 2020
authors:
  - "Kasra Momeni"
  - "Yanzhou Ji"
  - "Yuanxi Wang"
  - "Shiddartha Paul"
  - "Sara Neshani"
  - "Dundar E. Yilmaz"
  - "Yun Kyung Shin"
  - "Difan Zhang"
  - "Jin-Wu Jiang"
  - "Harold S. Park"
  - "Susan Sinnott"
  - "Adri van Duin"
  - "Vincent Crespi"
  - "Long-Qing Chen"
venue: "npj Computational Materials (uncorrected proof PDF in corpus)"
pdf_sha256: "227fd62a0c89c880268e2f915effc94d5ff7c8e5f1de4392a30f876b0bfb3235"
pdf_path: "papers/Momeni_2D_review_NPJ_CompMat_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020momeni-npj-computat-multiscale-computational-2 -->

??? info "PDF variant"
    **Uncorrected proof** PDF. Canonical article text and stable pagination: [[2020momeni-npj-computat-multiscale-computational]] (`papers/Momeni_2D_review_NPJ_CompMat_2020.pdf`).

## Summary

The uncorrected proof PDF `papers/Momeni_2D_review_NPJ_CompMat_proof.pdf` corresponds to the **npj Computational Materials** review DOI `10.1038/s41524-020-0280-2`, “Multiscale computational understanding and growth of 2D materials.” The extract opens by noting graphene’s 2004 isolation and the subsequent expansion of layered semiconductors and heterostructures, then states the review’s aim: to overview **theoretical, computational, and machine-learning** tools across **length and time scales** to assist design and synthesis of 2D materials **beyond graphene**. It announces three methodological tiers: **(i)** nanoscale atomistic simulations including **DFT** and MD with **empirical and reactive** potentials; **(ii)** mesoscale methods such as **phase-field** modeling; and **(iii)** macroscale **continuum** approaches coupling thermal and chemical transport. It further promises discussion of machine learning combined with computation and experiments to link structures and properties and to guide discovery, plus an outlook on computational approaches to synthesis and growth.

## Methods

As a review, the article surveys heterogeneous literature rather than a single protocol. The **Introduction** in the extract contrasts **top-down** approaches (mechanical and liquid-phase exfoliation) with **bottom-up** CVD/ALD routes, notes sensitivity of morphology to thermodynamic and kinetic conditions (heat/mass transfer, reaction kinetics, adsorption, nucleation), and lists multiscale challenges: quantum and atomistic **activation energies** for migration, **FEM** mass transport, **substrate defects**, **wrinkling**, **van der Waals** interactions at mesoscales, and growth kinetics specific to atomically thin films, including flexural phonon modeling issues for 2D materials. The following section heading **ATOMISTIC COMPUTATIONAL METHODS** begins with **First-principles calculations**, describing DFT’s role in comparing **chemical potentials** of polymorphs and analyzing **kinetic pathways** via transient structures; it notes standard **PBE-GGA** usage and limitations such as underestimated reaction barriers from delocalization error, and introduces “above-hull” energy as a practical stability screen. Detailed numerical settings for any one cited study remain in primary references; follow [[2020momeni-npj-computat-multiscale-computational]] for the finalized sectioning.

## Findings

The proof excerpt argues that developing design tools for 2D synthesis requires bridging **very wide** length and time scales—for example, reactive force-field calculations of surface migration barriers coupled to **finite-element** mass transport—and that useful multiscale models must be **efficient**, **accurate**, and able to capture multi-physical links among growth conditions, morphology, and properties, with an eventual goal of guiding reactor design for **uniform large-area** films. Because the excerpt shown is only the opening and the start of atomistic methods, later sections on mesoscale approaches and machine-learning integrations are **partially** represented here; full positioning of ReaxFF alongside classical potentials and continuum solvers appears in the published PDF summarized on [[2020momeni-npj-computat-multiscale-computational]]. Final figure and equation numbering may differ between uncorrected proof and issue PDF.

## Limitations

Uncorrected proofs can differ from the final Nature Partner Journal PDF in typography and minor editorial fixes. Use the VOR ingest for citation locators.

## Relevance to group

Van Duin co-authorship ties the review’s atomistic sections—including reactive potentials—to Penn State’s broader 2D materials modeling ecosystem.

## Reader notes (navigation)

- [[2020momeni-npj-computat-multiscale-computational]]
- [[theme-2d-epitaxy-growth]]
- [[reaxff-family]]

## Citations and evidence anchors

DOI: [10.1038/s41524-020-0280-2](https://doi.org/10.1038/s41524-020-0280-2)
