---
id: paper:2018lotfi-venue-research
type: paper
title: "Molecular dynamics simulations of perfluoropolyether lubricant degradation in the presence of oxygen, water, and oxide nanoparticles using a ReaxFF reactive force field"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:organics-polymers-pyrolysis
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - material:oxide
  - material:polymer-organic
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.7b09660"
year: 2018
authors:
  - "Roghayyeh Lotfi"
  - "Adri C. T. van Duin"
  - "Mousumi Mani Biswas"
venue: "J. Phys. Chem. C"
pdf_sha256: "4d9add9bb494ff97e3c8d1dd7678bc66bc7708db8cf1bd2d6c24abc55f3cddb1"
pdf_path: "papers/Lotfi_JPC_C_2018_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018lotfi-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF MD** at **high temperature** is used to study **degradation** of a **Demnum-class PFPE lubricant (D4OH)** in **hard-disk-drive–relevant** environments containing **O₂**, **H₂O**, and **oxide nanoparticles** (**SiO₂**, **goethite**, **Fe₂O₃**) with several **pretreatment states** (untreated vs **dry/wet air** exposure). The simulations emphasize that **water** strongly **accelerates** strand **scission chemistry**, while **O₂** plays a comparatively **minor** role under the modeled conditions, and that **nanoparticles** generally **catalyze / accelerate** degradation—with **material-specific** rankings across **oxide** types and **pretreatments**. **Adri C. T. van Duin** is corresponding-group coauthor with **Lotfi** and **Biswas** (Western Digital affiliation on the experimental/industry side).

## Methods

**Force field.** **ReaxFF** covers **PFPE** **C/F/O** chemistry together with gas-phase **O\(_2\)**, **H\(_2\)O**, and **oxide nanoparticle** surfaces (**SiO\(_2\)**, **goethite**, **Fe\(_2\)O\(_3\)**) as enumerated in *J. Phys. Chem. C* (`papers/Lotfi_JPC_C_2018_proof.pdf` is an **ACS proof**; reconcile tables and figure callouts with the version-of-record when citing numbers).

**Reactive MD (degradation cells).** **LAMMPS** **ReaxFF MD** of **multi-strand Demnum-class D4OH** lubricant places explicit **O\(_2\)**, **H\(_2\)O**, and **nanoparticle** contacts in periodic **supercells** (**atom** totals in **Methods**/figures). **Pretreatment:** **nanoparticles** see **dry** vs **wet** **air** exposure before **thermal degradation** runs to vary **surface hydroxylation** / adsorption. **PBC:** **three-dimensional PBC** for bulk reactive cells (**N/A — any frozen boundary layers** per **Methods** if used). **Ensemble:** **NVT**/**NVE**-style thermalized **reactive** sampling for the high-temperature **degradation** windows (exact label per stage in **Methods**). **Thermostat / barostat / timestep:** **N/A — not transcribed** from this proof-ingest note—import from the **VOR** PDF after DOI reconciliation. **Duration / stages:** **nanosecond**-scale **production** segments at **1500 K** (abstract) with preceding **equilibration** in **Methods** (exact **ps/ns** in **PDF**); **1500 K** is a **kinetic accelerator**, not an HDD operating temperature. **Pressure:** **N/A — not highlighted** in the abstract-level summary used here. **Electric field:** **N/A — not used**. **Enhanced sampling:** **N/A — not indicated** for this degradation study.

**Analysis.** **Fragmentation** products and **relative degradation** rates are compared across **oxide** types and **pretreatments** using the article’s **figures** and **tables**.

**Experiments / context.** **Industrial** motivation appears via coauthor affiliations; **primary** evidence summarized here is **computational**—confirm any laboratory claims in the full article.
## Findings

**Outcomes.** **Water** is the **dominant accelerant** among the small-molecule oxidants treated in the abstract-level comparison. **Nanoparticle pretreatment** (dry vs wet **air** exposure) shifts **surface hydroxylation / adsorption** and modulates **degradation** rankings across **SiO\(_2\)**, **goethite**, and **Fe\(_2\)O\(_3\)**. **O\(_2\)**-only environments give comparatively **minor acceleration** vs **H\(_2\)O**-containing cases.

**Comparisons / sensitivity.** The study contrasts **oxide** identity and **pretreatment** state under the shared **high-T** MD protocol (**1500 K** in the abstract).

**Limitations / outlook.** **Proof PDF** path (`papers/Lotfi_JPC_C_2018_proof.pdf`); confirm final figure numbering against the **VOR** before citing tabulated rates.

**Corpus honesty.** This slug tracks an **ACS proof** ingest for DOI **10.1021/acs.jpcc.7b09660**; detailed fragmentation statistics should be anchored to the **published** article PDF where it diverges from proof layout.
## Limitations

- **Elevated temperature** is a **kinetic accelerator**, not a direct **operating temperature** of devices; extrapolation requires **care**.
- **PFPE chemistry** is complex; **quantitative** product distributions may be **force-field sensitive**.
- **Catalyst** **metals**, **lubricant** **additives**, and **laser-assisted** **heating** in **real** **HDD** **tests** introduce **degradation** **channels** beyond **O\(_2\)**/**H\(_2\)O**/**oxide** **NP** scenarios in the **simulation** **matrix**.
- **Tribocharging**, **meniscus** **films**, and **shear** **rates** at **head–disk** **contacts** couple **mechanochemistry** to **thermal** **hotspots** in ways not fully represented by **isothermal** **bulk** **ReaxFF** **cells**.
- **FEP**/**Zdol**-class **PFPE** **blends** used in **some** **HDD** **formulations** may show **branching** **scission** not captured by **single** **D4OH** **strand** **models**.

## Relevance to group

Illustrates **ReaxFF** applied to **tribology / storage** lubricant **pyrolysis-like** chemistry with **industrial coauthorship**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpcc.7b09660` (printed on the **ACS proof** PDF `papers/Lotfi_JPC_C_2018_proof.pdf`).

## Related topics

- [[reaxff-family]]
