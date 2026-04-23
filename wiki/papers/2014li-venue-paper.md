---
id: paper:2014li-venue-paper
type: paper
title: "Fluorination of graphene enhances friction due to increased corrugation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - material:graphene-carbon-nano
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:tribology
  - keyword:graphene-carbon
  - keyword:2d-materials
  - keyword:lammps
  - keyword:reaxff-application
  - keyword:berendsen-thermostat
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/nl502147t"
year: 2014
authors:
  - "Qunyang Li"
  - "Xin-Z. Liu"
  - "Sang-Pil Kim"
  - "Vivek B. Shenoy"
  - "Paul E. Sheehan"
  - "Jeremy T. Robinson"
  - "Robert W. Carpick"
venue: "Nano Lett. (2014); DOI 10.1021/nl502147t"
pdf_sha256: "d86a8c028ae6ebb9beecad9d7c15b4d5caf81b67a1d5930ccf566ff9082f4a05"
pdf_path: "papers/ReaxFF_others/Li_Shenoy_Fluor_graphene_NanoLetters_2014.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2014li-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **peer-reviewed Nano Letters** article identified by `doi` and `pdf_path`. This page is **not** a substitute for the full paper (figures, quantitative friction trends, and simulation details).

## Summary

**FFM** on **patterned CVD graphene** with **XeF\(_2\)** fluorination is combined with **LAMMPS ReaxFF+QEq** sliding simulations (**Pt tip** on **G/FG**). **Fluorination raises nanoscale friction** (several-fold to **~9×** in places) and **disorders stick–slip** on FG versus **ordered** lattice friction on G. The authors attribute the enhancement primarily to **larger interfacial energy corrugation** from **localized charge** at **F** sites (**Prandtl–Tomlinson** picture), not increased **puckering** (Just Accepted PDF).

## Methods

**Experiments:** **CVD graphene** on **Cu**, transferred to **SiO\(_2\)/Si**, patterned with **photoresist**, and **fluorinated** in **XeF\(_2\)** (**60–1200 s**, ~**30 °C**, **1 Torr** XeF\(_2\), **35 Torr** N\(_2\) carrier, pulse mode) so **uncovered** regions become **FG** while resist-protected areas stay **pristine**. After resist strip, **friction force microscopy (FFM)** compares **G vs FG** under **dry N\(_2\)** (**RH < 2%**); **Raman** (**532 nm**) characterizes fluorination. **AFM:** RHK UHV350 and Asylum MFP-3D; **Mikromasch CSC37** Si tips with **Sader**-calibrated stiffness and a **diamagnetic lateral-force calibrator**.

**MD (LAMMPS):** A **hemispherical Pt(111)** asperity (**1,626 atoms**, radius **2.3 nm**) slides on **graphene or FG** supported on a **stepped Pt(181)** substrate (**5,280 atoms**, ~**10 × 6 × 1.2 nm³**) at **10 K**, mimicking **substrate roughness**. **ReaxFF** with **QEq** charge equilibration each step; **Berendsen** thermostat; **Δt = 0.5 fs**; **PBC** in-plane. **Normal load** set by initial **tip–film** height; top **3 tip layers** constrained to slide direction only. A **virtual atom** **40 Å** ahead links through a **spring (K = 80 N/m)** to mimic **lateral compliance**; drag speed **2 m/s**. **Static friction** from **peak lateral force**; **energy corrugation** maps from **tip–sample interaction energy** vs position (**Nano Lett.** Methods; Just Accepted PDF).

### 1 — MD application (tip-on-film sliding)

- **Engine / code:** **LAMMPS** with **ReaxFF** + **QEq** each step (**Methods** above; `papers/ReaxFF_others/Li_Shenoy_Fluor_graphene_NanoLetters_2014.pdf`).
- **System / composition:** **Pt** tip (**1,626** atoms) on **graphene** or **fluorinated graphene** on **Pt(181)** support (**5,280** atoms); **~10 × 6 × 1.2 nm³** cell (**Methods**).
- **Boundaries / periodicity:** **PBC** **in-plane** (**Methods**).
- **Ensemble / thermostat / temperature:** **NVT**-class framing with **Berendsen** thermostat at **10 K** (**Methods**).
- **Timestep:** **0.5 fs** (**Methods**).
- **Duration / stages / equilibration lengths:** **N/A — total trajectory lengths not copied into this wiki note** (Nano Lett. Methods).
- **Barostat / pressure control:** **N/A — not stated as constant-pressure dynamics** in the excerpted Methods above; **normal load** is set geometrically via **tip–film** height (**Methods**).
- **Shear / strain:** **2 m/s** lateral drive via **spring-coupled** virtual atom (**K = 80 N/m**, **40 Å** offset) (**Methods**).
- **Electrostatics:** **QEq** each step (**Methods**); **N/A — cutoffs/precision details not copied here** (full article).
- **Electric field:** **N/A — not indicated** in the excerpted Methods above.
- **Replica / enhanced sampling:** **N/A — not indicated** in the excerpted Methods above.

## Findings

**FFM** shows **μ\(_\text{FG}\)** much larger than **μ\(_\text{G}\)** (e.g. **~6–7×** in a representative boundary scan; monotonic increase with fluorination across samples). **MD** reproduces **greatly increased peak friction** on **FG** and **μ\(_\text{FG}\)/μ\(_\text{G}\) ~7.3–8.0:1** without **increased puckering** of FG (ruling out puckering as the dominant mechanism). **Interaction-energy corrugation** grows strongly with **F content** (e.g. **~12.9 meV** on pristine vs **~206 meV** on a **C\(_8\)F** model at **0 nN** load in one comparison). The authors interpret friction enhancement via **Prandtl–Tomlinson** behavior (**E\(_0\)** vs contact stiffness) and **localized negative charge** on **F** increasing **potential roughness**—consistent with **AFM** trends and prior **hydrogenation** MD (Just Accepted PDF).

## Limitations

The registered PDF is a **“Just Accepted”**–era extract in the corpus; **partial** text extraction. Quantitative comparison to experiment should be taken from the **final typeset article** when available.

## Relevance to group

**Tribology and 2D materials** context; **not** a van Duin-group ReaxFF methods paper—kept as neighboring **graphene functionalization / mechanics** literature.

## Citations and evidence anchors

- https://doi.org/10.1021/nl502147t — Communication title and DOI as in front matter.

## Reader notes (navigation)

- Corpus also registers a second path for the same DOI: `paper:2014nanoletters-venue-paper` (duplicate PDF ingest).

## Related topics

- [[graphene-nanocarbon]]
