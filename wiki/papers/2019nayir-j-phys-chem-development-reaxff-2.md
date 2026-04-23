---
id: paper:2019nayir-j-phys-chem-development-reaxff-2
type: paper
title: "Development of the ReaxFF Reactive Force Field for Inherent Point Defects in the Si/Silica System"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - method:reaxff
  - task:parameterization
  - task:validation
  - material:silicate-glass
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.9b01481"
year: 2019
authors:
  - "Nadire Nayir"
  - "Adri C. T. van Duin"
  - "Sakir Erkoc"
venue: "J. Phys. Chem. A 123:4303-4313 (2019)"
pdf_sha256: "e83be92a076307cb250a2862abfbcfc690943f4398b88fd38eab3318eec84ad8"
pdf_path: "papers/Nayir_JPC_C_SiOx_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019nayir-j-phys-chem-development-reaxff-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Si/O/H ReaxFF parameters are redeveloped to treat O interstitials and migration in bulk Si and oxidation chemistry at a-SiO2/Si interfaces, emphasizing point-defect behavior omitted by earlier fits. The new “ReaxFF\(_\text{present}\)” reproduces the bond-centered hopping pathway for O in Si with a barrier near 65 kcal/mol, closer to experiment/DFT than prior SiOH(2010) behavior that spuriously allowed deep O diffusion at 300 K. Annealing simulations of prepared a-SiO2 on Si recover expected interfacial O transport relative to literature, including fixing the low-temperature spurious diffusion issue.

## Methods

**2 — Force-field training.** Starting from **Fogarty** *et al.* **ReaxFF\(_\text{SiOH(2010)}\)**, the authors add **DFT**-based training on **O-related** **defects** in **a-SiO\(_2\)/Si** and the **O**-**migration** **path** in **bulk** **Si**, then **re-fit** **selected** **Si–Si**, **Si–O**, and **valence** **angle** **parameters** with a **single-parameter** **least-squares**-style **search** (eq. 1 in the *J. Phys. Chem. A* paper) until **ReaxFF** and **QM/experiment** **targets** **compromise** under **σ**-**weighted** **errors**.

**1 — MD application.** **Molecular dynamics** is performed with **ReaxFF\(_\text{present}\)** (reactive **MD**; **N/A** for a **unique** **public** **code** **string** in the **short** **p1–2** **excerpt**—**see** the **J. Phys. Chem. A** **PDF** **/ SI** for **the** **MD** **engine** **if** **required**). **ReaxFF\(_\text{present}\)** **trajectories** use **PBC** and the **velocity** **Verlet** **integrator** with a **0.5 fs** **time** **step** in the **a-SiO\(_2\)** **annealing** **protocol** quoted in **§2** of the **PDF**; **Berendsen**-style **thermal** **and** **pressure** **damping** are set to **100 fs** and **5000 fs** in that **glass**-**preparation** **block**. The **a-SiO\(_2\)** **melt**/**quench** **sequence** alternates **high-**T **NVT** and **NPT** **ramps** at **P = 0** (see the **7000 K → 300 K** **two-** **step** **anneal** with **50–500 ps** **holds** and **final** **NPT** **relaxation** to a **~2.21 g cm⁻³** **glass** in the **Methods**). **O** **diffusion** in **bulk** **Si** is studied with **NVT** **MD** on **800–2400 K** **targets** in the **Results** **text**; **interface** **anneals** use the **prepared** **a-SiO\(_2\)/Si** **cells** described in the same **article** (**Figure** **6** **ff.**). **Two-phase** **melting-** **point** **MD** for **validation** uses **NVT**/**NPT** **stages** with **2744-** **atom** **phases** as **narrated** in the **text**. **Shear / shock:** **N/A**. **External uniform electric field:** **N/A**. **Replica / metadynamics:** **N/A** — direct **NVT**/**NPT** sampling in the reported stages. **Barostat:** **NPT** at **zero** mean **pressure** in the glass-formation legs; **NVT** in selected high-*T* holds without stress servocontrol (per the protocol paragraphs). **MD engine (package name):** **N/A** in the short indexed excerpt; treat as **ReaxFF** **MD** with the stated **ensembles** and **fs**-level controls in the VOR **PDF**.

**3 — Static DFT** as a **sole** **Method** **block**:** **N/A** — **DFT** **trains** the **ReaxFF**; **the** **reported** **evidence** is **largely** **ReaxFF** **MD** **plus** **QM** **targets**.

## Findings

**O** **in** **bulk** **Si** **hops** **BC→BC** in the **(110)** **plane** with a **split-**type **saddle**; **ReaxFF\(_\text{present}\)** **predicts** a **~64.8** **kcal** **mol⁻¹** **barrier** in **line** with **cited** **DFT**/**experiment**. **NVT** **diffusion** **runs** **(800–2400 K)** show **onset** of **appreciable** **O** **motion** **above** **~1400 K** with **BC-**only **hops** at **high** **T** and **D(T)** **trends** **consistent** with **published** **data** in the **broad** **sense** **of** the **article**. **a-SiO\(_2\)** **density** and **RDF**/**coordination** **metrics** **for** the **new** **FF** **match** **experiments** **more** **closely** than **SiOH(2010)** on the **comparisons** **plotted** in **Figs. 10–11**/**Table 4**. **a-SiO\(_2\)/Si** stack anneals on **ReaxFF\(_\text{present}\)** reproduce **O** transport at the interface without the unphysical **room-temperature** deep **O** penetration seen for **SiOH(2010)** in the same class of setup (the low-*T* spurious-diffusion regression the authors target).

## Limitations

Focus on Si/SiO2 defect and interface phenomena; parameters are not automatically transferable to unrelated chemistries (e.g., alkali-containing silicates) without testing. Alkali contamination, strain from epitaxial Si, and high-κ dielectric adjacency are named in the broader literature as contexts requiring additional validation beyond the pure Si/O/H scope emphasized in the *J. Phys. Chem. A* article. Stress-assisted diffusion, H charging, and radiation damage in power devices may require additional training data not central to the bulk Si / a-SiO\(_2\) defect benchmarks highlighted there.

## Relevance to group

Foundational ReaxFF for silicon oxidation—central to much group and field work on gate stacks and silica.

## Citations and evidence anchors

`papers/Nayir_JPC_C_SiOx_2019.pdf` — main text (ReaxFF\(_\text{present}\) training, a-SiO\(_2\) anneal protocol, O diffusion and interface tests). https://doi.org/10.1021/acs.jpca.9b01481

Supporting information PDF: [[2019nayir-venue-paper]].

## Related topics

- [[2019nayir-venue-paper]]
- [[reaxff-family]]
