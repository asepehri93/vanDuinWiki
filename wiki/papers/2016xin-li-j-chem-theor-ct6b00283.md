---
id: paper:2016xin-li-j-chem-theor-ct6b00283
type: paper
title: "Optical Properties of Gold Nanoclusters Functionalized with a Small Organic Compound: Modeling by an Integrated Quantum-Classical Approach"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - method:hybrid-qmmm
  - method:dft-static
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.6b00283"
year: 2016
authors:
  - "Xin Li"
  - "Vincenzo Carravetta"
  - "Cui Li"
  - "Susanna Monti"
  - "Zilvinas Rinkevicius"
  - "Hans Ågren"
venue: "J. Chem. Theory Comput. (2016) 12, 3325–3339"
pdf_sha256: "54142e3381667c55d97bef5089f6eff6a734a7361e953579a0cac417a121b8d8"
pdf_path: "papers/ReaxFF_others/Li_Monti_Au_peptide_acs.jctc.2016.pdf"
extraction_quality: "good"
group_affiliation: false
paper_keywords:
  - keyword:dft-static
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:polarizable-ff
---
<!-- id:paper:2016xin-li-j-chem-theor-ct6b00283 -->

## Summary

Li *et al.* study **one- and two-photon absorption** of **para-nitroaniline (pNA)** on **Au nanoparticles** (facet-resolved **AuNP887**, **AuNP1505**, **AuNP1985**, **AuNP3007** models) using a pipeline that couples **ReaxFF molecular dynamics** sampling to **QM/capacitance–molecular mechanics (QM/CMM)** **TD-DFT** in **DALTON**. The **QM/CMM** layer follows **Rinkevičius *et al.*, *J. Chem. Theory Comput.* 2014**, treating the metal with **Gaussian-broadened fluctuating charges and dipoles** and **capacitance–polarizability** couplings while the **QM** region uses **range-separated CAM-B3LYP** / **TZVP** for each **pNA** within **3 Å** of the surface; the article stresses that **plasmonic** enhancement of the external field is **not** included, which matters especially for **two-photon** bands overlapping **Au** plasmons.

## Methods

**1 — MD application (ReaxFF).** **Engine / code:** **ReaxFF** as implemented in **ADF** and **LAMMPS** (citations **56–57** in the article). **Systems:** cubic **400 × 400 × 400 Å** supercells with **three-dimensional periodic boundaries** containing facet-explicit **Au** nanoparticles (**Figure 2**) with **pNA** placed initially as **two shells** farther than **5 Å** from the surface to drive adsorption. **Adsorption leg:** **NVT** at **300 K** with slow heating while monitoring potential energy; the first adsorption/equilibration segment averages **~50 ps** while **pNA** migrates (reported surface uptake **44–72%** depending on **AuNP** size). **Production MD:** after **75 ps** further equilibration, **500 ps** **NVT** production at **300 K** (“ambient pressure” wording in the paper refers to the stated conditions, not a stress-fluctuation barostat). **Thermostat:** **Berendsen** with **0.1 ps** coupling time. **Timestep:** **0.25 fs** with **Verlet** leapfrog integration; configurations saved every **0.025 ps**. **Analysis:** **RDFs**, **SDFs**, minimum **pNA–Au** distances, **pNA–pNA** RDFs, **Au–Au** RDF, radius of gyration, **I_max/I_min**, and eccentricity to classify binding sites and **NP** shape drift; representative late-trajectory snapshots feed the **QM/CMM** stage. **Barostat / external pressure control:** **N/A —** **NVT** cells without **NPT** stress targeting. **Electric field:** **N/A —** not applied in the **MD** stages described. **Replica / enhanced sampling:** **N/A —** conventional **MD** only.

**2 — Force-field training (ReaxFF for pNA–Au).** **Parent model:** **Rom *et al.*** **ReaxFF** parameters for **TNT**-like **nitro-aromatic** chemistry provide the **pNA** intramolecular starting point; **Au** interactions begin from **van Duin**-lineage **Au** parameters (**refs 26–28**). **QM reference:** **plane-wave DFT** trajectories and minima from prior work (**ref 41**) on **pNA** on a three-layer **Au(111)** slab (parallel vs perpendicular binding families), plus gas-phase **B3LYP/6-311+G(d)** constrained bond scans (**Gaussian 09**) for **pNA** internal modes. **Training targets:** **X/Au** (**X = N, C, O, H**) pair interactions refit while intramolecular **pNA** terms are held fixed, using the **serial ReaxFF** single-parameter search optimizer. **Validation:** **Table 2** in the article compares **ReaxFF** and **DFT** relative energies for **pNA–Au(111)** binding motifs.

**3 — Static QM / TD-DFT (QM/CMM).** **Snapshots:** one relaxed geometry per **AuNP** size, drawn randomly from the last picoseconds of production **MD** when adsorbates are settled. **QM/CMM:** **Au** treated as the polarizable **MM** metal with **Jensen & Jensen** capacitance–polarizability parameters; **pNA** molecules within **3 Å** of **Au** each get a **QM/CMM** calculation (**81 / 106 / 142 / 160** molecules for the four **AuNP** sizes), and spectra are averaged over that pool. **TD-DFT:** **range-separated CAM-B3LYP** with **triple-ζ TZVP**; **one-** and **two-photon** linear and quadratic response in **DALTON**. **Dispersion / short-range:** included in the **QM/CMM** Hamiltonian as described in **§2.4** (together with the article’s caveat that **TPA** may overlap plasmon bands not modeled). **k-sampling:** **N/A —** gas-phase **QM** regions extracted from finite **MD** cells.

**4 — Reviews / experiments.** **N/A —** computational study with comparison to earlier **QM** benchmarks, not a new laboratory experiment.
## Findings

**Outcomes.** **QM/CMM TD-DFT** shifts **one-photon** bands versus gas-phase **TD-DFT** through both **transition energies** and **relative intensities** because **charge imaging / polarization** of the **Au** support reshapes the contributing states (**abstract** and **§3**). **Two-photon** results are presented more as a **method demonstration** because **TPA** energies can overlap **plasmon** excitations that the **QM/CMM** Hamiltonian omits (**§2.4** caveat).

**Sensitivity / levers.** **Facet** distributions (**Figure 2**) and **NP** size set **pNA** coverage statistics (**44–72%** adsorbed fractions quoted in **§2.3**), which feeds how many orientations enter the spectral average; smaller **NPs** emphasize facet differences called out in the **abstract**.

**Comparisons.** **ReaxFF** binding motifs and relative energies align with prior **DFT** data for **pNA** on **Au(111)** within the **Table 2** benchmarks; optical benchmarks vs experiment are developed with **SI** material on **`[[2016susanna-venue-paper]]`**.

**Limitations (authored).** Besides the **TPA / plasmon** caveat, **nanosecond**-scale **MD** may still under-sample rare **pNA** arrangements the authors flag when discussing dynamics (**Discussion**).

**Corpus honesty.** This article is a **ReaxFF parametrization + MD** paper **and** a **QM/CMM spectroscopy** paper; use **`[[reaxff-family]]`** for the reactive **MD** lineage and the **SI** slug for **SI-only** figures.
## Limitations

**TD-DFT** accuracy depends on **CAM-B3LYP**/**TZVP** choices; **QM/CMM** omits explicit **plasmon–field** coupling. **ReaxFF MD** may miss rare **pNA** arrangements important for charge-transfer-sensitive excitations. Downstream citations should name the **Rinkevičius *et al.*, *J. Chem. Theory Comput.* 2014** coupling reference exactly as in the **JCTC** article.

## Reader notes (navigation)

The **SI** PDF is registered separately as **`[[2016susanna-venue-paper]]`**; keep that sibling link intact when refactoring **Monti**/**gold cluster** clusters in the graph.

## Relevance to group

Methodological neighbor to **Monti**/**Li** **Au–biomolecule** threads documented via **`[[2016susanna-venue-paper]]`** and related pages.

## Citations and evidence anchors

- DOI: [10.1021/acs.jctc.6b00283](https://doi.org/10.1021/acs.jctc.6b00283)
- Text-aligned pointers: `normalized/extracts/2016xin-li-j-chem-theor-ct6b00283_p1-2.txt`
- SI PDF: `papers/ReaxFF_others/Li_Monti_Au_peptide_acs.jctc.2016_SI.pdf` → **`[[2016susanna-venue-paper]]`**

## Related topics

- [[2016susanna-venue-paper]]
- [[2016susanna-monti-j-phys-chem-jz5b02769]]
