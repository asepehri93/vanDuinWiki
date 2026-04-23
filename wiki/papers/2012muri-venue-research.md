---
id: paper:2012muri-venue-research
type: paper
title: "Oxygen interactions with silica surfaces: coupled cluster and density functional investigation and development of a new ReaxFF potential"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - material:silicate-glass
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:silica-silicate
  - keyword:oxide-surface
  - keyword:galley-or-proof-pdf
source_refs: []
doi: "10.1021/jp3086649"
year: 2012
authors:
  - "Kulkarni, Anant D."
  - "Truhlar, Donald G."
  - "Srinivasan, Sriram Goverapet"
  - "van Duin, Adri C. T."
  - "Norman, Paul"
  - "Schwartzentruber, Thomas E."
venue: "Journal of Physical Chemistry C"
pdf_sha256: "4a9153e6b39ca2db3b38e459a12e763d9c091bd8e80be89162b33f988d67f895"
pdf_path: "papers/MURI_team_SiOx_JPCC_2012_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2012muri-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi` and `pdf_path`. The corpus filename suggests a **galley** PDF; pagination may differ from the final issue.

## Summary

**CCSD(T)-F12b** and **Minnesota density functionals** supply **cluster** energies for **atomic** and **molecular oxygen** approaching **nondefective** and **defective** **silica** surface motifs (including **under-coordinated Si**, **nonbridging O**, and **ring** defects). **DFT** binding energies extend a **ReaxFF SiO** parametrization—previously for **bulk** **silica** polymorphs—to **gas–surface** **oxygen–silica** interactions (**ReaxFF SiO_GSI** in the paper). **ReaxFF** binding energies are reported to agree well with **DFT** for the training structures, enabling large-scale **reactive MD** of **oxygen–silica** processes (e.g. **oxide growth**, **heterogeneous O recombination**).

## Methods


**QM training data:** **Cluster** models represent **experimentally motivated** **nondefective** **silica** motifs (sites above **four-coordinate** surface **Si**, **bridging** **O**) and **defective** motifs (**under-coordinated Si**, **nonbridging oxygen**, **ring** defects). **Energies** for **atomic** and **molecular** **O** approaching these clusters in multiple **geometries** were computed with **explicitly correlated** **CCSD(T)-F12b** and with **Minnesota** **density functionals**, reported as mutually consistent. **DFT** **binding energies** were then computed for **all** clusters, including **singlet/triplet** states for **nondefective** clusters and **doublet/quartet** manifolds for **defective** clusters.

**ReaxFF extension:** The bulk **silica** **ReaxFF** of **van Duin et al.** (*J. Phys. Chem. A* **2003**) is extended to **gas-surface** **oxygen-silica** interactions (**ReaxFF SiO_GSI**) with **Coulomb** taper (**10 A** cutoff noted in Section 2.2) and **EEM**-style charges as in standard **ReaxFF** **SiO**. Training uses **cluster** cuts from **(001)** **reconstructed** **alpha-quartz** (cleave, **Chen et al.** procedure plus **ReaxFF** **relax**), covering **bridging-O** and **four-coordinate Si** sites (**S1**, **B1**) and **defect** motifs (**nonbridging oxygen**, **under-coordinated Si**); **O** and **O2** approaches include multiple **orientations** (**perpendicular**/**parallel** to the surface in **T4**-type clusters).

**MD role:** The parametrization targets **large-scale** **reactive MD** of **O**/**O\(_2\)** at **silica** **interfaces** (e.g. **oxidation**, **recombination**), but the **indexed excerpt** centers on **QM** benchmarks and **ReaxFF** fitting—not new production trajectories.

### MD application (large-scale reactive MD; forward-looking)

**N/A — production trajectories:** the excerpted pages emphasize **cluster QM**, **DFT binding energies**, and **ReaxFF** extension rather than reporting a new **MD** protocol with tabulated **timesteps**, **ensembles**, and **run lengths**.

**Engine / code:** **N/A —** no **LAMMPS**/package identifier is tied to an executed **MD** benchmark in the indexed excerpt (see **`pdf_path`** for any downstream validation examples).

**System size & composition:** **Cluster** cuts from **(001)** **α-quartz**-derived motifs (**S1**, **B1**, defects) plus **O**/**O\(_2\)** approaches—**atom** counts per cluster are in **`pdf_path`**, not duplicated here.

**Boundaries / periodicity:** **Cluster** models for **QM**; **N/A —** **PBC** **MD** supercells are not specified in the indexed excerpt.

**Ensemble / timestep / duration / thermostat:** **N/A —** **NVE**/**NVT**/**NPT** assignments for any large-scale **MD** validation runs are not stated in the indexed excerpt (confirm in **`pdf_path`** if such runs are reported beyond the **QM**/fitting focus).

**Barostat / pressure control:** **N/A —** not stated for **MD** in the indexed excerpt.

**Temperature:** **N/A —** explicit **MD** thermostat temperatures or gas-surface dynamics temperatures are not recovered from `normalized/extracts/2012muri-venue-research_p1-2.txt` (see **`pdf_path`** for any follow-on **MD** validation).

**Pressure / stress:** **N/A —** not a controlled **MD** variable in the indexed excerpt.

**Electric field:** **N/A —** not used in the quoted **MD** forward look.

**Replica / enhanced sampling:** **N/A —** not used.

### Force-field training (ReaxFF SiO_GSI extension)

**Parent FF / elements:** Extends the bulk **silica** **ReaxFF SiO** parametrization of **van Duin et al.** (*J. Phys. Chem. A* **2003**) to **gas–surface** **oxygen–silica** interactions (**ReaxFF SiO_GSI**), retaining **EEM**-style charges and adding a **Coulomb** taper with a **10 Å** cutoff (Section 2.2 in **`pdf_path`**).

**QM reference:** **CCSD(T)-F12b** and **Minnesota** **DFT** functionals on finite **cluster** models; **DFT** binding energies for **O**/**O\(_2\)** approaches across **spin** manifolds as summarized above.

**Training set / reference data:** **Cluster** geometries for **nondefective** and **defective** **silica** motifs, including **O**/**O\(_2\)** approach orientations drawn from **(001)** **α-quartz**-derived cuts.

**Optimization:** **N/A —** detailed **least-squares** / **ParReaxFF** optimization workflow is not excerpted on pages **1–2**; see **`pdf_path`** for the full fitting protocol.

**Reference data used:** **CCSD(T)-F12b**, **Minnesota DFT**, and extended **DFT** binding sets used to train/score **ReaxFF SiO_GSI** against **QM** trends.

## Findings

**Outcomes / mechanisms:** **Defective** **cluster** motifs bind **atomic** and **molecular** **oxygen** more strongly than **nondefective** surface motifs in the **QM** training set. **ReaxFF SiO_GSI** reproduces the **DFT** binding trends on those **clusters**, supporting its intended use in **reactive** **O/O\(_2\)** + **silica** **MD** for **oxidation** and **heterogeneous recombination** problems.

**Comparisons:** **CCSD(T)-F12b** and **Minnesota** **DFT** are reported as mutually consistent on the sampled **clusters**; **ReaxFF** is compared directly to the **DFT** binding energies used for training.

**Sensitivity / design levers:** **Defect** type (**under-coordinated Si**, **nonbridging oxygen**, **ring** defects) shifts **O**/**O\(_2\)** binding strengths relative to **bridging**/**four-coordinate** sites.

**Limitations / outlook (authored tone):** **Cluster** models approximate **gas–surface** motifs; transferability to full **reconstructed** surfaces and **finite-temperature** dynamics requires additional validation beyond the excerpted pages.

**Corpus / KB honesty:** `pdf_path` points to a **galley** filename; pagination may differ from the **version of record**. Summaries lean on **`pdf_path`** plus `normalized/extracts/2012muri-venue-research_p1-2.txt` (short extract).

## Limitations

**Cluster** models and **galley** PDF; **ReaxFF** transferability to full **reconstructed** **surfaces** at **temperature** requires separate validation.

## Relevance to group

**Adri C. T. van Duin** coauthored **ReaxFF** extension for **silica** **gas–surface** **oxygen** chemistry—central to **aerospace**/**plasma**/**microelectronics** contexts cited in the paper.

## Citations and evidence anchors

- DOI **10.1021/jp3086649** — *J. Phys. Chem. C* (volume/pages per publisher record).
- PDF: `papers/MURI_team_SiOx_JPCC_2012_galley.pdf`; extract: `normalized/extracts/2012muri-venue-research_p1-2.txt`.

## Related topics

- [[reaxff-family]]