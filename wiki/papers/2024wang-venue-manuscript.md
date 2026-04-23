---
id: paper:2024wang-venue-manuscript
type: paper
title: "Prediction of a Novel Electromechanical Response in Polar Polymers with Rigid Backbones: Contrasting Furan-Derived Nanothreads to Poly(vinylidene fluoride)"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:application
  - material:polymer-organic
  - material:graphene-carbon-nano
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:lammps
  - keyword:nose-hoover
  - keyword:polymer
  - keyword:2d-materials
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.nanolett.4c01431"
year: 2024
authors:
  - "Tao Wang"
  - "Yawei Gao"
  - "Bo Chen"
  - "Vincent H. Crespi"
  - "Adri C. T. van Duin"
venue: "Nano Lett."
pdf_sha256: "72bc95f0bb4e3c87e6329172a21ab1b970a3e6ad9b8164fa50e8d4e91305ed35"
pdf_path: "papers/Wang_Nanoletters_Furan_nanothread_2024_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024wang-venue-manuscript -->

!!! abstract "Scope"
    **Syn furan nanothreads** (polar, rigid ladder backbone) vs **PVDF**: **ReaxFF** (**ReaxFF_furan2024** retraining of **CHO2008**) and **Gao et al. PVDF ReaxFF** simulate **electric-field** response—**torque**, **poling**, and **ferroelectric-like** ordering in **crystals**.

## Summary

**Carbon nanothreads** are stiff **sp³** polymers; **syn furan** threads place **oxygens on one side**, giving a **strong transverse dipole** and unusual **electromechanical** coupling. The authors compare **furan-derived syn nanothreads** to **β-phase PVDF**-like chains: PVDF responds through **σ-bond rotation** (flexible backbone), whereas **rigid nanothreads** can **twist** under field, producing **length-dependent torque** and coupling **field rotation history** to **axial tension** in **anchored** geometries. **Bulk crystal** simulations address **collective poling**.

## Methods

The extract includes **“Reactive Force Field Optimization and Validation”** and **“Molecular Dynamics”** subsections. **ReaxFF_furan2024** refines **Chenoweth et al. ReaxFF_CHO2008** for **C/H/O** combustion chemistry toward **furan nanothreads**: improved **straight vs. bent oligomer** energetics vs. **DFT**, **Bader-like charges**, **dipole moment per formula unit** (~**0.26–0.27 e·Å**), and reduced error on the **furan dimerization barrier** (**~12.3 → ~4.9 kcal/mol** vs. DFT, as quoted). **PVDF** uses the **C/H/O/F/Al** parametrization of **Gao et al.** (cited as matching DFT/experiment for polarizability and phase stability).

**1 — MD application (field + bulk poling).** **Engines:** **standalone** **ReaxFF** program (**velocity** **Verlet**) for **end-anchored** **syn** **furan** and **all-trans** **PVDF** **oligomers** under **electric** **field**; **LAMMPS** **molecular** **dynamics** + **Nosé–Hoover** **thermostat** for **bulk** **crystal** **packings** of **nanothreads** and **β-PVDF**-like **cells** (**0.25** **fs** **time** **step** in the extract). **E-field** magnitudes, **PBC** **supercell** **sizes**, and **ps/ns** **durations** per **case** are **N/A** on *this* summary (extract **cuts** mid-**crystal** discussion—confirm in **`pdf_path`** / **SI**). **Isothermal** **T** and **E**-**ramp** **stages** are in the **letter**/**SI** beyond the **snippet**. **Barostat / NPT, umbrella/metadynamics, replica** — **N/A** in the high-level text summarized here.

**2 — Force-field training** (same **ReaxFF** lines as the paragraph above): **furan** thread **reparameterization** vs **CH2008** with the **0.26–0.27 e·Å** dipole, **dimer** **barrier** error reduction, and **Gao** **ReaxFF** for **PVDF** trajectories. **3 — Static QM** — DFT as **ReaxFF** **training** and **check**; not a **QM-only** **application** **paper** beyond that.
## Findings

**Electromechanics, comparisons, and limitations (abstract + letter).** **PVDF**-like **chains** show **length**-**independent** **torque** through **σ**-**bond** **torsion** under **E**; **syn** **furan** **nanothreads** show **length**-**dependent** **torque** and **backbone** **twist** that **couples** **field** **cycling** to **axial** **tension** in **anchored** **geometries**—a **reactive**-**to**-**rigid** **contrast** **vs** **flexible** **backbone** **deformation**. **Dense** **polar** **crystal** **assemblies** **polar** as **~3** **GV**·**m⁻¹** and **T** = **300** **K** with **ferroelectric**-**like** **P**-**E**-type **phenomenology** **analogous** in **spirit** to **simulated** **β-PVDF** **(abstract)**. **Authors' caveats** about **ReaxFF**-level **polarization** and **long**-**time** **relaxation** are echoed under **`## Limitations`**; **outlook** toward **1D** **ferroic** **materials** is **narrative**-**level** in the **summary** **prose**.
## Limitations

Local PDF is a **galley**. **Field strengths** and **system sizes** in *Nano Lett.* should be verified against the **final PDF**. **ReaxFF** remains approximate for **excited** electronic polarization and **long** dielectric relaxation times.

## Relevance to group

**Adri C. T. van Duin** is corresponding author; the work connects **ReaxFF reparameterization** to **1D polar polymers** and **ferroelectric** phenomenology.

## Citations and evidence anchors

- DOI: [10.1021/acs.nanolett.4c01431](https://doi.org/10.1021/acs.nanolett.4c01431)

## Reader notes (navigation)

These sections summarize what the checked-in extraction and abstracts support; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter above. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
