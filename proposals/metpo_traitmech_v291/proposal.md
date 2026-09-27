# METPO ROBOT Template Proposal - SNIPE System (v291, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v290 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for SNIPE system, the
genome-level possession trait for a membrane-localized phage-defense locus that
exploits the spatial organization of phage genome injection and directly
cleaves incoming phage DNA to block siphovirus infection. Saxton et al.
experimentally support SNIPE as an anti-bacteriophage defence system that
localizes to the bacterial cell membrane in Escherichia coli, directly cleaves
phage DNA during genome injection, and defends against diverse siphoviruses.
The pinned DefenseFinder article registry maps the SNIPE system name to that
article.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for SNIPE system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1036800` is reserved for this one-row class cohort. The v290 cohort used
`METPO:1036700`, so v291 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files outside
`.git` across the curation corpus. It found no exact same-scope SNIPE record,
`snipe_system` slug, Saxton et al. DOI, `traitmech:000414`,
`metpo_traitmech_v291`, or `METPO:1036800` / `METPO:10368xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1036800` | SNIPE system | `METPO:1016300` phage defense system |

SNIPE system captures genome-level possession of a membrane-localized
anti-bacteriophage locus that targets injected phage DNA. It excludes
individual `SNIPE` genes or proteins, host genome-entry proteins, phage tape
measure proteins, phage genome injection as a biological process, individual
Escherichia coli assay strains, source database rows naming one SNIPE system,
DefenseFinder model rows that are absent from the pinned HMM and rules files,
and other phage-defense systems.

`traitmech:000414` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`, as the closest proposed upstream ancestor.

## External Mappings

No exact external mapping is proposed. `SNIPE` is included as an exact synonym
because Saxton et al. use the token for the characterized anti-bacteriophage
defence system and the pinned DefenseFinder article registry uses the same
token as a system name.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with the
  SNIPE acronym as an exact synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000414` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000414` as traceability during the migration.

## Change Log

- v291, 2026-09: lifts `traitmech:000414 SNIPE system` into the
  `METPO:1036800` block.
