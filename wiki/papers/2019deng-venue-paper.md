---
id: paper:2019deng-venue-paper
type: paper
title: "Journal proof PDF (Na-Si-O glass study; use VOR sibling for article text)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - material:silicate-glass
  - method:reaxff
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:silica-silicate
source_refs: []
doi: "10.1111/jace.16837"
year: 2019
authors:
  - "Lu Deng"
  - "Shingo Urata"
  - "Yasuyuki Takimoto"
  - "Tatsuya Miyajima"
  - "Seung Ho Hahn"
  - "Adri C. T. van Duin"
  - "Jincheng Du"
venue: "Journal proof workflow PDF (not standalone article text)"
pdf_sha256: "c7dd9c04db519db1be332101c0d546af7b5c7f1d3f5973f482885eb0b20b5c36"
pdf_path: "papers/Deng_NaSiOx_JaCERS_2019_proof.pdf"
extraction_quality: "partial"
group_affiliation: false
---
<!-- id:paper:2019deng-venue-paper -->

??? info "Corpus limitation"
    The local extract (`normalized/extracts/2019deng-venue-paper_p1-2.txt`) is **Wiley e-annotation instructions**, not the article. Scientific content is curated on [[2020deng-venue-structural-features]] (same DOI).

## Summary

The file `papers/Deng_NaSiOx_JaCERS_2019_proof.pdf` is a Wiley publisher **proof** package for the Journal of the American Ceramic Society article DOI `10.1111/jace.16837` on sodium silicate glasses modeled with ReaxFF relative to diffraction and neutron scattering data. The automated text extract (`normalized/extracts/2019deng-venue-paper_p1-2.txt`) contains **USING e-ANNOTATION TOOLS FOR ELECTRONIC PROOF CORRECTION**, including requirements for Adobe Acrobat Professional or Reader version 11 or above, step-by-step descriptions of Replace, Strikethrough, Commenting, Insert, Attach File, Stamp, and Drawing Markup tools, and boilerplate about reprint purchases through Sheridan. No manuscript abstract or results section appears in that extract layer, so this wiki cannot responsibly restate melt–quench protocols, radial distribution functions, \(Q_n\) distributions, or agreement metrics from the PDF path registered here. All substantive scientific content for the peer-reviewed study is maintained on [[2020deng-venue-structural-features]], which references the version-of-record article PDF ingested under that slug.

## Methods

**What this PDF is (corpus honesty).** `papers/Deng_NaSiOx_JaCERS_2019_proof.pdf` is a **Wiley e-proof / annotation-instruction** workflow package for the **Journal of the American Ceramic Society** article **DOI `10.1111/jace.16837`**. The mechanical text extract registered for this slug (`normalized/extracts/2019deng-venue-paper_p1-2.txt`) is dominated by **“USING e-ANNOTATION TOOLS…”** boilerplate rather than the manuscript **Methods** section, so this wiki page **must not** be used to recover **melt–quench schedules**, **RDF/\(Q_n\)** validation tables, or **LAMMPS** settings.

**Where the real protocol lives.** For **ReaxFF** development, **glass** preparation, and **diffraction/neutron** comparisons, use the **version-of-record** corpus page **`[[2020deng-venue-structural-features]]`** (and its `pdf_path`) as the primary reading path for the same DOI.

**MD application (checklist honesty for this slug).** The proof PDF + indexed extract do not expose a usable **LAMMPS** input deck here. For machine slot coverage only (all **N/A —** defer to **`[[2020deng-venue-structural-features]]`**): **Engine** **N/A**; **system size & composition** **N/A**; **PBC**/**boundary** conditions **N/A**; **ensemble** (**NVT**/**NPT**/**NVE**) **N/A**; **timestep** (**fs**) **N/A**; **equilibration**/**production** **ps**/**ns** spans **N/A**; **thermostat** **N/A**; **barostat** **N/A**; **300 K**-style **temperature** ramps **N/A** to quote from this file; **hydrostatic pressure** **N/A**; **electric field** and **enhanced sampling** **N/A**.
## Findings

Glass structure metrics, scattering comparisons, and force-field performance statements are documented on the sibling page tied to the readable article PDF. The structural limitation of this slug is that Wiley’s e-annotation instructions occupy the beginning of the text layer, so mechanical extractors may never surface the scientific sections unless the PDF’s reading order places article text before the instruction booklet or unless full-text extraction is run on a different file variant. Anyone needing sodium silicate network statistics, neutron and X-ray comparisons, or ReaxFF validation metrics must follow [[2020deng-venue-structural-features]], which is curated against the article PDF rather than the proof workflow. This page exists so `pdf_sha256` and `pdf_path` rows remain interpretable when the corpus retains publisher workflow PDFs alongside primary research files.

## Limitations

This slug exists for manifest alignment with a workflow PDF. Do not use it as a primary reading copy; cite the DOI and the VOR wiki entry.

## Relevance to group

Na-silicate glass validation with van Duin co-authorship; paired with the curated VOR note for reproducibility.

If the corpus later acquires a text layer for the proof PDF that actually includes the article, rerun `scripts/sync_wiki_paper_frontmatter.py` (when applicable) and refresh extracts before elevating this slug to a primary reading path; until then, treat the proof strictly as archival.

Automated benchmarks that scan for “Na silicate glass ReaxFF” should attach `extraction_quality: partial` metadata to this slug so evaluators know summaries intentionally defer to the sibling page.

## Reader notes (navigation)

- [[2020deng-venue-structural-features]]
- [[reaxff-family]]
