---
id: paper:2014srinivasan-carbon-82-20-direction-dependent
type: paper
title: "Direction dependent etching of diamond surfaces by hyperthermal atomic oxygen: a ReaxFF based molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:application
  - task:validation
  - material:graphene-carbon-nano
  - scale:atomistic
source_refs: []
doi: "10.1016/j.carbon.2014.10.076"
year: 2014
authors:
  - "Sriram Goverapet Srinivasan"
  - "Adri C.T. van Duin"
venue: "Carbon 82 (2015) 314–326"
pdf_sha256: "7c0fdcb52e1dc825f335d17a1ecba286ba0507e0958eb0137c9f6fe9cb0ae464"
pdf_path: "papers/Srinivasan_Carbon_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014srinivasan-carbon-82-20-direction-dependent -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Srinivasan and van Duin report **ReaxFF reactive MD** of **hyperthermal atomic oxygen** impacts on **low-index diamond** surfaces, motivated by **low Earth orbit (LEO)**-relevant collision energies (~**5 eV**) and high **O** fluxes (introduction cites representative densities and fluxes). Small **O**-terminated slabs rationalize **oxygenated functional groups** (ethers, peroxides, radicals, dioxetanes) consistent with prior experiment and higher-level modeling. Larger reconstructed surfaces show **anisotropic etching** among **(100), (111), and (110)** with **(110)** fastest and **(100)** slowest in the abstract’s summary, with **erosion yields** described as consistent with experimental trends; an **Arrhenius-type** rate law for **mass loss** is extracted from the simulation campaign. The authors argue **diamond thin films** are promising **spacecraft** surface candidates under LEO-style exposure and position **ReaxFF** as a screening tool for such extreme environments. Definitive numerical diagnostics are in **papers/Srinivasan_Carbon_2014.pdf** and any **SI**.

## Methods

**Force-field training.** **N/A** for a new fit in the indexed abstract/introduction: the **Carbon** article applies an established **ReaxFF** parametrization for **C/O** chemistry suited to **hyperthermal O + diamond** in an **LEO**-motivated setting.

**MD application (hyperthermal O + diamond).** **ReaxFF**-based **reactive molecular dynamics** (implementation details such as **MD** code build and **QEq** update choices in **`papers/Srinivasan_Carbon_2014.pdf`**, **N/A** on this page’s short extract) addresses two protocol classes from the abstract: (i) **small oxygen-terminated diamond slabs** to survey **ethers**, **peroxides**, **oxy radicals**, and **dioxetanes** in qualitative agreement with prior **experiment** and **first-principles** work; (ii) **larger reconstructed** diamond surfaces under **successive** hyperthermal **O** impacts to compare **(100)**, **(111)**, and **(110)** etching. The introduction cites **O(\(^3P\))** number density, **atomic oxygen** fluxes, and an average **collision energy near ~5 eV** as **LEO**-relevant context. **Periodic** (**PBC**) supercells, substrate **temperature**, impact schedule, timestep, **equilibration**/**production** **durations** (**ps**/**ns**), **NVT**/**NVE**/**NPT** staging, thermostat, and **barostat**/**pressure** control (if any) are **N/A** on the **p1–2** extract and must be taken from the full PDF/SI.

**Static QM.** **N/A** as headline production method: **DFT** appears as literature context for oxygenated surface groups; reported chemistry is **ReaxFF MD**.

## Findings

On **small O-terminated slabs**, trajectories populate **C–O** motifs—including **ethers**, **peroxides**, **radicals**, and **dioxetanes**—in qualitative agreement with earlier **experiment** and **first-principles** work (abstract). On **larger reconstructed** surfaces under **successive O** impacts, **(110)** etches fastest and **(100)** slowest among **(100)/(111)/(110)**, with **erosion yields** described as in **good agreement** with **experiment** (abstract). The authors also extract an **Arrhenius-type** law for **mass loss** from the simulation campaign (abstract) and argue **diamond thin films** are promising **spacecraft** surface candidates under **LEO**-like exposure, positioning **ReaxFF** as a **screening** tool for such environments (abstract).

## Limitations

- LEO environments include **ions, VUV, and contamination** not represented in the gas-phase O-beam MD model class.
- Journal volume/year is **2015** while corpus slug uses **2014** receipt metadata; cite using the **DOI** as canonical.

## Relevance to group

**Adri C. T. van Duin** co-authorship; extends **ReaxFF carbon/oxygen** reactive capabilities to **diamond** under **extreme oxidative** fluxes relevant to aerospace materials screening.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1016/j.carbon.2014.10.076](https://doi.org/10.1016/j.carbon.2014.10.076)

## Related topics

- [[reaxff-family]]
