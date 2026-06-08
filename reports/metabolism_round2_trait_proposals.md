# Candidate METABOLISM traits, round 2 — literature-backed proposal

**Date:** 2026-06-08 · **Curator:** claude (LLM-assisted) · **Status of all entries:** `PROPOSED`

## Why these traits

Metabolism round 1 added carbon-fixation pathways, product-specific fermentations, DNRA,
dissimilatory iron reduction, manganese oxidation, AOM, photosynthesis, and proteorhodopsin
phototrophy. This **round 2** fills the remaining high-value gaps: the rest of the nitrogen and
sulfur cycles, additional metal redox, fermentative hydrogen production, and a **biopolymer-
degradation** family (the corpus had no macromolecule-degradation traits at all). Adds **12 candidate
traits**, each backed by **≥2 distinct, verified literature citations**, enforced by
`scripts/audit_proposals.py` in `just qc` / CI.

Authored in `data/traits/metabolism/` with `mapping_status: PROPOSED`, minted
`traitmech:000103`–`traitmech:000114`. (IDs `000075–000102` are reserved by the open PHYSIOLOGY
PR #87 and GENOMICS PR #88, so round 2 continues from `000103`.) All absent from METPO/corpus.
Respiratory traits parent to the existing `METPO:1000802` (anaerobic respiration); the manganese
trait reuses the round-1 `traitmech:000039` (dissimilatory metal reduction) axis; hydrogen
production parents to `METPO:1002005` (Fermentation).

## Proposed traits

### Nitrogen cycle
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000103 | nitrogen fixation | METPO:1000060 | DOI:10.1038/nrmicro.2018.9; DOI:10.1038/nrmicro954 |
| traitmech:000104 | denitrification | METPO:1000802 | DOI:10.1128/mmbr.61.4.533-616.1997; DOI:10.1038/nrmicro.2018.9 |

### Sulfur cycle
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000105 | dissimilatory sulfate reduction | METPO:1000802 | DOI:10.1038/nrmicro1892; DOI:10.3389/fmicb.2011.00081 |
| traitmech:000106 | sulfur oxidation | METPO:1000060 | DOI:10.1111/j.1574-6976.2009.00187.x; DOI:10.1128/AEM.67.7.2873-2882.2001 |

### Metal redox
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000107 | iron oxidation | METPO:1000060 | DOI:10.1146/annurev.micro.112408.134208; DOI:10.1099/mic.0.045344-0 |
| traitmech:000108 | dissimilatory manganese reduction | traitmech:000039 | DOI:10.1128/mr.55.2.259-287.1991; PMID:7826009 |

### Hydrogen
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000109 | fermentative hydrogen production | METPO:1002005 | DOI:10.3389/fmicb.2021.703525; DOI:10.1016/S0360-3199(02)00131-3 |

### Biopolymer degradation
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000110 | biopolymer degradation | METPO:1000060 | DOI:10.1016/j.cbpa.2015.10.018; DOI:10.1128/MMBR.66.3.506-577.2002 |
| traitmech:000111 | cellulolysis | traitmech:000110 | DOI:10.1128/MMBR.66.3.506-577.2002; DOI:10.1016/j.cbpa.2015.10.018 |
| traitmech:000112 | chitinolysis | traitmech:000110 | DOI:10.3389/fmicb.2013.00149; DOI:10.1080/07388550601168223 |
| traitmech:000113 | xylan degradation | traitmech:000110 | DOI:10.1111/j.1757-1707.2009.01004.x; DOI:10.1016/j.cbpa.2015.10.018 |
| traitmech:000114 | lignin degradation | traitmech:000110 | DOI:10.1039/c1np00042j; DOI:10.1016/j.cbpa.2015.10.018 |

## Citation index (all DOIs/PMIDs verified)
| Reference | Work |
|-----------|------|
| DOI:10.1038/nrmicro.2018.9 (PMID:29398704) | Kuypers, Marchant & Kartal, "The microbial nitrogen-cycling network" (2018) |
| DOI:10.1038/nrmicro954 (PMID:15263897) | Dixon & Kahn, "Genetic regulation of biological nitrogen fixation" (2004) |
| DOI:10.1128/mmbr.61.4.533-616.1997 (PMID:9409151) | Zumft, "Cell biology and molecular basis of denitrification" (1997) |
| DOI:10.1038/nrmicro1892 (PMID:18461075) | Muyzer & Stams, "The ecology and biotechnology of sulphate-reducing bacteria" (2008) |
| DOI:10.3389/fmicb.2011.00081 (PMID:21734907) | Plugge et al., "Metabolic flexibility of sulfate-reducing bacteria" (2011) |
| DOI:10.1111/j.1574-6976.2009.00187.x (PMID:19645821) | Ghosh & Dam, "…lithotrophic sulfur oxidation…" (2009) |
| DOI:10.1128/AEM.67.7.2873-2882.2001 (PMID:11425697) | Friedrich et al., "Oxidation of reduced inorganic sulfur compounds by bacteria…" (2001) |
| DOI:10.1146/annurev.micro.112408.134208 | Emerson, Fleming & McBeth, "Iron-oxidizing bacteria…" (2010) |
| DOI:10.1099/mic.0.045344-0 (PMID:21511765) | Hedrich, Schlömann & Johnson, "The iron-oxidizing proteobacteria" (2011) |
| DOI:10.1128/mr.55.2.259-287.1991 (PMID:1886521) | Lovley, "Dissimilatory Fe(III) and Mn(IV) reduction" (1991) |
| PMID:7826009 | Nealson & Saffarini, "Iron and manganese in anaerobic respiration" (1994) |
| DOI:10.3389/fmicb.2021.703525 | "Energy Conservation in Fermentations of Anaerobic Bacteria" (2021) |
| DOI:10.1016/S0360-3199(02)00131-3 | Hallenbeck & Benemann, "Biological hydrogen production…" (2002) |
| DOI:10.1016/j.cbpa.2015.10.018 (PMID:26583519) | Cragg et al., "Lignocellulose degradation mechanisms across the Tree of Life" (2015) |
| DOI:10.1128/MMBR.66.3.506-577.2002 (PMID:12209002) | Lynd et al., "Microbial cellulose utilization…" (2002) |
| DOI:10.3389/fmicb.2013.00149 (PMID:23785358) | Beier & Bertilsson, "Bacterial chitin degradation…" (2013) |
| DOI:10.1080/07388550601168223 (PMID:17364687) | Bhattacharya et al., "Bacterial chitinases: properties and potential" (2007) |
| DOI:10.1111/j.1757-1707.2009.01004.x | Dodd & Cann, "Enzymatic deconstruction of xylan for biofuel production" (2009) |
| DOI:10.1039/c1np00042j (PMID:21918777) | Bugg et al., "Pathways for degradation of lignin in bacteria and fungi" (2011) |

## Validation
- Reuses the `PROPOSED` state + `scripts/audit_proposals.py` citation bar — no schema change.
- `just validate-strict` → 0 errors over **443** files; `audit-proposals` → **86/86** PROPOSED passing
  on this branch (74 prior + 12 round 2); `pytest` → 70 passed; round-2 IDs 000103–000114; all
  `traitmech:` parent references resolve (incl. the round-1 `traitmech:000039` metal-reduction axis).

## Follow-ups (out of scope)
- Remaining degradation traits with thinner reviews: starch/amylolysis, pectinolysis, proteolysis,
  lipolysis; and aerobic methanotrophy / hydrogen oxidation (note: trophic-mode equivalents
  methanotrophic/hydrogenotrophic already live in PHYSIOLOGY).
- Add evidence-backed `causal_graphs` + ontology groundings when promoted PROPOSED → REVIEWED.
