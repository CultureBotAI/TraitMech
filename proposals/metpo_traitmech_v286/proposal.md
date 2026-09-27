# METPO ROBOT Template Proposal - Gao-Her System (v286, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v285 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Gao-Her system, the
genome-level possession trait for the DefenseFinder `Gao_Her` family containing
`Gao_Her_DUF` and `Gao_Her_SIR` phage-defense loci. Gao et al. discovered
widespread antiviral gene cassettes with diverse enzymatic activities against
specific bacteriophages, and the pinned DefenseFinder commit maps the `Gao_Her`
family key to Gao et al. while modeling `Gao_Her_DUF` and `Gao_Her_SIR` as
two-profile subsystems.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Gao-Her system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1036300` is reserved for this one-row class cohort. The v285 cohort
used `METPO:1036200`, so v286 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Gao-Her system record,
`gao_her_system` slug, `traitmech:000409`, `metpo_traitmech_v286`, or
`METPO:1036300` / `METPO:10363xx` proposal block. The only `Gao_Her` mentions
were in the existing Gao-Her-DUF and Gao-Her-SIR child records, their generated
pages, their add-record scripts, their history records, and their proposal
cohorts as narrower subsystem or explicit broader-family-key text.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1036300` | Gao-Her system | `METPO:1016300` phage defense system |

Gao-Her system captures genome-level possession of a `Gao_Her` locus represented
by DefenseFinder as either a `Gao_Her_DUF` or `Gao_Her_SIR` two-profile
subsystem. It excludes the narrower Gao-Her-DUF and Gao-Her-SIR possession
traits, source database rows naming one subsystem, individual Gao-Her HMM
profiles, individual Gao-family genes or proteins, other Gao-family systems, and
other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The DefenseFinder `Gao_Her` family key,
the two subsystem labels, and the custom component profiles are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  DefenseFinder family key as a related synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000409` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000409` as traceability during the migration.
4. Reparent Gao-Her-DUF and Gao-Her-SIR below the assigned parent METPO ID once
   `METPO:1036300` is minted.

## Change Log

- v286, 2026-09: lifts `traitmech:000409 Gao-Her system` into the
  `METPO:1036300` block.
