# METPO Proposal v461: Gravitaxis

## Context

Lift `traitmech:000584 gravitaxis`, an organismal disposition for
gravity-relative directional swimming. Primary evidence comes from
Nasir et al. (DOI:10.1038/s41598-018-26046-8) and Roberts
(DOI:10.1242/jeb.050666), not a sequence-feature prediction.

Temporary seeding emitted 399 identifiers: 344 present and 55 absent from
the pre-change 978-record corpus. Both frozen release-review tables were
read and checked against live records. Whole-repository searches included
ignored and hidden files, labels, geotaxis/gravitactic alternatives,
citations, GO and taxon identifiers, protein accessions and the proposed
ID block. Only gyrotaxis boundary notes mentioned the candidate; no exact
record, METPO class or unresolved exact graph node was found. The upstream
METPO issue search returned no gravitaxis result.

## Scope

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: local trait lift | 1 | motile | 1 |
| B: predicates | 0 | None proposed | 0 |
| C: schema enums | 0 | Outside this addition | 0 |

## Hierarchy Decisions

| Proposed ID | Local ID | Label | Parent |
|---|---|---|---|
| METPO:1053800 | traitmech:000584 | gravitaxis | METPO:1000702 |

The parent denotes energy-dependent locomotion; directional bias need not
require an active receptor. Passive settling and speed changes alone are
insufficient. PHYSIOLOGY follows neighboring behavioral taxis records.
Gyrotaxis names a torque-mediated mechanism rather than this directional
phenotype. The two may overlap, but no equivalence, disjointness or new
subsumption between them is asserted in this addition. Existing gyrotaxis
boundary notes remain correct; no older trait YAML is edited.

## Evidence And Mapping Boundaries

- Both DOI evidence items have short contiguous snippets. Nasir's main text
  and supplement were inspected, including visual checks of the quoted
  introduction and supplementary panels. The record uses the actual
  flagellar-length panel 5e rather than the main-text pointer to 5c.
- The Euglena example retains culture and control-treatment qualifiers.
  Roberts' publisher text supports the Paramecium example and a physical
  orientation interpretation, not a universal rejection of gravity sensors.
  Equation images and any Roberts supplement were not inspected.
- NCBI resolves 3039 to Euglena gracilis and 5885 to Paramecium caudatum,
  both species rather than strain identifiers.
- QuickGO resolves active GO:0042332 as a biological process, with geotaxis
  among its lexical synonyms. No equivalent disposition xref or SSSOM
  mapping is asserted merely from that name match.
- A causal graph is deferred explicitly, not because mechanism evidence is
  absent. UniProt's exact EU935858 match is unreviewed B5THA2 without a
  Proteomes cross-reference; an EgPCDUF4201 name query returned no hit.
  Neither result licenses a substitute paralog or a claim of sequence
  absence. The physical branch also needs faithful representation under
  the current protein-requiring MECHANISTIC audit. Two discussions preserve
  these mapping, scope and grounding decisions.

Authority checks: 2026-10-04. No new protein instance is asserted.

## ID Space And Subset

Reserve `METPO:1053800-1053899`, using only `1053800`, after v460's
`1053700` block. Ignored-and-hidden searches found no collision with the
local identifier, cohort or block. The block does not intersect CommunityMech
v1 `1007100-1007220`. Subset: `metpo_traitmech_2026_10`.

## Files

| File | Data rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 1 |
| proposal.md | Narrative |
| Properties and SSSOM | Omitted: no predicate or equivalent mapping |

The 11-column header matches the refreshed kg-microbe class template,
including three trailing empty cells in the ROBOT directive row.

## Verification

Run `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v461`,
`scripts/robot_validate_proposal.py proposals/metpo_traitmech_v461` and
`scripts/verify_metpo_proposal.py --coverage`. Actual validation results and
rendered-page checks are recorded in the PR.

## Upstream Path

Submit the verified TSV to berkeleybop/metpo after TraitMech review.
The reserved placeholder is not an accepted or released METPO identifier.

## Round-Trip Plan

After upstream acceptance, refresh METPO, seed a temporary tree and migrate
to the released identifier while retaining `traitmech:000584` in provenance.
Regenerate affected artifacts; do not publish the placeholder as released.

## Change Log

- v461, 2026-10-04: add gravitaxis with primary evidence and bounded examples.
