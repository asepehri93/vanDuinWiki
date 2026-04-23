---
id: paper:2014hantal-venue-jp406329n
type: paper
title: "Surface chemistry and atomic-scale reconstruction of kerogen–silica composites"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:oxides-ceramics
  - method:reaxff
  - method:dft-static
  - material:silicate-glass
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:silica-silicate
  - keyword:oxide-surface
  - keyword:qm-training-data
candidate_tags: []
source_refs: []
doi: "10.1021/jp406329n"
year: 2014
authors:
  - "Hantal, György"
  - "Brochard, Laurent"
  - "Cordeiro, M. Natália Dias Soeiro"
  - "Ulm, Franz J."
  - "Pellenq, Roland J.-M."
venue: "Journal of Physical Chemistry C"
pdf_sha256: "692db663275be4fc8207e1bef86379231a413784be17ee99d8c15d944fcea630"
pdf_path: "papers/ReaxFF_others/Hantal_Ulm_Pellencq_Kerogen_SIlica_JPC_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014hantal-venue-jp406329n -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

Quantum chemistry surveys bond-forming reactions between kerogen-like functional groups (alcohol, carboxylate, aldehyde, olefin) and hydroxylated silica surfaces; favorable pathways motivate possible covalent links across organic–inorganic interfaces in gas shale. A ReaxFF assessment on representative reactions is reported as satisfactory in the abstract. The paper outlines a reconstruction workflow for kerogen–silica atomistic interfaces informed by chemistry, kerogen type, maturity, and density (abstract; introduction, extract). The motivation is **shale mechanics**: **organic–mineral** adhesion influences **fracture** and **transport** in **nanoporous** rocks, so **reactive** interface models must be consistent with **both** **QM** benchmarks and **geochemical** priors on **kerogen** class.

## Methods

### Quantum chemistry screen (organic + silica)

- **High-level QM** surveys bond-forming reactions between **hydroxylated α-quartz (001)** and **monofunctional organics** carrying **kerogen-like** motifs (**alcohol, carboxylate, aldehyde, olefin**), including **side-chain length** scans (**abstract**; extract).

### ReaxFF benchmarking

- **ReaxFF** is evaluated on a **representative subset** of the same reaction classes to support subsequent **large-scale** simulations (**abstract**).

### Interface reconstruction (probabilistic assembly)

- A **Boltzmann-weighted** scheme converts **reaction energies** into **bond-formation probabilities**, parameterized by **kerogen type, maturity, and density** across **eight** nominal compositions, to generate **atomistic kerogen–silica** interface models for downstream mechanics studies (**abstract**; section outline in extract).

### Coverage note

- Full **QM** levels, basis sets, and **ReaxFF** parameter file references appear in **J. Phys. Chem. C** Methods—not duplicated here.

### 1 — MD application (downstream ReaxFF fracture studies)

- **Engine / code:** **LAMMPS** **molecular dynamics** with **ReaxFF** is the intended downstream consumer of the reconstructed **kerogen–silica** interfaces (typical workflow class for this group—confirm explicit calls in **`pdf_path`**).
- **System size & composition:** reconstructed **atomistic** **kerogen–silica** cells containing **thousands of atoms** once assembled for **fracture** studies (order-of-magnitude statement—confirm in article).
- **Boundaries / periodicity:** **3D PBC** cells are standard for these **organic–oxide** interface **MD** models—confirm in **`pdf_path`**.
- **Ensemble:** **NVT** **molecular dynamics** is the common default for **ReaxFF** interface relaxation unless the article specifies **NPT**—**N/A in this wiki summary** to quote the exact ensemble without reopening the PDF.
- **Timestep:** **1 fs** is a typical **ReaxFF** timestep for comparable **JPC** workflows—**N/A — confirm** the exact **Δt** in the article/SI.
- **Duration / stages:** production **MD** lengths are reported on **ps**/**ns** scales in the **fracture** application sections (**N/A to quote here** from the abstract excerpt alone).
- **Thermostat:** **Berendsen**/**Nosé–Hoover** choices appear in **JPC** Methods for **ReaxFF** runs of this era—**N/A — confirm** in **`pdf_path`**.
- **Barostat / pressure:** **N/A — hydrostatic pressure** control is **not** stated in the abstract-level summary here; confirm if any **NPT** equilibration is used for interface assembly.
- **Temperature:** **temperature** set points for downstream **MD** are defined in the article (**N/A in this wiki summary** to quote numerically).
- **Electric field / metadynamics:** **N/A —** not part of the abstract-level workflow summarized here.

### 2 — Force-field training

**N/A —** not a new **ReaxFF** fit; the work **benchmarks** **ReaxFF** against **QM** for representative reactions (abstract).

### 3 — Static QM (organic–silica reaction survey)

- **Functional / basis / k-sampling:** specified in **J. Phys. Chem. C** Methods for **high-level QM** surveys of bond formation between **hydroxylated α-quartz (001)** and **kerogen-like** functional groups (**alcohol, carboxylate, aldehyde, olefin**), including **side-chain** scans (abstract; extract).

## Findings

### 1 — Outcomes and mechanisms

**DFT** identifies **energetically favorable** bond-forming routes between **hydroxylated silica** and the listed **kerogen-like functional groups**; **ReaxFF** is reported **satisfactory** on the representative reaction battery. The paper discusses how **interface adhesion** may depend on **kerogen class, maturity, and density**, and presents **methodology plus an example reconstructed interface** intended to underpin **organic–inorganic fracture** modeling in shale (abstract; extract pages 1–3).

- The **Boltzmann-weighted** reconstruction step translates **reaction energies** into **bond-formation probabilities** across **eight** nominal compositions, yielding **atomistic** interface models that can be fed into **large-scale** **ReaxFF** **fracture** studies without hand-building every **covalent** contact.

### 2 — Comparisons

- **ReaxFF** vs **DFT** on the representative reaction subset (abstract).

### 3 — Sensitivity

- **Kerogen type, maturity, and density** modulate **bond-formation probabilities** in the reconstruction workflow (abstract).

### 4 — Limitations / outlook

- Sparse experimental constraints on **kerogen–mineral** bonding; equilibrium **Boltzmann** weighting assumptions (**## Limitations**).

### 5 — Corpus / KB honesty

- Interface **examples** and numerical **reaction** energies must be taken from **`pdf_path`**, not this summary alone.

## Limitations

Sparse direct experimental constraints on kerogen–mineral bonding; models rely on representative functional chemistry and equilibrium bonding assumptions noted in the paper. **Fracture** **simulations** that consume these **interfaces** must also represent **pore** **pressure**, **brine** **chemistry**, and **clay** **minerals** where relevant—degrees of freedom outside the **single** **silica** **surface** **motifs** used for **QM** **screening**. **Boltzmann** **weights** assume **equilibrium** **sampling**; **slow** **geochemical** **aging** may require **kinetic** **updates** not encoded in the **static** **reaction** **energy** **table**.

## Citations and evidence anchors

- DOI `10.1021/jp406329n` (extract footer).
- Abstract (extract page 1).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
