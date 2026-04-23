---
id: paper:2022clares-at-ah-at-at-tx-abs
type: paper
title: "Increasing density and mechanical performance of binder jetting processing through bimodal particle size distribution"
updated: "2026-04-23"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - material:alloy-bulk
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.18063/msam.v1i3.16"
year: 2022
authors:
  - "Ana Paula Clares"
  - "Yawei Gao"
  - "Ryan Stebbins"
  - "Adri C. T. van Duin"
  - "Guha Manogharan"
venue: "Mater. Sci. Addit. Manuf."
pdf_sha256: "f208fabf66447c987a4e3cc2e35aa1f2325840acce6d5688e6554f03ea425fbd"
pdf_path: "papers/Clares_Bimodal_Binder_Jetting_MSAM_2022_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022clares-at-ah-at-at-tx-abs -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the **MSAM** article identified by `doi` and `pdf_path`. **Percent** improvements and **sinter** schedules should be verified against the **PDF**.

## Summary

Binder jetting of stainless steel 316L compares several unimodal powder size groups to bimodal blends of coarse and fine particles under shared processing conditions. Sintered density and flexural strength rise markedly for bimodal feeds; companion ReaxFF molecular dynamics highlights stronger interparticle bonding when fines fill voids between coarser particles. **Binder jetting** is attractive for **complex** **geometries** but **green** **density** limits **final** **mechanical** properties; **particle** **packing** optimization is therefore a central **process** knob (introduction framing).

## Methods

**1 — MD application (atomistic dynamics).** The article reports **ReaxFF**-based atomistic simulations (LAMMPS/PuReMD class) used to compare unimodal and bimodal **SS316L** powder-contact configurations and neck-formation trends.

- **System size & composition:** Stainless steel 316L particle-contact models (unimodal vs bimodal packing motifs); exact atom counts, box dimensions, and oxide-fraction setup are not stated in this abstract-thin/galley source.
- **Boundaries / periodicity:** **N/A — not stated** in the available abstract-level source (no explicit PBC/non-PBC configuration reported).
- **Ensemble:** **N/A — not stated** in the available source (no explicit NVE/NVT/NPT declaration in the indexed text).
- **Timestep:** **N/A — not stated** in the available source.
- **Duration / stages:** **N/A — not stated** in the indexed abstract-level text for this slug (no explicit equilibration/production times are provided).
- **Thermostat:** **N/A — not stated** in the available abstract-level source (thermostat type and damping/time constant not reported here).
- **Barostat:** **N/A — not stated** in the available source.
- **Temperature:** **N/A — not stated** for the MD trajectories in this source; only the experimental furnace schedule is described elsewhere on this page.
- **Pressure:** **N/A — not stated** for the MD trajectories in the available source.

The ReaxFF layer is used to interpret relative interparticle bonding/necking trends and does not replace continuum-scale sintering kinetics. **N/A** — static electric field; **N/A** — replica/enhanced sampling.

**2 — Force-field training.** **N/A** — the work **applies** a **published**-style **stainless-**-**relevant** **ReaxFF**; **retraining** is **out** of **scope** on this page.

**3 — Static QM / DFT-only.** **N/A**.

**4 — Additive processing and tests.** **Binder** **jet** **deposition** on **unimodal** and **bimodal** **SS316L** **powders**; **green** **cure**/**depowder**; **sintering** in **inert** **Ar** with a **ramp** to **\(\sim 1120\,^\circ\text{C}\)** and **holds** as **reported**. **Density** by **geometric**/**mass** **or** **micro-CT** where used; **three-**-**point** **flexure** (with **statistical** tests, e.g. **ANOVA** or **Kruskal–Wallis** as in the **article**). **Paired** **slug** under **DOI** **10.18063/msam.v1i3.20** (`paper:2022clares-at-ah-at-at-tx-abs-2`, **VOR**-style **PDF**) is the **same** **study**; prefer **VOR** **for** **pagination** **when** **citing** **figure**s.

## Findings

**Outcomes and mechanisms (reported in the source).** The abstract-level comparison claims **\(\sim 20\%\)** higher **sintered** **density** and **\(\sim 170\%\)** higher **flexural** **strength** for **bimodal** **feeds** relative to the **best** **unimodal** **group** under their **AM**+**furnace** **window** (confirm **exact** **percent** **ranges** in the **VOR** **text**; the **admonition** in **`## Summary`** on **%** still applies if **not** re-verified). The authors **interpret** the **gains** as **better** **packing**/**necking** **(experiment)** with **ReaxFF**-consistent **trends** of **stronger** **necks** when **fines** **infill** **pores** **in** a **coarse** **skeleton** **(simulation)**.

**Comparisons.** Bimodal vs unimodal **at** **matched** **AM**+**furnace** **settings**; **experiment**+**ReaxFF** are **juxtaposed** (not a **1:1** **parameter**-**match** **of** **full** **sinter** kinetics).

**Corpus / KB honesty.** The corpus **`pdf_path`** is a **galley** for **10.18063/msam.v1i3.16**; **sibling** **`2022clares-at-ah-at-at-tx-abs-2`** hosts the **online** **issue** file—see the **duplicate** **note** below and **`## Limitations`**.
## Limitations

Furnace batching and atmosphere variability can scatter strength results; ReaxFF models idealize particle surfaces and sinter chemistry.

**Binder** chemistry and **residual** **organics** after **debinder** are not captured in **metal** **ReaxFF** **necks**—treat **simulation** as **illustrative** of **contact** **adhesion** trends only.

**Process** **repeatability:** **binder** **jetting** **porosity** is sensitive to **powder** **spreadability** and **layer** **uniformity**—the **bimodal** gains should be interpreted within the **specific** **machine** **settings** reported.

## Relevance to group

van Duin-group reactive MD coupled to additive-manufacturing experiments for metallic powder beds.

!!! note "Duplicate ingest"
    See also `paper:2022clares-at-ah-at-at-tx-abs-2` for the online issue PDF of the same study under a different MSAM page/DOI.

## Citations and evidence anchors

<!-- Prefer DOI link when `doi` is present in frontmatter. -->

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
