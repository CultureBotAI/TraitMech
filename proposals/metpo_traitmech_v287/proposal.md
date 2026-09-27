# METPO ROBOT Template Proposal - Integrative Conjugative Element (v287, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v286 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for integrative conjugative
element, the genome-level possession trait for self-transmissible genomic
islands that integrate into host DNA, excise under induced expression, and
encode type IV secretion machinery for conjugative transfer to recipient cells.
Johnson and Grossman summarize the defining features and life cycle of ICEs,
and Bioteau et al. place integrative and conjugative elements among the
mobile-genetic-element subclasses encompassed by genomic islands.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for integrative conjugative element |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1036400` is reserved for this one-row class cohort. The v286 cohort used
`METPO:1036300`, so v287 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope integrative conjugative element
record, `integrative_conjugative_element` slug, `traitmech:000410`,
`metpo_traitmech_v287`, or `METPO:1036400` / `METPO:10364xx` proposal block.
The only `integrative_conjugative_element` live-data mention was an ungrounded
genomic-island causal node that this branch resolves by grounding to the new
local trait.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1036400` | integrative conjugative element | `METPO:1007688` mobile genetic element |

Integrative conjugative element captures genome-level possession of a bacterial
or archaeal self-transmissible genomic island that can excise, transfer by
conjugation, and integrate into recipient DNA. It excludes integrative and
mobilizable elements, Actinomycete ICEs with different transfer machinery,
conjugative plasmids, prophages, transposons, ICEfinder or AtollGenDB
classification rows, individual mobility or secretion proteins, and adaptive
cargo phenotypes such as phage defense or antibiotic resistance.

`traitmech:000410` is a direct local child of `traitmech:000093` genomic
island. The direct parent has no METPO placeholder yet, so this proposal uses
`METPO:1007688 mobile genetic element`, the v5 placeholder for
`traitmech:000089`, as the closest proposed upstream ancestor.

## External Mappings

No exact external mapping is proposed. `ICE` is included as a related synonym
because Johnson and Grossman explicitly expand the acronym, but a short acronym
should not be the primary exact label for this organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  ICE acronym as a related synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000410` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000410` as traceability during the migration.
4. Reparent integrative conjugative element below the assigned genomic-island
   METPO ID once `traitmech:000093` has also been lifted.

## Change Log

- v287, 2026-09: lifts `traitmech:000410 integrative conjugative element` into
  the `METPO:1036400` block.
