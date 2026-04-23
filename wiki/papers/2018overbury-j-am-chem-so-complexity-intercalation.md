---
id: paper:2018overbury-j-am-chem-so-complexity-intercalation
type: paper
title: 'Complexity of Intercalation in MXenes: Destabilization of Urea by Two-Dimensional
  Titanium Carbide'
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:2d-layered
- domain:batteries-electrochemistry
- domain:reactive-md
- domain:reaxff-lineage
- method:reaxff
- task:application
- scale:atomistic
candidate_tags: []
source_refs: []
doi: 10.1021/jacs.8b05913
year: 2018
authors:
- Steven H. Overbury
- Alexander I. Kolesnikov
- Gilbert M. Brown
- Zhiyong Zhang
- Gokul S. Nair
- Robert L. Sacci
- Roghayyeh Lotfi
- Adri C. T. van Duin
- Michael Naguib
venue: J. Am. Chem. Soc.
pdf_sha256: 42a24a3169f9736e5dc3ada97a96845d147a3b086dba228ea57d75cff07c3f8d
pdf_path: papers/Overbury_JACS_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018overbury-j-am-chem-so-complexity-intercalation -->

## Summary

This **JACS** article combines **inelastic neutron scattering**, **infrared spectroscopy**, and **ReaxFF reactive molecular dynamics** to study **urea** in **Ti₃C₂Tₓ MXene** interlayers. The central experimental conclusion is that **urea is chemically destabilized** under conditions relevant to intercalation, producing **fragments such as ammonium** (seen with INS) and **CO₂** (IR), rather than behaving as a passive intercalated molecule. **ReaxFF** simulations are used to propose **atomistic pathways and energetics** consistent with the measurements, highlighting how **guest chemistry** in **MXene galleries** can diverge from naive “insert a molecule” pictures—important for **electrochemical storage**, **sensing**, and **water-related** uses of MXenes.

MXene galleries can host solvents and electrolytes for energy storage and sensing; treating guests as inert intercalants can mis-predict chemistry when reactive fluids encounter hydrophilic terminations. Combining vibrational probes with reactive MD clarifies when urea decomposes versus persists, informing safe electrolyte selection and interpretation of interlayer spectroscopy in 2D electrode materials. Consult the peer-reviewed PDF and any Supporting Information for authoritative tables, figures, and numerical diagnostics behind the summaries above.
## Methods
**1 — Experiments (MXene + urea).** **Ti₃AlC₂-derived Ti₃C₂Tₓ** is prepared by **HF** etching, washing to **pH > 4**, drying, then treated with **50 wt % aqueous urea** (**0.9 g MX** in **20 g** solution, **15 h** at **60 °C**). **Inelastic neutron scattering (INS)** and **FTIR** probe **guest chemistry** against reference solids (see article/SI for instrument parameters and reference syntheses).

**2 — MD application (ReaxFF, urea–water–MXene).** **Reactive molecular dynamics** with **ReaxFF** supplies **atomistic pathways** for **urea** in contact with **hydrophilic Ti₃C₂Tₓ** terminations and intercalated **water**. Representative production runs discussed in the main text use a **temperature ramp of 0.005 K per iteration** with an integration **timestep of 0.1 fs** to accelerate chemistry relative to laboratory timescales. **Engine / PBC / ensemble:** **LAMMPS**-style **ReaxFF** inputs with **three-dimensional PBC** supercells are documented in the **Supporting Information** (cell sizes, **NVT/NPT** staging, and total **ps**/**ns** durations are not reproduced on this wiki page). **Thermostat:** coupling law and **thermostat** implementation (e.g., **Nosé–Hoover** vs **Berendsen**) are specified in the **Supporting Information** rather than the short ramp excerpt in the main text. **Barostat / pressure:** **N/A —** main-text excerpt refers readers to **SI** for hydrostatic stress control details. **Electric fields / enhanced sampling:** **N/A —** not used in the excerpted reactive MD discussion.

**3 — Force-field training.** **N/A —** the study **uses** a published **ReaxFF** parameterization for **Ti–C–O/H/N** chemistry rather than refitting parameters.

**4 — Static QM.** **N/A —** **DFT** is not the headline partner method alongside INS/IR + ReaxFF in this article.

## Findings
**Outcomes / mechanisms:** **INS** of **urea-treated MXene** aligns more closely with **ammonium-bearing** references than with **intact urea** or **Ti–urea** complexes, supporting **urea decomposition** and **NH₄⁺-related** guests in galleries. **FTIR** shows **CO₂**, consistent with **decarboxylation/decomposition** rather than passive **urea intercalation**.

**Comparisons:** spectroscopic fingerprints are compared against deliberately synthesized **reference** solids and **blank** controls as described in **JACS**.

**Sensitivity / levers:** **temperature** (**60 °C** soak) and **termination disorder** modulate interlayer chemistry; the **ReaxFF** section explores how **hydrophilic surfaces** steer **bond-breaking** and **proton transfer**.

**Limitations / outlook:** the authors caution that **guest speciation** in **MXene** galleries can be **misread** if **gallery expansion** alone is interpreted as intact **urea** insertion.

**Corpus honesty:** detailed **ReaxFF** boundary conditions live in the **SI** PDF linked from the article; quote **timestep/ramp** values from the **main text** figure discussion where reproduced here.

## Limitations

- **Termination disorder** and **water activity** strongly affect interlayer chemistry; quantitative rates may depend on **sample-specific** details.
- **Force-field** accuracy for **N–C–O** chemistry next to **Ti–C–O/H** motifs should be checked when extending to **other MXenes** or **electrochemical potentials**.

## Relevance to group

Coauthored by **Adri C. T. van Duin**; demonstrates **ReaxFF** as a partner tool to **neutron spectroscopy** on **2D energy materials**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/jacs.8b05913` (`papers/Overbury_JACS_2018.pdf`).

## Related topics

- [[reaxff-family]]
