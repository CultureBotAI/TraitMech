# METPO ROBOT Template Proposal - Viperin System (v140, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v139 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Viperin system, the
genome-level possession trait for a prokaryotic viperin anti-phage locus.
Bernheim et al. showed that prokaryotic viperins produce antiviral modified
ribonucleotides, and DefenseFinder models Viperin with a required pVip profile
in its article registry, rules table, and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000263` was minted locally because METPO has no active exact Viperin-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1021700` is reserved for this one-row class cohort. The v139 cohort used
`METPO:1021600`, so v140 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v140`, no live record used
`traitmech:000263`, and no prior proposal reserved `METPO:1021700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1021700` | Viperin system | `METPO:1016300` phage defense system |

Viperin system captures genome-level possession of a prokaryotic viperin locus
represented by a pVip DefenseFinder profile. It excludes individual pVip genes;
prokaryotic or eukaryotic viperin proteins; radical-SAM enzymatic activities;
individual modified ribonucleotide products; DefenseFinder HMM profiles;
predicted source-database rows naming one Viperin locus; and other
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual pVip genes, pVip protein
profiles, DefenseFinder HMMs, and radical-SAM molecular functions are shifted
from this organism-level GENOMICS possession trait.

`Viperin` and `pVip` are proposed as related synonyms, not exact synonyms,
because both can denote the protein family or one protein rather than the
organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  related Viperin labels and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000263` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000263` as traceability during the migration.

## Change Log

- v140, 2026-09: lifts `traitmech:000263 Viperin system` into the
  `METPO:1021700` block.
