---
id: paper:2025hamdy-arkoub-acs-surface-orientation-dependent
type: paper
title: "Surface Orientation-Dependent Corrosion Behavior of NiCr Alloys in Molten FLiNaK Salt"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:reactive-md
  - domain:oxides-ceramics
  - material:alloy-bulk
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:metallic-systems
  - keyword:validation-experiment
doi: "10.1021/acsami.5c06557"
year: 2025
authors:
  - "Hamdy Arkoub"
  - "Daniel Flynn"
  - "Adri C. T. van Duin"
  - "Miaomiao Jin"
venue: "ACS Appl. Mater. Interfaces 2025, 17, 38708–38719"
pdf_sha256: "cb2cd1b9e9bc1c90a08343341ebf84cb97870484426891e839f7e9a6eaad830f"
pdf_path: "papers/Arkoub-et-al-2025-surface-orientation-dependent-corrosion-behavior-of-nicr-alloys-in-molten-flinak-salt.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025hamdy-arkoub-acs-surface-orientation-dependent -->

## Summary

Molten **fluoride salts** such as **FLiNaK** are discussed widely for **thermal energy storage** and **nuclear** heat-transfer applications, but structural alloys can suffer **corrosion** that depends on **temperature**, **salt chemistry**, and **interfacial** transport. This **ACS Appl. Mater. Interfaces** article uses **ReaxFF-based reactive molecular dynamics (RMD)** to study **molten FLiNaK** attack on **Ni\(_{0.75}\)Cr\(_{0.25}\)** as a function of **surface orientation**, **temperature**, and **uniform electric fields** normal to the interface—motivated by the idea that corrosion is not always isotropic even when bulk alloy composition is fixed. The abstract frames the problem around **Cr dissolution** and **near-surface diffusion** leading to **pitting-like** roughening, and it highlights **orientation-dependent** susceptibility and **field-dependent** suppression or acceleration of attack. **Adri C. T. van Duin** coauthors the study as part of the group’s **molten-salt / alloy interface** simulation portfolio.

## Methods

The simulations employ **ReaxFF** reactive MD with parameters consistent with prior **Ni–Cr–F/K/Li** training discussed in the article (see Methods/SI for the precise parameter line and validation hooks). The authors compare **(100)**, **(110)**, and **(111)** surface terminations of **Ni\(_{0.75}\)Cr\(_{0.25}\)** in contact with **molten FLiNaK** over a **temperature** range **600–800 °C** (reported in **°C**; convert to **K** when comparing to other MD literature), including runs **with and without** uniform **electric fields** perpendicular to the interface reported as **+0.10 V Å\(^{-1}\)** and **−0.10 V Å\(^{-1}\)** in the abstract-level summary. Structural evolution is interpreted in terms of **dissolution**, **diffusion**, and **morphological roughening** metrics described in the full text; local extract `normalized/extracts/2025hamdy-arkoub-acs-surface-orientation-dependent_p1-2.txt` aligns with the title-page framing. **N/A** in this short summary: **time step**, **trajectory** **duration**, **thermostat** type and **damping**, **barostat** (if any), full **PBC** **slab** **supercell** **atom** counts, and full **NPT** vs **NVT** **ensemble** labelling—see **version-of-record** **PDF**/**SI** (the **melt** on **faceted** **Ni–Cr** **slabs** is treated with **3D** **PBC** in the standard **LAMMPS** **slab** pattern described there). **Replica** / **metadynamics**-class **sampling:** **N/A** — not part of the abstract-level description.

## Findings

The abstract reports that **Cr dissolution** and **near-surface diffusion** drive **pitting-like** roughening, with a clear **orientation ranking**: **(110)** is the **most corrosion-prone**, while **(100)** and **(111)** are comparatively more resistant, and **(111)** is described as the **most stable** among the facets compared. **Arrhenius** analysis yields **activation energies** in the **0.27–0.41 eV** range, described as consistent with **limited experiments** but **much smaller** than **bulk diffusion** barriers—interpreted as evidence for **near-surface kinetic control** rather than bulk-diffusion limitation of the simulated process. Regarding **electric fields**, a **positive** normal field is reported to **promote Cr dissolution**, whereas a **negative** field **strongly suppresses** corrosion, suggesting a possible **mitigation** lever for interfacial engineering under polarized conditions. Full numerical protocol details (timestep, sizes, equilibration) should be confirmed in the article and SI beyond the p1–2 extract. The orientation-dependent ranking is especially relevant for interpreting **polycrystalline** alloy exposures where multiple facets present simultaneously: simulations provide a **facet-resolved** hypothesis that can be tested against **post-mortem** microscopy and **depth profiles** where available. Finally, the reported **field** response should be read as a qualitative lever for interfacial driving forces in molten salts, not a literal reproduction of full electrochemical cell polarization without explicit **electrode** chemistry. **Corpus** note: numbers above follow the **abstract** and **p1–2** **extract**; the **PDF** is authoritative for **cutoffs**, **sample** **statistics**, and **SI** detail.

## Limitations

Field magnitudes and boundary conditions are idealizations of complex electrochemical environments; long-time extrapolation from nanoscale MD requires experimental corroboration.

## Relevance to group

**van Duin**-group **ReaxFF** for **molten-salt** corrosion on **alloys** relevant to high-temperature energy systems.

## Citations and evidence anchors

https://doi.org/10.1021/acsami.5c06557 — *ACS Appl. Mater. Interfaces* **17**, 38708–38719 (2025).

## Reader notes (navigation)

- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
