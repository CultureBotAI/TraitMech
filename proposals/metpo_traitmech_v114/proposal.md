# METPO ROBOT Template Proposal - PARIS System (v114, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v113 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the PARIS system, the
genome-level possession trait for AriA/AriB abortive-infection systems that
sense phage anti-restriction or other foreign proteins. The v86 cohort
proposed a `phage defense system` parent, v91 proposed its `abortive infection
system` child, v102, v104-v107, and v110 proposed ToxIN, AbiQ, AbiE, AbiZ,
AbiK, and AbiT children, and this cohort adds PARIS as another narrower
abortive-infection-system child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000237` was minted locally because METPO has no active exact PARIS-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1019100` is reserved for this one-row class cohort. The v113 cohort used
`METPO:1019000`, so v114 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v114`, no live record used
`traitmech:000237`, and no prior proposal reserved `METPO:1019100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1019100` | PARIS system | `METPO:1016800` abortive infection system |

PARIS system captures genome-level possession of an AriA/AriB antiphage locus
that detects phage anti-restriction or other foreign proteins, releases AriB
TOPRIM-family nuclease activity, cleaves host lysine tRNA, and blocks phage
propagation through translational inhibition. It excludes individual `ariA` or
`ariB` genes; AriA or AriB proteins; AriA/AriB immune-complex assembly;
lysine-tRNA cleavage without a complete antiphage locus; phage Ocr, Ptr1,
Ptr2, or T5 tRNA anti-defense factors; source database rows naming one PARIS
locus; PARIS trigger-specific subtypes; and other abortive-infection systems
such as ToxIN, AbiQ, AbiE, AbiK, AbiT, and AbiZ.

## External Mappings

No exact external mapping is proposed. AriA, AriB, lysine tRNA, the T7 Ocr
trigger, the T5 Ptr1/Ptr2 triggers, the T5 tRNA suppressor, PADLOC, and
DefenseFinder records are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact PARIS long-form synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000237` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000237` as traceability during the migration.

## Change Log

- v114, 2026-09: lifts `traitmech:000237 PARIS system` into the
  `METPO:1019100` block.
