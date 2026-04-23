---
id: paper:2020ndayishimiye-open-ceramic-roadmap-densification
type: paper
title: "Roadmap for densification in cold sintering: chemical pathways"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:review-or-perspective
  - keyword:oxide-surface
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1016/j.oceram.2020.100019"
year: 2020
authors:
  - "Arnaud Ndayishimiye"
  - "Mert Y. Sengul"
  - "Takao Sada"
  - "Sinan Dursun"
  - "Sun Hwi Bang"
  - "Zane A. Grady"
  - "Kosuke Tsuji"
  - "Shuichi Funahashi"
  - "Adri C. T. van Duin"
  - "Clive A. Randall"
venue: "Open Ceramics"
pdf_sha256: "8e372023d01827362eecd6ae33017fc71271d621dff65efe97ae151b17fdcc93"
pdf_path: "papers/Ndayishimiye_Roadmap_ColdSintering_2020.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020ndayishimiye-open-ceramic-roadmap-densification -->

## Summary

The **abstract** defines **cold sintering (CSP)** as densification of ceramics and composites at **very low temperatures (T < ~400 °C)** with **uniaxial pressure** and a **transient solvent**, arguing that CSP can offer **energy and emission savings** and **fast processing** versus conventional sintering. It states that CSP has been applied across **many materials, compounds, solid solutions, and composites**, and that **transient phase selection** and **subtle chemical reactions** with powders drive densification—while **in situ** interrogation of chemistry under CSP conditions remains difficult. The paper aims to **summarize main pathways** and chemical insights used to cold-sinter “most” important ceramics/composites, highlight **current understanding**, and flag **limitations and challenges**. Historically, the introduction traces **pressure + solvent** routes from **cement** and **hydrothermal** lineages through **hydrothermal hot pressing** and related methods, then positions modern CSP interest and **pressure-solution creep** as the dominant densification picture.

## Methods

The work is primarily a **review and taxonomy**, not a single benchmark study. **Section 2.1** (per extract) describes representative **lab protocols**: manual mixing of powder and transient liquid (**agate mortar**, **2–5 min**), loading into **12.6 or 13 mm** steel dies, **uniaxial pressing** with **Carver** or **ENERPAC**-style presses (sometimes coupled to **dilatometry** / **Keyence** displacement sensing), an initial **room-temperature** hold under pressure (**~10 min**) for **particle rearrangement**, then **ramp** (**~20 °C min⁻¹** stated) to the **sintering temperature**, dwell, and **manual or automatic pressure readjustment** during shrinkage—with **conditions summarized in Supplementary Table S1** in the article. **Section 2.2** explains **pressure-solution** mechanics (high-stress contact dissolution vs lower-stress precipitation through **thin liquid films**) and contrasts activation barriers with **Coble/Nabarro–Herring** creep. The article cites **ReaxFF molecular dynamics** among tools for interrogating **interfacial chemistry** alongside experiments.

## Findings

**Mechanism narrative:** Densification is framed as **material- and solvent-specific**, with **successful** CSP often relying on **transient chemistries** distinct from the final ceramic phase. The authors stress that **fundamental CSP understanding** remains challenging because **instrumentation** for **in situ** reaction monitoring is limited, yet **chemistry** is “undeniable” in **solvent selection** and proposed mechanisms. **Practical takeaway:** classifying **rate-limiting chemical steps** versus **mechanical compaction** is essential for **scaling** CSP manufacturing. **Modeling angle:** **atomistic simulation** (including **reactive MD**) complements characterization for **interfacial reaction sequences**—consistent with the **ReaxFF** keyword in the article metadata.

## Limitations

Roadmap articles **select** literature rather than exhaust it; **processing windows** in §2.1 are **illustrative** of common lab practice, not universal industrial recipes. Quantitative **kinetic parameters** for each material system require **primary sources** cited within the review rather than this summary.

## Relevance to group

Lead/corresponding Penn State authors with van Duin for reactive modeling hooks to CSP chemistry.

## Reader notes (navigation)

- [[2020ndayishimiye-open-ceramic-roadmap-densification-2]] (journal pre-proof PDF)
- [[2020ndayishimiye-journal-of-t-comparing-hydrothermal]] (ZnO HS vs CSP + ReaxFF)
- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
