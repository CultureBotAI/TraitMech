# METPO ROBOT Template Proposal - Druantia System (v111, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v110 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Druantia system,
the genome-level possession trait for DruE-core antiphage defenses. The v86
cohort proposed a `phage defense system` parent, v87 through v110 proposed
BREX, DISARM, CBASS, phosphorothioate, abortive-infection, Gabija, Thoeris,
Zorya, Wadjet, Hachiman, Shedu, Dnd, Ssp, DndCDEA-PbeABCD, Kiwa,
abortive-infection-family, Lamassu, and Septu children, and this cohort adds
Druantia as another narrower phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000234` was minted locally because METPO has no active exact Druantia-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1018800` is reserved for this one-row class cohort. The v110 cohort used
`METPO:1018700`, so v111 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v111`, no live record used
`traitmech:000234`, and no prior proposal reserved `METPO:1018800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1018800` | Druantia system | `METPO:1016300` phage defense system |

Druantia system captures genome-level possession of a Druantia antiphage locus
built around a conserved DruE-family helicase-nuclease and subtype-specific
partner proteins, including the DruABCDE, DruMFGE, and DruHE architectures
described for Type I, Type II, and Type III loci. It excludes individual
`druE` or `druH` genes; DruE, DruH, or other Dru proteins; DUF1998-domain or
YprA-like SF2 helicase-nuclease activity without a Druantia locus;
Type III-specific DruH phage sensing; RecBCD-dependent DNA processing; Zorya II
synergy; source database rows naming one Druantia subtype; and other antiphage
systems such as BREX, DISARM, CBASS, Gabija, Hachiman, Shedu, Thoeris, Zorya,
Kiwa, Lamassu, Septu, phosphorothioate defense, CRISPR-Cas, and
abortive-infection families.

## External Mappings

No exact external mapping is proposed. Druantia gene, protein, protein-domain,
DNA-processing, PADLOC, and DefenseFinder records are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Druantia synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000234` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000234` as traceability during the migration.

## Change Log

- v111, 2026-09: lifts `traitmech:000234 Druantia system` into the
  `METPO:1018800` block.
