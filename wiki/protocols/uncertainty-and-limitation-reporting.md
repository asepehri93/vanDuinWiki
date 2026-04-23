---
id: methodprotocol:uncertainty-and-limitation-reporting
type: methodprotocol
title: "Uncertainty and Limitation Reporting Protocol"
updated: "2026-04-23"
confidence: high
canonical_tags:
  - domain:methods-software
  - task:method-development
  - task:validation
  - task:review
candidate_tags: []
source_refs: []
aliases:
  - uncertainty reporting
  - limitations section protocol
related_ids:
  - concept:theme-reactive-md-corpus
applies_to:
  - paper pages
  - synthesis pages
evaluates:
  - uncertainty transparency
  - evidence traceability
  - reproducibility readiness
---

<!-- id:methodprotocol:uncertainty-and-limitation-reporting -->

This protocol standardizes how to write uncertainty and limitation sections so readers and downstream agents can distinguish evidence-backed conclusions, open assumptions, and unresolved gaps.

## Summary

Use this protocol whenever writing or revising uncertainty and limitation content in:
- `wiki/papers/*.md` pages (publication-level interpretation boundaries).
- Synthesis pages (`wiki/concepts/`, `wiki/materials/`, `wiki/forcefields/`, `wiki/debates/`) where cross-paper claims can overgeneralize.

Core objective:
- Make uncertainty explicit, scoped, and actionable.
- Tie each non-trivial caveat to a traceable source context.
- Prevent hidden assumptions from being mistaken as conclusions.

## Inputs and prerequisites

Required inputs:
- Target page draft with frontmatter complete.
- Relevant `source_refs` and linked `paper:` pages.
- Any available protocol context from `## Methods` and `## Findings` on cited paper pages.

Preconditions before drafting uncertainty text:
- Claims in the target page are already grouped by topic.
- Each group has at least one evidence anchor candidate (paper id plus locator context).
- You know whether the page is:
  - Paper-focused (single-study interpretation constraints), or
  - Synthesis-focused (cross-paper consistency and transferability constraints).

Minimum evidence anchor unit:
- `paper_id` plus at least one of:
  - section label,
  - page range,
  - short locator note tied to method/result context.

## Procedure

1. Build a claim inventory first.
- List each substantive claim in the page in one sentence.
- Mark each claim as:
  - Directly measured/reported,
  - Derived inference,
  - Hypothesis-level interpretation.

2. Classify uncertainty type for each claim.
- Method uncertainty: model choice, functional/formulation, force-field transferability, sampling limitations.
- Data uncertainty: sparse points, missing controls, low extraction quality, SI-only visibility.
- Scope uncertainty: domain shift across materials, temperatures, fields, interfaces, time scales.
- Reporting uncertainty: missing parameters, unclear validation, unresolved disagreement in corpus.

3. Attach evidence anchors.
- For every uncertainty statement, attach at least one anchor path:
  - For paper pages: anchor to the same publication sections backing Methods/Findings.
  - For synthesis pages: anchor to specific supporting papers in `source_refs`.
- If uncertainty is due to absence of evidence, state that explicitly ("not reported in indexed source") and identify what source tier was checked (PDF, SI, extract, metadata).

4. Write uncertainty statements in reproducible format.
- Use the pattern:
  - **Observation:** what is known.
  - **Uncertainty:** what is not constrained.
  - **Impact:** what interpretation may change.
  - **Check/next evidence:** what would reduce uncertainty.
- Keep one uncertainty per paragraph or bullet; avoid merged caveats with mixed causes.

5. Add limitations with boundary conditions.
- For each major conclusion, add at least one "valid under..." boundary:
  - method regime,
  - composition/system class,
  - thermodynamic window,
  - sampling/time horizon.
- State non-applicability where needed ("do not transfer to X without validation").

6. Encode confidence and residual risk.
- Align wording with frontmatter `confidence`:
  - `high`: anchored claims with narrow residual uncertainty.
  - `med`: evidence present but transferability or parameter dependence remains.
  - `low`: thin or indirect evidence; interpretation primarily provisional.
- Include a short residual-risk line for decision-critical claims.

7. Add explicit corpus-honesty note when evidence is incomplete.
- Required when page relies on SI-only, galley/proof, or extract-thin sources.
- Distinguish:
  - "Not in this corpus/source" from
  - "Unknown to science."

## Validation checks and acceptance criteria

Quality gates (all required):
- Coverage gate: every major claim has at least one associated uncertainty or explicit "no material uncertainty identified under current scope" statement.
- Anchor gate: every uncertainty/limitation statement has a traceable evidence anchor or explicit absence-of-evidence declaration.
- Scope gate: each limitation specifies where it applies (system, regime, method, or data boundary).
- Impact gate: each uncertainty states why it matters for interpretation, comparison, or protocol choice.
- Actionability gate: each high-impact uncertainty includes a concrete follow-up check.

Reproducibility checklist:
- Another curator can reconstruct why each limitation exists from cited anchors.
- A retrieval agent can parse uncertainty type without guessing intent.
- No limitation sentence depends on implicit background knowledge.

Reject and revise if any of the following occur:
- Generic caveats with no evidence path ("results may vary" without conditions).
- Mixed certainty language ("proves" and "possibly" in the same claim scope).
- Overreach beyond cited pages or source quality.
- Limitations that repeat Methods details without interpretation consequences.

## Failure modes and mitigations

Failure mode: boilerplate uncertainty text reused across unrelated pages.
- Mitigation: require claim-specific anchors and impact statements.

Failure mode: uncertainty phrased as disclaimer only, not analysis.
- Mitigation: enforce Observation -> Uncertainty -> Impact -> Check pattern.

Failure mode: synthesis page hides cross-paper disagreement.
- Mitigation: add explicit disagreement bullets and link to a debate page where relevant.

Failure mode: paper page claims transferability not shown in source.
- Mitigation: add "transferability untested beyond reported domain" unless direct evidence exists.

Failure mode: confidence level inflated by polished prose.
- Mitigation: calibrate `confidence` from anchor density, source quality, and unresolved contradictions.

## Variants and when to choose them

Variant A: Paper-page uncertainty block (single publication).
- Use when curating `type: paper`.
- Prioritize protocol transparency, parameter omissions, and in-study validation limits.

Variant B: Synthesis-page uncertainty block (cross-paper).
- Use for concept/material/forcefield/debate pages.
- Prioritize comparability constraints, heterogeneity of methods, and corpus coverage gaps.

Variant C: Entry-point page uncertainty block (decision support).
- Use for query-first pages that route readers.
- Prioritize decision risk, common misreads, and minimum verification before method selection.

## Outputs and downstream links

Expected outputs after applying this protocol:
- Updated uncertainty/limitation prose in the target page, evidence-anchored and scope-bounded.
- Frontmatter `confidence` aligned with uncertainty burden.
- Improved retrieval reliability for MAS workflows that rank by confidence and evidence density.

Recommended downstream maintenance:
- If uncertainty themes recur across pages, open or update a relevant debate page under `wiki/debates/`.
- If recurring method caveats are operational, link to or extend a companion protocol page.
- Refresh section-level chunks after substantive edits using:
  - `python3 scripts/build_chunks.py`

## Evidence anchors

Anchor hierarchy for this protocol:
1. Version-of-record paper PDF and SI (if locally available).
2. Curated paper page Methods/Findings sections tied to that publication.
3. `source_refs` on synthesis pages with explicit `paper_id` locators.
4. Extract-only fallback with explicit quality caveat.

Evidence anchor formatting guidance:
- Prefer compact citations in prose that include `paper_id` and locator context.
- Keep locator language stable enough that another curator can find it.
- Never use an uncertainty claim without an anchor path or explicit "not reported" statement.

Minimum anchor density targets:
- Paper pages: at least one anchor for each major limitation category.
- Synthesis pages: at least one anchor per cross-paper uncertainty cluster.

??? info "MAS / retrieval"
    Stable id: `methodprotocol:uncertainty-and-limitation-reporting`.
    Query synonyms: "uncertainty section", "limitations section", "evidence-qualified claims", "confidence calibration".
    Refresh when corpus source quality changes (new PDFs/SI, corrected extractions, or updated paper-level Methods/Findings curation).
