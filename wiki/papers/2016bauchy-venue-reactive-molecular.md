---
id: paper:2016bauchy-venue-reactive-molecular
type: paper
title: "Reactive molecular dynamics simulations of sodium silicate glasses — toward an improved understanding of the structure"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - material:silicate-glass
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:silica-silicate
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1111/ijag.12248"
year: 2016
authors:
  - "Yingtian Yu"
  - "Bu Wang"
  - "Mengyi Wang"
  - "Mathieu Bauchy"
  - "Gaurav Sant"
venue: "Int. J. Appl. Glass Sci."
pdf_sha256: "682916e9d197d87d530d25a47ababb6e01313a2a6be0e3a3f3c4b63d1ec78dd7"
pdf_path: "papers/ReaxFF_others/bauchy_reaxff_jjag2016.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2016bauchy-venue-reactive-molecular -->

## Summary

Yu, Wang, Wang, Bauchy, and Sant use **ReaxFF reactive molecular dynamics** to study **sodium silicate glass** structures and compare the resulting predictions to both a **classical** silicate force field and experimental structural references (*Int. J. Appl. Glass Sci.*, DOI `10.1111/ijag.12248`). The central question is pragmatic for the **glass** community: when modeling **multicomponent silicates**, does a **bond-order** reactive potential materially improve **short-** and **medium-range** **order**—including **modifier** **Na⁺** effects on the **Si–O** network—relative to a cheaper **classical** model, without paying **ab initio** costs? The paper frames **ReaxFF** as an intermediate tier: more flexible than fixed-charge **silicate** models for **chemically** **responsive** environments, yet still accessible for **large** **amorphous** cells.

## Methods

### MD application (atomistic dynamics)

Yu *et al.* build glasses of **~3000 atoms** (**alkali-rich sodium silicate (NS)**) in **3D periodic** cubic cells using **LAMMPS** (explicitly named in the **Methodology** section of **`pdf_path`**). **Glass formation (classical stage):** atoms are placed randomly (avoiding overlaps), melted at **4000 K** for **100 ps**, then **linearly quenched** from **4000 K → 300 K** at **1 K/ps** under **NPT at zero average pressure**; the cell is further held at **300 K** for **1 ns** **NPT** to relax the quenched glass. **Thermostat / barostat:** the article documents **NPT** at **0 pressure** through these classical stages but **does not name** a specific **thermostat**/**barostat** algorithm in the extracted **Methodology** text—confirm coupling details in **`pdf_path`** for exact integrator settings. This entire melt–quench pathway uses the classical **Teter** empirical silicate potential for efficiency.

**ReaxFF refinement stage:** the classical-quenched structure is **relaxed for 1 ns** with **ReaxFF** in **NPT at zero pressure** before structural analysis; the authors **do not** perform a full high-temperature **ReaxFF** quench, arguing that **Na–O** dynamics at melt temperatures would force an **extremely small timestep** and make a full **ReaxFF** quench prohibitively expensive. **Timestep (classical melt/quench):** **N/A —** the article discusses timestep demands qualitatively for **ReaxFF** at high **T** but **does not print** an explicit **Δt** value for the **Teter** stages in the PDF text extracted here—copy integrator settings from **`pdf_path`** if you need exact numbers.

**Electric field:** **N/A — not used.** **Replica / enhanced sampling:** **N/A — not used.** The introduction’s **~10×** (**ReaxFF** vs classical MD) and **~10⁶×** (**ab initio** vs classical) remarks are **authored scaling** statements, not timings from this study’s hardware.

### Force-field training

**N/A — not a new ReaxFF parameterization paper**; the study **applies** **ReaxFF** and contrasts it to a classical model rather than reporting a fresh QM optimization campaign for NS glasses.

### Static QM / DFT

**N/A — not a DFT production study**; QM appears as motivation and accuracy context for when reactive vs classical vs **ab initio** methods are appropriate.

## Findings

- **Structural accuracy:** The authors report that **ReaxFF** improves **short-** and **medium-range** structure relative to the tested **classical** potential, especially in capturing **modifier effects** on the **Si–O** network where **bond-order** responsiveness matters.
- **Na⁺ / network coupling:** Because **bond orders** adapt to local environments, **ReaxFF** better tracks **Na⁺-related** structural signatures (e.g., **Si–O** bond elongation / connectivity patterns) than the **fixed-charge** classical description in their comparison.
- **Scope honesty (authored):** The paper emphasizes **static structure** validation here and notes that **dynamics**, **mechanics**, and **long-time aging** need **separate** validation beyond this structural benchmark.
- **Workflow implication (authored discussion):** For **flexible** depolymerized glasses, the authors discuss combining **classical quench** with subsequent **ReaxFF** refinement as a pragmatic route; **silica-like rigidity** makes that shortcut problematic (as they argue referencing prior silica work).

## Relevance to group

Glass and oxide-network chemistry overlaps with geochemical and materials themes in ReaxFF applications.

## Citations and evidence anchors

- DOI: [10.1111/ijag.12248](https://doi.org/10.1111/ijag.12248)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
