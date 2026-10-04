# METPO Proposal v459: Rheotaxis

## Context

Lift `traitmech:000582 rheotaxis`, a reusable motile phenotype distinguished
by fluid-velocity-gradient-biased self-propelled movement. The two primary
sources are Marcos et al. (DOI:10.1073/pnas.1120955109) and Kaya and Koser
(DOI:10.1016/j.bpj.2012.03.001).

Fresh temporary seeding emitted 399 IDs: 344 present and 55 absent from the
976-record pre-change corpus. Both frozen release-review tables were inspected.
Whole-repository searches included ignored and hidden files, OWL, history,
research, proposals and pages, using rheotax/rheotact variants, primary
citations and flow-directed-movement descriptions. No exact existing record or
METPO term was found. Semantic-search hits were unrelated ontology-migration
history. The upstream METPO issue search for rheotaxis returned no result.

## Scope

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: local trait lift | 1 | motile | 1 |
| B: predicates | 0 | None required | 0 |
| C: schema enums | 0 | Not biological trait proposals | 0 |

## Hierarchy Decisions

| Proposed ID | Local ID | Label | Parent |
|---|---|---|---|
| METPO:1053600 | traitmech:000582 | rheotaxis | METPO:1000702 |

The reviewed parent denotes independent energy-dependent movement. Physical
orientation can bias powered locomotion without an active sensory circuit.
Passive advection is insufficient. Neither upstream direction nor a surface
is universally required, and chemotaxis is not the parent. No older trait is
edited. PHYSIOLOGY follows the behavioral scope of neighboring taxis traits.

## Evidence And Mapping Boundaries

- Marcos et al. distinguish bulk transverse rheotaxis from near-surface
  upstream movement. Their OI4139 smooth-swimming mutant is evidence, not
  a wild-type canonical example or a verified strain-168 protein anchor.
- Kaya and Koser's publisher-formatted article was inspected from the author
  institution's repository. Its K12 preparation underwent repeated motility
  selection; the canonical example retains that and the flow/surface context.
  No supplementary movies were viewed or numerical thresholds imported.
- A protein-resolved causal graph is explicitly deferred. The discussion
  names the missing experiment/strain/accession link; no synthetic protein
  identity or universal shear sensor is introduced to fill the graph.
- NCBI taxonomy resolves 83333 to Escherichia coli K-12. QuickGO returned no
  rheotaxis term. No exact synonym, xref or SSSOM equivalence is asserted.

Authority checks: 2026-10-04. Both evidence items have short contiguous
snippets; source interpretation is in notes.

## ID Space And Subset

Reserve `METPO:1053600-1053699`, using only `1053600`, after v458's
`1053500` block. Ignored-and-hidden allocation searches found no collision
with the local ID, cohort or block. This does not intersect CommunityMech v1
`1007100-1007220`. Subset: `metpo_traitmech_2026_10`. The proposed ID is
not a released METPO identity.

## Files

| File | Data rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 1 |
| proposal.md | Narrative |
| Properties and SSSOM | Omitted: no predicate or equivalent mapping |

The 11-column header follows the refreshed kg-microbe master template,
including three required trailing empty ROBOT header cells.

## Verification

Run `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v459`,
`scripts/robot_validate_proposal.py proposals/metpo_traitmech_v459` and
`scripts/verify_metpo_proposal.py --coverage`. Actual validation results,
source checks and page inspection are recorded in the PR.

## Upstream Path

Submit the verified TSV to berkeleybop/metpo after TraitMech review. This
local proposal does not establish upstream acceptance or a minted identifier.

## Round-Trip Plan

After upstream acceptance, refresh METPO, seed a temporary tree and migrate
to the released identifier. Preserve `traitmech:000582` in provenance and
regenerate affected artifacts. Do not emit the placeholder as released.

## Change Log

- v459, 2026-10-04: add rheotaxis with context-qualified primary evidence.
