---
id: paper:2016tsafack-carbon-105-2-exploring-interface
type: paper
title: "Exploring the interface between single-walled carbon nanotubes and epoxy resin"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:mechanics-tribology
  - material:graphene-carbon-nano
  - material:polymer-organic
  - method:reaxff
  - method:dft-static
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2016.04.066"
year: 2016
authors:
  - "Thierry Tsafack"
  - "John M. Alred"
  - "Kristopher E. Wise"
  - "Benjamin Jensen"
  - "Emilie Siochi"
  - "Boris I. Yakobson"
venue: "Carbon (2016) 105, 600–606"
pdf_sha256: "6727746fad7e256f78046c7b3673426da2a2c346c5526180155bb087491730e2"
pdf_path: "papers/ReaxFF_others/Tsafack_Epoxide_CNT_Carbon_2016.pdf"
extraction_quality: "good"
group_affiliation: false
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:graphene-carbon
  - keyword:polymer
  - keyword:lammps
---
<!-- id:paper:2016tsafack-carbon-105-2-exploring-interface -->

## Summary

**Carbon fiber** composites gain stiffness and strength when **single-walled carbon nanotubes (SWCNTs)** tether covalently to **epoxy** matrices, but **interface** design must trade off **tube integrity**, **chemical** **heterogeneity**, and **processing** cost. **NASA**-adjacent **aerospace** **motivation** appears throughout the **Carbon** article because **epoxy** **infused** **CNT** **yarns** are **candidate** **structural** **elements** where **inter-tube** **shear** often **limits** **bulk** **strength** even when **individual** **tubes** are **strong**. **Tsafack** et al. screen **DGEBA epoxy** coupling to **(n,0) zigzag SWCNTs** with **n = 5–15** using **DFT** for **quantum** reference energies and **ReaxFF MD** for **large** **configuration** sweeps. The study varies **B**, **N**, and **Si** **dopants**, introduces **monovacancy**, **Stone–Wales**, and **N-terminated** defects, and compares **oxygen** functionalization motifs (**O**, **OH**, **COOH**, **NH\(_2\)**, **O+OH** pairs) to rank **binding**, **affinity indices**, and **shear fracture** forces relevant to **inter-tube** **load transfer** in **yarn**-like assemblies.

## Methods

**1 — MD application (ReaxFF / LAMMPS).** **Engine:** **LAMMPS** with **ReaxFF** parametrizations for **fullerene** and **silicon carbide** literature sets cited in §2.2, using a **0.25 fs** timestep. **Thermostat:** **Nosé–Hoover** coupling whenever **NVT** segments are specified below. **Systems:** **(n,0) zigzag SWCNTs** with **n = 5–15** plus **DGEBA**-linked motifs spanning **dopants** (**Si**, **B**, **N** in direct/adjacent sites), **defects** (**monovacancy**, **N-terminated mono- and divacancies**, **Stone–Wales**), and **oxygen-bearing functionalizations** (**O**, **OH**, **COOH**, **NH\(_2\)**, **O+OH**). **Binding-energy MD:** two-stage equilibration (**NVT**, **300 K**, **Nosé–Hoover**, **100 ps**; then **NVE**-like segment **25 ps** with velocity rescaling to damp fluctuations) with **binding energies** sampled every **25 fs** between **100–125 ps** per Equation (1). **Affinity-index workflow:** **NVT** equilibration (**300 K**, **Nosé–Hoover**, **100 ps**) pulling **DGEBA** from ~**15 Å** toward the tube, followed by **NVE** segment **25 ps**; cylindrical shells (**ΔR = 0.5 Å**) accumulate atom counts for the **affinity index** definition in §2.2–2.3. **Shear fracture tests:** **60 × 60 × 52 Å\(^3\)** cells with **PBC along the tube axis** and fixed boundaries transverse to the tubes; **NVT** preequilibration **12.5 ps** at **300 K**, then stepped pulls of the right **handle** by **0.05 Å** each **1 ps** cycle until **DGEBA** rupture (**~0.05 Å/ps** pull speed as stated). **Barostat / bulk pressure control:** **N/A —** not used in these gas-phase/junction models. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** this study **applies** published **ReaxFF** databases; it does not report a new fit.

**3 — Static QM (DFT).** **Program:** **CP2K** quickstep with **mixed Gaussian / plane-wave** representation. **Functional / potentials:** **PBE** with **Goedecker–Teter–Hutter (GTH)** double-ζ polarized Gaussians; **280 Ry** plane-wave cutoff and **efficient orbital transformation** for relaxations/electronic steps (§2.2). **Structures:** relaxed **CNT–DGEBA** motifs parallel to the MD screening set. **k-sampling:** **N/A —** cluster/supercell setups as described in the paper rather than dense **k**-meshes for extended metals.

**4 — Metrics.** **Binding energies**, **affinity indices** from cylindrical distributions, and **fracture forces** (peak load prior to **DGEBA** scission) are reported as defined in §2–3.

## Findings

**Outcomes.** The **abstract** highlights that, within the screened **(n,0)** series and chemistries, **smaller-diameter** tubes, **Si doping**, **O+OH** co-functionalization, and **monovacancy** motifs tend to give the **strongest** **interfacial metrics** (binding/affinity/fracture) among the cases emphasized there—exact ordering and numerical tables are in *Carbon* **105** Results.

**Comparisons.** **DFT** and **ReaxFF** binding trends are reported to be **qualitatively aligned** for functional-group rankings (**O+OH > O > NH\(_2\) > OH > COOH** in the discussion) and largely consistent for many **defect** motifs, while **diameter dependence** appears more pronounced in **DFT** than in **MD** for some sets (**§3**).

**Sensitivity / levers.** **§3** contrasts how **dopants**, **defects**, and **functional groups** change both **thermodynamic** binding metrics and **mechanical** fracture loads; **non-covalent** wrapping alone yields **poor shear transfer** relative to **covalent** bridges, motivating **grafting** strategies for **yarn**-level load transfer.

**Limitations (authored / scope).** Models isolate **local junction** chemistry; **coverage**, **cure chemistry**, and **polycrystalline** **CNT** ensembles in real composites extend beyond the sampled motifs.

**Corpus honesty.** Quantitative **nN** fracture examples and **per-configuration** energies should be copied from **Figures 3–4** in the **PDF**, not from this summary alone.

## Limitations

- Models isolate **local** interface motifs; real composites involve **coverage**, **cure chemistry**, **entanglement**, and **defect distributions** beyond the sampled set.
- **ReaxFF** + **DFT** agreement should be checked on a case-by-case basis for new chemistries.

## Relevance to group

**CNT–polymer** interface engineering with **ReaxFF**—complements **graphene oxide / epoxy** style reactive simulations elsewhere in the corpus.

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2016.04.066](https://doi.org/10.1016/j.carbon.2016.04.066)
- Text-aligned pointers: `normalized/extracts/2016tsafack-carbon-105-2-exploring-interface_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
