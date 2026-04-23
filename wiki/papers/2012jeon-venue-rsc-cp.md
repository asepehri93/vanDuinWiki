---
id: paper:2012jeon-venue-rsc-cp
type: paper
title: "Nanoscale oxidation and complex oxide growth on single crystal iron surfaces and external electric field effects"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:oxides-ceramics, domain:alloys-metallurgy, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1039/c2cp43490c"
year: 2012
authors: ["Jeon, Byoung Seon", "Van Overmeere, Quentin", "van Duin, Adri C. T.", "Ramanathan, Shriram"]
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "a640cbe9ae6642389a8d87ae02dcb44eec0e913f3d744875508cceb612143ba6"
pdf_path: "papers/Jeon_PCCP_2012_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2012jeon-venue-rsc-cp -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Corpus note:** this slug points at the **galley / proof PDF** (`papers/Jeon_PCCP_2012_galley.pdf`). The **same PCCP article** is fully curated on **`[[2012jeon-venue-rsc-cp-2]]`** using the **final article PDF** (`papers/Jeon_PCCP_Iron_Efield_2013.pdf`). The study applies **ReaxFF reactive MD** to **early-stage oxidation** and **nanoscale oxide growth** on **Fe(100), Fe(110), and Fe(111)** with and without an **external electric field (~10 MV/cm)**. At **300 K** over **~1 ns**, oxidation rates order roughly **(110) > (111) > (100)**; raising temperature accelerates oxidation. The mechanism discussion highlights **oxygen interstitial transport** forming **non-stoichiometric wüstite-like** regions that evolve toward more stoichiometric **wüstite/hematite**-like films as oxygen uptake proceeds, with increasing **cation outward transport**. Post-growth **relaxation** between **600–1500 K** yields **Arrhenius** estimates for **oxygen diffusion activation energies** near **0.32, 0.26, and 0.28 eV** on **(100), (110), (111)** respectively. The field **accelerates early oxidation** via interstitial oxygen transport but the oxide approaches a **self-limiting thickness**; effects on **barriers** are modest while **cation outward migration** is slightly promoted.

## Methods

**Corpus / PDF role:** This slug points to a **galley/proof PDF** (`papers/Jeon_PCCP_2012_galley.pdf`). For **version-of-record** **protocol** detail (**supercell sizes**, **1 fs** integration to **1 ns**, **10 MV/cm** field implementation, **Arrhenius** **O diffusion** post-processing), use **`[[2012jeon-venue-rsc-cp-2]]`** and **`papers/Jeon_PCCP_Iron_Efield_2013.pdf`**.

### 1 — MD application (atomistic dynamics) (high level; verify VOR)

At the article level (as summarized on **`[[2012jeon-venue-rsc-cp-2]]`**): **ReaxFF** simulations study **dry O₂-driven oxidation** on **Fe(100)**, **Fe(110)**, and **Fe(111)** with **controlled O₂ insertion**, including runs at **300 K** and **900 K**, and optional **~10 MV/cm** **normal electric fields** at **300 K** implemented via **charge–field coupling** in the **ReaxFF** energy/force framework (Eqs. (6)–(9) on the VOR page).

- **Engine / code:** **ReaxFF** **reactive MD**; **N/A —** MD engine not confirmed from this **galley** file in this KB pass—see VOR page.
- **System size & composition:** **N/A —** exact **Fe** slab atom counts not duplicated here—see **`[[2012jeon-venue-rsc-cp-2]]`**.
- **Boundaries / periodicity:** **PBC** **slab** models with vacuum padding along the surface normal are used on the VOR page; **N/A —** explicit box vectors not copied here from the galley PDF.
- **Ensemble:** **NVT** (VOR page).
- **Timestep:** **1 fs** (VOR page).
- **Duration / stages:** **~1 ns** oxidation segment plus shorter reference relaxations on the VOR page; **N/A —** not re-verified against the galley PDF bytes here.
- **Thermostat / barostat:** **N/A —** thermostat/barostat algorithm naming not copied here—see VOR **`pdf_path`**.
- **Temperature:** **300 K** and **900 K** campaigns (VOR summary).
- **Pressure / stress:** **N/A — hydrostatic pressure** control not emphasized in the VOR summary copied here.
- **Electric field:** **~10 MV/cm** normal field cases at **300 K** (VOR summary).
- **Replica / enhanced sampling:** **N/A —** not used (VOR summary).

### 2 — Force-field training

**N/A —** application/follow-up analysis of an **Fe–O** **ReaxFF** description; see VOR for parameter lineage citations.

### 3 — Static QM / DFT-only

**N/A —** not the paper type.

## Findings

**Same scientific conclusions** as **`[[2012jeon-venue-rsc-cp-2]]`**: **facet-dependent** oxidation kinetics, **two-stage** growth (**fast** **O** **interstitial** ingress then **slowing**/ **saturation**), **non-stoichiometric** early oxide, **Arrhenius** **O** **diffusion** barriers **~0.32/0.26/0.28 eV** (**no field**) and **~0.33/0.24/0.23 eV** (**10 MV/cm**), and **field** effects strongest in **early** stages.

- **Retrieval note:** cite figures/tables from the **final** PDF on **`[[2012jeon-venue-rsc-cp-2]]`**; keep this page for **duplicate-PDF** provenance only.

## Limitations

Prefer **`[[2012jeon-venue-rsc-cp-2]]`** for figure references and any post-proof corrections; this galley file exists for **corpus provenance** tracking.

## Relevance to group

Canonical technical narrative: **`[[2012jeon-venue-rsc-cp-2]]`**. Operators maintaining the graph should prefer linking simulation details (timestep, supercell vectors, field implementation) from the **version-of-record** page to avoid duplicating numbers that may differ between **galley** and **final** PDFs.

## Citations and evidence anchors

- **DOI:** 10.1039/c2cp43490c — **Phys. Chem. Chem. Phys., 2013, 15, 1821–1830** (final pagination on VOR PDF).

## Related topics

- [[reaxff-family]]
- [[2012jeon-venue-rsc-cp-2]]
