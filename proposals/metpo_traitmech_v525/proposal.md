# Extracellular Membrane Vesicle Production: METPO Proposal v525

## Context

Add `traitmech:000649 extracellular membrane vesicle production`, a PROPOSED
PHYSIOLOGY class, on base `29871fd90cddc7073736947ae2b9da6a74357e33`.
This records an organismal phenotype, not a vesicle material entity, a
sequence feature, or an inference from vesicle cargo.

Ignored-and-hidden whole-repository searches covered terminology, slugs,
vesiculation, biogenesis/release, source DOI/PMID bundles and prospective
identifiers, including CommunityMech proposals. Existing mentions concern
RodZ-associated shape, L-form proliferation, gas vesicles, predation,
metabolism or gene transfer. None is an exact production-trait record or
an unresolved exact causal node that needs reassignment.

A fresh seed contains 399 records; 344 identifiers occur in the pre-addition
1,043-record corpus. The 55 absent seed terms are 38 supporting-field terms
and 17 reviewed duplicates. All 38 formerly unselected classes are now live.
Structured review covered 1,546 release-delta rows, 153 active-review rows
and the 12,617-triple ontology. The gas-vesicle neighbor is obsolete and
not exact; the secretion neighbors are also obsolete. This demonstrates
candidate novelty, not exhaustion of microbial-trait discovery.

All-state GitHub searches found no indexed exact candidate or new block
reservation. Upstream [#269](https://github.com/berkeleybop/metpo/issues/269)
concerns intracellular inclusions, and
[#57](https://github.com/berkeleybop/metpo/issues/57) lists gas vesicles and
broad secretion-system labels. Their bodies and comments were inspected.
The [PR #1761 landing receipt](https://github.com/CultureBotAI/TraitMech/pull/1761#issuecomment-6024036782)
already names this research lead without allocating it; index silence does
not erase that prior mention.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The endpoint is intact extracellular lipid-membrane vesicles. The definition
does not require viable producers, intact-vesicle release before lysis,
one membrane architecture, a size threshold, a particular cargo or an
ecological benefit. Production includes the observed post-lysis reassembly
route. Mere blebbing, unclosed fragments, gas vesicles, intracellular
vesicles, daughter cells and virions do not establish this trait.

Exocytosis (`traitmech:000637`) describes fusion-pore discharge, a different
axis. The yeast source implicates conventional and unconventional traffic;
therefore `traitmech:000648` is not a universal parent. Overlap is not
disjointness. Outer-membrane vesicles and exosomes are not asserted as exact
synonyms. No existing records are reparented. Exact external equivalences
remain unresolved, so xrefs, synonyms and SSSOM mappings are omitted.

## Evidence and Limits

| DOI | PMID | Role |
| --- | --- | --- |
| 10.1038/ncomms11220 | 27075392 | Definition and lytic membrane reassembly; PMC4834629 |
| 10.1038/s41467-017-00492-w | 28883390 | Wall-hole extrusion; PMC5589764 |
| 10.1371/journal.pone.0011113 | 20559436 | Yeast production and trafficking boundary; PMC2885426 |
| 10.1038/s41467-025-60272-9 | 40461479 | Archaeal production and strain example; PMC12134362 |

Four snippets come from directly read Europe PMC XML. The first three are
scientific-abstract spans, not editorial teasers; the fourth is Results
Sec3. Selected Results and Methods were also read. Actual panels and
supplements remain visually uninspected. The bacterial papers share
investigators and are not independent-laboratory replications.

One canonical example is `NCBITaxon:420247 Methanobrevibacter smithii ATCC
35061`, qualified to PS cultures and supported by the 2025 paper. NCBI
Taxonomy resolves the strain and its parent species 2173. The
[DSMZ record](https://www.dsmz.de/collection/catalogue/details/culture/DSM-861)
supplies strain provenance, not independent trait evidence. No in-gut assay
or increase in methane output is claimed.

Two OPEN discussions retain mapping and mechanism work. A route-specific
graph needs remaining figure/strain review and taxon-paired protein
grounding; the current evidence does not imply one universal apparatus.
This is not an assertion that no mechanisms are known.

## ID Space and Files

Reserve fresh block 1060200-1060299, using `METPO:1060200`, after v524's
1060100 block. Local ID: `traitmech:000649`.
Subset: `metpo_traitmech_2026_10`. Earlier cohorts remain unchanged.

The upstream repository is `Knowledge-Graph-Hub/kg-microbe`, not
`monarch-initiative/kg-microbe` (the latter returned 404). Current contract
and template blobs were verified at
`1408e7099d039026d7611c240938d8e177753406`; headers have 11/13 columns.
The configured sibling skill path is absent. CommunityMech v1 and TraitMech
v1 were read as worked examples. No local, CommunityMech or pinned-upstream
candidate/block collision was found. The writer guards parent scope,
rejects target/template drift, prevalidates and defaults to dry run.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

Production dry run, guarded apply and 20 focused writer tests passed.
Direct LinkML, single-record strict validation, history/products and the
proposal verifier passed. ROBOT ELK passed without UNSAT; parsed RDF has
15 class-template, 12,628 merged and 12,632 reasoned triples. The child
attaches to the real w3id METPO phenotype/quality hierarchy, not a legacy
OBO-prefix stub. Full corpus QC and Ruff passed. The complete local suite
passed 2,810 tests with two dependency deprecation warnings; the separate
artifact-focused run passed 45 tests. Committed-history and required PR/queue
checks remain required before merge; their results will be recorded on the PR.

All four snippets exact-match contiguous source XML with markup removed
and whitespace normalized. The maintained abstract resolver reports two
VERIFIED, one LIKELY_PARAPHRASE and one NOT_IN_ABSTRACT. The apparent
paraphrase is exclusively the API's `100-300` versus the XML's `100–300`;
the stored quote preserves the directly read XML. The non-abstract match
is the explicitly identified 2025 Results Sec3 span. These actual resolver
outcomes are retained, not relabeled as four automated verifications.
The NCBI-backed canonical-example audit resolved all 728 examples with
zero errors and 24 pre-existing label-drift warnings; the new strain matches.

All 1,043 prior YAML records, including the protected record, are unchanged.
The 1,042 non-parent pages change only in their corpus footers; phenotype
gains the new child. Its priority child count changes from 144 to 145.
All 529 historical templates and previous proposal narratives are unchanged.
The shared generator was verified against all 139 source blobs of reviewed
commit `6d0a6fbbaeec47f42c6f999233b460e3f56bae89` before regeneration.
The new corpus contains 1,044 records and 590 discussions across 515 records.

Playwright checks at 1440 and 390 px passed identity, four quotes, the
qualified example, two OPEN discussions, hierarchy navigation and dashboard
counts/image loading, with no page errors or overflow. Screenshots were
visually inspected. The configured embedding sources are absent, so
embedding artifacts were not regenerated.

The ordinary staged whitespace check flags only the three required empty
trailing cells in the ROBOT directive row. Both headers have 11 columns.
After inspecting that exact line, the checks excluding only this template
and disabling blank-at-EOL only for this template passed. Required cells
were not trimmed and global Git whitespace settings were not weakened.

## Upstream and Round Trip

Submit the class and scope notes to upstream METPO after review. The issues
above are not an existing proposal for this class; no new upstream issue
has been opened. After acceptance, refresh the ontology, migrate the local
identifier and references to the accepted METPO ID, preserve local
provenance and append-only history, and regenerate products without
creating a duplicate record. Scientific discussions require separate review.

## Change Log

- v525, 2026-10-06: propose extracellular membrane vesicle production with
  bacterial, yeast and archaeal evidence and a strain-qualified exemplar.
