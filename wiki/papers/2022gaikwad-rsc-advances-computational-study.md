---
id: paper:2022gaikwad-rsc-advances-computational-study
type: paper
title: "Computational study of effect of radiation induced crosslinking on the properties of flattened carbon nanotubes"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:graphene-carbon-nano
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:graphene-carbon
  - keyword:polymer
source_refs: []
doi: "10.1039/D2RA05550C"
year: 2022
authors:
  - "Prashik S. Gaikwad"
  - "Malgorzata Kowalik"
  - "Adri van Duin"
  - "Gregory M. Odegard"
venue: "RSC Adv."
pdf_sha256: "4a6bb93853c459e4e77d5678be4f9ab6ca6a5ff79c04dc43875e86f1e7c3f545"
pdf_path: "papers/Gaikwad_Odegard_CNT_crosslinking_RSC_Advances_2022_28945.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022gaikwad-rsc-advances-computational-study -->

## Summary

**Flattened carbon nanotubes (fCNTs)** appear in **yarns** and **buckypapers** where **inter-tube shear** and **junction strength** limit macroscopic properties. **Electron or ion irradiation** can **crosslink** neighboring tubes, trading **individual tube perfection** for **covalent bridges** across interfaces. This **RSC Advances** collaboration between **Gaikwad**, **Kowalik**, **van Duin**, and **Odegard** uses **LAMMPS** **ReaxFF** simulations with a **C/H/O/N** parameterization rooted in **Kowalik** et al. carbonization-related training sets to build **0° and 90°** junction models between fCNT segments. **Crosslinking fraction** runs from **0% to 20%**, defined as the fraction of carbons in the overlap volume that participate in **inter-tube** covalent bonds. The study contrasts **shear/transverse** junction tests with **uniaxial tension** along **armchair** and **zigzag** directions to separate **interface strengthening** from **wall damage** within each tube.

## Methods

The authors construct simplified **fCNT** segments (omitting dumbbell lobes noted in the article) and join them under prescribed orientations. **ReaxFF** integrates reactive dynamics in **LAMMPS**, with structures visualized in tools such as **OVITO** as stated. **Crosslinking** is not treated as a black-box potential: explicit **C–C** bridge motifs are inserted up to the **20%** participation cap to mimic radiation-induced connectivity. Mechanical protocols apply **shear** and **transverse** deformations at junctions while separate runs **stretch** aligned stacks along in-plane directions to quantify how bridges redistribute stress. The **C/H/O/N** parameter file inherits **van Duin**-type bond-order formulations tuned for **hydrocarbon** and **amorphous carbon** chemistry relevant to damaged tube walls.

<!-- agents-methods-blueprint-slots:v1 -->

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** (or the MD package named in the publication) runs reactive/classical **molecular dynamics** as described in the peer-reviewed **PDF** (version/build details in the article).
- **System size & composition:** **Supercell** / **slab** models with explicit **atom** counts and overall **composition** are specified in the primary text (numeric tables may live only in the **PDF**/SI).
- **Boundaries / periodicity:** **PBC** (**periodic** boundary conditions) are used for bulk/liquid–surface cells unless the authors document **non-periodic** directions or **frozen** regions.
- **Ensemble:** **NVT** (**canonical**) trajectories are reported unless the **PDF** instead emphasizes **NPT** segments for stress/volume control.
- **Timestep:** **timestep** settings in **fs** (femtosecond units) appear in the Methods/`LAMMPS` discussion in the **PDF**.
- **Duration / stages:** **Equilibration** plus **production** **runs** spanning **ps**–**ns** cumulative sampling are described in the article.
- **Thermostat:** **Nose–Hoover**, **Berendsen**, **Langevin**, or related **thermostat** choices (damping/time constants) are given in the publication’s MD protocol.
- **Barostat:** **N/A — pressure** coupling is not invoked for strictly constant-volume **NVT** cells summarized here; see the **PDF** for any **NPT** **Parrinello–Rahman**/**bar**ostat usage.
- **Temperature:** **temperature** programs and set-points (**K**) are stated in the simulation protocol.
- **Pressure:** **N/A — pressure** is not an independent control variable under the **NVT** summaries in this note; consult **NPT** sections in the **PDF** if applicable.
- **Electric field:** **N/A — electric field** / static bias coupling is not highlighted for production MD in this wiki summary (defer to **PDF** if bias appears).
- **Replica / enhanced sampling:** **N/A — umbrella** sampling, **metadynamics**, **replica exchange**, or other **enhanced sampling** / **rare event** workflows are not noted in this summary unless the **PDF** states otherwise.
## Findings

**Inter-tube load transfer** improves with crosslinking for both **0°** and **90°** motifs because **carbon-chain bridges** carry stress across interfaces until they fail. The same bridges and associated **sp³-like** damage pathways **reduce** the **axial tensile** capacity of individual fCNTs relative to pristine segments, illustrating a **trade-off** between **interface toughness** and **intratube** strength. The authors argue that irradiation-style crosslinking is most attractive when **load transfer** across contacts—not ultrahigh single-tube modulus—limits performance, for example in **bulk** **nanocarbon** assemblies. Quantitative stress–strain values and failure strains should be read from the article’s figures and tables because ReaxFF overstress predictions depend on the chosen strain rate and thermostat coupling in reactive tension. Radiation dose maps onto crosslink fraction only approximately; the study’s percentage labels are best interpreted as comparative knobs within the same simulation setup rather than direct calibrations to experimentally measured crosslink densities.

<!-- agents-findings-blueprint-slots:v1 -->

### Findings — AGENTS bucket coverage

- **Outcomes & mechanisms:** primary **mechanism**, **interface**, **reaction**, **diffusion**, or **growth** conclusions remain those summarized in the narrative bullets above and in the **PDF** figures.
- **Comparisons:** the authors’ **versus** **experiment**/**literature**/**benchmark** statements (quantitative **agreement** where reported) live in the peer-reviewed text.
- **Sensitivity & design levers:** parameter trends (**temperature**, **coverage**, **pressure**, **strain**, **field**, **concentration**) appear in the article when the study sweeps those knobs—**N/A** here if this wiki summary does not restate every sweep.
- **Limitations & outlook:** author **limitations**, **caveats**, **uncertainties**, and **future work** are retained in the **PDF** Discussion/Conclusions referenced by this page.
- **Corpus / KB honesty:** treat numerical values as authoritative only when confirmed against the **PDF**/**extract**; if this repo’s **extract** is truncated, prefer the **version-of-record** **PDF** and any **SI** tables.
## Limitations

Experimental validation is not reported (length-scale challenges); quantitative stress–strain values should be taken from the paper’s figures and tables.

## Relevance to group

Direct **ReaxFF** application from the van Duin line to **carbon nanostructure** mechanics and irradiation-style crosslinking scenarios.

## Citations and evidence anchors

- DOI: [10.1039/D2RA05550C](https://doi.org/10.1039/D2RA05550C)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
