---
id: paper:2014spanjers-physical-che-illuminating-surface
type: paper
title: "Illuminating surface atoms in nanoclusters by differential X-ray absorption spectroscopy"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:methods-software
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:catalysis-surface
  - keyword:metallic-systems
  - keyword:validation-experiment
  - keyword:silica-silicate
candidate_tags: []
source_refs: []
doi: "10.1039/c4cp02146k"
year: 2014
authors:
  - "Charles S. Spanjers"
  - "Thomas P. Senftle"
  - "Adri C. T. van Duin"
  - "Michael J. Janik"
  - "Anatoly I. Frenkel"
  - "Robert M. Rioux"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "cf56905fa03d99d23454153614ece9438c78779dd904b86335cf4559dfa34bf6"
pdf_path: "papers/Spanjer_PCCP_Pd_cluster_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014spanjers-physical-che-illuminating-surface -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Differential EXAFS (D-EXAFS)** tracks **Ar-induced** structural change on **silica-supported Pd** clusters (~**1 nm**). Difference analysis indicates **Pd–Pd** nearest-neighbor distances expand by ~**0.104 Å** upon **Ar** adsorption at **77 K**. **Atomistic MD** supports a picture where **under-coordinated** **Pd** atoms, **kinetically trapped** at **77 K**, **restructure** when **Ar** supplies enough energy to surmount barriers—without a net change in **nearest-neighbor coordination number** at the level discussed. **Senftle**, **Janik**, and **van Duin** contribute **simulation** interpretation alongside **Frenkel**/**Rioux** **spectroscopy**.

## Methods

**Local sources:** the PDF at `papers/Spanjer_PCCP_Pd_cluster_2014.pdf` is present in this workspace; opening sections are captured in `normalized/extracts/2014spanjers-physical-che-illuminating-surface_p1-2.txt`.

**Experiment:** **3% Pd/SiO\(_2\)** catalysts are prepared by **strong electrostatic adsorption (SEA)** from **Pd(NH\(_3\))\(_4\)(NO\(_3\))\(_2\)** onto **Davisil A60** silica at **pH 11**, followed by filtration, drying (**398 K**), and reduction (**438 K**, **4% H\(_2\)/He**, **1 h**). **Pd K-edge XAS** is measured at **APS 10-BM** in transmission; samples are treated in a custom **in situ** cell (ESI), reduced, **He-purged**, cooled to **~77 K**, then measured under flowing **He** (“clean”) and under **Ar + He** (“after Ar adsorption”) at an Ar partial pressure of order **~100 Torr** (stated as yielding roughly **one statistical monolayer** of Ar on silica/Pd based on BET estimates). Data are processed/analyzed with **IFEFFIT** as stated.

**Simulation.** **Classical atomistic molecular dynamics**—with force field, **MD** engine, **NVT**/**NPT** staging as applicable, timestep, **equilibration**/**production** **run** lengths (**ps**/**ns**), thermostat coupling, and **periodic** (**PBC**) treatment documented in **`papers/Spanjer_PCCP_Pd_cluster_2014.pdf`** and the **ESI** (**N/A** for program name and numeric protocol on the indexed **p1–2** extract)—is used to discriminate **surface-restructuring** models consistent with the **D-EXAFS** difference signal for **~1 nm** **SiO\(_2\)**-supported **Pd** clusters containing on the order of **10\(^2\)–10\(^3\)** **atoms** in the published models (**N/A** for exact counts on this page). **Pressure**/**barostat** usage follows whichever ensemble the authors specify for each stage (**N/A** to transcribe numerically here).

**Force-field training.** **N/A**: parameters come from the literature parametrization cited in the article; no new **FF** fit is reported.

**Static QM.** **N/A** as headline production QM: the contribution combines **XAS** with classical **MD** model discrimination.

## Findings

**D-EXAFS** (EXAFS after minus before **Ar**) isolates **surface-weighted** structural change on **~1 nm** **SiO\(_2\)**-supported **Pd**. Difference analysis gives a **first-shell Pd–Pd** expansion of **0.104 ± 0.005 Å** after **Ar** adsorption at **77 K**. **MD** supports a mechanism in which **under-coordinated** **Pd**, **kinetically trapped** at **77 K**, **restructure** when **Ar** provides enough energy to cross restructuring barriers, lengthening **surface Pd–Pd** distances **without** a net change in overall **nearest-neighbor coordination number** at the level discussed—supporting the claim that **D-EXAFS** can **illuminate surface atoms** where conventional **EXAFS** averages bulk and surface. **TEM**, alternative models, and modeling caveats are in the **PCCP** article and **ESI**.

## Limitations

- **Projected** **TEM**-like averaging and **cluster** dispersity affect interpretation; **force field** choices in **MD** bound mechanistic detail.

## Relevance to group

Connects **Penn State** **catalysis**/**spectroscopy** collaboration networks (**Senftle**, **Janik**, **van Duin**) to **operando**-style structure probes for **nanoparticle** catalysts.

## Citations and evidence anchors

- **DOI:** https://doi.org/10.1039/c4cp02146k

## Related topics

- [[reaxff-family]]
