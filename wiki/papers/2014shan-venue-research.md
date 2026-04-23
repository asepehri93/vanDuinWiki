---
id: paper:2014shan-venue-research
type: paper
title: "Development of a ReaxFF reactive force field for ammonium nitrate and application to shock compression and thermal decomposition"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:shock-compression
  - keyword:hugoniot
  - keyword:thermal-decomposition
  - keyword:energetic-materials
  - keyword:lammps
  - keyword:qm-training-data
candidate_tags: []
source_refs: []
doi: "10.1021/jp408397n"
year: 2014
authors:
  - "Tzu-Ray Shan"
  - "Adri C. T. van Duin"
  - "Aidan P. Thompson"
venue: "J. Phys. Chem. A"
pdf_sha256: "0ea9170ee6eb0aaf19d52d6d407bd1e8d379d991d5b41aaf401bd8f51e55ecc7"
pdf_path: "papers/Shan_Thompson_AN_proof_JPCA_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014shan-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF** for **ammonium nitrate (AN)** is built by extending a **nitramine/TATB** parameterization with **QM-targeted** fits to **dissociation barriers**, **heats of formation**, and **crystal** properties of **AN** phases. The field predicts the **isothermal P–V** response of **phase IV** **AN** within about **10%** of **DFT** and experiment over the compression range considered, while the **unreacted principal Hugoniot** comes out stiffer than experiment by roughly **~17%**. **Thermal decomposition** simulations on heating to **2500 K** reproduce **pathway** trends consistent with experiment. **Adri C. T. van Duin** coauthors with **Sandia** (**Shan**, **Thompson**).

## Methods

**Local sources:** the PDF at `papers/Shan_Thompson_AN_proof_JPCA_2014.pdf` is present in this workspace; the abstract and introduction are captured in `normalized/extracts/2014shan-venue-research_p1-2.txt` and duplicated in `normalized/extracts/2014shan-venue-jp408397n_p1-2.txt` (same DOI text).

**Force field development:** the authors extend the **nitramine/TATB ReaxFF** and **reoptimize** parameters against **electronic-structure** targets for **NH\(_4\)NO\(_3\)**—including **barriers** for **hydrogen transfer** between **NH\(_4^+\)** and **NO\(_3^-\)**, **heats of formation**, and **crystal** data for **AN** phases—using **NWChem** for key quantum calculations and **VASP** **PBE** **DFT** with **PAW** potentials (**550 eV** cutoff, **6×6×6** **k**-mesh) for **bulk** **phase IV** **P–V** references (Section 2 of the article). **ReaxFF** parameter fitting uses the **standalone ReaxFF code**; **production MD** is run in **LAMMPS**. Existing **C/H/O/N** ReaxFF sets are first shown inadequate for **AN** (e.g., spontaneous **NH\(_4^+\)+NO\(_3^-\)→NH\(_3\)+HNO\(_3\)** in **NPT** tests), motivating the new fit.

**Applications.** **Isothermal compression** and **unreacted Hugoniot** states for **phase IV** use **isotropic** cell compression in **MD** (the article flags **MSST**/**uniaxial** shock as future work where relevant). **Thermal decomposition** uses **4×4×4** **phase IV** supercells heated from **0 K** to **500–2500 K** over **40 ps** at **fixed volume**, then held at the target temperature for **1000 ps**, with species tracked from **bond orders** (sampled every **1 fs** and time-averaged over **100 fs** windows). Additional **PBC** vectors, thermostat coupling for ramp versus hold, and any **NPT** segments used for EOS/Hugoniot benchmarks are only fully tabulated in **`papers/Shan_Thompson_AN_proof_JPCA_2014.pdf`** (**N/A** for complete damping/staging transcription on this page).

## Findings

The **new ReaxFF** reproduces **lattice parameters** for **AN** phases **I, IV, and V** within about **±3%** vs. **DFT**. The **isothermal P–V** curve for **phase IV** agrees with **DFT** and **experiment** within about **10%** over the range reported. **Unreacted** **US–uP** and **P–V** Hugoniot points track experimental scatter **below** **U\(_P\)\(\approx 1\,\mathrm{km/s}\)** and **P\(\approx 15\,\mathrm{GPa}\)** but the model is **too stiff** at higher compression (about **17%** vs. experiment on the principal Hugoniot in the abstract’s summary; the discussion ties part of the error to **isotropic** compression vs. experiment and **density** offsets). **Thermal decomposition** at **2500 K** shows **NH\(_4\)NO\(_3\)** dissociation to **NH\(_3\)** and **HNO\(_3\)** followed by **HNO\(_3\)** chemistry, with major products after **1 ns** including **H\(_2\)O**, **N\(_2\)**, **NO\(_2\)**, and **OH**, qualitatively aligned with reported high-temperature routes—while onset temperatures are **higher** than experiment, attributed to **barriers**, **small cells**, **fast heating**, and **defect-free** crystals.

## Limitations

- **Proof-class** PDF in corpus—confirm pagination and final edited text against the **J. Phys. Chem. A** issue for the **DOI** above; the **version-of-record** reading copy is **`[[2014shan-venue-jp408397n]]`** (`papers/Shan_Thompson_AN_JPCA_2014.pdf`).
- **Reactive FF** uncertainty for **detonation**-grade **multiphysics** remains; compare to higher-fidelity **kinetics** when available.

## Relevance to group

Core **ReaxFF** development for **energetic** **nitrate** systems tied to **safety** and **shock** physics—direct **van Duin** collaboration with **national-lab** partners.

## Citations and evidence anchors

- **DOI:** https://doi.org/10.1021/jp408397n

## Related topics

- [[reaxff-family]]
