---
id: paper:2014raju-venue-nl404533k
type: paper
title: "Mechanisms of oriented attachment of TiO₂ nanocrystals in vacuum and humid environments: reactive molecular dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - material:oxide
  - domain:water-silica-geo
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/nl404533k"
year: 2014
authors:
  - "Raju, Muralikrishna"
  - "van Duin, Adri C. T."
  - "Fichthorn, Kristen A."
venue: "Nano Letters"
pdf_sha256: "b90c3e1dde40cc93525aed6f237f9c6deacd3641187616ad262edaf753574219"
pdf_path: "papers/Raju_Nano_Letters_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014raju-venue-nl404533k -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

ReaxFF MD compares aggregation of Wulff-shaped anatase nanocrystals in vacuum versus water vapor. Vacuum collisions coalesce along approach directions into polycrystalline agglomerates, whereas humid conditions enable reorientation into oriented attachment (OA) pathways mediated by dynamic hydrogen-bond networks between surface hydroxyls and oxygens, yielding single or twinned crystals. OA is argued to dominate on facets with the greatest water-dissociation propensity, matching experimentally observed aqueous OA and underscoring solvent control for oxide nanoparticle synthesis (abstract; introduction, extract pages 1–2). The introduction reviews **OA** history (**Penn & Banfield** on hydrothermal anatase) and frames **intrinsic** nanocrystal forces versus **solvent-mediated** interactions; **ReaxFF** is chosen to reach **nanometer** particles with **reactive** chemistry at cost below **ab initio** MD (introduction, extract).

## Methods

**Ti/O/H ReaxFF** follows **Kim et al.** with validations against **DFT** reference data and prior **molecular dynamics** benchmarks on **water dissociation** across **anatase** and **rutile** facets; the parameter set shares **O/H** and general terms with broader organic/inorganic **ReaxFF** lines for **transferability** (methods narrative, extract). **Wulff** **bipyramidal** **anatase** nanoparticles are studied at two sizes (**~2691** Ti+O atoms **large**, **~840** atoms **small**), with additional **asymmetric** shapes in SI figures referenced in text. **Eight** nanocrystals are placed in **125 × 325 × 125 Å** cells with varied **separations/orientations**; **NVT** at **573 K** for **1.0–2.0 ns** (simulation cells of order **15 000–18 000** atoms), using **ReaxFF** in **ADF** as stated (methods, extract). **Timestep and thermostat:** **N/A —** not on the two-page extract (`normalized/extracts/2014raju-venue-nl404533k_p1-2.txt`); see **`pdf_path`**. **Cell boundary / PBC details beyond the box size:** **N/A —** confirm wording in full letter. **Barostat:** **NVT** excerpt implies **constant-volume** **thermal** control; **NPT** — **N/A —** not stated on indexed pages. **Pressure / stress targets:** **N/A —** same scope. **Electric field / enhanced sampling:** **N/A —** not used in excerpted protocol description.

### 2 — Force-field training

**N/A —** this letter **applies** the **Kim *et al.*** **Ti/O/H** training; it does not report a new **ReaxFF** fit.

## Findings

**Outcomes and mechanisms.** **Vacuum** aggregation proceeds along the **direction of approach** into **polycrystalline** mergers **without oriented attachment (OA)**, consistent with prior **simulation** work cited (**Alimohammadi & Fichthorn**). **Humid** runs show **reorientation** and **OA** into **single/twinned** crystals via **dynamic hydrogen-bond networks** between **surface hydroxyls** and **oxygens**, implicating **interfacial** **water chemistry** in the **growth** pathway.

**Comparisons.** The **abstract** states the **nanocrystal** behavior is **consistent with experiment** for **aqueous** **oxide** systems and highlights solvent control relative to **vacuum**.

**Sensitivity.** **Temperature** is set to **573 K** to echo cited **hydrothermal** experiments; **humidity** (dissociative/molecular water at surfaces) is the key environmental variable contrasted with **vacuum**.

**Limitations and outlook.** Finite **nanocrystal** sizes, finite **simulation** times, and idealized vapor-phase humidity models mean **quantitative** transfer to all colloidal syntheses requires caution—authors nevertheless argue for a **general** solvent-mediated mechanism for **aqueous oxide** **nanoparticle aggregation**.

**Corpus honesty.** Grounded in **`pdf_path`** and **`normalized/extracts/2014raju-venue-nl404533k_p1-2.txt`**; deeper numerical tables and **SI** movies should be checked in the full **Nano Letters** PDF.

## Limitations

Nanocrystal size and simulation times remain finite; real colloids include counterions and broader polydispersity omitted here.

## Relevance to group

Raju–van Duin–Fichthorn collaboration extending TiO₂/water ReaxFF work into nanostructure growth mechanisms.

## Citations and evidence anchors

- Nano Lett. 2014, 14, 1836–1842; DOI `10.1021/nl404533k` (extract page 2 footer).
- Abstract + OA background (extract pages 1–2).

## Related topics

- [[reaxff-family]]
