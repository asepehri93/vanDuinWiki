---
id: paper:2017kumar-physical-che-dislocation-assisted
type: paper
title: "Dislocation assisted crack healing in h-BN nanosheets"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:lammps
  - keyword:2d-materials
  - keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: "10.1039/C7CP04455K"
year: 2017
authors:
  - "Rajesh Kumar"
  - "Avinash Parashar"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "842d68ef66d84460c17e0a8d66e29d3d06a3977678f1ceab52071128854a2cce"
pdf_path: "papers/Others/Kumar_BN_Tersoff_PCCP_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017kumar-physical-che-dislocation-assisted -->

Classical **molecular dynamics** with a **Tersoff** potential for **hexagonal boron nitride (h-BN)** explores how **5|7 dislocations** interact with **mode-I cracks**, reporting **substantial toughening** (on the order of tens of percent) relative to pristine benchmarks for selected geometries.

## Summary

Polycrystalline h-BN sheets contain grain boundaries whose low-angle cores are often described as **dislocations**—here **pentagon–heptagon (5|7)** pairs. Kumar and Parashar embed **central cracks** in large h-BN sheets and vary **dislocation–crack** arrangements. **Quasi-static tensile** loading drives mode-I failure; **virial stress** analysis yields failure stresses and **mode-I stress-intensity–related** metrics. Relative to reference cases without the beneficial dislocation–crack coupling, the study reports **fracture toughness improvements from about 11% to 74%**, depending on geometry, and attributes the effect to **interaction of dislocation and crack stress fields** (shielding, bonding across flanks, crack arrest in favorable configurations).

## Methods

**1 — MD application (classical fracture MD in LAMMPS).** All simulations use **Tersoff parameters for h-BN from Albe et al.** as cited, in **LAMMPS**; **OVITO** is used for post-processing. **Monolayer h-BN sheets** are **~302 × 302 Å²** with **centrally embedded mode-I cracks** (**~25 Å** along armchair loading, **~27 Å** along zigzag loading after convergence tests on **15–30 Å** crack lengths). **System size & composition:** **single-layer h-BN** supercells of the above lateral size (**~10000 atoms** order-of-magnitude for a monolayer sheet of the stated area—exact counts follow from the supercell repeat vectors in the PDF). **5|7 dislocations** are embedded in **pair configurations** consistent with the paper’s Fig. 1 geometries. **Relaxation** proceeds in two **50 ps** segments under **NPT** (**Nose–Hoover thermostat and barostat**): first with **dislocations present**, then after **introducing the crack**. **Quasi-static in-plane uniaxial tension** follows, with **strain rate ~10⁻³ ps⁻¹** (as stated in the article; the PDF text uses scientific notation). The authors report **in-plane boundary conditions** to limit **size/edge** artifacts. **Simulation temperature** is **50 K** to **minimize thermal noise** in extracted **\(K_\text{IC}\)** trends; they note **insensitivity** of **\(K_\text{IC}\)** to modest **thermal distribution** choices at this low temperature. **Virial stress** (their eqn (2)) feeds **critical stress intensity** estimates (eqn (3)). **N/A — integration timestep (fs)**: not recovered reliably from the extracted PDF text on the pages used for this pass—confirm in the article if a precise **Δt** is required for reproduction.

**2 — Force-field training.** **N/A — new fit**: **fixed literature Tersoff** parameters (**Albe et al.**) are used.

**3 — Static QM / DFT.** **N/A — production DFT**: the fracture study is **classical MD** only.

**4 — Review / non-simulation framing.** **N/A**: primary **PCCP** application paper.

## Findings

**Outcomes and mechanisms.** **5|7 dislocations** paired with cracks can **raise** estimated mode-I toughness by **~11%–74%** relative to their **pristine** baselines in the scenarios reported, depending on **dislocation–crack geometry**. The authors attribute improvements to **interaction of dislocation and crack stress fields** (compressive shielding near crack edges, **lattice trapping** of bond-breaking paths, and **cross-linking / chain formation** across crack flanks in some configurations).

**Comparisons.** **Pristine armchair / zigzag** benchmark **\(K_\text{IC}\)** values from their model are stated to agree with **prior published results** for h-BN sheets. They also contrast **dislocations** with literature on **Stone–Thrower–Wales (STW)** defects being **more detrimental** to mechanical response in h-BN.

**Sensitivity and design levers.** **Separation parameters** between dislocations and crack (**\(R_y\)**, **\(R_{xy}\)**, in-line offsets, etc.—see Fig. 1 families **aBN–eBN** in the paper) strongly modulate whether **toughness enhancement** appears, **saturates**, or disappears; **armchair versus zigzag** crack alignment changes which **bridging** motifs dominate.

**Limitations and outlook (as authored).** The study highlights **limited prior work** specifically on **5|7 dislocations versus fracture** in h-BN and points to **further research** on **other defect types** and experimental validation.

**Corpus / PDF honesty.** Numbers and geometry labels above follow the **checked-in PCCP PDF** text; if local **extracts** disagree, prefer the **PDF** bytes referenced by `pdf_path`.


## Limitations

Classical **Tersoff** MD omits **charge transfer** and **quantum** effects; sheet sizes and loading rates are **nanoscale / quasi-static** and may not map one-to-one to macroscopic fracture tests. Geometry choices (single dislocation types, periodic supercells) bound generality.

## Relevance to group

Illustrates **non-ReaxFF** **classical MD** on **2D BN** mechanics and **fracture**, complementary to reactive MD studies on BN and carbon systems in the corpus.

## Citations and evidence anchors

- DOI: [10.1039/C7CP04455K](https://doi.org/10.1039/C7CP04455K) — *Phys. Chem. Chem. Phys.* **19** (2017) 21739–21747.

## Reader notes (navigation)

These sections summarize what the checked-in extraction and abstracts support; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter above. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[graphene-nanocarbon]]
- [[2016rajesh-kumar-j-phys-chem-jp6b05812]]
