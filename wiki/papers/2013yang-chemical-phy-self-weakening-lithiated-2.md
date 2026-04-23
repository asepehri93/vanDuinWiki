---
id: paper:2013yang-chemical-phy-self-weakening-lithiated-2
type: paper
title: "Self-weakening in lithiated graphene electrodes"
updated: "2026-04-20"
confidence: med
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:graphene-carbon
  - keyword:reactive-md
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:mechanics-tribology
  - domain:reactive-md
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.cplett.2013.01.048"
year: 2013
authors:
  - "Hui Yang"
  - "Xu Huang"
  - "Wentao Liang"
  - "Adri C. T. van Duin"
  - "Muralikrishna Raju"
  - "Sulin Zhang"
venue: "Chem. Phys. Lett."
pdf_sha256: "efd24f0a7ed7ce510b4164eee0d0e12056ff18b87a4505d058351dac94448d8d"
pdf_path: "papers/Yang_Huang_Zhang_Raju_CPLetters_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013yang-chemical-phy-self-weakening-lithiated-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For numerical results and mechanistic detail, use the peer-reviewed article (`papers/Yang_Huang_Zhang_Raju_CPLetters_2013.pdf`).

## Summary

Reactive molecular dynamics with **ReaxFF** is used to study **fracture in lithiated graphene** with a pre-existing crack. The work argues that **lithium migrates toward the crack tip** under the stress gradient, **accumulates at the tip**, and both **relieves stress** and **weakens bonds** at the tip; the **chemical weakening** contribution is reported as the **dominant** factor in the modeled **self-weakening** behavior, with implications for **degradation of carbonaceous anode materials**.

## Methods

**1 — MD application (atomistic dynamics).** **Reactive MD** with **ReaxFF** treats **Li–C** / **hydrocarbon** chemistry for a **K-dominant** cracked **graphene** patch of **1910 carbon atoms** (`papers/Yang_Huang_Zhang_Raju_CPLetters_2013.pdf`). **Atoms within ~3 Å** of the patch **boundary** are **fixed**; the interior is free. The pristine sheet is relaxed at **10 K** with a **Berendsen thermostat**, then **mode I** crack-tip displacements are imposed using the **K-dominant** elastic field with **Poisson ratio \(\mu = 0.4\)** (from **MD**). **Li** configurations **X0–X3** vary **tip concentration** and motifs up to **LiC₃**-like clusters; fracture is tracked via normalized **\(\hat{K}_I = K_I / (2\mu)\)** at the **first C–C bond rupture** (letter **Results**). **Engine / code:** **N/A —** MD package not named on this wiki layer. **Timestep / total trajectory duration:** **N/A —** not stated in the excerpted summary used here; see **article/SI**. **Ensemble during production loading:** **N/A —** beyond the **10 K Berendsen** relaxation description, the letter does not restate thermostat/ensemble labels for the displacement-controlled stage on this page. **Barostat / hydrostatic pressure:** **N/A —** quasi-static **mode I** loading, not **NPT**. **Electric field / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** The letter reports **~3%** agreement between **ReaxFF** and **DFT** for a **hollow-to-hollow Li migration barrier** on monolayer graphene and points to **Supplementary Information** for **functional form and parameters** (**N/A —** full training-set tables not reproduced here).

**3 — Static QM / DFT-only.** **N/A —** **DFT** appears as a **benchmark** for the **Li** migration barrier check, not as the production dynamics engine.

## Findings

**Outcomes & mechanisms.** Under the imposed **stress gradient**, **Li migrates toward the crack tip** and **accumulates**, coupling **bond weakening** with **local hydrostatic stress relaxation** (Virial-stress profiles in the letter). Reported **normalized fracture loads** \(\hat{K}_I\) at first **C–C** rupture are **0.86** (**X0**, pristine tip), **0.75** (**X1**), **0.71** (**X2**), and **0.70** (**X3**, **LiC₃**-like tip), so **chemical weakening** dominates over **stress relaxation** for these tip chemistries. Because **fracture load decreases with Li at the tip** even though **stress relaxation alone would tend to raise** it, the authors conclude **chemical weakening** is the **dominant driver** of **self-weakening** in this model.

**Comparisons.** **ReaxFF** vs **DFT** on a **Li migration barrier** (**~3%** deviation) as a sanity check; **fracture loads** are compared across **X0–X3** configurations.

**Sensitivity & design levers.** **Tip Li concentration / motif** (**X0–X3**) controls \(\hat{K}_I\) trends.

**Limitations & outlook.** Single **atomistic** crack in **graphene**; **anode microstructure** and **electrolyte** complexity lie outside the letter’s scope (**## Limitations**).

**Corpus honesty.** Integration **timestep** and full production schedule are **PDF/SI-grounded**; this page summarizes the **VOR** letter PDF rather than the **proof** sibling **`paper:2013yang-chemical-phy-self-weakening-lithiated`**.

## Limitations

- **Atomistic** models and **finite** simulation times; **real electrodes** involve **microstructure**, **electrolyte**, and **cycling** effects not fully captured in a single cracked-graphene setup.

## Relevance to group

**Adri C. T. van Duin** and **Muralikrishna Raju** (Penn State) coauthor; connects **ReaxFF** to **Li–carbon mechanics** and **battery anode** degradation narratives.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.cplett.2013.01.048` (`papers/Yang_Huang_Zhang_Raju_CPLetters_2013.pdf`).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- [[graphene-nanocarbon]]
