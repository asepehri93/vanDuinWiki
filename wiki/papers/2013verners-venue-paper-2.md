---
id: paper:2013verners-venue-paper-2
type: paper
title: "Molecular dynamics simulation of Al grain mixing in Fe/Ni matrices and its influence on oxidation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
  - scale:atomistic
  - domain:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1063/1.4812387"
year: 2013
authors:
  - "Verners, O."
  - "Shin, Y. K."
  - "van Duin, A. C. T."
venue: "Journal of Applied Physics"
pdf_sha256: "fbdf7986903d464be7451f648bb5a156f58bdc34cb594f78494089348911586c"
pdf_path: "papers/Verners_J_App_Phys_2013.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013verners-venue-paper-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Aluminum-bearing nickel and iron alloys are candidate structural materials for high-temperature oxidizing environments because they can develop protective oxide skins whose kinetics depend on how aluminum reservoirs mix into the metallic matrix. Verners, Shin, and van Duin use ReaxFF molecular dynamics to study aluminum grain embedding in pure nickel and pure iron hosts at roughly one-to-three grain-to-matrix atom ratios, with heating ramps from 300 K to 3000 K at constant pressure followed by cooling back to 300 K. The study is duplicated in corpus coverage with `paper:2013verners-venue-paper` (same science, alternate manifest row) for PDF hash tracking.

## Methods

**1 — MD application (atomistic dynamics).** **ReaxFF** **molecular dynamics** at **constant pressure** with **stepwise** heating from **300 K** to **3000 K** and subsequent **cooling** to **300 K** studies **Al** grains embedded in **pure Ni** or **pure Fe** matrices at ~**1:3** grain:matrix **atom** ratio, varying **Al** grain size (`papers/Verners_J_App_Phys_2013.pdf`; `normalized/extracts/2013verners-venue-paper-2_p1-2.txt` reproduces the **J. Appl. Phys.** abstract header). **Supplementary slab oxidation** exposes **O\(_2\)** to compare **unmixed**, **partially mixed**, and **alloyed** regions. **Engine / code, timestep, thermostat, duration, PBC, and full oxidation protocol:** **N/A —** not in the **p1–2** extract; read **Section II**/**Computational methods** in the PDF. **Barostat / pressure / ensemble:** **constant-pressure** **NPT**-class **MD** is stated in the abstract block; see **`pdf_path`** for thermostat/barostat parameters. **Electric field / enhanced sampling:** **N/A —** not stated in the excerpt.

**2 — Force-field training.** **N/A —** application paper using **ReaxFF** (not a new fit documented on this wiki layer).

**3 — Static QM / DFT-only.** **N/A —** reactive **MD** is central.

## Findings

**Outcomes & mechanisms.** **Ni** hosts yield **lower chemical strain energy** for dissolved **Al** and **complete mixing** at **lower temperature** than **Fe** hosts, consistent with **Al–Ni** being more stable than **Al–Fe** in the model and with experimental trends cited in the abstract. **Grain-size** trends invert between matrices: **larger Al** favors **Fe**, **smaller Al** favors **Ni**, linked to **formation energies** and **metal–metal distances**. **Cooling** produces **chemically disordered crystalline** solids, with **Fe** solidifying at **lower T** than **Ni** for the quoted cooling window and the **Ni** product **less ordered** than **Fe**. **Oxidation slabs:** **unmixed Al** and **unmixed Ni** are most reactive to **oxygen**; **Al/Ni alloy** and **pure Fe** oxidize more slowly under the **preliminary** protocol.

**Comparisons.** Abstract-level alignment with experiment for **Al–Ni** vs **Al–Fe** stability.

**Sensitivity & design levers.** **Host** (**Ni** vs **Fe**), **Al grain size**, and the **thermal cycling** window.

**Limitations & outlook.** Oxidation work is explicitly **preliminary** in the abstract; engineering-scale oxide growth is not claimed resolved.

**Corpus honesty.** Duplicate ingest row vs **`paper:2013verners-venue-paper`** tracks alternate PDFs; this slug uses the **journal article** PDF path rather than the **proof** PDF on the sibling page.

## Limitations

Automated extract coverage spans two pages; figures beyond page two require the full PDF. Duplicate ingest rows exist for workflow hash tracking across PDF variants.

## Relevance to group

Same authorship line (Verners, Shin, van Duin) tying alloy oxidation to ReaxFF applications. The duplicate manifest entry exists only to track alternate PDF hashes for the same scientific content.

## Citations and evidence anchors

- Citation footer: doi `10.1063/1.4812387`, J. Appl. Phys. 114, 023501 (2013) (extract page 1).
- Abstract (extract pages 1–2).

## Related topics

- [[reaxff-family]]
