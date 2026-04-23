---
id: paper:2017bentria-acta-materia-role-emerging
type: paper
title: "The role of emerging grain boundary at iron surface, temperature and hydrogen on metal dusting initiation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:catalysis-surfaces
  - method:reaxff
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:metallic-systems
  - keyword:catalysis-surface
candidate_tags: []
source_refs: []
doi: "10.1016/j.actamat.2017.06.049"
year: 2017
authors:
  - "El Tayeb Bentria"
  - "Gawonou K. N'tsouaglo"
  - "Charlotte S. Becquart"
  - "Othmane Bouhali"
  - "Normand Mousseau"
  - "Fedwa El-Mellouhi"
venue: "Acta Mater."
pdf_sha256: "edbe7909d319632b9abdc6c7e5cc0364b7c69a45dbe28da5e6dd2125f3a7e383"
pdf_path: "papers/ReaxFF_others/Bentria_ActaMateriala_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017bentria-acta-materia-role-emerging -->

## Summary

**Metal dusting** corrodes **Fe**-based alloys in **carbon-supersaturated**, **high-temperature** gases, often initiating at **microstructural defects** where **carbon** activity and **surface** mobility differ from terraces. Bentria *et al.* combine **DFT** with **ReaxFF MD** on **iron** models that include **emerging grain boundaries** and **groove** geometries under **CO-rich** environments representative of dusting exposures. The study targets **CO dissociation** as a gate to **carbon** uptake and emphasizes how **boundary** **topography** steers **local** reactivity. The **Acta Materialia** article is explicitly aimed at **engineering** **metal dusting** risk where **CO** and **hydrocarbon** feeds interact with **defective** **Fe** surfaces.

## Methods

**Static QM (DFT).** The authors compare **carbon adsorption** site preference and **relative stabilization** on **flat bcc-Fe** terraces versus **groove** motifs built where an **emerging grain boundary** meets a **free surface** (including **missing Fe rows** to mimic local damage). The DFT block is used to argue that **grooves** provide **preferential C binding** relative to neighboring smooth regions.

**MD application (ReaxFF).** **Reactive MD** uses a **2016 Fe/C/O/H ReaxFF** parameterization from the **van Duin** lineage (cited as fitted to DFT and experiment for **C–O–H** chemistry on **bcc-Fe**). **Supercells** span **Σ3** and **Σ5** **emerging** grain boundaries terminating at **(111)** and **(210)** surfaces, again with **groove** constructs at the **GB–surface** junction. **Gas environments** feature **CO**, with **H\(_2\)** added in some runs so the authors can separate **H** as a **CO-dissociation promoter** versus **H** reacting with **dissociated C** (hydrocarbon product channels). **Temperature** is scanned to count **CO dissociation** and **recombination** events and to compare **groove** vs **non-groove** segments of the same boundary models.

**Force-field training** is **N/A**: the paper **adopts** the published **ReaxFF** set rather than refitting.

**Protocol numerics** (**MD code**, **ensemble**, **timestep**, **thermostat/barostat**, **total simulated time**, **full atom counts**, **PBC** vectors, **pressure control**, **electric fields**, **enhanced sampling**) are specified in the *Acta Mater.* **Computational methods**; this wiki page does **not** transcribe those tables from the short front-matter extract—consult the **PDF** for reproducibility.

**MD blueprint honesty (not substitute for the PDF).** **PBC** applies to the **bcc-Fe** **slab** and **grain-boundary** supercells. The manuscript names the **MD engine** (community default for this lineage is **LAMMPS** with **ReaxFF**—verify wording in *Acta Mater.*). **Ensemble** (**NVT** vs **NPT** vs **NVE**), **timestep**, **thermostat**, **barostat** usage (if any), **target pressure** for **NPT**, **equilibration**/**production** durations (**ps**/**ns**), and **electric-field**/**enhanced-sampling** controls are **N/A** on this page because they are not recoverable from the short indexed excerpt—copy them from the primary **PDF**.

## Findings

**Grooves** stabilize **carbon** more strongly than neighboring **terraces** in the **DFT** data, providing a **geometric** rationale for **localized** **susceptibility** at **emerging** **boundaries**. **ReaxFF** trajectories report **faster CO dissociation** inside **groove** regions than on smoother segments of the same **boundary** models. **Hydrogen** plays a **dual** role: it **promotes** **CO** **scission** under some conditions while also **scavenging** **carbon** through **hydrocarbon** product channels, yielding **temperature-dependent** trends that the authors connect—within their modeling assumptions—to **measured** **metal dusting** kinetics. The **abstract** further argues that, after **characterizing mechanisms** versus **reactant content**, the modeled **CO dissociation** response to **temperature** can be placed in **linear correspondence** with **experimental metal dusting rates**—an explicit attempt to bridge **atomistic** kinetics with **engineering** corrosion observables. The **Introduction** situates **metal dusting** in **carbon-rich** gases (including **CO** and **hydrocarbons**) at roughly **600–1100 K**, where **hydrocarbon dissociation**, **subsurface carbon** uptake, and eventual **cementite** formation drive **powdering** of **Fe** alloys; the modeling focus on **grooved** **grain-boundary** exits is motivated as a **preferential** initiation locus within that broader mechanism picture.

## Limitations

Iron **ReaxFF** quality is system- and parameterization-dependent; quantitative rates should be validated against the article’s uncertainty discussion. **Idealized** **surface** models omit **oxide** spallation, **sulfur** poisoning, and **long-time** **microstructure** evolution present in industrial **dusting** exposures. Coupling to **continuum** **CFD** **carbon activity** fields would be needed for plant-scale **risk** assessment beyond these **atomistic** samples.

## Relevance to group

Demonstrates **ReaxFF + DFT** workflow for **high-temperature metal corrosion** chemistry on **defective Fe** surfaces.

## Citations and evidence anchors

- DOI: `10.1016/j.actamat.2017.06.049`.

## Related topics

- [[reaxff-family]]
