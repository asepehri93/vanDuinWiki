---
id: paper:2014carbon-venue-online-proofing
type: paper
title: "Direction dependent etching of diamond surfaces by hyperthermal atomic oxygen: A ReaxFF based molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
  - domain:methods-software
candidate_tags: []
source_refs: []
doi: ""
year: 2014
authors:
  - "Srinivasan, Sriram Goverapet"
  - "van Duin, Adri C. T."
venue: "Carbon"
pdf_sha256: "97e040a9a5c93ba8edc71afba2c3e54c9121903b5123d6f5a94e5063e27e91c4"
pdf_path: "papers/CARBON_9458_edit_report.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014carbon-venue-online-proofing -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Low-Earth-orbit (LEO)** spacecraft encounter **hyperthermal atomic oxygen (~5 eV flux ~10¹⁵ cm⁻² s⁻¹)** that erodes **carbonaceous** surfaces. The article (Elsevier **online proofing** PDF in corpus) applies **ReaxFF reactive MD** to **hyperthermal O** impacts on **diamond** **low-index** surfaces as a model for **ordered pyrolytic graphite** systems used in experiments. **Small** **oxygen-terminated** slabs characterize **surface groups** (**ethers**, **peroxides**, **radicals**, **dioxetanes**) consistent with **prior** **experiment** and **QM** references. **Larger** **reconstructed** surfaces compare **etching** **yields** across **(100)**, **(111)**, and **(110)**, finding **(100)** **slowest** and **(110)** **fastest**, matching **experimental** **erosion** ordering; the work discusses **Arrhenius-like** **mass-loss** **rate laws** (per abstract/extract). The **introduction** excerpt motivates the need for **fundamental** **chemical-response** models because **polymers** and **carbon composites** are common **spacecraft** **external** materials exposed to **atomic oxygen**. **Orientation-dependent** **etching** emphasized in the **abstract** provides a **clear** **test** of whether **ReaxFF** can recover **anisotropic** **erosion** trends known experimentally for **carbon** **surfaces** under **hyperthermal** **O** **impact**.

## Methods

### Force field and setup (from abstract / introduction extract)

- **Reactive MD:** **ReaxFF** reactive molecular dynamics is used to model **low-index diamond** surfaces exposed to **hyperthermal atomic oxygen** collisions representative of **low Earth orbit (LEO)** conditions (introduction cites **~5 eV** average collision energy and **~10¹⁵ cm⁻² s⁻¹** flux class for atomic oxygen in LEO; exact simulation impact parameters are in the full Methods section of the PDF).
- **Two simulation tracks in the abstract:** (i) **small oxygen-terminated diamond slabs** to survey **surface functional groups** (**ethers**, **peroxides**, **oxy radicals**, **dioxetanes**) and compare with **prior experiments** and **first-principles** references; (ii) **successive oxygen collisions** on **larger reconstructed diamond surfaces** to compare **etching yields** across **(100)**, **(111)**, and **(110)** orientations.
- **Not in the checked-in p1–2 extract:** integration **ensemble**, **timestep**, **thermostat**, and **nonbond cutoffs** for the successive-impact runs—consult the peer-reviewed **Carbon** article for full protocol tables.

### Analysis

- The abstract states simulations are further used to extract an **Arrhenius-type rate law** for **mass loss** from these surfaces under the modeled hyperthermal-oxygen conditions (parameters and temperature ranges in the article).

**1 — MD application (atomistic dynamics).** **Engine / code:** **ReaxFF** **reactive molecular dynamics** as described in the **Carbon** article; integrator package **N/A — not named** on pages 1–2 of `normalized/extracts/2014carbon-venue-online-proofing_p1-2.txt` (`papers/CARBON_9458_edit_report.pdf` is an **Elsevier online proofing** ingest). **Systems:** (i) **small oxygen-terminated diamond slabs** for **surface-group** survey; (ii) **larger reconstructed diamond** slabs under **successive** hyperthermal **O** impacts comparing **(100)**, **(111)**, and **(110)** etching. **Boundaries:** **diamond slab** models with **3D periodic boundary conditions (PBC)** in the surface supercells (abstract framing; exact lattice metrics **PDF-grounded**). **Ensemble / thermostat / timestep / duration:** **N/A — not stated** in the checked-in **p1–2** extract; full **NVT**/**Δt**/**ps**/**ns** production settings are in the **Methods** tables of the **version-of-record** article. **Barostat / bulk pressure:** **N/A —** beam-impact setup rather than a summarized **NPT** hydrostatic protocol here. **Temperature:** **N/A — MD thermostat schedule not in the p1–2 extract** beyond the abstract’s **Arrhenius** discussion context. **Electric field:** **N/A —** not used in the summarized protocol. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training:** **N/A —** applies published **ReaxFF** parameters for **C/O** chemistry (full citation in article), not a new parameterization documented on this proof page.

## Findings

- On **larger reconstructed** surfaces with **successive** hyperthermal **O** impacts, **diamond (100)** shows the **lowest etching rate**, **(110)** the **largest**, and **(111)** is intermediate—an **orientation-dependent** ordering that the abstract reports is in **good agreement** with **experimental erosion** trends for comparable systems.
- **Small** **oxygen-terminated** slab calculations support a **rich** oxygen **surface chemistry** (**ethers**, **peroxides**, **radicals**, **dioxetanes**) consistent with **earlier experiments** and **QM**-based studies cited in the paper.
- The authors use the trajectory data to motivate an **Arrhenius-type** description of **mass-loss** kinetics and argue that **diamond thin films** are **promising** candidate surfaces for **spacecraft** in **LEO**, with **ReaxFF** positioned as a **screening** tool for **materials** in **extreme atomic-oxygen** environments.

## Limitations

**Online proofing** PDF—**DOI** not captured in front matter; obtain from **Carbon** **issue** records when curating bibliography. **Diamond** models **approximate** **graphite** **surface** chemistry; **transferability** to **polymers** requires separate studies. **Successive** **impact** simulations may not capture **steady-state** **erosion** **morphologies** seen after **long** **exposure** in **orbital** tests without **additional** **dose** **accumulation** models. **Obtain** the **Carbon** **DOI** from the **journal** record when **available**—this proof **ingest** omits it in **front matter**.

## Relevance to group

**van Duin**-co-authored **materials-in-extreme-environments** thread aligned with other **LEO** **atomic-oxygen** degradation studies in the corpus. The **diamond** model system connects to **graphitic carbon** literature used as **proxies** for **spacecraft** **thermal protection** materials.

## Citations and evidence anchors

- Title + abstract paragraph beginning “ReaxFF based reactive molecular dynamics…” (Elsevier proof extract); introduction **LEO** **O-flux** context in `normalized/extracts/2014carbon-venue-online-proofing_p1-2.txt`; `papers/CARBON_9458_edit_report.pdf`.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
