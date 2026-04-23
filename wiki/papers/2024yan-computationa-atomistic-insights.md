---
id: paper:2024yan-computationa-atomistic-insights
type: paper
title: "Atomistic insights into chemical vapor deposition process of preparing silicon carbide materials using ReaxFF-MD simulation"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:alloys-metallurgy
  - method:reaxff
  - task:application
  - material:widegap-semiconductor
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nose-hoover
  - keyword:catalysis-surface
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2024.113032"
year: 2024
authors:
  - "Zefan Yan"
  - "Yu Tian"
  - "Rongzheng Liu"
  - "Bing Liu"
  - "Youlin Shao"
  - "Malin Liu"
venue: "Comput. Mater. Sci."
pdf_sha256: "e59587f62d2145672c1627a939f209fd9c97ea1b55770f3e2c12bb493e38f39f"
pdf_path: "papers/ReaxFF_others/Yan_CVD_SiC_CompMatSci_2024.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024yan-computationa-atomistic-insights -->

ReaxFF MD combined with DFT verification and an energy-based Monte Carlo (EMC)–MD workflow models methyltrichlorosilane (MTS) CVD on β-SiC, with emphasis on deposition efficiency, film stoichiometry versus temperature, and post-deposit crystallinity (OVITO IDS).

## Summary

The study addresses SiC chemical vapor deposition (CVD) relevant to coatings (e.g., TRISO fuel particles) using ReaxFF MD for the C–Si–Cl–H system. DFT (Gaussian, B3LYP/6-31G**) validates bond/angle curves and lattice constants against ReaxFF. Production MD uses LAMMPS and OVITO, NVT with Nosé–Hoover thermostat, 100 MTS molecules above a β-SiC (100)/(010)/(001) slab, minimization, 100 ps equilibration at 300 K, ramp 0.05 K/fs to target temperature, 1000 ps hold, Δt = 0.2 fs, periodic x/y and fixed z, substrate sizes 5a₀×5a₀×3a₀ and 10a₀×10a₀×3a₀ (a₀ = 0.4358 nm). Temperatures 1600–3800 K appear in the parameter table. An EMC–MD–CVD layer uses DFT-derived relative bond-strength ordering for C, Si, Cl, and H at the surface to preferentially remove H and Cl during deposition passes, implemented with Gaussian and LAMMPS; crystallinity uses a defined metric combining cubic diamond and neighbor-shell fractions (OVITO).

## Methods

- **ReaxFF and DFT checks:** Established C–Si–Cl–H ReaxFF; comparison to B3LYP/6-31G** for Si–C stretch and Cl–Si–C / Si–C–H bends; lattice constant of β-SiC and MTS internal coordinates versus experiment (article Table 2).
- **Direct MD:** LAMMPS, OVITO, NVT, Nosé–Hoover, Δt = 0.2 fs, 100 MTS precursors, thermal protocol above, β-SiC substrate orientation noted in text.
- **EMC–MD–CVD:** DFT bond-energy curves for Si–Si, Si–C, C–C, Cl–Si, Cl–C, H–Si, H–C combined into surface-atom energy scales; periodic removal of weakly bound H/Cl by Monte Carlo rules coupled to MD segments (Fig. 5–6 in article); temperature-dependent deposition efficiency and film composition (Figs. 7–10).
- **Crystallinity analysis:** OVITO Identify Diamond Structure (IDS) and a defined crystallinity metric from cubic diamond and first/second neighbor shell populations.

**1 — MD application (ReaxFF CVD, direct path).** **Engine:** **LAMMPS** + **ReaxFF**; **NVT** with **Nosé–Hoover** **thermostat**; **Δt = 0.2 fs**; **100** **MTS** **molecules** over **β-SiC** **(100)/(010)/(001)** **slabs**; **5a₀×5a₀×3a₀** and **10a₀×10a₀×3a₀** **cells** (\(a_0=0.4358\) **nm**); **PBC** in **x,y**; **fixed** **z**; **minimization**; **100 ps** **equilibration** at **300 K**; **ramp** **0.05** **K/fs**; **1000 ps** **hold**; **T** **1600–3800** **K** in **table**; **OVITO** post. **N/A** — no **NPT**/**barostat** or **external** **E-field** in the **direct** **MD** **path** summarized here. **N/A** — no **replica**/**metadynamics** in that **leg**; **EMC** is a **separate** **kinetic** **layer** (below).

**2 — Force-field training** — **N/A**; uses **established** **C–Si–Cl–H** **ReaxFF** with **DFT** **B3LYP** **checks** (not a new **FF** **fit** **paper** in the **sense** of **AGENTS** **block 2**—see **article** for **provenance**). **3 — Static QM (validation):** **Gaussian** **B3LYP/6-31G\*\*** for **bonds**/ **angles** and **lattice** **β-SiC** **vs** **ReaxFF**; **EMC** uses **DFT** **bond-strength** **orderings** for **surface** **H/Cl** **removal** **rules** ( § of **EMC** in **article**). **4 — Hybrid EMC–MD** — **Monte** **Carlo** **H/Cl** **stripping** **with** **MD** **segments**; **N/A** for **a** **single** **NPT** **barostat** **in** that **subprotocol**.

## Findings

1. The ReaxFF parameter set reproduces the validated DFT curves and β-SiC lattice data within small reported errors versus experiment.
2. The EMC–MD–CVD model yields deposition efficiency versus temperature with a maximum at intermediate temperatures and reduced efficiency at very high \(T\) (e.g., 3800 K vs 1600 K), interpreted as difficulty forming C–Si bonds when chemistry is too hot—consistent with trends described alongside experimental literature cited in the paper.
3. Film composition shifts from Si-rich at lower temperature to more balanced to C-rich at higher temperature, traced to gas-phase MTS pyrolysis products (e.g., CH₄ vs carbonaceous fragments) and differential removal of Si vs C at the surface in the EMC criterion—reported as aligning with prior experimental results from the authors’ group.
4. Larger-scale trajectories show an initially amorphous deposit that orders toward **β-SiC**-like character; crystallinity metrics from **OVITO** **IDS** increase strongly with **T** in the range studied.

**Corpus honesty** — not a host-group paper; see **`## Limitations`**.
## Limitations

Highly reactive high-temperature chemistry and simplified gas-phase chemistry remain approximate; EMC removal rules are a kinetic shortcut rather than full gas-phase reaction networks.

## Relevance to group

External collaboration context (Tsinghua); demonstrates ReaxFF + workflow coupling for industrial CVD-style SiC growth relevant to reactive MD practice in the broader community.

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2024.113032](https://doi.org/10.1016/j.commatsci.2024.113032)

## Related topics

- [[reaxff-family]]
