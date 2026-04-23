---
id: paper:2018micha-ka-ski-j-phys-chem-development-charge-implicit
type: paper
title: Development of a Charge-Implicit ReaxFF Potential for Hydrocarbon Systems
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:carbon-hydrocarbon
- domain:reaxff-lineage
- domain:reactive-md
- method:reaxff
- task:parameterization
- scale:atomistic
paper_keywords:
- keyword:reaxff-parameterization
- keyword:lammps
- keyword:reactive-md
- keyword:qm-training-data
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpclett.7b03155
year: 2018
authors:
- Michał Kański
- Dawid Maciążek
- Zbigniew Postawa
- Chowdhury M. Ashraf
- Adri C. T. van Duin
- Barbara J. Garrison
venue: J. Phys. Chem. Lett. 2018, 9, 359–363
pdf_sha256: f6de14878c82da293001c78b31a0e4685db58cd8496c94c83c1176be6a20662c
pdf_path: papers/Kanski_Ashraf_JPC_letters_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018micha-ka-ski-j-phys-chem-development-charge-implicit -->

## Summary

This *Journal of Physical Chemistry Letters* communication introduces **charge-implicit ReaxFF (ci-ReaxFF)** for **C/H** systems by **removing on-the-fly charge equilibration** (no **EEM/QEq**-like updates each step). The motivation is computational: conventional ReaxFF’s explicit charge dynamics can dominate cost in **very large** simulations and can produce **unphysical charged fragments** in **high-energy collision** regimes where electronic equilibration is not the right physical picture. The authors **reoptimize** bonded and nonbonded parameters against an expanded training corpus that includes **condensed-phase** configurations and **Ziegler–Biersack–Littmark (ZBL)**-style **short-range** repulsive pair terms for **keV**-scale nuclear collisions, aiming to retain **ReaxFF-2008**-class accuracy on the training metrics while improving throughput and stability for **organic solid** and **particle bombardment** use cases.

## Methods

Training follows the letter’s **Development** section: start from **ReaxFF-2008** datasets, augment with **condensed-phase** benchmarks and **ZBL** high-energy pairs using **distance-dependent weighting** so that close encounters are dominated by the nuclear repulsive wall. The authors also revisit **van der Waals cutoff** selection using **β-carotene** **NPT** equilibration tests described in the text. Implementation targets **LAMMPS** compatibility; potential files and usage examples are referenced to **Supporting Information**.

### MD application (throughput benchmarks)

**Engine / code:** **LAMMPS** **molecular dynamics** with the proposed **charge-implicit ReaxFF** for **C/H** systems (abstract). **System sizes:** benchmarked from **~13k** to **~900k** **atoms** in the reported speed tests. **PBC:** bulk **organic** cells implied by **β-carotene** **NPT** tests and **keV** **bombardment** examples. **Ensemble:** **NPT** referenced for **β-carotene** equilibration; **NVE**/**NVT** stages for cascades—**N/A — full staging** not transcribed from the excerpt. **Timestep / thermostat / barostat / run length:** **N/A — import from letter + SI** (`papers/Kanski_Ashraf_JPC_letters_2018.pdf`). **Temperature:** cascade tests emphasize **keV** energies rather than a single thermostat **K** in the abstract; thermal benchmarks use the letter’s stated conditions. **Pressure:** **NPT** targets appear for **β-carotene** cutoff tests (**exact pressure** in **Methods**). **Electric field:** **N/A — not used**. **Enhanced sampling:** **N/A — not indicated** beyond standard **MD** for the throughput comparisons summarized in the abstract.
## Findings

The manuscript reports that **ci-ReaxFF** matches **ReaxFF-2008** on the quoted training-quality metric while delivering roughly **2–5×** faster MD in reported tests spanning **13k–900k** atoms. Removing explicit charge dynamics is argued to eliminate **spurious charged species** in high-energy collision cascades that motivated the development. Applicability is explicitly **hydrocarbon-focused** as parameterized; polar chemistry and strong electrostatic heterogeneity are outside the intended scope.

**Comparisons.** Speed and accuracy comparisons are internal to **ReaxFF-2008** vs **ci-ReaxFF** under the letter’s benchmark protocols.

**Sensitivity / outlook.** Performance depends on **system size** and collision energy regime; users should mirror the letter’s **ZBL** blending and **cutoff** tests before claiming portability.

**Corpus honesty.** Numeric **speedup** factors and **atom** ranges come from the **J. Phys. Chem. Lett.** abstract; reproduce from the **PDF**/**SI** when auditing.
## Limitations

**Implicit charges** cannot reproduce full **electrostatic** chemistry of **full ReaxFF**; systems requiring accurate ionic solvation or strong charge separation need the explicit charge model or alternative parametrizations.

## Reproducibility notes

Operators should record **ZBL** blending weights, **cutoffs**, and **timestep** choices when running **ci-ReaxFF** cascade simulations, because keV-range collisions are sensitive to timestep-dependent energy deposition if integration is too aggressive. Benchmarks against **full ReaxFF** should use identical **geometry** and **ensemble** settings to isolate charge-model effects from protocol differences.

For organic **β-carotene** benchmarks used in cutoff selection, archive **NPT** target **pressure**, **temperature**, and equilibration length, because reported density sensitivities are only meaningful relative to those reference conditions. When publishing throughput comparisons, include **hardware**, **MPI** decomposition (if any), and **neighbor list** rebuild intervals so speedups are not tied to a single machine configuration.

## Relevance to group

**Adri C. T. van Duin**-linked **ReaxFF** variant aimed at **fast** **reactive** simulations of **organic** **solids** and **particle bombardment**.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acs.jpclett.7b03155](https://doi.org/10.1021/acs.jpclett.7b03155)

## Related topics

- [[reaxff-family]]
