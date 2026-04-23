---
id: paper:2022mao-venue-d2nr00203e
type: paper
title: "Cost-effective carbon fiber precursor selections of polyacrylonitrile-derived blend polymers: carbonization chemistry and structural characterizations"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - material:polymer-organic
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:reactive-md
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1039/d2nr00203e"
year: 2022
authors:
  - "Qian Mao"
  - "Siavash Rajabpour"
  - "Mahdi Khajeh Talkhoncheh"
  - "Jiadeng Zhu"
  - "Malgorzata Kowalik"
  - "Adri C. T. van Duin"
venue: "Nanoscale"
pdf_sha256: "3af19116af3c2e394bc141175a3b423dbb18dd5bdfb1622c48a28e050e536c0a"
pdf_path: "papers/Mao_Nanoscale_PAN_blend_carbonfibers_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2022mao-venue-d2nr00203e -->

!!! abstract "Scope"

ReaxFF reactive MD of PAN-based blend precursors during carbonization, with Raman and TEM validation, identifies PAN/cellulose as a strong candidate for high-yield, graphitic carbon fiber precursors.

## Summary

Polyacrylonitrile (PAN) is the dominant carbon fiber precursor but costly; blending PAN with commodity or bio-based polymers can lower cost if carbonization chemistry remains favorable. The study combines ReaxFF reactive molecular dynamics with experimental Raman and TEM on selected blends, tracking all-carbon ring formation, O- and N-bearing species, and migration toward turbostratic graphene-like structure.

Industrial carbon fibers require high char yield and graphitic microstructure; the paper uses atomistic trajectories to rationalize why some blends outperform others despite similar initial polymer cost.

## Methods

### A — ReaxFF (PAN-blend carbonization)

- **Lineage:** ReaxFF description for **C/H/O/N** chemistry in **polyacrylonitrile**-derived blends (parameter references in *Nanoscale* **Methods**).

### B — Reactive MD

- **Systems:** **Neat PAN**, **oxidized PAN**, **PAN/nylon 6,6**, **PAN/cellulose** stacks representing precursor films before full carbonization.
- **Protocol:** Thermal **ramps** / holds for **carbonization** chemistry; **RDFs**, **C–C** bond-length distributions, **sp\(^2\)** fractions, and ring/heteroatom evolution as diagnostics.
- **Software / ensemble:** LAMMPS ReaxFF as stated in the article; **timestep** and **thermostat** in **Methods**.

### C — Quantum chemistry

- Supplementary **QM** benchmarks if cited for validation of key bond energies (see article).

### D — Experiments

- **Raman** spectroscopy and **TEM** on **carbonized** fibers from the same blend families; compare **crystallinity** and **graphitic** character to simulation trends.

Simulation **heating** programs should be compared **qualitatively** to lab **pyrolysis** schedules when interpreting timing of ring growth; full temperature programs are in the **Nanoscale** **Methods**.

**ReaxFF pyrolysis MD:** **Engine: LAMMPS**; **C/H/O/N** **polymer** **blend** **supercells** ( **PAN** / **nylon** / **cellulose** ) with **3D** **PBC**; **NVT** with **ramped** **temperature** **(K)** **schedules** and **sub-fs** **timestep**; **Nose**–**Hoover**-class **thermostat** during **heating**; **ps**–**ns** **stages**; **barostat** **N/A** for **fixed**-**volume** **pyrolysis** **boxes**; **hydrostatic** **pressure** **N/A** unless **NPT**; **E-field** **N/A**; **replica** **exchange** **N/A**; **atom** **counts** in *Nanoscale*.

## Findings

Among the four precursors examined, PAN/cellulose shows the highest simulated carbon yield and the most extensive all-carbon ring clustering and graphitic growth; Raman and TEM on PAN/CL-derived carbon fibers indicate high crystallinity, consistent with the ReaxFF picture. The authors trace gasification and carbonization pathways for PAN/CL and argue that cellulose acetal moieties can catalyze cyclization of the blend, suggesting bio-based additives with similar functionality as tunable blend partners. PAN/CL is argued as a cost-effective route because cellulose is abundant, the blend can avoid a separate oxidation step, yield and ring formation are strong, and mechanical enhancement of the resulting fibers is plausible.

The convergence of simulation and microscopy supports using ReaxFF as a screening tool for precursor blends before lengthy fiber-spinning trials.

Nanoscale documents full simulation cell compositions, heating ramps, Raman peak assignments, and TEM statistics for each blend so carbon-fiber benchmarking can trace metrics to the peer-reviewed figures.


## Limitations

Atomistic models capture finite segments and heating protocols that should be cross-checked against the full Methods section for system sizes, ramp rates, and equilibration windows.

## Relevance to group

Group-authored ReaxFF study of polymer pyrolysis and carbonization with direct experimental validation.

## Citations and evidence anchors

- DOI: [10.1039/d2nr00203e](https://doi.org/10.1039/d2nr00203e)

## Related topics

- [[reaxff-family]]
