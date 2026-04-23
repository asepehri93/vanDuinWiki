---
id: paper:2019arash-khajeh-acs-effect-ambient
type: paper
title: Effect of Ambient Chemistry on Friction at the Basal Plane of Graphite
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:mechanics-tribology
- domain:carbon-hydrocarbon
- material:graphene-carbon-nano
- method:reaxff
- task:experiment-integrated
- scale:atomistic
candidate_tags: []
paper_keywords:
- keyword:tribology
- keyword:graphene-carbon
- keyword:reactive-md
- keyword:lammps
- keyword:validation-experiment
source_refs: []
doi: 10.1021/acsami.9b13261
year: 2019
authors:
- Arash Khajeh, Zhe Chen, Seong H. Kim, and Ashlie Martini
venue: ACS Appl. Mater. Interfaces 2019.11:40800-40807
pdf_sha256: ca364356edf7f9538644c89aec0df35010b3b8a6f20d9ee9b173fa65ced6758c
pdf_path: papers/ReaxFF_others/Effect of Ambient Chemistry on Friction at the Basal
  Plane of Graphite.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2019arash-khajeh-acs-effect-ambient -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **ACS Appl. Mater. Interfaces** DOI `10.1021/acsami.9b13261` and `normalized/extracts/2019arash-khajeh-acs-effect-ambient_p1-2.txt`.

## Summary

**Graphite** is a common **solid lubricant** owing to **layered** **shear**, but **ambient chemistry** strongly perturbs **friction**—contrasting **vacuum/dry** vs **humid** or **organic** environments in prior work. This paper compares **phenol** vs **n-pentanol** **vapor** using **AFM** and **ReaxFF** **reactive MD** on the **basal plane**. **Experiments** and **simulations** both show **higher friction with phenol** than **pentanol**. The authors test multiple mechanistic hypotheses in simulation and argue that **mechanically driven chemical bonding** between the **tip** and **phenol** is critical: bonding **raises** the **number of phenol-derived molecules** in contact, **increases adhesion**, and increases **registry/pinning** of atoms with the **top graphene** sheet—boosting **resistance to sliding** relative to **pentanol**. The **introduction** situates the study within broader observations that **graphite lubricity** is **not intrinsic** but **environment-coupled**, citing **vacuum/dry** **high friction** vs **molecular** **adsorbate** **low friction** trends observed from **macroscale** tests through **AFM** and **atomistic** simulations. **Together**, the **experimental** and **computational** lines aim to show that **organic** **vapor** chemistry can **reorder** **friction** rankings even when **bulk** **graphite** **structure** is unchanged—an important **practical** point for **sealed** **tribological** systems using **graphitic** **coatings**.

## Methods

### Atomic force microscopy

- **Silica** AFM tip on the **graphite basal plane** with controlled **organic vapor** environments, comparing **phenol (C₆H₅OH)** vs **n-pentanol (C₅H₁₁OH)**—selected to contrast **aromatic** vs **linear aliphatic** alcohol chemistry at comparable hydroxyl functionality (article Introduction/Methods).
- **Friction** reported as a function of **normal load** for each vapor condition; experimental trends are compared directly with the reactive MD workflow described in the article.

### Reactive molecular dynamics (ReaxFF)

The authors model an **amorphous silica AFM tip** on a **graphite basal plane** with adsorbed **phenol** vs **n-pentanol**, using the same **ReaxFF** parameterization lineage described in the article (**C/O/H/Si/F**-class parametrization with literature-mapped components).

**Engine / code:** **N/A —** the main-text PDF extraction used for this curation pass does not spell out the MD engine name explicitly (community **ReaxFF** workflows are commonly **LAMMPS**-driven; confirm in the article/SI if engine naming is required for reproducibility).

**System, periodicity, loads, and contact pressures.** The setup is a **periodic** reactive MD cell representing **vapor-phase adsorbates** on **graphite** under **tip sliding**; the article reports using **contact pressure** estimates in the **~5.0–8.1 GPa** range (as quoted in the **Methods** discussion) to overlap **AFM**-relevant loads.

**Ensemble, temperature, timestep, thermostat.** Simulations are run in the **canonical (NVT-like) ensemble** at **300 K** using a **Langevin thermostat** on **unconstrained** atoms, with **sliding-direction motion excluded** from the thermostat’s kinetic temperature estimate due to high **sliding velocity**. **Timestep:** **0.25 fs**. **Thermostat damping:** **20 fs**. **Barostat / hydrostatic stress servo:** **N/A — constant-volume** thermal sampling is used (no **NPT** barostat in the excerpted protocol).

**Stages / duration.** The paper analyzes **steady-state sliding** segments (e.g., averaging over the **last ~2 nm** of sliding for registry/contact metrics) and also discusses shorter windows such as **~0.1 ns** averages for **bond-count** analyses at multiple loads; full equilibration/sliding schedule details are in the article/SI.

**Electric fields / enhanced sampling.** **N/A —** no applied **electric field** biasing or **metadynamics/umbrella** workflow is part of the summarized friction protocol.

**Electrostatics / QEq.** **Charge equilibration (QEq)** and **ReaxFF** nonbonded/cutoff conventions follow the cited parameterization and software settings documented in the **Methods/SI** (not re-tabulated here).
## Findings

- **Experiments and ReaxFF MD agree:** friction is **higher with phenol than with n-pentanol** under the compared vapor conditions.
- The authors’ simulation analysis favors **mechanically driven chemical bonding between the tip and phenol** as a central distinction: bonding **increases the number of phenol-derived molecules participating in the contact**, raises **adhesion**, and increases the population of interfacial atoms **in registry** with the top graphene sheet—acting as **pinning sites** that **raise sliding resistance** relative to pentanol.
- The **Introduction** situates this pair study within broader literature showing **graphite lubricity is environment-coupled** (e.g., vacuum/dry vs humid air; defect–tip interactions; water roles at basal planes vs defects)—this page does not restate every cited comparison; use the PDF for quantitative humidity/vapor partial-pressure tables.

## Limitations

**ReaxFF** **organic** chemistry and **tip** **geometry** are **approximate**; **single** **alcohol** pair may not span all **industrial** **vapor** mixtures. **AFM** **experiments** integrate **multiple** **asperities** and **humidity** **backgrounds** not always replicated in **simulation** cells—interpret **quantitative** **friction** agreement as **semi-quantitative** unless the **SI** documents **full** **vapor** **activities**. **This wiki entry** paraphrases **abstract** and **introduction** excerpts plus the **stated** **simulation** conclusions—verify **numbers** in the **PDF**.

## Relevance to group

**Penn State** co-authorship (**Kim**, **Martini**) ties the study to the corpus **tribology** cluster using **ReaxFF** for **graphitic** **interfaces**. The **phenol vs pentanol** comparison is a concrete **organic-vapor** counterpart to broader literature on **humidity**-dependent **graphite** friction, helping **disambiguate** **physisorption**-dominated vs **chemically activated** mechanisms in **AFM** models.

## Citations and evidence anchors

- https://doi.org/10.1021/acsami.9b13261 — `papers/ReaxFF_others/Effect of Ambient Chemistry on Friction at the Basal Plane of Graphite.pdf`; extract `normalized/extracts/2019arash-khajeh-acs-effect-ambient_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[theme-2d-epitaxy-growth]]
