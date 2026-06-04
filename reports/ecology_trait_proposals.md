# Candidate missing ECOLOGY traits — literature-backed proposal

**Date:** 2026-06-02 · **Curator:** claude (LLM-assisted) · **Status of all entries:** `PROPOSED`

## Why these traits

The ECOLOGY category had only **10 records**, all confined to **pathogenicity** (`pathogenic_to_host`
+ animal/human/plant pathogen) and **biosafety levels** (BSL-1–5). It had **zero coverage** of the
core ecological dimensions of microbial life: symbiosis, host/habitat association, lifestyle, and
trophic ecology. This proposal adds **16 candidate traits** across those gaps, each backed by
**≥2 distinct, verified literature citations**, enforced by `scripts/audit_proposals.py` in `just qc` / CI.

Authored as `TraitRecord` YAMLs in `data/traits/ecology/` with `mapping_status: PROPOSED`, minted
`traitmech:000040`–`traitmech:000055` (continuing environment 000001–000018 and metabolism
000019–000039). METPO pre-check confirmed all are absent from METPO. Ecology traits parent to
`METPO:1000059` (*phenotype*), with intermediate axis classes for clean hierarchy.

## Proposed traits

### Symbiosis (host-interaction lifestyle)
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000040 | symbiosis | METPO:1000059 | DOI:10.1073/pnas.1218525110; DOI:10.1038/s41579-021-00550-7 |
| traitmech:000041 | mutualism | traitmech:000040 | DOI:10.1073/pnas.1218525110; DOI:10.1126/science.1104816 |
| traitmech:000042 | commensalism | traitmech:000040 | DOI:10.1038/s41579-021-00550-7; DOI:10.1073/pnas.1218525110 |
| traitmech:000043 | parasitism | traitmech:000040 | DOI:10.1038/s41579-021-00550-7; DOI:10.1073/pnas.1218525110 |
| traitmech:000044 | nitrogen-fixing symbiosis | traitmech:000041 | DOI:10.1038/nrmicro.2017.171; DOI:10.1038/nrmicro2990 |
| traitmech:000045 | endosymbiosis | traitmech:000040 | DOI:10.1038/nrmicro2670; DOI:10.1038/nrmicro.2017.171 |

### Pathogen lifestyle (extends existing pathogenic_to_host)
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000046 | opportunistic pathogen | METPO:1004000 | DOI:10.1016/j.tim.2012.04.005; DOI:10.1038/s41579-021-00550-7 |

### Habitat / niche association
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000047 | habitat association | METPO:1000059 | DOI:10.1038/nrmicro1341; DOI:10.1038/nrmicro.2017.87 |
| traitmech:000048 | free-living | traitmech:000047 | DOI:10.1038/nrmicro1341; DOI:10.1038/nrmicro.2017.171 |
| traitmech:000049 | host-associated | traitmech:000047 | DOI:10.1073/pnas.1218525110; DOI:10.1126/science.1104816 |
| traitmech:000050 | soil-dwelling | traitmech:000047 | DOI:10.1038/nrmicro.2017.87; DOI:10.1038/nrmicro1341 |
| traitmech:000051 | rhizosphere association | traitmech:000047 | DOI:10.1038/nrmicro3109; DOI:10.1038/nrmicro.2017.87 |
| traitmech:000052 | gut-associated | traitmech:000049 | DOI:10.1126/science.1104816; DOI:10.1073/pnas.1218525110 |

### Lifestyle & trophic ecology
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000053 | biofilm formation | METPO:1000059 | DOI:10.1038/nrmicro.2016.94; DOI:10.1038/s41579-019-0162-0 |
| traitmech:000054 | predatory bacterium | METPO:1000059 | DOI:10.1146/annurev.micro.091208.073346; DOI:10.1111/1462-2920.13171 |
| traitmech:000055 | saprotrophy | METPO:1000059 | DOI:10.3389/fmicb.2012.00348; DOI:10.1038/nrmicro.2017.87 |

## Citation index (all DOIs/PMIDs verified)
| Reference | Work |
|-----------|------|
| DOI:10.1073/pnas.1218525110 (PMID:23391737) | McFall-Ngai et al., "Animals in a bacterial world…" (PNAS 2013) |
| DOI:10.1038/s41579-021-00550-7 (PMID:33875863) | Drew et al., "Microbial evolution and transitions along the parasite–mutualist continuum" (NRM 2021) |
| DOI:10.1126/science.1104816 (PMID:15790844) | Bäckhed et al., "Host-bacterial mutualism in the human intestine" (Science 2005) |
| DOI:10.1038/nrmicro.2017.171 | Poole et al., "Rhizobia: from saprophytes to endosymbionts" (NRM 2018) |
| DOI:10.1038/nrmicro2990 (PMID:23493145) | Oldroyd, "Speak, friend, and enter" (NRM 2013) |
| DOI:10.1038/nrmicro2670 (PMID:22064560) | McCutcheon & Moran, "Extreme genome reduction in symbiotic bacteria" (NRM 2012) |
| DOI:10.1016/j.tim.2012.04.005 (PMID:22564248) | Brown, Cornforth & Mideo, "Evolution of virulence in opportunistic pathogens" (2012) |
| DOI:10.1038/nrmicro1341 (PMID:16415926) | Martiny et al., "Microbial biogeography: putting microorganisms on the map" (NRM 2006) |
| DOI:10.1038/nrmicro3109 | Philippot et al., "Going back to the roots: the microbial ecology of the rhizosphere" (NRM 2013) |
| DOI:10.1038/nrmicro.2017.87 | Fierer, "Embracing the unknown: disentangling the complexities of the soil microbiome" (NRM 2017) |
| DOI:10.1038/nrmicro.2016.94 (PMID:27510863) | Flemming et al., "Biofilms: an emergent form of bacterial life" (NRM 2016) |
| DOI:10.1038/s41579-019-0162-0 | Flemming & Wuertz, "Towards a quantitative view of the global ubiquity of biofilms" (NRM 2019) |
| DOI:10.1146/annurev.micro.091208.073346 (PMID:19575566) | Sockett, "Predatory lifestyle of Bdellovibrio bacteriovorus" (2009) |
| DOI:10.1111/1462-2920.13171 | Pérez et al., "Bacterial predation: 75 years and counting!" (Environ. Microbiol. 2016) |
| DOI:10.3389/fmicb.2012.00348 (PMID:23055998) | Schimel & Schaeffer, "Microbial control over carbon cycling in soil" (2012) |

## Validation
- Reuses the `PROPOSED` state + `scripts/audit_proposals.py` citation bar — no schema change.
- `just validate-strict` → 0 errors over **412** files; `audit-proposals` → **55/55** PROPOSED passing
  (18 environment + 21 metabolism + 16 ecology); `pytest` → 70 passed; minted IDs contiguous
  000001–000055; all `traitmech:` parent references resolve.

## Follow-ups (out of scope)
- Add evidence-backed `causal_graphs` + ontology groundings when promoted PROPOSED → REVIEWED.
- Possible further ecology axes: marine/freshwater habitat (overlaps ENVO/environment salinity),
  plant-associated lifestyles (endophyte/epiphyte), planktonic vs sessile, ectosymbiosis.
- Distinguish `parasitism` (ecological) from the existing `pathogenic_to_host` (acute disease) during
  curator review; consider linking them.
