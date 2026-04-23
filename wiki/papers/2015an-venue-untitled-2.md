---
id: paper:2015an-venue-untitled-2
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
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevLett.115.105501"
year: 2015
authors:
  - "Qi An"
  - "William A. Goddard III"
venue: "Phys. Rev. Lett."
pdf_sha256: "c0d4ca60155145b0b7454817c11b24cbf6770466f0f49cca322450c404045e00"
pdf_path: "papers/ReaxFF_others/An_Goddard_PRL_B4C_brittle_failure_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015an-venue-untitled-2 -->

## Summary

**Boron carbide (B₄C)** combines **extreme hardness** with a **Hugoniot elastic limit** near **18–20 GPa**, motivating armor applications, yet **hypervelocity impact** experiments show **anomalously low fracture toughness** above roughly **900 m s⁻¹** despite that high HEL. Prior hypotheses invoked **low-density** regions or **phase transitions** without unified experimental support; **nanoindentation** and impact studies instead document **thin amorphous bands** (nanometer width, ~100–200 nm length) that may govern failure. An and Goddard use **large-scale reactive molecular dynamics** with **ReaxFF**—trained against **QM** data on **icosahedral fragments**, **boron polymorph equations of state**, multiple **B₄C stoichiometries**, and **shear deformations** that produce amorphous structures—to simulate **finite shear** in **~200,000-atom** periodic cells at **room temperature** and follow failure on slip systems tied to **twinning** and **amorphous-band** formation.

## Methods

**Force-field training (ReaxFF / ReaxF2).** ReaxFF is trained to DFT reference data on B\(_{10}\)C\(_2\)H\(_{12}\)-like units, equations of state for α-B\(_{12}\), γ-B\(_{28}\), T-B\(_{50}\), multiple B\(_4\)C compositions, heats of formation, and shear-driven amorphization along **(01\(\bar{1}\bar{1}\))/[\(\bar{1}\)101]**. A refined **ReaxF2** set targets improved QM shear-stress tracking; the Supplemental Material compares ReaxFF versus ReaxF2 elastic constants and twin/amorphous detail (`papers/ReaxFF_others/An_Goddard_PRL_B4C_brittle_failure_2015.pdf`).

**MD application (room-temperature shear to failure).** Simulations impose finite shear under three-dimensional periodic boundaries until mechanical failure, contrasting **(0001)/[10\(\bar{1}\)0]** (twinning-related) with **(01\(\bar{1}\bar{1}\))/[\(\bar{1}\)101]** (amorphous-band-related). For **(0001)/[10\(\bar{1}\)0]**, the letter quotes a **~29.4 × 2.2 × 24.0 nm³** cell with **216,000 atoms** (**14,400** formula units). The PRL PDF text layer in this corpus path does **not** spell out the MD program name, integrator timestep, thermostat or barostat parameters, explicit ensemble labels (**NVT**/**NVE**/**NPT**), total strain history, or segment **duration**s—those appear in the Supplemental Material.

**AIMD corroboration.** Smaller-cell AIMD in the publication supports the high mass density inferred for shear-induced amorphous regions.

**Not used as headline tools in the letter:** applied electric fields; replica-based rare-event acceleration; full shock-piston impact loading of macroscopic tiles.

## Findings

**(01\(\bar{1}\bar{1}\))/[\(\bar{1}\)101]** shear yields **amorphous bands** without preceding twins, followed by **cavitation** and **cracks**. **(0001)/[10\(\bar{1}\)0]** shear shows **discrete twinning**, then **amorphous bands**, **cavitation**, and **cracks**. The authors attribute brittle failure to **dense amorphous regions** created when **icosahedra fracture**, generating locally **negative pressures** and void growth, and they propose **alloying** routes that favor **intericosahedral slip** over **icosahedral rupture** for improved ductility. Another manifest entry covers the same **DOI** with `papers/ReaxFF_others/An_Goddard_BC_PhysRevLett.115.105501.pdf`; narrative content should stay aligned between [[2015an-venue-untitled]] and this page.

## Limitations

The study uses **crystalline shear cells** without explicit **grain boundaries**, **porosity**, or **shock loading** conditions of full impact experiments. **ReaxFF** cannot capture full **QM** accuracy for all excited configurations; **ReaxF2** improves **elastic** response but yields the **same mechanistic sequence**. This slug duplicates another ingest (`paper:2015an-venue-untitled`) with the **same DOI**; keep one narrative canonical for citations.

**Confidence rationale:** `high`—extract provides quantitative cell sizes, slip systems, and mechanistic claims tied to the PRL text.

## Reader notes (navigation)

- Sibling ingest (same DOI): [[2015an-venue-untitled]]
- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[reaxff-family]]
