---
id: paper:2017ostadhossein-venue-microsoft-word
type: paper
title: "Supporting information (part I): BGF structures and energies for MoS₂ ReaxFF training (Ostadhossein et al.)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - task:parameterization
paper_keywords:
  - keyword:qm-training-data
  - keyword:reaxff-parameterization
  - keyword:supporting-information
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: ""
year: 2017
authors:
  - "Alireza Ostadhossein"
  - "Adri C. T. van Duin"
venue: "Supporting information (ACS Publications)"
pdf_sha256: "afa0401a9f4c44c2416c6697038433186417a2b5757a9e59e6161f6783e02111"
pdf_path: "papers/Ostadhossein_MoS2_JPC_Letters_2017_SI_I.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017ostadhossein-venue-microsoft-word -->

!!! abstract "Non-primary PDF"

    **Supporting Information package I** for the **JPCL** ReaxFF letter on **MoS\(_2\)** (`Ostadhossein_MoS2_JPC_Letters_2017.pdf`). Listed in maintainer style as **SI-primary** ingest in `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md` (section A pattern). Scientific interpretation belongs with **`[[2017ostadhossein-venue-research]]`**.

## Summary

This PDF archives **BIOGRF** structure blocks and **single-point energies** (kcal/mol) for small **Mo–S–H** clusters used in the **MoS\(_2\)** ReaxFF optimization workflow (examples named in the extract include **MoS\(_6\)**, **MoS(SH)\(_2\)H**, **MoS\(_2\)SHH**, **MoS\(_4\)H\(_2\)**). The file supplies **coordinates**, **connectivity**, and **reference energies** paired to the training pipeline described in the parent letter and companion SI parts. It is **not** a standalone research article: claims about MoS\(_2\) edge energetics, catalysis, or MD validation appear in the main JPCL text.

For **parameterization audits**, the value of this ingest is **transparency**: each cluster entry ties a **specific** **connectivity** pattern to a **reference energy** used in the **objective function** during **genetic** or **least-squares** optimization. That pairing is what downstream reviewers need when asking whether edge, vacancy, or hydrogenated motifs were **balanced** against one another during the fit.

## Methods

**Force-field training / fitting.** This **Supporting Information (Part I)** PDF lists **BIOGRF** structure blocks and **reference energies** (kcal/mol) for small **Mo–S–H** clusters used in the **MoS₂** **ReaxFF** optimization reported in **`[[2017ostadhossein-venue-research]]`**. Entries pair **connectivity**, **coordinates**, and **single-point energies** that enter the published **least-squares / genetic** objective together with **Table S1/S2** and **`trainset.in` weights** in **[[2017ostadhossein-venue-microsoft-word-2]]** / **[[2017ostadhossein-venue-microsoft-word-3]]**.

**MD application (atomistic dynamics).** **N/A —** this file is **training data** only; production **MD** validation trajectories are described in the **parent JPCL** letter.

**Static QM / DFT.** **QM** levels, basis/cutoff conventions, and **DFT** benchmarks for the same training set are documented on **`[[2017ostadhossein-venue-microsoft-word-2]]`** and in the **main text** of **`[[2017ostadhossein-venue-research]]`**.

**Review / non-simulation framing.** **Non-primary SI** artifact; scientific interpretation and **DOI** (**10.1021/acs.jpclett.6b02902**) belong on **`[[2017ostadhossein-venue-research]]`**.

## Findings

**Outcomes.** The SI supplies the **numerical cluster training set** required to **audit** the published **ReaxFF** fit; it does **not** add standalone **mechanistic** conclusions beyond supporting the parent publication.

**Comparisons.** Each motif ties a **BIOGRF** structure to a **reference energy** used alongside **DFT** benchmarks summarized on the **VOR** page—use those tables when recomputing **training residuals**.

**Sensitivity / design levers.** Relative **weights** and **which bond/angle motifs** appear in **Part I** determine how much each **Mo–S–H** fragment constrains the fit; see **Part III** for explicit **per-observable weights**.

**Limitations / outlook.** When porting snippets to **LAMMPS** data decks, verify **periodic images** and **charge initialization** against the **parent letter** examples—**cluster** training geometries are not always literal **production supercells**.

**Corpus honesty.** **SI-only** ingest; cite the **JPCL** article for scholarly claims. Filename reflects **Microsoft Word** export history, not content type.

## Limitations

Filename reflects **Microsoft Word** export; cite the **parent letter DOI** for scholarly references. Frontmatter **`doi`** is empty here—use **`[[2017ostadhossein-venue-research]]`** for DOI **10.1021/acs.jpclett.6b02902** (verify on the VOR PDF).

## Relevance to group

Training-data artifact for **Penn State MoS\(_2\)** ReaxFF development.

## Citations and evidence anchors

- Parent letter: **`[[2017ostadhossein-venue-research]]`** (JPCL; DOI on that page).
**SI use.** Copy BIOGRF blocks and energies from this PDF into the same ReaxFF optimization toolchain described in `[[2017ostadhossein-venue-research]]`; cite the parent JPCL letter for scientific interpretation.

## Reproducibility and corpus locators

This note documents **where** to find primary evidence in-repo; it does **not** add new scientific claims beyond the cited publication.

**Normalized layer.** When present, `normalized/papers/{slug}.json` mirrors manifest hashes, bibliography fields, and extraction pointers; if `pdf_path` or PDF bytes change, follow `AGENTS.md` and `docs/PHASE3_RUNBOOK.md` to re-profile rather than editing PDFs in place.

**Authority chain.** For numerical settings (cutoffs, timesteps, ensembles, kinetics), use the peer-reviewed PDF (and publisher Supporting Information) as the authoritative source; this wiki summarizes for navigation and retrieval.

## Related topics

- [[reaxff-family]]
