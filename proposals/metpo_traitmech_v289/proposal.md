# METPO ROBOT Template Proposal - TgvAB System (v289, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v288 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for TgvAB system, the
genome-level possession trait for a two-gene VPI-2
modification-dependent restriction locus encoding TgvA and TgvB
GmrSD-related type IV restriction proteins. Vizzarro et al. experimentally
support TgvAB as a system embedded in a Vibrio cholerae pathogenicity island 2
type I restriction-modification cluster that restricts hypermodified phage
genomes, Gomez and Waters independently support both TgvA and TgvB as required
for restriction of glucosylated 5-hydroxymethylcytosine-containing T-even
phages, and the pinned DefenseFinder article and HMM inventories name the
TgvAB system and its two component profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for TgvAB system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1036600` is reserved for this one-row class cohort. The v288 cohort used
`METPO:1036500`, so v289 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files outside
`.git` across the curation corpus. It found no exact same-scope TgvAB record,
`tgvab_system` slug, `TgvAB`, `TgvA`, `TgvB`, `VC1767`, `VC1766`, the
Vizzarro et al. DOI, `traitmech:000412`, `metpo_traitmech_v289`, or
`METPO:1036600` / `METPO:10366xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1036600` | TgvAB system | `METPO:1007694` restriction-modification system |

TgvAB system captures genome-level possession of a two-gene locus encoding
TgvA and TgvB modification-dependent restriction proteins. It excludes
individual `tgvA` or `tgvB` genes, individual TgvA or TgvB proteins, GmrSD
restriction enzymes outside a complete TgvAB system, glucosylated hmC or
T-even-like phage DNA substrate classes, VPI-2 as a whole pathogenicity island,
the adjacent type I R-M module, source database rows naming one TgvAB system,
individual DefenseFinder HMM profiles, the absent DefenseFinder rule-level
model, and neighboring phage-defense systems.

`traitmech:000412` is a direct local child of `traitmech:000095`
restriction-modification system. This proposal uses `METPO:1007694`, the v5
placeholder for `traitmech:000095`, as the closest proposed upstream ancestor.

## External Mappings

No exact external mapping is proposed. `TgvAB` is included as an exact synonym
because Vizzarro et al. use the token as the name of the two-gene
modification-dependent restriction system and the pinned DefenseFinder article
registry uses the same token as a system name.

The `TgvAB__TgvA` and `TgvAB__TgvB` profile names are included as related
synonyms for DefenseFinder searchability. The pinned HMM rows are not lifted as
TgvA- or TgvB-specific traits because the pinned rules table has no TgvAB row,
so the rows currently support named system possession only.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  TgvAB system synonym and DefenseFinder HMM profile related synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000412` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000412` as traceability during the migration.

## Change Log

- v289, 2026-09: lifts `traitmech:000412 TgvAB system` into the
  `METPO:1036600` block.
