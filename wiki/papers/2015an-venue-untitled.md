---
id: paper:2015an-venue-untitled
type: paper
title: "Atomistic Origin of Brittle Failure of Boron Carbide from Large-Scale Reactive Dynamics Simulations: Suggestions toward Improved Ductility"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:validation-experiment
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevLett.115.105501"
year: 2015
authors:
  - "Qi An"
  - "William A. Goddard III"
venue: "Phys. Rev. Lett."
pdf_sha256: "928cb34c5d07c824a67fb326c055ab9aa946376ac1b496e8e19edd98e5008e4a"
pdf_path: "papers/ReaxFF_others/An_Goddard_BC_PhysRevLett.115.105501.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015an-venue-untitled -->

## Summary

This Physical Review Letters article addresses brittle failure of boron carbide (B\(_4\)C), an extremely hard ceramic that shows anomalous loss of fracture toughness under hypervelocity impact despite a high Hugoniot elastic limit. The authors perform large-scale reactive molecular dynamics using a quantum-mechanics-trained ReaxFF description to shear B\(_4\)C at room temperature in periodic cells containing roughly two hundred thousand atoms, large enough to capture nanometer-scale twin bands and amorphous shear bands. Two slip systems are emphasized: shear along (0001)/[10\(\bar{1}\)0], associated with deformation twinning in the literature, and shear along (01\(\bar{1}\bar{1}\))/[\(\bar{1}\)101], associated with amorphous band formation. The central claim is that brittle failure is tied to formation of higher-density amorphous regions when icosahedral units fracture, producing local negative pressures, cavitation, and crack opening rather than benign accommodation by low-density disorder alone.

## Methods

**Force-field training (ReaxFF for B–C ceramics).** The authors fit ReaxFF to QM benchmarks that include B\(_{10}\)C\(_2\)H\(_{12}\)-like dimers, equations of state for α-B\(_{12}\), γ-B\(_{28}\), T-B\(_{50}\), several B\(_4\)C stoichiometries, heats of formation, and shear-driven amorphization pathways, and they introduce a refined **ReaxF2** parameter set aimed at improved QM shear-stress agreement (letter plus Supplemental Material in `papers/ReaxFF_others/An_Goddard_BC_PhysRevLett.115.105501.pdf`).

**MD application (large-scale shear of B\(_4\)C near room temperature).** Reactive MD applies finite shear in three-dimensionally periodic supercells of order **~2×10⁵** atoms (**~1.25×10⁴** formula units in the abstract’s headline geometry) while following stress–strain and pressure traces until failure. Two slip systems anchor the comparison: **(0001)/[10\(\bar{1}\)0]** (twinning-prone) and **(01\(\bar{1}\bar{1}\))/[\(\bar{1}\)101]** (amorphous-band-prone). Supercell edge lengths for the primary setup, the MD program name, integrator timestep, thermostat or barostat type, explicit **NVT**/**NVE**/**NPT** labels, and **duration** of equilibration versus shear production segments are **not** recovered reliably from the short letter PDF in this workspace—the Supplemental Material tabulates those controls for reproduction.

**Static QM / AIMD corroboration.** Smaller-cell AIMD snapshots reported in the publication support the high mass density inferred for shear-induced amorphous regions referenced in the letter.

**Not used as primary dynamics engines here:** applied electric fields; replica-exchange or metadynamics acceleration; explicit shock-piston loading of the full impact problem. Hydrostatic pressure may appear as a diagnostic of local cavitation rather than as a staged **NPT** production target—confirm against the Supplemental Material for the shear protocol actually used.

## Findings

Along **(01\(\bar{1}\bar{1}\))/[\(\bar{1}\)101]**, icosahedral fracture precedes **high-density amorphous bands**, strongly negative local pressures, **void nucleation**, and **crack opening**. Along **(0001)/[10\(\bar{1}\)0]**, **discrete twinning** intervenes before amorphous bands, cavitation, and cracks. The authors argue brittle failure is tied to **icosahedron destruction** and the ensuing dense amorphous filaments rather than benign low-density disorder alone. **ReaxF2** sensitivity tests show improved elastic response versus the baseline ReaxFF parameterization but preserve the same qualitative failure sequence in their comparison. They suggest **alloying** strategies that promote **intericosahedral slip** while suppressing **icosahedral rupture** as a materials-design direction for more ductile B\(_4\)C-like ceramics. The introduction ties simulations to **hypervelocity impact** and **nanoindentation** observations of nanoscale amorphous bands and the long-standing debate over low-density disorder versus phase-transition explanations—framing why large reactive cells are needed.

## Limitations

**~200k-atom** cells and **shear** protocols still omit **quantum** effects and **long-range** crack mechanics; **ReaxF2** comparisons in the letter highlight **force-field** sensitivity for **stress** metrics.

## Relevance to group

Large-scale **ReaxFF** **mechanics** reference for **boron carbide** failure pathways—complements **ceramic** and **impact** modeling discussions in the corpus.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevLett.115.105501](https://doi.org/10.1103/PhysRevLett.115.105501)

## Reader notes (navigation)

- Ceramic mechanics at scale: [[reaxff-family]]; related high-strain ceramics elsewhere in corpus.

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
