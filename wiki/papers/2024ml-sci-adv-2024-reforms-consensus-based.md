---
id: paper:2024ml-sci-adv-2024-reforms-consensus-based
type: paper
title: "REFORMS: Consensus-based Recommendations for Machine-learning-based Science"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:methods-software
  - task:review
paper_keywords:
  - keyword:review-or-perspective
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1126/sciadv.adk3452"
year: 2024
authors:
  - "Kapoor, S."
  - "Cantrell, E. M."
  - "Peng, K."
  - "Pham, T. H."
  - "Bail, C. A."
  - "Gundersen, O. E."
  - "Hofman, J. M."
  - "Hullman, J."
  - "Lones, M. A."
  - "Malik, M. M."
  - "Nanayakkara, P."
  - "Poldrack, R. A."
  - "Raji, I. D."
  - "Roberts, M."
  - "Salganik, M. J."
  - "Serra-Garcia, M."
  - "Stewart, B. M."
  - "Vandewiele, G."
  - "Narayanan, A."
venue: "Sci. Adv."
pdf_sha256: "95c5a1d44453449cca7662f22800319ab0f7a59a91273d534ed93e4d634510f2"
pdf_path: "papers/Others/ML_review_sciadv.adk3452.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024ml-sci-adv-2024-reforms-consensus-based -->

## Summary

Kapoor and colleagues present **REFORMS** (Recommendations for machine-learning-based science): a **consensus checklist** of **32 items in eight modules**, each paired with reporting guidelines (supporting text S1 in the article), aimed at studies where **an ML model’s performance is used as evidence for a scientific claim** (“ML-based science”). The work distinguishes this scope from **ML methods research** (method development on benchmarks) and from **predictive analytics** where generalization to a defined scientific population is not the goal. The checklist is positioned as **field-agnostic** and informed by a literature review of reporting practice and failure modes across disciplines.

## Methods

The article is a **Science Advances** “Research Methods” review. The authors state that REFORMS was developed through **consensus among 19 researchers** spanning computer science, data science, mathematics, social sciences, and biomedical fields. They ground the checklist in **prior reporting standards** (including health-research checklists and ML replication initiatives) but emphasize differences: REFORMS targets **ML-based science** rather than only ML algorithm development, and includes items about **claims and distributions of interest** that benchmark-focused ML checklists may omit. The manuscript introduces **Table 1** (the 32-item checklist organized into eight modules) and states that **text S1** supplies detailed guidelines aligned with each item.

## Findings

The paper’s central deliverable is the **REFORMS checklist structure** (32 questions with paired guidance): it is presented as a practical tool for **study design**, **peer review**, and **journal policy** to improve **validity, reproducibility, and transparency** of ML-based scientific claims. The authors argue that clear, cross-field standards can reduce **recurrent error modes** in applied ML (for example, evaluation pitfalls and reporting gaps) that otherwise propagate across disciplines. **Table 1** lists modules and items; the PDF’s supporting information contains the elaborated guidance referenced in the main text.

For computational chemistry teams, the useful framing is **claim–evidence alignment**: checklist items push authors to state which **scientific conclusions** depend on ML performance, and what **data-generating process** those models were evaluated under.

## Limitations

REFORMS **does not replace domain-specific reporting standards** where they exist; some checklist items may be difficult to satisfy for particular study designs. The work explicitly scopes **ML-based science** and therefore does not directly govern pure methods papers or non-ML quantitative work. As with any checklist, **adherence quality** depends on authors, reviewers, and venues.

## Relevance to group

Primarily a **methods and reproducibility** reference for any ML-assisted atomistic or data-driven workflow; not chemistry-specific.

## Reader notes (navigation)

- [[theme-ml-atomistic-potentials]]

## Citations and evidence anchors

- Main checklist: Table 1 (PDF); item-level guidelines: text S1.

## Related topics

- [[reaxff-family]]
