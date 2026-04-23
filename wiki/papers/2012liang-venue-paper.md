---
id: paper:2012liang-venue-paper
type: paper
title: "Erratum: Parametrization of a reactive many-body potential for Mo–S systems [Phys. Rev. B 79, 245110 (2009)]"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:classical-ff-specialized
  - material:tmd
  - method:classical-md
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:lammps
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.85.199903"
year: 2012
authors:
  - "Tao Liang"
  - "Simon R. Phillpot"
  - "Susan B. Sinnott"
venue: "Physical Review B 85, 199903(E) (2012)"
pdf_sha256: "1c0a9f9a21ce76ce8455d240b1c14f614d12efc14cc02c0571ccea9b3b65de97"
pdf_path: "papers/Others/Liang_MoS2_PRB_erratum_PhysRevB.85.199903.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2012liang-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **erratum** corrects **implementation** issues discovered when coding the authors’ **Mo–S reactive many-body potential** into **LAMMPS**. It supplies **revised short-range pairwise parameters** and **Lennard-Jones** parameters for **Mo–Mo**, **S–S**, and **Mo–S**, replaces the **LJ** tail with a **cubic spline** beyond **0.95σ** to avoid an **excessively repulsive wall**, and fixes a misprinted **elastic constant** \(c_{12}\) for **bcc Mo** in the original paper (**correct value 189 GPa**). Additional **many-body** tables omitted originally are provided so third-party codes can reproduce the model. **MoS\(_2\)** **\(c_{11}\)** and **bulk modulus** values shift upward modestly after the correction (reported as **261 GPa** and **81 GPa** vs **242 GPa** and **75 GPa** respectively in the erratum text).

## Methods


This **erratum** supplies **corrected short-range pairwise parameters** and **Lennard–Jones (LJ)** parameters for **Mo–Mo**, **S–S**, and **Mo–S** interactions for implementation in **LAMMPS**, and corrects a misprinted **elastic constant** \(c_{12}\) for **bcc Mo** in the parent paper (**correct value 189 GPa**, consistent with the bulk modulus relation \(B=(c_{11}+2c_{12})/3\)). To avoid an **overly repulsive LJ wall**, the LJ tail is replaced by a **cubic spline** beginning at **0.95σ** (with σ the LJ diameter parameter) to smoothly terminate **van der Waals** interactions by the inner cutoff radii \(R_\mathrm{min}\). The erratum also publishes **many-body** tables omitted originally (coordination and sixth-order angular terms) plus an added **γ[cos θ]** term for **S** angles, needed for faithful reproduction of the potential. The corrections were developed cooperatively with **University of Arkansas** (**Stewart**, **Spearot**) LAMMPS implementation testing.

### Force-field training (Mo–S reactive many-body; erratum to PRB 2009)

**Parent FF / elements:** Corrected **short-range pairwise** terms and **Lennard–Jones** parameters for **Mo–Mo**, **S–S**, and **Mo–S** within the authors’ **Mo–S reactive many-body** framework as originally published (**Phys. Rev. B** **79**, 245110 (2009)); this erratum supplies tables needed for faithful **LAMMPS** implementation.

**QM reference:** **N/A —** new **DFT** benchmarks are not the focus of the erratum; the parent paper’s **QM** training context applies (see parent DOI in **Citations**).

**Training set / reference data:** **N/A —** additional training structures beyond the parent work are not introduced here; the erratum instead fixes implementation quantities and publishes omitted tables.

**Optimization:** **N/A —** no new global **optimization** campaign is reported in the erratum text (see parent publication for the original fit).

**Reference data used:** **Elastic** diagnostics at **300 K** (**MoS\(_2\)** **\(c_{33}\)** at **52 GPa**) motivate adjusting **S–S** **LJ** **ε**; revised **\(c_{11}\)**/**bulk modulus** for **MoS\(_2\)** are quoted after the **LJ**/**spline** fixes (**261 GPa** / **81 GPa** vs **242 GPa** / **75 GPa**).

### MD application (implementation note; no new trajectories in the erratum)

**Engine / code:** **LAMMPS** is the stated integration target for the corrected **Mo–S** potential forms.

**System size & composition:** **N/A —** no new **MD** supercell sizes or **stoichiometries** are reported in the erratum itself; users choose **composition** when applying the corrected tables to **Mo**, **S**, and **MoS\(_2\)** models.

**Boundaries / periodicity:** **Periodic** **bulk** and **lamellar MoS\(_2\)** contexts motivate the **long-range vdW** **LJ**/**spline** fix; explicit user **PBC** choices are **N/A —** outside the erratum’s scope.

**Ensemble / thermostat / timestep / duration:** **N/A —** the erratum does not specify **NVT**/**NPT** production settings, **thermostats**, **timesteps**, or **ps**/**ns** trajectory lengths (those belong to downstream application studies using the corrected potential).

**Barostat / pressure control:** **N/A —** not specified in the erratum beyond **elastic** property benchmarking language.

**Temperature:** **300 K** appears when discussing reproducing **MoS\(_2\)** **\(c_{33}\)** after adjusting **LJ** parameters.

**Pressure / stress:** **Elastic constants** (**GPa** scale) are used to discuss mechanical property shifts after the correction.

**Electric field:** **N/A —** not applicable.

**Replica / enhanced sampling:** **N/A —** not applicable.

## Findings

**Outcomes / mechanisms:** The authors state that revised **\(R_\mathrm{min}\)**, **\(R_\mathrm{max}\)**, and **LJ** parameters **do not materially change** strong **short-range** energetics or most **mechanical** predictions for **Mo**, **S**, and **MoS\(_2\)** relative to the original publication, while improving **long-range vdW** behavior in **lamellar MoS\(_2\)** via the **cubic spline** tail starting at **0.95σ**.

**Comparisons:** After correction, predicted **\(c_{11}\)** and **bulk modulus** for **MoS\(_2\)** **increase** to **261 GPa** and **81 GPa**, respectively, from **242 GPa** and **75 GPa** in the original table (as quoted in the erratum).

**Sensitivity / design levers:** The erratum notes that **short-range cutoffs** and **LJ** parameters may need adjustment depending on the **system** class being simulated (it cites analogous cutoff practices for **REBO** carbon nanotube fracture studies).

**Limitations / outlook (authored tone):** The piece is explicitly an **erratum** correcting implementation issues discovered during **LAMMPS** coding; users must merge these tables to avoid spurious **long-range** forces and misprinted **elastic** data.

**Corpus / KB honesty:** Grounded in **`pdf_path`** and `normalized/extracts/2012liang-venue-paper_p1-2.txt` (short excerpt); full parent-paper context lives at **Phys. Rev. B** **79**, 245110.

## Limitations

- Users of the **2009 PRB** paper must **merge** this erratum or risk **incorrect long-range** forces and **elastic** constants.

## Relevance to group

**MoS\(_2\)** **classical reactive** potential corrections relevant alongside **TMD** and **nanocarbon** mechanics papers in the corpus.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevB.85.199903](https://doi.org/10.1103/PhysRevB.85.199903)
- Parent potential paper: [10.1103/PhysRevB.79.245110](https://doi.org/10.1103/PhysRevB.79.245110)
- Text-aligned pointer: `normalized/extracts/2012liang-venue-paper_p1-2.txt`

## Related topics

- Transition metal dichalcogenide (TMD) classical potentials
- [[reaxff-family]] (contrast: Mo–S many-body potential line)
