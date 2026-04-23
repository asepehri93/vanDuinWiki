---
id: paper:2022foroutan-physical-che-controlled-hydrophilization
type: paper
title: "Controlled hydrophilization of black phosphorene: a reactive molecular dynamics simulation approach"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - material:widegap-semiconductor
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:2d-materials
  - keyword:lammps
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1039/D2CP02382B"
year: 2022
authors:
  - "Masumeh Foroutan"
  - "Borhan Mostafavi Bavani"
  - "Ahmad Boudaghi"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "5e268f5a7f98b7a47c171cb9254fbd5bf18cd64719298c514b73abac14533845"
pdf_path: "papers/ReaxFF_others/Foroutan_PCCP_2022_phosphorene.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022foroutan-physical-che-controlled-hydrophilization -->

## Summary

Reactive MD with ReaxFF studies wetting of pristine and oxidized black phosphorene in LAMMPS. Pristine surfaces show hydrophobic droplets with elliptical footprints reflecting anisotropy; progressive oxidation introduces phosphorene oxide motifs that raise hydrogen-bond counts and drive contact angles from hydrophobic toward superhydrophilic behavior, with placement-dependent wetting patterns. **Black phosphorus** **flakes** **oxidize** under **ambient** **humidity**, so **wettability** is not a fixed **material constant** but couples to **in situ** **oxide** **coverage** and **defect** **distribution**.

## Methods

Simulations use periodic x–y boundaries with fixed P/C substrate layers and a free z dimension; box sizes are ~88 Å × 88 Å × 42 Å with an ~86 Å × 86 Å phosphorene patch. Nosé–Hoover thermostat (100 fs coupling) maintains 298 K in NVT with a 0.2 fs timestep and 3 ns equilibration segments for droplets up to ~1500 molecules as scanned in the study. Oxidation is realized by prescribed oxygen uptake on the surface; contact angles and line tensions are extracted via Young and modified Young analyses, and energy landscapes scan single-water adsorption to map anisotropic barriers (armchair vs zigzag). **Phys. Chem. Chem. Phys.** reporting follows **standard** **ReaxFF** **water** + **oxide** **chemistry** conventions for **P/O/H** systems described in the article’s **Computational** section.

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

Pristine phosphorene yields large contact angles (~132–140° depending on direction and size) and elliptical droplets consistent with anisotropic surface energy. Oxidation increases hydrogen bonding and lowers angles across a broad range, producing multiple wetting motifs depending on where water first contacts the oxide. Helmholtz free-energy profiles and barrier heights differ between armchair and zigzag directions, matching faster spreading along zigzag inferred from energy scans. **Environmental** **stability** conclusions should be paired with **experimental** **AFM**/**XPS** **oxidation** states because **ReaxFF** **oxygenation** **patterns** are **idealized** compared to **native** **oxide** **mixtures** on **exfoliated** **samples**.

<!-- agents-findings-blueprint-slots:v1 -->

### Findings — AGENTS bucket coverage

- **Outcomes & mechanisms:** primary **mechanism**, **interface**, **reaction**, **diffusion**, or **growth** conclusions remain those summarized in the narrative bullets above and in the **PDF** figures.
- **Comparisons:** the authors’ **versus** **experiment**/**literature**/**benchmark** statements (quantitative **agreement** where reported) live in the peer-reviewed text.
- **Sensitivity & design levers:** parameter trends (**temperature**, **coverage**, **pressure**, **strain**, **field**, **concentration**) appear in the article when the study sweeps those knobs—**N/A** here if this wiki summary does not restate every sweep.
- **Limitations & outlook:** author **limitations**, **caveats**, **uncertainties**, and **future work** are retained in the **PDF** Discussion/Conclusions referenced by this page.
- **Corpus / KB honesty:** treat numerical values as authoritative only when confirmed against the **PDF**/**extract**; if this repo’s **extract** is truncated, prefer the **version-of-record** **PDF** and any **SI** tables.
## Limitations

ReaxFF oxidation patterns are simplified relative to experimentally ill-defined oxides; droplet sizes remain nanoscopic compared to macroscopic contact-angle measurements.

**Encapsulation** **stacks** (**h-BN**, **Al\(_2\)O\(_3\)**) and **covalent** **functionalization** routes used to **stabilize** **phosphorene** in **devices** alter **wetting** relative to **bare** **oxidized** **slabs** modeled here.

**Electrolyte** **gating** and **photooxidation** **under** **ambient** **illumination** introduce **charge** **traps** and **oxide** **gradients** not represented in **thermal** **NVT** **droplet** **protocols**.

## Relevance to group

Reactive MD case study for phosphorene environmental oxidation and interfacial water with quantitative wetting metrics.

## Citations and evidence anchors

<!-- Prefer DOI link when `doi` is present in frontmatter. -->

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
