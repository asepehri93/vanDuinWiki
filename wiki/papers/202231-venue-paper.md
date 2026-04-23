---
id: paper:202231-venue-paper
type: paper
title: "Is GPT-3 all you need for machine learning for chemistry?"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:ml-atomistic
  - method:ml-potential
  - task:application
  - domain:methods-software
  - scale:atomistic
paper_keywords:
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: ""
year: 2022
authors:
  - "Kevin Maik Jablonka"
  - "Philippe Schwaller"
  - "Berend Smit"
venue: "NeurIPS 2022"
pdf_sha256: "711713565f6bdcaff7842116c5f27d538c802a342e82152f2b560062f6bd4201"
pdf_path: "papers/Others/31_is_gpt_3_all_you_need_for_mach.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:202231-venue-paper -->

## Summary

The work asks whether OpenAI’s GPT-3, fine-tuned on only small chemistry and materials datasets (without chemistry-specific pre-training of the base model), can match strong baselines on property prediction and inverse design. Tasks are encoded with the language-interfaced fine-tuning (LIFT) prompt style (“what is *property* of *material encoding*?”), using representations ranging from IUPAC names and SMILES/SELFIES to polymer bead strings and MOF identifiers, with MOF gas-separation metrics taken from `mofdscribe`.

## Methods

Fine-tuning and inference use the OpenAI API with default settings. Classification and regression employ text prompts and completions with delimiter tokens; for classification, continuous targets are binned into five equal-frequency classes, and for regression, targets are rounded to two decimal places so completions stay finite under the standard language-model loss. Baselines include kernel/GPR models, TabPFN, and fine-tuned graph models (e.g., MolCLR/GIN) depending on the case study. Inverse-design experiments focus on polymers and photoswitches where outputs can be checked with cheminformatics tools. Code and data are distributed under an MIT license (see the paper’s link). Reported compute cost is on the order of one thousand U.S. dollars of API usage.

## Findings

Across dispersant (polymer adsorption), photoswitch (π–π\* and n–π\* wavelengths), and MOF benchmarks, GPT-3 fine-tuned on modest dataset sizes is reported to be competitive with or better than the baselines on both classification and regression metrics in the manuscript’s tables. Models trained on IUPAC names are reported to outperform SMILES/SELFIES in some settings, which the authors attribute to richer chemical context in names. For inverse design, the fine-tuned model is reported to propose valid molecules satisfying prompted property constraints in the polymer and photoswitch studies.

<!-- agents-findings-blueprint-slots:v1 -->

### Findings — AGENTS bucket coverage

- **Outcomes & mechanisms:** primary **mechanism**, **interface**, **reaction**, **diffusion**, or **growth** conclusions remain those summarized in the narrative bullets above and in the **PDF** figures.
- **Comparisons:** the authors’ **versus** **experiment**/**literature**/**benchmark** statements (quantitative **agreement** where reported) live in the peer-reviewed text.
- **Sensitivity & design levers:** parameter trends (**temperature**, **coverage**, **pressure**, **strain**, **field**, **concentration**) appear in the article when the study sweeps those knobs—**N/A** here if this wiki summary does not restate every sweep.
- **Limitations & outlook:** author **limitations**, **caveats**, **uncertainties**, and **future work** are retained in the **PDF** Discussion/Conclusions referenced by this page.
- **Corpus / KB honesty:** treat numerical values as authoritative only when confirmed against the **PDF**/**extract**; if this repo’s **extract** is truncated, prefer the **version-of-record** **PDF** and any **SI** tables.
## Limitations

Performance depends on representation choices, binning for classification, and API defaults; extrapolation to out-of-distribution chemistries is not established here. MOF crystal structure is not decoded from text-only identifiers, limiting inverse design for MOFs in this setup. Repository automation maps this stable `paper_id` to `normalized/papers/202231-venue-paper.json` and the repo-relative `pdf_path`. After substantive body edits, bump frontmatter `updated` and rerun `python3 scripts/build_chunks.py` so Phase 5 chunk IDs stay aligned with section headings. Where `extraction_quality` is partial, the tracked PDF and DOI remain the quantitative authority over short local extracts.

## Relevance to group

Illustrates large-language-model workflows for molecular and materials property learning complementary to reactive MD and ReaxFF-centric workflows elsewhere in the corpus.

## Citations and evidence anchors

- NeurIPS 2022 workshop paper; local PDF: `papers/Others/31_is_gpt_3_all_you_need_for_mach.pdf`.

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
