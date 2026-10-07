# Mitophagy: METPO Proposal v515

> Parent scope correction (2026-10-06, #1754): use v519's corrected
> `METPO:1059100` autophagy context when combining proposals. This cohort's
> TSV remains unchanged; its mitophagy row and allocation are unaffected.

## Context

Add `traitmech:000639 mitophagy`, a PROPOSED PHYSIOLOGY class, on base
`4f6c030329b373a698e8fafaf181f795ab491900`. This is a reusable selective
organelle-turnover phenotype, not a gene, sequence feature, detector
profile or bacterial induction of an animal host response.

Whole-repository searches included ignored and hidden files, candidate
labels, mitochondrial-turnover variants, source identifiers, the local
identifier and prospective 1059200-1059299 block. CommunityMech proposals
were included. No exact record or reservation was found. A preliminary
bare-number search also found an unrelated matplotlib decimal; the
CURIE/IRI-qualified search found no allocation. Complete all-state GitHub
queries for mitophagy in TraitMech and METPO, and 1059200 upstream, returned
zero results.

The pre-addition corpus has 1,033 records. A freshly generated 399-record
seed shares 344 IDs; its 55 absent IDs comprise 38 supporting-field terms
and 17 reviewed duplicates. All 38 formerly unselected classes are now
live. The full 1,546-row release delta and 153-row active review were parsed.
All 12,617 pinned METPO triples were checked for candidate terminology and
the new block, with no hit. This establishes local novelty, not exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | traitmech:000638 autophagy / METPO:1059100 |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Selective mitochondrial degradation distinguishes the child from broad
autophagy. Nonspecific capture during bulk turnover, marker recruitment,
organelle fragmentation, depolarization and gene presence alone are not
the endpoint. Neither universal starvation nor damaged-only cargo is
required. Existing extracellular proteolysis, uptake/feeding, secretion,
prokaryotic inclusions and chemical-compartmentalization properties are
not equivalent or better parents. No same-scope graph or synonym needs
repair, and no existing trait YAML changes.

This draft follows the selective-turnover usage explicitly named in the
fission-yeast Results, while retaining the 2007 selective/microautophagic
context. It does not make the membrane route universal. The issuing
[GO records](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000422,GO%3A0000423,GO%3A0000424)
were directly resolved: GO:0000423 uses mitophagy for selective
macroautophagy, GO:0000424 micromitophagy is not its child, and broader
GO:0000422 lists mitophagy as a narrow synonym. These process-level and
route-specific distinctions remain an OPEN human-review discussion;
no exact xref, synonym or SSSOM mapping is asserted.

The TSV includes the v514 autophagy row unchanged as dependency context,
not a newly minted class or a second allocation. This gives standalone
ROBOT output the actual autophagy -> phenotype -> quality ancestry.
The writer checks both the live parent's eight-field projection and its
complete original proposal before any write. Parent YAML and v514 stay
unchanged. Upstream should deduplicate the identical context row when
combining these cohorts.

## Evidence and Limits

| DOI | PMID | Quote Words | Source and Role |
| --- | --- | ---: | --- |
| 10.7554/eLife.61245 | 33138913 | 16 | Full-text Results s2-2; definition and selectivity |
| 10.1016/j.devcel.2009.06.014 | 19619495 | 15 | Scientific Abstract; distinction from other autophagy |
| 10.1016/j.devcel.2009.06.013 | 19619494 | 15 | Scientific Abstract; qualified receptor proposal |
| 10.4161/auto.4034 | 17377488 | 20 | Scientific Abstract; selective/nonselective route boundary |

All four short spans directly match retrieved primary text. The maintained
abstract-only resolver returns three VERIFIED rows at 1.00 and one
NOT_IN_ABSTRACT at 0.40 for the full-text quote. That inconclusive result
is preserved, not relabeled VERIFIED. The latter span was independently
exact-matched in the scientific Results of PMC7609059, separate from its
Abstract and embedded review correspondence.

For 2020, Results s2-1/s2-2, selected other body passages, Methods
s4-1/s4-5/s4-8, actual Figure 1 and its first figure supplement were read.
The partial allele, full deletion, complementation, protease control and
weak residual Tom70 processing are distinguished in the record. Other
actual figures, complete Methods and Key Resources Table were not audited.
The two 2009 and 2007 studies have directly retrieved scientific abstracts;
their full methods, actual figures and strain provenance were not inspected.
The Atg32 receptor interpretation retains the authors' proposal language.

The record has no canonical examples or protein graph: independent natural
strain provenance and accession-level taxon-paired functional grounding
remain unresolved. Atg43 and Atg32 findings are not a universal gene list.
Two OPEN discussions retain these limits. PROPOSED status requires human
signoff; neither snippet matching nor CI supplies that signoff.

## ID Space and Files

Reserve `METPO:1059200` in the fresh 1059200-1059299 block, following v514.
Local ID: `traitmech:000639`; subset: `metpo_traitmech_2026_10`.
`METPO:1059100` remains the existing v514 parent allocation. No collision
with CommunityMech proposals was found, including ignored files.
The upstream kg-microbe contract was rechecked at
`1408e7099d039026d7611c240938d8e177753406`; both 11-column header rows match
its immutable class template. Use w3id METPO IRIs, not legacy purl stubs.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class + 1 unchanged parent-context class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The writer dry run, 22 focused tests, Ruff and single-record LinkML
validation passed. Tests cover selectivity, source-section limits,
parent/template identity, dry-run immutability, replay, drift refusal and
validation before writes. Direct quote and upstream-header checks passed;
the exact resolver outcomes are recorded above.

Strict validation, history/products validation, `just qc`, proposal and
cross-cohort verification, ROBOT/ELK and Ruff passed. Full pytest passed
2,480 tests with two dependency warnings in 611.95 seconds; the 45 focused
dashboard/README/priority tests passed separately in 326.78 seconds.
The emitted w3id child, labeled autophagy parent and phenotype/quality
ancestry were inspected with an RDF parser: classes, merged and reasoned
graphs contain 25, 12,638 and 12,642 triples respectively.

The artifact audit confirmed that all 1,033 pre-existing trait YAMLs and
the parent proposal remain byte-identical. Existing pages have footer-only
changes except autophagy's new child link; its only priority-row change is
children 0 -> 1. Shared discussion templates and the protected record remain
unchanged. The live corpus has 1,034 records, 519 PROPOSED records and 153
PHYSIOLOGY records. Both configured embedding source paths are absent, so
embedding artifacts were not regenerated.

Desktop/mobile browser checks at 1440/390 pixels passed, including identity,
four quotes, two OPEN discussions, parent/child navigation, the QC count,
coverage-image loading and no horizontal overflow. Screenshots were inspected.
Canonical-example shape validation passed; taxon resolution was not run because
no examples were added. Staged-file PR sanity passed.

The ROBOT directive header retains three required empty trailing cells.
The ordinary staged whitespace check flagged only those required tabs;
the documented exact-file scoped checks passed without trimming cells or
weakening global checks. PR review, committed-history validation, exact-head
CI, native queue and verified landing will be recorded on the PR.

## Upstream and Round Trip

Submit the new class together with the existing autophagy dependency for
METPO review. On acceptance, refresh the ontology, migrate the identifier
and parent references to accepted METPO IDs, retain minting provenance and
append-only history, and regenerate without duplicate primary records.
The route-scope and exemplar/mechanism discussions remain OPEN.

## Change Log

- v515, 2026-10-06: propose microbial mitophagy with four DOI-backed quotes,
  explicit scope and access limits, and unchanged autophagy parent context.
