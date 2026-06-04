# Candidate missing MORPHOLOGY traits — literature-backed proposal

**Date:** 2026-06-03 · **Curator:** claude (LLM-assisted) · **Status of all entries:** `PROPOSED`

## Why these traits

MORPHOLOGY is the largest category (65 records), with thorough coverage of **cell shape, Gram type,
cell size, pigmentation, and basic motility**. But it had **zero coverage of cell ultrastructure** —
surface layers, cellular appendages, intracellular inclusions, protein microcompartments,
flagellar arrangement, surface-motility sub-types, and cyanobacterial/actinomycete differentiation.
This proposal adds **19 candidate traits** across those gaps, each backed by **≥2 distinct, verified
literature citations**, enforced by `scripts/audit_proposals.py` in `just qc` / CI.

Authored as `TraitRecord` YAMLs in `data/traits/morphology/` with `mapping_status: PROPOSED`, minted
`traitmech:000056`–`traitmech:000074` (continuing env 000001–018, metab 000019–039, ecology
000040–055). METPO pre-check confirmed all are absent. Traits parent to existing METPO morphology
classes where possible (`METPO:1000704` flagellated, `METPO:1000702` motile, `METPO:1000059`
phenotype) with new intermediate axis classes.

## Proposed traits

### Flagellar arrangement (under existing flagellated, METPO:1000704)
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000056 | flagellar arrangement | METPO:1000704 | DOI:10.1093/femsre/fuv034; DOI:10.3390/biom9070279 |
| traitmech:000057 | monotrichous | traitmech:000056 | DOI:10.1093/femsre/fuv034; DOI:10.3390/biom9070279 |
| traitmech:000058 | lophotrichous | traitmech:000056 | DOI:10.1093/femsre/fuv034; DOI:10.3390/biom9070279 |
| traitmech:000059 | amphitrichous | traitmech:000056 | DOI:10.1093/femsre/fuv034; DOI:10.3390/biom9070279 |
| traitmech:000060 | peritrichous | traitmech:000056 | DOI:10.1093/femsre/fuv034; DOI:10.3390/biom9070279 |

### Surface-motility sub-types (under existing motile, METPO:1000702)
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000061 | twitching motility | METPO:1000702 | DOI:10.1146/annurev.micro.56.012302.160938; DOI:10.1146/annurev.micro.57.030502.091014 |
| traitmech:000062 | swarming motility | METPO:1000702 | DOI:10.1038/nrmicro2405; DOI:10.1146/annurev.micro.57.030502.091014 |

### Cell-surface structures & appendages
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000063 | capsule | METPO:1000059 | DOI:10.1146/annurev.micro.50.1.285; DOI:10.1146/annurev.biochem.75.103004.142545 |
| traitmech:000064 | S-layer | METPO:1000059 | DOI:10.1038/nrmicro3213; DOI:10.1038/s41579-025-01258-8 |
| traitmech:000065 | prosthecate | METPO:1000059 | DOI:10.1111/j.1365-2958.2007.05633.x; DOI:10.1128/MMBR.00040-09 |

### Intracellular inclusions, storage granules & microcompartments
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000066 | intracellular inclusion | METPO:1000059 | DOI:10.1038/s41579-020-0413-0; DOI:10.1038/nrmicro.2018.10 |
| traitmech:000067 | polyhydroxyalkanoate granule | traitmech:000066 | DOI:10.1128/mr.54.4.450-472.1990; DOI:10.1038/s41579-020-0413-0 |
| traitmech:000068 | polyphosphate granule | traitmech:000066 | DOI:10.1146/annurev.biochem.77.083007.093039; DOI:10.1038/s41579-020-0413-0 |
| traitmech:000069 | sulfur globule | traitmech:000066 | DOI:10.1016/S0065-2911(08)00002-7; DOI:10.1038/s41579-020-0413-0 |
| traitmech:000070 | gas vesicle | traitmech:000066 | DOI:10.1038/nrmicro2834; DOI:10.1038/s41579-020-0413-0 |
| traitmech:000071 | magnetosome | traitmech:000066 | DOI:10.1038/nrmicro.2016.99; DOI:10.1038/nrmicro842 |
| traitmech:000072 | carboxysome | traitmech:000066 | DOI:10.1038/nrmicro.2018.10; DOI:10.1038/nrmicro1913 |

### Cellular differentiation / multicellular forms
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000073 | heterocyst | METPO:1000059 | DOI:10.1101/cshperspect.a000315; DOI:10.1093/femsre/fuw029 |
| traitmech:000074 | mycelial growth | METPO:1000059 | DOI:10.1038/nrmicro1968; DOI:10.1038/nrmicro3178 |

## Citation index (all DOIs/PMIDs verified)
| Reference | Work |
|-----------|------|
| DOI:10.1093/femsre/fuv034 (PMID:26195616) | Schuhmacher, Thormann & Bange, "How bacteria maintain location and number of flagella?" (2015) |
| DOI:10.3390/biom9070279 (PMID:31337100) | Nakamura & Minamino, "Flagella-Driven Motility of Bacteria" (Biomolecules 2019) |
| DOI:10.1146/annurev.micro.56.012302.160938 (PMID:12142488) | Mattick, "Type IV pili and twitching motility" (2002) |
| DOI:10.1146/annurev.micro.57.030502.091014 (PMID:14527279) | Harshey, "Bacterial motility on a surface" (2003) |
| DOI:10.1038/nrmicro2405 (PMID:20694026) | Kearns, "A field guide to bacterial swarming motility" (2010) |
| DOI:10.1146/annurev.micro.50.1.285 | Roberts, "The biochemistry and genetics of capsular polysaccharide production in bacteria" (1996) |
| DOI:10.1146/annurev.biochem.75.103004.142545 | Whitfield, "Biosynthesis and assembly of capsular polysaccharides in E. coli" (2006) |
| DOI:10.1038/nrmicro3213 (PMID:24509785) | Fagan & Fairweather, "Biogenesis and functions of bacterial S-layers" (2014) |
| DOI:10.1038/s41579-025-01258-8 | "Assembly, architecture and functional roles of microbial surface layers" (NRM 2025) |
| DOI:10.1111/j.1365-2958.2007.05633.x (PMID:17376069) | Wagner & Brun, "Out on a limb: …Caulobacter stalk…" (2007) |
| DOI:10.1128/MMBR.00040-09 (PMID:20197497) | Curtis & Brun, "Getting in the loop: regulation of development in Caulobacter crescentus" (2010) |
| DOI:10.1038/s41579-020-0413-0 (PMID:32710089) | Greening & Lithgow, "Formation and function of bacterial organelles" (2020) |
| DOI:10.1038/nrmicro.2018.10 | Kerfeld et al., "Bacterial microcompartments" (2018) |
| DOI:10.1038/nrmicro1913 | Yeates et al., protein-based organelles in bacteria / carboxysomes (2008) |
| DOI:10.1128/mr.54.4.450-472.1990 (PMID:2087222) | Anderson & Dawes, bacterial polyhydroxyalkanoates (1990) |
| DOI:10.1146/annurev.biochem.77.083007.093039 (PMID:19344251) | Rao, Gómez-García & Kornberg, "Inorganic polyphosphate: essential for growth and survival" (2009) |
| DOI:10.1016/S0065-2911(08)00002-7 (PMID:18929068) | Frigaard & Dahl, "Sulfur metabolism in phototrophic sulfur bacteria" (2009) |
| DOI:10.1038/nrmicro2834 (PMID:22941504) | Pfeifer, "Distribution, formation and regulation of gas vesicles" (2012) |
| DOI:10.1038/nrmicro.2016.99 | Uebe & Schüler, "Magnetosome biogenesis in magnetotactic bacteria" (2016) |
| DOI:10.1038/nrmicro842 (PMID:15083157) | Bazylinski & Frankel, "Magnetosome formation in prokaryotes" (2004) |
| DOI:10.1101/cshperspect.a000315 (PMID:20452939) | Kumar, Mella-Herrera & Golden, "Cyanobacterial heterocysts" (2010) |
| DOI:10.1093/femsre/fuw029 (PMID:28204529) | Herrero, Stavans & Flores, "The multicellular nature of filamentous heterocyst-forming cyanobacteria" (2016) |
| DOI:10.1038/nrmicro1968 (PMID:19079351) | Flärdh & Buttner, "Streptomyces morphogenetics" (2009) |
| DOI:10.1038/nrmicro3178 (PMID:24384602) | Claessen et al., "Bacterial solutions to multicellularity" (2014) |

## Validation
- Reuses the `PROPOSED` state + `scripts/audit_proposals.py` citation bar — no schema change.
- `just validate-strict` → 0 errors over **431** files; `audit-proposals` → **74/74** PROPOSED passing
  (18 environment + 21 metabolism + 16 ecology + 19 morphology); `pytest` → 70 passed; minted IDs
  contiguous 000001–000074; all `traitmech:` parent references resolve.

## Follow-ups (out of scope)
- Further morphology gaps for a future round: pili/fimbriae & type IV pili (note: "pili" already
  appears in METPO), holdfast, sheath, slime layer/glycocalyx, akinete, baeocyte, budding division,
  fruiting body, additional cell arrangements (streptococcus/staphylococcus/tetrad/sarcina/palisade),
  and magnetotaxis as a behavioural trait.
- Add evidence-backed `causal_graphs` + ontology groundings when promoted PROPOSED → REVIEWED.
