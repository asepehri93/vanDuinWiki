# Paper wiki slugs that are not “full primary article” entries

This list documents `wiki/papers/*.md` notes whose **`pdf_path`** (or ingest state) is **not** the recommended standalone **version-of-record research article** PDF for that DOI/work. Use it when interpreting “thin” pages: some are **intentionally** navigation records for **SI**, **proof/galley duplicates**, or **workflow artifacts**.

Maintainers: when the corpus later acquires a clean VOR PDF, update `pdf_path`, `extraction_quality`, and expand the wiki body from the new extract.

## A. Supporting information (SI) packages

These slugs primarily register an **SI PDF**; the narrative article is another file/slug.

| Slug | Notes |
|------|--------|
| `2015kim-venue-paper` | Langmuir SI for tribochemistry / silica oxidation |
| `2016yoon-venue-microsoft-word` | SI for ion irradiation / graphene defects |
| `2018ho-venue-paper` | SI for NaSiOx/water ReaxFF |
| `2019nayir-venue-paper` | SI for Si/silica defects ReaxFF |
| `2020zhang-venue-si-rev2` | Revised SI for graphene-on-SiC growth |
| `2022prenger-venue-paper` | SI for MXene supercapacitor study |
| `2023roshan-venue-paper` | SI for Cu/Si/O ReaxFF optimization |
| `2023uene-venue-paper` | SI tables for BN ALD ReaxFF |

## B. Publisher workflow / non-article PDFs

| Slug | Notes |
|------|--------|
| `2016page-venue-paper` | ACS **TOC / proof** banner fragment—not an article |
| `2013chapter6-venue-untitled` | Book/chapter **placeholder** ingest |
| `2013chapter6-venue-untitled-2` | Duplicate placeholder path |

## C. Ingest without usable article text (operator follow-up)

| Slug | Notes |
|------|--------|
| `2015senftle-venue-paper` | PDF registered; **normalized extract empty / poor**—curate from PDF when possible |

## D. Proof / galley / preprint duplicate (full article often exists under another slug)

These corpus PDFs are **proof or galley** variants. The wiki should carry **substantive duplicated summaries** (or pointers) to the **VOR sibling** where one exists.

| Slug | Canonical sibling / VOR |
|------|-------------------------|
| `2012jeon-venue-rsc-cp` | `2012jeon-venue-rsc-cp-2` (`papers/Jeon_PCCP_Iron_Efield_2013.pdf`) |
| `2014islam-venue-rsc-cp` | `2014islam-physical-che-reaxff-molecular` (`papers/Islam_PCCP_LiS_2014.pdf`) |
| `2014sen-venue-untitled` | `2014sen-nat-oxidation-assisted-ductility` (Nat. Commun. article) |
| `2014senftle-venue-research` | Related Senftle PCCP / Cat. Commun. entries with full text |
| `2014zou-venue-paper` | Acta Mater. proof—use non-proof Acta ingest when available |
| `2015hong-venue-research-2` | Proof duplicate—see `2015hong-venue-research` |
| `2017mao-carbon-121-2-formation-incipient-2` | Duplicate of `2017mao-carbon-121-2-formation-incipient` |
| `2016yoon-venue-research` | Galley proof—see `2016yoon-venue-nn6b03036` |
| `2019kwon-venue-paper` | Uncorrected proof—see `2019kwon-fuel-correct-numerical-simulations` |
| `2021lele-venue-paper` | Galley—see `2021lele-fuel-297-202-reaxff-molecular` |
| `2021leven-x-recent-advances` | Accepted proof—see `2021itai-leven-j-chem-theor-recent-advances` |

## E. Special cases

| Slug | Notes |
|------|--------|
| `2013yang-chemical-phy-self-weakening-lithiated` | Local **`normalized/extracts`** is **proof query + highlights only**; the **published article** is a full CPL letter (DOI `10.1016/j.cplett.2013.01.048`). Wiki prose should follow the published work, not only the p1–2 extract. |
| `2013jacobs-venue-rsc-cy` | Proof query extract—prefer final RSC Advances PDF when ingested |
| `2013vanduin-venue-paper` | Editorial correspondence—not a research article |

---

**Not listed:** Slugs whose `pdf_path` is a normal journal article PDF but whose wiki was briefly “thin” should receive **expanded summaries** in `wiki/papers/`; they are **not** exempt from full curation.
