---
id: paper:2018sengul-venue-reaxff-molecular
type: paper
title: ReaxFF molecular dynamics simulation of intermolecular structure formation
  in acetic acid-water mixtures at elevated temperatures and pressures
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:organics-polymers-pyrolysis
- domain:reactive-md
- domain:water-silica-geo
- method:enhanced-sampling
- method:reaxff
- scale:atomistic
- task:application
paper_keywords:
- keyword:enhanced-sampling
- keyword:reaxff-application
- keyword:npt-simulation
- keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: ''
year: 2018
authors:
- Mert Y. Sengul
- Clive A. Randall
- Adri C. T. van Duin
venue: J. Chem. Phys.
pdf_sha256: 9cea029e1d57180745970c068bb1d85b40b6eee5a18d7ee7ec7132b6e2db4437
pdf_path: papers/Sengul_aceticacid_water_JCP_2018_online.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018sengul-venue-reaxff-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the JCP article identified by `title` and `pdf_path`.

## Summary

**ReaxFF reactive MD** in **ADF** is used to study **structure and hydrogen-bonding** in **acetic acid–water** mixtures from **ambient** conditions to **supercritical** states (temperature–pressure ranges in the article, e.g. up to roughly **600–1200 K** and **5–150 MPa** as stated in the introduction). A **combined** ReaxFF (water potential plus biomolecular acetic acid subset, with **O–C–O valence conjugation** adjusted) is checked against **metadynamics** on **acetic acid dissociation** so that the acid dissociation free-energy difference yields a realistic **\(K_a\)**. Canonical MD with **0.25 fs** timesteps and **Berendsen** thermalization analyzes **RDFs**, hydrogen-bond accounting, and cluster statistics versus composition \(x_{\mathrm{HAc}}\).

## Methods

- **Force-field merge and \(K_a\) calibration:** Water ReaxFF from prior work; acetic acid subset from biomolecular O/H/C parameters; **valence conjugation** term adjusted (reported change from **−19.93** to **−5.0** for the optimized parameter) so metadynamics gives two minima in the **\(S_{\mathrm{OH}}\)** collective variable with \(\Delta G\) translating to **\(K_a \approx 4.88\)**, near experiment (**4.76**). Metadynamics uses **Gaussian** hill deposition (height/width and deposition interval in the paper), **NPT** equilibration (**1 ns**, **300 K**, **0.1 MPa**) of one acetic acid in 60 waters in a **12.26 Å** cube.
- **Bulk MD:** **1000** molecules total, varying **acetic acid mole fraction** \(1.0 \ge x_{\mathrm{HAc}} \ge 0.2\); densities from **1.0** and **1.05 g/cm\(^3\)** for water and acid components; **canonical** ensemble; **0.25 fs** timestep; **Berendsen** thermostat (**0.1 ps** damping); heating in **100 K** increments with **50 ps** equilibration and extended runs (**≥0.5 ns** at 300 K, **≥1 ns** at final \(T\)) until homogeneous density.
- **Analysis:** **RDFs** for OO, carbonyl–hydroxyl oxygen, methyl–carbonyl carbon, etc.; **hydrogen-bond** criteria using donor/acceptor oxygen distances from RDF minima and angular cutoffs (relaxed in supercritical conditions); averages over the last **0.25 ns** with **500** samples.

**Bulk production MD (consolidated).** **ADF** **ReaxFF** **reactive MD** on **1000** molecules in **periodic** cubic **supercells** with **PBC**; **NVT** **Berendsen** control (**0.1 ps** damping), **0.25 fs** timestep, staged **100 K** heating with **50 ps** **equilibration** per step and **≥0.5 ns** (**300 K**) / **≥1 ns** (target **T**) sampling; **supercritical** grids per article. **Metadynamics** calibration uses **NPT** (**1 ns** at **300 K**, **0.1 MPa**) before bulk **NVT** sweeps. **Barostat for bulk sweeps:** **N/A — see JCP Methods** for each state point. **Electric field:** **N/A — not used**. **Enhanced sampling:** **metadynamics** for **\(K_a\)** only; **N/A — umbrella / replica exchange** otherwise.
## Findings

At **ambient** \(T\), **P = 0.1 MPa\): for **acid-rich** compositions, **cyclic dimers** and **chain-like** assemblies appear (RDF peaks ~**2.7 Å** and longer-range peaks ~**5–9 Å**); increasing **water** disrupts dimers/chains, and released acid molecules show **~4 Å** correlations consistent with **dipole–dipole** pairing. **Water–water** RDFs match experimental-like shell structure at high water content; distorted shells appear as acetic acid dominates. In the **supercritical** regime, long-range structural order (e.g. second/fourth neighbor features) **weakens**; water–water RDFs remain consistent with literature, while **first-neighbor acid–water** correlations persist at lower supercritical \(T\) but **fade** at higher \(T\) within the studied range.

**Comparisons, sensitivity, and limitations.** The **metadynamics** calibration explicitly targets **agreement** with experimental **\(K_a\)** for acetic acid dissociation, anchoring the merged **ReaxFF** before **composition**/**temperature**/**pressure** sweeps. **Sensitivity** to **\(x_{\mathrm{HAc}}\)** shows systematic changes in hydrogen-bond motifs and RDF shell structure, with additional broadening of hydrogen-bond definitions in **supercritical** regimes as described in the article. **Limitations** include the usual **ReaxFF** approximations to **quantum** hydrogen-bonding effects. **Corpus honesty:** cite `pdf_path` for exact state points and any **SI** figures beyond this summary.
## Limitations

Reactive MD with empirical parameters may not capture all quantum effects in hydrogen bonding; supercritical analysis relies on broader HB geometric cutoffs.

## Reader notes (navigation)

- Author proofs in corpus: [[2018sengul-venue-total-number]], [[2018sengul-venue-total-number-2]]
- ZnO interface companion: [[2018sengul-acs-reaxff-molecular]]

## Related topics

- [[reaxff-family]]
