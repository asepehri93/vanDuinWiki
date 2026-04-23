---
id: paper:2016amiri-venue-oxidation-nickel-2
type: paper
title: "Oxidation of nickel surfaces through the energetic impacts of oxygen molecules: Reactive molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - domain:oxides-ceramics
  - material:metal-surface
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:metallic-systems
  - keyword:reactive-md
candidate_tags:
  - "duplicate-ingest-same-doi-as-2016amiri-venue-oxidation-nickel"
source_refs: []
doi: "10.1063/1.4945421"
year: 2016
authors:
  - "Negar Amiri"
  - "Hassan Behnejad"
venue: "J. Chem. Phys."
pdf_sha256: "ec6bbfefa5bcbc5e7ce791b60cad7c256dd123de3c3c863cf8733019a1098755"
pdf_path: "papers/ReaxFF_others/Amiri_Ni_O_JCP_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2016amiri-venue-oxidation-nickel-2 -->

## Summary

This slug is a **duplicate PDF ingest** for the *Journal of Chemical Physics* article **DOI [10.1063/1.4945421](https://doi.org/10.1063/1.4945421)** (**volume 144**, article **144705**, 2016), with file `papers/ReaxFF_others/Amiri_Ni_O_JCP_2016.pdf` (distinct bytes from **`[[2016amiri-venue-oxidation-nickel]]`** / `Amiri_NiO_impact_JCP_2016.pdf`). The publication uses **reactive molecular dynamics** with **ReaxFF** to study **hyperthermal** oxidation of **Ni(100)** and **Ni(111)** by **O₂** impacts at **5 eV** translational energy with surface temperatures **300**, **600**, and **900 K**. The work examines where **oxide nuclei** first appear, whether **island-growth** kinetics apply, **oxygen uptake** vs temperature, and the **amorphous** character of the growing **NiO** film via **radial distribution functions**, **oxygen density profiles**, and **charge** profiles across **Ni | NiO**. The introduction situates **nickel** alloys and **NiO** in corrosion-resistant and device contexts and contrasts **hyperthermal** exposure with conventional thermal oxidation—a framing that motivates the **successive impact** protocol used in the simulations.

## Methods

This slug is a **second ingested PDF** for the same *J. Chem. Phys.* article as **`[[2016amiri-venue-oxidation-nickel]]`** (**DOI 10.1063/1.4945421**). The simulation protocol is **identical in scientific content**; only **`pdf_path` / `pdf_sha256`** differ at the corpus layer.

### MD application (atomistic dynamics)

The scientific protocol matches **`[[2016amiri-venue-oxidation-nickel]]`** (**same DOI**, different ingested PDF bytes). **LAMMPS** with **variable-charge ReaxFF** treats **Ni(100)** in a **(9×9)** surface cell (**162** surface **Ni atoms**) and **Ni(111)** in **(7×7)** (**196** surface **Ni atoms**), each with **eight** Ni layers. Surfaces are **periodic in-plane**; **O₂** approaches along the non-periodic **Z** direction. After **20 ps** **Berendsen** equilibration (**0.1 ps** damping) at **300**, **600**, or **900 K**, trajectories use **10 ps NVE** relaxation, then **200** successive **5 eV** **O₂** impacts (**2.5 ps** spacing, random in-plane placement) with **Berendsen** cooling between impacts to remove excess energy. Integration uses **velocity Verlet** with **Δt = 0.25 fs**. **Barostat / controlled pressure:** **N/A — not used** in the documented hyperthermal impact workflow.

### Force-field training

**N/A — application paper** (same as sibling slug).

### Static QM / DFT

**N/A — same as sibling slug** (QM appears as reference data for parameterization context, not AIMD production for the impacts).

## Findings

The **duplicate PDF** does not change the abstract-level conclusions: **oxide nuclei** at **arbitrary impact sites**, **Langmuir-like** growth kinetics preferred over **island-growth** under these hyperthermal conditions, **~18.75% / ~23%** increased **oxygen consumption** on **Ni(100) / Ni(111)** from **300 → 900 K**, and an **amorphous NiO** film by **RDF**/density metrics after **200 O₂** impacts per supercell.

- **Comparisons:** The introduction contrasts **hyperthermal** oxidation with prior **thermal** island-growth literature; quantitative agreement statements should be taken from **`pdf_path`**, not duplicated here.
- **Sensitivity:** Trends are keyed to **surface temperature** (**300–900 K**) and **impact energy** (**5 eV** as modeled).
- **Limitations / outlook:** **Hyperthermal** beams are a specific **aerospace**-motivated boundary condition; extrapolation to long-time **corrosion** requires bridging models beyond this paper’s scope.
- **Corpus honesty:** This slug exists because **two PDFs** share one **DOI**; always cite **`pdf_path`** when quoting pagination, and prefer **`[[2016amiri-venue-oxidation-nickel]]`** for primary narrative unless you are auditing checksums.

## Limitations

Two **PDFs** for one **DOI** require explicit **checksum** discipline. **Hyperthermal** conditions model **energetic** oxygen exposure rather than thermal **Langmuir–Hinshelwood** oxidation alone. **Successive impacts** build oxide films far from **thermodynamic equilibrium** thicknesses expected from slow thermal oxidation at the same **T**; extrapolate to long-time corrosion only with explicit **kinetic** bridging models.

## Relevance to group

**Reactive MD** / **ReaxFF** line of work on **metal oxidation** under **hyperthermal** oxygen relevant to **aerospace** and surface science.

## Citations and evidence anchors

- DOI: [10.1063/1.4945421](https://doi.org/10.1063/1.4945421)
- *J. Chem. Phys.* **144**, 144705 (2016).

## Reader notes (navigation)

- Sibling PDF: [[2016amiri-venue-oxidation-nickel]]

## Related topics

- [[2016amiri-venue-oxidation-nickel]]
- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
