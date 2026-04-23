---
id: paper:2017akinwande-extreme-mech-review-mechanics
type: paper
title: "A review on mechanics and mechanical properties of 2D materials—Graphene and beyond"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - task:review
  - scale:multiscale
  - method:continuum-or-mesoscale
paper_keywords:
  - keyword:review-or-perspective
  - keyword:graphene-carbon
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1016/j.eml.2017.01.008"
year: 2017
authors:
  - "Deji Akinwande"
  - "Christopher J. Brennan"
  - "J. Scott Bunch"
  - "Philip Egberts"
  - "Jonathan R. Felts"
  - "Huajian Gao"
  - "Rui Huang"
  - "Joon-Seok Kim"
  - "Teng Li"
  - "Yao Li"
  - "Kenneth M. Liechti"
  - "Nanshu Lu"
  - "Harold S. Park"
  - "Evan J. Reed"
  - "Peng Wang"
  - "Boris I. Yakobson"
  - "Teng Zhang"
  - "Yong-Wei Zhang"
  - "Yao Zhou"
  - "Yong Zhu"
venue: "Extreme Mech. Lett."
pdf_sha256: "a55b7a768dfd28f954dfe85fe9d2a2b286fa343796fcdebd69843fbd5b22dfcf"
pdf_path: "papers/Others/Graphene_mechanical_properties_review.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017akinwande-extreme-mech-review-mechanics -->

## Summary

This article is a broad, multi-author review in *Extreme Mechanics Letters* that synthesizes theoretical and experimental knowledge on the mechanics of two-dimensional materials, with graphene as the best-developed reference case and "beyond graphene" materials included as the field expands. The abstract on the first page states the central thesis clearly: mechanics is not an auxiliary detail for 2D materials; it is essential for manufacturing, integration, and functional performance, and it is tightly coupled to thermal, electronic, and optical behavior.

The review presents mechanics as a unifying language across scales. At one end are nanoscale measurements (e.g., membrane deformation, contact-based probing, and interfacial friction/adhesion experiments); at the other are continuum and atomistic theories needed to interpret those measurements and translate them into design guidance. The opening contents list in the extracted pages shows the review's structure: elastic properties; inelastic behavior including defects/strength/toughness; electromechanical coupling; interfacial adhesion and friction; and application-facing implications.

A key summary message is that graphene launched the field, but its mechanical playbook cannot be transferred blindly to all 2D crystals. The review emphasizes that different crystal chemistry, anisotropy, and defect physics produce material-specific mechanical responses. It also highlights that real devices are usually substrate-supported or part of heterostructures, making interfaces (adhesion, sliding/friction, van der Waals coupling, and related mechanisms) central rather than secondary.

For this knowledge base, the paper serves as a framing reference: it links how properties are measured, how they are modeled, and why mechanics couples into broader functional outcomes. Because it is a review, this page summarizes the synthesis logic and section-level claims rather than presenting one new simulation protocol.

## Methods

This paper is a review/perspective article, so the method is evidence synthesis across prior literature rather than one newly executed simulation or experiment campaign.

- **Literature scope (as stated in abstract and table of contents):** Recent theoretical and experimental works on mechanics and mechanical properties of 2D materials, with graphene coverage plus extension to other 2D systems.
- **Organization strategy:** The article is structured by mechanics subdomains (elastic response; inelastic effects and defects; electromechanical coupling; interfacial adhesion/friction; applications), indicating a thematic synthesis rather than chronology-only narration.
- **Experimental evidence classes aggregated:** Mechanical characterization approaches such as membrane testing and probe-based methods; interface-focused studies for adhesion/friction behavior in device-like contexts.
- **Theory evidence classes aggregated:** Continuum mechanics treatments, condensed-matter-informed electromechanical analysis, and atomistic/theoretical predictions as reported in cited primary papers.

Blueprint-style protocol fields for this page:
- **1 - MD application block:** N/A - no single new MD engine/system/timestep/ensemble protocol is authored here.
- **2 - Force-field training block:** N/A - no new ReaxFF/classical potential fitting procedure is authored here.
- **3 - Static QM / DFT-only block:** N/A as a standalone primary computation; DFT/atomistic results are discussed from cited studies.
- **4 - Review methodology block (applicable):** The authors integrate cross-study evidence to compare property trends, mechanisms, and interface effects across material families and measurement/modeling approaches.

Corpus honesty note: `normalized/extracts/2017akinwande-extreme-mech-review-mechanics_p1-2.txt` contains abstract and early section map content; page-level quantitative values should be drawn from cited primary papers or deeper sections before reuse as numerical ground truth.

## Findings

The most important finding-level contribution is integrative: the review argues that mechanics must be treated as a first-class design axis for 2D materials, not merely a reliability afterthought. In the abstract language, mechanical behavior directly influences manufacturing yield, integration robustness, and device performance, and it must be analyzed jointly with electronic, thermal, and optical properties when designing applications.

A second cross-cutting result is that interfacial mechanics is indispensable for realistic device settings. The review explicitly highlights adhesion and friction as core topics, which reflects the practical reality that many 2D layers are transferred, stacked, contacted, or supported rather than kept as ideal freestanding membranes. This shifts attention from intrinsic sheet properties alone to interface-governed behavior in assembled systems.

A third contribution is the field map itself: by organizing literature into elastic response, inelastic/defect behavior, electromechanical coupling, and interface physics, the paper identifies where mechanics knowledge is already strong (especially graphene) and where broader materials classes require more systematic treatment. In this sense, the "finding" is partly a research-structure outcome: it clarifies which mechanistic questions recur across material families and which are material-specific.

For corpus-grounded interpretation, this page should be used as a synthesis gateway:
- It is appropriate for framing concepts, terminology, and research directions across 2D mechanics subfields.
- It is not the right source for quoting definitive single-number property values without tracing to primary citations.
- It does not provide executable MD/DFT run cards; protocol-level details remain in the cited primary studies.

Overall, the review's enduring value is methodological synthesis: it ties experimental observables, modeling abstractions, and interface realities into one coherent mechanics perspective for 2D materials development.

## Relevance to group

Background reference for **2D materials mechanics**; complements reactive MD work on carbon/oxide systems only indirectly.

## Citations and evidence anchors

- DOI: `10.1016/j.eml.2017.01.008`.

## Related topics

- [[graphene-nanocarbon]]
