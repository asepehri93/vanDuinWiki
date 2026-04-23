---
id: paper:2013u-khalilov-j-phys-chem-new-mechanisms
type: paper
title: "New mechanism for oxidation of native silicon oxide"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:berendsen-thermostat
  - keyword:nvt-simulation
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp400433u"
year: 2013
authors:
  - "U. Khalilov"
  - "G. Pourtois"
  - "S. Huygh"
  - "A. C. T. van Duin"
  - "E. C. Neyts"
  - "A. Bogaerts"
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "e79c8e81217506ec019c1b025a7d1581a57b71e92ffc67530cefa15ce0c94d30"
pdf_path: "papers/Khalilov_Si_oxidation_JPCC_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013u-khalilov-j-phys-chem-new-mechanisms -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

Reactive atomistic simulations study **hyperthermal oxygen (1–5 eV)** interacting with **thin native SiO\(_x\)** (\(x \le 2\)) films (~10 Å) on **Si(100)–(2×1)**. **Room temperature:** penetrant oxygen **resides mainly inside the oxide**, not at the **SiO\(_x\)|c-Si** interface. **≥ ~700 K:** oxygen **diffuses through** the oxide and reacts at the **crystalline Si** boundary—closer to **thermal oxidation** kinetics described by **Deal–Grove** at high \(T\). The article also analyzes **defect formation** during oxidation relevant to **ultrathin gate dielectrics** and discusses how **oxidant energy** and **temperature** steer mechanism. Readers should cross-check any quantitative barrier or rate statements against the figures and tables in the primary PDF rather than relying on this synopsis alone.

## Methods

**1 — MD application (atomistic dynamics).** **Molecular dynamics** simulations use a **Si|SiO\(_x\)** **ReaxFF** parameterization (**Buehler-type** Si oxidation force field, as cited in the article). A **native oxide** **slab** stack on **Si(100)-(2×1)** is described with an initial cell about **21.7 × 21.7 × 27.1 Å** containing **Si** and **O** **atoms** arranged as a thin **SiO\(_x\)** film, prepared by oxidizing with **1 eV O\(_2\)**, then **equilibrated** at **300, 700, and 900 K** under **NVT** with a **Berendsen** thermostat (**20 ps**, damping **0.1 ps**) followed by **10 ps** **NVE**; the authors report **no significant difference** between **Berendsen** and **Bussi** thermostats for this equilibration test. **Hyperthermal O/O\(_2\)** with **1–5 eV** beam conditions impinges on the **thin SiO\(_x\)** film to probe **localization vs interface reaction** vs **temperature** (`papers/Khalilov_Si_oxidation_JPCC_2013.pdf`; `normalized/extracts/2013u-khalilov-j-phys-chem-new-mechanisms_p1-2.txt`). **Engine / code:** **N/A —** MD software not named in the indexed excerpt (confirm **LAMMPS** or other engine in **`pdf_path`**). **Timestep:** **N/A —** not in the indexed excerpt. **Boundaries / PBC:** **N/A —** not spelled out in the excerpt used here. **Barostat:** **N/A —** **NVT/NVE** legs described without hydrostatic **NPT** control in this summary layer. **Pressure targets:** **N/A —** no **GPa/bar** hydrostatic protocol in the excerpted equilibration description. **Electric field:** **N/A —** not used in the excerpted protocol description. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** the page applies a literature **ReaxFF** parametrization for **Si/O** oxidation rather than reporting a new training workflow in the excerpted material.

**3 — Static QM / DFT-only.** **N/A —** reactive **MD** drives the hyperthermal oxidation study; **DFT** may appear elsewhere in the article for benchmarks, but is not summarized as the production engine here.

## Findings

**Outcomes & mechanisms.** At **room temperature**, penetrant oxygen **resides mainly inside the oxide**, not at the **SiO\(_x\)|c-Si** interface. At **≥ ~700 K**, oxygen **diffuses through** the oxide and reacts at the **crystalline Si** boundary—closer to **thermal oxidation** kinetics discussed with **Deal–Grove**-type expectations at high **\(T\)**. **Oxidant energy** and **temperature** steer **defect formation** and **interface chemistry** relevant to **ultrathin gate** stacks.

**Comparisons.** The synopsis ties **hyperthermal** localization behavior to **high-temperature** **diffusion-limited** oxidation pictures; detailed experimental comparison belongs to the PDF **Discussion**.

**Sensitivity & design levers.** **Substrate temperature** (**300 / 700 / 900 K** equilibration window cited above) and **hyperthermal** **1–5 eV** oxidant conditions control where oxygen localizes vs reacts at the **Si** interface.

**Limitations & outlook.** Model-size and classical-reactive approximations limit quantitative transfer to every experimental beam system; the article spans distinct **hyperthermal** vs **thermal** regimes—readers should not merge them without the authors’ caveats in the PDF.

**Corpus honesty.** Integration **timestep** and full **PBC** specification are **not** in the **`_p1-2`** extract; confirm in **`pdf_path`** for reproduction-grade detail.

## Limitations

Model sizes and classical reactive approximations limit direct quantitative agreement with every experimental beam system. The study spans **hyperthermal** impingement and **elevated temperature** diffusion regimes; operators should not collapse those into a single “oxidation mechanism” without reading the **temperature**-dependent localization discussion in the article.

## Relevance to group

**Silicon oxidation** with **van Duin** ReaxFF in the **PLASMANT** collaboration—bridging hyperthermal and thermal oxidation pictures. Connects to **gate dielectric** processing discussions where **beam energy** and **substrate temperature** jointly determine whether oxidation localizes in the **oxide** or reacts at the **Si** interface.

## Citations and evidence anchors

- DOI: [10.1021/jp400433u](https://doi.org/10.1021/jp400433u)
- Extract: `normalized/extracts/2013u-khalilov-j-phys-chem-new-mechanisms_p1-2.txt`

## Related topics

- [[reaxff-family]]
- Silicon oxides and gate-stack processing
