---
id: paper:2013zhang-fuel-uncorre-effect-supercritical
type: paper
title: "The effect of supercritical water on coal pyrolysis and hydrogen production: A combined ReaxFF and DFT study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:dft-static
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:thermal-decomposition
  - keyword:reactive-md
source_refs: []
doi: "10.1016/j.fuel.2013.01.064"
year: 2013
authors:
  - "Jinli Zhang"
  - "Xiaoxia Weng"
  - "You Han"
  - "Wei Li"
  - "Jingyao Cheng"
  - "Zhongxue Gan"
  - "Junjie Gu"
venue: "Fuel"
pdf_sha256: "1c1fe0b69b499508843f75d51d23f013fa3d3c078f7f1a7892cd964bfdafeb50"
pdf_path: "papers/ReaxFF_others/Zhang_Weng_supercriticalH2O_coal_Fuel2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013zhang-fuel-uncorre-effect-supercritical -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. Energies and mechanistic steps (e.g., kJ/mol values in the abstract) must be verified in the article.

## Summary

**ReaxFF MD** combined with **DFT** is used to study **coal pyrolysis** and **H₂ formation** in **supercritical water (SCW)**. The abstract argues that **water clusters** in SCW **weaken C–C bonds** in **aromatic** moieties, lowering **ring–ring** cleavage barriers relative to **dry** or **vapor** pyrolysis references (numerical values are given in the paper). Further steps describe **ring opening**, formation of **H-rich water clusters** after **OH** transfer, and **catalytic** roles of water in **H₂** and **OH** production, framed as a **cooperative** SCW–coal loop that **accelerates gasification** and **raises H₂ yield**.

## Methods

### Reactive MD (ReaxFF)

- **ReaxFF MD** simulations target **coal pyrolysis** and **hydrogen production** in **supercritical water (SCW)** using reactive force-field chemistry at atomistic resolution (abstract). The abstract frames **water clusters** in SCW as actors that **weaken C–C bonds** in **aromatic** units during **ring–ring** cleavage sequences.
- **Engine, timestep, thermostat, total trajectory length, and nonbond cutoffs** for the production ReaxFF runs are **not stated** in the checked-in **`_p1–2` extract**—consult the **Fuel** article **Computational methods** section for those settings.

### Static QM / cluster benchmarks (DFT)

- **DFT** complements ReaxFF by quantifying how **water-cluster** interactions change **C(ring)–C(ring)** **bond cracking energies** relative to **dry pyrolysis** and **water-vapor** pyrolysis reference paths (numerical shifts quoted in the abstract). **Functional, basis set, and cluster models** appear in the article text—not in the short corpus extract.

### Analysis

- Mechanistic interpretation in the abstract emphasizes **sequential ring opening** of **small cyclic** fragments, **OH transfer** events that produce **H-radical-rich water clusters**, and subsequent **H₂ / OH** release pathways feeding a **cooperative SCW–coal** loop.

**1 — MD application (atomistic dynamics).** **Engine / code:** **Reactive MD** with **ReaxFF**; software **N/A — not named** in `normalized/extracts/2013zhang-fuel-uncorre-effect-supercritical_p1-2.txt` (see **Fuel** PDF). **System:** atomistic **coal** with **supercritical water** as defined in **Computational methods** (**N/A — cell stoichiometry and atom counts not in the p1–2 extract**). **Boundaries:** **N/A — explicit PBC flags and box vectors not in the p1–2 extract** (confirm in PDF). **Ensemble / thermostat / barostat / timestep / trajectory length:** **N/A — not stated** in the p1–2 extract beyond “supercritical” framing—use the article for **NVT/NPT**, coupling constants, **Δt**, and production trajectory lengths in **ps** or **ns**. **Temperature / pressure (SCW):** **N/A — numerical T and P for the MD cells not in the p1–2 extract**; the abstract establishes **SCW** as the environment. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training:** **N/A —** combined **ReaxFF + DFT** study applies existing reactive parameters; any **QM level** for cluster benchmarks is in the article text, not the short extract.

**3 — Static QM / DFT-only (supporting block).** **DFT** cluster calculations support how **water-cluster** environments shift **C(ring)–C(ring)** cleavage energetics versus **dry** and **water-vapor** references (abstract); **functional / basis / k-mesh** details **N/A here — see Fuel article** beyond what this wiki quotes from the abstract.

## Findings

- The authors report that **water clusters in SCW weaken aromatic C–C bonds**, reducing **C(ring)–C(ring)** cleavage energies by up to **~287.3 kJ/mol** relative to **dry coal pyrolysis** and by **~94.6 kJ/mol** relative to **pyrolysis in water vapor**, for the representative cases highlighted in the abstract.
- After **rings fragment** into **small cycles** (e.g., **quaternary/ternary** rings in their description), **SCW clusters** continue to **open** those units; **water clusters** can convert into **H-radical-rich** clusters after **donating OH** to cyclic fragments, providing a major **H₂** source in their mechanism.
- **H radicals** from coal can also **combine with SCW clusters**, feeding the same **H-rich cluster** pool; catalyzed decomposition of these clusters yields **H₂** and **OH**, and **OH** further **attacks coal intermediates**, closing a **cooperative SCW–coal loop** that accelerates **gasification** and **H₂ yield** in the narrative of the paper.

## Limitations

- **Model** coal chemistry and **simulation** conditions; **industrial** gasification involves **minerals**, **pressure**, and **flow** not fully captured.

## Relevance to group

Illustrates **ReaxFF + DFT** workflows for **high-T** **hydrocarbon** chemistry in **water**, relevant to **fuel** and **gasification** simulation culture in reactive MD.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.fuel.2013.01.064` (`papers/ReaxFF_others/Zhang_Weng_supercriticalH2O_coal_Fuel2013.pdf`).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
