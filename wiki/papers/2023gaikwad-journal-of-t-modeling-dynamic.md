---
id: paper:2023gaikwad-journal-of-t-modeling-dynamic
type: paper
title: "Modeling Dynamic Evolution of Oxygen Vacancies in Solid Oxide Materials"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - method:ereaxff
  - method:monte-carlo
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:oxide-surface
  - keyword:reaxff-application
  - keyword:charge-equilibration
  - keyword:monte-carlo-sampling
candidate_tags: []
source_refs: []
doi: "10.1149/1945-7111/ad0722"
year: 2023
authors:
  - "Prashik S. Gaikwad"
  - "Yun Kyung Shin"
  - "Adri van Duin"
venue: "J. Electrochem. Soc."
pdf_sha256: "9a3ab57dc08b79affc36a117cbbd1a0970ab5cd5fb1d1823adffc2e69702426e"
pdf_path: "papers/Gaikwad_J_Electrochem_2023_O_vacancies.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023gaikwad-journal-of-t-modeling-dynamic -->

## Summary

**Hybrid Monte Carlo / ReaxFF MD** equilibration of **oxygen vacancies** in **BaZr₀.₈Y₀.₂O₃₋δ (BZY20)** is followed by **eReaxFF** simulations that treat **explicit electrons** to follow **electron localization** and **mobility** in the presence of **vacancy–electron correlations**, with implications for **solid oxide electrolysis** and related **high-temperature electrochemical** devices. The **paper** positions **Oᵥ** not as **static** **lattice** **holes**, but as **mobile** **defects** that **restructure** near **interfaces** under **operando**-like **thermal** **driving**, motivating **joint** **MC**/**MD** **equilibration** before **electronic** **structure** **follow-on** with **eReaxFF**. Readers should treat **BZY20** as a **model** **perovskite-related** **electrolyte** **composition** chosen for **Y**/**Zr** **contrast** in **electronic** **response**, not as a **universal** **surrogate** for every **doped** **zirconate**.

## Methods

### Supercell construction

**BZY20** supercells (e.g. **3×3×3** “A” and **4×3×3** “B”) with **isolated O\(_v\)** at distinct **Zr–Zr**, **Zr–Y**, etc. environments (see figures).

### Hybrid MC / ReaxFF MD (B)

**Grand-canonical / hybrid Monte Carlo** + **ReaxFF MD** to equilibrate **O\(_v\)** distributions at **SOEC-relevant** **T** (thermostats/durations in **Computational Details**). The workflow alternates **Monte Carlo** moves that propose **oxygen** **occupancy** changes with **MD** relaxation segments under **ReaxFF**, so **O\(_v\)** distributions evolve from the coupled **MC–MD** equilibration rather than a single static **vacancy** **supercell** (see **Computational Details** for move definitions).

### eReaxFF electronic follow-on

**eReaxFF** trajectories with **explicit electrons** to resolve **trapping vs mobility**; **Y** vs **Zr** site roles in the authors’ analysis.

### MD application (integrated)

**Engine / code:** **LAMMPS**+**ReaxFF**+**eReaxFF**; **MC**/**MD** **hybrid** for **O\(_v\)**. **System & composition:** **BZY20** **3×3×3** and **4×3×3** **supercells**; **N/A — full atom count** in *J. Electrochem. Soc.* **Computational** details. **3D PBC** **bulk** perovskite-type **cell**. **Ensemble, thermostat, timestep, run lengths, target **temperature** (e.g. **~800–1000 K**-class **furnace**-relevant **K** in **SOEC** **O\(_v\)** **equilibration** as reported in the **article**; confirm in **VOR**), NPT vs NVT, barostat, pressure, applied bias for **SOEC**, umbrella/REX:** in **SI** when present—**N/A — not duplicated** on this stub to avoid **inventing** numbers; see **VOR** **PDF**. **N/A** — no **replica exchange** in the main **narrative** summarized here.

## Findings

### Vacancy migration

**O\(_v\)** migrate toward **surfaces**, raising **surface** vacancy content by ~**10%** in their conditions.

### Site-resolved electronics

**Y** tends to **trap** electrons and **slow** migration; **Zr** environments **accelerate** electron migration along sampled paths.

### SOEC-relevant link

**Surface O\(_v\)** enrichment couples to **local electronic density** available for **oxygen evolution**-adjacent processes in the paper’s **SOEC** framing. **Comparisons** to **kMC**/**continuum** in the **SOEC** literature (where cited) are **second-hand** on this page; **sensitivity** of **O\(_v\)** to **T** and **chemical** environment is a **lever** discussed in the **primary** text. **Mechanistic outcomes** tie **O\(_v\)** **migration** vs **Y**/**Zr**-site **trapping** to **wall** **speed** and **local** **polarization** **relaxation**; **comparisons** to **DFT**/**experiment** in the **article** should be read from the **PDF** for **quantitative** **barriers**. **Limitations & outlook (authored in spirit):** **bulk** **supercells** omit **grain** **boundaries** and **electrode** **contacts** that dominate **device** **degradation**; **open questions** include linking **O\(_v\)**-rich **wall** **segments** to **Faradaic** **losses** in **stacks**. **Corpus view:** re-check **K**, **P**, and **eReaxFF** **analysis** **windows** against the **VOR** before **MAS** reuse.

## Limitations

Finite supercells and simulation times may not capture long-range percolation or experimental microstructures; eReaxFF approximations must be benchmarked for each target operating window. The **BZY20** study is explicitly aimed at **SOEC**-relevant **oxygen** **non-stoichiometry**: after **hybrid** **MC/ReaxFF** **equilibration**, **eReaxFF** is used to discuss **where** **electrons** **localize** versus **hop**, with **Y** **trapping** contrasted against **Zr**-associated **mobility** in the authors’ trajectory analysis—use those **site-resolved** **labels** when linking this page to broader **proton**/**oxide** conductor debates. **Grain** **boundaries**, **electrode** **contacts**, and **chemical** **expansion** in **real** **cells** remain outside the **bulk** **supercell** **story** summarized here.

## Relevance to group

Demonstrates **ReaxFF + eReaxFF + MC** tooling for **defective oxide electrolytes** (**Shin**, **van Duin**, INL collaboration).

## Citations and evidence anchors

- DOI: [10.1149/1945-7111/ad0722](https://doi.org/10.1149/1945-7111/ad0722)

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
