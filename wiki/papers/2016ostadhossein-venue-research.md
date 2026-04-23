---
id: paper:2016ostadhossein-venue-research
type: paper
title: "Atomic insight into the lithium storage and diffusion mechanism of SiO2/Al2O3 electrodes of lithium ion batteries: ReaxFF reactive force field modeling"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:reaxff
  - method:monte-carlo
  - material:oxide
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:batteries-interfaces
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.5b11908"
year: 2016
authors:
  - "Alireza Ostadhossein"
  - "Sung-Yup Kim"
  - "Ekin D. Cubuk"
  - "Yue Qi"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. A (proof PDF in corpus)"
pdf_sha256: "465cc870e793e43005c7d04ad842accdcdf84f30e7eb8c88bbefe92a210c80d4"
pdf_path: "papers/Ostadhossein_JPC_2016_LiSiO_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016ostadhossein-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    This slug registers a **publisher proof** PDF for **J. Phys. Chem. A** (**DOI** in front matter). Narrative content matches **`[[2016ostadhossein-venue-jp-2015-119086]]`**; prefer the **version-of-record** PDF for citation unless you are documenting proof-specific layout.

## Summary

The article develops a **ReaxFF** parametrization for **Li–Si–O–Al** chemistry to describe **lithium** insertion, reaction, and transport in **silica** and **alumina** environments relevant to **oxide-coated silicon** anodes in **lithium-ion batteries**. The scientific goal is **atomistic** insight into how **ALD**-style **oxide** coatings can modify **lithiation** stress and **interfacial** chemistry compared with bare **Si**, including **diffusion** anisotropy in **crystalline** silica and transferability toward **amorphous** silica representations.

The work combines **hybrid GCMC + MD** (as summarized on related pages) to insert **Li** and study subsequent **dynamics**, reporting **diffusion** behavior and **thermodynamic** driving forces for **lithiation** in model **oxide** phases. Discussion ties **oxide** coatings to **volume buffering**, **SEI**-adjacent chemistry, and mechanical protection motifs discussed in **LIB** **anode** engineering.

## Methods

This slug registers a **publisher proof** PDF for the same *J. Phys. Chem. A* article as [[2016ostadhossein-venue-jp-2015-119086]] (DOI `10.1021/acs.jpca.5b11908`). The scientific protocol matches the version-of-record page: ReaxFF reparameterization for Li–Si–O–Al from DFT data on clusters, surfaces, and condensed phases; hybrid GCMC + MD to change lithium loading in crystalline and amorphous silica; **NVT**/**NPT** segments for diffusivity (including anisotropic crystalline channels); and larger cells with alumina-bearing regions for coating–silicon coupling. The MD workflow mirrors the issue article: **periodic** supercells with **PBC**, hybrid **GCMC**/**MD** lithium insertion, **300 K** diagnostics such as **250 ps** **NVT** RDF sampling, **NPT** densification at **P = 0**, **1 ns** melt–quench preparation of glassy silica, and **NEMD** tensile tests on **3000-atom** cells—see [[2016ostadhossein-venue-jp-2015-119086]] for the same numerical narrative. **N/A — MD engine name in this proof-PDF text** — treat **LAMMPS**/package choices as on the version-of-record page. **N/A — explicit fs timestep and thermostat coupling constants in this proof-PDF text layer** — copy integrator and **thermostat** settings from the issue **PDF**/SI when reproducing. **N/A — applied electric field; umbrella / metadynamics / replica exchange** as the primary workflow. DFT supports parametrization rather than replacing large-cell reactive dynamics.
## Findings

The fitted field is reported to reproduce **DFT-level** trends for **Li** site preferences and **migration** behavior in **silica**, including **anisotropic** diffusion in **crystalline** channels versus more **isotropic** hopping in **disordered** **amorphous** matrices, and to support discussion of how **oxide** coatings can **throttle** or **redirect** **Li** flux toward the **Si** active material. **Interface** models illustrate **stress** pathways during **lithiation** cycles. For **numerical** **diffusivities**, **insertion** isotherms, and **barrier** values, cite figures/tables on **`[[2016ostadhossein-venue-jp-2015-119086]]`**; this proof-ingest page does not duplicate those values.

## Limitations

**Proof PDFs** can differ slightly from final **pagination**. Real **ALD** microstructures are reduced to tractable **oxide** **slab**/**cluster** models; **electrolyte** and **electrochemical polarization** are not fully represented at the **ReaxFF** level used here.

When using this page for **battery** retrieval, pair it with **`[[2016ostadhossein-venue-jp-2015-119086]]`** for any claim about **numerical** **diffusivities** or **insertion** **isotherms**: this slug’s purpose is **manifest provenance** for the **proof** PDF bytes, while the canonical narrative should remain **one** authoritative page unless the wiki later **deduplicates** intentionally.

## Relevance to group

**van Duin-group** contribution on **ReaxFF** for **LIB** **oxide** coatings; this slug records **manifest provenance** for the **proof** file.

From a **knowledge-base** maintenance perspective, keep **diffusion** tensors, **insertion** isotherms, and **reaction** statements synchronized with the **VOR** page so **chunk** text does not diverge across duplicate **PDF** registrations.

## Citations and evidence anchors

- DOI [10.1021/acs.jpca.5b11908](https://doi.org/10.1021/acs.jpca.5b11908).

## Reader notes (navigation)

- Canonical wiki page: [[2016ostadhossein-venue-jp-2015-119086]].

## MAS / retrieval

Treat this entry as **manifest-linked** **duplicate provenance**: it exists so `pdf_path`/`pdf_sha256` in `normalized/` and chunk pipelines can point at the **proof** bytes without losing the **scientific** narrative on the **VOR** page.

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
