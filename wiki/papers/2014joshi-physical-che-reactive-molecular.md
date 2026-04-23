---
id: paper:2014joshi-physical-che-reactive-molecular
type: paper
title: "Reactive molecular simulations of protonation of water clusters and depletion of acidity in H-ZSM-5 zeolite"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:zeolite-porous
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:water-interfaces
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1039/c4cp02612h"
year: 2014
authors:
  - "Joshi, Kaushik L."
  - "Psofogiannakis, George"
  - "van Duin, Adri C. T."
  - "Raman, Sumathy"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "90af9ab949bfbcff698115955b782ff7390c263dab3f7149010042b7d4ba4029"
pdf_path: "papers/Joshi_PCCP_2014_Zeolite_protons.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014joshi-physical-che-reactive-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

Reactive MD with refitted Si/Al/O/H ReaxFF parameters probes water adsorption, diffusion, and acid-site chemistry in H-ZSM-5. Refit improves water–zeolite interactions relative to the prior parameter set; simulated water diffusivity matches experiment. Loading- and temperature-dependent water protonation yields growing protonated clusters at higher water content with short-lived cluster identities due to rapid proton hopping—mechanisms that relocate protons among Brønsted sites (abstract; introduction, extract). The scientific context emphasizes **Brønsted** **acidity** in **zeolite** **catalysis** and the difficulty of capturing **hydrated** **proton** **speciation** and **transport** in **confining** **micropores** with either **fixed-charge** force fields or **static** **QM** clusters alone (introduction themes).

## Methods

### Force-field training / scope

- **ReaxFF** parameters for **Si/Al/O/H** are **refit** against **DFT** benchmarks to improve **water–zeolite** and **proton–water** energetics in **H-ZSM-5 (MFI)** relative to an earlier parameterization (abstract).

### Reactive MD sampling

- **Reactive MD (RMD)** explores **water adsorption**, **self-diffusion**, and **Brønsted-site proton transfer** as functions of **water loading** and **temperature** in a **periodic** **MFI** framework (abstract).

### Observables

- Simulations extract **water diffusivity**, **protonation** statistics, **cluster** formation/breakup, and **inter-site proton hopping** pathways (abstract).

### Integration settings

- **Ensemble, timestep, thermostat, and run lengths** are specified in **PCCP** Methods/SI; the short **`_p1–2` extract** does not replace those tables.

### Proof / duplicate PDFs

- Publisher **proof** variants may exist as separate manifest rows; scientific content should be cited from the **version-of-record** PDF when available.

### 1 — MD application (H-ZSM-5 + water)

- **Engine / code:** **Reactive MD (RMD)** with **ReaxFF** as described in **PCCP**; **N/A — explicit “LAMMPS” string not on `normalized/extracts/2014joshi-physical-che-reactive-molecular_p1-2.txt`** (confirm in `papers/Joshi_PCCP_2014_Zeolite_protons.pdf`—ReaxFF studies in this corpus commonly use **LAMMPS**).
- **System / composition:** **Periodic MFI** framework for **H-ZSM-5** with variable **water loading** (**abstract**); **exact atom counts** are **N/A — not on indexed extract p1–2**.
- **Boundaries / periodicity:** **3D PBC** implied by **periodic MFI** framework language in the **abstract**.
- **Ensemble / timestep / duration / thermostat / barostat:** **N/A — numerical integration settings not stated on extract p1–2** (full **PCCP** Methods/SI).
- **Temperature:** **temperature** is an explicit control variable together with **water loading** (**abstract**); **N/A — explicit thermostat law/damping not on extract p1–2**.
- **Pressure / barostat:** **N/A — not stated as NPT-driven** in the abstract-level summary here.
- **Electric field:** **N/A — not indicated** in the abstract/extract opener.
- **Replica / enhanced sampling:** **N/A — umbrella/metadynamics not indicated** in the abstract/extract opener.

### 2 — Force-field training (Si/Al/O/H refit)

- **Parent FF / elements:** **ReaxFF** **Si/Al/O/H** parameters **refit** relative to an earlier parameterization to improve **water–zeolite** and **proton–water** energetics for **H-ZSM-5** (**abstract**).
- **QM reference / training set / optimization:** **DFT** benchmarks underpin the refit; **N/A — functional/basis/k-point lists and optimizer details not on extract p1–2** (article/SI).
- **External reference data:** **Experimental water diffusivity** used as a **comparison** target in the **abstract** narrative.

## Findings

The **refitted** force field yields a **water diffusion coefficient** in **excellent agreement** with **experiment**. **Higher water loading** increases **frequency of water protonation** and growth of **protonated water clusters** in channels; clusters are **short-lived** because **protons and water molecules exchange rapidly** among clusters. **Proton-hopping events** move **protons between distinct Brønsted sites**, depleting localized **acidity** in a loading/temperature-dependent manner, consistent with the abstract’s comparison to prior experimental and theoretical zeolite–water literature (abstract; extract pages 1–2).

**Acidity relocation:** the authors stress that **proton** **mobility** and **cluster** **dynamics** mean **acid strength** is not a fixed **per-site** property under **high** **humidity**—a mechanistic point relevant to **methanol-to-hydrocarbons** and **biomass** **upgrading** in **water-rich** feeds (discussion framing; abstract).

## Limitations

Force-field accuracy remains bounded by the DFT training set; long-time rare-event kinetics may need enhanced sampling beyond standard MD.

**Zeolite** **acid strength** in **operando** conditions may include **extra-framework** **Al** and **defects** beyond the **ideal** **Brønsted** **site** models emphasized here—extend cautiously to **real** **catalysts**.

**Throughput:** **ReaxFF** enables **nanosecond** **windows** at **experimental** **water** **loadings** that are **prohibitive** for **routine** **DFT** **MD**, at the cost of **empirical** **bond-order** uncertainty (discussion trade-off).

## Citations and evidence anchors

- DOI `10.1039/c4cp02612h` (extract header).
- Abstract (extract page 1).

## Related topics

- [[reaxff-family]]
- [[theme-porous-mof-zeolite]]
