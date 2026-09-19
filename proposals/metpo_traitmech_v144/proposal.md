# METPO ROBOT Template Proposal - Toutatis System (v144, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v143 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Toutatis system, the
genome-level possession trait for a Toutatis anti-phage locus. Darracq et al.
reported novel antiphage functions encoded by sedentary chromosomal integron
cassettes, and DefenseFinder models Toutatis with TutA_VCA0446 and
TutB_VCA0447 profiles in its article registry and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000267` was minted locally because METPO has no active exact Toutatis-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1022100` is reserved for this one-row class cohort. The v143 cohort used
`METPO:1022000`, so v144 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v144`, no live record used
`traitmech:000267`, and no prior proposal reserved `METPO:1022100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1022100` | Toutatis system | `METPO:1016300` phage defense system |

Toutatis system captures genome-level possession of a Toutatis locus
represented by TutA_VCA0446 and TutB_VCA0447 DefenseFinder profiles. It
excludes individual TutA_VCA0446 or TutB_VCA0447 genes; TutA_VCA0446 or
TutB_VCA0447 proteins; DefenseFinder HMM profiles; predicted source-database
rows naming one Toutatis locus; unresolved Toutatis trigger or effector
activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual TutA_VCA0446 and
TutB_VCA0447 genes, the corresponding proteins, DefenseFinder HMMs, and
unresolved Toutatis molecular activities are shifted from this organism-level
GENOMICS possession trait.

`TutA_VCA0446` and `TutB_VCA0447` are proposed as related synonyms, not exact
synonyms, because they are source-profile labels for the component HMMs rather
than lexical names for the organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  related Toutatis source-profile labels and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000267` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000267` as traceability during the migration.

## Change Log

- v144, 2026-09: lifts `traitmech:000267 Toutatis system` into the
  `METPO:1022100` block.
