---
id: paper:2013al-venue-mechanical-properties
type: paper
title: "Mechanical properties of amorphous Li_xSi alloys: a reactive force field study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - material:li-metal-anode
  - method:reaxff
  - domain:mechanics-tribology
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:validation-experiment
  - keyword:npt-simulation
source_refs: []
doi: "10.1088/0965-0393/21/7/074002"
year: 2013
authors:
  - "Fan, Feifei"
  - "Huang, Shan"
  - "Yang, Hui"
  - "Raju, Muralikrishna"
  - "Datta, Dibakar"
  - "Shenoy, Vivek B."
  - "van Duin, Adri C. T."
  - "Zhang, Sulin"
  - "Zhu, Ting"
venue: "Modelling and Simulation in Materials Science and Engineering"
pdf_sha256: "8052682b9093bcf35ecec0514f6d7b8b01882356d7d0e1efe4af775419007b18"
pdf_path: "papers/Fan_LiSi_MechProperties_MSME_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013al-venue-mechanical-properties -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

**ReaxFF** **MD** characterizes **mechanical** response of **amorphous** **Li_xSi** (**a-Li_xSi**) relevant to **Si** **anodes**. The abstract highlights **yield** and **fracture** strengths under several **chemomechanical** loadings (**constrained thin-film lithiation**, **biaxial compression**, **uniaxial tension/compression**), **loading-sequence** and **stress-state** effects, and a **bonding** narrative from **covalent** toward **metallic-glass-like** behavior with increasing **Li** content—aimed at interpreting **experiments** and **electrode** **design**. **Silicon** **anodes** **swell** and **fracture** during **cycling**; **computational** **stress** **tests** on **lithiated** **glassy** **Si** aim to connect **atomistic** **plasticity** to **macroscopic** **failure** **metrics** used in **continuum** **damage** **models**.

## Methods


**Force field:** **new** **Li-Si** **ReaxFF** (benchmarked in **Appendix A** vs **DFT** **metrics** cited in **Section 1**). **Structures:** **a-Si** from **melt-quench**; **lithiated** **phases** by **random** **Li** **insertion** (**20** **Li** **atoms** **per** **round**) with **300 K** **relax** **10 ps** **per** **step** under **thin-film** **constraint** (**in-plane** **periodic**, **out-of-plane** **free** **expansion**). **Mechanical** **probes:** **biaxial** **compression** of **pre-lithiated** **films** (**strain** **rate** **5e8 1/s**, **300 K** in **Figure 2**/**Section 2.2**); **constrained** **thin-film** **lithiation** **stress** **vs** **x** (**Section 2.1**); additional **loading** **modes** in **Sections 2.3+** of the **PDF**.

<!-- blueprint-slot-coverage:auto -->
### MD application (blueprint slots)

**Engine / code:** **molecular dynamics** reported; **N/A — specific MD package** not named in the indexed excerpt—verify `pdf_path`.
**System size & composition:** **N/A — atom** counts / full **stoichiometry** not restated in indexed excerpt; verify **`pdf_path`**.
**Boundaries / periodicity:** **Periodic** / **bulk** language appears in indexed text; confirm **PBC** details in PDF if needed.
**N/A — ensemble** (NVE/NVT/NPT) not clearly indexed here; verify PDF.
**Timestep:** **N/A — timestep** not recovered from indexed excerpt; verify PDF.
**Duration / stages:** **ps**/**ns** scale timing or **equilibration**/**production** language appears in indexed text—see PDF for full schedule.
**N/A — thermostat** type/damping not recovered from indexed excerpt; verify PDF.
**Barostat:** **N/A — barostat** / **NPT** usage not stated in indexed excerpt; verify **`pdf_path`**.
**Temperature:** 300 K (matched in indexed text)
**Pressure / stress:** **N/A — hydrostatic pressure** / stress control not stated for the indexed MD description (often implicit in **NVT** cluster demos).
**Electric field:** **N/A — external electric field** bias not indicated in indexed excerpt for MD (if any field appears, it belongs to static QM/experiment sections).
**Replica / enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not indicated in indexed excerpt.

<!-- /blueprint-slot-coverage:auto -->

## Findings

### Findings (blueprint coverage; excerpt-grounded)

- **Outcomes / mechanisms:** Indexed text discusses **reaction**/**kinetic**/**interface**/**mechanism**-level conclusions—see PDF for full argument.
- **Comparisons:** **Experiment**/**literature**/**compared** language appears in indexed text.
- **Sensitivity / design levers:** **Temperature**/**pressure**/**strain**/**field**/**concentration** language appears in indexed text where applicable.
- **Limitations / outlook (authored tone):** **N/A — limitations** and **future work** bullets are not excerpted here; consult the discussion section in **`pdf_path`**.
- **Corpus / KB honesty:** Claims on this wiki page are tied to **`pdf_path`** and `normalized/extracts/{slug}_*.txt`; figures/tables may be **not stated** in excerpt.
**Film** **stress** during **lithiation** peaks then **softens** as **x** **increases**, tracking **plastic** **relaxation** in the **MD** **model** (**magnitudes** **above** some **nanoindentation** **values**, **attributed** to **short** **MD** **times**). **Post-lithiation** **biaxial**/**uniaxial** **tests** show **strong** **dependence** on **loading** **path** and **Li** **content**, with **bonding** **evolving** from **covalent** **network** **toward** **more** **metallic** **glass-like** **character** at **high** **Li** **loading**.

**Path** **dependence** implies **electrode** **particles** experiencing **non-monotonic** **lithiation** **histories** may **fail** at **different** **states** than **uniform** **Li** **profiles** assumed in **simple** **homogenized** **models**.

## Limitations

**ReaxFF** **accuracy** for **amorphous** **alloys**; **simulation** **strain** **rates**; **room-temperature** **electrochemical** **paths** only partially represented by **mechanical** **tests**. **Li** **flux**, **SEI** **formation**, and **concentration** **gradients** during **cycling** are not captured in the **mechanical** **probing** workflows summarized on this page. **Crystalline** **Si** **particles** with **sharp** **interfaces** may behave differently than the **homogeneous** **a-Li_xSi** **models** emphasized in the article’s **amorphous** **route**.

## Relevance to group

**Adri C. T. van Duin** coauthored **ReaxFF** **mechanics** of **lithiated** **silicon** for **battery** **interfaces**.

## Citations and evidence anchors

- DOI **10.1088/0965-0393/21/7/074002** — *Modelling Simul. Mater. Sci. Eng.* **21**, 074002 (2013).
- Extract: `normalized/extracts/2013al-venue-mechanical-properties_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]

## Reader notes (navigation)

For **Si anode mechanics**, compare with later **large-deformation ReaxFF** and **continuum-coupled** studies cited from this paper’s introduction chain.
