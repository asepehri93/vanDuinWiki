---
id: paper:2015yeon-venue-research
type: paper
title: "ReaxFF Molecular Dynamics Simulations of Hydroxylation Kinetics for Amorphous and Nano-Silica Structure, and Its Relations with Atomic Strain Energy"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:reaxff-lineage
  - domain:mechanics-tribology
  - method:reaxff
  - material:silicate-glass
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:silica-silicate
  - keyword:water-interfaces
  - keyword:tribology
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b09784"
year: 2015
authors:
  - "Jejoon Yeon"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "28de23154eb1321f51bf0714a524ec5d995c13d0077a638c6e6130747e188b49"
pdf_path: "papers/Yeon_Silica_hydrolysis_JPCC_2015_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2015yeon-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the article identified by `doi` and `pdf_path`. Local file is a **proof** PDF.

## Summary

The **abstract** reports **ReaxFF molecular dynamics** of **hydrolysis** between **water** and **locally strained SiO₂** motifs, **reoptimizing** the **Fogarty et al. (2010)** silica–water database so **hydroxylation barriers** for **strained** vs **unstrained Si–O** motifs (**~20** vs **~30 kcal/mol** in the abstract) align with **DFT** after optimization. Simulations examine **silanol** formation at **high-strain** regions of a **silica nanorod**, supporting the idea that **water adsorption / hydroxyl formation** favors **higher strain energy** geometries. The authors identify **three hydroxylation pathways**: **H₃O⁺** formation from **adsorbed water**, **proton donation** from **H₃O⁺**, and **direct dissociation** of adsorbed water. Because **water** and **hydrogen-bond networks** respond to **temperature**, **silanol** kinetics are **temperature-dependent**. **Amorphous silica double-slit** models show **silanol** preference at **high-strain** sites, paralleling **nanorod** behavior; behaviors tied to **H₃O⁺** mirror **nanowire**-like simulations. The **abstract** explicitly links results to **tribology**: predicting **where lubricant films attach** on **locally strained silica**.

## Methods

`papers/Yeon_Silica_hydrolysis_JPCC_2015_proof.pdf` is a **proof** PDF with a noisy text layer; prefer the **final JPCC** issue for pagination and any missing labels.

**MD application:** **ReaxFF molecular dynamics** (the proof text does not always resolve the **MD engine** string cleanly—check SI or the published PDF if an explicit code name is required) on a **strained silica nanorod**, an **amorphous silica double-slit**, and related **a-SiO₂** constructs in **3D PBC** **supercells** with explicit **atom** positions and **low-density water vapor** (**0.22 kg dm⁻³**) as stated near the **800 ps** production description. **NVT** segments use **Berendsen** thermostat (**100 fs** damping), **0.1 fs** timestep, and **300–1500 K** in **100 K** steps to survey hydroxylation and hydrogen-bond restructuring. No barostat, controlled pressure, electric field, or enhanced sampling in those **NVT** sweeps.

**Force-field training (SiO-2015):** Starting from **Fogarty et al. (2010) Si/O/H** data, the authors **reoptimize** bond, off-diagonal, angle (**Si–O–Si**, **O–Si–O**, **O–Si–Si**), and **O–H–O** hydrogen-bond terms so **hydroxylation barriers** for **strained vs unstrained Si–O–Si** motifs (**~20 vs ~30 kcal mol⁻¹** before the fit in the abstract) align better with **DFT**.

**Static QM / DFT:** **DFT** enters as **training/validation** for the ReaxFF refit, not as standalone long-timescale AIMD production.

## Findings

After reoptimization, barrier targets for the benchmark **strained vs unstrained** **Si–O** motifs match **DFT** as claimed in the abstract. **Reactive MD** shows **silanol** formation biased to **high-strain** regions on the **nanorod** and in **double-slit** **a-SiO₂**, supporting **strain-promoted hydrolysis**. The abstract distinguishes **three pathways**—**H₃O⁺** formation from adsorbed water, **proton donation** from **H₃O⁺**, and **direct water dissociation**—with kinetics sensitive to **H-bond** topology and **temperature** (**300–1500 K** sweep). Before/after fit curves appear in article figures. Proof text may contain placeholders such as **XXXX** for volume data—cite the **published** issue for stable bibliographic data.

## Limitations

Local file is a **proof** PDF—prefer the **final JPCC** layout for pagination. **ReaxFF** remains **empirical**; rare **reaction channels** may require **QM** validation. **Nanoscale** models may omit **long-wavelength** mechanical coupling present in **macroscopic** contacts.

## Relevance to group

**Penn State** **ReaxFF** work on **silica hydroxylation** and **strain-biased** **water chemistry** underpins **tribochemistry**, **lubrication**, and **surface aging** narratives elsewhere in the corpus; the Fogarty-line **reoptimization** is a concrete **parameter evolution** example for **SiO₂–water** interfaces.

## Citations and evidence anchors

- **DOI:** `10.1021/acs.jpcc.5b09784` — `papers/Yeon_Silica_hydrolysis_JPCC_2015_proof.pdf`; extract `normalized/extracts/2015yeon-venue-research_p1-2.txt` (abstract and introduction).

## Related topics

- [[reaxff-family]]
