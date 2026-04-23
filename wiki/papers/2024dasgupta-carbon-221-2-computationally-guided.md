---
id: paper:2024dasgupta-carbon-221-2-computationally-guided
type: paper
title: "Computationally guided synthesis of carbon coated mesoporous silica materials"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - material:silicate-glass
  - method:reaxff
  - method:classical-md
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:silica-silicate
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2024.118891"
year: 2024
authors:
  - "Nabankur Dasgupta"
  - "Qian Mao"
  - "Adri C. T. van Duin"
venue: "Carbon 221 (2024) 118891"
pdf_sha256: "631d87774036b5ade2922dc6331699d13a03f6e9f1022ebff120548ec7f2b989"
pdf_path: "papers/Dagupta_Mao_mesopores_Carbon_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024dasgupta-carbon-221-2-computationally-guided -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow ***Carbon*** **221**, **118891** (**DOI** in front matter). Percentages and temperature programs are quoted from the **abstract**/article and should be checked against **tables**.

## Summary

The article builds a **computationally guided** picture of **mesoporous silica** formation and subsequent **high-temperature carbonization** of **hydrocarbon** precursors confined in **pores**, motivated by **biomedical** durability scenarios where **carbon** coatings can **heal** or **protect** **silica** frameworks. The workflow combines **classical MD** of **Pluronic L64** self-assembly in **water** (non-reactive) with **bond-boosted ReaxFF MD** for **silicic acid** condensation to mimic **mesostructure** development, then simulates **pyrolysis** of several **hydrocarbon** models (**polyethylene**, **lignite**, **sucrose**, and a **PET**-like structure) inside **silica** confinement at **2200–2600 K**, monitoring **six-membered ring** formation and **gas** evolution.

## Methods

### Micelle self-assembly (classical MD)

**Pluronic L64** + **water**; **H-bond** statistics between **hydrophilic** blocks and **water**.

### Silica polymerization (ReaxFF + bond boost)

**ReaxFF** with **bond boosting** at **300 K**; **1500 K** **unboosted** segments; **Si(OH)\(_4\)** addition protocols per *Carbon* **221** **118891**.

### In-pore carbonization (ReaxFF, high T)

**2200–2600 K** reactive runs on **PE**, **lignite**, **sucrose**, **PET**-like precursors—**sp²**, **H\(_2\)**, **turbostratic** signatures.

**MD application (ReaxFF + bond boost, classical micelles).** **Molecular dynamics** in **LAMMPS**: **NVT**/**NPT**-segmented **periodic** supercells; **classical** **force field** (non-reactive block) for **Pluronic L64**+**water** as named in the **article**; **ReaxFF**+**bond boost** for **silicic** **acid** **condensation** at **300 K**; **unboosted** **1500 K** **NVT**; **NVT** **heating** to **2200**–**2600 K** for **confined** **pyrolysis**. **Time step** (fs), **Nosé–Hoover** **thermostat**, **ps**/**ns** **stages**—*Carbon* **221**; **N/A**—**external** **E-field**; **bond** **boost** covers **rare** **reactive** **events**; **Hydrostatic** **pressure** **N/A** unless a **NPT** segment is used—**Methods** in **`papers/Dagupta_Mao_mesopores_Carbon_2024.pdf`**. **System** size and **Si/O/C/H** **atom** counts: **article**.

## Findings

**Outcomes and mechanisms (micelle → silica → pyrolysis).** In the **classical** **Pluronic**+**water** block, **~80%** of **H-bonds** link **hydrophilic** **micelle** blocks to **water**, supporting the self-assembly picture used to template **confinement**. In the **ReaxFF** **silicic**-**acid** **condensation** block, **>60%** of the **addition** sequences tested give **periodic** **mesoporous**-like **order**; **1500 K** **unboosted** runs **double** the **polymerization** **rate** relative to **300 K** **boosted** runs, highlighting **bond-boost** **artifacts** that must be read next to the **unboosted** **reference** **segments**. In the **high-**T **pyrolysis** block, **polyethylene** and **high-rank lignite** **carbon** **precursors** most readily form **turbostratic** **graphene**-like **carbon** in **pores**; **sucrose** gives the **least** **planar** **sp²** **content** in the **comparison** shown. A **PET**-like **trajectory** **produces** a **tar** that **coats** **pore** **openings** and can **block** **silicic** **acid** **ingress**—a **failure** **mode** for **continued** **condensation**.

**Comparisons, sensitivity, limitations (as presented).** The work **compares** **O/C/H**-rich **feeds** across **PE**, **lignite**, **sucrose**, and **PET**-like **cases**; **sensitivity** to **temperature** spans **room-temperature**-scale **condensation** through **2200**–**2600** **K** **pyrolysis** windows. **Open** **questions** include how **laboratory** **carbonization** maps to these **extreme-**T **toy** **models**—see **## Limitations**. **Corpus honesty:** a **proof**-PDF **sibling** exists as **`[[2024dagupta-venue-paper]]`**; cite **`paper:2024dasgupta-carbon-221-2-computationally-guided`** for the **version-of-record** **DOI** `10.1016/j.carbon.2024.118891`.

## Limitations

**Bond boosting** accelerates rare events—validate against **unboosted** segments and **QM** where provided. **Pyrolysis** temperatures are extreme relative to laboratory **carbonization**; qualitative **mechanism** insight is the primary output.

The **multi-precursor** comparison (**PE**, **lignite**, **sucrose**, **PET**-like) is the paper’s practical hook for **materials** design: different **O/C/H** compositions yield different **H₂** release, **sp²** development, and **tar** behavior inside **pores**, which matters when **coatings** must **block** further **silicic acid** transport versus allowing it.

## Relevance to group

**van Duin**-affiliated work combining **ReaxFF** **silica** **polycondensation** with **confined** **pyrolysis**, aligned with **biomaterials-adjacent** **carbon–oxide** processing themes.

The **Pluronic** self-assembly stage (classical **MD**) and the **ReaxFF** **silica** stage are intentionally **multiscale**: agents should not attribute **mesopore** metrics from the classical block to the reactive block without checking which section generated which structural claim.

## Citations and evidence anchors

- DOI [10.1016/j.carbon.2024.118891](https://doi.org/10.1016/j.carbon.2024.118891).
- Excerpt alignment: `normalized/extracts/2024dasgupta-carbon-221-2-computationally-guided_p1-2.txt`.

## MAS / retrieval

Group-affiliated **`paper:`** with **`keyword:polymer`** + **`keyword:silica-silicate`** supports **biomaterials**/**mesopore** queries that span **classical** self-assembly and **ReaxFF** **condensation**.

## Related topics

- [[reaxff-family]]
