---
id: paper:2019maxim-nat-visualization-supercritical
type: paper
title: "Visualization of supercritical water pseudo-boiling at Widom line crossover"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:water-interfaces
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/s41467-019-12117-5"
year: 2019
authors:
  - "Florentina Maxim"
  - "Cristian Contescu"
  - "Pierre Boillat"
  - "Bojan Niceno"
  - "Konstantinos Karalis"
  - "Andrea Testino"
  - "Christian Ludwig"
venue: "Nat. Commun."
pdf_sha256: "7a55eb6d953b10abbf9e976056f5c3180c02978ccd2a3325700cfb07360266a3"
pdf_path: "papers/Others/Maxim_Supercritical_water_NatureComm_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019maxim-nat-visualization-supercritical -->

## Summary

**Supercritical water** is used industrially in **oxidation**, **gasification**, and **nanoparticle** synthesis routes where **local density** controls **solvation** and **reaction** kinetics; yet **macroscopic** **homogeneity** assumptions often hide **strong fluctuations** near **pseudo-critical** crossovers. Maxim et al. use **neutron imaging** to visualize **density fluctuations** in **supercritical water** while heating **isobarically** across the **Widom line** region separating **liquid-like** and **gas-like** supercritical regimes. The **Nature Communications** article (DOI `10.1038/s41467-019-12117-5`) frames **supercritical water** as technologically relevant to **hydrothermal synthesis**, **waste treatment**, **bioenergy**, and **nuclear** applications, while noting that **fundamental** behavior near the **Widom** zone remains incompletely mapped experimentally. The authors connect observations to **pseudo-boiling** theory for **supercritical fluids**, in which **crossover** manifests as **boiling-like** density fluctuations despite **no macroscopic meniscus**.

## Methods

**4 — Neutron imaging experiment (not atomistic MD as the main vehicle).** The *Nature Communications* study uses **neutron** **radiography** / **imaging** at the **Paul** **Scherrer** **Institute** **beamline** **described** in the **article** to follow **time-resolved** **density** **fluctuations** in **supercritical** **water** while the fluid is **heated** **isobarically** through the **Widom**-line **region** that separates **liquid-like** and **gas-like** **supercritical** regimes. The **Introduction** reviews **textbook** **critical** **constants** for water (**T\(_{CP}\) ≈ 647 K**, **P\(_{CP}\) ≈ 221 bar**, **ρ\(_{CP}\) ≈ 322 kg m⁻³**) and the **thermodynamic** **framing** for **pseudo-boiling**; **full** **cell** **geometry**, **neutron** **optics**, and **data** **reduction** are in the **Methods** **PDF** (not re-derived here). **ReaxFF** or **classical** **MD** as the **main** result:** **N/A**—this paper’s **evidence** is **experimental** **(continuum-to-mesoscale)** **on** the **P–T** **paths** **stated** **in** the **VOR** **file**.

## Findings

**1 — Outcomes & mechanisms.** The **imaging** **tracks** **density** **heterogeneity** **(pseudo-boiling-** **like** **contrast** **in** the **neutron** **images**)** as** **isobaric** **heating** **crosses** the **Widom**-associated **LL↔GL** **crossover** **in** **supercritical** **water**—a **phenomenon** **posited** **by** **Widom-line**-based **pictures** of **maxima** **in** **thermodynamic** **response** **functions** but **rarely** **imaged** **in** **situ** on **laboratory** **paths** (per the **PRL/Nat.** **Comms** **-style** **narrative** in the **source**). **2 — Comparisons** **to** **prior** **scenarios** **that** **assume** **thermodynamically** **“homogeneous”** **supercritical** **phases** **(single**-**well**-**behaved** **state** **in** the **classroom** **sense**)**; **this** **work** **favors** a **pseudophase** **(LL/GL)**, **kinetic**-**looking** **decomposition** **in** the **Widom** **delta** **(see** **cited** **Gallo/** **Ha** **-** **line** **literature** **in** the **text** for** **how** the **Widom** **framework** is **imported** **to** **water**)**. **3 — Sensitivity** **&** **levers** — **P–T** **trajectory** (especially **P/** **P\(_C\)** **<** **~1.5** in the **isobaric** **protocol** **cited** **in** the **Widom**-line **discussion**), **heating** **rate** **(through** **affecting** **how** **sharply** the **Widom** **zone** **is** **encountered** in **time**)** , **and** **local** **density** **(which** **couples** to **solvating**-**reaction** **kinetics** **in** **applications**)** are **all** **implicit** **knobs** in **interpreting** the **imaging** **(see** **##** **Limitations** for** **where** the **neutron** **probe** **stops**)**. **4 —** **Authored** **limitations** & **outlook** — **reactor-** and **pilot-** **scale** **energy** **and** **separations** **challenges** **(already** **flagged** **in** the **article’s** **motivation**)**; **5 —** **Corpus** / **PDF** **honesty** — **reproduce** **plots** and **P–T** **paths** **from** the **publisher** **version** **(not** **a** **short** **p1**-**2** **extract** **only**)**. **6 —** **Atomistic** **kinetics** — **N/A** **in** the **neutron** **paper** **as** **a** **primary** **result**; **molecular** **reaction** **or** **diffusion** **explanations** **are** **outside** **this** **experimental** **work’s** **direct** **claims** **(per** the **separation** **in** our** **##** **Limitations**).

## Limitations

**Neutron imaging** resolves **mesoscale** fluctuations; **molecular** mechanisms require separate **simulation** studies. **Operational** challenges and **energy balances** for industrial **supercritical** processes remain as discussed in the introduction.

**Confidence rationale:** `high`—peer-reviewed experimental article; summary tied to abstract/extract.

## Citations and evidence anchors

**Nature Communications** hosts **PDF**, **HTML**, and **supplementary** files under the article DOI; if **neutron** **supplement** movies are added post-publication, fetch them from the **publisher** site rather than relying on this corpus PDF alone. DOI: [10.1038/s41467-019-12117-5](https://doi.org/10.1038/s41467-019-12117-5).

## Reader notes (navigation)

**Hydrothermal** **synthesis** papers in the corpus should cite this work when discussing **bulk** **SCW** **heterogeneity**, while **atomistic** **ReaxFF** studies of **SCW** (**[[2017ai-the-journal-reactive-force-2]]**) cover complementary **scales**.

- [[theme-reactive-md-corpus]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

— 
