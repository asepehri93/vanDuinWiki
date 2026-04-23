---
id: paper:2014rahnamoun-venue-jp4121029
type: paper
title: "Reactive molecular dynamics simulation on the disintegration of Kapton, POSS polyimide, amorphous silica, and Teflon during atomic oxygen impact using the ReaxFF reactive force-field method"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
  - domain:oxides-ceramics
candidate_tags: []
source_refs: []
doi: "10.1021/jp4121029"
year: 2014
authors:
  - "Rahnamoun, A."
  - "van Duin, A. C. T."
venue: "Journal of Physical Chemistry A"
pdf_sha256: "93cc87a97c87e24e54e52e12848c934fa661ccf1620434cbd45f07e2e2a13193"
pdf_path: "papers/Rahnamoun_Kapton_JPCA_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014rahnamoun-venue-jp4121029 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Low-Earth-orbit (LEO)** environments expose spacecraft materials to fast **atomic oxygen (AO)** formed by **solar UV** dissociation of **O\(_2\)**, with introductory text citing **~4.5 eV** collisions for **AO** (and **~8 eV** for **N\(_2\)**) as representative energy scales in the exposure model discussed in the paper. The authors simulate **ReaxFF** **reactive molecular dynamics** for **Kapton polyimide**, **POSS–polyimide** hybrids, **amorphous silica**, and **Teflon** under **comparable impact** conditions to compare **surface chemistry** and **erosion** propensity. **Kapton** is described as a widely used **lightweight** **polyimide** film; **POSS** additives (**(RSiO\(_{1.5}\))\(_n\)**, commonly **n = 8**) appear in space-qualified **composites**; **silica** and **fluoropolymers** likewise appear in thermal-protection and insulation roles. The study positions **ReaxFF** as enabling **large** reactive cells relative to **QM** for these **polymer**/**oxide** chemistries.

## Methods

### Materials modeled (condensed targets)

- **Kapton polyimide**, **POSS–polyimide** hybrids, **amorphous silica**, and **Teflon** targets are represented as **condensed-phase** models suitable for **atomic oxygen** impact simulations (**abstract**; introduction motivates each material class).

### Reactive MD (ReaxFF)

- **ReaxFF** **reactive MD** allows **bond formation and scission** during **atomic oxygen** bombardment, enabling chemistry beyond **elastic** collision models (**abstract**).

### Impact and environmental parameters (qualitative)

- Simulations vary **impact energy**, **target temperature**, and **composition**—including **silicon enrichment** in **Kapton**-like structures—to probe **fragmentation** and **heat release** trends (**abstract**).

### Analysis

- Trajectories are interpreted in terms of **relative erosion resistance**, **oxidation exothermicity**, and **heat-transfer** effects within solids during impacts (see **Findings**).

### 1 — MD application (ReaxFF reactive MD)

**Engine / code:** **ReaxFF** is invoked through the authors’ “**ReaxFF reactive force-field program**” language; the indexed extract (`normalized/extracts/2014rahnamoun-venue-jp4121029_p1-2.txt`) does not name a separate MD package before truncation—**N/A —** confirm **LAMMPS** or other driver in **`pdf_path`** §2+. **System size and composition:** slab models are built for **Kapton**, **Kapton–POSS**, **amorphous silica**, and **Teflon**; the indexed **§2.1** reports slab **mass densities** of **1.3**, **2**, **2.62**, and **2.2 g cm\(^{-3}\)** respectively, with **30**, **20**, and **5** polymer **monomers** for Kapton, Kapton–POSS, and Teflon, and **71** Si\(_8\)O\(_{12}\) cages compressed into a single **silica** molecule. **Boundaries / periodicity:** **N/A —** cell vectors and **PBC** details are not on the truncated extract pages—see figures **2–5** in the article. **Protocol stages:** after slab preparation, each run follows **four steps** (their **Figure 6**); the excerpt records **geometry optimization** followed by **NVT** equilibration before the remainder of the schedule (text cuts at “equilibra…”). **Timestep, thermostat coupling, total trajectory length, and barostat usage:** **N/A —** not present on the indexed two pages; read **`pdf_path`** §2.2 onward. **Temperature / impact energy sweeps:** the **abstract** states **impact energies**, **material composition**, and **target temperature** are varied across the comparative AO-impact series. **Pressure / stress control:** **N/A —** not specified on the indexed excerpt. **Electric field:** **N/A —** not mentioned for these AO bombardment runs. **Replica / enhanced sampling:** **N/A —** not part of the described protocol.

### 2 — Force-field training

**N/A —** this article **applies** **ReaxFF** for AO chemistry rather than reporting a new element-by-element refit in the indexed pages.

## Findings

**Outcomes and mechanisms.** **ReaxFF** trajectories are summarized as showing **Kapton** **less resistant** than **Teflon** to **AO damage**, with the authors stating **good agreement with experiment**. **Amorphous silica** is described as the **most stable** of the set **before** strongly **exothermic silicon oxidation** sets in, after which **oxidation** accelerates **disintegration**. **Silicon enrichment in the bulk** of Kapton-like models is reported to **enhance stability** against AO impact.

**Comparisons.** Explicit **experimental** comparison is claimed for the **Kapton vs Teflon** resistance ordering; other statements are framed as simulation-based screening.

**Sensitivity / design levers.** The **abstract** highlights sweeps of **AO impact energy**, **material composition** (including Si content in Kapton), and **temperature**, plus separate **canonical MD** runs used to argue that **increased in-material heat transfer** during AO impact **reduces disintegration** (emphasized for **silica** collisions).

**Limitations / outlook.** The introduction notes additional **LEO** stressors (**UV**, **micrometeoroids**, **debris**, **thermal cycling**) and that **AO+UV** combinations can **strongly increase degradation**—not fully replicated in the excerpted simulation description.

**Corpus honesty.** Detailed **collision schedules**, **cell sizes**, and **analysis metrics** beyond **`normalized/extracts/2014rahnamoun-venue-jp4121029_p1-2.txt`** require **`papers/Rahnamoun_Kapton_JPCA_2014.pdf`** (see §2–3).

## Limitations

The **abstract**-level summary does not substitute for full **multi-impact**, **radiation**, or **contamination** scenarios in **LEO**; **UV** and **electron** exposures noted in the introduction are **not** fully coupled in the simulations described on the first pages.

## Relevance to group

van Duin senior author on spacecraft materials screening with ReaxFF, parallel to other AO degradation entries.

## Citations and evidence anchors

- J. Phys. Chem. A 2014, 118, 2780–2787; DOI `10.1021/jp4121029` (extract page 2 footer).
- Abstract (extract page 1).

## Related topics

- [[reaxff-family]]
