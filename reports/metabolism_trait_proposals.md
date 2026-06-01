# Candidate missing METABOLISM traits — literature-backed proposal

**Date:** 2026-05-30 (updated 2026-05-31) · **Curator:** claude (LLM-assisted) · **Status of all entries:** `PROPOSED`

## Why these traits

The METABOLISM category (108 records) is dominated by **composition-primitive predicates**
(`uses_as_*`, `produces`, `ferments`, `does_not_*`, `has_*_observation`, …) and a small set of
high-level process classes (`respiration`, `fermentation`, `methanogenesis`, `acetogenesis`,
`syntrophy`, `oxidative_phosphorylation`, …). What it lacks is the layer of **named, pathway-level
metabolic capability classes** that microbiologists routinely use to describe organisms. This
proposal adds **21 candidate traits** (18 metabolic-capability traits + 3 intermediate axis
classes) across the clearest gaps, each backed by **≥ 2 distinct, verified literature citations**
(`definition_source` + `evidence`), enforced by `scripts/audit_proposals.py` in `just qc` / CI.

Candidates are authored as `TraitRecord` YAMLs in `data/traits/metabolism/` with
`mapping_status: PROPOSED`, minted `traitmech:000019`–`traitmech:000039` (continuing the
environment round 000001–000018). They flow through the existing closed-mode LinkML validation
and the citation audit with no schema change (the `PROPOSED` state already exists).

### Identifiers / parents
METPO pre-check (`data/raw/metpo.owl`) confirmed all are absent from METPO. The hierarchy uses
intermediate axis classes rather than attaching capabilities directly to `METPO:1000060`:
- **Carbon fixation:** the six pathways parent to a `carbon_fixation` head (`traitmech:000019` →
  `METPO:1000060` *metabolism*).
- **Fermentation:** the four product-specific fermentations parent to the existing
  **`METPO:1002005` Fermentation** class.
- **Phototrophy:** a new `phototrophy` head (`traitmech:000037` → `METPO:1000060`) with a
  `photosynthesis` child (`traitmech:000038`); oxygenic/anoxygenic photosynthesis parent to
  `photosynthesis`, and proteorhodopsin phototrophy parents to `phototrophy`.
- **Anaerobic respiration:** DNRA and AOM parent to the existing **`METPO:1000802`
  Anaerobic respiration** class; a new `dissimilatory_metal_reduction` axis
  (`traitmech:000039` → `METPO:1000802`) parents dissimilatory iron reduction.
- **Manganese oxidation** remains under `METPO:1000060` — it is metal *oxidation*
  (chemolithotrophy), not reduction or anaerobic respiration; a future "metal oxidation" /
  "chemolithotrophy" axis could parent it.

### Intermediate axis classes (minted 2026-05-31)
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000037 | phototrophy | METPO:1000060 | DOI:10.1016/j.tim.2006.09.001; DOI:10.1126/science.289.5486.1902 |
| traitmech:000038 | photosynthesis | traitmech:000037 | DOI:10.1016/j.tim.2006.09.001; DOI:10.1146/annurev-earth-060313-054810 |
| traitmech:000039 | dissimilatory metal reduction | METPO:1000802 | DOI:10.1128/mr.55.2.259-287.1991; PMID:7826009 |

### Already in the corpus / METPO (not proposed)
`acetogenesis`, `methanogenesis`, `fermentation`, `syntrophy`, `respiration`,
`oxidative_phosphorylation`, and `substrate_level_phosphorylation` already exist as classes and were
excluded. `nitrification`, `anammox`, and `ammonia/nitrite oxidation` exist in METPO (not yet seeded)
and are noted as a seeding gap rather than proposed here.

---

## Proposed traits

### Autotrophic carbon-fixation pathways (the marquee gap — corpus had trophic modes but no pathways)
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000019 | carbon fixation | METPO:1000060 | DOI:10.1128/AEM.02473-10; DOI:10.1146/annurev-marine-120709-142712 |
| traitmech:000020 | Calvin-Benson-Bassham cycle | traitmech:000019 | DOI:10.1128/AEM.02473-10; DOI:10.1146/annurev-marine-120709-142712 |
| traitmech:000021 | reductive tricarboxylic acid cycle | traitmech:000019 | DOI:10.1128/AEM.02473-10; DOI:10.1146/annurev-marine-120709-142712 |
| traitmech:000022 | Wood-Ljungdahl pathway | traitmech:000019 | DOI:10.1016/j.bbapap.2008.08.012; DOI:10.1128/AEM.02473-10 |
| traitmech:000023 | 3-hydroxypropionate bicycle | traitmech:000019 | DOI:10.1128/AEM.02473-10; DOI:10.1146/annurev-marine-120709-142712 |
| traitmech:000024 | 3-hydroxypropionate/4-hydroxybutyrate cycle | traitmech:000019 | DOI:10.1126/science.1149976; DOI:10.1128/AEM.02473-10 |
| traitmech:000025 | dicarboxylate/4-hydroxybutyrate cycle | traitmech:000019 | DOI:10.1128/AEM.02473-10; DOI:10.1126/science.1149976 |

Berg (AEM 2011) establishes that, beyond the Calvin cycle, five further autotrophic CO2-fixation
pathways are recognized; Hügler & Sievert (2011) cover their marine distribution; Ragsdale & Pierce
(2008) is the reference for Wood-Ljungdahl; Berg et al. (Science 2007) described the two archaeal
4-hydroxybutyrate pathways.

### Product-specific fermentations (children of the existing Fermentation class)
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000026 | lactic acid fermentation | METPO:1002005 | DOI:10.3389/fmicb.2021.703525; DOI:10.3390/molecules31020333 |
| traitmech:000027 | mixed-acid fermentation | METPO:1002005 | DOI:10.3389/fmicb.2021.703525; DOI:10.3390/molecules31020333 |
| traitmech:000028 | ethanol fermentation | METPO:1002005 | DOI:10.3390/molecules31020333; DOI:10.3389/fmicb.2021.703525 |
| traitmech:000029 | propionic acid fermentation | METPO:1002005 | DOI:10.3390/molecules31020333; DOI:10.3389/fmicb.2021.703525 |

### Element-cycling and energy metabolisms
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000030 | dissimilatory nitrate reduction to ammonium (DNRA) | METPO:1000802 | DOI:10.1126/science.1254070; DOI:10.1007/s11157-025-09719-5 |
| traitmech:000031 | dissimilatory iron reduction | traitmech:000039 | DOI:10.1128/mr.55.2.259-287.1991; PMID:7826009 |
| traitmech:000032 | manganese oxidation | METPO:1000060 | DOI:10.1016/j.tim.2005.07.009; DOI:10.1146/annurev.earth.32.101802.120213 |
| traitmech:000033 | anaerobic oxidation of methane (AOM) | METPO:1000802 | DOI:10.1038/35036572; DOI:10.3389/fmars.2025.1609892 |

DNRA: Kraft et al. (Science 2014) show the donor/acceptor ratio governs ammonium vs. N2.
Fe reduction: Lovley (1991) — *"The oxidation of organic matter coupled to the reduction of Fe(III)
or Mn(IV) is one of the most important biogeochemical reactions…"* AOM: Boetius et al. (2000)
described the ANME–sulfate-reducer consortium.

### Phototrophy
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000034 | oxygenic photosynthesis | traitmech:000038 | DOI:10.1016/j.tim.2006.09.001; DOI:10.1146/annurev-earth-060313-054810 |
| traitmech:000035 | anoxygenic photosynthesis | traitmech:000038 | DOI:10.1016/j.tim.2006.09.001; DOI:10.3389/fmicb.2024.1417714 |
| traitmech:000036 | proteorhodopsin phototrophy | traitmech:000037 | DOI:10.1126/science.289.5486.1902; DOI:10.1038/35081051 |

---

## Citation index (all DOIs/PMIDs verified)
| Reference | Work |
|-----------|------|
| DOI:10.1128/AEM.02473-10 (PMID:21183637) | Berg, "Ecological aspects of the distribution of different autotrophic CO2 fixation pathways" (AEM 2011) |
| DOI:10.1146/annurev-marine-120709-142712 (PMID:21329208) | Hügler & Sievert, "Beyond the Calvin cycle: autotrophic carbon fixation in the ocean" (2011) |
| DOI:10.1016/j.bbapap.2008.08.012 (PMID:18801467) | Ragsdale & Pierce, "Acetogenesis and the Wood-Ljungdahl pathway of CO2 fixation" (2008) |
| DOI:10.1126/science.1149976 (PMID:18079405) | Berg et al., "A 3-hydroxypropionate/4-hydroxybutyrate autotrophic CO2 assimilation pathway in Archaea" (Science 2007) |
| DOI:10.3389/fmicb.2021.703525 | "Energy Conservation in Fermentations of Anaerobic Bacteria" (Front. Microbiol. 2021) |
| DOI:10.3390/molecules31020333 | "Classical Food Fermentations… Alcoholic, Acetic, Butyric, Lactic and Propionic Pathways" (Molecules) |
| DOI:10.1126/science.1254070 (PMID:25104387) | Kraft et al., "The environmental controls that govern the end product of bacterial nitrate respiration" (Science 2014) |
| DOI:10.1007/s11157-025-09719-5 | Review: DNRA's competitive advantage over denitrification under nitrate-limited conditions (2025) |
| DOI:10.1128/mr.55.2.259-287.1991 (PMID:1886521) | Lovley, "Dissimilatory Fe(III) and Mn(IV) reduction" (Microbiol. Rev. 1991) |
| PMID:7826009 | Nealson & Saffarini, "Iron and manganese in anaerobic respiration" (Annu. Rev. Microbiol. 1994) |
| DOI:10.1016/j.tim.2005.07.009 | Tebo et al., "Geomicrobiology of manganese(II) oxidation" (Trends Microbiol. 2005) |
| DOI:10.1146/annurev.earth.32.101802.120213 | Tebo et al., "Biogenic manganese oxides" (Annu. Rev. Earth Planet. Sci. 2004) |
| DOI:10.1038/35036572 (PMID:11034209) | Boetius et al., "A marine microbial consortium apparently mediating AOM" (Nature 2000) |
| DOI:10.3389/fmars.2025.1609892 | Review: anaerobic oxidation of methane in marine sediments (2025) |
| DOI:10.1016/j.tim.2006.09.001 (PMID:16997562) | Bryant & Frigaard, "Prokaryotic photosynthesis and phototrophy illuminated" (2006) |
| DOI:10.1146/annurev-earth-060313-054810 | Fischer, Hemp & Johnson, "Evolution of Oxygenic Photosynthesis" (2016) |
| DOI:10.3389/fmicb.2024.1417714 | Review: anoxygenic photosynthesis in green sulfur bacteria (2024) |
| DOI:10.1126/science.289.5486.1902 (PMID:10976071) | Béjà et al., "Bacterial Rhodopsin: Evidence for a New Type of Phototrophy in the Sea" (Science 2000) |
| DOI:10.1038/35081051 | Béjà et al., "Proteorhodopsin phototrophy in the ocean" (Nature 2001) |

## Validation
- Reuses the `PROPOSED` lifecycle state and `scripts/audit_proposals.py` (≥2 distinct citations) added in
  the environment round — **no schema change** this time.
- `just validate-strict` → 0 errors over **396** files; `audit-proposals` → **39/39** PROPOSED records
  passing (18 environment + 21 metabolism); `pytest` → 70 passed; minted IDs contiguous 000001–000039;
  all `traitmech:` parent references resolve to existing records.

## Follow-ups (out of scope here)
- Add evidence-backed `causal_graphs` (and CHEBI/GO/KEGG groundings) when a candidate is promoted
  PROPOSED → REVIEWED.
- Intermediate axis classes for the dissimilatory/respiratory and phototrophy traits were minted
  on 2026-05-31 (`phototrophy`, `photosynthesis`, `dissimilatory_metal_reduction`); a remaining
  candidate axis is "metal oxidation" / "chemolithotrophy" to parent `manganese_oxidation`.
- Further gaps worth a future round: nitrogen fixation/diazotrophy, denitrification, sulfate reduction
  / sulfur oxidation, methanotrophy (aerobic), hydrogen oxidation/production, cellulolysis/chitinolysis,
  ureolysis, and the trophic-mode classes (chemolithoautotrophy, photoheterotrophy, mixotrophy).
- Seed the existing METPO `nitrification` / `anammox` / `oligotrophic` / `copiotrophic` classes.
