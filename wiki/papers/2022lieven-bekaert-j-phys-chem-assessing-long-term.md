---
id: paper:2022lieven-bekaert-j-phys-chem-assessing-long-term
type: paper
title: "Assessing the Long-Term Reactivity to Achieve Compatible Electrolyte–Electrode Interfaces for Solid-State Rechargeable Lithium Batteries Using First-Principles Calculations"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - method:aimd
  - method:dft-static
  - task:application
  - material:polymer-organic
  - material:li-metal-anode
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:aimd
  - keyword:batteries-interfaces
  - keyword:dft-static
source_refs: []
doi: "10.1021/acs.jpcc.2c01144"
year: 2022
authors:
  - "Lieven Bekaert"
  - "Ashish Raj"
  - "Jean-François Gohy"
  - "Annick Hubin"
  - "Frank De Proft"
  - "Mesfin H. Mamme"
venue: "J. Phys. Chem. C"
pdf_sha256: "a29532c96c125959cb3227a750629a1b99976cdab2ff6788b2fbd1506cee5e5f"
pdf_path: "papers/Others/Bekaert_Mamma_JPCC_2021_assesing lomg term...pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022lieven-bekaert-j-phys-chem-assessing-long-term -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

## Summary

This Journal of Physical Chemistry C article addresses a central challenge for next-generation rechargeable lithium batteries: designing electrode–electrolyte interfaces that remain compatible over long calendar life and under demanding operating conditions. The authors focus on nanoscopic interfaces involving solid polymer electrolytes in contact with negative electrodes of different reactivity—graphite, silicon, and lithium metal—because each electrode class poses distinct interfacial stability questions. The study uses ab initio molecular dynamics to obtain highly accurate interface dynamics at short times and small length scales, explicitly acknowledging that direct simulation of years-long degradation is infeasible. To bridge this timescale gap, the authors introduce an interpretational strategy based on bond-length distribution analysis for key polymer functional groups at the interface, treating shifts in these distributions under applied electric fields and temperature as indicators of relative reactivity and compatibility trends relevant to longer-term behavior.

## Methods

The computational framework is density-functional-theory-based ab initio molecular dynamics of solid polymer electrolyte segments placed at interfaces with graphite, silicon, and lithium electrodes. External electric fields and temperature are used as environmental controls, reflecting the fact that interfacial chemistry in batteries is not a single static configuration but depends on thermal activation and on field-driven orientation and polarization effects. Rather than relying on average bond lengths alone, the authors analyze full bond-length distributions over the AIMD trajectories, arguing that distributions capture fluctuation and local heterogeneity more faithfully than single mean values. The manuscript positions this analysis as a way to infer how strongly electrode surfaces attract specific functional groups and how accessible those groups remain to reaction, connecting thermodynamic attraction with kinetic mobility of polymer segments.

**AIMD protocol (first-principles MD, not LAMMPS):** **DFT**-based **ab** **initio** **molecular** **dynamics** of **SPE** **segments** at **graphite**, **Si**, and **Li** **electrodes** in **3D** **PBC** **supercells**; **plane-wave** **pseudopotential** **DFT** as in *J. Phys. Chem. C*; **~1 fs** (or **shorter**) **BOMD** **timestep**; **NVT** **thermostat**; **ps**-scale **trajectories** at **controlled** **temperature** in **K**; **external** **electric** **field** and **temperature** as **environmental** **sweeps** (see **abstract**); **barostat** **N/A** for the **constant**-**volume** **AIMD** **protocols** **described**; **hydrostatic** **pressure** **N/A**; **replica** **exchange** / **metadynamics** **N/A**; **atom** **counts** and **k**-**meshes** in the **article**.

## Findings

The abstract reports that bond-length distributions respond to environmental changes and relate to inferred long-term reactivity, with electrode surface interaction strength and accessibility of functional groups identified as critical factors. The authors further argue that balancing polymer mobility against functional-group attraction to electrode surfaces—kinetic versus thermodynamic considerations—can lead to selective spatial orientation of polar moieties under electric fields, with possible implications for low-temperature operation and high current density conditions where interfacial structure may depart from equilibrium pictures. The closing message is that understanding how reactive key SPE groups are, and how that reactivity shifts with field orientation, can inform design of more stable solid polymer electrolytes; the article does not introduce ReaxFF-scale reactive force fields, and extrapolation from picosecond AIMD to calendar aging remains interpretive rather than a direct numerical prediction.

The introduction additionally contrasts rigid inorganic solid electrolytes, which can offer high ionic conductivity but may suffer from poor interfacial wetting and voiding, with more compliant solid polymer electrolytes that improve contact but often reduce conductivity, motivating hybrid approaches; this landscape frames why interface-specific SPE chemistry must be optimized jointly for wetting, ion transport, and electrochemical stability against negative electrodes.


## Limitations

Time and size limits of **AIMD** require interpretive extrapolation; no explicit **ReaxFF** or continuum cell model in this study.

## Relevance to group

Complementary **first-principles** interface benchmark for **battery** **solid electrolytes**—useful contrast to **ReaxFF**-scale studies elsewhere in the corpus.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.2c01144](https://doi.org/10.1021/acs.jpcc.2c01144)

## Reader notes (navigation)

- Solid electrolyte interfaces (AIMD): [[batteries-interfaces-reaxff]]; theme: [[theme-oxides-silica-ceramics]].

## Related topics

- [[batteries-interfaces-reaxff]]
