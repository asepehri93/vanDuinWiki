---
id: paper:2015kim-venue-paper
type: paper
title: "Supporting information: effects of water on tribochemical wear of silicon oxide interfaces (ReaxFF MD study)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - domain:water-silica-geo
  - method:reaxff
  - task:validation
  - scale:atomistic
source_refs: []
doi: null
year: 2015
authors:
  - "Jejoon Yeon"
  - "Adri van Duin"
  - "Seong H. Kim"
venue: "Supporting information PDF (`papers/Yeon_Langmuir_2016_SI.pdf` in corpus)"
pdf_sha256: "5a239334ee85058aa07a42859d2be4721e977ece928f3b5a1a5e4402c21c6236"
pdf_path: "papers/Yeon_Langmuir_2016_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2015kim-venue-paper -->

## Summary

This corpus PDF is **Supporting Information** for a **ReaxFF molecular dynamics** study on **water effects in tribochemical wear of silicon oxide interfaces** (authors **Yeon**, **van Duin**, **Kim** in the extract). The excerpted pages document **Si(100) oxidation** with **400 O\(_2\)** molecules between slabs at **300 K** for **400 ps**, reporting **~5–6 Å** oxide growth consistent with prior MD, and summarize **amorphous SiO\(_2\)** density/RDF/angle benchmarks in **tabular form in the SI**, comparing **ReaxFF** to QM and experimental reference data. Additional **NVT** hydroxylation runs with **400 water molecules** on oxidized Si(001) and amorphous silica slabs reach **hydroxyl coverage steady state** by **~750 ps** according to the SI text.

## Methods

The SI documents **ReaxFF** validation steps ahead of the parent **Langmuir** tribochemistry study. **Oxidation sanity check:** **400 O\(_2\)** molecules between two **Si(100)** slabs in a **3D periodic** supercell, **300 K**, **400 ps** of **molecular dynamics**, giving **~5–6 Å** oxide thickness consistent with prior **MD** cited as **[1]** in the SI—**barostat / controlled pressure:** **N/A —** not stated for this oxidation box (constant-cell **300 K** run as described). **Amorphous silica:** **Table S1** compares **ReaxFF** to **QM/experiment** for **bulk density** (**2.15** vs **2.2** g cm\(^{-3}\)), first **Si–O RDF** peak (**1.65** vs **1.62** Å), **Si–O–Si** angle (**152.1°** vs **144°**), and **O–Si–O** angle (**110°** vs **109.5°**) on an **annealed SiO\(_2\)** slab (**500 K** **NVT** context in the SI). **Hydroxylation:** **NVT** runs with **400 H\(_2\)O** on **oxidized Si(001)** and **amorphous SiO\(_2\)** (**Figure S2**) reach **hydroxyl coverage** near **steady state** by **~750 ps** per the SI narrative. **Integration package for any MD shown here:** **N/A —** the SI pages summarized for this slug do not name the **MD engine** (only **ReaxFF** as the model). **Shear, normal load, tribo cell geometry, timestep, and thermostat damping** for wear production runs are likewise **N/A —** not on the short excerpt—use **`papers/Yeon_Langmuir_2016_SI.pdf`** in full plus the **parent article** for those parameters.

## Findings

Together, the SI excerpts support using this **Si/O/H ReaxFF** setup for subsequent **tribochemical** work: **~5–6 Å** oxide after **400 ps** / **300 K** with **400 O\(_2\)** between **Si(100)** slabs tracks prior **MD** cited in the SI; **Table S1** shows **ReaxFF** **bulk** and **angular/RDF** metrics for **annealed SiO\(_2\)** close to **QM/experiment** references; and **hydroxyl coverage** on **oxidized Si(001)** and **amorphous SiO\(_2\)** plateaus near **750 ps** for **400** water molecules. **Wear-rate or friction conclusions, sensitivity sweeps, and bibliographic DOI** are **not** asserted from this **SI-only** slug—see the **parent Langmuir** article (`doi: null` here reflects the SI ingest).

## Limitations

- This slug is **SI-only**; the **main article** claims, figures, and tribowear conclusions are not in the p1–2 extract.
- Manifest `paper_id` uses **2015kim-venue-paper** while the filename references **Yeon_Langmuir_2016_SI.pdf**; treat metadata as **corpus registration quirks** until reconciled.
- **Langmuir** **tribochemistry** studies often include **load** **histories** and **counterface** **roughness** not visible in the **oxidation** **validation** excerpt alone.

## Relevance to group

**Adri van Duin** is a co-author; the SI documents **Si/O/H ReaxFF** validation steps underpinning **tribochemistry** and **silica–water** interface studies from the group’s collaborations.

## Citations and evidence anchors

- No DOI present in the SI extract pages captured here; anchor via `pdf_path` until linked to the parent article record.

## Related topics

- [[reaxff-family]]
