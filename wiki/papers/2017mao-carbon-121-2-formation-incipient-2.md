---
id: paper:2017mao-carbon-121-2-formation-incipient-2
type: paper
title: "Formation of incipient soot particles from polycyclic aromatic hydrocarbons: A ReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2017.06.009"
year: 2017
authors:
  - "Qian Mao"
  - "Adri C. T. van Duin"
  - "K.H. Luo"
venue: "Carbon"
pdf_sha256: "a2b84fd4d5c2a30f28325de6e2b897b06245a6ef0c68d77937989012dea150ab"
pdf_path: "papers/QianMao_Carbon_Soot_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017mao-carbon-121-2-formation-incipient-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Corpus note:** this slug registers a second **PDF** path (`papers/QianMao_Carbon_Soot_2017.pdf`) for the same **Carbon (2017)** **ReaxFF** study as **`[[2017mao-carbon-121-2-formation-incipient]]`** (`papers/Mao_Qian_Carbon_soot_2017.pdf`). **ReaxFF MD** follows **incipient soot** formation from **PAH** monomers (**naphthalene** through **circumcoronene**) across **400–2500 K**. At **low temperature**, **stacked** clusters form by **physical** association; **intermediate** temperatures narrow which **large PAHs** remain productive; at **2500 K**, **chemical** growth yields **graphitizing** particles with rising **C/H** and morphologies spanning **fullerene-like** cages to **bridge-linked** stacks for the heaviest aromatics. The work targets **soot inception** debates in combustion modeling (**Tsinghua** / **UCL** / **van Duin** collaboration). **Soot** **nucleation** remains a **multiscale** bottleneck because **gas-phase** **PAH** chemistry couples to **particle** **coagulation** and **carbonization** on **ns–μs** timescales difficult to unify in single models (introduction themes; sibling page).

## Methods

**A — Force-field training / fitting:** Same **combustion ReaxFF** **PAH** parametrization as **`[[2017mao-carbon-121-2-formation-incipient]]`**.

**B — Molecular dynamics / sampling:** **Identical** **LAMMPS ReaxFF** protocol to **`[[2017mao-carbon-121-2-formation-incipient]]`** (**100 Å** cubic **periodic boundary conditions**, **0.25 fs**, **NVT** production **2 ns** at each reported temperature, **Nosé–Hoover thermostat** with **100 fs** damping, **50×** monomer replicas, etc.—see sibling for full narrative). **System size & composition:** same **50-copy PAH** cells as the primary page (e.g. **~900 atoms** for **50 naphthalene** molecules as a lower bound; larger PAHs toward **~10000 atoms** per cell—see sibling/`pdf_path`). **N/A — barostat / pressure**: **NVT** cells only.

**C — DFT / static QM:** **Not** used as summarized here.

**D — Review / non-simulation framing:** **Corpus** duplicate registration—mirror substantive **Methods/Findings** edits on **`[[2017mao-carbon-121-2-formation-incipient]]`** first.

## Findings

**Outcomes and mechanisms.** Same **soot inception** story as the **primary** page: **physical stacking** at **low T**, **selective chemical productivity** at **intermediate T**, and **high-T graphitizing** chemistry with **bridged stacks**/**fullerene-like** motifs for large PAHs.

**Comparisons / sensitivity / limitations.** Mirror **`[[2017mao-carbon-121-2-formation-incipient]]`**; this duplicate exists only for **binary provenance** (`papers/QianMao_Carbon_Soot_2017.pdf`).

**Corpus / PDF honesty.** **Duplicate PDF** of the same **DOI**; do not let narrative drift from the **primary** slug.


## Limitations

Keep **one DOI** for citations; retain both PDF hashes only for **binary provenance** tracking.

When updating **scientific** prose, edit **`[[2017mao-carbon-121-2-formation-incipient]]`** first, then mirror **non-provenance** changes here to prevent **content** **divergence** between **duplicate** ingests.

**Science reminder:** **incipient** **soot** mechanisms summarized here are **identical** to the **primary** page—differences should only reflect **PDF** **byte** **provenance**, not alternate **chemistry** claims.

**Chunking note:** substantive **edits** here should be **mirrored** on the **primary** page so **Phase 5** **chunk** **hashes** stay **aligned** for **retrieval** **pipelines** that **deduplicate** by **DOI**.

## Relevance to group

Duplicate corpus registration for the **van Duin** / **Luo** soot nucleation paper.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.carbon.2017.06.009` — `papers/QianMao_Carbon_Soot_2017.pdf` (duplicate of `papers/Mao_Qian_Carbon_soot_2017.pdf` entry).

## Related topics

- [[2017mao-carbon-121-2-formation-incipient]]
- [[reaxff-family]]
