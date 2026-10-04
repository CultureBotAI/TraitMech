# METPO Proposal v464: Photokinesis

## Context

Lift `traitmech:000587 photokinesis`, a light-dependent speed-response
trait supported by two primary papers:

- DOI:10.1128/AEM.67.12.5410-5419.2001 (PMID:11722886).
- DOI:10.1016/S0176-1617(00)80045-0 (PMID:12090268).

Temporary seeding emitted 399 identifiers: 344 present and 55 absent from
the pre-change 981-record corpus. Both frozen release-review tables were
checked against live records. Whole-repository searches included ignored
and hidden files, photokinesis/photo-kinesis, light-induced/dependent speed
phrases, citations, identifiers and the reserved block. No exact record,
METPO class or proposal was found. Nearby research mentions distinguish
phototaxis from motility and phototrophy; they remain valid. No exact YAML
node or synonym requires migration. The upstream METPO issue search was empty.

## Scope

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: local trait lift | 1 | motile | 1 |
| B: predicates | 0 | None proposed | 0 |
| C: schema enums | 0 | Outside this addition | 0 |

## Hierarchy Decisions

| Proposed ID | Local ID | Label | Parent |
|---|---|---|---|
| METPO:1054100 | traitmech:000587 | photokinesis | METPO:1000702 |

The parent denotes independent energy-dependent locomotion. The differentia
is light-dependent speed modulation, not direction. Neither increasing speed
nor a universal photosynthetic mechanism is required. Phototaxis and
photophobic responses are distinct and may coexist; no equivalence,
disjointness or parent-child relationship is asserted. The obsolete
`METPO:1000241` phototaxis class has neither a definition nor replacement
in the local OWL; it must not be revived as photokinesis. PHYSIOLOGY follows
the neighboring behavioral records.

## Evidence And Mapping Boundaries

The bacterial publisher full text and Figure 2A-B were inspected, including
methods, controls, caption and spectral convention. The algal abstract was
verified through Europe PMC; its subscription full text was not inspected.
Both evidence items contain contiguous snippets. Experimental qualifications
are in the record, including the negative oxic control. The second paper
concerns Chlamydomonas reinhardtii, not Euglena.

Natural-strain lineage and protein-resolved mechanisms remain open in two
discussions together with terminology boundaries. No canonical taxon,
universal receptor, exact synonym, equivalent xref or SSSOM mapping is
asserted. A mechanism graph is deferred, not labeled NONMECHANISTIC.

Source checks: 2026-10-04. No paid research was used.

## ID Space And Subset

Reserve `METPO:1054100-1054199`, using only `1054100`, after v463's
`1054000` block. Pre-write ignored-and-hidden searches found no collision.
The block is disjoint from the inspected CommunityMech v1 templates
(96 class rows, maximum 1008013; 19 property rows, maximum 2008002).
Subset: `metpo_traitmech_2026_10`.

## Files

| File | Data rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 1 |
| proposal.md | Narrative |
| Properties and SSSOM | Omitted: no predicate or equivalent mapping |

The refreshed upstream class template has 11 columns and three trailing
empty cells in the directive row. No property template is emitted.

## Verification

Run `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v464`,
`scripts/robot_validate_proposal.py proposals/metpo_traitmech_v464` and
`scripts/verify_metpo_proposal.py --coverage`. Actual validation and page
inspection results are recorded in the PR.

## Upstream Path

Submit the verified TSV to berkeleybop/metpo after TraitMech review.
The reserved placeholder is not an accepted or released METPO identifier.

## Round-Trip Plan

After upstream acceptance, refresh METPO, seed a temporary tree and migrate
to the released identifier while retaining `traitmech:000587` in provenance.
Regenerate affected artifacts; do not publish the placeholder as released.

## Change Log

- v464, 2026-10-04: add source-qualified photokinesis.
