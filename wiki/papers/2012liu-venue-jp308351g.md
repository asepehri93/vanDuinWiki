---
id: paper:2012liu-venue-jp308351g
type: paper
title: "Reactive dynamics study of hypergolic bipropellants: monomethylhydrazine and dinitrogen tetroxide"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:energetic-materials
  - keyword:reactive-md
  - keyword:nve-simulation
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
source_refs: []
doi: "10.1021/jp308351g"
year: 2012
authors:
  - "Liu, Yi"
  - "Zybin, Sergey V."
  - "Guo, Jiaqi"
  - "van Duin, Adri C. T."
  - "Goddard, William A., III"
venue: "Journal of Physical Chemistry B"
pdf_sha256: "e29987945956387224479cca5da5bbe705aa4cced9b8ea8b43fc491db53338d7"
pdf_path: "papers/Liu_Zybin_etal_MMH_DNTO_JPCB_2012.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2012liu-venue-jp308351g -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

**ReaxFF** **reactive dynamics** compares the **hypergolic** **MMH–NTO** interface with a **reactive but nonhypergolic** **EtOH–NTO** mixture. The abstract reports **faster energy release** for **MMH–NTO** on mixing, **H abstraction** and **N–N scission** as major early reactions, **more reaction channels** for **MMH–NTO** than **EtOH–NTO** in early-stage statistics, and **NO₂** diffusion into fuel as part of the coupling of **mixing** and **chemistry**. Hypergolic design is discussed in terms of **low barriers** for **H abstraction**/**bond scission** and **oxidizer diffusion**.

The introduction frames **MMH/NTO** as a storied **bipropellant** pairing where **spontaneous ignition** on contact must be understood from coupled **fluid mixing** and **reactive** pathways, motivating a controlled **liquid–liquid** interface model with an ethanol reference that ignites only at higher temperature.


Readers should verify numerical values, units, and section references against the peer-reviewed PDF and any Supporting Information, especially when extracts or galley PDFs truncate tables.

## Methods


**Systems:** Periodic **liquid** **interface** models for **MMH** (**128** molecules), **EtOH** (**128**), **NTO** (**256**), **MMH-NTO** (**128**/**256**), and **EtOH-NTO** (**128**/**256**); **NTO/MMH = 2:1** matches common **experimental** ratios. Fluids are **randomly** packed, then **five** **expansion-compression** **annealing** cycles to **experimental** **densities** (**NTO** **1443 kg/m^3**, **EtOH** **789**, **MMH** **880** at ambient); **half-density** variants are also reported. **Interface** boxes include **large-area** (**MMH-NTO** **36x36x29 A^3**, **EtOH-NTO** **36x36x30 A^3** at full density) and **small-area** (**15x15x170** and **15x15x176 A^3**) geometries (**Figure 1**); **premixed** vs **unpremixed** initial arrangements are compared.

**Protocol:** **Energy minimization** **1 ps**, **NVT** at **50 K** for **0.5 ps**, then **heat** **50 K -> 3000 K** at **1 K/fs** with **Berendsen** thermostat (**0.1 ps** coupling). **Production:** **NVE** or **NVT** **120 ps** at **1000-3000 K** (**250 K** steps). **Integration:** **Delta t = 0.1 fs**. **Code:** parallel **ReaxFF** in **GRASP** (Sandia **LAMMPS**-lineage implementation per article). Observables include **potential energy**, **temperature**, **bond orders**, and **product** **counts**.

### MD application (liquid–liquid interfaces)

**Engine / code:** **Parallel ReaxFF** dynamics in **GRASP** (article text ties this to Sandia’s **LAMMPS**-lineage reactive **MD** stack).

**System size & composition:** **Periodic** liquid cells with **128** **MMH** and **256** **NTO** molecules for the **2:1** **NTO/MMH** mixture (and analogous **EtOH**/**NTO** constructions) as enumerated in Section II.

**Boundaries / periodicity:** **Three-dimensional periodic** supercells sized to match experimental liquid **densities** after packing/**annealing** cycles (interface area variants **36×36×29 Å³** vs **15×15×170 Å³** classes summarized on the wiki from Figure 1).

**Ensemble:** **NVT** during minimization/heating stages; **production** segments use **NVE** or **NVT** as reported for the comparative hypergolic vs reference mixtures.

**Timestep:** **0.1 fs**.

**Duration / stages:** **1 ps** minimization; **0.5 ps** **NVT** at **50 K**; staged heating to **3000 K**; **120 ps** production segments sampled across **1000–3000 K** in **250 K** increments (per Section II / abstract-level summary).

**Thermostat:** **Berendsen** thermostat during heating with **0.1 ps** coupling time.

**Barostat / pressure control:** **N/A —** **NPT** barostat not emphasized for these condensed-phase interface models (density set during packing/**annealing**).

**Temperature:** **50 K** initial conditioning up to **3000 K** heating ramp; production sweeps **1000–3000 K**.

**Pressure / stress:** **N/A —** external **hydrostatic pressure** control not highlighted in the excerpted protocol summary.

**Electric field:** **N/A —** not applied in the quoted setup.

**Replica / enhanced sampling:** **N/A —** not used.

### Force-field training

**N/A —** the article applies an established **ReaxFF** parametrization for these **CHNO** propellant chemistries (development cited in **`pdf_path`**) rather than reporting a new fit in this publication.

## Findings

**Outcomes / mechanisms:** **MMH–NTO** releases energy more rapidly than **EtOH–NTO** upon mixing in the **ReaxFF** trajectories, with early chemistry dominated by **hydrogen abstraction** and **N–N bond scission** for **MMH–NTO**. **NO\(_2\)**-containing fragments **diffuse** into the **fuel** region, coupling **mixing** with **reactivity** in the authors’ interpretation.

**Comparisons:** **Hypergolic** **MMH–NTO** is compared **versus** **reactive but nonhypergolic** **EtOH–NTO** using the same **NTO** oxidizer, enabling a fuel-controlled comparison at the **liquid–liquid** interface (see experimental motivation cited in the article).

**Sensitivity / design levers:** **Temperature** (production sweeps up to **3000 K**), **interfacial area** (small vs large interface cells), and **initial density/packing** variants modulate how quickly **potential energy** drops and how **reaction channels** accumulate at early times.

**Limitations / outlook (as authored in abstract/discussion):** **ReaxFF** remains an empirical reactive model; **ps**-scale **MD** cannot capture full **engine** **fluid** **mixing** or **additive** chemistry—see **`pdf_path`** for caveats.

**Corpus / KB honesty:** Grounded in **`pdf_path`** and `normalized/extracts/2012liu-venue-jp308351g_p1-2.txt` (short excerpt); quantitative **reaction-event** statistics and figures should be read from the **PDF**.

## Limitations

**ReaxFF** chemistry and **finite** system/**time** sampling; **propellant** realism (additives, kinetics beyond early **ps**) not fully captured in a single interface study.

## Relevance to group

Co-authored **Adri C. T. van Duin**; **ReaxFF** application to **energetic** **liquid** **combustion** interfaces.

## Citations and evidence anchors

- DOI **10.1021/jp308351g** — *J. Phys. Chem. B* **116**, 14136–14145 (2012).
- Extract: `normalized/extracts/2012liu-venue-jp308351g_p1-2.txt`.

## Related topics

- [[reaxff-family]]
