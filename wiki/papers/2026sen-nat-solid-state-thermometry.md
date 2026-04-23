---
id: paper:2026sen-nat-solid-state-thermometry
type: paper
title: "Solid-state thermometry via ionic-electronic coupling in two-dimensional heterostructures"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - material:tmd
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:validation-experiment
  - keyword:charge-equilibration
source_refs: []
doi: "10.1038/s44460-026-00034-2"
year: 2026
authors:
  - "Dipanjan Sen"
  - "Anirban Chowdhury"
  - "Safdar Imam"
  - "Anshul Rasyotra"
  - "Joan M. Redwing"
  - "Zdenek Sofer"
  - "Alireza Sepehrinezhad"
  - "Adri van Duin"
  - "Arpan Ghosh"
  - "Chen Chen"
  - "Vlastimil Mazanek"
  - "Thomas S. Ie"
  - "Mercouri G. Kanatzidis"
  - "Saptarshi Das"
venue: "Nature Sensors"
pdf_sha256: "a1eeeb54593170c8be4b9f4ab4098176533b86c276b2259ce1b31cdef2973e86"
pdf_path: "papers/Sen_Nature_Sensors_2026_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2026sen-nat-solid-state-thermometry -->

## Summary

Monolayer MoS2 field-effect transistors with van der Waals bimetallic thiophosphate (ABP2X6) top-gate dielectrics use thermally activated cation migration to modulate channel conductance, enabling compact solid-state thermometry with roughly 1-2 degC resolution, fast electronic readout, and sub-nanojoule readout energy in about one square micrometer footprint, supported by electrical characterization and complementary molecular dynamics with a tailored ReaxFF description.

## Methods

Primary source: `papers/Sen_Nature_Sensors_2026_galley.pdf` (Nature Sensors; galley shows author queries in places).

**Materials and crystals.** Synthesis and chemical vapor transport growth protocols for representative ABP2X6 crystals (including multi-day two-zone furnace schedules with iodine transport agent), plus Raman, powder XRD, XPS, AFM, SEM, and EDS characterization as reported.

**Device fabrication.** Monolayer MoS2 on 25 nm Al2O3; e-beam lithography and SF6 RIE to pattern channels; mechanical exfoliation of 2D dielectrics onto channels; second lithography for source, drain, and top-gate electrodes; e-beam evaporation of Ni/Au contacts; dual-gated underlapped geometry.

**Electrical measurements.** Semi-automated probe station (Formfactor 11000) with Keysight B1500A parameter analyzer. Representative bias example from the manuscript: top-gate sweep -6 V to +6 V at fixed back-gate 3 V and drain 1 V; channel width 1 um. Transfer sweeps, sweep-range and sweep-rate studies, ambient temperature sweeps, time-resolved threshold tracking, and related analyses used to link hysteresis and on-off ratio to ion migration.

**Reactive MD (supporting mechanism).** A ReaxFF parametrization for Li-In-P-S was developed using DFT reference data (including elastic properties of beta-Li3PS4 and orthorhombic InPS4 from Materials Project structures, energy-strain fits, Birch-Murnaghan bulk modulus). Molecular dynamics simulations (Supplementary figures in the article) are used alongside experiment to support thermally activated Li+, Cu+, or Ag+ transport and extracted barriers and mobilities.

**1 — MD application (atomistic dynamics).** LAMMPS ReaxFF **molecular dynamics** in **PBC** **supercells**; **NVT**/**NPT** **equilibration** per Supplement (fs **time step**, ps/ns **duration**, **Berendsen** or **Nose–Hoover** **thermostat** on ion-transport runs). **N/A** on this one-page blurb: full **atom** counts. Gate **bias** **−6** **V** to **+6** **V** in ## Methods is a **laboratory** **electric field** on FETs; **N/A** to MD **E-field** in the ReaxFF summary. **N/A** — **NPT** **Parrinello** **barostat** details in this blurb. **N/A** — **replica** or **metadynamics**.

**2 — Force-field training.** **Li–In–P–S** **ReaxFF** fit to **DFT** (Materials Project **geometries**, Birch–Murnaghan **bulk** **modulus**, **strain** **traces**).

**3 — Static QM / DFT in training** — as above. **4 — Review** — **N/A.**
## Findings

- ABP2X6-gated MoS2 FETs show n-type behavior with large on-off ratio; dual-sweep top-gate operation yields counterclockwise hysteresis and sweep-direction-dependent subthreshold slope consistent with mobile ions rather than ferroelectric switching alone.
- Minor hysteresis loops under reduced sweep range and sweep-rate-dependent on-off ratio support diffusion-limited, history-dependent ion motion in the layered dielectric.
- Current on-off ratio increases with temperature under fixed sweep conditions, consistent with thermally activated ion migration.
- Combined experiment and MD analysis (including Arrhenius-style interpretation in the paper) ties device-level thermal sensitivity to ionic-electronic coupling in vdW thiophosphates.
- Reported sensor metrics in the abstract include roughly 1-2 degC resolution, sub-nanojoule readout energy, and ~1 um2 footprint for the demonstrated platform.

- **Corpus honesty / outlook:** **Galley** **(Sen_Nature_Sensors_2026_galley.pdf)**; **VOR**-level **reconciliation** for any **voltage**/**K**-**dependent** **figure**; **caveat** in `## Limitations` on **ionic** **drift** and **sweep** **rate**.

## Limitations

Galley PDF may differ from final pagination; ionic devices can show sensitivity to sweep protocol and ambient exposure.

## Relevance to group

Adri van Duin co-authors the ReaxFF parametrization and MD supporting ion-transport interpretation.

## Citations and evidence anchors

DOI: `10.1038/s44460-026-00034-2`.

## Related topics

- [[reaxff-family]]
