---
id: paper:2024sepehrinezhad-venue-manuscript
type: paper
title: 'ReaxFF Reactive Force Field for Exploring Electronically Switchable Polarization in Zn\(_{1-x}\)Mg\(_x\)O Ferroelectric Semiconductors'
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:ferroelectrics-polar
  - material:oxide
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:neb
  - keyword:npt-simulation
  - keyword:lammps
  - keyword:berendsen-thermostat
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.4c02233"
year: 2024
authors:
  - "Sepehrinezhad, A."
  - "Baksa, S. M."
  - "Dabo, I."
  - "van Duin, A. C. T."
venue: "J. Phys. Chem. C"
pdf_sha256: "fb12474abb205d0f1eb48eec443f7f20c3e68cd69116b27dc2f956c34598a91b"
pdf_path: "papers/Sepehrinezhad_ZnMgO_JPCC_2024_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024sepehrinezhad-venue-manuscript -->

## Summary

Sepehrinezhad and colleagues develop a **ReaxFF** parameterization for **wurtzite Zn\(_{1-x}\)Mg\(_x\)O** to study **ferroelectric switching** in **Mg-alloyed ZnO**, training against **Quantum ESPRESSO DFT** data for **equations of state**, **phase pathways**, and **domain-wall** and **intrinsic switching** paths (including **nudged elastic band (NEB)** images). Large-scale **MD** with **sinusoidal electric fields** explores **coercive fields** vs **Mg content**, **temperature**, and **Mg spatial distribution** (random, uniform/spaced, clustered), reporting **P–E** hysteresis characteristics such as **~10 nm** critical thickness for observable switching and **~100 μC/cm\(^2\)** residual polarization in the parameterized scenarios described in the abstract.

## Methods

**DFT reference.** **Quantum ESPRESSO** with **norm-conserving** **PseudoDojo** potentials; **PBE** GGA; **k**-spacing **0.05 Å\(^{-1}\)**; **80 Ry** wavefunction cutoff / **320 Ry** density cutoff (with stated SCF thresholds). **EOS** scans use **2×2×2** **wurtzite/rocksalt** supercells across **x = 0, 25, 50, 75, 100%**; **intrinsic switching** uses **3×3×2** supercells at **x = 5.6–27.8%** with **75-image NEB**; **domain-wall migration** uses **8×1×2** cells at **12.5% Mg** with **25-image** paths for **Mg behind/in front** of the wall.

**ReaxFF training.** Starting from **merged ZnO / MgO** ReaxFF priors (literature sets cited in §2.2), authors refine **Zn–Mg–O** interactions against DFT, including **bond/angle/off-diagonal** terms enumerated in §3.2.

**MD protocol.** After minimization, **NPT equilibration** at **100 K** with **Δt = 0.25 fs**; **Berendsen** thermostat (**100 fs** coupling) and barostat (**2500 fs** coupling). **Sinusoidal E-field** sweeps at **100–1000 K** for **Mg** fractions **0–37.5%**; **five repeats** per condition. **Fixed charges** (post-equilibration averages by species) are used during **field** runs to avoid spurious **bulk conduction** from **EEM**-style long-range charge transfer in wide-gap slabs (**§3.4**). **Polarization** computed via **Born effective charges** and atomic positions (**eq. 2**).

**Mg distributions.** **Random** substitution, **uniform** spacing via **farthest-point** sampling, and **clustered** arrangements.

**1 — MD application (field-driven ReaxFF).** **Engine:** **ReaxFF** in **LAMMPS**-class workflow (article). **System:** **wurtzite** **Zn\(_{1-x}\)Mg\(_x\)**O slabs and supercells; sizes and **PBC** in §3. **Ensemble and relaxation:** after minimization, **NPT equilibration** at **100 K**; **Berendsen** thermostat (**100 fs** coupling) and **barostat** (**2500 fs** coupling); **Δt = 0.25 fs**. **Production:** **sinusoidal electric field** sweeps at **100–1000 K**; **fixed** **post-equilibration** **species** **charges** during field runs to limit spurious long-range **charge** **sloshing** (**§3.4**). **Polarization:** via **Born effective charges** and atomic positions (**eq. 2**). **Electric field** — time-dependent **E-field** (sinusoidal sweep) as in §3. **N/A** — **umbrella sampling**, **metadynamics**, and **replica exchange** (not used as the main enhanced-sampling method in the summarized protocol).

**2 — Force-field training.** **Parent:** **merged** **ZnO** / **MgO** ReaxFF priors (cited in §2.2). **QM (training reference):** **Quantum ESPRESSO**, **PBE** **GGA**, **norm-conserving** **PseudoDojo** potentials, **0.05 Å\(^{-1}\)** k-spacing, **80 Ry** wavefunction / **320 Ry** density cutoffs, stated **SCF** tolerances. **Targets:** **EOS** for wurtzite/rocksalt **2×2×2** **supercells** at **x = 0, 25, 50, 75, 100%**; **NEB** (**75** **images**, **3×3×2** **intrinsic switching** at **5.6–27.8%** **Mg**); **domain wall** **paths** (**25** **images**, **8×1×2** at **12.5%** **Mg**). **Optimization:** **Zn–Mg–O** **bond/angle/off-diagonal** refits against DFT in §3.2.

**3 — Static QM** — the **DFT** reference block is **embedded** in training above; no separate “QM-only” application section is the focus.
## Findings

**Hysteresis and coercivity (trends with composition and arrangement).** **Higher** **Mg** (alloying) and **T** both trend toward **lower** **coercive** **E** in the **simulations**; **clustered** **Mg** can **raise** **E\_c** vs **uniform** spacing, and **random** **Mg** tends to **lower** it **vs** **uniform** at **similar** **x** (abstract/§3).

**Polarization, thickness, and levers.** Simulations point to **residual** **P** on the order of **~100 μC/cm\(^2\)** and a **~10 nm**-scale **critical** **thickness** for **switching** in the **parameterized** **scenarios** (abstract; verify numerics in VOR if pagination differs from **galley**). **Sinusoidal** **E-field** sweeps over **T** and **x** are the main **sensitivity** probes.

**Corpus honesty** — see **`## Limitations`** (galley, **fixed-charge** post-processing).
## Limitations

**Galley** PDF may differ slightly from **final JPCC** pagination; **fixed-charge** approximation addresses **EEM** artifacts but is not a full **polarizable electronic** treatment. **DFT** and **ReaxFF** remain approximations for **defective, disordered alloys**.

## Relevance to group

Direct **ReaxFF** **parameterization** output from the van Duin group on **ferroelectric oxide alloys** with explicit **DFT** training sets and **field-driven MD**.

## Citations and evidence anchors

- Methods: **§3** (*J. Phys. Chem. C*, **DOI 10.1021/acs.jpcc.4c02233**).

## Related topics

- [[reaxff-family]]
