---
id: paper:2018c-ulises-gonzalez-va-j-phys-chem-investigation-wetting
type: paper
title: "Investigation on the wetting behavior of 3C-SiC surfaces: theory and modeling"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - material:widegap-semiconductor
  - method:classical-md
  - task:application
paper_keywords:
  - keyword:water-interfaces
  - keyword:classical-ff
  - keyword:nvt-simulation
  - keyword:lammps
  - keyword:nose-hoover
  - keyword:nve-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.7b12271"
year: 2018
authors:
  - "C. Ulises Gonzalez-Valle"
  - "Satish Kumar"
  - "Bladimir Ramos-Alvarado"
venue: "J. Phys. Chem. C (2018); DOI 10.1021/acs.jpcc.7b12271"
pdf_sha256: "504a0945e85d41ce59c94af0bc7ceec5ef52a3f1b7cf629137cca68b7b31ab0f"
pdf_path: "papers/Others/19. Investigation on the Wetting Behavior of 3C-SiC Surfaces Theory and Modeling.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018c-ulises-gonzalez-va-j-phys-chem-investigation-wetting -->

## Summary

**Classical molecular dynamics** study of **water** on **3C-SiC** **(100)** and **(111)** surfaces with **Si-** vs **C-termination**, combining **contact-angle/wettability** metrics with a **mean-field** interpretation and **interfacial liquid structure** analysis to explain **crystallographic** and **chemical termination** effects. **3C-SiC** is a **wide-gap** candidate for **high-power** electronics; reliable **wet processing** and **thermal** **management** require knowing whether **intrinsic** surfaces are **hydrophobic** or **hydrophilic** as a function of **termination** and **facet**.

## Methods

From the J. Phys. Chem. C article PDF (`pdf_path`).

- **Water model:** **SPC/E**; **SHAKE** on water; **PPPM** electrostatics (**accuracy** **1e-5** as stated). **Solid substrate frozen** (no substrate dynamics). **Oxygen-only** solid-liquid LJ coupling for mapping to the mean-field wettability model; **C-O** parameters fixed to reproduce **~64 deg** contact angle on graphite; **Si-O epsilon** scanned (**SiC(100)** and **SiC(111)** ranges in article), **sigma** **2.63 A**, cutoff **15 A**. Droplet sizes **2500-8500** molecules; box **y = 30.61 A** (**100**) or **31.48 A** (**111**), **x = 250-350 A**, **z** large enough to avoid vacuum artifacts; **PBC** in **x,y,z**.
- **Integration:** **LAMMPS**; **timestep 1 fs**; droplet **COM** reset in **x,y** each step; neighbor list every step. **(i)** minimization; **(ii) NVT** equilibration **298 K**, **Nose-Hoover** thermostat **tau = 0.1 ps**, **0.75 ns**; **(iii) NVE** **1 ns** sanity check; **(iv) NVE production 5 ns**, frames every **0.5 ps**; contact angles from time-averaged density (**MRPM** procedure per Ramos-Alvarado et al., as cited).
- **System size / composition:** **SPC/E** water droplets of **2500–8500** molecules on frozen **3C-SiC** **slabs** (thousands of **water oxygen** **atoms** plus substrate **atoms**; box edges **~250–350 Å × ~30–31 Å** in-plane per facet as stated).
- **Barostat / hydrostatic pressure:** **N/A —** droplet-in-vapor setups use fixed orthorhombic cells without **NPT** **barostat** coupling to bulk **pressure** targets.

## Findings

- **Mechanism / outcomes:** **Termination** and **plane** strongly affect predicted **wetting**; **Si-terminated** **(111)** regions trend **more hydrophilic** in the simulations summarized in the abstract, tied to **interfacial** **adsorption** structure.
- **Comparisons:** **Mean-field** wettability modeling is **compared** against **MD**-resolved **density** profiles to show when a single interaction strength is insufficient versus **experimentally** relevant **contact-angle** trends.
- **Sensitivity:** **Si–O Lennard-Jones ε** scans, **droplet** size (**2500–8500** molecules), and **in-plane** orientation (**armchair** vs **zigzag**) modulate **footprint anisotropy** and extracted angles.
- **Limitations / outlook:** The abstract stresses **classical** **force-field** uncertainty for quantitative angles on real **CVD** **SiC**; **roughness** and **oxidation** are noted caveats in **Discussion**.
- **Corpus honesty:** Protocol lines follow the **J. Phys. Chem. C** article at `pdf_path`; confirm frozen-slab constraints and **PPPM** settings in the **PDF** before porting parameters.

## Limitations

- **Classical force fields** for **SiC–water** may require calibration against experiment for **quantitative** contact angles; the abstract emphasizes qualitative mechanistic trends.
- **Surface** **roughness**, **steps**, and **contamination** on **real** **CVD** **SiC** wafers perturb **droplet** **pinning** beyond the **atomically** **flat** **slabs** used for **MRPM** **contact-angle** extraction.
- **Electrochemical** **oxidation** of **SiC** in **aqueous** **environments** can change **termination** faster than **MD** **droplet** **equilibration** timescales unless **surface** **composition** is **fixed** **by** **protocol**.
- **Dissolved** **silica** **species** and **ionic** **strength** in **electrolyte** **solutions** can shift **interfacial** **water** **structure** relative to **pure** **SPC/E** **droplets** on **bare** **slabs**.

## Related topics

- [[2018gonzalez-valle-acs-thermal-transport]]
- [[reaxff-family]]
