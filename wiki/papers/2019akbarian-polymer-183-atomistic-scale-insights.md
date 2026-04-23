---
id: paper:2019akbarian-polymer-183-atomistic-scale-insights
type: paper
title: Atomistic-scale insights into the crosslinking of polyethylene induced by peroxides
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:organics-polymers-pyrolysis
- domain:reaxff-lineage
- material:polymer-organic
- method:reaxff
- task:experiment-integrated
- task:validation
- scale:atomistic
candidate_tags: []
source_refs: []
doi: 10.1016/j.polymer.2019.121901
year: 2019
authors:
- Dooman Akbarian
- Hossein Hamedi
- Behzad Damirchi
- Dundar E. Yilmaz
- Katheryn Penrod
- W. H. Hunter Woodward
- Jonathan Moore
- Michael T. Lanagan
- Adri C. T. van Duin
venue: Polymer
pdf_sha256: 5a2f6955f45b24df2928c0caded395bf66985f1ea7ab21a5521178610ede86cf
pdf_path: papers/Akbarian_Polymer_2019.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2019akbarian-polymer-183-atomistic-scale-insights -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF molecular dynamics** is combined with **FTIR mapping** and **wide-angle X-ray scattering (WAXS)** to dissect **peroxide-induced crosslinking** of **polyethylene (PE)**—motivated by **dicumyl peroxide (DCP)** chemistry in **high-voltage cable** **XLPE** insulation. The study reports **non-monotonic** behavior of **crosslink extent** with **curing temperature** (moderate heating to **~500 K** helps; **excessive** temperature can hurt), **density** effects, and **peroxide loading** trade-offs between **byproduct** formation and **XLPE** yield. **Electric field** in the **MD** protocol is found to have **little effect** on crosslinking, and an **alternative peroxide** is argued to be **less efficient** than **DCP** under the modeled conditions. **Adri C. T. van Duin** is a corresponding author with **Penn State** and **Dow** collaborators. The **Polymer** article emphasizes **joint** **simulation**/**metrology** loops so **atomistic** **radical** **pathways** can be checked against **bulk** **spectroscopic** **markers**.

## Methods

- **ReaxFF MD** of **PE + peroxide** mixtures under varied **temperature**, **density**, **stoichiometry**, and optional **field** (see **Polymer** for simulation cells).
- **FTIR** and **WAXS** on **cured** samples to **validate** **structural** and **crosslink** trends.

**MD application (*Polymer* **Methods**).** **Engine / code:** **ReaxFF** in **LAMMPS**. **Ensemble / duration:** **NVT-MD** with **2.25 ns** **equilibration** at each **target** **temperature**, **timestep 0.25 fs**, **Berendsen** **thermostat** (**100 fs** damping). **System & sweeps:** **butane**/**decane** + **DCP**-family **chemistry** across **~300–900 K** (varied **increments**) and **mass** **densities** **0.2–1.0 kg/dm³**; representative **DCP**/**alkane** cells (e.g., **40** **DCP** radicals with **500** **butane** molecules) are shown in the figures. **PBC** **bulk** **supercells** for each state point. **Barostat / pressure:** **N/A —** **NVT** **protocol** quoted here. **Electric field:** the article reports **MD** **tests** where an **external electric field** has **almost no effect** on **crosslinking** relative to the **no-field** cases. **Enhanced sampling:** **N/A —** not used.
## Findings

- **Atomistic** models reproduce **key experimental** trends for **crosslinking** extent and **byproduct** burden across the **processing** window explored.
- **High DCP:PE** can **increase byproducts** without proportionally increasing **XLPE** quality, informing **formulation** choices.

The **non-monotonic** **temperature** trend is interpreted as a **competition** between **radical** **initiation** **efficiency** and **side** **reactions** that **consume** **peroxide** **without** **network** **formation**.

## Limitations

- **Industrial** **XLPE** recipes include **additives** and **multiphase** morphology not fully captured in **idealized** **MD** cells.
- **ReaxFF** for **hydrocarbon + peroxide** chemistry should be **spot-checked** against **QM** when **new** initiators are studied.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

**Industry-facing** **ReaxFF** application to **polyolefin crosslinking** with **experimental** validation—parallel to other **group** **polymer** reactive MD papers.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.polymer.2019.121901` (`papers/Akbarian_Polymer_2019.pdf`).

## Related topics

- [[reaxff-family]]
