---
id: paper:2019gurcan-aral-journal-of-a-atomistic-insights
type: paper
title: "Atomistic insights on the influence of pre-oxide shell layer and size on the compressive mechanical properties of nickel nanowires"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:mechanics-tribology
  - method:reaxff
  - task:application
  - material:metal-surface
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:oxide-surface
  - keyword:nose-hoover
source_refs: []
doi: "10.1063/1.5080640"
year: 2019
authors:
  - "Gurcan Aral"
  - "Md Mahbubul Islam"
  - "Yun-Jiang Wang"
  - "Shigenobu Ogata"
  - "Adri C. T. van Duin"
venue: "Journal of Applied Physics"
pdf_sha256: "c083fe3b138fa2b42c01188235c6d08857c3f4d9fe239065af0f5c27215c0962"
pdf_path: "papers/Aral_Ni_nanowires_JAP_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019gurcan-aral-journal-of-a-atomistic-insights -->

## Summary

Metal nanowires gain oxidation shells in ambient processing, so their mechanical response reflects coupled metal plasticity and amorphous oxide chemistry rather than ideal single-crystal scaling laws. This Journal of Applied Physics study uses **ReaxFF molecular dynamics in LAMMPS** to compare **\[001\]-oriented nickel nanowires** at three pristine diameters (**about 5.0, 6.5, and 8.0 nm**) against the same sizes after spontaneous oxidation in **O\(_2\)** at **300 K**, which builds an **approximately 1 nm amorphous Ni\(_x\)O\(_y\)** shell (final diameters near **6.0, 7.6, and 8.9 nm**). **Uniaxial compression** along **\[001\]** at **300 K** applies engineering strain rates near **0.01% ps\(^{-1}\)** (order **10\(^8\) s\(^{-1}\)** in the article’s framing) to **14%** strain while tracking virial stress. The central comparison is how native oxide lowers yield stress and changes size scaling relative to pristine wires, with emphasis on dislocation nucleation near the disordered oxide–metal interface.

## Methods

Initial nickel cylinders are relaxed with conjugate-gradient minimization, **NPT** equilibration at **300 K** without applied stress, then compressed under **NVT** at **300 K** with **Nosé–Hoover** thermostats. The loading cell is **periodic along the compression axis** with **free lateral surfaces** so the wire can expand or contract laterally. Oxidation runs expose pristine wires to **O\(_2\)** under **NVT** until a self-limiting amorphous shell forms. Integration uses **velocity Verlet** with a **0.5 fs** timestep; stresses derive from the **virial** expression. Interactions use a **Ni/O/H ReaxFF** parameterization with **variable charges** so metallic bonding, ionic oxide motifs, and covalent oxygen chemistry share one reactive framework.

**MD engine and system sizes.** **Molecular dynamics** uses **LAMMPS** with the cited **Ni/O/H ReaxFF** on **nanowire** cylinders of order **10³ atoms** (pristine diameters **~5.0, 6.5, 8.0 nm**; oxidized shells **~1 nm** thick). **Boundaries:** **periodic** along **[001]** compression with **free** lateral surfaces. **Timestep:** **0.5 fs** as stated above. **Ensemble:** **NPT** at **300 K** for initial relaxation, then **NVT** compression at **300 K** with **Nose–Hoover** thermostats. **Barostat:** **NPT** only during the zero-stress relaxation leg; compression uses **NVT** without additional **hydrostatic pressure** servo. **External electric field:** **N/A**. **Enhanced sampling:** **N/A**.

## Findings

For **pristine** nanowires, **yield stress and strain rise with diameter** in the simulated diameter window, interpreted through **surface-stress–mediated dislocation nucleation** in defect-free cylinders—a trend that can differ from polycrystalline experiments where sources and statistics dominate. **Oxide-coated** wires yield at **lower stress** than their pristine counterparts and show **reduced sensitivity to diameter**, because the **rough oxide–metal interface** seeds plasticity earlier and homogenizes size effects. Stress–strain curves progress through elastic and nonlinear elastic regimes into plastic flow with **zigzag** character; the oxide shifts both the **onset** of plasticity and the **post-yield** hardening/softening pattern relative to bare nickel. Operators validating these trends should compare the reported stress definitions and engineering-strain conventions directly with `papers/Aral_Ni_nanowires_JAP_2019.pdf`, because high strain rates and nanometer dimensions amplify sensitivity to thermostat choice and stress averaging windows.

## Limitations

**High** **strain rates** and **idealized** cylindrical geometry differ from experiments; oxidation protocol is **simulation-specific** but consistent with prior **tensile** study from the same group.

## Relevance to group

**van Duin**-parameter **ReaxFF** **Ni/O/H** for **chemomechanics** of **oxidized** **metal** **NWs**.

## Citations and evidence anchors

- `papers/Aral_Ni_nanowires_JAP_2019.pdf`

## Related topics

- [[reaxff-family]]
