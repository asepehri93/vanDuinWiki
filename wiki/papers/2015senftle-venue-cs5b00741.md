---
id: paper:2015senftle-venue-cs5b00741
type: paper
title: "Role of Site Stability in Methane Activation on PdxCe1−xOδ Surfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:oxides-ceramics
  - method:dft-static
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:catalysis-surface
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acscatal.5b00741"
year: 2015
authors:
  - "Thomas P. Senftle"
  - "Adri C. T. van Duin"
  - "Michael J. Janik"
venue: "ACS Catalysis"
pdf_sha256: "b011add8aa315ef2f05806938bad3cd056b64909a2df0ca1af73e4bc72c64850"
pdf_path: "papers/Senftle_ACS Catalysis_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015senftle-venue-cs5b00741 -->

## Summary

**Spin-polarized density functional theory (DFT)** combined with **ab initio thermodynamics** is used to connect **methane activation** kinetics on **Pd-doped ceria (Pd_xCe_{1−x}O_δ)** surfaces to the **stability of Pd oxidation states** under operating **temperature** and **oxygen pressure**. The authors argue that rapid **C–H** activation on the mixed oxide can reflect **emergent** chemistry where **Pd^{4+} ↔ Pd^{2+}** behavior differs from catalysts dominated by a conventional **PdO_x** active phase: **Pd_xCe_{1−x}O_δ** activates methane by **hydrogen abstraction** at **Pd^{4+}**-related surface states, whereas **PdO_x** surfaces favor a **σ-complex** activation channel emphasized in prior work on **cus-Pd** sites. **Metastable Pd^{4+}** sites that appear under reaction conditions are reported to show **lower** methane activation barriers than **Pd^{2+}** states in the same analysis. The framework is generalized in **(T, P)** space by **phase boundaries** separating regions where each **Pd** surface oxidation state is **thermodynamically stable** versus **kinetically accessible**.

## Methods

**Static QM / DFT + thermodynamic mapping (no production MD).** **Electronic structure:** **Spin-polarized DFT** on **periodic slab** models of **Pd–CeO₂**-related surfaces; **functional**, **dispersion**, **basis**, **k-mesh**, **Hubbard/hybrid** settings, and **supercell** dimensions are given in **Computational methods** and **SI** on `pdf_path` rather than duplicated here. **Basis / potentials:** **plane-wave PAW** within **VASP** as stated in the article. **Structures / pathways:** periodic **oxide slabs**; relaxed **CH₄** adsorption motifs and **C–H** activation coordinates on **Pd-doped ceria** terminations. **Ab initio thermodynamics:** maps versus **T** and **P_O₂** identifying which **Pd** oxidation states are stabilized. **Kinetic coupling:** **apparent** methane activation barriers combine **reaction kinetics** with **thermodynamic** accessibility of **Pd^{4+}** versus **Pd^{2+}** states (abstract).

**MD application:** **N/A** — no atomistic dynamics production run is central to the abstract-framed workflow.

**Force-field training:** **N/A**.

## Findings

**Mechanistic contrast:** **Pd_xCe_{1−x}O_δ** activates methane through **hydrogen abstraction** at **Pd^{4+}**-related states, unlike the **σ-complex** route highlighted for **PdO_x** surfaces in the comparison framed by the authors (abstract).

**Metastability and barriers:** **Active Pd^{4+}** sites are described as **metastable**; they **form under the reaction environment** and can exhibit **lower** methane activation barriers than **Pd^{2+}** states in the same model set (abstract).

**Support effect:** Incorporating **Pd** in the **fluorite** lattice of **CeO₂** stabilizes **Pd^{4+}** chemistry relative to separated **PdO_x** / **CeO₂** references, yielding **emergent** behavior for the **mixed oxide** (abstract).

**(T, P) maps:** **Phase boundaries** separate regions where different **Pd** surface oxidation states are **thermodynamically stable** versus **kinetically active**, used to interpret how **temperature** and **oxygen pressure** move the system between regimes (abstract).

**Comparisons:** The introduction connects to experimental **Pd@CeO₂** and **solution combustion** catalyst literature that motivates **Pd–ceria** synergy; quantitative agreement claims live in the full text.

## Limitations

**DFT slab** idealizations omit **full reactor** transport, **particle-size** distributions, and **dynamic coverage** fluctuations. This publication is **not** a **ReaxFF** study—do not infer classical barriers from this page.

## Relevance to group

**Senftle / Janik / van Duin** collaboration supplying **electronic-structure** and **stability-map** context for **Pd/ceria** catalysis adjacent to reactive **MD** work elsewhere in the corpus.

## Citations and evidence anchors

- DOI [10.1021/acscatal.5b00741](https://doi.org/10.1021/acscatal.5b00741) — `papers/Senftle_ACS Catalysis_2015.pdf`.
- `normalized/extracts/2015senftle-venue-cs5b00741_p1-2.txt`.

## Related topics

- [[2015senftle-venue-research]] (proof duplicate sibling, same DOI)
- [[reaxff-family]]
