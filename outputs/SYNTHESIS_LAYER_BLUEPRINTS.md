# Synthesis-layer blueprints (themes, entry points, debates, protocols)

This document is the operational blueprint for reader-facing and MAS-facing synthesis pages.

## Shared writing requirements

- Use grounded, full-sentence prose with explicit scope boundaries.
- Keep substantive scientific claims traceable through `source_refs` and linked `paper:` pages.
- Use corpus honesty language for thin extracts, SI-only, proof, or duplicate PDFs.
- Prefer plain-language leads that explain why the page matters before technical detail.

## Theme hub blueprint (`wiki/concepts/theme-*.md`)

1. `!!! abstract` or lead
2. `## Scope (in / out)`
3. `## How this theme is organized in the corpus` (optional)
4. `## Literature review (this knowledge base)`
5. `## Analysis and cross-cutting patterns`
6. `## Debates, tensions, and limitations`
7. `## Gaps and open directions (corpus view)`
8. `## Methods and limitations`
9. `## Representative entry points` (optional)
10. `??? info "MAS / retrieval"`

## Cross-cutting entry-point blueprint (`wiki/concepts/*.md`, non-theme)

1. `!!! abstract` or lead
2. `## Scope and user intent`
3. `## Start-here pathways`
4. `## Decision levers and trade-offs`
5. `## Canonical starting papers`
6. `## Related protocols and debates`
7. `## Failure modes and interpretation pitfalls`
8. `??? info "MAS / retrieval"`

## Debate blueprint (`wiki/debates/*.md`)

1. `!!! abstract` or lead
2. `## Position statements`
3. `## Evidence by position`
4. `## Scope conditions and applicability`
5. `## Shared ground`
6. `## What evidence would resolve this`
7. `## Practical implications for modeling choices`
8. `## Key references`

## Protocol blueprint (`wiki/protocols/*.md`)

1. `## Summary`
2. `## Inputs and prerequisites`
3. `## Procedure`
4. `## Validation checks and acceptance criteria`
5. `## Failure modes and mitigations`
6. `## Variants and when to choose them`
7. `## Outputs and downstream links`
8. `## Evidence anchors`

## Execution policy for page-type waves

- Launch parallel sub-agents equal to the number of pages in the page type wave.
- After each wave, run validation and linkage checks before moving to the next type.
- Track completion with deterministic reports under `outputs/`.
