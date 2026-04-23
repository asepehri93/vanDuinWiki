---
id: paper:2022qiang-xu-acs-how-polytetrafluoroethylene
type: paper
title: "How Polytetrafluoroethylene Lubricates Iron: An Atomistic View by Reactive Molecular Dynamics"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - material:polymer-organic
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:tribology
  - keyword:polymer
  - keyword:reactive-md
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.1c23950"
year: 2022
authors:
  - "Qiang Xu"
  - "Jie Zhang"
  - "Xin Li"
  - "Diana M. van Duin"
  - "Yuanzhong Hu"
  - "Adri C. T. van Duin"
  - "Tianbao Ma"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "8633fa837f463cedfd56d6dab9ece09cdd4e163dce27c328e3ab4e7d2659fed6"
pdf_path: "papers/Xu_PTFE_Iron_lubrication_RxFF_Tianbao_ACS_AMI_2022_online.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2022qiang-xu-acs-how-polytetrafluoroethylene -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **ACS Appl. Mater. Interfaces** DOI `10.1021/acsami.1c23950`. This slug uses the **online/VOR** PDF path (`papers/Xu_PTFE_Iron_lubrication_RxFF_Tianbao_ACS_AMI_2022_online.pdf`); sibling galley: **`[[2022xu-x-manuscript]]`**.

## Summary

**PTFE** is widely applied as a **dry-film lubricant** on **steels**, yet **atomistic** routes to **transfer films** and **friction** minima involve coupled **shear**, **oxidation**, and **polymer scission**. The authors **extend ReaxFF** to **Fe–O–C–H–F** chemistry by building on prior **metal/oxide** and **fluorocarbon** databases with new **QM** training data, then simulate **single-asperity shear** of **PTFE** against **iron/oxide** from **10–300 K**. Mechanisms highlighted include **C–C scission** **radicals**, **oxidation/hydroxylation**, **Fe–C** and **Fe–F** **bonding** that **anchor** **transfer films**, and **temperature-dependent chain orientation**. **Friction** is **nonmonotonic**, peaking near **100 K** where **reduced mobility** and **stiffer** chains yield a **less oriented**, **brittle-like** **shear** response. Compare this **online** ingest with **`[[2022xu-x-manuscript]]`** when **reconciling** **identical-DOI** PDF variants in **`papers/`**. **Scientific** **content** should be **treated as** **one** publication with **two** **manifest** rows reflecting **ACS** **PDF** **pipelines**, not **two** independent studies.

## Methods

### A — ReaxFF training / fitting (Fe–O–C–H–F)

- **Lineage:** Extends existing ReaxFF databases for **iron/iron oxides**, **water**, and **fluorocarbon** chemistry with new quantum reference data for **PTFE–metal/oxide** interactions (full training-set composition in the article and Supporting Information).
- **QM reference:** Supplementary DFT (or related QM) data for bond dissociation, oxide/water, and fluoropolymer fragments as listed in the publication—not duplicated numerically on this wiki page.
- **Optimization:** Standard ReaxFF least-squares / Monte Carlo fitting workflow against the compiled training set (software and weighting per article/SI).

### B — Reactive MD (tribology)

- **Engine / code:** LAMMPS (ReaxFF pair style) for **single-asperity** shear of **PTFE** against **iron / iron oxide** surfaces.
- **System:** Atomistic contact models representing dry PTFE-on-steel tribochemistry (approximate sizes and oxide termination in the article).
- **Conditions:** Shear-driven trajectories from **10 K to 300 K**; loads, sliding velocities, and normal pressures specified in the **ACS AMI** article and **SI** (not restated here).
- **Thermostats / integration:** NVT or equivalent thermal control for low-temperature tribology; timestep and damping values in the SI—**not stated in the short local extract**.
- **Analysis:** Friction metrics, chain orientation, radical formation, and transfer-film chemistry from trajectories as reported.

### C — Quantum chemistry

- Used to build and validate the Fe–O–C–H–F extension (see §A); production tribology runs are classical ReaxFF MD.

### D — Connection to experiment

- Mechanistic interpretation is compared to prior **tribochemical** and spectroscopic literature on PTFE–steel transfer films (qualitative alignment stated in the paper).

<!-- blueprint-slots:v1 -->

### MD application — blueprint checklist (indexed text)

Use **`N/A`** where this **PDF role** or **short extract** does not restate a quantity; prefer linked **version-of-record** pages for definitive values.

- **Engine / code:** **LAMMPS** is the usual **reactive MD** engine when **ReaxFF** appears in this corpus; **N/A — additional engines** if not stated on this page.
- **System size & composition:** **Atom** counts / **stoichiometry** / **supercell** sizing are **N/A — not stated in the indexed extract** unless quoted above.
- **Boundaries / periodicity:** **Periodic boundary conditions (PBC)** are typical for slab/bulk models; **N/A — frozen layers / walls** if not stated here.
- **Ensemble:** **NVT** is typical for constant-volume production unless **NPT** is explicitly cited elsewhere for this entry.
- **Timestep:** **timestep** on the order of **0.25 fs** is common for **ReaxFF**; **N/A — exact fs** if not stated in the indexed text.
- **Duration / stages:** **Equilibration** and **production** lengths in **ps**/**ns** are **N/A — not stated** on this stub.
- **Thermostat:** **Nose–Hoover** / **Berendsen** / **Langevin** controls are **N/A — damping/time constant not stated** in the indexed pages.
- **Barostat:** **NVT** entries imply **N/A — barostat / hydrostatic pressure control** unless **NPT** is documented on the canonical article page.
- **Temperature:** **Temperature** setpoints (e.g., **300 K**) are **N/A — not restated** when this file is **SI/proof-only**.
- **Pressure:** **N/A — pressure / stress tensor** targets are **not stated** for this PDF role.
- **Electric field:** **N/A — external electric field / bias** not invoked on this page.
- **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not stated for the workflows summarized here.


## Findings

**Tribochemical** pathways produce **oxidized/hydroxylated** fragments consistent with **prior experiments**. **Transfer films** incorporate **Fe–C/Fe–F** networks and **strong** interactions with **Fe₂O₃** surfaces described as **chelation-like** in the text. **Friction** minima correlate with **ordered** **shear-induced** molecular layers; the **100 K** **friction maximum** reflects **competition** between **mobility** and **chain stiffness**.

## Limitations

**Single-asperity** **MD** omits **multi-asperity** contact statistics; **ReaxFF** uncertainty remains for **fluoropolymer** **oxidation** branches. **Temperature-dependent friction** maxima can reflect **both** **kinetic** and **mechanical** **stiffness** effects—validate **interpretations** against **supplementary** **velocity** and **load** sweeps in the **source** **PDFs**. **ACS** **AMI** **articles** often include **extensive** **SI** for **tribology** **protocols**; **do not** infer **contact area** or **pressure** from this **wiki** summary alone when building **benchmark** **suites**. **Pair** this page with **`[[2022xu-x-manuscript]]`** for **manifest** completeness when **auditing** **duplicate** **PDFs** ingested under the same DOI and matching SHA policy.

## Relevance to group

**van Duin-group** **tribochemistry** flagship alongside **`[[2022xu-x-manuscript]]`**, documenting the **online** PDF variant in **`papers/`** for **hash** provenance. Together these slugs cover **galley vs online** duplicates common in **ACS** ingest pipelines.

## Reader notes (navigation)

- Galley sibling: [[2022xu-x-manuscript]]

## Citations and evidence anchors

- DOI: [10.1021/acsami.1c23950](https://doi.org/10.1021/acsami.1c23950) — `papers/Xu_PTFE_Iron_lubrication_RxFF_Tianbao_ACS_AMI_2022_online.pdf`; extract `normalized/extracts/2022qiang-xu-acs-how-polytetrafluoroethylene_p1-2.txt`.

## Related topics

- [[reaxff-family]]
