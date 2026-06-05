# Candidate missing PHYSIOLOGY traits — literature-backed proposal

**Date:** 2026-06-04 · **Curator:** claude (LLM-assisted) · **Status of all entries:** `PROPOSED`

## Why these traits

The PHYSIOLOGY category (31 records) was **entirely trophic strategy** — every record is a
carbon/energy/electron-source mode (autotrophic, chemolithotrophic, photoheterotrophic, …) or a
nutrient-adaptation mode (oligotrophic/copiotrophic). It had **no coverage** of the broader
physiological *capabilities and responses* of cells: enzyme-activity phenotypes, stress responses,
dormancy states, and regulatory/behavioral physiology. This proposal adds **14 candidate traits**
across those gaps, each backed by **≥2 distinct, verified literature citations**, enforced by
`scripts/audit_proposals.py` in `just qc` / CI.

Authored as `TraitRecord` YAMLs in `data/traits/physiology/` with `mapping_status: PROPOSED`, minted
`traitmech:000075`–`traitmech:000088` (continuing env 000001–018, metab 000019–039, ecology
000040–055, morphology 000056–074). METPO pre-check confirmed all are absent. Traits parent to
`METPO:1000059` (phenotype) with two new intermediate axis classes.

### Scope / overlap avoidance
Deliberately excluded to avoid duplicating earlier rounds: osmotolerance/compatible solutes
(→ ENVIRONMENT salinity), secretion systems (→ MORPHOLOGY ultrastructure), antibiotic/secondary-
metabolite production (→ METABOLISM), and biofilm formation (already proposed under ECOLOGY).

## Proposed traits

### Enzyme-activity phenotypes (diagnostic physiology)
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000075 | catalase activity | METPO:1000059 | DOI:10.1007/s00018-003-3206-5; DOI:10.1038/nrmicro3032 |
| traitmech:000076 | oxidase activity | METPO:1000059 | DOI:10.3390/microorganisms10050926; DOI:10.1089/ars.2020.8039 |
| traitmech:000077 | urease activity | METPO:1000059 | DOI:10.1128/mr.59.3.451-480.1995; DOI:10.1128/mr.53.1.85-108.1989 |

### Stress responses
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000078 | stress response | METPO:1000059 | DOI:10.1146/annurev-micro-090110-102946; DOI:10.1038/nrmicro3032 |
| traitmech:000079 | oxidative stress response | traitmech:000078 | DOI:10.1038/nrmicro3032; DOI:10.1007/s00018-003-3206-5 |

### Dormancy & survival states
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000080 | dormancy | METPO:1000059 | DOI:10.1038/nrmicro2504; DOI:10.1038/nrmicro1557 |
| traitmech:000081 | viable but nonculturable state | traitmech:000080 | DOI:10.1111/j.1574-6976.2009.00200.x; DOI:10.1038/nrmicro2504 |
| traitmech:000082 | persister cell formation | traitmech:000080 | DOI:10.1146/annurev.micro.112408.134306; DOI:10.1038/nrmicro1557 |
| traitmech:000083 | spore germination | METPO:1000059 | DOI:10.1016/j.mib.2003.10.001; DOI:10.1038/nrmicro2504 |

### Regulatory, social & behavioral physiology
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000084 | quorum sensing | METPO:1000059 | DOI:10.1146/annurev.cellbio.21.012704.131001; DOI:10.1146/annurev.micro.55.1.165 |
| traitmech:000085 | bioluminescence | METPO:1000059 | DOI:10.1016/j.csbj.2018.11.003; DOI:10.1146/annurev.cellbio.21.012704.131001 |
| traitmech:000086 | chemotaxis | METPO:1000059 | DOI:10.1038/nrm1524; DOI:10.1038/nrmicro2505 |
| traitmech:000087 | natural competence | METPO:1000059 | DOI:10.1038/nrmicro3199; DOI:10.1038/s41579-021-00650-4 |
| traitmech:000088 | antibiotic resistance | METPO:1000059 | DOI:10.1038/nrmicro3380; DOI:10.1038/s41579-022-00820-y |

## Citation index (all DOIs/PMIDs verified)
| Reference | Work |
|-----------|------|
| DOI:10.1007/s00018-003-3206-5 (PMID:14745498) | Chelikani, Fita & Loewen, "Diversity of structures and properties among catalases" (2004) |
| DOI:10.1038/nrmicro3032 (PMID:23712352) | Imlay, "Molecular mechanisms and physiological consequences of oxidative stress" (2013) |
| DOI:10.3390/microorganisms10050926 | Hederstedt, "Diversity of cytochrome c oxidase assembly proteins in bacteria" (2022) |
| DOI:10.1089/ars.2020.8039 | Borisov et al., bacterial cytochrome bd-family oxidases (2021) |
| DOI:10.1128/mr.59.3.451-480.1995 (PMID:7565414) | Mobley, Island & Hausinger, "Molecular biology of microbial ureases" (1995) |
| DOI:10.1128/mr.53.1.85-108.1989 (PMID:2651866) | Mobley & Hausinger, "Microbial ureases: significance, regulation, and molecular characterization" (1989) |
| DOI:10.1146/annurev-micro-090110-102946 (PMID:21639793) | Battesti, Majdalani & Gottesman, "The RpoS-mediated general stress response in E. coli" (2011) |
| DOI:10.1038/nrmicro2504 (PMID:21233850) | Lennon & Jones, "Microbial seed banks: …dormancy" (2011) |
| DOI:10.1038/nrmicro1557 | Lewis, "Persister cells, dormancy and infectious disease" (2007) |
| DOI:10.1111/j.1574-6976.2009.00200.x (PMID:20059548) | Oliver, "…viable but nonculturable state in pathogenic bacteria" (2010) |
| DOI:10.1146/annurev.micro.112408.134306 (PMID:20528688) | Lewis, "Persister cells" (2010) |
| DOI:10.1016/j.mib.2003.10.001 (PMID:14662349) | Setlow, "Spore germination" (2003) |
| DOI:10.1146/annurev.cellbio.21.012704.131001 (PMID:16212498) | Waters & Bassler, "Quorum sensing: cell-to-cell communication in bacteria" (2005) |
| DOI:10.1146/annurev.micro.55.1.165 | Miller & Bassler, "Quorum sensing in bacteria" (2001) |
| DOI:10.1016/j.csbj.2018.11.003 | Brodl, Winkler & Macheroux, "Molecular mechanisms of bacterial bioluminescence" (2018) |
| DOI:10.1038/nrm1524 (PMID:15573139) | Wadhams & Armitage, "Making sense of it all: bacterial chemotaxis" (2004) |
| DOI:10.1038/nrmicro2505 | Porter, Wadhams & Armitage, "Signal processing in complex chemotaxis pathways" (2011) |
| DOI:10.1038/nrmicro3199 (PMID:24509783) | Johnston et al., "Bacterial transformation: distribution, shared mechanisms and divergent control" (2014) |
| DOI:10.1038/s41579-021-00650-4 | Arnold et al., "Horizontal gene transfer and adaptive evolution in bacteria" (2022) |
| DOI:10.1038/nrmicro3380 | Blair et al., "Molecular mechanisms of antibiotic resistance" (2015) |
| DOI:10.1038/s41579-022-00820-y (PMID:36411397) | "Molecular mechanisms of antibiotic resistance revisited" (2022) |

## Validation
- Reuses the `PROPOSED` state + `scripts/audit_proposals.py` citation bar — no schema change.
- `just validate-strict` → 0 errors over **445** files; `audit-proposals` → **88/88** PROPOSED passing
  (18 environment + 21 metabolism + 16 ecology + 19 morphology + 14 physiology); `pytest` → 70 passed;
  minted IDs contiguous 000001–000088; all `traitmech:` parent references resolve.

## Follow-ups (out of scope)
- Further physiology candidates: gelatinase/coagulase/other diagnostic enzymes, sporulation as a
  physiological program (morphology has the structural spore traits), cold/heat-shock responses,
  pH homeostasis, growth-rate/doubling-time quantitative traits, bacteriocin production.
- Add evidence-backed `causal_graphs` + ontology groundings when promoted PROPOSED → REVIEWED.
