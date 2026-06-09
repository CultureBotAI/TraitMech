# Leftover candidate traits — literature-backed proposal

**Date:** 2026-06-08 · **Curator:** claude (LLM-assisted) · **Status of all entries:** `PROPOSED`

## Why these traits

Mops up the small deferred items flagged across the category rounds: two more
biopolymer-degradation processes and the classic coccal cell arrangements that
complement the existing `diplococcus shaped`. **6 candidate traits**, each backed by
**≥2 distinct, verified literature citations**, enforced by `scripts/audit_proposals.py`.

Minted `traitmech:000115`–`traitmech:000120`. Degradation traits parent to the existing
`traitmech:000110` (biopolymer degradation, from metabolism round 2); arrangements parent to
`METPO:1000666` (cell shape), matching the existing `diplococcus shaped`. (Aerobic methanotrophy
was deliberately skipped — physiology already has the `methanotrophic` trophic-mode class.)

## Proposed traits
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000115 | starch degradation | traitmech:000110 | DOI:10.1016/S0168-1656(01)00407-2; DOI:10.1093/nar/gkt1178 |
| traitmech:000116 | proteolysis | traitmech:000110 | DOI:10.1128/mmbr.62.3.597-635.1998; DOI:10.1093/femsre/fuab046 |
| traitmech:000117 | streptococcus arrangement | METPO:1000666 | DOI:10.1128/MMBR.00001-06; DOI:10.1038/ncomms4842 |
| traitmech:000118 | staphylococcus arrangement | METPO:1000666 | DOI:10.1128/MMBR.00001-06; DOI:10.1038/ncomms4842 |
| traitmech:000119 | tetrad arrangement | METPO:1000666 | DOI:10.1128/MMBR.00001-06; DOI:10.1038/ncomms4842 |
| traitmech:000120 | sarcina arrangement | METPO:1000666 | DOI:10.1128/MMBR.00001-06; DOI:10.1038/ncomms4842 |

## Citation index (verified)
| Reference | Work |
|-----------|------|
| DOI:10.1016/S0168-1656(01)00407-2 | van der Maarel et al., "Properties and applications of starch-converting enzymes of the α-amylase family" (2002) |
| DOI:10.1093/nar/gkt1178 | Lombard et al., "The carbohydrate-active enzymes database (CAZy)" (2014) |
| DOI:10.1128/mmbr.62.3.597-635.1998 | Rao et al., "Molecular and biotechnological aspects of microbial proteases" (1998) |
| DOI:10.1093/femsre/fuab046 | "Ins and outs of Bacillus proteases…" (FEMS Microbiol. Rev. 2021) |
| DOI:10.1128/MMBR.00001-06 (PMID:16959965) | Young, "The selective value of bacterial shape" (2006) |
| DOI:10.1038/ncomms4842 | (repo) daughter-cell separation during bacterial cell division |

## Validation
- `just validate-strict` → 0 errors over **477** files; `audit-proposals` → **120/120** PROPOSED
  passing on this branch; `pytest` → 70 passed; IDs 000115–000120; all `traitmech:` parent refs resolve.
