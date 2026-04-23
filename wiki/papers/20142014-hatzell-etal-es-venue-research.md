---
id: paper:20142014-hatzell-etal-es-venue-research
type: paper
title: "Effect of strong acid functional groups on electrode rise potential in capacitive mixing by double layer expansion"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:methods-software
  - material:graphene-carbon-nano
  - method:classical-md
  - method:enhanced-sampling
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:water-interfaces
  - keyword:lammps
  - keyword:enhanced-sampling
  - keyword:berendsen-thermostat
  - keyword:reaxff-application
  - keyword:galley-or-proof-pdf
source_refs: []
doi: "10.1021/es5043782"
year: 2014
authors:
  - "Marta C. Hatzell"
  - "Muralikrishna Raju"
  - "Valerie J. Watson"
  - "Andrew G. Stack"
  - "Adri C. T. van Duin"
  - "Bruce E. Logan"
venue: "Environ. Sci. Technol."
pdf_sha256: "cdfae4471ac89b0114a74ec7e5f9db9df0fe3c7996cc88997a5dc5dddddd2c38"
pdf_path: "papers/2014-Hatzell-etal-ES&T-proofs.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20142014-hatzell-etal-es-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. The ingested PDF is a **proofs** file (`2014-Hatzell-etal-ES&T-proofs.pdf`); for pagination and publisher layout, prefer the **version-of-record** when available.

## Summary

The work links **capacitive mixing / double-layer expansion (CDLE)** performance to **surface chemistry** of **activated carbon** electrodes. Experiments on **five** carbons show **electrode rise potential** in **low-concentration** electrolyte **correlates** with **strong-acid** surface group loading (**P** value stated in abstract). **Nitric acid oxidation** of one carbon shifts **rise potential** and **whole-cell** voltage as described in the abstract. **MD** and **metadynamics** on **model carbon** surfaces (**pristine graphene** vs **oxidized / graphene-oxide-like**) interpret **EDL expansion vs compression** in **low salt**, connecting **functional groups** to **sign** of **rise potential**.

## Methods

- **Electrochemistry / materials:** Potentiometric titrations and **CDLE-style rise/fall** tests on **five activated carbons** spanning **strong-acid** loadings from **~0.05 to ~0.36 mmol g⁻¹**; **HNO₃ oxidation** of **YP50** provides a paired before/after case (details in the article).
- **ReaxFF MD (ADF):** **Pristine graphene (PG)** models **low** strong-acid coverage, while **graphene oxide (GO)** structures (from **Bagri et al.**) model **high** coverage (**SI Figure S11**). Slabs are **~43.35 Å × 40.04 Å** in plane with **~16 Å** solution gap; **KCl** solutions (**~2.4 M “HC”** and **~0.9 M “LC”** after ion removal) bracket the CDLE experiment. Parameters follow **Rahaman et al.** for **C/H/O** graphene–water and **Cl/O/H** chloride–water interactions.
- **Integration:** **NPT**, **Δt = 0.25 fs**, **Berendsen** thermostat (**100 fs**) and barostat (**500 fs**); energy minimization to **0.25 kcal Å⁻¹**; **50 ps** equilibration at **300 K**; **HC EDL** from **50 ps** production at **300 K**; **LC EDL** from **100 ps** total (**50 ps** equil + **50 ps** prod). **Well-tempered metadynamics** uses **PLUMED 1.3** via a **LAMMPS fix** (full CVs/collective variables in **SI**).

**1 — MD application (atomistic dynamics).** **Engine / code:** **LAMMPS** with **ReaxFF** and **PLUMED 1.3** for **well-tempered metadynamics** (`papers/2014-Hatzell-etal-ES&T-proofs.pdf`; ingested file is **proofs**—prefer **version-of-record** for pagination). **System:** **PG** vs **GO**-like **carbon** slabs **~43.35 × 40.04 Å** in-plane with **~16 Å** solution region; **KCl** at **~2.4 M** (“HC”) and **~0.9 M** (“LC”) after ion removal (Methods). **Boundaries:** **in-plane PBC** with finite **normal** gap (**slab**, not bulk **3D** liquid). **Ensemble:** **NPT** at **300 K** for equilibration/production segments stated above. **Timestep:** **0.25 fs**. **Duration:** **50 ps** equil + **50 ps** (**HC**) or **50+50 ps** (**LC**) as quoted. **Thermostat / barostat:** **Berendsen**, damping **100 fs** (**T**), **500 fs** (**P**). **Temperature:** **300 K**. **Pressure:** controlled via **NPT** barostat as above (proofs text). **Electric field:** **N/A —** not part of the summarized **EDL** protocol. **Replica / enhanced sampling:** **well-tempered metadynamics** (**PLUMED**); collective variables in **SI**.

**2 — Force-field training:** **N/A —** parameters follow **Rahaman et al.** (**C/H/O** graphene–water) plus **Cl/O/H** chloride–water interactions as cited—this work applies them to **EDL** structure, not a new **ReaxFF** fit.

## Findings

- Across carbons, **electrode rise potential in LC** correlates with **strong-acid group concentration** at **P = 10⁻⁵**; **low-acid** electrodes show **positive** rises (e.g., **59 ± 4 mV** at **~0.05 mmol g⁻¹**), whereas **high-acid** carbons trend **negative** (e.g., **−31 ± 5 mV** at **~0.36 mmol g⁻¹**).
- **Nitric acid oxidation** of **YP50** shifts the **rise potential** from **46 ± 2 mV** to **−6 ± 0.5 mV** and yields a **whole-cell** mixing potential of **53 ± 1.7 mV**, about **4.4×** the **12 ± 1 mV** obtained with **symmetric** electrodes in their comparison.
- **ReaxFF MD + metadynamics** link **PG** surfaces to **EDL expansion** in **LC** (positive-rise trend) and **GO** surfaces to **EDL compression** (negative-rise trend), matching the **functional-group** narrative of the experiments.

## Limitations

- **Model** surfaces vs **real** activated carbons; **proof** PDF may differ cosmetically from **final** ES&T layout.

## Relevance to group

**Muralikrishna Raju** and **Adri C. T. van Duin** (Penn State) coauthor; combines **carbon electrochemistry** with **atomistic** **EDL** interpretation for **energy** from **salinity gradients**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/es5043782` (`papers/2014-Hatzell-etal-ES&T-proofs.pdf`).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
