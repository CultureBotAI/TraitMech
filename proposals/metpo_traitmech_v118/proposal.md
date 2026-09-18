# METPO ROBOT Template Proposal - Hna System (v118, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v117 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Hna system, the
genome-level possession trait for single-effector Hna helicase/nuclease
antiphage loci. Sather et al. showed that an Hna protein protects
*Sinorhizobium meliloti* against diverse phages by triggering abortive
infection, and Hooper et al. connected phage-encoded single-stranded
DNA-binding protein stimulation to dysregulated Hna nuclease activation.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000241` was minted locally because METPO has no active exact Hna-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1019500` is reserved for this one-row class cohort. The v117 cohort used
`METPO:1019400`, so v118 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v118`, no live record used
`traitmech:000241`, and no prior proposal reserved `METPO:1019500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1019500` | Hna system | `METPO:1016300` phage defense system |

Hna system captures genome-level possession of a single-effector locus encoding
an Hna SF2 helicase/nuclease that can respond to phage single-stranded
DNA-binding protein challenge by activating nuclease-associated abortive
infection. It excludes individual `hna` genes; standalone SF2 helicase,
PD-(D/E)XK nuclease, and DinG-like protein families; Hna enzymatic
subactivities without a complete antiphage locus; phage single-stranded
DNA-binding proteins; Hna-triggering or Hna-escaping phage proteins;
DefenseFinder/PADLOC rows naming one predicted locus; source rows naming
helicase/nuclease proteins; and other antiphage systems such as Shedu,
Hachiman, SPARTA, AVAST, PARIS, RADAR, Pycsar, Retron, Septu, BREX, DISARM,
CBASS, Gabija, Zorya, phosphorothioate defense, CRISPR-Cas, and abortive
infection families.

## External Mappings

No exact external mapping is proposed. Hna proteins, SF2 helicases, PD-(D/E)XK
nucleases, phage single-stranded DNA-binding proteins, abortive-infection cell
death, nuclease activation, and locus prediction rows are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Hna long-form synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000241` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000241` as traceability during the migration.

## Change Log

- v118, 2026-09: lifts `traitmech:000241 Hna system` into the
  `METPO:1019500` block.
