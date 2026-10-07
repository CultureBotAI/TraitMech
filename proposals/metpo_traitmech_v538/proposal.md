# Fungal Rhizomorph Formation: METPO Proposal v538

## Context and Novelty

Add `traitmech:000662 fungal rhizomorph formation`, a PROPOSED MORPHOLOGY
class on base `6c9911a8ab8b0ba61a5b1b4b65d7300594a5d066`. This is a
reusable fungal formation phenotype, not a structure identifier, gene,
colony-outline label or individual observation.

Whole-repository searches included ignored and hidden files, rhizomorph,
rhizomorphic, mycelial/hyphal cord variants, source DOIs and proposed IDs.
No prior exact record, synonym, causal node or proposal was found. Structured
inspection of the 12,617-triple pinned METPO ontology found no matching
annotation. CommunityMech proposals were also searched with ignored and hidden
files included; the target and reserved block were unused. An all-state GitHub
search for rhizomorph across TraitMech and berkeleybop/metpo returned zero
indexed results with `incomplete_results: false`; this is not exhaustive
historical proof.

Fresh seeding produced 399 records, 344 shared with the pre-addition
1,056-record live corpus. The 55 absent IDs comprise 38 supporting fields
and 17 reviewed duplicates in the 153-row active-review table; the
1,546-row release-delta table was also read structurally. All 38 formerly
unselected classes are now live. Seed absence was not treated as novelty.
Further credible fungal trait leads remain; no global exhaustion is claimed.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The definition follows coordinated growth into root-like multihyphal
structures. It does not require a fixed hyphal count, black pigmentation,
underground growth, a hollow canal, a plant-like meristem, pathogenicity or
a universal transport function.

The existing `traitmech:000074 mycelial growth` is explicitly bacterial.
`METPO:1000674 filament shaped` concerns cell shape, while
`METPO:1007068 rhizoid colony` and `METPO:1007066 filamentous colony` concern
colony outline. `traitmech:000605 hyphal anastomosis` denotes fusion and
`traitmech:000660 fungal sclerotium formation` denotes compact resting bodies.
None is an exact existing trait or justified required parent. The phenotype
parent is an active class under `METPO:1000188 quality`; a closer fungal
growth-form parent remains an OPEN discussion rather than widening the
reviewed bacterial record.

Terminology is source-qualified. Koch et al. (2017) describe unmelanized
culture rhizomorphs. Oliveira et al. (2024) adopt a narrower melanized,
differentiated, organized-tip concept and distinguish mycelial cords from
Singer's white-rhizomorph usage. The original Singer/Rayner sources were not
retrieved. The broad formation definition preserves this discrepancy without
asserting exact cord/strand synonyms or settling the anatomical boundary.
No xrefs or SSSOM equivalences are asserted without authority-level review.

## Evidence and Example

| Reference | Directly Inspected Material |
| --- | --- |
| [10.1016/j.fgb.2009.04.005](https://doi.org/10.1016/j.fgb.2009.04.005) | Yafetto, Davis and Money (2009), PMID:19427390; scientific abstract from Europe PMC, not full text or figures |
| [10.1016/j.mycres.2005.09.006](https://doi.org/10.1016/j.mycres.2005.09.006) | Pareek, Allaway and Ashford (2006), PMID:16376531; abstract, Introduction, Methods, Results and Discussion from directly retrieved PDF; Table 1 and actual Figures 9-17 inspected |
| [10.1186/s12862-017-0877-3](https://doi.org/10.1186/s12862-017-0877-3) | Koch et al. (2017), PMID:28122504, PMC5264464; Discussion subsection on rhizomorph evolution and Table 2 from directly retrieved XML |
| [10.3114/fuse.2024.14.03](https://doi.org/10.3114/fuse.2024.14.03) | Oliveira et al. (2024), PMID:39830290, PMC11739697; PMC HTML abstract, Introduction and selected taxonomic text/captions; XML retrieval failed |

The 2009 scientific abstract is the strongest concise definition source.
The 2006 culture/microscopy study directly supports the canonical example
and is the strongest fully inspected experimental lead. The four snippets
are contiguous source spans of 16, 21, 25 and 22 words. The first two match
directly retrieved scientific abstracts; the third matches XML Discussion;
the fourth was checked directly against PMC Introduction text. A manual match
must not replace the maintained snippet resolver's actual verdict.

The canonical example is `NCBITaxon:153913 Armillaria luteobubalina`,
qualified to isolate 930199KGS. Primary Methods identify fruit-body origin
at Gore Hill Park, North Sydney, in June 1993 and the University of Western
Sydney culture collection. The record retains tested culture conditions,
not a species-wide guarantee. NCBI taxonomy efetch confirms ID, label and
species rank; natural origin is not inferred from a wild-type label.

The 2006 Results and Table 1 disagree on first tip appearance (day 6 versus
tips already counted on day 5). The record preserves the discrepancy, plate
denominator and distinction between air pores and rhizomorphs. Conductance
measurements using cut ends are not evidence for intact-rind permeability.
The 2009 osmolality-derived turgor estimate and force-derived contact pressure
are separate readouts, not thresholds. The 2017 culture/field contrast is an
author-attributed comparative summary, partly based on earlier literature,
not new experiments for every species or proof of absence in nature.

The remaining 2006 figure images and all supplements were not inspected.
The other papers' actual figures, complete Methods and additional isolate
provenance were not inspected. No extra canonical examples are inferred.
Physical growth and aeration have evidence; a protein-resolved formation
graph remains deferred pending additional perturbation evidence and verified
protein exemplars. Graph omission is not a claim that the mechanism is absent.

## ID Space and Subset

Reserve `METPO:1061500` in block `1061500-1061599`; v537 reserved
`1061400-1061499`. Before writing, the highest local ID was
`traitmech:000661` and the latest cohort was v537. Ignored-and-hidden searches
found no prior use of the local ID, cohort or reserved block. CommunityMech
v1 uses separate ranges `1007100-1007220` and `2007100-2007113`.
Subset: `metpo_traitmech_2026_10`. The live identifier remains the local ID
until an upstream release actually accepts an equivalent term.

Pinned kg-microbe `master` remains
`1408e7099d039026d7611c240938d8e177753406`. Its canonical class and
property headers were retrieved and decoded: 11 and 13 columns respectively.
Class blob: `b590cf303dc2fbdd57bed021668641cd0c32396d`.
Property blob: `b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`.
The class template preserves all three trailing empty directive cells.
METPO IRIs must expand to `https://w3id.org/metpo/`, not legacy purl stubs.

## Files and Mutation

| Artifact | Rows |
| --- | ---: |
| `metpo_proposal_classes_robot.tsv` | 1 class plus two headers |
| `metpo_proposal_properties_robot.tsv` | Not emitted; no predicates |
| `metpo_proposal_mappings.sssom.tsv` | Not emitted; no asserted equivalences |

`scripts/add_fungal_rhizomorph_formation_trait.py` defaults to dry-run,
prevalidates through `write_validated_trait`, guards an eight-field parent
projection and refuses target/template drift before writing. It deep-copies
the record and permits exact replay without changing existing records.
Twenty focused tests passed before application. The LLM-assisted mint event
and append-only repository history identify Codex explicitly:
`history/records/fungal_rhizomorph_formation/2026-10-07T100223Z-codex-52ca02.yaml`.

## Verification

Writer dry-run and 20 focused tests, single-record LinkML and strict validation,
proposal verification, ROBOT/ELK, history and product validation passed. History
validation found 1,143 records and zero invalid links. The online canonical
audit resolved all 739 examples across 554 records, with zero errors and
24 existing label warnings. The snippet resolver returned **2 VERIFIED,
2 NOT_IN_ABSTRACT**; the latter two spans were directly checked in full text,
not relabeled as abstract matches. Full `just qc` passed with no new snippet
findings and no changed baselines. Full pytest and PR review were pending
when this proposal was written; their final outcomes must be recorded on the
PR before merge.

Structured artifact comparison confirms all 1,056 existing trait YAMLs and
542 historical proposal TSVs are byte-identical. Of the old trait pages,
1,055 differ only in footer totals/coverage; phenotype additionally gains the
new child link. Its child count changes from 157 to 158, the only pre-existing
priority-row delta. Discussion templates and protected spore germination are
unchanged. The corpus now has 1,057 records and 718 unchanged causal graphs.

RDF inspection found 15 class-template, 12,628 merged and 12,632 reasoned
triples. The label, definition, source annotation and phenotype-to-quality
hierarchy are intact, with no legacy METPO purl stub. ELK found no
unsatisfiable class. These are RDF triple counts, not physical OWL lines.

Playwright passed at 1440x900 and 390x900 for identity, four source spans,
qualified example, two OPEN discussions, history link, parent/child navigation,
browse filtering and dashboard count/image loading. Screenshots were visually
inspected without overflow or browser errors.

Ordinary staged whitespace checking flags only the three required trailing
tabs in the ROBOT directive row. Both header widths were verified, and the
documented exception is scoped to that exact TSV; other staged files pass
the ordinary check.

The reviewed shared dashboard source snapshot `6d0a6fb` was rechecked against
tree `6a1ab0e03f518b8d76c261fda3d4119b70249782`; all 139 source blobs match.
Neither exact configured embedding source path exists, so embeddings will
not be regenerated. No dirty shared checkout is modified.

## Upstream Path and Round Trip

After TraitMech review, submit the TSV and scope questions to berkeleybop/metpo
or the kg-microbe proposal pipeline. This same-PR artifact is not replaced by
an upstream issue link. Review the fungal parent and competing anatomical
usages before acceptance.

After an upstream release mints the accepted term, update the pinned ontology,
seed into a temporary tree and compare the exact accepted definition and
hierarchy. Migrate only after equivalence review, preserve `traitmech:000662`
as provenance rather than an exact lexical synonym, reconcile downstream
references and append history. Regenerate pages, reports and coverage and
rerun all gates. Do not replace the local ID with an unreleased placeholder.

## Change Log

- 2026-10-07: Propose fungal rhizomorph formation with four DOI-backed snippets,
  an isolate-qualified example and explicit terminology/readout limits.
