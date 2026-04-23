---
id: paper:2019mao-carbon-159-2-predicting-cost-effective
type: paper
title: "Predicting cost-effective carbon fiber precursors: Unraveling the functionalities of oxygen and nitrogen-containing groups during carbonization from ReaxFF simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:polymer-organic
  - scale:atomistic
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:reaxff-application
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2019.12.008"
year: 2019
authors:
  - "Qian Mao"
  - "Siavash Rajabpour"
  - "Malgorzata Kowalik"
  - "Adri C. T. van Duin"
venue: "Carbon"
pdf_sha256: "90c9a22f2d000663f1e047e0e39a8d82cd412f51e2526b2d1c8a48f79f47f171"
pdf_path: "papers/Mao_Carbon_2019_carbon_fiber.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019mao-carbon-159-2-predicting-cost-effective -->

## Summary

Polyacrylonitrile (PAN) remains the dominant carbon-fiber precursor despite cost pressure for automotive-scale markets. Blending PAN with poly(\(p\)-phenylene-2,6-benzobisoxazole) (PBO) offers a potential route to lower precursor cost while preserving spinnability and carbon-yield characteristics attractive for industrial carbon fiber production. Mao et al. use ReaxFF reactive molecular dynamics to follow volatile release and all-carbon six-membered ring formation during heating and carbonization for nine PAN/PBO blend ratios, comparing blends against neat PAN, neat PBO, and pre-oxidized PAN references. The abstract frames the scientific question around how oxygen-containing versus nitrogen-containing functional groups participate differently in initiating carbonization chemistry, stabilizing radicals, and incorporating carbon into graphitic fragments.

## Methods

**2 — Force-field training (brief, as used).** The study uses the published **ReaxFF CHON-2019** parameterization for **C/H/O/N** **PAN/PBO** chemistry, including a **triple-bond stabilization** term for **N₂** **vs** the older **CHON-2010** set (see **§2.1** of *Carbon*). **In-text reoptimization** of the entire **ReaxFF** library is **not** the subject here—the authors **select** and **apply** the **CHON-2019** set with documented differences from **CHON-2010** (per **§2.1**).

**1 — MD application (reactive carbonization).** **ReaxFF** **reactive MD** is applied to **blend** **supercells** with **PAN/PBO** **mole** ratios from **50/0** to **0/50** in the stepped series named in the article, plus **pre-oxidized** **PAN** and the **pure** precursors. **System size / composition:** each **of** the **50** **parallel** **chains** is built from **16** **PAN** and **4** **PBO** monomer units in the **construction** in **§2.2** so that **C** **content** is **comparable**; the **resulting** **cells** are **multi–10⁴**-**atom** **systems** (**see** the **table** in **the** **Carbon** **article** for **exact** **atom** **totals** **per** **blend**). **Monomer** counts and **chain** count are as above. **Density** is set **~1.6 g cm⁻³** (within the **1.2–2.0 g cm⁻³** window cited for **PAN** **CF** processing). **PBC** in **3D**; **timestep** **0.25 fs**; **bond-order cutoff** for species ID **0.3**; **Berendsen** thermostat (damping **100 fs**). The protocol **equilibrates** at **300 K** in **NVT** for **300 ps** (regime **I**), then **ramps** **300 K → 2800 K** over **250 ps** at **10 K ps⁻¹** (regime **II**), and **holds** **2800 K** in **NVT** for **2000 ps** for **carbonization** (regime **III**). **Barostat / global pressure control during carbonization:** **N/A** — **NVT** at **fixed** **cell** **volume** and **imposed** **mass** **density** (no **NPT** mean-stress servocontrol in the quoted protocol). **Static external electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**. **MD engine (software package):** **N/A** in the main-text excerpt used here; **reactive** **ReaxFF** **MD** is the stated tool class—consult the **PDF**/**SI** if a **code** name is required for reproduction.
## Findings

### Mechanisms (O vs N functionality)

**Oxygen-containing** groups act as stronger **initiators** of carbonization chemistry; **nitrogen-containing** groups **persist** longer in nascent **graphitic** regions and **scavenge/couple** **carbon-centered radicals** into **extended** networks. **Oxygen-rich** motifs correlate with **earlier** **ring-growth** onset; **nitrogen retention** helps **stitch** **graphenic** fragments—blend **stoichiometry** shifts both **kinetics** and **porosity** of the developing network.

### Cost/design takeaway (1:1 blend)

For **1:1 PAN/PBO**, the abstract highlights **cost** advantages (**pre-oxidation** avoidance, strong **six-membered ring** metrics on simulated horizons, **~95%** of a stated ring metric—map precisely to the article’s **definition**).

### Limitations and future process coupling

Atomistic cells omit **melt flow**, **spinline** stress, and **furnace** gradients; results are **mechanistic** indicators for **precursor** design, not **factory** guarantees.

## Limitations

Atomistic cells omit melt flow, spinline tension, and furnace gradients present in industrial carbonization; results are mechanistic indicators, not process guarantees for factory-scale furnaces.

## Relevance to group

Connects ReaxFF carbonization modeling to precursor blending strategies for carbon fibers at Penn State. The work complements broader pyrolysis and polymer-decomposition entries in the corpus by tying atomistic order parameters to economically motivated blend design.

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2019.12.008](https://doi.org/10.1016/j.carbon.2019.12.008)

## Related topics

- [[reaxff-family]]
