# Plan: `concept:theme-reactive-md-corpus` (cross-cutting method hub)

## Inventory

- **Sources:** papers using **reactive MD** (ReaxFF or other reactive FFs), **QM/MM**, **bond-order** or **reaxff** method tags, shock/reactive workflows—not limited to `protocols/reaxff-parameterization-workflow` (training lineage is separate).
- **Index aids:** `method:reaxff`, `method:aimd`, `method:qm-mm` in [`taxonomy/canonical_tags.yml`](../../taxonomy/canonical_tags.yml); scan [`wiki/concepts/paper-index-by-domain.md`](../../wiki/concepts/paper-index-by-domain.md) across domains.
- **Disambiguation:** [[reaxff-family]], [[protocols/reaxff-parameterization-workflow]] = **parameterization / lineage**; this hub = **running** reactive simulations and **sampling** questions.

## Sub-themes

1. Reactive MD with **ReaxFF** (application studies).
2. Reactive MD with **other models** (alternative reactive FFs, tight-binding, hybrid) when present in KB.
3. **QM/MM** and multi-scale reactive setups.
4. **Rare events / shock / accelerated sampling** when tied to reactive pathways.
5. Software / LAMMPS workflow patterns (from paper methods sections).

## Section map

- Scope table: **in** method-level corpus coverage; **out** pure non-reactive FF fitting unless it enables a reactive run story.
- Literature review: **subsections** per bullet above—populate only from papers that actually use that stack.
- Analysis: compare **timestep / thermostat / system size** reporting density across domains (descriptive, from notes).
- Gaps: methods underrepresented in KB (e.g. path sampling) stated honestly.

## Draft `source_refs`

15–40 `paper_id` entries spanning multiple domains; prioritize diversity over duplicating one domain hub.

## Gap check (KB)

- Avoid duplicating domain synthesis—this hub is the **method** spine for MAS queries that are not “which ReaxFF paper trained parameter set X”.
