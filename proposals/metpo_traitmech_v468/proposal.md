# pH Taxis: METPO Proposal v468

## Context

TraitMech mints `traitmech:000591 pH taxis` as a PROPOSED organismal
motility phenotype supported by two primary studies. External-pH-directed
movement is distinct from growth preference, tolerance and pH homeostasis.

The fresh temporary seed has 399 identifiers, 344 present and 55 absent in
the pre-change 985-record corpus. Structured OWL search found no exact
pH-taxis term. Both frozen release-review tables were examined alongside
the live corpus. Whole-repository novelty searches included ignored and
hidden files, pH-taxis spelling variants, both DOI/PMID pairs and the new
identifier reservations. Only the chemotaxis research report and its
rendered copy mention pH taxis as a separate trait; no exact causal node,
synonym or discussion requires reconciliation. The upstream METPO issue
search returned no pH-taxis result.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000702 motile | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One record uses the new identity. No predicate or schema enum is lifted.
This is a reusable gradient-response phenotype, not a precomposed
organism-chemical utilization assertion.

## Hierarchy Decisions

The active `METPO:1000702 motile` parent denotes independently powered
locomotion. The new child adds directional response to external pH.
The local chemotaxis record imposes flagellar motor switching and is not
used to impose that apparatus universally. Growth pH preference and
tolerance do not imply taxis. Neither bidirectionality nor attraction to
neutral pH is a universal requirement. No external equivalent xref or
SSSOM mapping is asserted without authority and organismal-scope checks.

## Evidence

- Tohidifar et al., DOI:10.1128/jb.00491-19, PMID:31685537:
  abstract supports bidirectional external-pH taxis in Bacillus subtilis.
  Its neutral-pH preference is study-specific, not the class definition.
- Croxen et al., DOI:10.1128/jb.188.7.2656-2665.2006, PMID:16547053:
  abstract supports acid avoidance in Helicobacter pylori without requiring
  bidirectional attraction to a neutral optimum.

Both short snippets were checked against the exact Europe PMC abstracts.
Full texts and supplements were not systematically inspected. No receptor
mechanism, host-colonization requirement or canonical strain is inferred.
Two open discussions defer external equivalents, natural strain provenance,
taxon resolution and protein-resolved mechanism curation. The record stays
PROPOSED until human curator signoff.

## ID Space And Subset

Reserve `METPO:1054500` in block 1054500-1054599, following v467's
1054400-1054499 block. Ignored-and-hidden collision searches were empty.
The CommunityMech v1 ranges are disjoint. Subset: `metpo_traitmech_2026_10`.
The proposed placeholder is not an accepted identity; the record uses
`traitmech:000591`.

## Files

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus two header rows |
| Properties template | Omitted: no properties |
| SSSOM mappings | Omitted: no verified equivalent alignment |
| proposal.md | This narrative |

## Verification

LinkML and strict validation, cohort and cross-cohort coverage verification,
ROBOT/ELK with emitted-RDF inspection, both snippet checks, full QC and
history/product validation pass. Seven writer tests and 45 artifact/priority
tests pass. The PR records the full-suite result and independent review.
History validation covers 1,020 records with zero invalid. The emitted class
points to the real labeled motile parent and its hierarchy, without a legacy
METPO stub. Desktop (1440px) and mobile (390px) Chrome checks pass with two
evidence items, no canonical example claims, correct local identifier
provenance, a rendered 986-record QC dashboard and no overflow/page errors.
All 984 ordinary existing trait-page changes are footer counts; motile also
gains the expected child link. Both configured embedding inputs are absent,
so embedding artifacts were not regenerated.
The canonical class template has 11 columns, including three trailing empty
ROBOT directive cells. METPO IDs expand to `https://w3id.org/metpo/`;
the upstream skill's legacy-prefix command is not copied.

## Upstream Path

After review, submit the class TSV to berkeleybop/metpo or the KG-Microbe
proposal pipeline. Do not export the placeholder as an accepted METPO ID.

## Round-Trip Plan

After upstream acceptance, refresh the pinned ontology and seed a temporary
tree. Migrate to the actual accepted CURIE, preserve the local identifier
in traceability metadata, and reconcile references and proposal status in
a separately reviewed change.

## Change Log

- v468, 2026-10-04: one evidence-backed pH-taxis class, curated by codex.
