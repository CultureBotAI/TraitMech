# METPO proposal v549: cyanophycin granule

## Context and scope

Lift `traitmech:000673`, a reusable intracellular storage-inclusion morphology,
as `METPO:1062600`. The record remains `PROPOSED` pending human review.

| Scope | New terms | Parent |
| --- | ---: | --- |
| A: local trait class | 1 | intracellular inclusion, traitmech:000066 |
| B: causal predicates | 0 | not applicable |
| C: schema enums | 0 | not applicable |

The TSV also includes the parent's existing `METPO:1007665` context from v5.
Its identity, definition, source, parent and fallback link are unchanged; only
the subset is updated to this cohort's `metpo_traitmech_2026_10`. The source
v5 template and parent YAML are not modified. This is not a new parent allocation.

## Scientific boundaries

This is the cyanophycin-containing inclusion, not the polymer molecule,
soluble synthesis, a CphA sequence feature, or arbitrary nitrogen storage.
The parent matches the existing PHA and polyphosphate granule hierarchy.
Neither a fixed shape/size nor constitutive occurrence is required.
The 2001 enzyme paper's cyanobacteria-only wording is not imposed: the 2018
primary paper also reports cyanophycin distribution in heterotrophic bacteria.
Engineered amino-acid variants and soluble polymer production alone do not
establish the morphology. CGP is not asserted as an exact granule synonym.

Primary references, with deliberately short verbatim excerpts in the record:

- [Watzer and Forchhammer 2018](https://doi.org/10.1128/AEM.01298-18):
  definition authority and PCC 6803 cell biology. Main text, Methods and
  supplemental captions were read; actual figure images were not inspected.
  Reporter localization, deletion effects and magnesium effects in extracts
  have distinct experimental scopes. No universal growth advantage is asserted.
- [Li et al. 2001](https://doi.org/10.1007/s002030100281): directly retrieved
  publisher scientific abstract, including granule microscopy/biochemistry
  during nitrogen-fixing light/dark culture of ATCC 51142. Paywalled full text
  and figures were not read.
- [Aboulmagd et al. 2000](https://doi.org/10.1007/s002030000206):
  DOI-matched Europe PMC scientific abstract (PMID:11131019), supporting
  functional expression of PCC 6308 CphA in a heterologous host. Full text
  was not inspected.
- [Aboulmagd et al. 2001](https://doi.org/10.1128/AEM.67.5.2176-2182.2001):
  purified PCC 6308 enzyme and polymer output. Publisher abstract, Methods,
  Results and Tables 2/3 were read; actual figure images were not inspected.

The canonical example uses current NCBI name Crocosphaera subtropica ATCC
51142 (`NCBITaxon:43989`, rank no rank), historically Cyanothece. NCBI links
BH68/BH68K; the directly read [1993 isolation-paper abstract](https://doi.org/10.1128/jb.175.5.1284-1292.1993)
supports its natural provenance. That citation is provenance, not independent
cyanophycin evidence.

The five-node/four-edge graph integrates distinct source taxa, not one
experiment in the canonical organism. Reviewed `UniProtKB:P56947` is the
PCC 6308 CphA instance (`NCBITaxon:113355`, Geminocystis herdmanii PCC 6308),
entry version 91, sequence version 2, checked 2026-10-08. UniProt links
AF220099/AAF43647.2 and both enzyme papers; E. coli is the expression host,
not its source taxon or a natural trait exemplar. Generic protein grounding
`InterPro:IPR011810` denotes the family, not an ATP-grasp domain.
`CHEBI:65318` denotes the polymer, not an equivalent trait. Both were checked
at their issuing authorities. No record-level xrefs or SSSOM equivalences
are proposed. Existing RO/biolink predicates need no new allocation.

## Allocation and novelty

Reserve the entire **METPO:1062600-1062699** block; only 1062600 is used.
Local ID: **traitmech:000673**. This follows v548/1062500-1062599.
At allocation, main was `f16cadbfc9d8d11f95dcf751e456b0fc2ebef068`.
Ignored-and-hidden searches covered all then-existing TraitMech worktrees,
the whole CommunityMech checkout, and complete changed curation artifacts
from every open PR, including drafts. Searches included spelling variants,
CGP, all four primary citations, protein/family identifiers, the local ID,
cohort and full block. Dependency/cache mentions were not prior traits or
reservations. The pinned METPO graph contained 12,617 triples and no exact
cyanophycin-granule term. Existing inclusion, PHA and polyphosphate records
were read for semantic deduplication. No exact existing node needed repair.

Complete paginated open-head snapshot at allocation:

| PR | Head | Relevant curation reservation |
| --- | --- | --- |
| #1802 | `5d6cd392e31cc929313e6a8fcbb77af94a3405d9` | existing Shedu trait, no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `a138e46f803b5af9d48969217b86cf7c9a3b61bd` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

Main, worktrees and current open heads must be rechecked before publication.
The CommunityMech v1 class/property cohorts and extensions were read; their
ranges do not overlap this block.

## Artifacts and verification

The class TSV has two headers, one dependency-context row and one new class.
No property or SSSOM file is needed. Pinned upstream kg-microbe commit
`1408e7099d039026d7611c240938d8e177753406` has class header blob
`b590cf303dc2fbdd57bed021668641cd0c32396d` (11 columns) and property header
blob `b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (13 columns).
The three empty class directive cells remain intact.

Run before merge:

```bash
just verify-proposal metpo_traitmech_v549
just robot-validate-proposal metpo_traitmech_v549
just qc
```

Inspect emitted RDF for `https://w3id.org/metpo/` child and parent IRIs,
the parent's label, and its hierarchy through phenotype to quality. Keep
snippet resolver results separate from direct full-text/abstract inspection.
Run live canonical-taxonomy, UniProt and maintained ID-label audits, plus
focused writer tests, full pytest and generated-page browser inspection.
Original history is append-only: #1816 corrects the initial event's mistakenly
future timestamp by an explicit appended provenance event, not a rewrite.

## Upstream and round trip

Submit this template and narrative to berkeleybop/metpo or the kg-microbe
proposal pipeline after TraitMech review. No separate upstream issue or
released METPO term is claimed. After acceptance, refresh the ontology,
re-seed and migrate the record and its graph grounding to the accepted ID,
preserving the local identifier as traceability metadata and both history
trails. Keep unresolved assembly/degradation and synonym questions open.

## Change log

- v549, 2026-10-08: cyanophycin storage inclusion and source-bounded mechanism.
