# Candidate missing GENOMICS traits — literature-backed proposal

**Date:** 2026-06-05 · **Curator:** claude (LLM-assisted) · **Status of all entries:** `PROPOSED`

## Why these traits

The GENOMICS category was the smallest in the corpus — **only 5 records, all GC content**
(`GC content` + four GC-composition bins). It had **no coverage** of the rest of microbial genome
biology: mobile genetic elements, genome-defense systems, sequence-composition properties beyond GC,
and genome architecture. This proposal adds **14 candidate traits** across those gaps, each backed by
**≥2 distinct, verified literature citations**, enforced by `scripts/audit_proposals.py` in `just qc` / CI.

Authored as `TraitRecord` YAMLs in `data/traits/genomics/` with `mapping_status: PROPOSED`, minted
`traitmech:000089`–`traitmech:000102`. (IDs `000075–000088` are reserved by the open PHYSIOLOGY
PR #87, so genomics continues from `000089` to avoid collisions when both merge.) METPO pre-check
confirmed all are absent. Traits parent to `METPO:1000188` (the quality upper class that `GC content`
uses) with one new intermediate axis class (`mobile genetic element`).

## Proposed traits

### Mobile genetic elements
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000089 | mobile genetic element | METPO:1000188 | DOI:10.1038/nrmicro1235; DOI:10.1111/1574-6976.12067 |
| traitmech:000090 | plasmid carriage | traitmech:000089 | DOI:10.1128/MMBR.00020-10; DOI:10.1038/nrmicro1235 |
| traitmech:000091 | prophage | traitmech:000089 | DOI:10.1128/MMBR.67.2.238-276.2003; DOI:10.1038/ismej.2017.16 |
| traitmech:000092 | transposable element | traitmech:000089 | DOI:10.1111/1574-6976.12067; DOI:10.1038/nrmicro1235 |
| traitmech:000093 | genomic island | traitmech:000089 | DOI:10.1038/nrmicro884; DOI:10.1111/j.1574-6976.2008.00136.x |

### Genome-defense systems
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000094 | CRISPR-Cas system | METPO:1000188 | DOI:10.1038/s41579-019-0299-x; DOI:10.1016/j.molcel.2014.03.011 |
| traitmech:000095 | restriction-modification system | METPO:1000188 | DOI:10.1128/MMBR.00044-12; DOI:10.3389/fmicb.2015.00528 |

### Sequence composition
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000096 | codon usage bias | METPO:1000188 | DOI:10.1038/nrg2899; DOI:10.1146/annurev.genet.42.110807.091442 |
| traitmech:000097 | GC skew | METPO:1000188 | DOI:10.1093/oxfordjournals.molbev.a025626; DOI:10.1016/S0378-1119(99)00297-8 |

### Genome architecture & cardinality
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000098 | genome size | METPO:1000188 | DOI:10.1038/nrmicro3331; DOI:10.1038/ismej.2014.60 |
| traitmech:000099 | genome streamlining | METPO:1000188 | DOI:10.1038/ismej.2014.60; DOI:10.1038/nrmicro3331 |
| traitmech:000100 | ploidy | METPO:1000188 | DOI:10.1159/000368855; DOI:10.1073/pnas.0707522105 |
| traitmech:000101 | rRNA operon copy number | METPO:1000188 | DOI:10.1128/AEM.66.4.1328-1333.2000; DOI:10.1038/nmicrobiol.2016.160 |
| traitmech:000102 | pangenome openness | METPO:1000188 | DOI:10.1073/pnas.0506758102; DOI:10.1038/nmicrobiol.2017.40 |

## Citation index (all DOIs/PMIDs verified)
| Reference | Work |
|-----------|------|
| DOI:10.1038/nrmicro1235 (PMID:16138100) | Frost et al., "Mobile genetic elements: the agents of open source evolution" (2005) |
| DOI:10.1128/MMBR.00020-10 (PMID:20805406) | Smillie et al., "Mobility of plasmids" (2010) |
| DOI:10.1128/MMBR.67.2.238-276.2003 (PMID:12794192) | Canchaya et al., "Prophage genomics" (2003) |
| DOI:10.1038/ismej.2017.16 (PMID:28291233) | Howard-Varona et al., "Lysogeny in nature" (2017) |
| DOI:10.1111/1574-6976.12067 (PMID:24499397) | Siguier, Gourbeyre & Chandler, "Bacterial insertion sequences" (2014) |
| DOI:10.1038/nrmicro884 (PMID:15100694) | Dobrindt et al., "Genomic islands in pathogenic and environmental microorganisms" (2004) |
| DOI:10.1111/j.1574-6976.2008.00136.x (PMID:19178566) | Juhas et al., "Genomic islands: tools of bacterial HGT and evolution" (2009) |
| DOI:10.1038/s41579-019-0299-x (PMID:31857715) | Makarova et al., "Evolutionary classification of CRISPR-Cas systems" (2020) |
| DOI:10.1016/j.molcel.2014.03.011 (PMID:24766887) | Barrangou & Marraffini, "CRISPR-Cas systems: prokaryotes upgrade to adaptive immunity" (2014) |
| DOI:10.1128/MMBR.00044-12 (PMID:23471617) | Vasu & Nagaraja, "Diverse functions of restriction-modification systems…" (2013) |
| DOI:10.3389/fmicb.2015.00528 | "Restriction-modification systems as engines of diversity" (2015) |
| DOI:10.1038/nrg2899 (PMID:21102527) | Plotkin & Kudla, "Synonymous but not the same: …codon bias" (2011) |
| DOI:10.1146/annurev.genet.42.110807.091442 (PMID:18983258) | Hershberg & Petrov, "Selection on codon bias" (2008) |
| DOI:10.1093/oxfordjournals.molbev.a025626 (PMID:8676740) | Lobry, "Asymmetric substitution patterns in the two DNA strands of bacteria" (1996) |
| DOI:10.1016/S0378-1119(99)00297-8 (PMID:10570985) | Frank & Lobry, "Asymmetric substitution patterns: a review…" (1999) |
| DOI:10.1038/nrmicro3331 (PMID:25220308) | Batut et al., "Reductive genome evolution at both ends of the bacterial population size spectrum" (2014) |
| DOI:10.1038/ismej.2014.60 | Giovannoni, Cameron Thrash & Temperton, "Implications of streamlining theory for microbial ecology" (2014) |
| DOI:10.1159/000368855 (PMID:25732342) | Soppa, "Polyploidy in archaea and bacteria…" (2014) |
| DOI:10.1073/pnas.0707522105 (PMID:18445653) | Mendell et al., "Extreme polyploidy in a large bacterium" (2008) |
| DOI:10.1128/AEM.66.4.1328-1333.2000 (PMID:10742207) | Klappenbach, Dunbar & Schmidt, "rRNA operon copy number reflects ecological strategies" (2000) |
| DOI:10.1038/nmicrobiol.2016.160 (PMID:27617693) | Roller, Stoddard & Schmidt, "Exploiting rRNA operon copy number…" (2016) |
| DOI:10.1073/pnas.0506758102 (PMID:16172379) | Tettelin et al., "…the microbial 'pan-genome'" (2005) |
| DOI:10.1038/nmicrobiol.2017.40 (PMID:28350002) | McInerney, McNally & O'Connell, "Why prokaryotes have pangenomes" (2017) |

## Validation
- Reuses the `PROPOSED` state + `scripts/audit_proposals.py` citation bar — no schema change.
- `just validate-strict` → 0 errors over **445** files; `audit-proposals` → **88/88** PROPOSED passing
  on this branch (74 prior + 14 genomics); `pytest` → 70 passed; genomics IDs 000089–000102; all
  `traitmech:` parent references resolve.

## Follow-ups (out of scope)
- Quantitative GC/genome bins, integron/integrative-conjugative-element specifics, DNA
  supercoiling/topology, oriC/replicon structure, anti-phage defense systems beyond CRISPR/R-M.
- Add evidence-backed `causal_graphs` + ontology groundings when promoted PROPOSED → REVIEWED.
- This completes the six-category gap sweep (environment, metabolism, ecology, morphology,
  physiology, genomics).
