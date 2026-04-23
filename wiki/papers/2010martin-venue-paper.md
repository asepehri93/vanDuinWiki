---
id: paper:2010martin-venue-paper
type: paper
title: "Gas-phase lubrication of ta-C by glycerol and hydrogen peroxide: Experimental and computer modeling"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:validation-experiment
  - keyword:graphene-carbon
  - keyword:reactive-md
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - material:polymer-organic
  - method:reaxff
  - task:application
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp909940j"
year: 2010
authors:
  - "Jean-Michel Martin"
  - "Maria-Isabel De Barros Bouchet"
  - "Christine Matta"
  - "Qing Zhang"
  - "William A. Goddard III"
  - "Sachiko Okuda"
  - "Takumaru Sagawa"
venue: "Journal of Physical Chemistry C 114 (11), 5003–5011 (2010)"
pdf_sha256: "d3028a4e651f9f7322d55b091a9ab65cf29345ff319e5ea8bf3ae71bc91aaf85"
pdf_path: "papers/ReaxFF_others/Martin_Zhang_Goddard_DLC_JPC_2010.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2010martin-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose follows the **abstract** and methods introduction in the extract. Material characterization numbers (thickness, sp\(^3\) fraction, etc.) appear in the extract as printed.

## Summary

The study combines **gas-phase lubrication** experiments (**ToF-SIMS**, mass spectrometry) on **hydrogen-free tetrahedral amorphous carbon (ta-C)** with **ReaxFF** sliding simulations to interpret **ultralow friction** at **80 °C** in the presence of **OH-containing** molecules (**deuterated glycerol**, **H\(_2\)O\(_2\)**). Simulations suggest a **sp\(^2\)-rich** surface with some **sp\(^1\)** sites, consistent with prior **EFTEM**; sliding shows **hydroxylation** of surface carbon, **glycerol dissociation**, and **water** formation, aligning with experimental ion signals. Experiments and modeling together argue **surface hydroxylation** and a **water-rich** interfacial film are central to the friction reduction.

## Methods

Experiments use hydrogen-free tetrahedral amorphous carbon (ta-C) coatings deposited by arc-ion plating to about 0.9 µm thickness on steel substrates; characterization in the paper reports high sp\(^3\) fraction (roughly 70–80% from XANES/AES), mass density near 3.43 g cm\(^{-3}\) from EELS relations, hardness \(\sim 65 \pm 15\) GPa and Young’s modulus \(\sim 600 \pm 100\) GPa by nanoindentation, low bulk hydrogen from SIMS, and surface roughness and wetting data as tabulated. Gas-phase lubrication tests at 80 °C in ultrahigh vacuum use a reciprocating tribometer at 345 MPa contact pressure and 1 mm s\(^{-1}\) sliding speed with deuterated glycerol and hydrogen peroxide as reactive feeds; surfaces are analyzed by time-of-flight SIMS and mass spectrometry.

**ReaxFF MD (Section III–IV):** Bulk **ta-C** is generated from a **512-atom** diamond supercell by **melt** (e.g. to **~7722 °C** for **2 ps** in the reported protocol), **quench** to **27 °C** at stated **cooling rates**, then **equilibration** at **27 °C**; a **3.24 g cm\(^{-3}\)** model with **~83% sp\(^3\)**, **~16.6% sp\(^2\)**, and **~0.4% sp\(^1\)** carbon matches the experimental ta-C target used for surfaces. **Sliding** simulations compare **bare** vs **H/OH-terminated** ta-C with **one–four** **glycerol** monolayers as specified in the text, at **reported normal pressures** (e.g. **~0.5–0.85 GPa** in the MD discussion) and **high shear speeds** (e.g. **100 m/s** for a quoted friction coefficient). Trajectory lengths reach **~4–40 ps** in the cases described (e.g. **water** formation tracked after **4–20 ps** of sliding). **N/A —** MD **integration timestep**, **thermostat/barostat**, and **ensemble** keywords are **not recovered** from `normalized/extracts/2010martin-venue-paper_p1-2.txt` (verify **`pdf_path`** for the complete protocol block).

**2 — Force-field training.** **N/A —** this work **applies** ReaxFF to ta-C tribochemistry rather than deriving a new parameterization in the indexed pages.

**3 — Static QM / DFT.** **N/A —** central validation is **experiment + ReaxFF MD** in the excerpted framing.

**Checklist closure (indexed pages).** **Engine / code:** **ReaxFF molecular dynamics** is reported; **N/A — LAMMPS**/**GROMACS**/**CP2K** program name not recovered from `normalized/extracts/2010martin-venue-paper_p1-2.txt` (verify **`pdf_path`**). **Boundaries / periodicity:** **ReaxFF** bulk **melt/quench** uses a **periodic** **512-atom** diamond **supercell** as described in prior curation tied to the PDF; interfacial **sliding** models follow the article’s **PBC** conventions (**N/A —** full cell vectors not reprinted here). **Ensemble:** **N/A — NVT**/**NPT** for each MD stage is not spelled out on pp. 1–2—verify PDF. **Temperature:** experimental **80 °C** tribology plus MD **melt** to **~7722 °C** and **quench/equilibration** at **27 °C** as stated in the wiki Methods sourced from the article.

## Findings

**ReaxFF** sliding models reproduce a **predominantly sp\(^2\)** ta-C surface with **reactive sp\(^1\)** sites, **surface hydroxylation**, **glycerol** **fragmentation**, and **water** formation under shear—patterns that match **ToF-SIMS** / **RGA** signatures from the **gas-phase** tests. **H/OH-terminated** surfaces show **ultralow** modeled **friction coefficients** (**~0.01–0.03**) over **~0.6–2.2 GPa** contact pressures, while **bare** ta-C can reach **\(\mu > 1\)** with heavy **wear** in the simulations. **Glycerol-lubricated** cases yield **\(\mu \approx 0.02\)** at **100 m/s** and **~0.85 GPa** in one reported setup, with **water** produced by **tribochemistry** within **tens of picoseconds** of sliding as illustrated in the figures.

## Limitations

`extraction_quality` is **partial**; quantitative friction traces and full simulation cell parameters are in the full PDF. ReaxFF results depend on the specific carbon oxidation chemistry encoded in the parameterization used in the publication.

## Relevance to group

Shows **ReaxFF** applied to **tribochemistry** on **amorphous carbon** with **experimental** validation—useful cross-reference for carbon/surface reaction workflows.

## Citations and evidence anchors

- DOI: `10.1021/jp909940j`.
- PDF: `papers/ReaxFF_others/Martin_Zhang_Goddard_DLC_JPC_2010.pdf`.
- Extract: `normalized/extracts/2010martin-venue-paper_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
