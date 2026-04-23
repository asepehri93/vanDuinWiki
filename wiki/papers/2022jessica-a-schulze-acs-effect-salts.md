---
id: paper:2022jessica-a-schulze-acs-effect-salts
type: paper
title: "Effect of Salts on the Formation and Hypervelocity-Induced Fragmentation of Icy Clusters with Embedded Amino Acids"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:polymer-organic
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:reactive-md
  - keyword:lammps
source_refs: []
doi: "10.1021/acsearthspacechem.2c00267"
year: 2022
authors:
  - "Jessica A. Schulze"
  - "Dundar E. Yilmaz"
  - "Morgan L. Cable"
  - "Michael Malaska"
  - "Amy E. Hofmann"
  - "Robert P. Hodyss"
  - "Jonathan I. Lunine"
  - "Adri C. T. van Duin"
  - "Andres Jaramillo-Botero"
venue: "ACS Earth Space Chem."
pdf_sha256: "1aa87dfd487fe74c79d5f5e648bb8e8dfca3b7dd5d621506b2851b014e38cffb"
pdf_path: "papers/Schulze_Salt_Ice_cluster_ACS_Earth_Space_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022jessica-a-schulze-acs-effect-salts -->

## Summary

Schulze *et al.* use **ReaxFF molecular dynamics** to study **hypervelocity** (**3–10 km s⁻¹**) **normal impacts** on **icy clusters** that embed representative **amino acids**—**arginine**, **alanine**, and **histidine**—while varying **NaCl** **brine** concentration between **0.25** and **2.0 M** (*ACS Earth Space Chem.*, DOI `10.1021/acsearthspacechem.2c00267`). The motivation is **astrobiological** and **mission-oriented**: **mass spectrometry** of **ocean-world** plumes (**Enceladus**, **Europa**) detects **organic** signatures carried on **salt-rich** **ice grains**, but the **collisional** history of those grains in **instrument** inlets can **fragment** or **chemically alter** analytes. By simulating **reactive** collisions at speeds approaching **encounter** regimes discussed for **flythrough** sampling, the authors separate what is intrinsic to **impact energy** from what may be modulated by **salinity** and **ion–organic** interactions embedded in the **ice** matrix. **Adri C. T. van Duin** co-authorship ties the study to the group’s broader **ReaxFF** practice for **extreme** **nonequilibrium** chemistry.

## Methods

The computational framework is **ReaxFF** in a **large-scale** reactive MD setting appropriate for **bond rearrangement** during **shock-like** loading. The authors construct **ice** matrices containing **amino acid** solutes at controlled **NaCl** levels, then impact them at **normal incidence** across the **3–10 km s⁻¹** window, recording **fragment** identities, **internal energy** partitioning, and qualitative **pathway** differences between **neat** and **brine** cases. The manuscript frames **ReaxFF** as a pragmatic bridge between **fully quantum** impact chemistry (prohibitive at these system sizes) and **non-reactive** models that cannot capture **scission** and **recombination**. Observables emphasize **fragmentation yields**, **velocity thresholds** where chemistry becomes severe, and mechanistic hypotheses linking **Na⁺/Cl⁻** interactions with **side-chain** and **backbone** moieties, including **N–H**-centered pathways and **hydrogen-bond network** disruption in **ice**.

**ReaxFF MD setup (full parameters in the article):** **Engine: LAMMPS**; **large** **atomistic** **supercells** (**atom** **counts** in the **PDF**) in **ice**+**amino** **acid**+**brine** **assemblies** in **3D** **PBC** (or non-periodic **stopping** **walls** if the **article** uses them—check **PDF**); **nonequilibrium** **shock**/**impact** **protocols** (not a single **NVT** **cruise**); **NVE**-like **or** **thermostated** **segments** and **0.1–0.5 fs** **classical** **timestep** as reported; **simulation** **length** in **ps**; **Nose–Hoover** or **Langevin** only where the **authors** **re-equilibrate**; **barostat** **N/A** for the **impactor** **geometry**; **hydrostatic** **pressure** **N/A** for the **stated** **gas-phase**-like **shock** **box**; **external** **electric** **field** **N/A**; **replica** **exchange** / **metadynamics** **N/A**; **concentration** of **NaCl** **0.25**–**2.0** **M**; **room-temperature** **or** **cold** **preequilibration** then **shock** **(velocity 3**–**10** **km/s)**.

## Findings

**Mechanisms / levers: impact** **velocity** controls **reactive** **fragmentation**; **~3** **km/s** already **produces** **chemistry**; **salinity** ( **NaCl** ) **shifts** **pathways** **(secondary** **sensitivity**). **Comparisons: versus** **neat**-**ice** **baselines** and **across** **M**; **Cassini** / **plume** **mass** **spectrometry** is **context**, **not** a direct **laboratory** **match** to these **boxes**. The headline conclusion is hierarchical: **impact speed** is the **dominant** control on **fragmentation** severity, with substantial chemical activity already present near the **lower** end of the scanned window (**~3 km s⁻¹**), while **salinity** acts as a **secondary** knob that shifts **thresholds** and **branching** among channels. **Ions** are argued to **perturb** **H-bond** percolation and can **weaken** or **protect** specific bonds depending on local coordination, producing **salting-in/out**-like rearrangements of **residues** within the **ice** matrix that become more pronounced as **impact** energy rises. The discussion connects these simulation trends to the interpretation of **Cassini** and future **mass spectrometry** datasets, while acknowledging that **instrument** realities—ionization, detector biases, and non-single-collision histories—extend beyond the idealized MD setup described in the **Limitations** section. **Corpus / PDF:** all **velocities**, **timestep**, and **wall** **conditions** must be read from the **version-of-record**—this **summary** is **narrative** only.


## Limitations

Simulations omit full instrument geometry and charge-state distributions of ionized fragments in vacuum mass spectrometers.

## Relevance to group

**ReaxFF** application to **planetary** **astrobiology** sampling scenarios with **van Duin** collaboration.

## Citations and evidence anchors

- DOI: [10.1021/acsearthspacechem.2c00267](https://doi.org/10.1021/acsearthspacechem.2c00267)

## Related topics

- [[reaxff-family]]
