---
id: paper:2018yilmaz-j-phys-chem-defect-design
type: paper
title: Defect Design of Two-Dimensional MoS2 Structures by Using a Graphene Layer
  and Potato Stamp Concept
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:2d-layered
- domain:reactive-md
- material:tmd
- method:dft-static
- method:reaxff
- scale:atomistic
- task:application
paper_keywords:
- keyword:2d-materials
- keyword:reaxff-application
- keyword:neb
- keyword:lammps
- keyword:graphene-carbon
- keyword:qm-training-data
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpcc.8b02991
year: 2018
authors:
- Dundar E. Yilmaz
- Roghayyeh Lotfi
- Chowdhury Ashraf
- Sungwook Hong
- Adri C. T. van Duin
venue: J. Phys. Chem. C
pdf_sha256: 98adfafba934f328ed741549bb588d09090d2dea0d48bf8e9817d28c3be83187
pdf_path: papers/Yilmaz_potato_stamp_JPC_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018yilmaz-j-phys-chem-defect-design -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the JPCC article identified by `doi`, `title`, and `pdf_path`.

## Summary

The **“potato stamp”** concept proposes **patterned sulfur extraction** from **MoS\(_2\)** by contacting it with **graphene** bearing **carbon vacancies**: **DFT** and **ReaxFF NEB** show **S** atoms can **diffuse** into **graphene vacancies** with **favorable** barriers for **mono-/simple divacancies**, but **not** for some **reconstructed** defects. **ReaxFF MD** then mimics **contact**, **700 K** diffusion, and **pull-off** to transfer **S** to graphene, leaving **S vacancies** on MoS\(_2\)**. Subsequent MD places **epoxybutane** molecules that **dissociate** at **Mo-exposed** sites, illustrating **catalytic** chemistry at designed vacancies.

Introduction motivation notes demand for scalable **MoS\(_2\)** defect engineering beyond slow beam lithography and frames **graphene vacancy templates** as a contact-printing route to edge-rich, catalytically active motifs probed here with QM barriers and large-cell reactive dynamics.


Readers should verify numerical values, units, and section references against the peer-reviewed PDF and any Supporting Information, especially when extracts or galley PDFs truncate tables.

## Methods

- **DFT:** **VASP**-style setups per Methods; **binding energies** of **S / S\(_2\) / S\(_8\)** on pristine vs **vacancy** graphene; **PBE** (+**D2** vdW) comparisons to literature.
- **ReaxFF training:** Mo/S/C/H/O parameters from **Ostadhossein** MoS\(_2\) and **combustion** extensions; **C–S** terms fit to **DFT** S-binding data on graphene.
- **NEB (ReaxFF, LAMMPS):** **Single-layer MoS\(_2\)** (**~64.6 × 55.3 Å**) with graphene **2 Å** above; barriers for **S** migration toward **monovacancy**, **divacancy (simple)**, **Stone-Wales**, **585**, **555777** defects (barriers reported, e.g. **~2.5** and **~1.6 eV** for mono- and simple-divacancy paths; **unfavorable** paths **>6–13 eV**).
- **Stamp MD:** Large **MoS\(_2\)**/**graphene** cells (**~129 × 110 Å**) with **in-plane PBC**, lattice **slight strains** to commensurate; varied **vacancy counts** (densities up to **~10\(^{14}\) cm\(^{-2}\)**); approach to **2 Å**, **5 ps** forced contact at **700 K**, then **separation**; **three replicas** per case. **Atom** totals for these **stamp** supercells are given in the **JPCC** **Methods**/**tables** (multi-**10⁴** **atom** range for the largest cells—confirm exact counts in **`papers/Yilmaz_potato_stamp_JPC_2018.pdf`**).
- **Functionalization MD:** **100** **epoxybutane** molecules, **2 ns** (and **2.5 ns** cases) at **700 K** on **S-deficient** MoS\(_2\).

- **Replica / metadynamics / applied E-field:** **N/A — not used** beyond the **NEB** / **MD** protocols summarized above.

- **Ensemble / thermostat / barostat:** **NVT**-equivalent **constant-temperature** sampling at **700 K** is implied by the reported **stamp** and **functionalization** segments, but the **PDF** text available to this curation pass does not spell out a **thermostat** brand or **NPT** **barostat** settings—treat **hydrostatic pressure** control as **N/A — not stated** outside the **DFT** portions.

- **Timestep:** **N/A — fs timestep** not recovered cleanly from the extracted **JPCC** text; confirm in **`papers/Yilmaz_potato_stamp_JPC_2018.pdf`** before reproducing trajectories.

## Findings

- **Thermodynamic/kinetic selectivity:** **NEB** shows **S** migration into **mono- and simple-divacancy** graphene is accessible, unlike several **multi-vacancy** reconstructions with **very high** barriers.
- **Stamp efficiency:** Pull-off simulations transfer **~1 S per two monovacancies** on average (ratio discussed vs divacancy cases), consistent with barrier rankings.
- **Chemistry:** **Epoxy** adsorbs dissociatively at **vacancy** sites, exposing **Mo** centers with **catalytic** activity for further reactions as illustrated by sequential snapshots in the paper.

- **Corpus honesty:** Barrier tables and **NEB** images should be checked in **`papers/Yilmaz_potato_stamp_JPC_2018.pdf`**; this page condenses only headline numbers from the article.
## Limitations

ReaxFF barriers are approximate vs DFT; experimental realization of perfect stamp alignment is non-trivial.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
