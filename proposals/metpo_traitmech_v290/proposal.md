# METPO ROBOT Template Proposal - Tab System (v290, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v289 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Tab system, the
genome-level possession trait for a prophage-associated phage-defense locus
that expresses Tab, blocks tail assembly by invading phages, prevents infectious
virion production, and protects the bacterial community from further phage
spread. Patel et al. experimentally support Tab as a Pseudomonas aeruginosa
prophage-encoded defence protein that interferes with the invading phage virion
assembly pathway, and the pinned DefenseFinder article registry maps the Tab
system name to that article.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Tab system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1036700` is reserved for this one-row class cohort. The v289 cohort used
`METPO:1036600`, so v290 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files outside
`.git` across the curation corpus. It found no exact same-scope Tab record,
`tab_system` slug, `Tail assembly blocker`, the Patel et al. DOI,
`traitmech:000413`, `metpo_traitmech_v290`, or `METPO:1036700` /
`METPO:10367xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1036700` | Tab system | `METPO:1016300` phage defense system |

Tab system captures genome-level possession of the prophage-associated Tab
defence locus. It excludes individual `tab` genes, Tab proteins, the Tab
counter-defence protein, phage tail proteins, phage virion assembly as a
biological process, individual Pseudomonas prophages, source database rows
naming one Tab system, DefenseFinder model rows that are absent from the pinned
HMM and rules files, and other phage-defense systems.

`traitmech:000413` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`, as the closest proposed upstream ancestor.

## External Mappings

No exact external mapping is proposed. `Tab` is included as a related synonym
because Patel et al. use the token for the characterized tail-assembly-blocking
protein and the pinned DefenseFinder article registry uses the same token as a
system name.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  Tab acronym as a related synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000413` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000413` as traceability during the migration.

## Change Log

- v290, 2026-09: lifts `traitmech:000413 Tab system` into the
  `METPO:1036700` block.
