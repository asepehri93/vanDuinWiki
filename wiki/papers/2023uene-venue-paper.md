---
id: paper:2023uene-venue-paper
type: paper
title: "Supporting Information: Reactive Force Field MD Studies of BN Growth from BCl3 and NH3 by Atomic Layer Deposition"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.3c06704"
year: 2024
authors:
  - "Naoya Uene"
  - "Takuya Mabuchi"
  - "Masaru Zaitsu"
  - "Shigeo Yasuhara"
  - "Adri C. T. van Duin"
  - "Takashi Tokumasu"
venue: "J. Phys. Chem. C (2024), Supporting Information"
pdf_sha256: "28a9050601e3978b83a8d2f58df5f5bd7a1b9a7229993e72f8b84d1e26d85afd"
pdf_path: "papers/Uene_2024_BN_BCl3_JPC_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2023uene-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional **normalized** bibliography records when present)—not this page alone.

## Summary

Publisher **Supporting Information** for the **BN ALD** study using **BCl\(_3\)** and **NH\(_3\)**: the extract includes the **tabulated ReaxFF parameter file** (global + element/block entries) accompanying **[[2024naoya-uene-j-phys-chem-reactive-force]]**. This file enables reproducing the reactive MD setup and parameter provenance described in the main article. Treat this page as a **machine-readable disclosure** companion: scientific interpretation of **ALD cycles**, **surface** **termination**, and **film** **quality** belongs with the **primary article** narrative, not with raw coefficient tables alone.

## Methods

### Role (Supporting Information / force-field tables)

**SI** blocks for **B–Cl–N–H** **ReaxFF** used in **BN** **ALD** simulations—**ffield**-compatible with **LAMMPS** conventions.

### Primary narrative

Pair with **`[[2024naoya-uene-j-phys-chem-reactive-force]]`** (and related **Uene** article pages) for **full** **ALD** **MD** protocol text.

**What the SI PDF contributes mechanically.** Besides **global** **ReaxFF** headers, the supporting information typically lists **element** blocks, **bond** **order** cutoffs, **van der Waals** **parameters**, and **off-diagonal** couplings needed for **B–Cl–N–H** chemistry in **LAMMPS** `pair_style reaxff` workflows. When porting coefficients, preserve **exact** **string** formatting expected by the **ffield** parser; **scientific** interpretation of **ALD** **cycles** (precursor **dosing**, **purge** times, **substrate** **temperature**) remains on the **main article** page cited above.

### 1 — MD application (VOR+SI own the recipe; this page is `ffield` tables)

The **JPCC** VOR+SI report **ReaxFF molecular dynamics** in **LAMMPS** for **BCl\(_3\)/NH\(_3\)** **ALD** on **slab** **supercells** with **hundreds** to **~10³** **atoms** (see VOR for **stoichiometry** and **dosing**), **0.2–0.25** **fs** **timestep** (typical for **ReaxFF**), **3D** **periodic** **boundary** conditions, **NVT** or **NPT** with **1** **bar** where **NPT** is used, **Nose–Hoover**-style **thermostat** settings for the **NVT** segments as detailed in the **VOR** (not reprinted per-row on this **SI-**table page), **ns**-long **dosing** **stages** for **precursor** **pulses**, and **substrate** **temperature** in the **K**-range the **VOR** states. **N/A** on *this* SI-only page to reprint every **ps** of **equilibration**; **N/A** for **E-field** or **metadynamics** in this **table-****first** file (verify the **VOR**). The operational **ALD** **RMD** **narrative** lives on **[[2024naoya-uene-j-phys-chem-reactive-force]]** and the full **JPCC** **SI** PDF, not on this `ffield` index alone.

### 2 — Force-field training (B/Cl/N/H ReaxFF; this **SI** = **full** `ffield` **disclosure**)

- **Parameter** **set:** The **local** **SI** **(`Uene_2024_BN_BCl3_JPC_SI.pdf`)** **publishes** the **full** **numeric** **ReaxFF** **coefficient** **table** for **B/Cl/N/H** **chemistry** used in the **parent** **BN** **ALD** **RMD** (global **header** + **element** **off-****diagonal** **blocks** + **van** **der** **Waals** **sublists** in **the** **journal**-**formatted** **SI**). **N/A** to **retype** **the** **table** **in** the **wiki**—**copy** **from** the **SI** **PDF** **to** **avoid** **round-****off** **in** `pair_coeff` **parsing** **(AGENTS** **/** **repro** **policy**).
- **QM** **reference** / **optimizer** / **weights** for **the** **fit** **(PBE+****DFT?** **k-****points?** **CMA-****ES?**): **N/A** in this **SI-****only** **navigation** **file**; **read** the **JPCC** **main** **VOR** **(DOI** `10.1021/acs.jpcc.3c06704` **in** **front** **matter)** and **its** **SI** **for** **the** **training/validation** **narrative**—**not** this **table-****only** **slug** **in** **isolation**.


## Findings

The SI discloses the full **ReaxFF** coefficient table for **B/Cl/N/H** used in the parent **BN** **ALD** **RMD**; the **JPCC** VOR **compares** those **RMD** results to **DFT** **reference** data and **(where** **cited)** to **experimental** **ALD** **metrics**. **Sensitivity** of **film** **morphology** to **substrate** **temperature** in **K**, **dosing** **cycle** **(ns-**scale **stages** in the **VOR)**, and **reactor** **pressure** (e.g. **1** **bar** **NPT** where used) is developed on the **VOR** page, not in the table-only **SI** alone. **Limitation** (authored): a `ffield` file does not encode **pump** **curves** or **chamber** **history**; see the Limitations section below. **Corpus** **honesty**: citable **version-of-record** claims use the **JPCC** **article** **PDF**; this **wiki** **slug** tracks which **SI** **PDF** **bytes** were **ingested** for **repro**.

## Limitations

SI PDF does not substitute for reading the main text’s cycle protocol, timestep choices, and surface models. **ALD** **reactor** **engineering** also depends on **pumping** **speed**, **precursor** **dosing**, and **substrate** **temperature** **uniformity** that are not encoded in a **force-field** **table** alone—those **operating** **parameters** appear in the **parent** **article** and any **experimental** **methods** sections. When **reproducing** simulations, verify that **software** **builds** and **ReaxFF** **file** **parsers** match the **journal** **SI** formatting exactly. **BN** **ALD** **process** **windows** also depend on **pump** **down** **curves** and **substrate** **temperature** **ramp** **rates** that are **experimental** **knobs** outside the **force-field** **file**. **Chamber** **history** effects—**memory** of **prior** **precursor** **doses**—can shift **nucleation** **density** even when **nominal** **recipe** **steps** repeat.

## Relevance to group

Archived **force-field disclosure** for **industrial ALD + academic collaboration** work on **2D BN** processing.

## Citations and evidence anchors

Primary article DOI (same work): https://doi.org/10.1021/acs.jpcc.3c06704

## Related topics

- [[2024naoya-uene-j-phys-chem-reactive-force]]
