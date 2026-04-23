---
id: paper:2012r-paupitz-venue-graphene-fluorographene
type: paper
title: "Graphene to fluorographene and fluorographane: a theoretical study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:2d-materials
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:reactive-md
source_refs: []
doi: "10.1088/0957-4484/24/3/035706"
year: 2012
authors:
  - "Paupitz, R."
  - "Autreto, P. A. S."
  - "Legoas, S. B."
  - "Srinivasan, S. Goverapet"
  - "van Duin, Adri C. T."
  - "Galvão, D. S."
venue: "Nanotechnology"
pdf_sha256: "b20663f90062f8af612a20835552fd60442142678ca3c9118923407b396b24b9"
pdf_path: "papers/Paupitz_F_Graphene_Nanotech_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2012r-paupitz-venue-graphene-fluorographene -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. Journal **year** on PDF may read **2013** while bibliographic **year** is retained as in `normalized/papers` (**2012** receipt).

## Summary

**Reactive MD** with **ReaxFF** examines **fluorination** of **graphene** membranes toward **fluorographene**. The abstract reports **defective** regions with **C–C** **distortion**, **hole** formation and **C loss** at higher **F** loadings (linked to scattered **lattice** parameters in experiment), **H/F** **co-functionalization** kinetics (**H** slowing **F** incorporation at low **H**; **F** catalyzing **H** incorporation when **F** is minority), and spontaneous **hybrid** **chair/zigzag/boat-like** structures termed **fluorographane**.

The study targets synthesis-relevant questions—how halogen coverage develops on large sheets and when disorder overwhelms ordered stoichiometric fluorographene—rather than small-cluster reaction barriers alone.

## Methods


**Code:** **ReaxFF** in **LAMMPS**. **Membranes:** initial **graphene** sheets **~160 A x 160 A** (**~10 000 C**). **Atmosphere:** pure **F** or mixed **F/H** with **atom** counts up to **~2x** **C**, **random** placement on **both** **faces**; **constant-volume** cell. **Integration:** **Delta t = 1.0 fs** (smaller **dt** checks reported **consistent**); **Langevin** thermostat; **typical** **run** **length** **~1.0 ns** (**~10^6** **steps**). **DFT** benchmarks in the paper compare **ReaxFF** to **DFT** for **selected** **C-F** **dissociation** and **angle**/**torsion** cuts (**Figure 2**). **Bibliographic** **year** **2012** vs **Nanotechnology** **2013** **volume** on the **PDF** is a **publisher** **dating** **mismatch**.

Random dual-sided dosing explores steric crowding and face-to-face stress accumulation that small cluster models omit.

### MD application (fluorination / mixed H/F dosing)

**Engine / code:** **ReaxFF** reactive **MD** in **LAMMPS** (Section-level description in **`pdf_path`**).

**System size & composition:** Initial **graphene** sheets about **160 Å × 160 Å** (**~10 000 C** atoms) with **F** or mixed **F/H** atmospheres up to **~2×** the **C** count, placed randomly on **both faces**.

**Boundaries / periodicity:** **Constant-volume** **supercell** (in-plane **PBC** with vacuum normal implied by the membrane setup—verify **`pdf_path`** for the exact cell).

**Ensemble:** **NVT**-style thermalization via **Langevin** dynamics at **~300 K** for the primary runs discussed in the wiki summary.

**Timestep:** **1.0 fs** (with smaller **Δt** checks reported as consistent).

**Duration / stages:** **~1.0 ns** (**~10⁶** steps) typical run length for uptake/kinetics trends.

**Thermostat:** **Langevin** thermostat; **N/A —** friction/damping constants not transcribed here—see **`pdf_path`**.

**Barostat / pressure control:** **N/A —** **NPT** barostat not used for the quoted **constant-volume** membrane runs.

**Temperature:** **~300 K** primary focus; higher **T** runs show membrane damage (see article).

**Pressure / stress:** **N/A —** external **hydrostatic pressure** control not highlighted in the excerpted summary.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not used.

### Static QM / DFT (benchmarks)

**DFT** comparisons in the article (e.g., **Figure 2**) benchmark **ReaxFF** for selected **C–F** dissociation and angle/torsion cuts; **N/A —** full **DFT** functional/basis details are not duplicated on this wiki page—read **`pdf_path`**.

### Force-field training

**N/A —** applies an established **C/H/F** **ReaxFF** parametrization with **DFT** spot checks rather than reporting a new global fit in this article.

## Findings

**Fluorination** at **~300 K** shows **fast** then **slow** **uptake** regimes toward **saturation**; **higher** **T** **damages** **membranes**, so the **paper** **focuses** on **~300 K** for **ordered** **fluorographene**. **Mixed** **H/F** runs show **H** slowing **F** at **low** **H**, but **F** (minority) can **accelerate** **H** **uptake**; **defects** and **holes** appear at **high** **F** load, and **hybrid** **chair**/**zigzag**/**boat** **fluorographane** motifs **form** **spontaneously**.

These outcomes connect to experimental variability in lattice constants: locally defective, holey membranes may coexist with ordered fluorinated domains under aggressive fluorination.

The Nanotechnology article provides additional DFT validation curves, coverage-dependent uptake plots, and discussion of hybrid allotropes beyond the short summary suitable for this wiki note.

Cross-check halogen stoichiometry and membrane sizes against the article tables before reusing these protocols in new reactive MD studies.

## Limitations

**ReaxFF** chemistry limits; **finite** **membrane** size; **kinetics** vs **synthesis** conditions.

## Relevance to group

**Adri C. T. van Duin** coauthored; **ReaxFF** on **halogenated** **graphene** with **PSU** collaboration.

## Citations and evidence anchors

- DOI **10.1088/0957-4484/24/3/035706** — *Nanotechnology* **24**, 035706 (2013).
- Extract: `normalized/extracts/2012r-paupitz-venue-graphene-fluorographene_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
